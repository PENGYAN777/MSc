#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# Data for horizontal line
x1 = [0, 10]
y1 = [0, 0]

# Create figure
fig1 = plt.figure(dpi=300)
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7])

# Plot horizontal threshold line
axes.plot(x1, y1, 'k', lw=2)

# Plot threshold bars
plt.bar(9.5, 0.8, color='orange', width=1)
plt.bar(8.5, 0.8, color='yellow', width=1)
plt.bar(7.5, 0.8, color='purple', width=1)

plt.bar(2.5, -0.8, color='blue', width=1)
plt.bar(1.5, -0.8, color='maroon', width=1)
plt.bar(0.5, -0.8, color='green', width=1)

# Axis tick labels
axes.set_xticks([0.5, 1.5, 2.5, 7.5, 8.5, 9.5])
axes.set_xticklabels([r'$\tau_{C3}$', r'$\tau_{C2}$', r'$\tau_{C1}$',
                      r'$\tau_{R3}$', r'$\tau_{R2}$', r'$\tau_{R1}$'], fontsize=12)
axes.set_yticks([])
axes.set_ylim([-1, 1])
axes.set_xlim([-1, 10.5])  # Slightly expanded to fit annotation text

# Add legend
plt.bar(0, 0, color='green', label='Coarsening Thresholds')
plt.bar(0, 0, color='purple', label='Refinement Thresholds')
axes.legend(loc='upper left', fontsize=10)

# Add annotation arrows and labels (shifted inward)
axes.annotate('Refine if error > $\\tau_{R3}$',
              xy=(7.5, 0.1), xytext=(2.5, 0.5),
              arrowprops=dict(facecolor='black', arrowstyle='->', clip_on=False),
              fontsize=10, ha='left')

axes.annotate('Coarsen if error < $\\tau_{C3}$',
              xy=(0.5, -0.1), xytext=(3.5, 0.2),
              arrowprops=dict(facecolor='black', arrowstyle='->', clip_on=False),
              fontsize=10, ha='right')

# Save figure (ensure all elements are included)
fig1.savefig("threshold.pdf", bbox_inches='tight')
