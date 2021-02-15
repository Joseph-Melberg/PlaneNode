#!/bin/bash
if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo:"
    echo "sudo $0 $*"
    exit 1
fi


echo "What is the name of this node?"
read name
rm environ.env
touch environ.env
echo -n NAME=$name >> environ.env 
curl -sSL https://get.docker.com | sh
sudo apt-get install -y libffi-dev libssl-dev
sudo apt-get install -y python3 python3-pip
sudo apt-get remove python-configparser
sudo pip3 -v install docker-compose

