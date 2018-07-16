## Deployment instruction

0. Create account at PythonAnywhere
1. Execute step by step commands (see below)
2. Create a new web app, follow setup instructions https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/

## Step-by-step commands in PythonAnywhere bash

- mkvirtualenv --python=/usr/bin/python3.6 mysite-virtualenv
- git clone https://github.com/devrazdev/webreports.git
- cd webreports/
- pip install -r requirements.txt
- ./manage.py makemigrations
- ./manage.py migrate
- ./manage.py collectstatic
