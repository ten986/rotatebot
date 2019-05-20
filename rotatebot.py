# coding: utf-8

from requests_oauthlib import OAuth1Session
import json
import os
import random
import datetime
import base64

twitter = OAuth1Session(os.environ["CONSUMER_KEY"],  os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])

img_file = 'tokei3.jpeg'
b64 = base64.encodestring(open(img_file, 'rb').read())

print(b64)

params = {"image": open(img_file, 'rb').read()}
res = twitter.post("https://api.twitter.com/1.1/account/update_profile_image.json", params = params)

print(res.status_code)
