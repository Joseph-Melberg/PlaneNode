From balenalib/raspberry-pi-debian:latest
RUN apt-get update && apt-get install -y socat
COPY airplaneConnect.bash run.bash
ENTRYPOINT bash run.bash
#ENTRYPOINT socat -u TCP:0.0.0.0:30005 TCP:centurionx.net:30004
#CMD ["socat","-u", "TCP:0.0.0.0:30005" ,"TCP:centurionx.net:30004"]
