# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:44:15 2020

@author: PRAFULL
"""
from .fetchtrainingdata import fetch_training_data
from configuration.june_configuration import June_Configuration
import nltk
import pickle
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()


def preprocess_data():
    words=[]
    classes=[]
    documents=[]
    ignore_words=['?', '!']
    word_pickle_file_path=June_Configuration.get_words_pickle_file_path()
    classes_pickle_file_path=June_Configuration.get_classes_pickle_file_path()
    documents_pickle_file_path=June_Configuration.get_documents_pickle_file_path()
    intents=fetch_training_data()
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            #tokenize each word
            w = nltk.word_tokenize(pattern)
            words.extend(w)
            #add documents in the corpus
            documents.append((w, intent['tag']))
            # add to our classes list
            if intent['tag'] not in classes:
                classes.append(intent['tag'])
    
    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))
    # sort classes
    classes = sorted(list(set(classes)))
    # documents = combination between patterns and intents
    print (len(documents), "documents")
    # classes = intents
    print (len(classes), "classes", classes)
    # words = all words, vocabulary
    print (len(words), "unique lemmatized words", words)
    pickle.dump(words,open(word_pickle_file_path,'wb'))
    pickle.dump(classes,open(classes_pickle_file_path,'wb'))
    pickle.dump(documents,open(documents_pickle_file_path,'wb'))