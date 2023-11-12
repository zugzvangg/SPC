FROM ubuntu:latest

ENV $(cat .env | grep -v ^# | xargs)

WORKDIR /srv/

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip libmariadb-dev && \
    pip3 install mariadb pandas

# ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["python3", "/srv/fill.py"]


