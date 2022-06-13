# pull the Node.js Docker image
FROM alpine

# create the directory inside the container
WORKDIR /usr/src/app

# copy the package.json files from local machine to the workdir in container
COPY package*.json ./

# copy start shell script to keep docker container running
COPY start.sh ./

# install npm 
RUN apk add --update npm

# run npm install in our local machine
RUN npm install

# copy the generated modules and all other files to the container
COPY . .

# our app is running on port 3000 within the container, so need to expose it
EXPOSE 3000

# the command that starts our app
CMD ["./start.sh"]
