#account_id = '1703147532623413248'
'''
ACCOUNT_ID = '1703147532623413248'
CONSUMER_KEY = 'WnR7AjgfoTp4cwf6znbYJjRhq'
CONSUMER_SECRET = '2fzzhwKCtg1RgkraTTSqH5PbrlQUeYppIfpQjCFTYzF8AU0o5s'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAEL5pwEAAAAAfY9a5QOIt64YhuLEz8l0Dt8yjiU%3DkrIvApJAh6LGePfK7TK39RJhUQSk5zVcd6K1xHHWbnnpJubBiE'
ACCESS_TOKEN_KEY = '1703147532623413248-lpPQKAWZ0gMG8IY4DINBfXEYhN64aH'
ACCESS_TOKEN_SECRET = '8qsTnnOwes0VgQKOx7u9XIEnS5ZK1qKNFSmK00uhSUf1Z'
CLIENT_ID = 'ZlM5NkNhRU5xRGd6eGRaWGJnYjc6MTpjaQ'
CLIENT_SECRET = 'd_UZEGCMsJ9-ABpDuj0ObDRa43uiTrbUXN6qsY0bizWYbHQVI9'
OAUTH_NONCE = 'VkMwenZITmwwbWZoTU1GVmpOWXpBd3pCV0tuSjZ3MWQ%3D'
'''

from my_data import *
import os
import requests
import json


'''
def create_tweet(message):

    url = "https://api.twitter.com/2/tweets"

    payload = json.dumps({
      "text": message
    })
    
    headers ={
        "authorization": "OAuth oauth_consumer_key=CONSUMER_KEY, oauth_token=ACCESS_TOKEN_KEY, oauth_nonce=VkMwenZITmwwbWZoTU1GVmpOWXpBd3pCV0tuSjZ3MWQ%3D, oauth_signature_method=HMAC-SHA1, oauth_version=1.0, oauth_timestamp=1694930514, oauth_signature=1Gmj%2B5C3Zkk4ITxBPYwJDPfaCKU%3D",
       "content-type": "application/json",
        "host": "api.twitter.com",
      }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    return json.loads(response.text)["data"]["id"]   
'''

#print(create_tweet("test_5"))


import requests
import json
from requests_oauthlib import OAuth1Session

url = 'https://api.twitter.com/2/tweets'
#auth = OAuth1(consumer_key, consumer_secret, access_token_key, access_token_secret)
oauth = OAuth1Session(CONSUMER_KEY,
                            client_secret=CONSUMER_SECRET,
                            resource_owner_key=ACCESS_TOKEN_KEY,
                            resource_owner_secret=ACCESS_TOKEN_SECRET)

message = "test_7"

payload = json.dumps({
      "text": message
    })

print(oauth.post(url=url, data=payload))
