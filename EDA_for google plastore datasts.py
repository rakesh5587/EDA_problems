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


df=pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/main/googleplaystore.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.duplicated().sum()


# In[6]:


df.drop_duplicates(inplace=True,ignore_index=True)


# In[7]:


df.shape


# In[8]:


df.describe()


# In[9]:


#find out missing values
df.isnull().sum()


# In[10]:


df['Reviews'].unique()


# In[11]:


df['Reviews'].str.isnumeric().sum()


# In[12]:


df[~df['Reviews'].str.isnumeric()]


# In[13]:


df_copy=df.copy()


# In[14]:


df_copy=df_copy.drop(df_copy.index[9990])


# In[15]:


df_copy.head()


# In[16]:


#convert this reviews column data type to int
df_copy["Reviews"]=df_copy["Reviews"].astype(int)


# In[17]:


df_copy.info()


# In[18]:


df_copy['Size']# we also have to cleane it


# In[24]:


df_copy['Size']=df_copy['Size'].str.replace('M','000')
df_copy['Size']=df_copy['Size'].str.replace('k','')
df_copy['Size']=df_copy["Size"].replace('Varies with device',np.nan)
df_copy['Size']=df_copy['Size'].astype(float)


# In[25]:


df_copy['Size'].astype(float)
df_copy.info()


# In[26]:


df_copy['Installs'].unique()


# In[31]:


#now i have to remove all special character


# In[36]:


chars_to_remove=["+",",","$"]
cols_to_clean=['Installs', 'Price']
for items in chars_to_remove:
    for cols in cols_to_clean:
        df_copy[cols]=df_copy[cols].str.replace(items,'')


# In[39]:


df_copy['Installs'].unique()
df_copy['Installs']=df_copy['Installs'].astype(int)


# In[40]:


df_copy['Price'].unique()
df_copy['Price']=df_copy['Price'].astype(float)


# In[41]:


df_copy.info()


# In[42]:


#update last update column


# In[45]:


df_copy['Last Updated'].unique()


# In[46]:


#in order to convert this column in the standard format 
df_copy['Last Updated']=pd.to_datetime(df_copy['Last Updated'])


# In[47]:


df_copy['Last Updated'].unique()


# In[51]:


#we can make separate columns for day, month and year
df_copy['Day']=df_copy['Last Updated'].dt.day
df_copy['Month']=df_copy['Last Updated'].dt.month
df_copy['Year']=df_copy['Last Updated'].dt.year


# In[52]:


df_copy.head()


# In[53]:


df_copy['Content Rating'].unique()


# In[54]:


df_copy['Content Rating']=df_copy['Content Rating'].map({'Everyone':0, 'Teen':13, 'Everyone 10+':10, 'Mature 17+':17,
       'Adults only 18+':18, 'Unrated':0})


# In[56]:


df_copy.head()
df_copy['Content Rating'].unique()


# In[57]:


df_copy.info()


# In[58]:


df_copy['Genres'].unique()


# In[ ]:




