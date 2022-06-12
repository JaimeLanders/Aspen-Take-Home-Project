#!/bin/sh

[ ! -f ./.env ]
then
    touch ./.env
fi

npm start

while true
do
    sleep 1
done
