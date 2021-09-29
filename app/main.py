"""
  Marley Collins
  Radical Software, Fall 2021
  Project 1
  Sept 30, 2021
  python3
"""

import tweepy

from authorization_tokens import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

import random

# MadLib affirmation bot
string_template_list = [ "You are deserving of {}, regardless of {}.",
                         "You deserve {}, even if you {}.",
                         "You are just as deserving of {} when you don't {} as when you do." ]

string_template = random.choice(string_template_list)

word_list1 = [ "love", "affection", "respect", "happiness", "joy", "kindness" ]
word_list2 = [ "your weight", "what you ate today", "your appearance",
               "how your pants fit today", "how your clothes fit",
               "how much you ate today", "how much you exercise"]
word_list3 = [ "relapse", "don't exercise today", "can't exercise today",
               "binge today", "don't feel comfortable in your body today",
               "overeat"]
word_list4 = [ "exercise", "feel confident in your appearance", "take perfect care of yourself",
               "have it all together" ]


word1 = random.choice(word_list1)

if string_template == "You are deserving of {}, regardless of {}.":
    word2 = random.choice(word_list2)
elif string_template == "You deserve {}, even if you {}.":
    word2 = random.choice(word_list3)
elif string_template == "You are just as deserving of {} when you don't {} as when you do.":
    word2 = random.choice(word_list4)

message = string_template.format(word1,word2)

api.update_status(message)
print("Done.")
