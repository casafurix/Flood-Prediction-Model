# importing the libraries
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
import pandas as pd
import pickle

dataset = pd.read_csv("Datasets/Kerala_modified_dataset.csv")

X = dataset.iloc[:, 1:6]
y = dataset.iloc[:, -1]

# splitting training and test set
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# feature scaling
standardscaler = StandardScaler()
# X_train = standardscaler.fit_transform(X_train)
# X_test = standardscaler.transform(X_test)
X = standardscaler.fit_transform(X)

# instantiating the model
lr = LinearRegression()

# fitting model with training data
lr.fit(X, y)

# saving model to disk
pickle.dump(lr, open('model.pkl', 'wb'))

# loading model to compare results
model = pickle.load(open('model.pkl', 'rb'))
