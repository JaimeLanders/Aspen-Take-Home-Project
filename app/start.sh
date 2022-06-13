#!/bin/sh

[ ! -f ./.env ]
    touch ./.env

npm start

while true; do
    sleep 1
done
