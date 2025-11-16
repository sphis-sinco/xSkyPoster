import tweepy

consumer_key = open("consumer_key.txt")
consumer_secret = open("consumer_secret.txt")
access_token = open("access_token.txt")
access_token_secret = open("access_token_secret.txt")

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)