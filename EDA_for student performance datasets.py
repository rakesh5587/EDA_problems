#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df=pd.read_csv('StudentsPerformance.csv')
df.head()


# In[3]:


df.shape


# In[14]:


df.info()# also gives the datatype of each column


# In[15]:


df.isnull().sum()#there is no null values in the dataset


# In[20]:


df.describe()#explain statistics of the dataset


# In[21]:


df[df.duplicated()]


# In[22]:


#noduplicate data is present hare


# In[23]:


df.isna().sum()


# In[19]:


#find unique number in each column
df.nunique()


# In[31]:


#seggregating categorical and numerical fetures
numerical_feature=[column for column in df.columns if df[column].dtype!='object']
categorical_feature=[column for column in df.columns if df[column].dtype=='object']


# In[32]:


numerical_feature,categorical_feature


# In[33]:


##aggregate the total score with mean
df['total_score']=df['math score']+df['reading score']+df['writing score']
df['average_score']=(df['math score']+df['reading score']+df['writing score'])/3


# In[34]:


df.head()


# In[39]:


#explore more aboout visualisation
import seaborn as sns
fig,axis=plt.subplots(1,2,figsize=(15,7))
plt.subplot(121)
sns.histplot(data=df,x='average_score', bins=30,kde=True,color='g')
plt.subplot(122)
sns.histplot(data=df,x='average_score',bins=30,kde=True,hue='gender')


# In[40]:


sns.histplot(data=df,x='average_score', bins=30,kde=True,color='g')


# In[41]:


sns.histplot(data=df,x='average_score',bins=30,kde=True,hue='gender')


# In[50]:


plt.subplots(1,3,figsize=(15,5))
plt.subplot(141)
sns.histplot(data=df,x='average_score',kde=True,hue="lunch")
plt.subplot(142)
sns.histplot(data=df[df.gender=='female'],x='average_score',kde=True,hue="lunch")
plt.subplot(143)
sns.histplot(data=df[df.gender=='male'],x='average_score',kde=True,hue="lunch")


# In[53]:


sns.heatmap(df.corr(),annot=True)


# In[ ]:




