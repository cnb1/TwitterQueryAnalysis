import requests
import os
import json
import pandas as pd
import csv
import datetime
import dateutil.parser
import unicodedata
import time
import tweepy

import constants

consumer_key = constants.CONSUMER_KEY
consumer_secret = constants.CONSUMER_KEY_SECRET
access_key = constants.ACCESS_TOKEN
access_secret = constants.ACCESS_TOKEN_SECRET
bearer_token = constants.BEARER_TOKEN


def get_tweets(username):
          
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)
  
        # Calling api
        api = tweepy.API(auth)
  
        # 200 tweets to be extracted
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)
  
        # Empty Array
        tmp=[] 
  
        # create array of tweet information: username, 
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
        for j in tweets_for_csv:
  
            # Appending tweets to the empty array tmp
            tmp.append(j) 
  
        # Printing the tweets
        print(tmp)
  
  
# Driver code
if __name__ == '__main__':
  
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("devdevdev1001") 