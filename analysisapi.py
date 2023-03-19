#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI


# In[3]:


app = FastAPI()


# In[4]:


@app.get("/")
async def root():
    return {"message": "Hello World"}


# In[ ]:




