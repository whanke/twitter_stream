# Twython.
# by Tatjana Scheffler
# A simple example script for corpus collection from Twitter using Tweepy https://github.com/tweepy

import sys
import tweepy
import langid
import csv
import codecs
from urllib3.exceptions import ConnectionError
from twitter_oauth import access_key, access_secret, consumer_key, consumer_secret

import time
from datetime import date


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


# open log file
logfile = open('twython.log', 'a')


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        global old_date
        global writer
        global outfile
        new_date = date.today()
        if not new_date == old_date:
            outfile.close
            outfile = codecs.open("tweets-" + str(new_date) + ".txt", "ab", encoding="utf-8")
            writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
            old_date = new_date
        try:
            lang = langid.classify(status.text)[0]
            if lang == "en":
                if not status.text.startswith('RT'):  # forget all the Retweets
                    writer.writerow((status.created_at, status.id_str, status.in_reply_to_status_id_str, status.text.replace('\n', ' ').replace('\r', '')))
        except Exception:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            sys.exc_clear()
#                pass

    def on_error(self, status_code):
        logfile.write(str(time.asctime(time.localtime(time.time()))) + ' Encountered error with status code:' + str(status_code) + "\n")
        return True  # Don't kill the stream

    def on_timeout(self):
        logfile.write(str(time.asctime(time.localtime(time.time()))) + ' Timeout...' + "\n")
        return True  # Don't kill the stream

    # def on_data(self, data):
    #     print data
    #     return True


localtime = time.asctime(time.localtime(time.time()))
logfile.write(localtime + " Tracking terms from ../twython-keywords.txt\nStarting stream \n" + str([line.strip() for line in open('twython-keywords.txt', encoding="utf-8")]))

# longer timeout to keep SSL connection open even when few tweets are coming in
stream = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=1000.0)

terms = [line.strip() for line in open('twython-keywords.txt', encoding="utf-8")]
emoji_check = []

# open output file
old_date = date.today()
outfile = codecs.open("tweets-" + str(old_date) + ".txt", "ab", "utf-8")
writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')

while True:
    try:
        stream.filter(track=terms)
    except ConnectionError:
        # avoid: urllib3.exceptions.ProtocolError: ('Connection broken: IncompleteRead(0 bytes read)', IncompleteRead(0 bytes read))
        print('ConnectionError on ' + str(time.asctime(time.localtime(time.time()))))
        logfile.write(str(time.asctime(time.localtime(time.time()))) + ' ConnectionError...' + "\n")
        continue
