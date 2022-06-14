# import alpline
FROM alpine

# pull the apline container image 
WORKDIR /root

# install python, pip, aws-cli and aws-cdk
RUN apk add --no-cache python3 py3-pip nodejs npm
RUN apk add --no-cache aws-cli
RUN npm install -g aws-cdk

# add cdk project files
ADD ./ ./

# install project dependencies
RUN pip install -r requirements.txt