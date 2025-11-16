import backend, json

twitter_api = backend.x_api
bluesky_client = backend.bluesky_client

post_name = input("What's the post name?\n> ")
post = json.loads(open("_posts/" + post_name + ".json").read())
