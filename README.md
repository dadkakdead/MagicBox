### What is ntReport? ###

**ntReport** is web application, which you deploy to provide easy access to your data crunching scripts. It's built with Django.

---

### How easy is it for users? ###

No more than drag & drop.

![ntReport-demo](https://github.com/devrazdev/ntReport/raw/master/misc/demo.gif)

### Why should I use it? ###
Once you write a Python script for a repetitious spreadsheet operation on a local computer, there is a need to provide a simple interface for others to use it — **ntReport** let's you do it with just a few clicks in admin panel and copy-paste to template file. See the whole process in the [product demo]. 

Examples of "repetitious spreadsheet operation", which are worth automating:
- Generating reports from [Excel databases], which usually require "Merge", "Transform", "Lookup" operations
- Post-processing of text format export files
- Reformating operations, which usually require macros / [Windows automation]

### Why Microsoft Excel is not enough? ###
Microsoft Excel plays a huge role in everyday data cruching tasks (it's used by [100s millions people], some of them even [recommend] it for working with Big Data). It's not the best tool for heavy calculations, but many business-critical applications are built with it, so there is constant search for workarounds (even [cloud computing of Excel Spreadsheets]).

One of the approaches is doing data analysis with Python (edit in Jupyter, import Pandas + Numpy + whatsoever). Gossip news: [Microsoft considers adding Python support to Microsoft Excel].

Reality is that Excel is intuitive and Python is not, so people rather "wait until calculation finishes" ot "repeat manually" than anything. For such people there are "visual programming" solutions ([Alteryx], [Easymorph]), but desktop versions are priced like Tesla, and server versions — like rocketships. Meaning, your 10 lines of Python code can be very time-saving.

---

## Developers corner ##

### Installation ###
Suggesting you deploy it on PythonAnywhere. If you pay them [5$] for Jupyter notebook support, you can switch the whole script management (editing + publishing) to the cloud... and you will never want to go back.

1. [Create free account at PythonAnywhere]
2. Go to PythonAnywhere dashboard, open new bash console, run the following commands:
    - git clone https://github.com/devrazdev/ntReport.git
    - mkvirtualenv --python=/usr/bin/python3.6 mysite-virtualenv
    - cd ntReport/
    - sh install.sh (you will be asked to set login/pass for superuser)
3. [Create new web application]

[Create free account at PythonAnywhere]: <https://www.pythonanywhere.com/registration/register/beginner/>
[Create new web application]: <https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/>

### Under the hood ###
- Front end: [Dropzone.js] for drag & drop UI; total number of files and files' extensions are validated
- Back end: [Django] for business logic; received files are stored in ZIP archive

## How to ##
- [Configure PythonAnywheres's notebooks to use the same virtual environment]
- [Automate boring stuff]

## Farewell ##
I would be happy to hear any feedback/news about how you use **ntReport** in real life. Feel free to write me at devrazdev@gmail.com. Thank you.


[5$]: <https://www.pythonanywhere.com/pricing/>
[product demo]: <https://github.com/devrazdev/ntReport/raw/master/misc/demo.gif>
[100s millions people]: <https://medium.com/@hjalli/microsoft-excel-office-has-about-1-2billion-62239c4728ad>
[recommend]: <https://www.amazon.com/Data-Smart-Science-Transform-Information/dp/111866146X>
[cloud computing of Excel Spreadsheets]: <https://www.redpixie.com/azure-calculation-engine>
[Excel databases]: <https://www.lifewire.com/create-a-database-in-excel-3123446>
[Pandas]: <https://pandas.pydata.org/>
[Numpy]: <http://www.numpy.org/>
[Microsoft considers adding Python support to Microsoft Excel]:<https://www.bleepingcomputer.com/news/microsoft/microsoft-considers-adding-python-as-an-official-scripting-language-to-excel/>
[Alteryx]: <https://www.alteryx.com/>
[Easymorph]: <https://easymorph.com/learn.html>
[Windows automation]: <https://autohotkey.com/>
[Dropzone.js]: <https://www.dropzonejs.com/>
[Django]: <https://www.djangoproject.com/>
[Configure PythonAnywheres's notebooks to use the same virtual environment]: <https://help.pythonanywhere.com/pages/IPythonNotebookVirtualenvs/>
[Automate boring stuff]: <https://automatetheboringstuff.com/>
