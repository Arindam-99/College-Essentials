#Assignment: 1 || Introduction to Matplotlib: Plotting Line, Bar, and Scatter Charts
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 10, 12]

# Plotting
plt.plot(x, y, marker='o', color='b', linestyle='-')
plt.title("Line Chart Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# Bar
categories = ["A", "B", "C", "D"]
values = [10, 24, 36, 18]

# Plotting
plt.bar(categories, values, color='green')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Scatter

x = [5, 7, 8, 7, 6, 9, 5, 6]
y = [99, 86, 87, 88, 100, 86, 103, 87]

# Plotting
plt.scatter(x, y, color='red', marker='x')
plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
