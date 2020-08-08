import sys
print(sys.path)
from .middlewares import login_required
from flask import Flask, json, g, request
from flask_cors import CORS
from app.june.starttraining import start_training
from app.june.responsecontroller import get_response_from_prediction

app=Flask(__name__)
CORS(app)

@app.route("/askJune", methods=["GET"])
#@login_required
def ask_june():
    
    #method to ask goes here
    que=request.args.get('ask')
    return json_response(get_response_from_prediction(que))


@app.route("/trainModel", methods=["POST"])
def train_model():
    start_training('start')
    return json_response("trained Successfully")

#common functions here
def json_response(payload, status=200):
    return (json.dumps(payload), status, {'Content-type': 'application/json'})