FROM ubuntu:latest

ENV $(cat .env | grep -v ^# | xargs)

WORKDIR /srv/
EXPOSE 8000

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    pip3 install flask pymysql

ENTRYPOINT ["flask", "--app", "web", "run", "--port=8000", "--debug", "--host=0.0.0.0"]
