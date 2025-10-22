# Assignment 18: To compute confusion matrix, precision, recall, and F1 score

# Import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, f1_score, recall_score, confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv("sonar data.csv", header=None)

X = df.drop(columns=[60])
y = df[60]

le = LabelEncoder()
y = le.fit_transform(y)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred_log = log_reg.predict(X_test)

# Model Evaluation
print("Precision:", precision_score(y_test, y_pred_log))
print("F1 Score:", f1_score(y_test, y_pred_log))
print("Recall:", recall_score(y_test, y_pred_log))

# Confusion Matrix
cm_lr = confusion_matrix(y_test, y_pred_log)
disp_lr = ConfusionMatrixDisplay(cm_lr, display_labels=np.unique(y))
disp_lr.plot()
plt.title("Confusion Matrix - Logistic Regression")
plt.show()