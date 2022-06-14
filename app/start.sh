#!/bin/sh

# helper script for starting the express server on the docker container and keeping it from exiting

# create .env on the container if it doesn't exit
[ ! -f ./.env ]
    touch ./.env

# stat the express server
npm start

# prevent the container for exiting
while true; do
    sleep 1
done
