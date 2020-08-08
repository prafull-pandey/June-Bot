# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:00:29 2020

@author: PRAFULL
"""
import numpy as np

ERROR_THRESHOLD = 0.25

def predict_model_class(model, bow, classes):
    res = model.predict(np.array([bow]))[0]
    
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list