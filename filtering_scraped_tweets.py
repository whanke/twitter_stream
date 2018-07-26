# -*- coding: utf-8 -*-
import os
import glob
import emoji
import re


path = 'C:\\Users\\Wilm Hanke\\Documents\\GitHub\\twitter_stream\\tweet_files'

filtered_tweets = "C:\\Users\\Wilm Hanke\\Documents\\GitHub\\twitter_stream\\filtered_tweets.txt"

"""
1. datei öffnen
2. jeden tweet/zeile nehmen
    a. schauen ob er ein emoji beinhaltet
    b. wenn ja: in seperate datei speichern
3.
"""


def strip_tweet_files():
    # in datei werden alle '\n' gelöscht
    for filename in glob.glob(os.path.join(path, '*.txt')):
        newfilepath = filename + '_strip.txt'
        with open(filename, encoding="utf-8") as f:
            with open(newfilepath, "a", encoding="utf-8") as newf:
                for line in f:
                    newf.write(line.strip('\n'))


def set_rows_on_tweet_files():
    # Transformation in eine einheitliche Formatierung: pro Zeile ein Tweet --> lesbar für pandas Library
    for filename in glob.glob(os.path.join(path, '*_strip.txt')):
        newfile = filename + '_set_rows.txt'
        with open(filename, 'r+', encoding="utf-8") as f:
            pattern = re.compile(r'"2018-0\d-\d\d \d\d:\d\d:\d\d","\d*","\d*","(\b|.)*"') # r'"2018-0.*","\d*","\d?",".*"'
            matches = pattern.finditer(f.read())
            with open(newfile, 'a', encoding='utf-8') as newf:
                for match in matches:
                    tweet = match.group()
                    newf.writelines(tweet + '\n')


def get_tweets_w_emoji():
    # nimmt alle dateien aus einem ordner und schreibt die tweets in neue datei
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(filename, encoding="utf-8") as f:
            for tweet in f:
                count_emoji = 0
                for char in tweet:
                    if char in emoji.UNICODE_EMOJI:
                        count_emoji += 1
                if count_emoji >= 1:
                    with open(filtered_tweets, 'a', encoding="utf-8") as f2:
                        f2.write(tweet + "\n")


def concat_tweet_files():
    path2 = 'C:\\Users\\Wilm Hanke\\Documents\\GitHub\\twitter_stream\tweet_files'
    for filename in glob.glob(os.path.join(path2, '*rows.txt')):
        newfile = 'concat_all_tweets_2.txt'
        with open(filename, encoding="utf-8") as f:
            with open(newfile, "a", encoding="utf-8") as newf:
                for line in f:
                    newf.write(line.strip('\n'))


#strip_tweet_files()
#set_rows_on_tweet_files()
concat_tweet_files()
