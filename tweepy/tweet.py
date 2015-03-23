# -*- coding: utf-8 -*-
import tweepy
import time
from tweepy import OAuthHandler
from tweepy import Cursor


consumer_key = ''
consumer_secret = ''
atoken = ''
asecret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

MarSec = tweepy.Cursor(api.search, q='BeyazFutbolaDiyorumki').items(100)

for tweet in MarSec:
    print " "
    print tweet.created_at, tweet.text.encode('utf-8'), tweet.lang.encode('utf-8')

saveFile = open('MarSec.csv', 'a')
for tweet in MarSec:
    print " "
    print tweet.created_at, tweet.text, tweet.lang
    saveFile.write("%s %s %s\n"%(tweet.created_at, tweet.lang, tweet.text))

saveFile.close()