# -*- coding: utf-8 -*-
# suggested name: tweepyFlujoArchivo
import tweepy
from tweepy.api import API

API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
key = tweepy.OAuthHandler(API_KEY, API_SECRET)
key.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

class Stream2File(tweepy.StreamListener):
    def __init__(self, api=None):
        self.api = api or API()
        self.n = 0
        self.m = 100
        self.output = open('/Users/TOSHIBA/Desktop/web mining/twitter/tweet.txt', 'w')

    def on_status(self, status):
        self.output.write(status.text.encode('utf8') + "\n")
        self.n = self.n+1
        if self.n < self.m: return True
        else:
            self.output.close()
            print 'tweets = '+str(self.n)
            return False

stream = tweepy.streaming.Stream(key, Stream2File())
stream.filter(track=['en'], languages=['tr'])