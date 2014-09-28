WorstBandEver
=============

Website for comparing bands with information pulled from Last.fm using MongoDB, Nginx, Gunicorn and Flask.

Installation
------------

The following assumes Ubuntu 14.04 64-bit

### Install pip

```
sudo apt-get install -U python-pip
```

### Setup Virtualenv

```
sudo pip install virtualenv
virtualenv virtualenv
source virtualenv/bin/activate
```

### Install script requirements

```
sudo pip install -r requirements.txt
```

### Install MongoDB and Nginx

```
sudo apt-get install mongodb
```

### Register for API Keys and Generate Random String for Flask

Sign up at [Twitter](https://dev.twitter.com) and [Last.fm](http://www.last.fm/api)


Rename keys_example.py to keys.py and insert your API keys into the file


Generate a random string for Flask and include in keys.py

### Configuring Nginx

See [Configuring Nginx](https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-apps-using-gunicorn-http-server-behind-nginx) in Digital Oceans "How to Deploy Python WSGI Apps Using Gunicorn HTTP Server Behind Nginx"

### Populate the Artist Database

Run getartists.py to populate the database. 


This script pulls the information from Last.fm and creates and populates the database in MongoDB

### Start the Site

```
gunicorn -b 127.0.0.1:8080 -w=3 worstband:app &
sudo service nginx start
python worstbandever.py &
```
