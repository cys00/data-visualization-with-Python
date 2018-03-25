#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:34:41 2018

@author: yusheng
"""
import nltk
#nltk.download()

from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

import string

p = string.punctuation
d = string.digits
p_d = p + d

p_d_table = str.maketrans(p_d,len(p_d)*' ')

import json

with open('tweet_stream_Seattle_10000.json','r') as f:
    data = json.load(f)

tweets_txt = ''
for tweet in data:
    t_txt = tweet['text'].translate(p_d_table)
    t_txt_stem = wnl.lemmatize(t_txt)
    tweets_txt += ' {}'.format(t_txt_stem)

with open('clean_tweets_txt_Seattle.txt','w') as outfile:
    outfile.write(tweets_txt)

with open('clean_tweets_txt_Seattle.txt','r') as infile:
    lst_of_tokens = nltk.word_tokenize(infile.read().lower())

stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(['qemtg','uu','anto…','please','year','bavenss','asking','stuff',
                  'lotta','https','co','rt','san','part','includes','San','RT','Part'])
removed_stopwords = [w for w in lst_of_tokens if w not in stopwords and len(w) > 1]

freq = nltk.FreqDist(removed_stopwords)
freq.plot(20)

#from collections import Counter
#c = Counter(removed_stopwords) 
#c.most_common(30)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from os import path
from PIL import Image
import numpy as np
from wordcloud import STOPWORDS
s_p = set(STOPWORDS)
s_p.update(['Anto','qemtg','uu','anto…','Anto…','please','year','bavenss','asking','stuff',
                  'lotta','https','co','rt','san','part','includes','San','RT','Part'])

d = path.dirname(__file__)
wordcloud_txt = open(path.join(d,'clean_tweets_txt_Seattle.txt')).read()

wordcloud_mask = np.array(Image.open(path.join(d,'seattle_skyline.jpg')))

w_c = WordCloud(background_color='white',max_words=2000,mask=wordcloud_mask,stopwords=s_p)

w_c.generate(wordcloud_txt)

w_c.to_file(path.join(d,'Seattle_wordcloud.jpg'))

plt.imshow(w_c,interpolation='bilinear')
plt.axis('off')
plt.figure
plt.imshow(wordcloud_mask,cmap=plt.cm.gray,interpolation='bilinear')
plt.axis('off')
plt.show()














