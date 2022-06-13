#!/bing/bash

# helper script for building and deploying the express app image

# build the docker image
docker build -t aspen-app .

# tag the docker image
docker tag aspen-app:latest jaimelanders/aspen-app:latest

# deploy the docker image
docker push jaimelanders/aspen-app:latest
