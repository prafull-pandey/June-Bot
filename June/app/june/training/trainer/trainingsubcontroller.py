# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 23:17:05 2020

@author: PRAFULL
"""
from .Initializer import initialize_training_data
from configuration.june_configuration import June_Configuration
from .Algorithm.BasicSequential import train_model

def start_modeling():
    train_x, train_y=initialize_training_data()
    training_data_file_path=June_Configuration.get_training_model_file_path()  
    train_model(train_x, train_y, training_data_file_path)
    