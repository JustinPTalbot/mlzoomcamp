import requests

url = 'http://localhost:1616/predict'

client = {"job": "unknown", "duration": 270, "poutcome": "failure"}

result = requests.post(url, json=client).json()

print(result)