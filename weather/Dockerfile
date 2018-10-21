FROM python:alpine3.7

MAINTAINER SayfEddine "sayf.piratos@gmail.com"

COPY ./requirements-weather.txt  /app/requirements-weather.txt

WORKDIR /app

RUN pip install -r requirements-weather.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["weather_app.py"]
