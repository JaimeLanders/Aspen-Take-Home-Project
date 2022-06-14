#!/bin/bash

# helper script for tearing down the cluster and cleaning up containers/images on the system

# tear down the cluster
sudo docker-compose down

# remove all containers, images and networks (requires confirmation) 
sudo docker system prune -a