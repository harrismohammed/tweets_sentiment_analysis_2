# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 00:33:42 2018

@author: harris
"""

#Importing the libraries

import numpy as np
import tensorflow as tf
import re
import time
import json

######## DATA PREPROCESSING ######

#Importing raw_tweet_data
#Before importing the dataset, put the json objects in an array and assign a key for easier access

x =open('pollution.json',encoding = 'utf=8',errors = 'ignore')

#Loading the raw_tweet_data
data = json.load(x)

#Getting text data from retweets and orignal tweets

tweets = []

for p in range(len(data['foo'])):
    if data['foo'][p]['lang'] == 'en':
        if len(data['foo'][p]) == 27:
            tweets.append(data['foo'][p]['text'])
        elif len(data['foo'][p]) >= 28:
            if data['foo'][p]['is_quote_status'] == 'True':
                tweets.append(data['foo'][p]['quoted_status']['extended_tweet']['full_text'])
            else:
                tweets.append(data['foo'][p]['text'])
        elif len(data['foo'][p]) >= 29:
            if data['foo'][p]['is_quote_status'] == 'True':
                tweets.append(data['foo'][p]['quoted_status']['extended_tweet']['full_text'])
            else:
                tweets.append(data['foo'][p]['text'])
      

def clean_text (text):
    text = text.lower()
    text = text.replace("rt ","")
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"/;:|<>{}+=#_.,']", "", text)
    return text

    
#Cleaming the tweets
clean_tweets = []

for tweet in tweets:
    clean_tweets.append(clean_text(tweet))


########### SENTIMENT ANALYSIS (T E X T B L O B)############


from textblob import TextBlob

analysed_tweets_b = []



def print_sentiment_scores_b(clean):
    analyserb = TextBlob(clean)
    sent = analyserb.sentiment
    analysed_tweets_b.append("{:-<40} {}".format(clean, str(sent)))


for clean in clean_tweets:
    print_sentiment_scores_b(clean)


