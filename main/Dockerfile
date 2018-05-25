FROM python:3.6-slim

MAINTAINER SayfEddine "sayf.piratos@gmail.com"

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends build-essential git-core openssl libssl-dev libffi6 libffi-dev curl  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


COPY ./requirements-main.txt  /app/requirements-main.txt

WORKDIR /app

RUN pip install -r requirements-main.txt

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends wget \
    && wget -P data/mitie/ https://s3-eu-west-1.amazonaws.com/mitie/total_word_feature_extractor.dat \
    && apt-get remove -y wget \
    && apt-get autoremove -y


COPY . /app

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["chatapp.py"]
