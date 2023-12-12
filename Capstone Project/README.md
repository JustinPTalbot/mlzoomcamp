# Electric Vehical Regression Model w/ Heroku Cloud Deployment
## mlzoomcamp midtern project

### Dataset
[Electric Vehicle Specifications and Prices](https://www.kaggle.com/datasets/fatihilhan/electric-vehicle-specifications-and-prices/)

I've also committed the dataset to this repo, see EV_cars.csv

This dataset has various metrics about various electric vehicles including their price which we will use as the target variable.

The models purpose is to predict the price of a new EV given various datapoints about it.

### EDA and Model Evaluation
Please see *notebook.ipynb* for the jupyter notebook containing EDA and model evalutation.
- EDA
  - Cleaned column names
  - Dropped rows w/ null values
  - Checked min and max values of each feature
  - Inspected correlation matrix
  - Inspected histograms for each variable
- Model Selection
  - Prepped features using DictVectorizer
  - Trained KNN regressor model using mean squared error as the score
  - Tested various n_neighbors values
  - Prepped features into DMatrix for use in xgboost model
  - Trained xgboost regression model using mean squared error as the score
  - Selected xgboost model to move forward with
- Hyperparameter Tuning and Model Eval
  - Decided on most efficient number of boost rounds
  - Tested different eta
  - Tested different max_depth
  - Tested different min_child_weight
 
### Training the Final Model
The file *train.py* trains the xgboost model and exports the model as *model.pkl*
```
python train.py
```

### Local Docker Deployment
I used pipenv to lock dependencies which are stored in the Pipfile and Pipfile.lock. The model can be deployed locally using docker. With docker installed and running on your system, first build the image:
```
docker build -t fetal_health .
```
Next, you can run the container locally:
```
docker run -it -p 1616:1616 fetal_health:latest
```
### Local Testing
With the container running locally, we can now test it. I've prepared a python script *predict_test_local.py* with some data and code to send a POST request to the endpoint via port 1616 and receieve a prediction about the price of the car. You can run the file with: 
```
python predict_test_local.py
```
The expected result in this case is *{'price': 59874.14}*

### Cloud Deployment
I've used a PaaS called Heroku to deploy my app  to the cloud. I connected my Heroku account to a dedicated github repo for this project and wrote a simple Procfile to enable me to deploy the app.
The url it is hosted at is:
```
https://evprice-1ba58eb40b90.herokuapp.com
```
Please note that I did not build a front end so nothing renders on that page.
In order to get a predicted value from the service, you must use the predict endpoint:
```
https://evprice-1ba58eb40b90.herokuapp.com/predict
```
I've preparred a python script *predict_test_heroku.py* that lets you send a POST request to the heroku app and see the predicted value.

