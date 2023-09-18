# Written by Miranda Livengood.


# Stored data for my personal keys and secrets.
from my_data import *

import requests
import json
from requests_oauthlib import OAuth1Session

def create_tweet(message):
    url = 'https://api.twitter.com/2/tweets'
    authority = OAuth1Session(CONSUMER_KEY,
                                client_secret=CONSUMER_SECRET,
                                resource_owner_key=ACCESS_TOKEN_KEY,
                                resource_owner_secret=ACCESS_TOKEN_SECRET)
    
    payload = {"text": message}
    
    response = authority.post(url=url, json=payload)

    return dict(response.json())["data"]["id"]
