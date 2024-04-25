import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set limits and labels
ax.set_xlim([0, 100])
ax.set_ylim([0, 100])
ax.set_zlim([0, 100])
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Z Coordinate (swapped to Y)')
ax.set_zlabel('Y Coordinate (swapped to Z)')

# Enable interactive mode
plt.ion()

# Initial empty plot elements
scat = ax.scatter([], [], [], color='blue')  # Start with an empty scatter plot

# Loop to update the plot dynamically
for _ in range(10):  # Example loop
    # Generate random data
    x = np.random.rand(10) * 100
    z = np.random.rand(10) * 100  # Notice the swap of y and z
    y = np.random.rand(10) * 100

    # Update data in scatter plot
    scat._offsets3d = (x, z, y)  # Update the positions
    
    # Redraw the plot
    fig.canvas.draw_idle()
    plt.pause(0.5)

# Disable interactive mode and show the plot
plt.ioff()
plt.show()
