#Done by Ben Kwon - delete-tweet and Flask back-end
from flask import Flask

app = Flask(__name__)

consumer_key=""
consumer_secret = ""
access_token =""
access_token_secret = ""

import requests
from requests_oauthlib import OAuth1Session
import json

@app.route('/create-tweet/<text>', methods=["POST"])
def create_tweet(text):

  oauth = OAuth1Session(
    client_key=consumer_key,
    client_secret = consumer_secret,
    resource_owner_key = access_token,
    resource_owner_secret = access_token_secret,
  )

  data = {"text": text}

  response = oauth.post("https://api.twitter.com/2/tweets", json=data)

  resJson = response.json()

  if "status" in resJson and resJson['status'] == 403:
    return "", 403
  if "data" in resJson:
    return resJson, 202

@app.route('/delete-tweet/<id>', methods=["DELETE"])
def delete_tweet(id):
  oauth = OAuth1Session(
  client_key=consumer_key,
  client_secret = consumer_secret,
  resource_owner_key = access_token,
  resource_owner_secret = access_token_secret,
  )

  response = oauth.delete(f"https://api.twitter.com/2/tweets/{id}")

  resJson = response.json()

  if "data" in resJson and resJson['data']['deleted'] == True:
    return "", 204
  else:
    return resJson
