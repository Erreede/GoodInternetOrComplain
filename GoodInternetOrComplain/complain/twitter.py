from twitter import *
import json
from config import config

def complainOnTwitter(data):
    try:
        t = Twitter(auth=OAuth(config.twitterAPI_oAuthToken, config.twitterAPI_oAuthSecret, config.twitterAPI_appClientID, config.twitterAPI_appClientSecret))
        message = data['png_url']
        tweet = t.statuses.update(status=message)
        if 'id' in  tweet:
            data['tweet_id'] = tweet['id']
    except Exception as err:        
        print(f'Error occurred: {err}')
