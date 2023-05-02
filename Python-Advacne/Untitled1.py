#!/usr/bin/env python
# coding: utf-8

# In[9]:


a='Apple'
a[::-1]==a


# In[20]:


b='Happy momentum'
b[2:len(b)-2]


# In[1]:


sentence="Hello Good Morning"
sentence[3:len(sentence)-4]


# In[5]:


a='AddA'
a[::-1]==a


# In[9]:


# string='Vinod'
# print(string[::-1])
sentence="Hello good morning"
print(sentence[2:len(sentence)-2])


# In[4]:


sentence='I\'m learning programing'
import time
from datetime import date
from datetime import datetime
now=datetime.now()
now


# In[14]:


today = date.today()
yesterday=date(today.year, 5, 1)
if today > yesterday:
    print('Fuck the Past')
else:
    print('Think about the feature')


# In[8]:


sentence1='What you do now ?'
sentence2='I\'m Learnig the Programming'
if sentence !=sentence2:
    print('Fuck the Past')
else:
    print('Well think about feature')


# In[16]:


result=''
for char in sentence1:
    if char in result:
        pass
    else:
        result=result+char
print(result)


# In[22]:


for char in sentence1:
    if char not in result:
        result=result+char
    else:
        pass
print(result)


# In[ ]:




