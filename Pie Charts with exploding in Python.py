#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Pie Charts with exploding in Python
import matplotlib.pyplot as pyplot


# In[4]:


labels = ('Python', 'Java', 'Scala', 'C#')


# In[15]:


sizes= [45, 30, 15, 10]


# In[16]:


#only "explodes" the 1st slice (i.e. 'Python')


# In[22]:


explode= (0.1, 0, 0, 0)


# In[23]:


pyplot.pie(sizes,
explode=explode,
labels=labels,
autopct='%1.f%%',
shadow=True,
counterclock=False,
startangle=45)
pyplot.show()


# In[ ]:




