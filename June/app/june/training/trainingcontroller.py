# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 22:50:06 2020

@author: PRAFULL
"""
import rawdatafetch.fetchandpreprocessdata as preprocessor
import trainer.trainingsubcontroller as subcontroller

def main_controller():
    #crete training data 
    preprocessor.preprocess_data()
    #trainng data created
    
    #start model building
    subcontroller.start_modeling()
    