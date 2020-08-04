# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:43:38 2020

@author: PRAFULL
"""
#from .. Abstract_Data_Fetch import Abstract_Data_Fetch
from configuration.june_configuration import June_Configuration
import json

class Fetch_JSON_Intents():

    def get_intents_from_json(self):
        file_path=June_Configuration.get_intents_json_file_path()
        data_file=open(file_path).read()
        intents=json.loads(data_file)
        return intents
        
    def get_intents(self):
        print('Its here')
        return self.get_intents_from_json()