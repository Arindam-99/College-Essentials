#  Assignment : 24 : To use Decision trees and random forests for prediction
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = sns.load_dataset("titanic") # dataset

data = df[['survived', 'pclass', 'sex', 'age', 'fare', 'embarked']].dropna() # Select the useful columns

# Encode categorical variables
le = LabelEncoder()
data['sex'] = le.fit_transform(data['sex'])
data['embarked'] = le.fit_transform(data['embarked'])

X = data[['pclass', 'sex', 'age', 'fare', 'embarked']] # Features
y = data['survived'] # Target

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42) #Split

# Decision Tree
dt_model = DecisionTreeClassifier(max_depth=4, random_state=42)

dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)
print("Decision Tree Accuracy =", accuracy_score(y_test, y_pred_dt))

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
print("Random Forest Accuracy =", accuracy_score(y_test, y_pred_rf))