#!/bin/sh

# Install Heroku toolbelt
utils/install.sh

# Update apt-get
sudo apt-get update

# Install necessary C libraries, if needed
sudo apt-get install libevent-dev -y
sudo apt-get install libpq-dev -y
sudo apt-get install libmemcached-dev -y
sudo apt-get install zlib1g-dev -y
sudo apt-get install libssl-dev -y
sudo apt-get install python-dev -y 
sudo apt-get install build-essential -y

# Install PostgreSQL
sudo apt-get install postgresql-client -y

# Install Git
sudo apt-get install git -y

# Install Pip
sudo apt-get install python-pip -y

# Install Django
sudo pip install django