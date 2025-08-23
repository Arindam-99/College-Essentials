# Question : || Exploring Seaborn: Creating Histograms and KDE Plots ||

#  Seaborn Examples: Histogram, KDE Plot, and Combined Plot
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = [7, 8, 5, 6, 7, 9, 6, 5, 6, 7, 8, 7, 6, 7, 5, 8, 9, 6, 7, 8]


# 1. HISTOGRAM
# ============================================================
sns.histplot(data, bins=6, color="skyblue", edgecolor="black")
plt.title("Seaborn Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()



# 2. KDE (Kernel Density Estimation) PLOT
# ============================================================
sns.kdeplot(data, fill=True, color="red")
plt.title("Seaborn KDE Plot Example")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()


# 3. HISTOGRAM + KDE COMBINED
# ============================================================
sns.histplot(data, bins=6, kde=True, color="purple")
plt.title("Histogram with KDE Overlay")
plt.xlabel("Value")
plt.ylabel("Frequency / Density")
plt.show()
