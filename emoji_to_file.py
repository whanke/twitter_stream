# writes emoji as aliases and pictures to a txt file named "twython-keywords.txt" 
# using in twitter stream to filter tweets

import emoji

def write_aliases_to_file(filename):
	for e in emoji.EMOJI_UNICODE: 
		with open(filename, "a+", encoding = "utf-8") as f:
			f.write(e + "\n")


def write_emoji_pic_to_file(filename):
	for e in emoji.EMOJI_UNICODE:
		emoji_pic = emoji.emojize(e)
		with open(filename, "a+", encoding = "utf-8") as f:
			f.write(emoji_pic + "\n")

write_emoji_pic_to_file("twython-keywords.txt")