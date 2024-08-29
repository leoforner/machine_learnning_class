import numpy as np

import matplotlib.pyplot as plt

# Generate data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
'''
# Plot the surface
ax.plot_surface(X, Y, Z)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot')

# Show the plot
plt.show()
'''
import numpy as np
import matplotlib.animation as animation

# Create a function to update the plot
def update_plot(frame):
    ax.cla()  # Clear the current plot
    Z = np.sin(np.sqrt(X**2 + Y**2 + frame))  # Update the Z values
    ax.plot_surface(X, Y, Z)  # Plot the updated surface
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Plot')
    
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
        
    
# Create the animation
ani = animation.FuncAnimation(fig, update_plot, frames=150, interval=1)

# Show the animation
plt.show()