
# Assignment 21: To compare decision tree and random forest models

import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = sns.load_dataset("titanic")  # Dataset

data = df[['survived', 'pclass', 'sex', 'age', 'fare', 'embarked']].dropna() # Relevant features

# Encode categorical variables
le = LabelEncoder()
data['sex'] = le.fit_transform(data['sex'])
data['embarked'] = le.fit_transform(data['embarked'])

X = data[['pclass', 'sex', 'age', 'fare', 'embarked']]  # Feature
y = data['survived']  # Target

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42) # Train-test split

# Initialize models
dt = DecisionTreeClassifier(max_depth=4, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train models
dt.fit(X_train, y_train)
rf.fit(X_train, y_train)

# Predictions
y_pred_dt = dt.predict(X_test)
y_pred_rf = rf.predict(X_test)

# Comparison Table
results = pd.DataFrame({
    "Model": ["Decision Tree", "Random Forest"],
    "Accuracy": [accuracy_score(y_test, y_pred_dt), accuracy_score(y_test, y_pred_rf)],
    "Precision": [precision_score(y_test, y_pred_dt), precision_score(y_test, y_pred_rf)],
    "Recall": [recall_score(y_test, y_pred_dt), recall_score(y_test, y_pred_rf)],
    "F1 Score": [f1_score(y_test, y_pred_dt), f1_score(y_test, y_pred_rf)]
})

print("Model comparison:\n")
print(results)