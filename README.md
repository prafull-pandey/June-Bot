# June-Bot
A Chat bot Application based on python, react and Java Microservice

#Installation
Python based project June is based on virtual environment
 Git clone the repo
 go to June/Scripts folder
 
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
 virtual environment will be setup
 (Since this is flask based application June\app\http\api\endpoints.py is api file
 the same path is used as FLASK_APP path, This is already set)
 
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


 
 
 
 
 
 
 
