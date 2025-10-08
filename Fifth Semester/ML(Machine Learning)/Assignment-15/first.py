# Assignment 15: To implement linear regression using scikit-learn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Import Data
df = pd.read_csv('BostonHousing.csv')

# Features (X) and Target (y)
X = df.drop("MEDV", axis=1)
y = df["MEDV"]

# Split the dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Linear Regression model
model = LinearRegression()

# Train the model on training data
model.fit(X_train, y_train)

# Predict on testing data
y_pred = model.predict(X_test)
print("Predicted values (first 5):", y_pred[:5])
print("Actual values (first 5):", y_test[:5].values)