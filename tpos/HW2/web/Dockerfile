FROM ubuntu:latest

WORKDIR /srv/

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip vim
RUN pip3 install flask requests

# ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["python3", "/srv/app.py"]