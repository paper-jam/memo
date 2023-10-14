# pour Debian BUSTER - version 10

# import the MongoDB public GPG Key
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -

# en cas d'erreur
# sudo apt-get install gnupg
# puis relancer la commande

#
echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org

# empêche l'upgrade automatique des packages suivants
echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-org-shell hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections


# data files in /var/lib/mongodb
# log files in /var/log/mongodb

# to start
sudo service mongod status  # to start
sudo service mongod status  # to check
sudo service mongod stop    # to stop
sudo service mongod restart # to restart

# mongo shell
mongo

# start and automatic start (default port : 27017)
sudo systemctl start mongod
sudo systemctl enable mongod




