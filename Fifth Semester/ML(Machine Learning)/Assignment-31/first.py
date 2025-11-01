# Import libraries
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

df = sns.load_dataset("titanic") # Load dataset

data = df[['survived', 'pclass', 'sex', 'age', 'fare']].dropna() # Select relevant columns

# Encode categorical variable
le = LabelEncoder()
data['sex'] = le.fit_transform(data['sex']) # male=1, female=0

# Split features and target
X = data[['pclass', 'sex', 'age', 'fare']]
y = data['survived']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# --- Bagging Classifier ---
bagging = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=10, random_state=42)
bagging.fit(X_train, y_train)
y_pred_bag = bagging.predict(X_test)
print("Bagging Classifier Results:")
print(f"Accuracy:", accuracy_score(y_test, y_pred_bag))
print(classification_report(y_test, y_pred_bag))

# --- Boosting Classifier (AdaBoost) ---
boosting = AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1), n_estimators=50, learning_rate=1.0, random_state=42)
boosting.fit(X_train, y_train)
y_pred_boost = boosting.predict(X_test)
print("\nBoosting (AdaBoost) Results:")
print(f"Accuracy:", accuracy_score(y_test, y_pred_boost))
print(classification_report(y_test, y_pred_boost))