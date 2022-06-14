# App 
This project is for implementing simple the node.js express application. 


## Project Overview
This project uses docker to containerize the node.js express app. It exposes port 3000 to be forwarded from the NGINX reverse proxy.  It uses the predefined network setup for the cluster to make sure that the three containers can communicate with each other.    


## Configuration
The following characteristics are configurable in the application through
environment variables. Create a `.env` file to control the configuration.

**IMPORTANT**: You MUST provide a `.env` file even if you do not override any of the default configuration values. 

|Variable|Required|Default|Description|
|---|:-:|---|---|
|MESSAGE|F|"Hello world!"|Friendly message|
|PORT|F|3000|Server port|

**Note:** A blank template .env is included for the docker container, if you modify this then you must rebuild the docker image. 

## Pre-Requisites 
- If you want to run the project locally, make sure you have docker and docker-compose installed.


## Getting Started
This module should be built and deployed using docker-compose in the parent project subfolder.  However, the container can be run by itself as well as described below. 

1. Clone the project into the desired location if you haven't already:

    ```bash
    git clone https://github.com/JaimeLanders/Aspen-Take-Home-Project.git
    ```

2. In the nginix subfolder, build  docker container:
   
   ```bash
   docker build -t app ./
   ```
3. Run in interactive terminal mode to run the commands in usage manually:

   ```bash 
   docker run -it --rm -p 3000:3000 app bash 
   ```
    Or detatched mode to let it run automatically:
   ```bash
   docker run -d --rm -p 3000:3000 app 
   ```

## Usage

**Note:** the docker container includes a bash script (```start.sh```) to run the the npm start command and keep the container from exiting.  However, you can also run the container in interactive mode as shown above and issue the commands below manually. 

### Run
Launch the server. The npm package `forever` keeps the process alive.

```bash
npm start
```

### Status
The npm status script uses the `forever` package's `list` command to retrieve the status of the app.

```bash
npm run status
```

### Stop
Then npm stop script uses the `forever` package's `stopall` command can be used to stop the app.

```bash
npm run stop
```

### Test
Test the server.

```bash
npm test
```
