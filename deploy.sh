# populate config.ini

git pull origin master

pip install -r requirements.txt

# edit systemd service with proper path for Gunicorn
# server will run locally at localhost:5000
sudo cp code-cluster.service /etc/systemd/system/

sudo systemctl daemon-reload

sudo systemctl start code-cluster

sudo systemctl restart code-cluster
