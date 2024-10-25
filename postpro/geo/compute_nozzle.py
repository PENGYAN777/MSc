#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:14:22 2024

@author: yan
"""

import matplotlib.pyplot as plt
import numpy as np

"""
1. convergent part
"""

# Circle parameters
radius = 30
center_x, center_y = 0, 3+radius


# Angle values for circle plot
theta = np.linspace(1.35*np.pi, 1.5 * np.pi, 100)

# Circle coordinates
x1 = center_x + radius * np.cos(theta)
y1 = center_y + radius * np.sin(theta)

# Plotting
plt.figure(figsize=(6, 6))
plt.plot(x1, y1, label=f"Circle (center=({center_x}, {center_y}), radius={radius})")
plt.scatter(center_x, center_y, color='red')  # mark the center
plt.title("Circle with Center (0, 23) and Radius 20")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.show()


"""
2. divergent part
"""

# Define the starting and ending points
x_start, y_start = 0, 3
x_end, y_end = 6.9, 3.9

# Generate x values along the line
x_values = np.linspace(x_start, x_end, num=100)  # 100 points along the line
# Calculate corresponding y values
y_values = y_start + (y_end - y_start) * (x_values - x_start) / (x_end - x_start)

# Plot the line with points
plt.plot(x_values, y_values, label="Line from (0,3) to (6.9,3.9)", color='b')
plt.scatter(x_values, y_values, color='r', s=10)  # Plot points along the line

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Straight Line with Points Along It")
plt.legend()

# Show plot
plt.grid(True)
plt.show()

"""
3. write into csv file
"""
import pandas as pd
x = np.append(x1, x_values)
x = x-6.9
y = np.append(y1, y_values)

pd.DataFrame(x).to_csv('nozzle.csv', index_label = "Index", header  = ['x']) 
data = pd.read_csv("nozzle.csv", ",")
# append new columns
D =pd.DataFrame({'y': y})
newData = pd.concat([data, D], join = 'outer', axis = 1)
# save newData in csv file
newData.to_csv("nozzle.csv")

