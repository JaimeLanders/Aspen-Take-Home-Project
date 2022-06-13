# Aspen Take Home Project 
This project is for implementing the Aspen Capital take home project defined [here](https://github.com/aspencapital/candidate-project-sre]).


## Project Overview
This project uses AWS' Cloud Development Kit (cdk) implemented in Python to provision a single EC2 instance with the following architecture: 

![architecture](./public/img/test-sre.png)


## Implementation Explaination 
Due to the requirements of a single nginx reverse proxy forwarding to two instances of the application, EC2 seems like the best choice for this implementation.  If we needed multiple instances with each having their own reverse proxy, an ECS with a sidecar implementation would have been a better choice. ECS excells in providing it's own load balancing with multiple instances of the same container (app in this case), so NGINX would have been redundant and the sidecar implementation would not have fit the requirements.  

Other alternatives considered were using fargate as well as other serverless containerization services. Ultimately, EC2 felt the most appropriate given the requirements and budget constraints as part of this excersize was to utilize the free tier as much as possible to show ability to anaylyze and stay within a budget.  


## Languages and Tools:
The provided app was written in express node.js while the cdk deployment was implemented in python.  I chose to use docker containers for each of the apps and the NGINX instance in order to simplify orchestration using docker compose.  Shell scripts were also used extensively to help with provisioning the deployed system, as well as starting the express app (and keeping the container running), building and deploying the docker images. 