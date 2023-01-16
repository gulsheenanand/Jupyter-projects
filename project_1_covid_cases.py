#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[7]:


data=pd.read_csv(r"C:\Users\HP-PC\Downloads\4. covid_19_data.csv")


# In[8]:


data


# In[9]:


#1
#df.count()
#df.isnull().sum()


# In[10]:


data.count()

#null values means missing values


# In[13]:


data.isnull()


# In[14]:


data.isnull().sum()


# In[15]:


#2 
#import seaborn as sns
#import matplotlib.pyplot as plt
#sns.heatmap(data.isnull())
#plt.show()


# In[16]:


import seaborn as sns


# In[17]:


import matplotlib.pyplot as plt


# In[19]:


sns.heatmap(data.isnull())


# In[20]:


# Q1. Show the number of confirmed,Deaths and Recorvered cases in each Region.
#data.groupby('Region').sum().head(50)
#data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(20)
#data.groupby('Region')['Confirmed','Recovered'].sum()


# In[21]:


data.head(2)


# In[24]:


data.groupby('Region').sum().head(20)


# In[26]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(20)


# In[27]:


data.groupby('Region')['Deaths'].sum().sort_values(ascending=False).head(20)


# In[30]:


#Q2 Remove all the records where Confirmed Cases is Less Than 10
#data.Confirmed <10
#data[data.Confirmed <10]
#data[~(data.Confirmed <10)]                # ~ removes the record
#data=data[~(data.Confirmed<10)]


# In[31]:


data.head(2)


# In[32]:


data.Confirmed < 10


# In[33]:


data[data.Confirmed <10]


# In[34]:


data=data[~(data.Confirmed <10 )]   #To remove the records satisfying a particular condition


# In[35]:


data


# In[36]:


data.head(20)


# In[37]:


# Q3 In wich Region,maximum number of Confirmed csses were Recorded?
#data.groupby('Region').Confirmed.sum().sort_values(ascending=False).head(20)


# In[38]:


data


# In[39]:


data.head(2)


# In[40]:


data.groupby('Region').Confirmed.sum().sort_values(ascending=False)


# In[41]:


#Q4 In which Region minimum number of Deaths cases were recorded?
#data.groupby('Region').Deaths.sum().sort_values(ascending=True)


# In[44]:


data.groupby('Region').Deaths.sum().sort_values(ascending=True)


# In[45]:


#Q5 How many Confirmed Deaths & Recovered cases were reported from India till 29 april 2020?
#data[data.Region=='Country_name']


# In[46]:


data


# In[48]:


data[data.Region=='India']


# In[49]:


data[data.Region=='Canada']


# In[50]:


# Q6 Sort the entire data wrt No. of Confirmed cases in Ascending Order.
#data.sort_values(by=['Confirmed'],ascending=True)


# In[53]:


data.sort_values(by=['Confirmed'],ascending =True)


# In[54]:


# Q7 Sort the entire data wrt No.of Recovered cases in descending Order.
#data.sort_values(by=['Recovered'],ascending=False)


# In[55]:


data.sort_values(by=['Recovered'],ascending=False)


# In[56]:


data.sort_values(by=['Recovered'],ascending=False).head(10)


# In[ ]:




