import os

import twitter

from sys import argv


# Use Python os.environ to get at environmental variables
#ls
# Note: you must run `source secrets.sh` before running this file
# to make sure these environmental variables are set.

from markovgenerator import TweetableMarkovGenerator

tweet = TweetableMarkovGenerator()
# print "TweetableMarkovGenerator"
# print tweet.make_text(tweet.make_chains(argv)), len(tweet.make_text(tweet.make_chains(argv)),)

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# This will print info about credentials to make sure they're correct
print api.VerifyCredentials()

# Send a tweet
status = api.PostUpdate(tweet.make_text(tweet.make_chains(argv)))
print status.text