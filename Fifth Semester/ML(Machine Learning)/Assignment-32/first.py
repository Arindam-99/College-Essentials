# Import libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

df = sns.load_dataset("titanic") # Load dataset

data = df[['survived', 'pclass', 'sex', 'age', 'fare', 'embarked']].dropna() # Select features

# Encode categorical variables
le = LabelEncoder()
data['sex'] = le.fit_transform(data['sex'])
data['embarked'] = le.fit_transform(data['embarked'])

# Define features and target
X = data[['pclass', 'sex', 'age', 'fare', 'embarked']]
y = data['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # Split data

# Train Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test) # Predictions

# Evaluation
print(f"Accuracy:", accuracy_score(y_test, y_pred))
print(f"\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
disp = ConfusionMatrixDisplay.from_estimator(rf_model, X_test, y_test)
disp.ax_.set_title("Confusion Matrix - Random Forest")
plt.show()

# Feature Importance
importances = rf_model.feature_importances_
feature_names = X.columns

plt.figure(figsize=(6,4))
plt.barh(feature_names, importances, color='skyblue')
plt.xlabel("Importance Score")
plt.title("Feature Importance (Random Forest)")
plt.show()