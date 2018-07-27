## Clean installation
Deploy using PythonAnywhere

1. (create account at PythonAnywhere)
2. (open bash console and run the following)
    - git clone https://github.com/devrazdev/webreports.git
    - mkvirtualenv --python=/usr/bin/python3.6 mysite-virtualenv
    - cd webreports/
    - sh install.sh
    - (enter login/pass/etc.)
3. (create new web application: *Django* -> *Python 3.6* -> *Manual configuration*)
4. (enter the name of virtual environment: *mysite-virtualenv*)
5. (edit the wsgi file: leave Django, uncomment, replace *mysite* to *webreports*)
6. (reload the web application)

## Updating the application
Assuming you have previously setup the web application using instruction above.

1. (remove the /webreports folder)
2. (open bash console and run the following)
    - git clone https://github.com/devrazdev/webreports.git
    - workon mysite-virtualenv    
    - cd webreports/
    - sh update.sh
    - (enter login/pass/etc.)
3. (reload the web application)

## Using your virtual environment in PythonAnywhere notebooks
- https://help.pythonanywhere.com/pages/IPythonNotebookVirtualenvs/

## Links
- https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
