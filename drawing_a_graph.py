import matplotlib.pyplot as plt

# Given X values and corresponding Y values (X^2)
X = [2, 3, 4, 5, 6]
Y = [x**2 for x in X]

# Plotting the graph
plt.plot(X, Y, marker='o', color='b', label='Y = X^2')

# Adding labels and title
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Graph of Y = X^2')

# Display grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
