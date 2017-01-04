
# coding: utf-8

# # Group by Operations
# 
# After loading, merging, and preparing a data set, a familiar task is to compute group statistics or possibly pivot tables for reporting or visualization purposes. pandas provides a flex- ible and high-performance groupby facility, enabling you to slice and dice, and sum- marize data sets in a natural way.
# 
# After loading, merging, and preparing a data set, a familiar task is to compute group statistics or possibly pivot tables for reporting or visualization purposes. pandas provides a flex- ible and high-performance groupby facility, enabling you to slice and dice, and sum- marize data sets in a natural way.
# 
# Hadley Wickham, an author of many popular packages for the R programming lan- guage, coined the term split-apply-combine for talking about group operations, and I think that’s a good description of the process. In the first stage of the process, data contained in a pandas object, whether a Series, DataFrame, or otherwise, is split into groups based on one or more keys that you provide. The splitting is performed on a particular axis of an object. For example, a DataFrame can be grouped on its rows (axis=0) or its columns (axis=1). Once this is done, a function is applied to each group, producing a new value. Finally, the results of all those function applications are com- bined into a result object
# 
# ## Split

# In[3]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                'key2' : ['one', 'two', 'one', 'two', 'one'],
                'data1' : np.random.randn(5), 'data2' : np.random.randn(5)})
df


# The split works with any of the axis. Simply put, you must give the groupby operator something to compute an array that identifies the group for each of the components of the axis belongs. For example, you can group the observations (axis = 0) by the values they take in one or more columns:

# In[5]:

grouped = df.groupby(['key1', 'key2'])


# In[8]:

for (x1, x2), group in grouped:
    print(x1, x2)
    print(group)


# Of course, you can choose to do whatever you want with the pieces of data. A recipe you may find useful is computing a dict of the data pieces as a one-liner:

# In[10]:

pieces = dict(list(df.groupby(['key1', 'key2'])))
pieces[('b', 'one')]    


# We can also group by the levels of a hierarchical index:

# In[24]:

import pandas_datareader.data as web
end = '2015-01-01'
start = '2007-01-01'
get_px = lambda x: web.DataReader(x, 'yahoo', start=start, end=end)['Adj Close']
symbols = ['SPY','TLT','MSFT']
# raw adjusted close prices
data = pd.DataFrame({sym:get_px(sym) for sym in symbols})
data = data.reset_index()
data2 = pd.melt(data, id_vars ='Date',var_name = 'Index', value_name = 'Value')
data3 = data2.set_index(['Index', 'Date'])
data3.head()


# In[13]:

for name, group in data3.groupby(level= 'Index'):
    print(name)


# We can also group by applying a function to the index and use the resulting array. For example:

# In[26]:

data5 = data.set_index('Date')
data5.groupby(lambda x: x.year).mean()


# ### Syntactic sugar
# 
# Most of the time, it's not necessary to take all the columns with you. 

# df.groupby('key1')['data1'] == df['data1'].groupby(df['key1'])

# ## Apply
# 
# Once you have the data split by groups, the next step is to apply a function to each group.
# 
# ### Aggregate
# 
# Aggregate functions are the type of functions that take an array and return a scalar. Thus, for each group, these functions will return a scalar. 

# In[16]:

data3.groupby(level = 'Index')['Value'].mean() ## Optimized


# In[19]:

data3['Returns'] = data3['Value'].pct_change()
data3.groupby(level = 'Index')['Returns'].agg([('Average', 'mean'),
                                              ('Volatility', 'std')])


# In[20]:

data3.groupby(level = 'Index').agg({'Returns': ['min', 'max', 'std', 'mean'],
                                   'Value': 'mean'}) # Hierarchical columns


# ### Transformations: transform and apply
# 
# More than simple aggregations on each group. For example, let's say we want to get the last 5 observation for each index. 

# In[40]:

def top(group):
    return group.iloc[:5]
data3.groupby(level = 'Index').apply(top).sort_index()


# In[29]:

df = DataFrame({'category': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'], 
                'data': np.random.randn(8),'weights': np.random.rand(8)})
df


# Let's compute the annual correlation of the daily returns of the different tickers.

# In[30]:

grouped = df.groupby('category').apply(lambda g: np.average(g['data'], weights = g['weights']))
grouped


# In[39]:

def ret_aritmetico(group):
    return group['Value'].pct_change()
data3 = data3.sort_index()
data10 = data3.groupby(level = 'Index', group_keys = False).apply(ret_aritmetico)
data10.groupby(level = 'Index', group_keys= False).apply(top)


# In[42]:

data10 = data10.dropna()
data10.head()


# In[51]:

data11 = data10.unstack(0)
data11.head()


# In[52]:

data11.groupby(lambda x: x.year).apply(lambda g: g.corrwith(g['SPY']))


# In[ ]:



