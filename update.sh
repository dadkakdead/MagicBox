#!/bin/bash
# Update the application in PythonAnywhere
./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic
./manage.py createsuperuser
