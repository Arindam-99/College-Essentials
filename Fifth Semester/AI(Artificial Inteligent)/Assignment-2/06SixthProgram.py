# vi. Naive Bayes Classifier using sklearn (Iris)
try:
 from sklearn.datasets import load_iris
 from sklearn.model_selection import train_test_split
 from sklearn.naive_bayes import GaussianNB
 from sklearn.metrics import accuracy_score
 iris = load_iris()
 X = iris.data; y = iris.target
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
 model = GaussianNB()
 model.fit(X_train, y_train)
 y_pred = model.predict(X_test)
 acc = accuracy_score(y_test, y_pred)
 print("Predictions:", list(y_pred))
 print("Actual Labels:", list(y_test))
 print("\nAccuracy of Naive Bayes Classifier:", round(acc, 3))
except Exception as e:
 print("sklearn-based example could not run in this environment:", e)