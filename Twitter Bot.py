import sys
import random
import os
import tweepy

auth = tweepy.OAuthHandler('')
auth.set_access_token('')
print("program run")
api = tweepy.API(auth)
results = api.search(q="FT: from:AFL")
Timeline = api.user_timeline()
for result in results:
    tweetfound = False
    #prints tweet to screen 
    print(result.text)
    #check if tweet has already been sent
    for pasttweets in Timeline:
        if result.text == pasttweets.text:
            tweetfound = True
    #if tweet is not already been a status update will be made
    if tweetfound == False:
        api.update_status(result.text)

