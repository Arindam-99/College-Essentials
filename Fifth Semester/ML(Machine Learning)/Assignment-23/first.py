# Assignment 23: To split data using training/test and cross-validation methods

# Import libraries
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = sns.load_dataset("titanic")

# Select relevant features and drop missing values
data = df[['survived', 'sex', 'age', 'pclass']].dropna()

# Encode categorical variable
le = LabelEncoder()
data['sex'] = le.fit_transform(data['sex'])

# Features and target
X = data[['sex', 'age', 'pclass']]
y = data['survived']

# --- Train-Test Split Method ---

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = model.predict(X_test)
print("=== Train-Test Split Evaluation ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")


# --- Cross-Validation Method ---

# Note: We use the *full* X and y datasets for cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')

print("\n=== K-Fold Cross-Validation Evaluation ===")
for i, score in enumerate(cv_scores, 1):
    print(f"Fold {i}: {score * 100:.2f}%")

print(f"Mean Accuracy: {cv_scores.mean() * 100:.2f}%")