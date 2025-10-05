# Assignment 10: To create dashboards using subplots and multiple chart types

# Library Functions
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = sns.load_dataset("titanic")

# Create subplots layout (2 rows, 2 columns)
# Specs define the type of plot for each subplot:
# 'xy' for standard 2D plots (bar, scatter)
# 'domain' for plots that use domain coordinates (pie)
fig = make_subplots(rows=2, cols=2, specs=[[{"type": "xy"}, {"type": "domain"}], [{"type": "xy"}, {"type": "xy"}]],
                    subplot_titles=("Survival Count", "Class Distribution", "Age vs Fare", "Survival by Gender"))

# Plot 1: Survival count (bar chart)
survival_counts = df['survived'].value_counts()
fig.add_trace(go.Bar(x=survival_counts.index, y=survival_counts.values, name="Survival Count"), row=1, col=1)

# Plot 2: Passenger class distribution (pie chart)
class_counts = df['class'].value_counts()
fig.add_trace(go.Pie(labels=class_counts.index, values=class_counts.values, name="Class Distribution"), row=1, col=2)

# Plot 3: Age vs Fare (scatter plot)
fig.add_trace(go.Scatter(x=df['age'], y=df['fare'], mode='markers', name="Age vs Fare"), row=2, col=1)

# Plot 4: Survival by gender (bar chart)
# Calculate the mean survival rate (1 for survived, 0 for not) for each gender
gender_survival = df.groupby('sex')['survived'].mean()
fig.add_trace(go.Bar(x=gender_survival.index, y=gender_survival.values, name="Survival by Gender"), row=2, col=2)

# Update layout for better display
fig.update_layout(height=800, width=1000, title_text="Titanic Dashboard - Multiple Chart Types")

# Show the figure
fig.show()