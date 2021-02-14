From balenalib/raspberry-pi-debian:latest
RUN apt-get update &&  install_packages python3 python3-pip
RUN pip3 install pika
COPY Heart.py Heart.py
ENTRYPOINT python3 /Heart.py
