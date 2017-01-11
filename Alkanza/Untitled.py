
# coding: utf-8

# In[1]:

from pandas import DataFrame, Series
import pandas as pd
import numpy as np


# In[5]:

tickers = pd.read_excel('tickers.xlsx')
tickers = tickers['Ticker'].tolist()
tickers[-1] = '^GSPC'
tickers


# In[127]:

import pandas_datareader.data as web
end = '2017-01-10'
start = '2015-12-31'
get_px = lambda x: web.DataReader(x, 'yahoo', start=start, end=end)['Close']
data = pd.DataFrame({sym:get_px(sym) for sym in tickers})
data.head()


# In[23]:

hardcoded = pd.read_clipboard()
hardcoded.head()


# In[37]:

from datetime import datetime
hardcoded2 = hardcoded.reset_index()
del hardcoded2['index']
hardcoded3 = hardcoded2.set_index(Series(datetime(2015, 12, 31)))
hardcoded3


# In[123]:

#data.iloc[0] = hardcoded3.iloc[0]
data.head()


# In[69]:

def take_dividends(df):
    mask = df['action'].isin(['DIVIDEND'])
    return df.ix[mask, 'value']
end = '2017-01-10'
start = '2015-12-31'
def get_px_div(x):
    df = web.DataReader(x, 'yahoo-actions', start=start, end=end)
    return take_dividends(df)
dividends = {}
for x in tickers:
    try:
        dividends[x] = get_px_div(x)
    except:
        pass 
dividends


# In[70]:

div = DataFrame(dividends)


# In[71]:

div.head()


# In[82]:

div2 = div.fillna(0)
div2.index.name = 'Date'
div2.head()


# In[128]:

first = data - data.shift(1)
first.head()


# In[129]:

tot = first.add(div2, fill_value = 0)
ret = tot.div(data.shift(1), fill_value = 1)


# In[130]:

ret.head()


# In[ ]:




# In[109]:




# In[131]:

writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
ret.to_excel(writer)
writer.save()


# In[ ]:



