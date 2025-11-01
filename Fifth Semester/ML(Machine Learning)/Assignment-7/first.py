# Question : || Working with Pandas for DataFrame Visualization (plotting from CSV data) ||
#  Pandas DataFrame Visualization (from CSV data)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use the existing 'df' DataFrame (Titanic dataset)
print("First 5 rows of the dataset:")
print(df.head())  # Display first few rows

# Basic Info
print("\nBasic Info:")
print(df.info(), "\n")

# Summary statistics (only for numeric columns)
print("\nStatistical summary:")
print(df.describe(), "\n")

# Visualize distributions of numerical columns
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['age'].dropna(), bins=20, kde=True)
plt.title('Distribution of Age')

plt.subplot(1, 2, 2)
sns.histplot(df['fare'], bins=20, kde=True)
plt.title('Distribution of Fare')
plt.tight_layout()
plt.show()

# Visualize relationships between categorical and numerical columns
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.boxplot(x='survived', y='age', data=df)
plt.title('Survival by Age')

plt.subplot(1, 2, 2)
sns.boxplot(x='survived', y='fare', data=df)
plt.title('Survival by Fare')
plt.tight_layout()
plt.show()

# Visualize counts of categorical columns
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.countplot(x='survived', data=df)
plt.title('Survival Count')

plt.subplot(1, 2, 2)
sns.countplot(x='pclass', data=df)
plt.title('Passenger Count by Class')
plt.tight_layout()
plt.show()