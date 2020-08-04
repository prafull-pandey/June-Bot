import sys
print(sys.path)
from .middlewares import login_required
from flask import Flask, json, g, request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/askJune", methods=["GET"])
#@login_required
def ask_june():
    
    #method to ask goes here
    
    return json_response("Thisismessage")


#common functions here
def json_response(payload, status=200):
    return (json.dumps(payload), status, {'Content-type': 'application/json'})