import os
from dotenv import load_dotenv
load_dotenv()

twitterAPI_oAuthToken = os.getenv('twitterAPI_oAuthToken')
twitterAPI_oAuthSecret = os.getenv('twitterAPI_oAuthSecret')
twitterAPI_appClientID = os.getenv('twitterAPI_appClientID')
twitterAPI_appClientSecret = os.getenv('twitterAPI_appClientSecret')
twitterComplain = os.getenv('twitterComplain', False) == 'True'
