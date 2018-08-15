### What is MagicBox? ###

**MagicBox** is a web application that provides easy access to data crunching scripts. It is built with [Django].

---

### How easy is it to use **MagicBox**? ###

Simply drag and drop spreadsheets or CSV files into **MagicBox** and click "Go" to run the scripts.

![MagicBox-demo](https://github.com/devrazdev/MagicBox/raw/master/misc/demo.gif)

### Why should I use **MagicBox**? ###
**MagicBox** provides a simple interface to run shared Python scripts to automate "repetitious spreadsheet operations."

Examples of "repetitious spreadsheet operations" include:
- Generating reports from [Excel databases], which often require "Merge," "Transform," and "Lookup" operations
- Post-processing of text format export files
- Reformatting operations, which often require macros / [Windows automation]

[Excel databases]: <https://www.lifewire.com/create-a-database-in-excel-3123446>
[Windows automation]: <https://autohotkey.com/>

### Why is Microsoft Excel not enough? ###
Microsoft Excel is used by [millions] for everyday data crunching operations, and many critical business applications are built around this software.  but it is not efficient for bulky and repetitive data processing. Many critical business applications are built around Microsoft Excel, but there is a constant search for workarounds to process such bulky data. (even [cloud computing of Excel Spreadsheets]).

One of the approaches is doing data analysis with Python (edit in Jupyter, import [Pandas] + [Numpy] + whatsoever). Gossip news: [Microsoft considers adding Python support to Microsoft Excel].

Reality is that Excel is intuitive and Python is not, so people rather "wait until calculation finishes" ot "repeat manually" than anything. For such people there are "visual programming" solutions ([Alteryx], [Easymorph]), but desktop versions are priced like Tesla, and server versions — like rocketships. Meaning, your 10 lines of Python code can be very time-saving for them.

[100s millions people]: <https://medium.com/@hjalli/microsoft-excel-office-has-about-1-2billion-62239c4728ad>
[recommend]: <https://www.amazon.com/Data-Smart-Science-Transform-Information/dp/111866146X>
[cloud computing of Excel Spreadsheets]: <https://www.redpixie.com/azure-calculation-engine>
[Pandas]: <https://pandas.pydata.org/>
[Numpy]: <http://www.numpy.org/>
[Microsoft considers adding Python support to Microsoft Excel]:<https://www.bleepingcomputer.com/news/microsoft/microsoft-considers-adding-python-as-an-official-scripting-language-to-excel/>
[Alteryx]: <https://www.alteryx.com/>
[Easymorph]: <https://easymorph.com/learn.html>

---

## Developers corner ##

### Installation ###
Suggesting you deploy it on PythonAnywhere. If you pay them [5$] for Jupyter notebook support, you can switch the whole script management (editing + publishing) to the cloud... and you will never want to go back.

1. [Create free account at PythonAnywhere]
2. Go to PythonAnywhere dashboard, open new bash console, run the following commands:
    - mkvirtualenv --python=/usr/bin/python3.6 mysite-virtualenv
    - git clone https://github.com/devrazdev/MagicBox.git
    - cd MagicBox/
    - sh install.sh (you will be asked to set login/pass for superuser)
3. [Create new web application]

[5$]: <https://www.pythonanywhere.com/pricing/>
[Create free account at PythonAnywhere]: <https://www.pythonanywhere.com/registration/register/beginner/>
[Create new web application]: <https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/>

### Test run ###
1. After installation, open MagicBox in your browser
2. Choose one of two sample reports: **garmin** or **telegram**
    - **garmin**: [very frequent request on Gamin forum]. There is a bunch of CSV files with export data from [Garmin Connect] for 1 day. The task is to derive the heart rate time series.
    - **telegram**: there are 4 lists of [Telegram channels] from 4 sources ([1], [2], [3], [4]), all in different formats. The task is to create a single list of unique channels and flag the source (can be multiple)
3. Drag & drop the sample data. [Sample data] and [scripts] are included in the repo, Jupyter Notebooks can be [downloaded from Google Drive].
4. Click "GO"
5. Download and open the report

### Adding new report ###
1. After installation, open MagicBox in your browser
2. Click "Manage reports"
3. From the administrator intefrace, click "Add report"
4. Fill the form, save it
5. On the server side, edit the *~/MagicBox/webrequest/scripts/<report_key>_script.py*
6. Reload the web application

There is also a 5-minutes-long [video tutorial].

[Telegram channels]: <https://telegram.org/faq_channels>
[1]: <https://inten.to/telegram/>
[2]: <https://tlgrm.ru/channels>
[3]: <http://tchannels.me/>
[4]: <http://tsear.ch/>
[a bunch of CSV files]: <https://github.com/devrazdev/MagicBox/tree/master/misc/sample%20input/garmin>
[Garmin Connect]: <https://connect.garmin.com/en-US/>
[very frequent request on Gamin forum]: <https://forums.garmin.com/search?q=export+%22heart+rate%22&searchJSON=%7B%22keywords%22%3A%22export+%5C%22heart+rate%5C%22%22%7D>

[Sample data]: <https://github.com/devrazdev/MagicBox/tree/master/misc/sample%20input/>
[scripts]: <https://github.com/devrazdev/MagicBox/tree/master/webrequest/scripts>
[downloaded from Google Drive]: <https://drive.google.com/open?id=1LMCaCXxlBzrezmLBOI-wpp1WEdyFurLl>
[video tutorial]: <https://www.youtube.com/watch?v=GMMdzOEEptk>


### Under the hood ###
- Front end: [Dropzone.js] for drag & drop and initial validation
- Back end: [Django] for business logic; received files are stored in ZIP archives

[Dropzone.js]: <https://www.dropzonejs.com/>
[Django]: <https://www.djangoproject.com/>

## How to ##
- [Configure PythonAnywhere's notebooks to use the same virtual environment as MagicBox]
- [Automate boring stuff with Python]

[Configure PythonAnywhere's notebooks to use the same virtual environment as MagicBox]: <https://help.pythonanywhere.com/pages/IPythonNotebookVirtualenvs/>
[Automate boring stuff with Python]: <https://automatetheboringstuff.com/>

## Farewell ##
I would be happy to hear any feedback/news about how you use **MagicBox** in real life. Feel free to email me at devrazdev@gmail.com. Thank you.
