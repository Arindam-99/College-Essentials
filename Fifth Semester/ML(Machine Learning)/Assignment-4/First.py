# Question : || Creating Categorical Plots: Boxplots, Violin Plots, and Countplots || 

# Seaborn Categorical Plots: Boxplot, Violin Plot, Countplot
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("tips")

# 1. BOX PLOT
# ============================================================
sns.boxplot(x="day", y="total_bill", data=tips, palette="Set2")
plt.title("Boxplot: Total Bill by Day")
plt.show()


# 2. VIOLIN PLOT
# ============================================================
sns.violinplot(x="day", y="total_bill", data=tips, palette="muted")
plt.title("Violin Plot: Total Bill by Day")
plt.show()


# 3. COUNT PLOT
# ============================================================
sns.countplot(x="day", data=tips, palette="coolwarm")
plt.title("Countplot: Number of Records per Day")
plt.show()
