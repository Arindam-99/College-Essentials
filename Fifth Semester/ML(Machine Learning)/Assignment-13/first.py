# Assignment 13: To scale features using standard and min-max techniques

# Import libraries
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Load Titanic dataset
df = sns.load_dataset('titanic')

# Select numerical columns
# Selects columns with integer or float dtype
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
print("Numeric columns:", numeric_cols.tolist())

# Drop rows with missing values for simplicity
# This ensures that the scaling is performed only on rows with complete numerical data.
df_num = df[numeric_cols].dropna()

# Standard Scaling
# Standard Scaler (Z-score normalization) scales data to have a mean of 0 and a standard deviation of 1.
scaler_standard = StandardScaler()
df_standard_scaled = scaler_standard.fit_transform(df_num)

# Convert back to DataFrames
df_standard = pd.DataFrame(df_standard_scaled, columns=df_num.columns)
print("\nOriginal Data (first 5 rows):\n", df_num.head())
print("\nStandard Scaled Data (first 5 rows):\n", df_standard.head())

# --------------------------------------------------------------------------------

# Min-Max Scaling
# Min-Max Scaler (Normalization) scales data to a fixed range, typically 0 to 1.
scaler_minmax = MinMaxScaler()
df_minmax_scaled = scaler_minmax.fit_transform(df_num)

# Convert back to DataFrames
df_minmax = pd.DataFrame(df_minmax_scaled, columns=df_num.columns)
print("\nMin-Max Scaled Data (first 5 rows):\n", df_minmax.head())