FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["q6_app.py", "./"]

EXPOSE 1616

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:1616", "q6_app:app"]