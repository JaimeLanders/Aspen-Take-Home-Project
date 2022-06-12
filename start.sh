#!/bin/bash

sudo docker network create -d bridge aspen

sudo docker-compose -f ~/Aspen-Take-Home-Project/docker-compose.yml scale app=2 nginx=1