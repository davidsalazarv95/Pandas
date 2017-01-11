
# coding: utf-8

# In[1]:

from pandas import DataFrame, Series
import pandas as pd
import numpy as np


# In[7]:

hardcoded = pd.read_clipboard()
hardcoded.head()


# In[8]:

hardcoded.index.name = 'Date'
hardcoded


# In[9]:

returns = pd.read_excel('returns.xlsx')
returns.head()


# In[10]:

returns2 = returns.set_index('Date')
returns2.head()


# In[15]:

returns2[hardcoded.columns.values]


# In[ ]:



