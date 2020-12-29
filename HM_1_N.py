#!/usr/bin/env python
# coding: utf-8

# Задание 1

# In[1]:


import numpy as np


# In[3]:


a = np.array([[1,6],[2,8],[3,11],[3,10],[1,7]])
a


# In[4]:


mean_a = a.mean(axis=0)
mean_a


# Задание 2

# In[5]:


a_centered = a - mean_a
a_centered


# Задание 3

# In[6]:


a_centered_sp = np.dot(a_centered[:,0],a_centered[:,1])/4
a_centered_sp


# Задание 4

# In[7]:


np.cov(a.T)


# Pandas
# 
# Задание 1

# In[9]:


import pandas as pd
authors = pd.DataFrame({"author_id": [1, 2, 3], "author_name": ["Тургенев", "Чехов", "Островский"]})
authors


# In[10]:


book = pd.DataFrame({"author_id": [1,1,1,2,2,3,3], "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],"price":[450, 300, 350, 500, 450, 370, 290]})
book


# Задание 2

# In[11]:


author_price = pd.merge(authors,book,on ='author_id', how ='outer')
author_price


# Задание 3

# In[23]:


top5 = pd.DataFrame(author_price['price'].nlargest(5))
top5


# Задание 4

# In[95]:


maxprice = author_price.groupby('author_name').agg({'price':'max'}).rename(columns={'price' : 'max_price'})
minprice = author_price.groupby('author_name').agg({'price':'min'}).rename(columns={'price' : 'min_price'})
meanprice = author_price.groupby('author_name').agg({'price':'mean'}).rename(columns={'price' : 'mean_price'})
authors_stat = pd.concat([maxprice, minprice, meanprice], axis = 1)
authors_stat


# In[ ]:




