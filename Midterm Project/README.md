# Fetal Health Classification
## mlzoomcamp midtern project

### Dataset
[Fetal Health Classification](https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification)

The data is committed in this repo as fetal_health.csv

This dataset contains information about fetal health that was gathered from Cardiotocograms (CTGs). Fetal Health is classified as 1 - Normal, 2- Suspect, 3 - Pathological. For simplicity, I've reduced this to a binary classification model to predict health as normal or abnormal.

The model's purpose is to intepret the complicated information output by CTGs and use it to determine if the health of the fetus appears abnormal and a docter will need to investigate and treat the issue. This can help prevent child and maternal mortality.

### EDA and Model Evaluation
Please see *notebook.ipynb* for the jupyter notebook containing EDA and model evalutation.
- EDA
  - Checked for nulls
  - Cleaned column names
  - Checked for features w/ weak correlation to the target; dropped them from the training data
  - Checked for features w/ strong correlation to the target
  - Simplified multiclass target variable to binary
- Model Selection
  - Prepped features using DictVectorizer
  - Trained decision tree model on various depths, checked auc using validation data
  - Prepped features into DMatrix for use in xgboost model
  - Trained xgboost classification model
  - Selected xgboost model to move forward with
- Hyperparameter Tuning and Model Eval
  - Selected num_boost_round based
  - Tested different eta
  - Tested different max_depth
  - Tested different min_child_weight
 
### Training the Final Model
The file *train.py* trains the xgboost model and exports the model as *model.pkl*
```
python train.py
```

### Model Deployment
I used pipenv to lock dependencies which are stored in the Pipfile and Pipfile.lock. The model can be deployed locally using docker. With docker installed and running on your system, first build the image:
```
docker build -t fetal_health .
```
Next, you can run the container locally:
```
docker run -it -p 1616:1616 fetal_health:latest
```
### Testing The Web Service
With the container running locally, we can now test it. I've prepared a python script *predict_test.py* with some data and code to send a POST request to the endpoint via port 1616 and receieve a prediction about the health of the fetus. You can run the file with: 
```
python predict_test.py
```
The expected result in this case is *{'health': 'Normal'}*
