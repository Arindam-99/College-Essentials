# ASSIGNMENT 11: To clean datasets and handle missing values

# Library Functions
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('titanic')

# Display first few rows
print("\nFirst few rows:")
print(df.head(), "\n")

# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum(), "\n")

# Handle Missing Values

# Method 1: Drop rows with missing values in a specific column (example: 'age')
df_age_clean = df.dropna(subset=['age'])
print("\nAfter dropping rows with missing age values, the shape of the clean dataset:", df_age_clean.shape)

# Method 2: Fill missing numerical values with mean
df['age'] = df['age'].fillna(df['age'].mean())
print("\nAfter filling 'age' missing values with mean:")
print(df['age'])

# Method 3: Fill missing categorical values with mode
# Note: The mode() method returns a Series, so we use [0] to get the first mode.
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
print("\nAfter filling 'embarked' missing values with mode:")
print(df['embarked'])

# Method 4: Drop entire columns if too many missing values (example: 'deck')
# 'deck' has 688 missing values (from the image's output), which is a large portion.
df = df.drop(columns=['deck'])
print("\nAfter dropping 'deck' column:")
print(df.head())

# Verify no missing values remain
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Display cleaned dataset shape
print("\nFinal dataset shape:", df.shape)