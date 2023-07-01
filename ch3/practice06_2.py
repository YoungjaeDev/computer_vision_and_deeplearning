import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calculate the Gaussian function
mean = [0, 0]
cov = [[1, 0], [0, 1]]
Z = np.exp(-0.5 * (np.square(X - mean[0]) + np.square(Y - mean[1])) / cov[0][0]) / (2 * np.pi * np.sqrt(np.linalg.det(cov)))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the Gaussian function
ax.plot_surface(X, Y, Z, cmap='viridis')

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Gaussian(x, y)')
ax.set_title('Three-Dimensional Gaussian Function')

# Show the plot
plt.show()
