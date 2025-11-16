from pytwitter import Api as TwitterApi
from atproto import Client

x_consumer_key = open("x/consumer_key.txt").read()
x_consumer_secret = open("x/consumer_secret.txt").read()
x_access_token = open("x/access_token.txt").read()
x_access_token_secret = open("x/access_token_secret.txt").read()

x_api = TwitterApi(
    consumer_key=x_consumer_key, 
    consumer_secret=x_consumer_secret, 
    access_token=x_access_token, 
    access_token_secret=x_access_token_secret
)

bluesky_client = Client()
bluesky_client.login(open("bluesky/identifier.txt").read(), open("bluesky/password.txt").read())