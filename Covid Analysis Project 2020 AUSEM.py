#!/usr/bin/env python
# coding: utf-8

# # COVID-19 SMALL DATA SET ANALYSIS
# 
# 
# 
# This is a small/ sample data set intended for python usage and can be used for our project AUSEM2020-2021. We wll be working on some old data as new data isn't sufficient and also there are some problems in my pc with SSL Certificates.    The data used here is till 29 April 2020 and has records as on 29-April 2020.
# 
# The data is available in CSV file and downloaded from Kaggle
# 
# We will analyse this data using the Pandas Data Frame.

# In[1]:


import pandas as pd


# In[3]:


#Data IMporting
data=pd.read_csv(r"C:\Users\aryam\Downloads\4. covid_19_data.csv")


# In[4]:


#Having a look at it
data


# In[5]:


#Data Exploring
data.count()

#Null Values means Missing Values(Not in the form of decimals or numbers)


# In[6]:


data.isnull()
#True means its NUll
#false menas it's not NUll


# In[7]:


data.isnull().sum()
#Number of Null values in parameters


# In[8]:


import seaborn as sns


# In[9]:


import matplotlib.pyplot as plt


# In[10]:


sns.heatmap(data.isnull())


# In[12]:


sns.heatmap(data.isnull())
plt.show()


# # Number of Confirmed Deaths and Recovered cases in each Region

# In[14]:


data.head(3)


# In[15]:


data.groupby('Region')


# In[16]:


data.groupby('Region').sum()


# In[17]:


data.groupby('Region').sum().head(20)
#top 20


# In[18]:


data.groupby('Region')['Confirmed'].sum()


# In[20]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False)


# In[21]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending=True)


# In[22]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(10)
#Top 10


# In[23]:


data.groupby('Region')['Confirmed','Recovered'].sum()


# # Removing All Records where Confirmed Cases less than 10

# In[24]:


data.head(2)


# In[25]:


data.Confirmed<10


# In[26]:


data[data.Confirmed < 10]
#In form of Data Frame


# In[30]:


data[~(data.Confirmed < 10)]


# In[31]:


data


# In[32]:


data = data[~(data.Confirmed < 10)]  #Removing Records less than 10


# In[33]:


data


# In[34]:


data.head(20)


# # Region in which maximum number of cases were Recorded

# In[35]:


#Import Original Data Again


# In[36]:


data=pd.read_csv(r"C:\Users\aryam\Downloads\4. covid_19_data.csv")


# In[37]:


data


# In[38]:


data.head(2)


# In[39]:


data.groupby('Region').Confirmed.sum().sort_values(ascending = False)


# In[40]:


data.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(20)


# # Confirmed , Deaths & Recovered cases were reported from US till 29 April 2020?

# In[41]:


data.head(2)


# In[42]:


data.Region == 'US'


# In[43]:


data[data.Region == 'US']# in the form of data frame


# # Sort the Entire Data with respect to No. of Confirmed cases in ascending order

# In[45]:


data.head(10)


# In[46]:


data.sort_values(by = ['Confirmed'],ascending = True)


# In[47]:


data.sort_values(by = ['Confirmed'],ascending = True).head(50)


# # Sorting Entire Data with respect to number of Recovered Cases in Descending Order

# In[48]:


data.head(10)


# In[49]:


data.sort_values(by = ['Recovered'],ascending = False)


# In[55]:


data.sort_values(by = ['Recovered'],ascending = False).head(50)


# In[51]:


data.columns


# In[53]:


data.describe()


# # Some Visualisation

# # Relating Variables with scatterplots

# In[56]:


sns.relplot(x="Confirmed",y="Deaths",data=data)


# In[57]:


sns.relplot(x="Confirmed",y="Recovered",data=data)


# In[58]:


sns.relplot(x="Confirmed",y="Recovered",hue='Deaths',data=data)


# # A MORE DETAILED VISUALISATION

# In[59]:


sns.pairplot(data)


# In[61]:


sns.relplot(x='Confirmed' , y='Deaths',kind='line',data=data)


# In[62]:


sns.relplot(x='Confirmed' , y='Recovered',kind='line',data=data)


# In[64]:


sns.relplot(x='Deaths' , y='Recovered',kind='line',data=data)


# # Categorical Plots

# In[68]:


sns.catplot(x = 'Confirmed',y='Deaths',data=data)


# In[69]:


sns.catplot(x = 'Confirmed',y='Recovered',data=data)


# In[ ]:




