from twython import Twython





from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)
    
twitter = Twython(consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)

 





photo = open("/home/pi/Downloads/trump.jpeg", "rb")

response = twitter.upload_media(media=photo)
twitter.update_status(status="TRUMP 2052",media_ids=[response["media_id"]])
