docker build -t aspen-app .

docker tag aspen-app:latest jaimelanders/aspen-app:latest

docker push jaimelanders/aspen-app:latest
