# Clone the project repository for access to scripts
git clone --branch main https://github.com/JaimeLanders/Aspen-Take-Home-Project.git /home/ubuntu/Aspen-Take-Home-Project

# Make sure all scripts are executable
chmod +700 -R /home/ubuntu/Aspen-Take-Home-Project

# Install dependencies for app and nginx
/home/ubuntu/Aspen-Take-Home-Project/install.sh

# Build and deploy using docker-compose
/home/ubuntu/Aspen-Take-Home-Project/start.sh