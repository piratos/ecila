FROM python:alpine3.7

MAINTAINER SayfEddine "sayf.piratos@gmail.com"

COPY ./requirements-web.txt  /app/requirements-web.txt

WORKDIR /app

RUN pip install -r requirements-web.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["server.py"]
