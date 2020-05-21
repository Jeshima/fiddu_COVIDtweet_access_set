#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
from textblob import TextBlob


# In[2]:


auth=tweepy.OAuthHandler("jsU0a5IcdcEcleXmyrnAcQW1f","pYO1KsrMvHmzBeMvAVDZLRWRETWUb3vXHUKTWP6NMGzpOuerCG")


# In[3]:


auth.set_access_token("1254072447873122305-zL36dujdsPmfRfZ83QJ5AH2j1xwTNM"
,"KEBBJlNvLAF5lto7eulxH53jPktGYCKMkraT6Ml1qnpAm")


# In[4]:


api=tweepy.API(auth)
query=input('Enter the word to find sentiments about: ')
public_tweets= api.search(query)


# In[5]:


for tweet in public_tweets:  
    print(tweet.text)    
    analysis = TextBlob(tweet.text)   
    print(analysis.sentiment)    
    if analysis.sentiment[0]>0:       
        print ('Positive\n'  )  
    elif analysis.sentiment[0]<0:       
        print ('Negative\n')    
    else:      
        print ('Neutral\n')


# In[9]:


import json
import csv


f = open('COVID19_line_list_data.csv','a',encoding='utf-8')
csvWriter = csv.writer(f)
headers=['full_text','retweet_count','user_followers_count','favorite_count','place','coordinates','geo','created_at','id_str']
csvWriter.writerow(headers)

for inputFile in ['sb_04_08_19.txt']:#all the text-file names you want to convert to Csv in the sae folder as this code
    tweets = []
    for line in open(inputFile, 'r'):
        tweets.append(json.loads(line))

    print('HI',len(tweets))
    count_lines=0
    for tweet in tweets:
        try:
            csvWriter.writerow([tweet['full_text'],tweet['retweet_count'],tweet['user']['followers_count'],tweet['favorite_count'],tweet['place'],tweet['coordinates'],tweet['geo'],tweet['created_at'],str(tweet['id_str'])])
            count_lines+=1
        except Exception as e:
            print(e)
    print(count_lines)


# In[ ]:




