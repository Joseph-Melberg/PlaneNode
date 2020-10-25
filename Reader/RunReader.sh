docker stop airrun
docker rm airrun
docker run -d -p 30005:30005 --restart=unless-stopped --privileged -v /dev/bus/usb:/dev/bus/usb --name airrun airrun

