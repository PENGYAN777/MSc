#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modified: Parity Plot with Sorted Reference Values and 10% Error Band
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reference diameter
D = 6.5

# Load datasets
try:
    ex = pd.read_csv("../../../vv/ex.csv", ",", skiprows=0)
    refer = pd.read_csv("../ref/axis.csv", ",", skiprows=0)
    gd = pd.read_csv("d/axis.csv", ",", skiprows=0)
    gm = pd.read_csv("m/axis.csv", ",", skiprows=0)
    gp = pd.read_csv("p/axis.csv", ",", skiprows=0)
    gt = pd.read_csv("t/axis.csv", ",", skiprows=0)
    dm = pd.read_csv("dm/axis.csv", ",", skiprows=0)
    dp = pd.read_csv("dp/axis.csv", ",", skiprows=0)
    pm = pd.read_csv("pm/axis.csv", ",", skiprows=0)
except FileNotFoundError as e:
    print("Error: One or more files not found.", e)
    exit()

# Select axial positions ex.iloc[:,0]
axial_positions = np.array(ex.iloc[:,0])
ref_x = refer.iloc[:, -3] / D  # Normalize X-axis
selected_indices = [np.abs(ref_x - x).idxmin() for x in axial_positions]  # Find closest indices

# Extract reference pressure values at selected positions
ref_p = refer.iloc[selected_indices, 10] / refer.iloc[0, 10]

# Function to extract and normalize other solutions at selected positions
def extract_values(df):
    return df.iloc[selected_indices, 10] / df.iloc[0, 10]

# Extract all datasets
gd_p = extract_values(gd)
gm_p = extract_values(gm)
gp_p = extract_values(gp)
gt_p = extract_values(gt)
dm_p = extract_values(dm)
dp_p = extract_values(dp)
pm_p = extract_values(pm)

# Sort ref_p in increasing order and reorder all corresponding values
sorted_indices = np.argsort(ref_p)  # Get sorting indices
ref_p = ref_p.iloc[sorted_indices]  # Sort reference values

# Reorder all predicted values based on the sorted reference
gd_p = gd_p.iloc[sorted_indices]
gm_p = gm_p.iloc[sorted_indices]
gp_p = gp_p.iloc[sorted_indices]
gt_p = gt_p.iloc[sorted_indices]
dm_p = dm_p.iloc[sorted_indices]
dp_p = dp_p.iloc[sorted_indices]
pm_p = pm_p.iloc[sorted_indices]

# Plot parity plot
fig, ax = plt.subplots(figsize=(6,6), dpi=300)

# Reference parity line (y = x)
ax.plot(ref_p, ref_p, 'k--', lw=1.5, label="Parity Line ($y = x$)")

# 10% Error Band
lower_bound = ref_p * 0.9
upper_bound = ref_p * 1.1
ax.fill_between(ref_p, lower_bound, upper_bound, color='gray', alpha=0.2, label="±10% Error Band")

# Scatter plots for each dataset
ax.scatter(ref_p, gd_p, color='r', label="$\\nabla \\rho$", marker='o')
ax.scatter(ref_p, gm_p, color='b', label="$\\nabla M$", marker='o')
ax.scatter(ref_p, gp_p, color='g', label="$\\nabla P$", marker='o')
ax.scatter(ref_p, gt_p, color='y', label="$\\nabla T$", marker='o')
ax.scatter(ref_p, dm_p, color='m', label="$\\nabla \\rho$ + $\\nabla M$", marker='o')
ax.scatter(ref_p, dp_p, color='c', label="$\\nabla \\rho$ + $\\nabla P$", marker='o')
ax.scatter(ref_p, pm_p, color='orange', label="$\\nabla P$ + $\\nabla M$", marker='o')

# Labels and legend
ax.set_xlabel("Reference Solution $P/P_t$", fontsize=12)
ax.set_ylabel("Predicted Solutions $P/P_t$", fontsize=12)
ax.legend(loc="best", fontsize=10)
ax.grid(True, linestyle='--', linewidth=0.5)

# Save and show the plot
plt.savefig("parity_n_gra_p.pdf", bbox_inches='tight')
plt.show()
