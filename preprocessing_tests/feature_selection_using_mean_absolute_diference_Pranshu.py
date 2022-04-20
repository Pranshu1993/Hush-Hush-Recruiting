#!/usr/bin/env python
# coding: utf-8

# In[131]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans


# In[91]:


df = pd.read_csv("data_frame_records.csv")


# In[92]:


df.shape


# In[93]:


df.head()


# In[94]:


df.isnull().sum()


# In[95]:


#Check For Correaltion
df.corr()

#Plotting correlation Heatmap
corr_plot = sns.heatmap(df.corr(),cmap="YlGnBu",annot=True)

#Displaying Heatmap
plt.show()

##### INcrease the size of Heatmap


# In[96]:


#Df for Boxplot(Numerical) Columns
df_new = df.drop(['_id','link','display_name','email'],axis=1)


# In[97]:


df_new.columns


# In[119]:


### We should Apply Log function here
pd.set_option('display.max_rows', 32000)
# print(df_new['reputation'])
df_new['reputation'].value_counts()


# In[118]:


### Most of the values are 0 or negative---> Does not make sense to apply log here
pd.set_option('display.max_rows', 32000)
# print(df_new['reputation_change_quarter'])
df_new['reputation_change_quarter'].value_counts()


# In[117]:


#### Does not make sense to apply log here as many values are zero 
pd.set_option('display.max_rows', 32000)
# print(df_new['view_count'])
df_new['view_count'].value_counts()


# In[116]:


### Does not make sense to Apply log
# print(df_new['answer_count'])
df_new['answer_count'].value_counts()


# In[120]:


###Does not make sense to apply Log
df_new['bronze'].value_counts()


# In[121]:


###Does not make sense to apply Log
df_new['silver'].value_counts()


# In[122]:


###Does not make sense to apply Log
df_new['gold'].value_counts()


# ## Apply Log in 'Reputation' column

# In[125]:


df_new['Log_reputation'] = np.log(df_new['reputation'])
df_new['Log_reputation'].value_counts()


# In[126]:


df_new = df_new.drop(['reputation'],axis=1)


# In[128]:


df_new.head()


# ## Applying Standard Scaler on df_new 

# In[130]:


X = StandardScaler().fit_transform(df_new)
X


# ## Applying KMeans 

# In[134]:


kmeans = KMeans(n_clusters=2,init = 'random', n_init = 10, max_iter = 300,random_state = 47)


# In[135]:


kmeans.fit(X)


# In[136]:


kmeans.labels_


# In[140]:


df_new['Selected'] = [True if label == 1 else False for label in kmeans.labels_]


# In[142]:


df_new['Selected'].value_counts()


# In[123]:


# df_new['log_view_count'] = np.log10(df_new['view_count'])
# df_new['log_answer_count'] = np.log10(df_new['answer_count'])
# df_new['log_question_count'] = np.log10(df_new['question_count'])
# df_new['log_reputation_change_quarter'] = np.log10(df_new['reputation_change_quarter'])
# df_new['log_reputation'] = np.log10(df_new['reputation'])
# df_new['log_bronze'] = np.log10(df_new['bronze'])
# df_new['log_silver'] = np.log10(df_new['silver'])
# df_new['log_gold'] = np.log10(df_new['gold'])


# In[ ]:


# #Find the upper Limit & Lower Limit 
# upper_limit_gold = df['gold'].quantile(0.96)
# upper_limit_silver =df['silver'].quantile(0.96) 
# upper_limit_bronze = df['bronze'].quantile(0.96)
# # lower_limit = df['gold'].quantile(0.01)

# print(upper_limit_gold)
# print(upper_limit_silver)
# print(upper_limit_bronze)
# # print(lower_limit)


# In[47]:


# df_update = df_new[(df_new['gold']>=upper_limit_gold) & (df_new['silver']>=upper_limit_gold) & (df_new['bronze']>=upper_limit_gold) ]


# In[48]:


# print(df_update)
# print(df_update.shape)
# df_update.head()


# In[49]:


#StandarScaler
from sklearn.preprocessing import StandardScaler


# In[50]:


# df1 = df_update[['question_count','reputation']]


# In[61]:


X = StandardScaler().fit_transform(df_new)
import math
Y = np.log(X)
print(Y)


# In[53]:


# Y = StandardScaler().fit_transform(df1)
# Y


# In[55]:


X.shape


# ### Mean Absolute Difference

# In[57]:


mean_abs_diff = np.sum(np.abs(X - np.mean(X, axis=0)), axis=0)/X.shape[0]


# In[58]:


print(mean_abs_diff)


# In[18]:


type(X)


# In[19]:


plt.bar(np.arange(X.shape[1]),mean_abs_diff,color='teal')
plt.xlabel(X)


# In[ ]:




