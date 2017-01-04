
# coding: utf-8

# # Getting Started: Series, DataFrame
# 
# To get started with pandas, you will need to get comfortable with its two workhorse data structures: Series and DataFrame. 
# 
# ## Series 
# 
# A Series is a one-dimensional array-like object containing an array of data (of any NumPy data type) and an associated array of data labels, called its index. That is, a Series is a 1-d numpy array with a label for each component, called __index__.

# In[3]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
obj = Series([4, 7, -5, 3]) # Default index is from 0 to 1
obj


# In[4]:

obj.values # Both index and values are attributes
obj.index


# Compared with a regular NumPy array, you can use values in the index when selecting single values or a set of values:

# In[5]:

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2['a'])
obj2[['a', 'c']]


# NumPy array operations, such as filtering with a boolean array, scalar multiplication, or applying math functions, will preserve the index-value link:

# In[8]:

print(obj2[obj2 > 4])
np.exp(obj2)


# Another way to think about a Series is as a fixed-length, ordered dict, as it is a mapping of index values to data values. Should you have data contained in a Python dict, you can create a Series from it by passing the dict:

# In[9]:

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
obj3


# Additionaly, you can have a list for values and list for the index.

# In[12]:

pop = [35000, 71000, 16000, 5000]
state = ['Ohio', 'Texas', 'Oregon', 'Utah']
obj4 = Series(pop, index = state)
obj4


# ### Missing Data
# 
# The isnull and notnull functions in pandas should be used to detect missing data:

# In[15]:

obj4.isnull() #method


# Both the Series object itself and its index have a name attribute, which integrates with other key areas of pandas functionality:

# In[17]:

obj4.name = 'Population'
obj4.index.name = 'State'
obj4


# A Series’s index can be altered in place by assignment:

# In[19]:

obj4.index = ['Radnor', 'McConaughey', 'Pot', 'Lebron James']
obj4


# ## DataFrame
# 
# A DataFrame represents a tabular, spreadsheet-like data structure containing an ordered collection of columns, each of which can be a different value type (numeric, string, boolean, etc.). The DataFrame has both a row and column index; __it can be thought of as a dict of Series (one for all sharing the same index)__.
# 
# Thus, there you have one way of creating a dataframe.

# In[24]:

equipos = Series({'Madrid': 'Real Madrid', 'Barcelona': 'FCB', 'Valencia': 'Valencia'})
reino = Series({'Madrid': 'Reyes Españoles', 'Barcelona': 'Catalunya', 'Valencia': 'Valencia'})
data = {'equipos': equipos, 'reino': reino} # names are the names of the columns.
df = DataFrame(data)
df


# A column in a DataFrame can be retrieved as a Series either by dict-like notation or by attribute:

# In[25]:

print(df['equipos'])
df['reino']


# Columns can be modified (and added) by assignment

# In[27]:

df['Deuda'] = [100, -100, 0]
df


# When assigning lists or arrays to a column, the value’s length must match the length of the DataFrame.

# In[32]:

df['Visitado'] = Series({'Barcelona': 0, 'Madrid': 0, 'Valencia': 0, 'NY': 1}) #ignores if it's not in the original index
df


# To delete a column, do the same as you would delete a key-value in a dict:

# In[33]:

del df['Visitado']
df.columns


# ### Index Objects
# 
# pandas’s Index objects are responsible for holding the axis labels and other metadata (like the axis name or names). Any array or other sequence of labels used when con- structing a Series or DataFrame is internally converted to an Index

# In[34]:

obj = Series(range(3), index=['a', 'b', 'c'])
obj.index


# Index objects are immutable and thus can’t be modified by the user. Immutability is important so that Index objects can be safely shared among data structures:

# In[36]:

try:
    obj.index[3] = 'd'
except:
    print('Index Objects are inmutable')


# As objects, index objects have their own attributes and their own methods. 

# # Functionality
# 
# ## Reindexing
# 
# When conforming an already existing pandas object to a new index, use .reindex.

# In[3]:

obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj


# We can also alter the columns index as follows:

# In[5]:

frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
frame


# In[6]:

states = ['Texas', 'Utah', 'California']
frame.reindex(columns=states)
frame


# ## Dropping entries from axis
# 
#  As that can require a bit of munging and set logic, the drop method will return a new object with the indicated value or values deleted from an axis:

# In[3]:

obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
obj.drop('c')


# With DataFrame, index values can be deleted from either axis:

# In[4]:

data = DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data


# In[5]:

data.drop(['Colorado', 'Ohio']) # Dropping rows with the index.
data.drop(['two', 'three'], axis = 1) # Dropping columns with their names.


# ## Indexing, Selection and Filtering
# 
# Series indexing (obj[...]) works analogously to NumPy array indexing, except you can use the Series’s index values instead of only integers. That is, three ways: (i) integer slicing, (ii) boolean slicing, (iii) index slicing.
# 
# ### Series

# In[7]:

obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj[1]) # integer
print(obj[[True, False, False, False]]) # Boolean
obj['b'] # Index


# Slicing with labels behaves differently than normal Python slicing in that the endpoint is inclusive:

# In[8]:

obj['b':'c']


# ### DataFrames
# 
# For the DataFrame object, things work a little differently. Slicing with labels slice columns of the DataFrame. Slicing with numbers or slicing with booleans, slices some of the rows of the DataFrame.

# In[9]:

data = DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data


# In[12]:

print(data['two'])
data[['three', 'one']]


# In[13]:

data[:2] #first two rows


# In[14]:

data[data['three'] > 5] # boolean indexing


# For DataFrame label-indexing on the rows, I introduce the special indexing field ix. It enables you to select a subset of the rows and columns from a DataFrame with NumPy- like notation plus axis labels.

# In[15]:

data.ix[['Colorado', 'Utah'], [3, 0, 1]]


# In[16]:

data.ix[:'Utah', 'two']


# In[17]:

data.ix[data.three > 5, :3]


# Moraleja: for any fancy indexing, use .ix. 

#  ## Arithmetic and Data Alignment
#  
#  One of the most important pandas features is the behavior of arithmetic between ob- jects with different indexes. When adding together objects, if any index pairs are not the same, the respective index in the result will be the union of the index pairs.

# In[18]:

s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1 + s2 # The internal data alignment introduces NA values in the indices that don’t overlap.


# In the case of DataFrame, alignment is performed on both the rows and the columns:

# In[19]:

df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1 + df2 # Adding these together results in NA values in the locations that don’t overlap. must be in both


# In[20]:

df1.add(df2, fill_value=0) # if in one but not in both, take as zero. 


# ## Function Application and Mapping
# 
# NumPy ufuncs (element-wise array methods) work fine with pandas objects. 

# In[21]:

frame = DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame


# In[22]:

frame.abs()


# Another frequent operation is applying a function on 1D arrays to each column or row. DataFrame’s apply method does exactly this:

# In[24]:

f = lambda x: x.max() - x.min()
frame.apply(f, axis = 0) # per column


# In[25]:

frame.apply(f, axis = 1) # per row


# More complicated functions can also be defined:

# In[27]:

def f(x):
    '''
    Given a np.array, return the following. 
    '''
    return Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(f, axis = 0)


# The analogous of apply with series is map.

# In[28]:

format = lambda x: '%.2f' % x
frame['e'].map(format)


# ## Sorting and Ranking
# 
# Sorting a data set by some criterion is another important built-in operation. To sort lexicographically by row or column index, use the sort_index method, which returns a new, sorted object:

# In[30]:

obj = Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index(axis = 0) # sort by index


# In[37]:

obj.sort_values()


# In[40]:

frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
frame.sort_index()


# In[41]:

frame.sort_values(by=['a', 'b'])


# ## Summarizing and Computing Descriptive Statistics
# 
# pandas objects are equipped with a set of common mathematical and statistical meth- ods. Most of these fall into the category of reductions or summary statistics, methods that extract a single value (like the sum or mean) from a Series or a Series of values from the rows or columns of a DataFrame. Compared with the equivalent methods of vanilla NumPy arrays, they are all built from the ground up to exclude missing data

# In[43]:

df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], 
               index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
print(df.sum(axis = 0)) # sum across rows
df.sum(axis = 1) # sum across columns


# In[44]:

df.mean(axis=1, skipna=False) # mean for each row


# Some methods, like idxmin and idxmax, return indirect statistics like the index value where the minimum or maximum values are attained:

# In[45]:

df.idxmax()


# In[46]:

df.describe()


# ## Correlation and covariance
# 
# Some summary statistics, like correlation and covariance, are computed from pairs of arguments.

# In[49]:

import pandas_datareader.data as web
end = '2015-01-01'
start = '2007-01-01'
get_px = lambda x: web.DataReader(x, 'yahoo', start=start, end=end)['Adj Close']
symbols = ['SPY','TLT','MSFT']
# raw adjusted close prices
data = pd.DataFrame({sym:get_px(sym) for sym in symbols})
data.head(5)


# In[51]:

returns = data.pct_change(axis = 0)
returns.tail(5)


# The corr method of Series computes the correlation of the overlapping, non-NA, aligned-by-index values in two Series. Relatedly, cov computes the covariance:

# In[52]:

returns.MSFT.corr(returns.SPY) # Series


# In[53]:

returns.corr() # DataFrame


# In[54]:

returns.corrwith(returns.SPY)


# ## Unique Values, Value Counts, and Membership

# In[56]:

obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
obj.unique()


# In[57]:

obj.value_counts()


# The very, very __important__ isin() method. Analogous to %in% in R. 

# In[58]:

mask = obj.isin(['b', 'c'])
obj[mask]


# ## Handling Missing Data
# 
# ### Filtering out missing

# ## Hierarchical Indexing
# 
# Hierarchical indexing is an important feature of pandas enabling you to have multiple (two or more) index levels on an axis. Somewhat abstractly, it provides a way for you to work with higher dimensional data in a lower dimensional form.
# 
# ## Series

# In[5]:

data = Series(np.random.randn(10), 
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'], 
              [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
data


# In[6]:

data.index # MultiIndex


# With a hierarchically-indexed object, so-called partial indexing is possible, enabling you to concisely select subsets of the data:

# In[7]:

data['b']


# Selection is even possible in some cases from an “inner” level:

# In[8]:

data[:, 2]


# In[9]:

data.unstack()


# In[11]:

data.unstack().stack()


# Many descriptive and summary statistics on DataFrame and Series have a level option in which you can specify the level you want to sum by on a particular axis.

# In[12]:

data.index.names = ['key1', 'key2']
data.mean(level = 'key1', axis = 0)


# It’s not unusual to want to use one or more columns from a DataFrame as the row index; alternatively, you may wish to move the row index into the DataFrame’s col- umns. 

# In[13]:

frame = DataFrame({'a': range(7), 'b': range(7, 0, -1), 
                   'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})
frame2 = frame.set_index(['c', 'd'])
frame2


# In[14]:

frame2.reset_index()


# In[60]:

import pandas_datareader.data as web
end = '2015-01-01'
start = '2007-01-01'
get_px = lambda x: web.DataReader(x, 'yahoo', start=start, end=end)['Adj Close']
symbols = ['SPY','TLT','MSFT']
# raw adjusted close prices
data = pd.DataFrame({sym:get_px(sym) for sym in symbols})
data.head(5)


# In[61]:

data = data.reset_index()
data2 = pd.melt(data, id_vars ='Date',var_name = 'Index', value_name = 'Value')
data2.head(5)


# In[65]:

data2.set_index(['Index', 'Date']).head(5)

