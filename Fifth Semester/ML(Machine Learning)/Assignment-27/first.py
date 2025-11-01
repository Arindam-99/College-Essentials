import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle, joblib

# Load dataset
df = sns.load_dataset('titanic')
data = df[['survived', 'sex', 'age', 'pclass']].dropna()

# Encode categorical data
le = LabelEncoder()
data['sex'] = le.fit_transform(data['sex'])

# Split into features and target
X = data[['sex', 'age', 'pclass']]
y = data['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train a model
model = LogisticRegression()
model.fit(X_train, y_train)

# ---- SAVE MODEL ----
# Method 1: Using Pickle
with open('logistic_model.pkl', 'wb') as file: pickle.dump(model, file)

# Method 2: Using Joblib
joblib.dump(model, 'logistic_model.joblib')

print("Models saved successfully!")

# ---- LOAD MODEL ----
# Load Pickle model
with open('logistic_model.pkl', 'rb') as file: loaded_model_pickle = pickle.load(file)

# Load Joblib model
loaded_model_joblib = joblib.load('logistic_model.joblib')

# --- VERIFY LOADED MODELS ----
# Make predictions using loaded models
print("\nPickle model prediction:", loaded_model_pickle.predict(X_test[:5]))
print("Joblib model prediction:", loaded_model_joblib.predict(X_test[:5]))