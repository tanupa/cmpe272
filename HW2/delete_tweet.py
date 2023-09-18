consumer_key=""
consumer_secret = ""
access_token =""
access_token_secret = ""

import requests
from requests_oauthlib import OAuth1Session
import json

class DeleteTweet:
  def delete(id):
    oauth = OAuth1Session(
    client_key=consumer_key,
    client_secret = consumer_secret,
    resource_owner_key = access_token,
    resource_owner_secret = access_token_secret,
    )

    response = oauth.delete(f"https://api.twitter.com/2/tweets/{id}")

  def test_delete_tweet(self):
    tweet_id_to_delete = "insert number here"
    deleting_tweet_id = DeleteTweet.deleting_tweet(tweet_id_to_delete)
    self.assertEqual(deleting_tweet_id, tweet_id_to_delete, "Tweet deletion failed")

