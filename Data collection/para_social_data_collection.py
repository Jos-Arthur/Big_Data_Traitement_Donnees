#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 15:17:39 2020

@author: jose-arthur
"""
import threading
import time
import tweepy
import facebook
import json
import codecs
import os

####input your credentials here
""" 
    The following shows the use of the token 
    for data collection on the social network Twitter!
"""
consumer_key = 'j9Rj7NpkJpMS0QWkZeXwCojcC'
consumer_secret = 'O1QYWlbfBLUHi4bICpsIQMbnhqBefA7m6As47JlvsnlHI3SLW5'
access_token = '1283183414221377537-BA8exaLOxUNuYO1z9tvWVysSsYW9hT'
access_token_secret = 'HhSmgiMi4yoeEiRmr6sF5dacjp8xtKDlbXquicw3G6VVP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)



"""

    The use of token for data collection on the social network Facebook!

"""

# access_token_facebook = 'EAAEMoEaTd3wBAAku48d4vF3BLSJh5tCgEN5UaasM1ZBID2hZAYOlLGUQrBldkeX8Uo5H8VQaNYXlrbwjj2Ao1EbXMZCIBmYXYTNh2vINkvwrMVOmqFPt7LuRnkXLCTTQFUZBPmnEYnv3VKldy6mUrXnZAYYrx2UH1Brj8bObietzv42eAZAv6bjD2BhbR7fo0ZD'

start_time = time.time()

def task1():
    #First bloc to collect data for terrorism
    start_time_t1 = time.time()
    results = tweepy.Cursor(api.search,q="#Terrorism",count=70,
                               lang="en",
                               since="2020-10-24").items()
    end_time_t1 = time.time()
    print("Le temps d'execution du task1-Twitter-Terrorism {}", end_time_t1 -start_time_t1)
    print()
    fichier = open("output/para_terrorism_data.csv", "a")
    for _result in results:
        print("Data collecting of TERRORISM")
        fichier.write(str(_result.text))
    fichier.close()

def task2():
    #Second bloc to collect data for covid19
    start_time_t2 = time.time()
    covids = tweepy.Cursor(api.search,q="#COVID19",count=70,
                               lang="en",
                               since="2020-10-24").items()
    end_time_t2 = time.time()
    print("Le temps d'execution du task2Twitter-Covid19 {}", end_time_t2 -start_time_t2)
    print()
    
    fichier = open("output/para_covid_data.csv", "a")
    for _result in covids:
        print("Data getting of COVID19")  
        fichier.write(str(_result.text))
    fichier.close()

#def task3():
#    #Third bloc to collect data for covid19
#    
#    token = access_token_facebook
#    graph = facebook.GraphAPI(token)   
#    start_time_t3 = time.time()
#    
#    users_posts = graph.get_object('me',fields='posts.fields(type, name, message, created_time, object_id).limit(70)')
#    end_time_t3 = time.time()
#    
#    print("Le temps d'execution du task3-Facebook_Data {}", end_time_t3 -start_time_t3)
#    print()
#    
#    fichier = codecs.open("/home/jose-arthur/tests/para_facebook_data.json", "a", encoding='utf8')
#    print("Data gattering of Graph API")
#    fichier.write(str(json.dumps(users_posts, indent=4)))
#    fichier.close()
#    
#end_time = time.time()
#print ("Le temps d'execution global des trois Thread =", end_time -start_time)
        
if __name__ == "__main__":
 
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))
 
    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))
   
    # creating threads
   
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')  
#    t3 = threading.Thread(target=task3, name='t3')  
 
    # starting threads
    print("starting threads Now !")
    t1.start()
   
    t2.start()
    
#    t3.start()
    
    # wait until all threads finish
    print("Wait until all threads finish")
    t1.join()
    
    t2.join()
    
#    t3.join()
   
