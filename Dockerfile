FROM python:3.12

WORKDIR /tasknado_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080" ]