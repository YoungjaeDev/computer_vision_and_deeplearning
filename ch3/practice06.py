import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-5, 5, 100)

std_dev = 1
y = np.exp(-0.5 * (x / std_dev) ** 2) / (std_dev * np.sqrt(2 * np.pi))

# Plot the Gaussian function
plt.plot(x, y)

# Set labels and title
plt.xlabel('x')
plt.ylabel('Gaussian(x)')
plt.title('One-Dimensional Gaussian Function')

# Show the plot
plt.show()
