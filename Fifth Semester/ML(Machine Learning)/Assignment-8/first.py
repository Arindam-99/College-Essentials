# Question : ||Real-world Dataset Visualization: Exploratory Data Analysis (e.g., Titanic Data)||
# titanic_eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load Dataset
# -----------------------------
# Titanic dataset is available in seaborn
titanic = sns.load_dataset("titanic")

print("First 5 rows of dataset:")
print(titanic.head())

# Step 2: Basic Info
# -----------------------------
print("\nDataset Info:")
print(titanic.info())

print("\nMissing Values:")
print(titanic.isnull().sum())

# Step 3: Univariate Analysis
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="survived", data=titanic, palette="Set2")
plt.title("Survival Count (0 = Died, 1 = Survived)")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x="sex", data=titanic, palette="Set1")
plt.title("Gender Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(titanic["age"].dropna(), bins=30, kde=True, color="blue")
plt.title("Age Distribution")
plt.show()

# Step 4: Bivariate Analysis
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="pclass", hue="survived", data=titanic, palette="Set3")
plt.title("Survival by Passenger Class")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x="sex", hue="survived", data=titanic, palette="Set2")
plt.title("Survival by Gender")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x="survived", y="age", data=titanic, palette="Set1")
plt.title("Age vs Survival")
plt.show()

# Step 5: Correlation Heatmap
# -----------------------------
plt.figure(figsize=(8,6))
sns.heatmap(titanic.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# Step 6: Multivariate - Survival by Class & Gender
# -----------------------------
plt.figure(figsize=(8,6))
sns.catplot(x="pclass", hue="sex", col="survived",
            data=titanic, kind="count", palette="Set2")
plt.subplots_adjust(top=0.8)
plt.suptitle("Survival by Passenger Class & Gender")
plt.show()
