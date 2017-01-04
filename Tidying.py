
# coding: utf-8

# # Tidying Data
# 
# Tidying Data refers to the process of structuring data to facilitate analysis. That is, first acknowledge that Data is not in the format you wish and then organize it. 
# 
# ## Standard Pandas Operations
# 
# ### Database-style DataFrame Merges
# 
# Merge or join operations combine data sets by linking rows using one or more keys. These operations are central to relational databases. The merge function in pandas is the main entry point for using these algorithms on your data.
# 
# pandas merge, pd.merge, will join the two dataframes will use the columns with overlapping names as keys.

# In[2]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})
pd.merge(df1, df2) # Overlapping name: key


# If the name of the key column is the same in both dataframes, use the argument on. If it's different, use both arguments: left_on, right_on.

# In[4]:

pd.merge(df1, df2, on = 'key')


# To specify the type of relational database join that you want, use the argument how.

# In[5]:

pd.merge(df1, df2, on = 'key', how = 'outer') # inner, left, right. 


# Usually, you'll want to merge on the indeces of the dataframes. Use the arguments left_index and right index, which are both boolean. 

# In[6]:

left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'], 
                  columns=['Ohio', 'Nevada'])
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                   index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
pd.merge(left2, right2, how = 'inner', left_index = True, right_index = True)


# ### Concatenate along an axis
# 
# There are two axis: the horizontal, 0, and the vertical. There are two things you must remember when concatenating: what to do with the components of the other axis that do not overlap, and if you want to be able to distinguish what came from where in the resulting dataframe. The first problem of the extra axis can be solved with the argument join; the second problem can be solved by using hierarchical index using the keys argument.

# In[8]:

df1 = DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'], columns=['one', 'two'])
df2 = DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'], columns=['three', 'four'])
pd.concat([df1, df2], join = 'inner', axis=1, keys=['level1', 'level2']) # add columns


# ## Reshaping and pivoting
# 
# There are a number of fundamental operations for rearranging tabular data. These are alternatingly referred to as reshape or pivot operations.
# 
# ### With hierarchical index
# 
# - stack: from the columns to the rows.
# - unstack: from the rows to the columns.

# In[9]:

data = DataFrame(np.arange(6).reshape((2, 3)),
                 index=pd.Index(['Ohio', 'Colorado'], name='state'),
                 columns=pd.Index(['one', 'two', 'three'], name='number'))
data


# In[10]:

data.stack()


# In[11]:

data.stack().unstack()


# In[12]:

data.stack().unstack('state')


# ### Reshape: Pivot and Melt
# 
# Without using the index.

# In[7]:

import pandas_datareader.data as web
end = '2015-01-01'
start = '2007-01-01'
get_px = lambda x: web.DataReader(x, 'yahoo', start=start, end=end)['Adj Close']
symbols = ['SPY','TLT','MSFT']
# raw adjusted close prices
data = pd.DataFrame({sym:get_px(sym) for sym in symbols})
data = data.reset_index()
data2 = pd.melt(data, id_vars ='Date',var_name = 'Index', value_name = 'Value')
data2.iloc[[100, 2000, 5000]]


# In[9]:

data2.set_index(['Date', 'Index']).unstack(1).head(5)


# In[13]:

data3 = data2.pivot(index = 'Date', columns = 'Index', values = 'Value')
data3.head(5)


# In[18]:

pd.melt(data3.reset_index(), id_vars = 'Date', var_name = 'index', value_name = 'value').head(5)


# ## Others
# 
# To create a new variable based on a dictionary that takes the values in another variable.

# In[19]:

data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                           'corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],
                  'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data


# In[24]:

meat_to_animal = { 'bacon': 'pig', 'pulled pork': 'pig', 'pastrami': 'cow', 
                  'corned beef': 'cow', 'honey ham': 'pig', 'nova lox': 'salmon'}
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
data


# In[ ]:



