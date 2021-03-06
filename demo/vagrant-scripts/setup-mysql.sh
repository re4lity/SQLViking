#!/bin/bash

sudo apt-get install git -y
sudo apt-get install unzip -y
sudo apt-get install debconf-utils -y
echo "mysql-server-5.5 mysql-server/root_password password toor" | sudo debconf-set-selections
echo "mysql-server-5.5 mysql-server/root_password_again password toor" | sudo debconf-set-selections
sudo apt-get install mysql-server-5.5 -y
cp -f /vagrant/vagrant-scripts/config/my.cnf /etc/mysql/my.cnf
mysql -u root --password=toor -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'toor'"
sudo service mysql restart
mkdir /opt/sql/
cp -R /vagrant/* /opt/sql/

