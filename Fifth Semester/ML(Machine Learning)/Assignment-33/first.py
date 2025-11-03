# Assignment 33: Implement XGBoost or LightGBM for Classification...
# Install libraries
!pip install xgboost lightgbm --quiet

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import xgboost as xgb
import lightgbm as lgb
import matplotlib.pyplot as plt

df = pd.read_csv("wineQuality.csv")  # Load dataset
print(df.head())

# Convert quality to binary classification (Good vs Not Good)
df['quality'] = (df['quality'] >= 7).astype(int)  # quality >=7 are 'Good'(1), otherwise 'Not Good'(0)

# Split into features and target
X = df.drop(['quality'], axis=1)
y = df['quality']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Feature scaling
scaler = StandardScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

# Train XGBoost model
xgb_model = xgb.XGBClassifier(eval_metric='logloss', random_state=42)
xgb_model.fit(X_train, y_train)
xgb_pred = xgb_model.predict(X_test)

# Train LightGBM model
lgb_model = lgb.LGBMClassifier(objective='binary', metric='accuracy', random_state=42, verbose=-1)
lgb_model.fit(X_train, y_train)
lgb_pred = lgb_model.predict(X_test)

# Model Evaluation
print("=== XGBoost Results ===")
print("Accuracy:", accuracy_score(y_test, xgb_pred))
print(confusion_matrix(y_test, xgb_pred))
print(classification_report(y_test, xgb_pred))

print("\n=== LightGBM Results ===")
print("Accuracy:", accuracy_score(y_test, lgb_pred))
print(confusion_matrix(y_test, lgb_pred))
print(classification_report(y_test, lgb_pred))