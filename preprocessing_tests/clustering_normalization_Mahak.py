from utils import read_records, create_collection, simple_eda
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
import numpy as np



# Creating the Dataframe ----------------------------------------
# Connect to the Stackoverflow Mongodb collection
stackoverflow = create_collection('Stackoverflow')

# Transform and save the data in a pandas dataframe
records = [record for record in read_records(stackoverflow)]
df = pd.DataFrame(records)
# print(df)
df = df.set_index('_id')
# Mapping the badge_count dictionary column into new columns
df = pd.concat([df.drop(['badge_counts'], axis=1),
                df['badge_counts'].apply(pd.Series)], axis=1)

# df['log_reputation_change_quarter'] = np.log10(df['reputation_change_quarter'])
# df['log_reputation'] = np.log10(df['reputation'])
# df['log_bronze'] = np.log10(df['bronze'])
# df['log_silver'] = np.log10(df['silver'])
# df['log_gold'] = np.log10(df['gold'])

# for col in df.columns:
#     print(col)

# Data Understanding --------------------------------------------
print(simple_eda(df))

# Preprocessing -------------------------------------------------
# Selecting our models features
features = df.select_dtypes(include=['int64', 'float', 'int'])
features.head()
# # Feature scaling with standardization
scaler = MinMaxScaler()
features[['view_count', 'answer_count', 'reputation_change_quarter', 'reputation']] = scaler.fit_transform(features[['view_count', 'answer_count', 'reputation_change_quarter', 'reputation']])
# print(features)
# ordinal_encoder = OneHotEncoder()
#
# # preprocess the features Product and ZipCode
# features[['bronze', 'silver', 'gold']]= ordinal_encoder.fit_transform(features[['bronze', 'silver', 'gold']])
print(features)

# Reducing our dimensions with PCA
# X_pca = PCA().fit_transform(scaled_features)
# X_selected = X_pca[:, :2]
# print(X_pca)
# print(X_selected)

# # Scatter plot of our datapoints in the PCA dimensions
# plt.figure(figsize=(10, 5))
# plt.title('Scatter Plot of our PCA Dimensions')
# plt.xlabel('Dimension 1')
# plt.ylabel('Dimension 2')
# plt.scatter(X_pca[:, 0], X_pca[:, 1])
# plt.show()

# Running a K-means cluster to create a new 'Selected' column
kmeans = KMeans(n_clusters=2)
kmeans.fit(features[['view_count', 'answer_count', 'reputation_change_quarter', 'reputation']])
print(kmeans.labels_)
#
# # Appending the new 'Selected' column to the dataframe
df['Selected'] = [True if label == 1 else False for label in kmeans.labels_]
#
# # Print number of Selected and not selected candidates
print(df['Selected'].value_counts())

# plt.title("KMeans clusters")
# # #
# plt.xlabel('reputation_change_quarter')
# plt.ylabel('reputation')
# # #
# plt.scatter(features['reputation_change_quarter'], features['reputation'], c=kmeans.labels_)
# # #
# plt.show()


# # Modelling ---------------------------------------------------
# # Defining our prediction variable and features
y = df['Selected']
x = features
#
# # Splitting the data in test and train
train_x, testing_x, train_y, testing_y = train_test_split(x, y, test_size=0.4)
#
# # Splitting the test data into test and validation (test_size default = 0.25)
test_x, val_x, test_y, val_y = train_test_split(testing_x, testing_y)
#
# # Create model
model = LogisticRegression(solver='liblinear')
#
# # Fit the model
model.fit(train_x, train_y)
#
#
# # Testing -----------------------------------------------------
# # Get model score on training data
model.score(train_x, train_y)
#
# # Get confusion matrix on test data
confusion_matrix(test_y, model.predict(test_x))
# # Confusion matrix output format:
# # ([True Positive, False Negative]
# #  [False Posiive, True Negative]])
#
# # After making changes to the model to improve the results
# # on the test data we can measure it on the validation data
confusion_matrix(val_y, model.predict(val_x))
