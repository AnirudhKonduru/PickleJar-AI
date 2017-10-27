import tweepy
from Senses.input import listen
from Senses.output import say

consumer_key = 'ePwNSaFxX9PghCkcJGmTnyjjZ'
consumer_secret = 'Yu307s1NkO7lr9Yszr3GftFVPSalLAZlQwuFui7ZCX6DltbqHT'
access_token = '269667930-xyROxqWoDg46qvPGFYVVLwpjphGpNStNYBnQqBf3'
access_token_secret = '1RTgc7alg8KgfkZnrAiTMoPgdnr5Wxw3aljxPFqDioBDt'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)




triggers = {
<<<<<<< HEAD

'tweet':[['send','tweet']],
'read_tweet':[['read', 'tweet']]

=======
    'tweet': [['send', 'tweet']]
>>>>>>> 6518d5df16998ef9085d0f83d571593500aace5b
}


def tweet(s):
    say("What should i tweet?")
    tweet_text = listen()
    api.update_status(status=tweet_text)
    return "Tweet Sent"


def read_tweet(s):
    mentions = api.mentions_timeline(count=1)

    for mention in mentions:
        a = mention.text
        b = mention.user.screen_name
        c = mention.id

    print(c)

    say("your last tweet is "+a +" by "+b)

    say("Do you want me to reply?")
    choice = listen()

    if choice == "yes":

        say("What should i tweet?")
        text = listen()
        tweet = "@" + b + " " + text

        api.update_status(tweet, c)
        return "Tweet Sent"




    return "tweet read."










