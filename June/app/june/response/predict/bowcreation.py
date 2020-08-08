# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:00:13 2020

@author: PRAFULL
"""

import numpy as np

def get_bag_of_words(sentence_words, words):
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
               
    return(np.array(bag))