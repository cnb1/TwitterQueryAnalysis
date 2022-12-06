import constants
import tweepy

#Store you corrent tokens and keys in a constants.py folder in the same directory
consumer_key = constants.CONSUMER_KEY
consumer_secret = constants.CONSUMER_KEY_SECRET
access_key = constants.ACCESS_TOKEN
access_secret = constants.ACCESS_TOKEN_SECRET
bearer_token = constants.BEARER_TOKEN

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret,
                            access_token=access_key, access_token_secret=access_secret,
                            return_type=tweepy.Response, wait_on_rate_limit=False)