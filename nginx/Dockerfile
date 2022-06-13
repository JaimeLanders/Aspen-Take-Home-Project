FROM nginx

COPY default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /etc/nginx/certs

COPY ./certs/crt.crt /etc/nginx/certs/
COPY ./certs/crt.key /etc/nginx/certs/
