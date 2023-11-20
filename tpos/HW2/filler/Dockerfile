FROM ubuntu:latest

ENV $(cat .env | grep -v ^# | xargs)

WORKDIR /srv/

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    pip3 install pandas pymysql

ENTRYPOINT ["python3", "/srv/fill.py"]


