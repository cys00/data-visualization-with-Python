#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:10:40 2018

@author: yusheng
"""
from twython import TwythonStreamer
#import sys
import json

tweets = []

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'lang' in data and data['lang'] == 'en':
            tweets.append(data)
            print('received tweet #',len(tweets),data['text'][:100])

        if len(tweets) >= 10000:
            self.store_json()
            self.disconnect()
            
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()
    
    def store_json(self):
        with open('tweet_stream_Seattle_{}.json'.format(len(tweets)),'w')as f:
            json.dump(tweets, f, indent=4)
            
if __name__ == '__main__':
    with open('/Users/yusheng/Documents/Python/yusheng_twitter_credentials.json','r') as f:
        credentials = json.load(f)
        
    CONSUMER_KEY = credentials['CONSUMER_KEY']
    CONSUMER_SECRET = credentials['CONSUMER_SECRET']
    ACCESS_TOKEN = credentials['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']
    
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    #if len(sys.argv) > 1:
        #keyword = sys.argv[1]
    #else:
        #keyword = 'apple'
    stream.statuses.filter(track='Seattle')
    