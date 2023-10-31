FROM ubuntu:latest

WORKDIR /srv/
EXPOSE 8000

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip libmariadb-dev
RUN pip3 install flask mariadb requests

# ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["flask", "--app", "web", "run", "--port=8000", "--debug", "--host=0.0.0.0"]
