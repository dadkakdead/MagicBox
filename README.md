### What is MagicBox? ###

**MagicBox** is a web application that provides easy access to data crunching scripts. It is built with [Django].

---

### How easy is it to use **MagicBox**? ###

Simply drag and drop spreadsheets or CSV files into **MagicBox** and click "Go" to run the script.

![MagicBox-demo](https://github.com/devrazdev/MagicBox/raw/master/misc/demo.gif)

### Why should I use **MagicBox**? ###
**MagicBox** provides a simple interface to run shared Python scripts to automate "repetitious spreadsheet operations."

Examples of "repetitious spreadsheet operations" include:
- Generating reports from [Excel databases], which often require "Merge," "Transform," and "Lookup" operations
- Post-processing of text format export files
- Reformatting operations, which often require writing macros or [Windows automation]

[Excel databases]: <https://www.lifewire.com/create-a-database-in-excel-3123446>
[Windows automation]: <https://autohotkey.com/>

### Why is Microsoft Excel not enough? ###
Microsoft Excel is used by [millions] for everyday data crunching operations, and many critical business applications are built around this software. However, it is not efficient for bulky and repetitive data processing. There is a constant search for improvements and workarounds to process data more efficiently. Specifically, people usually go for interface automation and/or calculation acceleration (check out [cloud computing of Excel Spreadsheets]). 

One of the approaches is doing data analysis with Python using common libraries like [Pandas] and [Numpy]. Gossip news: [Microsoft considers adding Python support to Microsoft Excel].

The biggest advantage of Excel is the intuitive interface. People would manually click the buttons over and over again and wait for calculation completion rather than write code. For such people there are tools with visual interface such as [Alteryx] or [Easymorph]. Unfortunatelly desktop versions cost a fortune and server versions are even more expensive.

[millions]: <https://medium.com/@hjalli/microsoft-excel-office-has-about-1-2billion-62239c4728ad>
[cloud computing of Excel Spreadsheets]: <https://www.redpixie.com/azure-calculation-engine>
[Pandas]: <https://pandas.pydata.org/>
[Numpy]: <http://www.numpy.org/>
[Microsoft considers adding Python support to Microsoft Excel]:<https://www.bleepingcomputer.com/news/microsoft/microsoft-considers-adding-python-as-an-official-scripting-language-to-excel/>
[Alteryx]: <https://www.alteryx.com/>
[Easymorph]: <https://easymorph.com/learn.html>

---

## Developers corner ##

### Installation/Deployment ###
The best place to host your **MagicBox** is PythonAnywhere. If you pay them [5$ per month] for Jupyter notebook support, you can switch the whole script management (editing + publishing) to the cloud... and you will never want to go back.

1. [Create free account at PythonAnywhere]
2. Go to PythonAnywhere dashboard, open new bash console, run the following commands:
    - mkvirtualenv --python=/usr/bin/python3.6 mysite-virtualenv
    - git clone https://github.com/devrazdev/MagicBox.git
    - cd MagicBox/
    - sh install.sh (you will be asked to set login/pass for superuser)
3. [Create new web application]

[5$ per month]: <https://www.pythonanywhere.com/pricing/>
[Create free account at PythonAnywhere]: <https://www.pythonanywhere.com/registration/register/beginner/>
[Create new web application]: <https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/>

### Test run ###
1. After installation, open **MagicBox** in your browser.
2. Choose one of the two example scripts (links on the right side of the page): **garmin** or **telegram**.
    - **garmin**: [very frequent request on Garmin forum]. Garmin is a smart watch brand that allows real-time heart rate monitoring. The task is to create a graph of heart rate over time throughout the day based on raw data downloaded from [Garmin website]. The tricky part is the custom binary raw data format. Moreover, the data for 1 day of measurements is split into dozens of files.  
    - **telegram**: There is data organized in columns (this is actually information about [Telegram channels]). Each line represents a data entry (a channel) and each column is a property such as name, description or size. 4 files available contain data from 4 sources ([1], [2], [3], [4]), all in different column formats. The task is to create a single list of data entries with unique name and flag the source file (can be multiple). 
3. Drag & drop the sample data. [Sample data] and [scripts] are included in the repo, Jupyter Notebooks can be [downloaded from Google Drive].
4. Click "GO".
5. Download and open the report.

### Adding new script ###
Step-by-step guide:
1. After installation, open **MagicBox** in your browser
2. Click "Manage scripts" to open administrator panel
3. From the administrator panel, click "Add report"
4. Fill the form, save it
5. On the server side, edit the *~/MagicBox/webrequest/scripts/<report_key>_script.py*
6. Reload the web application at PythonAnywhere

Video tutorial: [5 minutes long video, available on Youtube]

[Telegram channels]: <https://telegram.org/faq_channels>
[1]: <https://inten.to/telegram/>
[2]: <https://tlgrm.ru/channels>
[3]: <http://tchannels.me/>
[4]: <http://tsear.ch/>
[Garmin website]: <https://connect.garmin.com/en-US/>
[very frequent request on Garmin forum]: <https://forums.garmin.com/search?q=export+%22heart+rate%22&searchJSON=%7B%22keywords%22%3A%22export+%5C%22heart+rate%5C%22%22%7D>

[Sample data]: <https://github.com/devrazdev/MagicBox/tree/master/misc/sample%20input/>
[scripts]: <https://github.com/devrazdev/MagicBox/tree/master/webrequest/scripts>
[downloaded from Google Drive]: <https://drive.google.com/open?id=1LMCaCXxlBzrezmLBOI-wpp1WEdyFurLl>
[5 minutes long video, available on Youtube]: <https://www.youtube.com/watch?v=GMMdzOEEptk>


### Under the hood ###
- Front end: [Dropzone.js] (version 5.2.0) for drag & drop interface and initial validation
- Back end: [Django] (version 2.1.0) for business logic; received files are stored in ZIP archives

[Dropzone.js]: <https://www.dropzonejs.com/>
[Django]: <https://www.djangoproject.com/>

## How to ##
- [Configure PythonAnywhere's notebooks to use the same virtual environment as MagicBox]
- [Automate boring stuff with Python]

[Configure PythonAnywhere's notebooks to use the same virtual environment as MagicBox]: <https://help.pythonanywhere.com/pages/IPythonNotebookVirtualenvs/>
[Automate boring stuff with Python]: <https://automatetheboringstuff.com/>

## Farewell ##
I would be happy to hear any feedback about your use of **MagicBox**. Feel free to write me at devrazdev@gmail.com. Thank you.
