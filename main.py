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

#Store you corrent tokens and keys in a constants.py folder in the same directory
consumer_key = constants.CONSUMER_KEY
consumer_secret = constants.CONSUMER_KEY_SECRET
access_key = constants.ACCESS_TOKEN
access_secret = constants.ACCESS_TOKEN_SECRET
bearer_token = constants.BEARER_TOKEN

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret,
                            access_token=access_key, access_token_secret=access_secret,
                            return_type=tweepy.Response, wait_on_rate_limit=False)

def get_client():
    return client

def getUser(username):
    client = get_client()

    user = client.get_user(username=username)

    print(user)

def count_tweets(query):
    client = get_client()

    count = client.get_recent_tweets_count(query=query)

    print(count.meta)

# Driver code
if __name__ == '__main__':

    getUser("devdevdev1001")

    count_tweets("bitcoin")