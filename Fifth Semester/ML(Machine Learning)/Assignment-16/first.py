import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Import Data
df = pd.read_csv('BostonHousing.csv')

# Features (X) and Target (y)
X = df.drop("MEDV", axis=1)
y = df["MEDV"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error (MAE):", mae)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE):", mse)

rmse = np.sqrt(mse)
print(f"Root Mean Squared Error (RMSE):", rmse)

r2 = r2_score(y_test, y_pred)
print(f"R2 Score:", r2)