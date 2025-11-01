# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#  Load the SONAR dataset directly from UCI
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
df = pd.read_csv(url, header=None)

# Separate features (X) and target (y)
X = df.drop(columns=[60])
y = df[60]

# Encode labels (M = 0, R = 1)
le = LabelEncoder()
y = le.fit_transform(y)

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

# Model Training
log_reg = LogisticRegression(max_iter=1000)  # Added max_iter for convergence
log_reg.fit(X_train, y_train)

# Model Predictions
y_pred_log = log_reg.predict(X_test)

# Display first 10 predictions
print(f"Predictions (Logistic Regression - first 10): {y_pred_log[:10]}")

# Optional: print accuracy
print(f"Accuracy: {accuracy_score(y_test, y_pred_log):.4f}")
