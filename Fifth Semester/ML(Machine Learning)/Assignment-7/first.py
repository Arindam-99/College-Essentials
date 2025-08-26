# pie_donut_charts.py
# Creating Pie Charts and Donut Charts using Matplotlib

import matplotlib.pyplot as plt

# -----------------------------
# Example 1: Pie Chart
# -----------------------------
sizes = [25, 30, 20, 25]
labels = ["A", "B", "C", "D"]
colors = ["skyblue", "lightgreen", "salmon", "orange"]

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        startangle=90, shadow=True, explode=(0, 0.1, 0, 0))
plt.title("Pie Chart Example")
plt.show()

# -----------------------------
# Example 2: Donut Chart
# -----------------------------
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add center circle to make it donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Donut Chart Example")
plt.show()

