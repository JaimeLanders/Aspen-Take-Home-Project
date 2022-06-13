#!/bing/bash

# helper script for building and deploying the nginx image

# build the docker image
docker build -t aspen-nginx .

# tag the docker image
docker tag aspen-nginx:latest jaimelanders/aspen-nginx:latest

# deploy the docker image
docker push jaimelanders/aspen-nginx:latest
