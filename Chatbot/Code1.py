from typing import re

import nltk
import numpy as np
import pandas as pd
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
np.set_printoptions(threshold=np.nan)

f = open('ChatbotWikipedia.txt', 'r')

rawText = f.read().lower()

"""
print('Downloading punkt')
nltk.download('punkt')

print('Downloading wordnet')
nltk.download('wordnet')
"""

sentence_tokens = nltk.sent_tokenize(rawText, language='english')
word_tokens = nltk.word_tokenize(rawText, language='english')

print(sentence_tokens[:3])
print(word_tokens[:10])

lemmer = nltk.stem.WordNetLemmatizer()


def lemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


removePunctDict = dict((ord(punct), None) for punct in string.punctuation)


def lemNormalize(text):
    return nltk.word_tokenize(text.lower().translate(removePunctDict))


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "Namaste"]

def greeting():
    return random.choice(GREETING_RESPONSES)

def respond(user_input):
    robo_response = ''
    TfIdfVec = TfidfVectorizer(tokenizer=lemNormalize, stop_words='english')
    tfidf = TfIdfVec.fit_transform(sentence_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sentence_tokens[idx]
        return robo_response

flag = True

print('Start')

while flag:
    user_input = input('').lower()
    if user_input != 'bye':
        if user_input in GREETING_INPUTS:
            print('>>:', greeting())
        else:
            sentence_tokens.append(user_input)

            word_tokens += nltk.word_tokenize(user_input)
            final_words = list(set(word_tokens))
            print('>>>:', respond(user_input))
            sentence_tokens.remove(user_input)
    else:
        flag = False
        print('Bye. :) See you l8r')


print('Done')