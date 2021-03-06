# CDK 
This project is for implementing the AWS Cloud Development Kit (CDK) pipeline for deploying the application. 


## Project Overview
This project uses the CDK implemented in python to provision an EC2 instance and then deploy and run the NGINX and express apps.  It uses user data to clone this repo and run an ```install.sh``` helper script for installing all requisite packages.  Next, it runs the ```start.sh``` script in the parent project folder to run the docker commands for pulling the images and then running the containers.  Once set up with the pre-requisites below, the user should only need to run the ```cdk deploy``` command and after about 5 minutes, the application should be running on AWS.  


## Pre-Requisites 
1. Make sure you have [aws-cli](https://aws.amazon.com/cli/) installed and configured before using CDK to deploy the project.  If you want to use a separate account and region you may set the variables in .env in the cdk project subfolder. See [this](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) for more information. 

2. Make sure you have python3 and venv installed for use with the cdk.

3. If you want to run CDK in the provided docker container, make sure you have Docker installed


## Getting Started in Docker 
The option is provided to build and run this project in a Docker container to make it easy to get going and isolate the environment from existing installations.

1. Build the Docker image: 

```bash
docker build -t cdk ./
```

2. Run the docker container in interactive tty mode to issue commands in CDK usage:

```bash
docker run -it cdk bash 
```

**Note:** I didn't use the --rm option to keep this container available for future use.  Otherwise, these steps need to be repeated.

3. Configure the aws cli using the account name, region, and access key pair.

```bash
aws configure 
```

4. Copy example .env and set environment variables:

```bash
cp ./.env-example ./.env 
vi .env
```


Now you can proceed to CDK usage below.


## Getting Started in Python Virtual Environment
This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.


```bash
python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```bash
source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```bash
.venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```bash
pip install -r requirements.txt
```

Copy example .env and set environment variables:

```bash
cp ./.env-example ./.env 
vim .env
```

Now you can proceed to CDK usage below.


## CDK Usage

At this point, you can now synthesize the CloudFormation template for this code.

```bash
cdk synth
```

To deploy the stack to AWS, bootstrap before the first run and then deploy:

```bash
cdk boostrap
```

```bash
cdk deploy 
```

To tear down the stack (delete the EC2 instance, etc.)

```bash
cdk destroy <optional stack name>
```

**Note:** Sometimes the destroy command does not work, at which point the user can delete the stack for  AWS consoles CloudFormation section. 

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!



