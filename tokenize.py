# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:45:38 2020

@author: nzubair
"""

from nltk.tokenize import sent_tokenize
text="Today is a great day. It is even better than yesterday. And yesterday was the best day ever."
print (sent_tokenize(text))

tokens = nltk.tokenize.word_tokenize(text)
print (tokens)

tagged = nltk.pos_tag(tokens)
print (tagged)