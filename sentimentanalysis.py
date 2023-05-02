#!/usr/bin/env python
# coding: utf-8

# In[4]:


import nltk
nltk.download('subjectivity')
nltk.download('vader_lexicon')


# In[5]:


from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *


# In[6]:


n_instances = 100
subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
len(subj_docs), len(obj_docs)


# In[7]:


subj_docs[0]


# In[8]:

# BTB Was Here Today

train_subj_docs = subj_docs[:80]
test_subj_docs = subj_docs[80:100]
train_obj_docs = obj_docs[:80]
test_obj_docs = obj_docs[80:100]
training_docs = train_subj_docs+train_obj_docs
testing_docs = test_subj_docs+test_obj_docs


# In[9]:


sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])


# In[10]:


unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
len(unigram_feats)


# In[11]:


sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)


# In[12]:


training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)


# In[13]:


trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)


# In[14]:


for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):print('{0}: {1}'.format(key, value))


# In[15]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer


# In[16]:


from nltk import tokenize


# In[43]:


import json


# In[45]:


def analyze_sentence(fsentence):
    sid = SentimentIntensityAnalyzer()
    print(fsentence)
    ss = sid.polarity_scores(fsentence)
    negVal = ss["neg"]
    posVal = ss["pos"]
    neuVal = ss["neu"]
    highest = "Neutral"
    highVal = 0
    if negVal > highVal:
        highest = "Negative"
        highVal = negVal
    if posVal > highVal:
        highest = "Positive"
        highVal = posVal
    if neuVal > highVal:
        highest = "Neutral"
        highVal = neuVal
    finalValue = {
        "text": fsentence,
        "sentiment": highest,
        "value": highVal
    }
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()
    return json.dumps(finalValue)


# In[ ]:


from fastapi import FastAPI


# In[ ]:


app = FastAPI()


# In[ ]:


@app.get("/")
async def root():
    return analyze_sentence("This is the default sentence")


# In[42]:


@app.get("/{sentence}")
async def analyzeGivenSentence(sentence: str):
    return analyze_sentence(sentence)


# In[ ]:





# In[ ]:




