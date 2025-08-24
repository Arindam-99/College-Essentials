# Question : || Working with Pandas for DataFrame Visualization (plotting from CSV data) || 
#  Pandas DataFrame Visualization (from CSV data)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# 1. READ CSV FILE
# ============================================================

# Make sure you have a CSV file named "data.csv" with columns like:
# Date, Sales, Profit, Category
df = pd.read_csv("data.csv")

print("First 5 rows of the dataset:")
print(df.head())  # Display first few rows


# 2. LINE PLOT (Sales over Time)
# ============================================================
df.plot(x="Date", y="Sales", kind="line", marker="o", color="blue")

plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()


# 3. BAR PLOT (Sales by Category)
# ============================================================
df.plot(x="Category", y="Sales", kind="bar", color="green")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()


# 4. SCATTER PLOT (Sales vs Profit)
# ============================================================
df.plot(x="Sales", y="Profit", kind="scatter", color="red")

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()


# 5. HISTOGRAM (Sales Distribution)
# ============================================================
df["Sales"].plot(kind="hist", bins=10, color="purple", edgecolor="black")

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()
