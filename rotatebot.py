# coding: utf-8

from tweepy import *
from requests_oauthlib import OAuth1Session
import json
import os
import random
import datetime
import base64
import sys
import urllib
import cv2

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


img = cv2.imread('tokei.jpeg')
#高さを定義
height = img.shape[0]
#幅を定義
width = img.shape[1]
#回転の中心を指定
center = (int(width/2), int(height/2))
#回転角を指定
angle = 45.0
#スケールを指定
scale = 1.0
#getRotationMatrix2D関数を使用
trans = cv2.getRotationMatrix2D(center, angle , scale)
#アフィン変換
image2 = cv2.warpAffine(img, trans, (width, height))

cv2.imwrite('out.jpg', image2)

try:
  api.update_profile_image('out.jpg')
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
