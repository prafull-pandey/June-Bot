# June-Bot
A Chat bot Application based on python, react and Java Microservice
Python 3.7.5

#Installation
make sure you have instaled virtualenv from pip
```bash
python -m pip install --upgrade virtualenv
```
Create a folder and setup virtual env inside that
```bash
python -m virtualenv .
```
 Git clone the repo inside folder
 
 go to June/Scripts folder
 
 edit activate.bat file and add the following lines at starting
 
 ```bat
 @echo off

if not "%VIRTUAL_ENV%" == "" (

	goto gotHome

) else (

	cd ..

)

set "VIRTUAL_ENV=%cd%"

set "FLASK_APP=%cd%/June-Bot/June/app/http/api/endpoints.py"

cd "%CURRENT_DIR%"

:gotHome

if exist "%VIRTUAL_ENV%\Scripts\activate.bat" (

	goto okHome

) else (

	goto end

)

:okHome

 ```
 
 and these lines at end
 ```bat
 set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

set "PATH=%VIRTUAL_ENV%\June-Bot\June;%PATH%"
set "PYTHONPATH=%VIRTUAL_ENV%\June-Bot\June;%PYTHONPATH%"
 ```
 
 Code for linux and powershell will be written soon
 
 
 start virtual environment based on your favorite terminal
 
 for powershell
 ```bash
 ./Activate.ps1
 ```
 for CMD
  ```bash
 activate.bat
 ```
 for linux
 ```bash
 ./activate
 ```
 
 Now we need to install the dependencies as used by project 
 The dependency file exists at June/requirements.txt
 to install these dependencies
  activate virtual env as above method
  
  ```dos
  pip install -r June-Bot\June\requirements.txt
  ```
 
 virtual environment will be setup
 (Since this is flask based application June\app\http\api\endpoints.py is api file
 the same path is used as FLASK_APP path, This is already set)
 
 go to June-Bot\June\configuration\june_training_configuration.ini 
 and edit the paths as your local systems
 
 Another Important thing is NLTK resources
 
 ```dos
 python
 import nltk
 nltk.download()
 ```
 Download all
 
 
 after activating virtual environment run the following command
 ```bash
 python -m flask run
 ```
 
 Flask server will start at http://localhost:5000/
 
 # API Usage
 
###### GET    /askJune?ask=<your_text>
<your_text> replaces the talk you want to speak to June

###### POST   /trainModel
This starts training model from updated intents file
Right now this project is based on training model fron json file stored at June/extras/intents.json, the path can be configured from configuration/june-configuration.ini


 
 
 
 
 
 
 
