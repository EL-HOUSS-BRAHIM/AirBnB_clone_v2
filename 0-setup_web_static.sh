#!/usr/bin/env bash
#create and deploy test hbnb files
sudo apt update -y
sudo apt install nginx -y
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared/
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
