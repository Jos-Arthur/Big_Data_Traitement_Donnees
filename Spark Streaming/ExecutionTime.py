#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 05:53:14 2020

@author: jose-arthur
"""

import sys
import tweepy
import csv
import json
import time

# Set up your credentials from http://apps.twitter.com

consumer_key = 'j9Rj7NpkJpMS0QWkZeXwCojcC'
consumer_secret = 'O1QYWlbfBLUHi4bICpsIQMbnhqBefA7m6As47JlvsnlHI3SLW5'
access_token = '1283183414221377537-BA8exaLOxUNuYO1z9tvWVysSsYW9hT'
access_token_secret = 'HhSmgiMi4yoeEiRmr6sF5dacjp8xtKDlbXquicw3G6VVP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Create a class that will listen to tweets from Streamlistener
class TweetsListener(tweepy.StreamListener):
    
  def __init__(self, list_=None, dict_= None):
      self.keys_= list_
      self.dict = dict_

  def on_data(self,data):
      
    search_word = ['#Terrorism','#COVID19','#Coronavirus']  
    l = TweetsListener(list_=search_word , dict_=create_dict(search_word))
    
    start_time = time.time()
    streamingAPI = tweepy.streaming.Stream(api.auth, l)
    streamingAPI.filter(track= search_word, languages = ["en"])
    end_time = time.time()
    
    Temps = end_time -start_time
    
    print("Le temps d'execution est {} :", Temps)
    
        
    
def create_dict(list_):
    no_of_tweets = 100
    dict_ =  {k:no_of_tweets for k in list_ }
    return dict_
    

def on_error(self, status_code):
    
    if status_code == 420:
        return False
    else:
        print('Encountered error with status code:', status_code, sys.stderr)
    #return False # Don't kill the stream
def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream
# Writing csv titles
with open('/home/jose-arthur/streaming/reaming.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Text','User_ID', 'User_Name',  'Location','Hash_Tag'])
if __name__ == '__main__':
    
    search_word = ['#Terrorism','#COVID19','#Coronavirus']  
    l = TweetsListener(list_=search_word , dict_=create_dict(search_word))
    
    start_time = time.time()
    streamingAPI = tweepy.streaming.Stream(api.auth, l)
    streamingAPI.filter(track= search_word, languages = ["en"])
    end_time = time.time()
    
    Temps = end_time -start_time
    
    print("Le temps d'execution est {} :", Temps)
  
    print("TRUE")