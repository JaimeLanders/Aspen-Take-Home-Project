# NGINX 
This project is for implementing the NGINX load balancer 


## Project Overview
This project uses AWS' Cloud Development Kit (cdk) implemented in Python to provision a single EC2 instance with the following architecture: 


## Implementation Explaination 
Due to the requirements of a single nginx reverse proxy forwarding to two instances of the application, EC2 seems like the best choice for this implementation.  If we needed multiple instances with each having their own reverse proxy, an ECS with a sidecar implementation would have been a better choice. ECS excells in providing it's own load balancing with multiple instances of the same container (app in this case), so NGINX would have been redundant and the sidecar implementation would not have fit the requirements.  

Other alternatives considered were using fargate as well as other serverless containerization services. Ultimately, EC2 felt the most appropriate given the requirements and budget constraints as part of this excersize was to utilize the free tier as much as possible to show ability to anaylyze and stay within a budget.  


## Languages and Tools:
The provided app was written in express node.js while the CDK deployment was implemented in python.  I chose to use docker containers for each of the apps and the NGINX instance in order to simplify orchestration using docker compose.  Shell scripts were also used extensively to help with provisioning the deployed system, as well as starting the express app (and keeping the container running), building and deploying the docker images. 

# Pre-Requisites: 
1. If you want to run the project locally, make sure you have docker and docker-compose installed


# Getting Started:
This module should be built and deployed 
The general workflow for building and deploying the application:

1. Clone the project into desired location

```git clone https://github.com/JaimeLanders/Aspen-Take-Home-Project.git .```

2. Create .env in the cdk subfolder (.env_example provided for ease) to customize the deployment  

3. Deploy the application to the desired account and region

Visit the [cdk](https://github.com/JaimeLanders/Aspen-Take-Home-Project/tree/main/cdk) [app](https://github.com/JaimeLanders/Aspen-Take-Home-Project/tree/main/app), [nginx](https://github.com/JaimeLanders/Aspen-Take-Home-Project/tree/main/nginx) and project subfolders for more details and instructions.  