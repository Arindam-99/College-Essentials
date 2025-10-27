# Assignment 22: To apply cross-validation techniques

# Import library
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score

# Load dataset
df = sns.load_dataset("titanic")

# Select relevant features and drop missing values
data = df[['survived', 'sex', 'age', 'pclass']].dropna()

# Encode categorical column (sex)
le = LabelEncoder()
data['sex'] = le.fit_transform(data['sex'])

# Features and Target
X = data[['sex', 'age', 'pclass']] 
y = data['survived'] 

# Model Training
model = LogisticRegression() 

# k-fold cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
cross_val_results = cross_val_score(model, X, y, cv=kf)

# Evaluation metrics
print("Cross-Validation Results (Accuracy):")
for i, result in enumerate(cross_val_results, 1):
    print(f"  Fold {i}: {result * 100:.2f}%")

print(f"Mean Accuracy: {cross_val_results.mean() * 100:.2f}%")