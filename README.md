## Deployment instruction

0. Create account at PythonAnywhere
1. Follow setup instructions https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
2. Copy static files https://help.pythonanywhere.com/pages/DjangoStaticFiles

## Step-by-step commands

- git clone https://github.com/devrazdev/webreports.git  
- mkvirtualenv --python=/usr/bin/python3.6 mysite-virtualenv
- git clone https://github.com/devrazdev/webreports.git
- cd webreports/
- pip install -r requirements
- ./manage.py makemigrations
- ./manage.py migrate
- ./manage.py collectstatic
