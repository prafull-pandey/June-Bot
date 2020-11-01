# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:58:51 2020

@author: PRAFULL
"""
import pickle
from keras.models import load_model

from app.june.response.predict.cleanup import clean_up_sentence
from app.june.response.predict.bowcreation import get_bag_of_words
from app.june.response.predict.modelprediction import predict_model_class
from configuration.june_configuration import June_Configuration

def start_predicting(sentence):
    
    words, classes=load_words_and_classes()
    model=load_model_file()
    print('Inside Algo')
    print('Input sentence: '+sentence)
    #clean and tokenize the sentence
    sentence_words=clean_up_sentence(sentence)
    print('Tokenized sentence: ')
    print(sentence_words)
    
    #get bag of words
    bow=get_bag_of_words(sentence_words, words)

    print('Bag of Words: ')
    print(bow)
    
    #predict the class from model
    possible_intent_list=predict_model_class(model, bow, classes)
    
    return possible_intent_list
     
def load_words_and_classes():
    words_pickle_file_path=June_Configuration.get_words_pickle_file_path()
    classes_pickle_file_path=June_Configuration.get_classes_pickle_file_path()
    
    words=read_pickle_file(words_pickle_file_path)
    classes=read_pickle_file(classes_pickle_file_path)
    
    return words, classes

def read_pickle_file(file_path):
    objects = []
    with (open(file_path, "rb")) as openfile:
        while True:
            try:
                objects=pickle.load(openfile)
            except EOFError:
                break
    return objects

def load_model_file():
    training_data_file_path=June_Configuration.get_training_model_file_path()
    model = load_model(training_data_file_path)
    return model