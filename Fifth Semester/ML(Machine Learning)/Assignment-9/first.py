# Assignment-9 : To build interactive charts using Ploty
#Library Function
import pandas as pd
import seaborn as sns
import plotly.express as px

#Load Titanic dataset from seaborn
df = sns.load_dataset('titanic')

# Interactive bar chart: Survival count by gender
fig = px.bar(df,x='sex',color ="survived",barmode='group',title="Survival by Gender")
fig.show()


#Interactive scatter plot: Age vs Fare
fig2 = px.scatter(df,x='age',y='fare', color='pclass',size="fare", hover_name='sex',title= 'Age vs Fare with class ')
fig2.show()