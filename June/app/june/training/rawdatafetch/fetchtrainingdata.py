# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:33:01 2020

@author: PRAFULL
"""
from .data_fetch import Abstract_Data_Fetch_Factory as fetch_factory

def fetch_training_data():
    source='JSON'
    
    data_source_object=get_data_fetch_source_object(source)
    return data_source_object.get_intents()
        
def get_data_fetch_source_object(source):
    fetch_factory_obj=fetch_factory.Abstract_Data_Fetch_Factory()
    return fetch_factory_obj.create_data_fetcher(source)