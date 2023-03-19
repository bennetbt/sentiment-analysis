#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *


# In[3]:


n_instances = 100
subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
len(subj_docs), len(obj_docs)


# In[4]:


subj_docs[0]


# In[5]:


train_subj_docs = subj_docs[:80]
test_subj_docs = subj_docs[80:100]
train_obj_docs = obj_docs[:80]
test_obj_docs = obj_docs[80:100]
training_docs = train_subj_docs+train_obj_docs
testing_docs = test_subj_docs+test_obj_docs


# In[6]:


sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])


# In[7]:


unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
len(unigram_feats)


# In[8]:


sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)


# In[9]:


training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)


# In[10]:


trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)


# In[11]:


for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):print('{0}: {1}'.format(key, value))


# In[12]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer


# In[13]:


from nltk import tokenize


# In[14]:


sentence = "This is a terrible test"


# In[15]:


sid = SentimentIntensityAnalyzer()
print(sentence)
ss = sid.polarity_scores(sentence)
for k in sorted(ss):
    print('{0}: {1}, '.format(k, ss[k]), end='')
print()


# In[ ]:




