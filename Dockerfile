FROM python:3.8.12-slim
RUN pip install pipenv
WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --deploy --system
COPY ["*.py", "model_logistic.bin", "./"]
EXPOSE 8181
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8181", "predict:app"]