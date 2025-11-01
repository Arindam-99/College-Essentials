#Assignment" 5 || Visualizing Relationships: Pairplot and Heatmap using Seaborn || 
# Seaborn Relationship Plots: Pairplot & Heatmap
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt

# 1. PAIRPLOT
# ============================================================

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Create a pairplot (scatterplot matrix)
sns.pairplot(iris, hue="species", palette="Set1")

plt.suptitle("Pairplot of Iris Dataset", y=1.02)  # Title above plots
plt.show()


# 2. HEATMAP
# ============================================================

# Load the Tips dataset
tips = sns.load_dataset("tips")

# Compute correlation matrix
corr = tips.corr()

# Create a heatmap of correlations
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)

plt.title("Heatmap of Correlation Matrix (Tips Dataset)")
plt.show()
