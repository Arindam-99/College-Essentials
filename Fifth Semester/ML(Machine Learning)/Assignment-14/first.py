# Assignment 14: To split datasets into training and testing sets
import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset from an online source (no local file needed)
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(url)

# Features (X) and Target (y)
X = df.drop("medv", axis=1)   # Note: column name is lowercase "medv" in this version
y = df["medv"]

# Split the dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display dataset sizes
print("Training set size:", X_train.shape)
print("Testing set size:", X_test.shape)
