# Assignment: 2 || Customizing Charts: Titles, Labels, Legends, and Gridlines

import matplotlib.pyplot as plt

# 1. LINE CHART
# ============================================================
x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 10, 12]

plt.plot(x, y, marker='o', color='b', linestyle='-')
plt.title("Line Chart Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# 2. BAR CHART
# ============================================================
categories = ["A", "B", "C", "D"]
values = [10, 24, 36, 18]

plt.bar(categories, values, color='green')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()


# 3. SCATTER PLOT
# ============================================================
x = [5, 7, 8, 7, 6, 9, 5, 6]
y = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x, y, color='red', marker='x')
plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()



# 4. CUSTOMIZATION (Titles, Labels, Legends, Gridlines)
# ============================================================
x = [1, 2, 3, 4, 5]
y1 = [2, 5, 7, 10, 12]
y2 = [1, 3, 6, 8, 11]

plt.plot(x, y1, label="Product A", color="blue", marker="o")
plt.plot(x, y2, label="Product B", color="orange", marker="s")

plt.title("Sales Comparison with Customizations")   # Title
plt.xlabel("Months")   # X-axis label
plt.ylabel("Sales (in 1000s)")   # Y-axis label
plt.legend()   # Add legend
plt.grid(True) # Add gridlines
plt.show()
