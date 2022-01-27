import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

# TAKING THE COLUMNS WHICH ARE TO USED FOR TRAINING THE MODEL
# 16 MARCH-MAY
# 22- AVG OF 10 DAYS JUNE
# 23- DIFFERENCE OF RAINFALL FROM MAY TO JUNE
# 20 - BINARY CLASS OF FLOOD- 0 OR 1
# MORE DATA CAN BE ADDED FOR TRAINING, BY JUST ADDING MORE NUMBER OF COLUMNS FROM THE CSV FILE
# WE USE LOGISTIC REGRESSION FOR TRAINING

x = pd.read_csv("out1.csv")
X = x.iloc[:, [16, 22, 23, 19]]
y1 = x.iloc[:, 20]

# (X_train, X_test, Y_train, Y_test) = train_test_split(X, y1, random_state=0)

lr = LogisticRegression()

lr.fit(X, y1)

# saving model to disk
pickle.dump(lr, open('model2.pkl', 'wb'))

# loading model to compare results
model = pickle.load(open('model2.pkl', 'rb'))

