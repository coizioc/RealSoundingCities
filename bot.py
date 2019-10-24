from time import sleep

import tweepy

from config import auth
from get_city import get_city

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
    while True:
        tweet = get_city()
        print(tweet)
        api.update_status(tweet)
        sleep(3600)
except:
    print("Error during authentication")
