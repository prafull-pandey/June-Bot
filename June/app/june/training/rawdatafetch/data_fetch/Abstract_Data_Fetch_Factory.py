# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:36:29 2020

@author: PRAFULL
"""
from .data_fetch_impl.Fetch_JSON_Intents import Fetch_JSON_Intents

class Abstract_Data_Fetch_Factory():
    def create_data_fetcher(self, typ):
        fetchers={
                "Json":Fetch_JSON_Intents
                }
        
        targetclass=typ.capitalize()
        return fetchers[targetclass]()
