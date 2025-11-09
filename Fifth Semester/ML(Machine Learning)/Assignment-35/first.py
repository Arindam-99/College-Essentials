# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.metrics import accuracy_score

data = load_iris() # Load dataset
X, y = data.data, data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Base models
base_models = [('decision_tree', DecisionTreeClassifier(random_state=42)),
               ('random_forest', RandomForestClassifier(n_estimators=100, random_state=42))]

# Meta model (final layer)
meta_model = LogisticRegression(max_iter=200)

# Create stacking model
stacking_clf = StackingClassifier(estimators=base_models, final_estimator=meta_model)

# Train and evaluate
stacking_clf.fit(X_train, y_train)
y_pred = stacking_clf.predict(X_test)
print("Stacking Ensemble Accuracy:", accuracy_score(y_test, y_pred))