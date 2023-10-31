FROM ubuntu:latest

ENV $(cat .env | grep -v ^# | xargs)

WORKDIR /srv/

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip libmariadb-dev vim
RUN pip3 install mariadb pandas

# ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["python3", "/srv/fill.py"]


