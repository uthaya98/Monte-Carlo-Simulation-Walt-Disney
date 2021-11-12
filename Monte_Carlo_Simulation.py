#!/usr/bin/env python
# coding: utf-8

# In[156]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
from pandas import Series, DataFrame
import seaborn as sns
import matplotlib.dates as mdates
sns.set_style('whitegrid')


# In[157]:


Year = mdates.DateFormatter('%y')


# In[158]:


DSN = pd.read_csv('disney_movies1.csv')


# In[159]:


DSN_budget = DSN['BUDGET'].copy()
DSN_Box_Office = DSN['Box Office']


# In[160]:


DSN_budget.head()


# In[161]:


DSN_budget.tail()


# In[188]:


plt.plot(DSN['BUDGET'])
plt.title('Monte Carlo Simulation Budget Disney Movies',color='blue')
plt.ylabel('Budget', color='red')
plt.xlabel('Number of days per year', color='red')


# In[163]:


plt.plot(DSN['Box Office'])
plt.title('Monte Carlo Simulation Box Office Disney Movies',color='blue')
plt.ylabel('Box Office', color='red')
plt.xlabel('Number of days per year', color='red')


# In[164]:


print("Count:", len(DSN['BUDGET']))
print("Mean: ", DSN['BUDGET'].mean())
print("SD: ",DSN['BUDGET'].std())
print("Max: ",DSN['BUDGET'].max())
print("Min: ", DSN['BUDGET'].min())


# In[165]:


print("Count:", len(DSN['Box Office']))
print("Mean: ", DSN['Box Office'].mean())
print("SD: ",DSN['Box Office'].std())
print("Max: ",DSN['Box Office'].max())
print("Min: ", DSN['Box Office'].min())


# In[166]:


print("Count:", len(DSN['BUDGET']))
print("Mean: ", DSN['BUDGET'].mean())
print("SD: ",DSN['BUDGET'].std())
print("Min: ", DSN['BUDGET'].min())
print("25%: ", (DSN['BUDGET'].sum() * 25 / 100))
print("50%: ", (DSN['BUDGET'].sum() * 50 / 100))
print("75%: ", (DSN['BUDGET'].sum() * 75 / 100))
print("Max: ",DSN['BUDGET'].max())


# In[167]:


print("Count:", len(DSN['Box Office']))
print("Mean: ", DSN['Box Office'].mean())
print("SD: ",DSN['Box Office'].std())
print("Min: ", DSN['Box Office'].min())
print("25%: ", (DSN['Box Office'].sum() * 25 / 100))
print("50%: ", (DSN['Box Office'].sum() * 50 / 100))
print("75%: ", (DSN['Box Office'].sum() * 75 / 100))
print("Max: ",DSN['Box Office'].max())


# In[168]:


budget = DSN['BUDGET']
Box_Office = DSN['Box Office']


# In[169]:


budget


# In[170]:


Box_Office


# In[171]:


plt.hist(budget, bins=100)


# In[172]:


plt.hist(Box_Office, bins=100)


# In[173]:


plot=sns.distplot(budget,color='y')
plot.set_ylabel('Box office',color='b')


# In[174]:


plt.scatter(budget,Box_Office,color='r')


# In[187]:


plt.plot(DSN['BUDGET'], color='r')
plt.plot(DSN['Box Office'], color='b')
plt.ylabel('Financial Value', color='red')
plt.xlabel('Number of days per year', color='red')


# In[ ]:





# In[ ]:




