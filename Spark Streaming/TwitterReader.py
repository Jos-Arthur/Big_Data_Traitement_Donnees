#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 05:53:14 2020

@author: jose-arthur
"""

import tweepy
from tweepy.auth import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
import csv
import sys
import time

# Set up your credentials from http://apps.twitter.com

consumer_key = 'j9Rj7NpkJpMS0QWkZeXwCojcC'
consumer_secret = 'O1QYWlbfBLUHi4bICpsIQMbnhqBefA7m6As47JlvsnlHI3SLW5'
access_token = '1283183414221377537-BA8exaLOxUNuYO1z9tvWVysSsYW9hT'
access_token_secret = 'HhSmgiMi4yoeEiRmr6sF5dacjp8xtKDlbXquicw3G6VVP'

# Create a class that will listen to tweets from Streamlistener
class TweetsListener(StreamListener):

  def __init__(self, csocket, list_=None, dict_= None):
      self.client_socket = csocket
      self.keys_= list_
      self.dict = dict_

  def on_data(self,data):
        if data:
            tweet_json = json.loads(data)
            # print(tweet_json['user']['location'])
            print(" GET Streaming DATA ON TWITTER!!!")
            if not (tweet_json['text'].strip().startswith('RT ')):
               
                Created = tweet_json['created_at']            #tweet posted at UTC time
                Text = tweet_json['text']
                # id_str = tweet_json['id_str']
                Userid = tweet_json['user']['id_str']
                Username = tweet_json['user']['screen_name']
                Location = tweet_json['user']['location']
                Hastag = tweet_json['entities']['hashtags']
                
                self.client_socket.send( tweet_json['text'].encode('utf-8') )
               
                with open('OutputStreaming.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([Created, Text, Userid, Username ,Location ,Hastag])
                    time.sleep(5)
        return True
    

def on_error(self, status_code):
    
    if status_code == 420:
        return False
    else:
        print('Encountered error with status code:', status_code, sys.stderr)
    #return False # Don't kill the stream
  
 # Writing csv titles
with open('OutputStreaming.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Text','User_ID', 'User_Name',  'Location','Hash_Tag'])

def create_dict(list_):
    no_of_tweets = 10
    dict_ =  {k:no_of_tweets for k in list_ }
    return dict_


def sendData(c_socket):
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  
  search_word = ['#Terrorism','#COVID19','#Coronavirus']  
  
  start_time = time.time() # Start time in seconds
  twitter_stream = Stream(auth, TweetsListener(c_socket,list_=search_word , dict_=create_dict(search_word)))
  twitter_stream.filter(track= search_word, languages = ["en"])
  end_time = time.time()
  
  Temps = end_time -start_time
  
  with open('temps.csv', 'a') as fichier:
    writer = csv.writer(fichier)
    writer.writerow([Temps])
    
  with open('temps.csv', 'w') as fichier:
    writer = csv.writer(fichier)
    writer.writerow(['Temps'])

                    
if __name__ == "__main__":
  s = socket.socket()         # Create a socket object
  host = "127.0.0.1"     # Get local machine name
  port = 5555                # Reserve a port for your service.
  s.bind((host, port))        # Bind to the port

  print("Listening on port: %s" % str(port))

  s.listen(5)                 # Now wait for client connection.
  c, addr = s.accept()        # Establish connection with client.

  print( "Received request from: " + str( addr ) )

  sendData( c )
  
  
    
    


    
    
    
