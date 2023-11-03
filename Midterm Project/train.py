import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.feature_extraction import DictVectorizer
import pickle

def ingest_csv():
    df = pd.read_csv('fetal_health.csv')
    return df

def data_prep(df):
    # let's simplify this into a binary classification problem and remap healthy to 0 and unhealthy codes to 1
    fetal_health_dict = {
        1: 0, # normal
        2: 1, # abnormal
        3: 1, # abnormal
    }
    df.fetal_health = df.fetal_health.map(fetal_health_dict)

    # and drop the features w/ particularly low corr
    df.drop(['histogram_number_of_peaks','histogram_number_of_zeroes'], axis = 1, inplace = True)

    # dropping target variable
    y = df.fetal_health
    del df['fetal_health']

    # vectorizing data
    dv = DictVectorizer(sparse=False)
    data_dict = df.to_dict(orient='records')
    data = dv.fit_transform(data_dict)

    # converting to DMatrix
    features = dv.feature_names_
    DMatrix = xgb.DMatrix(data, label = y, feature_names = features)
    return DMatrix, dv

def train_xgboost(DMatrix):
    xgb_params = {
    'eta': .3,
    'max_depth': 6,
    'min_child_weight': 1,

    'objective': 'binary:logistic',
    'nthread': 8,
    'eval_metric':'auc',

    'seed': 1,
    'verbosity': 1,
    }

    model_final = xgb.train(xgb_params, DMatrix, num_boost_round=40)
    return model_final

if __name__ == "__main__":
    df = ingest_csv()
    DMatrix, dv = data_prep(df)
    model = train_xgboost(DMatrix)

    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open("dv.pkl", "wb") as f:
        pickle.dump(dv, f)
