# Assignment 34: Build a Voting Ensemble with Multiple Models
# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

data = load_iris()  # Load dataset
X, y = data.data, data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create base models
log_reg = LogisticRegression(max_iter=200)
dt = DecisionTreeClassifier(random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Voting Classifier
voting_clf = VotingClassifier(estimators=[('lr', log_reg), ('dt', dt), ('rf', rf)], voting='hard')

# Train and evaluate
voting_clf.fit(X_train, y_train)
y_pred = voting_clf.predict(X_test)
print("Voting Ensemble Accuracy:", accuracy_score(y_test, y_pred))
