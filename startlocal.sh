#!/bin/bash

# helper script for building and deploying the cluster locally

# create the network used for the app and nginx containers 
sudo docker network create -d bridge aspen

# build and deploy two app and a nginix container 
sudo docker-compose scale app=2 nginx=1
