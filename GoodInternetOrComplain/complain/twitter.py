from twitter import *
import json
from config import config

def complainOnTwitter(data):
    try:
        #Define the message for the ISP provider
        downspeed = str(round((round(data['download']) / 1048576), 2)) + " Mb/s"
        upspeed = str(round((round(data['upload']) / 1048576), 2)) + " Mb/s"
        ping = str(round(data['ping'], 2)) + " ms"
        
        message = "La velocidad de mi conexión es:\r\n-Bajada: " + downspeed + "\r\n-Subida: " + upspeed + "\r\n-Ping: " + ping + "\r\nDetalle: " + data['png_url']

        #Create the Twitter wrapper and attach the screenshot of the speedtest
        t = Twitter(auth=OAuth(config.twitterAPI_oAuthToken, config.twitterAPI_oAuthSecret, config.twitterAPI_appClientID, config.twitterAPI_appClientSecret))
        tweet = t.statuses.update(status=message)
        if 'id' in  tweet:
            data['tweet_id'] = tweet['id']
    except Exception as err:        
        print(f'Error occurred: {err}')
