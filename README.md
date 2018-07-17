## Clean installation
Deploy using PythonAnywhere

1. (create account at PythonAnywhere)
2. (open bash console and run the following)
    - git clone https://github.com/devrazdev/webreports.git
    - mkvirtualenv --python=/usr/bin/python3.6 mysite-virtualenv
    - cd webreports/
    - pip install -r requirements.txt
    - ./manage.py makemigrations
    - ./manage.py migrate
    - ./manage.py collectstatic
    - ./manage.py createsuperuser
    - (enter login/pass/etc.)
3. (create new web application (Django -> Python 3.6 -> Manual configuration)
4. (enter the name of virtual environment)
5. (fix the wsgi file)
6. (reload the web application)

## Updating the application
Assuming you have previously setup the web application using instruction above.

1. (remove the /webreports folder)
2. (open bash console and run the following)
    - git clone https://github.com/devrazdev/webreports.git
    - workon mysite-virtualenv    
    - cd webreports/
    - ./manage.py makemigrations
    - ./manage.py migrate
    - ./manage.py collectstatic
    - ./manage.py createsuperuser
    - (enter login/pass/etc.)
3. (reload the web application)


## Links
- https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
