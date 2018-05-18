# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 10:12:33 2018

@author: uljana
"""
import nltk
import math
from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict


sentences = reuters.sents()
tokens = reuters.words()

print sentences
print tokens


tri_model = defaultdict(lambda: defaultdict(lambda: 0))

for sentence in reuters.sents():
    for w1, w2, w3 in trigrams(sentence, pad_left=True, pad_right=True):
        tri_model[(w1, w2)][w3] +=1
        
print tri_model[None, None]["The"]   #8839
print tri_model["and", "functions"]["of"] #1

for w12 in tri_model:
    count = float(sum(tri_model[w12].values()))
    for w3 in tri_model[w12]:
        tri_model[w12][w3] /= count
        
print tri_model[None, None]["The"]   #0.161543241465
print tri_model["and", "functions"]["of"] #1
print tri_model["and", "functions"]["some_random_word"] #0

import random

text = [None, None]

sentence_finish = False

while not sentence_finish:
    rand = random.random()
    acc = .0
    
    for w in tri_model[tuple(text[-2:])].keys():
        acc += tri_model[tuple(text[-2:])][w]
        
        if acc >= rand:
            text.append(w)
            break
        
    if text[-2:] == [None, None]:
        sentence_finish = True
        
        
new_sentence = ' '.join([t for t in text if t])

print "Sentence:" + new_sentence

#Out[45]: u'It said Manning has resigned from the system would face a credibilty problem on Wall Street dealers with too little collateral with which talks are on different sides , dealers said the measures passed by the booking of residuals arising from the RCA acquisition ."'


