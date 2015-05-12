# -*- coding: utf-8 -*-
#I used this code to aggregate tweets.
import simplejson as json
import tweepy

config = {
	"consumer_key": "",
	"consumer_secret" : "",
	"access_token": "",
	"access_token_secret": ""
}

auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])
api = tweepy.API(auth)

def getByHashtags(str):
    items = tweepy.Cursor(api.search, q=str).items(100)
    for item in items:
	    #print  json.dumps(item.text)
        print item.text.encode('utf-8')
		
getByHashtags('AKP')
