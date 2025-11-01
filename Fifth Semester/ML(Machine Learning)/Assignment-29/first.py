# Assignment 29: Spam Email Classification

# 1. Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2. Load Dataset
# You can replace this with your dataset path if downloaded
data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv", sep='\t', header=None)
data.columns = ['label', 'message']

# 3. Encode labels
data['label_num'] = data.label.map({'ham':0, 'spam':1})

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(
    data['message'], data['label_num'], test_size=0.2, random_state=42)

# 5. Convert text to numeric vectors
vectorizer = CountVectorizer(stop_words='english')
X_train_dtm = vectorizer.fit_transform(X_train)
X_test_dtm = vectorizer.transform(X_test)

# 6. Train Model
model = MultinomialNB()
model.fit(X_train_dtm, y_train)

# 7. Make Predictions
y_pred = model.predict(X_test_dtm)

# 8. Evaluate Model
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
