# get a original tweet by a reply_id of a tweet
#
from twitter_oauth import access_key, access_secret, consumer_key, consumer_secret

twitter = Twython(
    consumer_key, consumer_secret,
    access_key, access_secret)

id_of_tweet = "899143901927268352"

tweet = twitter.show_status(id=id_of_tweet)
print(tweet['text'])
