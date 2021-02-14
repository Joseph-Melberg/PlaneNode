From balenalib/raspberry-pi-debian:latest
RUN apt-get update &&  install_packages python3 python3-pip cron
RUN pip3 install pika
COPY Heart.py Heart.py
COPY cronfile cronfile
RUN crontab < cronfile
ENTRYPOINT bash sleep 1000
