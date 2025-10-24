# Assignment 20: To build and visualize decision trees

# Import libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix

df = sns.load_dataset("titanic")

print("\nMissing values:\n", df.isnull().sum())

# Categorical columns
data = df[['survived', 'pclass', 'sex', 'age', 'fare', 'embarked']]

# Handle missing values
data = data.dropna()

# Encode categorical variables
le = LabelEncoder()
data['sex'] = le.fit_transform(data['sex'])
data['embarked'] = le.fit_transform(data['embarked'])

# Define features and target
X = data[['pclass', 'sex', 'age', 'fare', 'embarked']]
y = data['survived']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Model Training
dt_model = DecisionTreeClassifier(max_depth=4, random_state=42)
dt_model.fit(X_train, y_train)

# Model Predictions
y_pred = dt_model.predict(X_test)

# Model Evaluation
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Visualize Decision Tree
plt.figure(figsize=(16,10))
plot_tree(dt_model, feature_names=['pclass', 'sex', 'age', 'fare', 'embarked'], class_names=['Not Survived', 'Survived'], filled=True, fontsize=10)
plt.show()