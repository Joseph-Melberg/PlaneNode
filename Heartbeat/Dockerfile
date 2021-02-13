From balenalib/raspberry-pi-debian:latest
RUN apt-get update && apt-get install -y python3 python3-pip crontab
RUN pip3 install pika
COPY Heart.py Heart.py
COPY cronfile cronfile
RUN crontab < cronfile
