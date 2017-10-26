import tweepy
from Senses.stt import listen
from Senses.tts import say

consumer_key = 'ePwNSaFxX9PghCkcJGmTnyjjZ'
consumer_secret = 'Yu307s1NkO7lr9Yszr3GftFVPSalLAZlQwuFui7ZCX6DltbqHT'
access_token = '269667930-xyROxqWoDg46qvPGFYVVLwpjphGpNStNYBnQqBf3'
access_token_secret = '1RTgc7alg8KgfkZnrAiTMoPgdnr5Wxw3aljxPFqDioBDt'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


triggers = {

'tweet':[['send','tweet']]

}

def tweet(s):
    say("What should i tweet?")
    tweet = listen()
    api.update_status(status= tweet)
    return "Tweet Sent"








