
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

(df.groupby(s.eq(0).cumsum().mask(s.eq(0))).cumcount() + 1).mask(s.eq(0), 0).tolist()


# In[9]:


dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B') 
s = pd.Series(np.random.rand(len(dti)), index=dti)
print(s)


# In[10]:


s[dti.weekday == 2].sum() 


# In[15]:


s.resample('m').mean()


# In[19]:


s.groupby(pd.Grouper(freq='4M')).idxmax()

