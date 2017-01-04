
# coding: utf-8

# # Numpy

# One of the key features of NumPy is its N-dimensional array object, or ndarray, which is a fast, flexible container for large data sets in Python. Arrays enable you to perform mathematical operations on whole blocks of data using similar syntax to the equivalent operations between scalar elements.

# An ndarray is a generic multidimensional container for homogeneous data; that is, all of the elements must be the same type. Every array has a shape, a tuple indicating the size of each dimension, and a dtype, an object describing the data type of the array

# In[1]:

import numpy as np
from numpy import random
data = np.array([1,2,3]); data


# In[2]:

print(data.shape); data.dtype


# The easiest way to create an array is to use the array function. This accepts any se- quence-like object (including other arrays) and produces a new NumPy array contain- ing the passed data. Nested sequences, like a list of equal-length lists, will be converted into a multidimen- sional array:

# In[3]:

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2); print(arr2)
arr2.shape


# In[4]:

print(np.zeros((2,3)).shape); np.eye(4,2).shape


# You can explicitly convert or cast an array from one dtype to another using ndarray’s astype method:

# In[5]:

float_arr = arr2.astype(np.float64); float_arr


# arange is an array-valued version of the built-in Python range function:

# In[6]:

np.arange(15)


# Arrays are important because they enable you to express batch operations on data without writing any for loops. This is usually called vectorization. Any arithmetic op- erations between equal-size arrays applies the operation elementwise.
# 
# Arithmetic operations with scalars are as you would expect, propagating the value to each element.

# In[7]:

print(arr2-arr2); arr2/2


# ## Basic Index and slicing

# NumPy array indexing is a rich topic, as there are many ways you may want to select a subset.

# In[8]:

arr = np.arange(10)
arr[5]


# In a two-dimensional array, the elements at each index are no longer scalars but rather one-dimensional arrays.
# 
# In multidimensional arrays, if you omit later indices, the returned object will be a lower- dimensional ndarray consisting of all the data along the higher dimensions (i.e., pass first dimension and np will understand as give me the other dimensions)

# In[9]:

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2] # third row
arr2d[0, 2] # first row and second column
arr2d[:, :1] # All rows and the first column


# In multidimensional arrays, if you omit later indices, the returned object will be a lower- dimensional ndarray consisting of all the data along the higher dimensions.
# 
# Boolean indexing: both the boolean and the array must be of the same length. You can combine boolean indexing with integer indexs.

# In[10]:

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = random.randn(7, 4)
data[names == 'Bob'] # pass me rows that match the boolean tuple name == 'Bob'


# To select everything but 'Bob', you can either use != or negate the condition using ~:

# In[11]:

data[~(names == 'Bob')]


# In[12]:

print(data.shape)
data.T.shape # Transpose


# A universal function, or ufunc, is a function that performs elementwise operations on data in ndarrays

# In[13]:

np.abs(data); # unary
np.greater(data, data)


# In[14]:

x = random.randn(8)
y = random.randn(8)
np.maximum(x, y) # element-wise maximum


# ## Vectorization

# Using NumPy arrays enables you to express many kinds of data processing tasks as concise array expressions that might otherwise require writing loops. This practice of replacing explicit loops with array expressions is commonly referred to as vectoriza- tion.
# 
# The numpy.where function is a vectorized version of the ternary expression x if condition else y. That is, it returns for the array evaluated what'd be done with a for loop.
# 
#  A typical use of where in data analysis is to produce a new array of values based on another array. Suppose you had a matrix of randomly generated data and you wanted to replace all positive values with 2 and all negative values with -2. This is very easy to do with np.where:

# In[15]:

arr = random.randn(4, 4)
print(np.where(arr > 0, 2, -2))
np.where(arr > 0, 2, arr) # set only positive values to 2


# ## Mathematical functions

# A set of mathematical functions which compute statistics about an entire array or about the data along an axis are accessible as array methods. arrays have different axes: the first running vertically downwards across rows (axis 0), and the second running horizontally across columns (axis 1).

# In[16]:

arr = np.random.randn(5, 4) # normally-distributed data
print(arr)
arr.mean(axis = 0) # mean for columns
arr.mean(axis = 1) # mean for rows


# Boolean arrays also have different methods.

# In[17]:

arr = random.randn(100)
(arr > 0).sum() # Number of positive values


# In[18]:

large_arr = random.randn(1000)
large_arr.sort()
large_arr[int(0.05 * len(large_arr))] # 5% quantile


# NumPy has some basic set operations for one-dimensional ndarrays. Probably the most commonly used one is np.unique, which returns the sorted unique values in an array:

# In[19]:

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names)


# ## Linear Algebra

# In[20]:

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[1., 2.], [3, 4], [5., 6.]])
x.dot(y)


# In[21]:

mat = x.T.dot(x)
mat


# ## Random
# 
# The numpy random generator is much faster than the python one. For example, let's generate many random walks. 

# In[ ]:

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size = (nwalks, nsteps) )
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(axis = 1) # Cumulative sum for each row, that is, each walk

