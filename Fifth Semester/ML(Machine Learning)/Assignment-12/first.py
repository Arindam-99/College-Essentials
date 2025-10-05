# Assignment 12: To encode categorical variables

# Import libraries
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Load Titanic dataset
df = sns.load_dataset("titanic")

# Select categorical columns
# Selects columns with object (string) or category dtype
categorical_cols = df.select_dtypes(include=['object', 'category']).columns
print("Categorical columns:", categorical_cols.tolist())

# Label Encoding example (for 'sex' column)
# Label Encoding is suitable for binary or ordinal data. 'sex' is binary.
label_encoder = LabelEncoder()
df['sex_encoded'] = label_encoder.fit_transform(df['sex'])
print("\nLabel Encoded 'sex':\n", df[['sex', 'sex_encoded']].head())

# One-Hot Encoding example (for 'class' column)
# One-Hot Encoding is suitable for nominal data with more than two categories. 'class' is nominal.
# drop_first=True avoids the dummy variable trap (perfect multicollinearity) by dropping one of the generated columns.
df_onehot = pd.get_dummies(df, columns=['class'], drop_first=True)
# Filter for the original 'class' column and the new one-hot encoded columns
print("\nOne-Hot Encoded 'class' (first 5 rows):\n", df_onehot.filter(like='class').head())