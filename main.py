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

def get_client():
    return tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret,
                            access_token=access_key, access_token_secret=access_secret,
                            return_type=tweepy.Response, wait_on_rate_limit=False)

def getUser(username):
    client = get_client()

    user = client.get_user(username=username)

    print(user)

# Driver code
if __name__ == '__main__':

    getUser("devdevdev1001")