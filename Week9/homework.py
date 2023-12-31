import tensorflow as tf
from tensorflow import keras
from io import BytesIO
from urllib import request
from PIL import Image
import tensorflow.lite as tflite
import numpy as np
import os

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def prepare_input(img):
    return img / 255.0

#MODEL_NAME = os.getenv('MODEL_NAME', 'bees-vs-wasps.tflite')
#interpreter = tflite.Interpreter(model_path=MODEL_NAME)


interpreter = tflite.Interpreter(model_path='C:/Users/justin.talbot/Documents/Git/mlzoomcamp/Week9/bees-vs-wasps.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

def predict(url):
    img = download_image(url)
    img = prepare_image(img, target_size=(150, 150))

    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = prepare_input(X)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()

    preds = interpreter.get_tensor(output_index)

    return float(preds[0, 0])

def lambda_handler(event, context):
    url = event['url']
    pred = predict(url)
    result = {
        'prediction': pred
    }

    return result
