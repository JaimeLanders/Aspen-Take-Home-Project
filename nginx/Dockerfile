# dockerfile for building the nginx image 

# pull the nginx Docker image
FROM nginx

# copy the default nginx conf file 
COPY default.conf /etc/nginx/conf.d/default.conf

# copy the ssl certificates for https 
RUN mkdir -p /etc/nginx/certs
COPY ./certs/crt.crt /etc/nginx/certs/
COPY ./certs/crt.key /etc/nginx/certs/
