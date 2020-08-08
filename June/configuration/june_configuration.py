# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:06:55 2020

@author: PRAFULL
"""

import configparser
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

class June_Configuration:
    
    def __init__(self):
        self.basic_config=self.loadBasicConfiguration()
        self.training_config=self.load_training_config()         
    
    @staticmethod
    def loadBasicConfiguration():
        # Load the configuration file
        my_file = os.path.join(THIS_FOLDER, 'basicconfiguration.ini')
        config = configparser.ConfigParser()
        config.read(my_file)
        return config
    
    @staticmethod
    def load_training_config():
        # Load the configuration file
        my_file = os.path.join(THIS_FOLDER, 'june_training_configuration.ini')
        config = configparser.ConfigParser()
        config.read(my_file)
        return config
    
   
    #basic_config=loadBasicConfiguration()
    


    @staticmethod
    def get_intents_json_file_path():
        training_config=June_Configuration.load_training_config()
        return training_config['filePaths']['intentsjsonfilepath']
    
    @staticmethod
    def get_words_pickle_file_path():
        training_config=June_Configuration.load_training_config()
        return training_config['filePaths']['pickleWordsPath']
    
    @staticmethod
    def get_classes_pickle_file_path():
        training_config=June_Configuration.load_training_config()
        return training_config['filePaths']['pickleclassesPath']
    
    @staticmethod
    def get_documents_pickle_file_path():
        training_config=June_Configuration.load_training_config()
        return training_config['filePaths']['pickledocumentsPath']

    @staticmethod
    def get_training_model_file_path():
        training_config=June_Configuration.load_training_config()
        return training_config['filePaths']['trainedmodelpath']


    