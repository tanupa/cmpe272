


# Stored data for my personal keys and secrets.
from my_data import *

import requests
import json
from requests_oauthlib import OAuth1Session
import unittest

# Written by Miranda Livengood.
class Tweet:
  def create_tweet(message):
      url = 'https://api.twitter.com/2/tweets'
      authority = OAuth1Session(CONSUMER_KEY,
                                  client_secret=CONSUMER_SECRET,
                                  resource_owner_key=ACCESS_TOKEN_KEY,
                                  resource_owner_secret=ACCESS_TOKEN_SECRET)
    
      payload = {"text": message}
    
      response = authority.post(url=url, json=payload)

      return dict(response.json())["data"]["id"]

# Written by Tanupa Thaker.
class TestTweet(unittest.TestCase):
    def test_create_tweet(self):
        message = "test to create tweet."
        tweet_id = Tweet.create_tweet(message)
        self.assertIsNotNone(tweet_id, "Tweet creation failed")
