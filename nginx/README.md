# NGINX 
This project is for implementing the NGINX reverse proxy load balancer. 


## Project Overview
This project uses docker to containerize the NGINX reverse proxy load balancer. It exposes ports 80 and 443 (for https) and forwards to each of the apps port 3000.  It uses the predefined network setup for the cluster to make sure that the three containers can communicate with each other.    


## Pre-Requisites 
- If you want to run the project locally, make sure you have docker and docker-compose installed.


## Getting Started
This module should be built and deployed using docker-compose in the parent project subfolder.  However, the container can be run by itself as well as described below. 

1. Clone the project into the desired location if you haven't already

    ```bash
    git clone https://github.com/JaimeLanders/Aspen-Take-Home-Project.git
    ```

2. In the nginix subfolder, build  docker container:
   
   ```bash
   docker build -t nginx ./
   ```
3. Run in interactive terminal mode:

   ```bash 
   docker run -it --rm -p 80:80 nginx  
   ```

    Or detatched mode:

   ```bash
   docker run -d --rm -p 80:80 nginx  
   ```
