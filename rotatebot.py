# coding: utf-8

from tweepy import *
from requests_oauthlib import OAuth1Session
import json
import os
import random
import datetime
import base64
import sys

def get_oauth():
	consumer_key = os.environ["CONSUMER_KEY"]
	consumer_secret = os.environ["CONSUMER_SECRET"]
	access_key = os.environ["ACCESS_TOKEN_KEY"]
	access_secret = os.environ["ACCESS_TOKEN_SECRET"]
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	return auth

auth = get_oauth()
api = API(auth)

try:
  api.update_profile_image('tokei3.jpeg')
except:
  print("a")
  # print("error response code: " + str(e.response.status))
  # print("error message: " + str(e.response.reason))

# twitter = OAuth1Session(os.environ["CONSUMER_KEY"],  os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])

# img_file = 'tokei3.jpeg'
# b64 = base64.encodestring(open(img_file, 'rb').read())

# print(b64)

# params = {"image": b64}
# res = twitter.post("https://api.twitter.com/1.1/account/update_profile_image.json", params = params)

# print(res.status_code)
