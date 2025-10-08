#Assignment 14 : To split datasets into training and testing sets
import pandas as pd 
from sklearn.model_selection import train_test_split
#import Data
df = pd.read_csv('BostonHousing.csv')

#Features (X) and Target (y)
X = df.drop("MEDV",axis=1)
y=df["MEDV"]
#Split the dataset (80% train, 20% test)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print("Training set size:",X_train.shape)
print("Testing set size:",X_test.shape)