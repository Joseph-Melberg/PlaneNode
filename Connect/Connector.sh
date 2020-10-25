docker stop connect
docker rm connect
sudo docker run -d --name=connect --restart=unless-stopped --net=container:airrun airconnect:latest
