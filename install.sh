#!/bin/bash

# install script for installing dependencies on freshly provisioned instance

# update the system prior to install packages
sudo apt-get -y update

# install docker dependencies 
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# prepare folder for keyrings 
sudo mkdir -p /etc/apt/keyrings

# install ubuntu and docker gpg keys 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# download and install docker 
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
            $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# install docker compose 
sudo apt install -y docker-compose