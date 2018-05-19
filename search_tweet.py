# get a original tweet by a reply_id of a tweet
#
from twitter_oauth import access_key, access_secret, consumer_key, consumer_secret
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# WIP/to-do: reply_tweet


# Open/Create a file to append data
csvFile = open('ua.csv', 'a')


def search_tweets_by_hashtag():
    for tweet in tweepy.Cursor(api.search, q="#unitedAIRLINES", lang="en").items():
        # WIP/to-do: write to file
        #csvWriter.writerow([status.created_at, status.id_str, status.in_reply_to_user_id_str, status.text.encode('utf-8')])
        print(status.created_at, status.id_str, status.in_reply_to_user_id_str, status.text)
        return


def search_tweets_by_id():
    id_of_tweet = "806179924407107585"
    tweet = api.get_status(id_of_tweet)
    print(tweet.text)
    return
