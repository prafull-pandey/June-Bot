# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 22:50:06 2020

@author: PRAFULL
"""
import app.june.training.rawdatafetch.fetchandpreprocessdata as preprocessor
import app.june.training.trainer.trainingsubcontroller as subcontroller

def main_controller():
    #crete training data 
    preprocessor.preprocess_data()
    #trainng data created
    
    #start model building
    subcontroller.start_modeling()
    