# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 22:56:12 2020

@author: PRAFULL
"""
import pickle
from configuration.june_configuration import June_Configuration
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import random
import numpy as np

def initialize_training_data():
    training = []
    
    words_pickle_file_path=June_Configuration.get_words_pickle_file_path()
    classes_pickle_file_path=June_Configuration.get_classes_pickle_file_path()
    documents_pickle_file_path=June_Configuration.get_documents_pickle_file_path()  
    
    words=read_pickle_file(words_pickle_file_path)
    classes=read_pickle_file(classes_pickle_file_path)
    documents=read_pickle_file(documents_pickle_file_path)
    
    print (len(documents), "documents")
    # classes = intents
    print (len(classes), "classes", classes)
    # words = all words, vocabulary
    print (len(words), "unique lemmatized words", words)
    # create an empty array for our output
    output_empty = [0] * len(classes)
    # training set, bag of words for each sentence
    for doc in documents:
        # initialize our bag of words
        bag = []
        # list of tokenized words for the pattern
        pattern_words = doc[0]
        # lemmatize each word - create base word, in attempt to represent related words
        pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
        # create our bag of words array with 1, if word match found in current pattern
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)
        
        # output is a '0' for each tag and '1' for current tag (for each pattern)
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        
        training.append([bag, output_row])
    # shuffle our features and turn into np.array
    random.shuffle(training)
    training = np.array(training)
    # create train and test lists. X - patterns, Y - intents
    train_x = list(training[:,0])
    train_y = list(training[:,1])
    print("Training data created")
    return train_x, train_y
    
def read_pickle_file(file_path):
    objects = []
    with (open(file_path, "rb")) as openfile:
        while True:
            try:
                objects=pickle.load(openfile)
            except EOFError:
                break
    return objects