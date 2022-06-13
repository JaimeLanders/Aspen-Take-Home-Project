docker build -t aspen-nginx .

docker tag aspen-nginx:latest jaimelanders/aspen-nginx:latest

docker push jaimelanders/aspen-nginx:latest
