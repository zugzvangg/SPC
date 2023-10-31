FROM ubuntu:latest

WORKDIR /srv/

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip libmariadb-dev
RUN pip3 install flask requests mariadb

# ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["flask", "--app", "web", "run", "--port=8000", "--debug"]
