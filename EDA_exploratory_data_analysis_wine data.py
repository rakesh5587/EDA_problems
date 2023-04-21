#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv('winequality-red.csv')


# In[4]:


df.head()


# In[5]:


df.corr(method='spearman')


# In[7]:


df.info()#gives summer at a glance


# In[10]:


df.describe()#gives a summery of statistics
#descriptive summary of datasets


# In[12]:


#checking all the missing value 
df.isnull().sum()


# In[14]:


##duplicate record analysis
df.duplicated().sum()


# In[15]:


df[df.duplicated()]


# In[16]:


#these are the duplicate records in the datasets 
df.shape


# In[18]:


df.drop_duplicates(inplace=True,ignore_index=True)


# In[19]:


df.head()


# In[20]:


df.shape


# In[21]:


df.corr()


# In[26]:


import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
import seaborn as sns
sns.heatmap(df.corr(),annot=True)


# In[25]:


#if you want to see it in a better manner
import seaborn as sns
sns.heatmap(df.corr(),annot=True)


# In[28]:


#visualisation
#its an imbalance datasets
df.quality.value_counts()


# In[31]:


df.quality.value_counts().plot(kind='bar')
plt.xlabel("Wine quality")
plt.ylabel('quantity')
plt.show()


# In[39]:


# we can see distribution of each and every feature
for column in df.columns:
    plt.figure(figsize=(10,6))
    sns.histplot(df[column], kde=True)


# In[40]:


#univariate,bivariate and multivariate analysis
sns.pairplot(df)


# In[42]:


#categorical plot
sns.catplot(x='quality',y='alcohol',data=df, kind='box')


# In[ ]:




