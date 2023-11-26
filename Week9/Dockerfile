FROM agrigorev/zoomcamp-bees-wasps:v2

RUN pip install keras-image-helper

COPY homework.py .
ENV MODEL_NAME=bees-vs-wasps-v2.tflite

CMD [ "homework.lambda_handler"]