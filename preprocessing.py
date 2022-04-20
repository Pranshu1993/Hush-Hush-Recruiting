from utils import read_records, create_collection, simple_eda
import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression


def correlation(dataset, threshold):
    '''Returns name of columns to drop due to high correlation with other features'''
    col_corr = set()
    corr_matrix = dataset.corr()
    for x in range(len(corr_matrix.columns)):
        for y in range(x):
            if corr_matrix.iloc[x,y] > threshold:     # Absolute Coefficient Value
                col_name = corr_matrix.columns[x]     # Get the name of the column
                col_corr.add(col_name)
    return col_corr


# Creating the Dataframe ----------------------------------------
# Connect to the Stackoverflow Mongodb collection
stackoverflow = create_collection('Stackoverflow')

# Transform and save the data in a pandas dataframe
records = [record for record in read_records(stackoverflow)]
df = pd.DataFrame(records)
df = df.set_index('_id')
# Mapping the badge_count dictionary column into new columns
df = pd.concat([df.drop(['badge_counts'], axis=1),
                df['badge_counts'].apply(pd.Series)], axis=1)

# Data Understanding --------------------------------------------
# simple_eda(df)

# Preprocessing -------------------------------------------------
# Selecting our models features

corr_features = correlation(df, 0.9)
new_df = df.drop(corr_features, naxis=1)

features = new_df.select_dtypes(include=['int64', 'float', 'int'])

# Feature scaling with standardization
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Reducing our dimensions with PCA
# X_pca = PCA().fit_transform(scaled_features)
# X_selected = X_pca[:, :2]

# Scatter plot of our datapoints in the PCA dimensions
# plt.figure(figsize=(10, 5))
# plt.title('Scatter Plot of our PCA Dimensions')
# plt.xlabel('Dimension 1')
# plt.ylabel('Dimension 2')
# plt.scatter(X_pca[:, 0], X_pca[:, 1])
# plt.show()

# Running a K-means cluster to create a new 'Selected' column
kmeans = KMeans(init="random", n_clusters=2, n_init=10,
                max_iter=300, random_state = 47)
kmeans.fit(scaled_features)

# Appending the new 'Selected' column to the dataframe
df['Selected'] = [True if label == 1 else False for label in kmeans.labels_]

# Print number of Selected and not selected candidates
# print(df['Selected'].value_counts())


# Modelling ---------------------------------------------------
# Defining our prediction variable and features
y = df['Selected']
x = scaled_features

# Splitting the data in test and train
train_x, testing_x, train_y, testing_y = train_test_split(x, y, test_size=0.4)

# Splitting the test data into test and validation (test_size default = 0.25)
test_x, val_x, test_y, val_y = train_test_split(testing_x, testing_y)

# Create model
model = LogisticRegression(solver='liblinear')

# Fit the model
model.fit(train_x, train_y)


# Testing -----------------------------------------------------
# Get model score on training data
model.score(train_x, train_y)

# Get confusion matrix on test data
confusion_matrix(test_y, model.predict(test_x))
# Confusion matrix output format:
# ([True Positive, False Negative]
#  [False Posiive, True Negative]])

# After making changes to the model to improve the results
# on the test data we can measure it on the validation data
confusion_matrix(val_y, model.predict(val_x))
