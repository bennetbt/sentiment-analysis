#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI


# In[3]:


app = FastAPI()


# In[4]:


@app.get("/")
async def root():
    with open("sentiment-analysis.py") as f:
        exec(f.read())


# In[ ]:




