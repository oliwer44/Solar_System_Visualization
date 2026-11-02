import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('dark_background')

planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
semi_major_axis = [0.39, 0.72, 1.0, 1.52, 5.2, 9.58, 19.22, 30.05]  # in AU (astronomical units)
orbit_period = [0.24, 0.62, 1.0, 1.88, 11.86, 29.46, 84.01, 164.8]  # in years

# INPUT YOUR CODE HERE: Create a figure of size (8, 8) and assign it to a variable called fig
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# INPUT YOUR CODE HERE: Plot the Sun at the center
ax.scatter(0, 0, color='yellow', s=100, label='Sun')

# Plot orbits of planets
for i, planet in enumerate(planet_names):
    # INPUT YOUR CODE HERE: Create a variable orbital_radius and assign it to the semi major axis value for each planet
    orbital_radius = semi_major_axis[i]
    # INPUT YOUR CODE HERE: Create a variable orbit_theta and assign it to a set of 100 equally spaced values from 0 to 2pi
    orbit_theta = np.linspace(0, 2*np.pi, 100)
    # INPUT YOUR CODE HERE: Create a variable x and assign it to the x-axis values of each orbit
    x = orbital_radius * np.cos(orbit_theta)
    # INPUT YOUR CODE HERE: Create a variable y and assign it to the y-axis values of each orbit
    y = orbital_radius * np.sin(orbit_theta)
    z = np.zeros_like(x)
    ax.plot(x, y, z, label=planet)

# INPUT YOUR CODE HERE: Set X, Y, and Z labels
ax.set_xlabel("X (AU)")
ax.set_ylabel("Y (AU)")
ax.set_zlabel("Z (AU)")
# INPUT YOUR CODE HERE: Set Title of Graph
ax.set_title("Solar System")
# INPUT YOUR CODE HERE: Initialize Graph Legend
ax.legend()
# INPUT YOUR CODE HERE: Show the Plot
plt.show()
