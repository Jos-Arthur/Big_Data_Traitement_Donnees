#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 01:11:04 2020

@author: jose-arthur
"""

import tweepy
import time
import facebook
import json
import os
import codecs


####input your credentials here
consumer_key = 'j9Rj7NpkJpMS0QWkZeXwCojcC'
consumer_secret = 'O1QYWlbfBLUHi4bICpsIQMbnhqBefA7m6As47JlvsnlHI3SLW5'
access_token = '1283183414221377537-BA8exaLOxUNuYO1z9tvWVysSsYW9hT'
access_token_secret = 'HhSmgiMi4yoeEiRmr6sF5dacjp8xtKDlbXquicw3G6VVP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data

access_token_facebook = 'EAAEMoEaTd3wBAAku48d4vF3BLSJh5tCgEN5UaasM1ZBID2hZAYOlLGUQrBldkeX8Uo5H8VQaNYXlrbwjj2Ao1EbXMZCIBmYXYTNh2vINkvwrMVOmqFPt7LuRnkXLCTTQFUZBPmnEYnv3VKldy6mUrXnZAYYrx2UH1Brj8bObietzv42eAZAv6bjD2BhbR7fo0ZD'

start_time = time.time()
# print ID of current process
print("ID of process running main program: {}".format(os.getpid()))
   
start_time_t1 = time.time()
#First bloc to collect data for terrorism
results = tweepy.Cursor(api.search,q="#Terrorism",count=100,
                           lang="en",
                           since="2020-10-20").items()
end_time_t1 = time.time() 
print("Le temps d'execution du task1-Terrorism {}", end_time_t1 -start_time_t1)

start_time_t2 = time.time()   
#Second bloc to collect data for covid19
covids = tweepy.Cursor(api.search,q="#COVID19",count=100,
                           lang="en",
                           since="2020-10-20").items()
end_time_t2 = time.time()
print("Le temps d'execution du task2-covid19 {}", end_time_t2 -start_time_t2)

start_time_t3 = time.time()

#SThird  bloc to collect data for Facebook
token = access_token_facebook
graph = facebook.GraphAPI(token)   

users_posts = graph.get_object('me',fields='posts.fields(type, name, message, created_time, object_id).limit(100)')
end_time_t3 = time.time()
print("Le temps d'execution du task3-Facebook Posts {}", end_time_t3 -start_time_t3)

end_time = time.time()
print("Result for execution time in sequentiel method =", end_time - start_time)

fichier = open("output/seq_terrorism_data.csv", "a")
for _result in results:
    print("Writting sequentiel terrorism data!")
    fichier.write(str(_result.text))
    fichier.close()
    
fichier1 = open("output/seq_covid_data.csv", "a")     
for _result in covids:  
    print("Writting sequentiel covid19 data!")
    fichier1.write(str(_result.text))
    fichier1.close()
    
fichier2 = codecs.open("output/seq_facebook_data.json", "a", encoding='utf8')
print("Writting sequentiel Facebook Posts!")
fichier2.write(str(json.dumps(users_posts, indent=4)))
fichier2.close()



