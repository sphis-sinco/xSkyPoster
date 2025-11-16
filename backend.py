import tweepy
from atproto import Client

x_consumer_key = open("x/consumer_key.txt")
x_consumer_secret = open("x/consumer_secret.txt")
x_access_token = open("x/access_token.txt")
x_access_token_secret = open("x/access_token_secret.txt")

x_auth = tweepy.OAuth1UserHandler(
    x_consumer_key, x_consumer_secret, x_access_token, x_access_token_secret
)

x_api = tweepy.API(x_auth)

public_tweets = x_api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

bluesky_client = Client()
bluesky_client.login(open("bluesky/identifier.txt"), open("bluesky/password.txt"))