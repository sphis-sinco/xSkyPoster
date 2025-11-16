import backend, json

twitter_api = backend.x_api
bluesky_client = backend.bluesky_client

post_name = input("What's the post name?\n> ")
post = json.loads(open("_posts/" + post_name + ".json").read())

print('"' +post["text"]+ '"')

if input("Are you sure you want to post this? (y/n)\n> ") == "y":
    if not (post["image"] == None) and not (post["image"]["path"] == None):
            with open('_posts/resources/' + post["image"]["path"], 'rb') as media:
                img_data = media.read()
                
                resp = twitter_api.upload_media_simple(media=img_data)
                print(resp)
                
                if not (post["image"]["alt"] == None):
                    twitter_api.create_tweet(text=post["text"], media=resp)
                    bluesky_client.send_image(text=post["text"], image=img_data, image_alt=post["image"]["alt"])
                else:
                    twitter_api.create_tweet(text=post["text"], media=resp)
                    bluesky_client.send_image(text=post["text"], image=img_data)
    else:
        twitter_api.create_tweet(text=post["text"])
        bluesky_client.send_post(post["text"])