# get a original tweet by a reply_id of a tweet
#
from twitter_oauth import access_key1, access_secret1, consumer_key1, consumer_secret1
import tweepy
import pandas as pd
import json
import datetime
import csv
import codecs
from twython import Twython


auth = tweepy.OAuthHandler(consumer_key1, consumer_secret1)
auth.set_access_token(access_key1, access_secret1)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# WIP/to-do: reply_tweet


# Open/Create a file to append data
#csvFile = open('ua.csv', 'a')

def get_tweets_by_hashtag_twython():
    tw = Twython(app_key=consumer_key1,
                 app_secret=consumer_secret1,
                 oauth_token=access_key1,
                 oauth_token_secret=access_secret1)

    search = tw.search(q='#RoyalWedding',  # **supply whatever query you want here**
                       count=100)
    tweets = search['statuses']

    save_file = codecs.open("C:\\Users\\Wilm Hanke\\Documents\\GitHub\\twitter_stream\\tweets-hashtag-RoyalWedding-2018-05-19.txt", "ab", encoding="utf-8")
    writer = csv.writer(save_file, quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
    for tweet in tweets:
        writer.writerow((tweet['created_at'], tweet['id_str'], tweet['in_reply_to_user_id_str'], tweet['text'], '\n'))
        return True


def get_tweets_by_hashtag(hashtag):
            # lädt nur ein tweet per query
    tweetCount = 0
    maxTweets = 3000000
    tweetsPerQry = 100
    save_file = codecs.open("C:\\Users\\Wilm Hanke\\Documents\\GitHub\\twitter_stream\\tweets-hashtag-RoyalWedding-2018-05-19.txt", "ab", encoding="utf-8")
    writer = csv.writer(save_file, quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
    while tweetCount < maxTweets:
        for tweet in tweepy.Cursor(api.search, q=hashtag, count=tweetsPerQry, lang="en", since='2018-05-19', max='2018-05-20').items(1000000):
            # schreibt nur eine reihe / einen tweet !!!!!!!!!!!!!
            if not tweet.text.startswith("RT"):
                writer.writerow((tweet.created_at, tweet.id_str, tweet.in_reply_to_user_id_str, tweet.text.encode('utf-8')))
            # print(status.created_at, status.id_str, status.in_reply_to_user_id_str, status.text)
            return (print("Downloaded {0} tweets".format(tweetCount)))


def get_raw_tweet():
    filepath = "C:\\Users\\Wilm Hanke\\Documents\\GitHub\\twitter_stream\\tweets-2018-05-19.txt"
    for line in open(filepath, encoding='utf-8'):
        yield json.loads(line)


def get_tweet_in_reply_to_user_id_str():
    tweet = get_raw_tweet()
    df = pd.DataFrame(tweet)
    # df["in_reply_to_user_id_str"]
    # reply_id =  # dataframe identifying reply_id
    return reply_id


def search_tweets_by_id():
    id_of_tweet = "806179924407107585"
    tweet = api.get_status(id_of_tweet)
    print(tweet.text)
    return


get_tweets_by_hashtag_twython()
