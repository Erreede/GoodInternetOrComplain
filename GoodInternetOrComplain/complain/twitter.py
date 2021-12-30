from twitter import *
import json
from config import config

def complainOnTwitter(data):
    try:
        #Define the message for the ISP provider
        hired_bandwidth = 1000
        hired_bandwidth_str = "1 Gb/s simétricos"
        downspeed =  round((round(data['download']) / 1048576), 2)
        downspeed_str = str(downspeed) + " Mb/s"
        downspeed_quality = str(round(100 * float(downspeed)/float(hired_bandwidth), 2)) + "%"
        upspeed = round((round(data['upload']) / 1048576), 2)
        upspeed_str = str(upspeed) + " Mb/s"
        upspeed_quality = str(round(100 * float(upspeed)/float(hired_bandwidth), 2)) + "%"
        ping = str(round(data['ping'], 2)) + " ms"
        
        message = "La velocidad de mi conexión es:\r\n-Bajada: " + downspeed_str + "\r\n-Subida: " + upspeed_str + "\r\n-Ping: " + ping + "\r\n\r\nDetalle: " + data['png_url'] + "\r\n\r\nContratado: " + hired_bandwidth_str + ", lo que supone un " + downspeed_quality + " de la bajada y un " + upspeed_quality + " de la subida."

        #Create the Twitter wrapper and attach the screenshot of the speedtest
        t = Twitter(auth=OAuth(config.twitterAPI_oAuthToken, config.twitterAPI_oAuthSecret, config.twitterAPI_appClientID, config.twitterAPI_appClientSecret))
        tweet = t.statuses.update(status=message)
        if 'id' in  tweet:
            data['tweet_id'] = tweet['id']
    except Exception as err:        
        print(f'Error occurred: {err}')
