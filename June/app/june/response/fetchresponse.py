# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:01:04 2020

@author: PRAFULL
"""

import random
from app.june.training.rawdatafetch.fetchtrainingdata import fetch_training_data

def get_response_from_intents(valid_intents):
    
    intents=fetch_training_data()
    tag = valid_intents[0]['intent']
    list_of_intents = intents['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result