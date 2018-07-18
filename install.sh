#!/bin/bash
# Install the application in PythonAnywhere
pip install -r requirements.txt
./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic
./manage.py createsuperuser
