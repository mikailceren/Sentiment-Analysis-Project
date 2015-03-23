#!/usr/bin/env python
# coding: utf-8

import tweepy

import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        
        decoded = json.loads(data)
        
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Showing all tweets for #BeyazFutbolaDiyorumki:"

    stream = tweepy.Stream(auth, l)
    stream.filter(track=['BeyazFutbolaDiyorumki'])
