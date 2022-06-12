#!/bin/bash

sudo docker network create -d bridge aspen

sudo docker-compose scale app=2 nginx=1