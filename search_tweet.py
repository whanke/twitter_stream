# get a original tweet by a reply_id of a tweet
#
from twitter_oauth import access_key, access_secret, consumer_key, consumer_secret
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

id_of_tweet = "473447672"

tweet = api.get_status(id_of_tweet)
print(tweet.text)