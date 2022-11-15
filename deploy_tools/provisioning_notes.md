Provisioning a new site
=======================

## Required Packages
* nginx
* Python 3.10
* virtualenv + pip
* Git

eg, on Ubuntu:
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python3 python3-venv

## Nginx Virtual Host Config
* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service
* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder Structure:

Assume we have a user account at /home/username

/home/username
|___ sites
     |___ DOMAIN1
     |    |__ .env
     |    |__ db.sqlite3
     |    |__ manage.py etc
     |    |__ static
     |    |__ virtualenv
     |
     |_____DOMAIN2
           |__ .env
           |__ db.sqlite3
           |___etc
