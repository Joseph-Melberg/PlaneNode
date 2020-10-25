From balenalib/raspberry-pi-debian:latest
RUN apt-get update && apt-get install -y dump1090-mutability
EXPOSE 30005
ENTRYPOINT dump1090-mutability --net --interactive --net-bind-address 0.0.0.0
