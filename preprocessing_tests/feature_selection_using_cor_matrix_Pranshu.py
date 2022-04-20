#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# In[2]:


df = pd.read_csv("data_frame_records.csv")


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.isnull().sum()


# ## Drop the Below columns as they do not Contribute in prediction

# In[6]:


df = df.drop(['_id','link','display_name','email'],axis=1)


# In[7]:


## Check For Correlation Matrix

#Plotting correlation Heatmap
plt.figure(figsize=(12,10))
corr_plot = sns.heatmap(df.corr(),cmap="YlGnBu",annot=True)

#Displaying Heatmap
plt.show()


# In[8]:


# With the following function we can select highly correlated features using a threshold values
# It will remove the first feature that is correlated with any other feature.

def correlation(dataset, threshold):
    col_corr = set()
    corr_matrix = dataset.corr()
    for x in range(len(corr_matrix.columns)):
        for y in range(x):
            if corr_matrix.iloc[x,y] > threshold:     # Absolute Coefficient Value
                col_name = corr_matrix.columns[x]          # Get the name of the column
                col_corr.add(col_name)
    return col_corr


# In[9]:


corr_features = correlation(df, 0.90)
len(set(corr_features))


# In[10]:


corr_features


# In[11]:


df_new = df.drop(corr_features,axis=1)


# ## Applying StandardScaler

# In[12]:


X = StandardScaler().fit_transform(df_new)
X


# ## Applying KMeans

# In[13]:


kmeans = KMeans(n_clusters=2, init ='k-means++', n_init = 10, max_iter = 300,random_state = 47)


# In[14]:


kmeans.fit(X)


# In[15]:


kmeans.labels_


# In[16]:


df['Selected'] = [True if label == 1 else False for label in kmeans.labels_]


# In[17]:


df['Selected'].value_counts()


# In[25]:


###Splitting the data in test and train
train_x, test_x, train_y, test_y = train_test_split(X, df['Selected'], test_size=0.4)


# In[29]:


### Logistic - Yet to try
from sklearn.linear_model import LogisticRegression

# Create model
model = LogisticRegression(solver='liblinear')

# Fit the model
model.fit(train_x, train_y)


# In[39]:


model.score(train_x,train_y)

threshold = 0.5

pred_y = model.predict(test_x)

prob_pred_y = (model.predict_proba(test_x)[:,1] > threshold).astype(int)

print(prob_pred_y)

x =0 
y =0
for n in prob_pred_y:
    if n == 0:
        x = x+1
    else:
        y=y+1

print("Count of 0 = ",x) 
print("Count of 1 = ",y) 

model.score(test_x,test_y)


# In[ ]:




