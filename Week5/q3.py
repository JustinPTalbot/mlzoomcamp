import pickle

def load(filename):
    with open(filename, 'rb') as file_in:
        return pickle.load(file_in)

dv = load('dv.bin')
model = load('model1.bin')

client = {
    "job": "retired",
    "duration": 445,
    "poutcome": "success"
    }

X = dv.transform(client)
y_pred = model.predict_proba(X)[0, 1]

print(y_pred)
