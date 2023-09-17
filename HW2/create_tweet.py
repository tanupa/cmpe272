#account_id = '1703147532623413248'
#
consumer_key = 'lgIy5gxSn8YW5lxhh3YCNPT00'
consumer_secret = 'eCccvjOrXAH0P7bafRbRLIrgebjvBKqirKbb35ZRuIHST4S0dA'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAEL5pwEAAAAA5T%2FdB86AU8nPt6k5amnaP6Y0AEM%3DW1XilzwuMTjzv6kduzjUcjAHXcWKwzqgUOg3ITSEvDpiROCYyx'
access_token_key = '1703147532623413248-E3oLFyQlnTTOwydlaTvZsEJvBPLRFn'
access_token_secret = 'FeV2Lg0ZpuUWmSAV5P2ilBS2YEKoKisG8U8md4fbjRQPU'
client_id = 'ZlM5NkNhRU5xRGd6eGRaWGJnYjc6MTpjaQ'
client_secret = 'f9-7fqSQDXbPC6KmTKFC3TbJ1X9oNeAUC_dGwjhCvPNBvfy40k'
 
import os
import requests
import json
import unittest

class Tweet:
    def create_tweet(message):

        url = "https://api.twitter.com/2/tweets"

        payload = json.dumps({
        "text": message
        })
    
        headers ={
            "authorization": "OAuth oauth_consumer_key=lgIy5gxSn8YW5lxhh3YCNPT00, oauth_token=1703147532623413248-E3oLFyQlnTTOwydlaTvZsEJvBPLRFn, oauth_nonce=VkMwenZITmwwbWZoTU1GVmpOWXpBd3pCV0tuSjZ3MWQ%3D, oauth_signature_method=HMAC-SHA1, oauth_version=1.0, oauth_timestamp=1694930514, oauth_signature=1Gmj%2B5C3Zkk4ITxBPYwJDPfaCKU%3D",
            "content-type": "application/json",
            "host": "api.twitter.com",
        }
    
        response = requests.request("POST", url, headers=headers, data=payload)
    
        return json.loads(response.text)["data"]["id"]

    def delete_tweet(tweet_id):
        url = "https://api.twitter.com/2/tweets/{tweet_id}"

        headers = {
            "authorization": "OAuth oauth_consumer_key=lgIy5gxSn8YW5lxhh3YCNPT00, oauth_token=1703147532623413248-E3oLFyQlnTTOwydlaTvZsEJvBPLRFn, oauth_nonce=VkMwenZITmwwbWZoTU1GVmpOWXpBd3pCV0tuSjZ3MWQ%3D, oauth_signature_method=HMAC-SHA1, oauth_version=1.0, oauth_timestamp=1694930514, oauth_signature=1Gmj%2B5C3Zkk4ITxBPYwJDPfaCKU%3D",
            "content-type": "application/json",
            "host": "api.twitter.com",
        }

        try:
            response = requests.delete(url, headers=headers)
         else:
            print("Deleting tweet failed")

    #print(create_tweet("test_5"))

class TestTweet(unittest.TestCase):
    def test_create_tweet(self):
        message = "test to create tweet."
        tweet_id = Tweet.create_tweet(message)
        self.assertIsNotNone(tweet_id, "Tweet creation failed")

    def test_delete_tweet(self):
        tweet_id_to_delete = "insert number here"
        deleting_tweet_id = Tweet.deleting_tweet(tweet_id_to_delete)
        self.assertEqual(deleting_tweet_id, tweet_id_to_delete, "Tweet deletion failed")


# import requests
# import json
# from requests_oauthlib import OAuth1
#
# url = 'https://api.twitter.com/2/tweets'
# auth = OAuth1(consumer_key, consumer_secret, access_token_key, access_token_secret)
# #twitter = = OAuth1Session('client_key',
# #                            client_secret='client_secret',
# #                            resource_owner_key='resource_owner_key',
# #                            resource_owner_secret='resource_owner_secret')
# message = "test_4"
# payload = json.dumps({
#      "text": message
#    })
# print(requests.request(method="POST", url=url, auth=auth, data=payload))
