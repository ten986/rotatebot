# coding: utf-8

from tweepy import *
from requests_oauthlib import OAuth1Session
import json
import os
import random
from datetime import datetime, timedelta
import base64
import sys
import urllib
import cv2
import math

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
DIFF_JST_FROM_UTC = 9
time = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
angle = (time.hour + time.minute / 60.0+ time.second / 3600.0) * -30.0
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
