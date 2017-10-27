#import pickle
#pickle.init()
#from Senses.input import listen
#from Senses.output import say
from process import process
import time


import tweepy
import re

consumer_key = 'ePwNSaFxX9PghCkcJGmTnyjjZ'
consumer_secret = 'Yu307s1NkO7lr9Yszr3GftFVPSalLAZlQwuFui7ZCX6DltbqHT'
access_token = '269667930-xyROxqWoDg46qvPGFYVVLwpjphGpNStNYBnQqBf3'
access_token_secret = '1RTgc7alg8KgfkZnrAiTMoPgdnr5Wxw3aljxPFqDioBDt'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

print("----1----")
mention = api.mentions_timeline(count=1)[0]
a = mention.text
b = mention.user.screen_name
c = mention.id
print("----2----")

while True:
    print("Waiting...")
    time.sleep(1)
    mention = api.mentions_timeline(count=1)[0]
    new_id = mention.id
    new_screenName = mention.user.screen_name
    
    if (new_id != c):
        ip = mention.text
        print("recieved: "+ip)
        ip = re.sub(r'#\w+ ?', '', ip)
        ip = re.sub(r'http\S+ ?', '', ip)
        ip = re.sub(r'@\w+ ?', '', ip)
        print("processed: "+ip)
        response = process(ip)

        if response is None:
            response = "Could not understand "+mention.text

        tweet = "@" + new_screenName + " " + response
        reply_tweet = api.update_status(tweet, new_id)
        c = reply_tweet.id
        print("New Tweet")