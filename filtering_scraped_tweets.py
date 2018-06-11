import os
import glob
import emoji
import re


path = 'C:\\Users\\Wilm Hanke\\Documents\\GitHub\\twitter_stream\\tweet files'

filtered_tweets = "C:\\Users\\Wilm Hanke\\Documents\\GitHub\\twitter_stream\\filtered_tweets.txt"

"""
1. datei öffnen
2. jeden tweet/zeile nehmen
    a. schauen ob er ein emoji beinhaltet
    b. wenn ja: in seperate datei speichern
3.
"""


def prepare_tweet_file():
    # wenn zeile mit \n startet -> \n löschen
    # wenn zeile == \n -> \n löschen
    for filename in glob.glob(os.path.join(path, '*.txt')):
        newfile = filename + '_strip.txt'
        with open(filename, encoding="utf-8") as f:
            for line in f:
                with open(newfile, "a", encoding="utf-8") as newf:
                    newf.write(line.strip('\n'))


def prepare_one_special_tweet_file(f_name):
    # wenn zeile mit \n startet -> \n löschen
    # wenn zeile == \n -> \n löschen
    filename = f_name
    newfile = filename + '_strip.txt'
    with open(filename, 'r+', encoding="utf-8") as f:
        for line in f:
            with open(newfile, 'a', encoding='utf-8') as newf:
                newf.write(line.strip('\n'))


def prepare_one_special_tweet_file2(f_name):
     # "2018-05-26 21:34:58","1000490499814420480","","#WhereAreTheChildren https://t.co/1k4014bXRs"
     # --> "","",""
     # --> matchObj = re.match(r'"2018-05-\d\d \d\d:\d\d:\d\d","\d*","\d*",".*"')
    filename = f_name
    newfile = filename + '_strip2.txt'
    pattern = re.compile(r'"2018-05-\d\d \d\d:\d\d:\d\d","\d*","\d*","(\b|.)*"', re.UNICODE)
    with open(filename, 'r+', encoding="utf-8") as f:
        for line in f:
            matches = pattern.finditer(line)
            with open(newfile, 'a', encoding='utf-8') as newf:
                for match in matches:
                    #newf.write(match.group() + '\n')
                    print(match.group())


def seperate_one_special_tweet_file(f_name):
    filename = f_name
    newfile = filename + '_split.txt'
    with open(filename, 'r+', encoding="utf-8") as f:
        for line in f:
            with open(newfile, 'a', encoding='utf-8') as newf:
                for element in line.split('""'):
                    newf.write(element)


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


def append_char(filename):
    with open(filename, "a", encoding="utf-8") as f:
        for line in f:
            ''.join(line, "\"")


# append_char(filtered_tweets)
# get_tweets_w_emoji()
# prepare_tweet_file()
#seperate_one_special_tweet_file('C:\\Users\\Wilm Hanke\\Documents\\GitHub\\twitter_stream\\tweet files\\tweets-2018-05-26.txt_strip.txt')

prepare_one_special_tweet_file2('C:\\Users\\Wilm Hanke\\Documents\\GitHub\\twitter_stream\\tweet files\\tweets-2018-05-26.txt_strip.txt')  # funktionert -> file wird in eine einzige zeile geschrieben
