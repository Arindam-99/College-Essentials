# To perform EDA on a real-world dataset like Titanic using various plots
# Library Functions
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

# Load Titanic dataset 
df = sns.load_dataset('titanic')

# Display first few rows 
print("/nFirst few rows:")
print(df.head(),"\n")

#Basic Info 
print("\nBasic Info:")
print(df.info(),"\n")

#Summary statistics (only for numeric columns)
print("\nBasic Info:")
print(df.info(),"\n")

# Summery statuctics (only for numeric columns)
print("\nStatistical summery:")
print(df.describe(),"\n")

# Histogram 
sns.histplot(df['age'],bins=20,color='brown')
plt.title('Histogram of Age')
plt.show()


# KDE plot 
sns.kdeplot(df['age'],fill=True,color="red")
plt.title('KDE Plot of Age')
plt.show()

#Countplot
sns.countplot(x='class', data=df,color='lightblue')
plt.title('Passenger Count by class')
plt.show()

#Barplot 
sns.countplot(x='sex',data=df,color='violet')
plt.title("passenger Count by Sex")
plt.show()

# Scatter plot
sns.scatterplot(x='age',y='fare',date=df)
plt.titlr('Age Vs Fare')
plt.show()

#Boxplot
sns.boxplot(x='class',y='fare',data=df,color='pink')
plt.title("Fare Distribution by Class")
plt.show()

#Violin plot
sns.violinplot(x='class',y='age',data=df)
plt.title('Age by Passenger Class')
plt.show()
