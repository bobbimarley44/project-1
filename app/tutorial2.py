import tweepy

consumer_key = "gO4uS9FcgbwiFR6rKUtjrRi83"
consumer_secret = "1yoN1hz30tetGHb9ofXf9c2fwLkcF9N7OmNaIfCmG5VotYVanJ"

access_token = "1297695443179188225-1ZlsVs00Af6A0oe8IcrmJotJAcCdm3"
access_token_secret = "f2dTQToJTTyxjta1Am1uE2NBIzzkwHSDEsuEnT7pvrdE8"

import random


# # Option 1: Select a message randomly from a list of messages
# phrase_list = ["Howdy partner.", "Hey there cowboy.", "Howdy cowgirl."]
#
# message = random.sample(phrase_list, k=1)


# Option 2: A simple Mad Lib

# string_template = "Some people want {} but I just want {}."
# word_list = ["sadness", "coffee grounds", "a sink", "life", "happiness",
# "Y2K aesthetics", "emotions"]
#
# word1 = random.choice(word_list)
# word2 = random.choice(word_list)
#
# message = string_template.format(word1,word2)


# Option 3: A list of possible Mad Libs
# template_list = [ "I like to think I'm {} but really I'm just {}.",
#                   "People say I'm {} but I'm really just {}.",
#                   "I am {} only when I'm {}." ]
#
# word_list1 = [ "mean", "caring", "aggressive", "upset" ]
# word_list2 = [ "John Cena", "Mark Ruffalo", "Dr. Scott" ]
#
# template = random.choice(template_list)
#
# word1 = random.choice(word_list1)
# word2 = random.choice(word_list2)
#
# message = template.format(word1,word2)

# Option 4: Using IF statements
# string_template = "Hi, I'm {}, master of {}."
#
# word_list1 = [ "FrankNFurter", "Dr. Scott" ]
#
# word_list2_a = [ "science", "horror", "biochemical research", "Rocky", "committing crimes" ]
# word_list2_b = [ "intruding", "the zen room", "Eddy", "Brad"]
#
# word1 = random.choice(word_list1)
#
# if word1 == "FrankNFurter":
#     word2 = random.choice(word_list2_a)
# elif word1 == "Dr. Scott":
#     word2 = random.choice(word_list2_b)

# message = string_template.format(word1,word2)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print("Done.")
