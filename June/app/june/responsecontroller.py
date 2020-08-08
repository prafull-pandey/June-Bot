# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:58:12 2020

@author: PRAFULL
"""

from app.june.response.predictcontroller import start_predicting
from app.june.response.fetchresponse import get_response_from_intents

def get_response_from_prediction(sentence):
    
    
    #fetch possible intents list
    valid_intents=start_predicting(sentence)
    
    response=get_response_from_intents(valid_intents)
    return response