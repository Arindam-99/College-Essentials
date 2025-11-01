# Load the dataset from the downloaded file
df = pd.read_csv("BostonHousing.csv", header=None, names=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'], delim_whitespace=True)

# The rest of the code from the original cell
X = df.drop(columns=['MEDV']) # Features
y = df['MEDV'] # Target

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- KNN Classification ---
# Convert regression target into binary classification
median_price = np.median(y)
y_class = (y > median_price).astype(int) # 1 = expensive, 0 = cheap

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_class, test_size=0.3, random_state=42)

# KNN Classifier Model
knn_clf = KNeighborsClassifier(n_neighbors=5)
knn_clf.fit(X_train, y_train)
y_pred_class = knn_clf.predict(X_test)

# Evaluation
print("KNN Classification Results:")
print(confusion_matrix(y_test, y_pred_class))
print(classification_report(y_test, y_pred_class))


# --- KNN Regression ---
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# KNN Regressor Model
knn_reg = KNeighborsRegressor(n_neighbors=5)
knn_reg.fit(X_train, y_train)
y_pred_reg = knn_reg.predict(X_test)

# Evaluation
print("\nKNN Regression Results:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred_reg))
print("R2 Score:", r2_score(y_test, y_pred_reg))