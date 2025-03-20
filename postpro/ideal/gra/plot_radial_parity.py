#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modified: Parity Plots for Density, Mach, and Temperature with 10% Error Band
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
try:
    refer = pd.read_csv("../ref/radial.csv", ",", skiprows=0)
    gd = pd.read_csv("d/radial.csv", ",", skiprows=0)
    gm = pd.read_csv("m/radial.csv", ",", skiprows=0)
    gp = pd.read_csv("p/radial.csv", ",", skiprows=0)
    gt = pd.read_csv("t/radial.csv", ",", skiprows=0)
    dm = pd.read_csv("dm/radial.csv", ",", skiprows=0)
    dp = pd.read_csv("dp/radial.csv", ",", skiprows=0)
    pm = pd.read_csv("pm/radial.csv", ",", skiprows=0)
except FileNotFoundError as e:
    print("Error: One or more files not found.", e)
    exit()

D = 6.5  # Reference diameter

# Select axial positions [0, 0.5, 1.0, 1.5, 2.0, 2.5]
# axial_positions = np.array([0, 0.5, 1.0, 1.5, 2.0, 2.5])
axial_positions = np.arange(0, 2.6, 0.2)  # End value is exclusive, so use 2.6 to include 2.5

ref_x = refer.iloc[:, -2] / D  # Normalize X-axis
selected_indices = [np.abs(ref_x - x).idxmin() for x in axial_positions]  # Find closest indices

# Function to extract and normalize values at selected positions
def extract_values(df, col):
    return df.iloc[selected_indices, col] / df.iloc[0, col]

# Extract data for Density, Mach, and Temperature
ref_p_rho = extract_values(refer, 0)
ref_p_mach = refer.iloc[selected_indices, 5]  # No normalization for Mach
ref_p_temp = extract_values(refer, 15)

# Extract predicted values
gd_p_rho, gd_p_mach, gd_p_temp = extract_values(gd, 0), gd.iloc[selected_indices, 5], extract_values(gd, 15)
gm_p_rho, gm_p_mach, gm_p_temp = extract_values(gm, 0), gm.iloc[selected_indices, 5], extract_values(gm, 15)
gp_p_rho, gp_p_mach, gp_p_temp = extract_values(gp, 0), gp.iloc[selected_indices, 5], extract_values(gp, 15)
gt_p_rho, gt_p_mach, gt_p_temp = extract_values(gt, 0), gt.iloc[selected_indices, 5], extract_values(gt, 15)
dm_p_rho, dm_p_mach, dm_p_temp = extract_values(dm, 0), dm.iloc[selected_indices, 5], extract_values(dm, 15)
dp_p_rho, dp_p_mach, dp_p_temp = extract_values(dp, 0), dp.iloc[selected_indices, 5], extract_values(dp, 15)
pm_p_rho, pm_p_mach, pm_p_temp = extract_values(pm, 0), pm.iloc[selected_indices, 5], extract_values(pm, 15)

# Sort reference values in increasing order and reorder predictions accordingly
def sort_and_reorder(ref_p, *pred_values):
    sorted_indices = np.argsort(ref_p)
    return ref_p.iloc[sorted_indices], [p.iloc[sorted_indices] for p in pred_values]

ref_p_rho, (gd_p_rho, gm_p_rho, gp_p_rho, gt_p_rho, dm_p_rho, dp_p_rho, pm_p_rho) = sort_and_reorder(
    ref_p_rho, gd_p_rho, gm_p_rho, gp_p_rho, gt_p_rho, dm_p_rho, dp_p_rho, pm_p_rho
)
ref_p_mach, (gd_p_mach, gm_p_mach, gp_p_mach, gt_p_mach, dm_p_mach, dp_p_mach, pm_p_mach) = sort_and_reorder(
    ref_p_mach, gd_p_mach, gm_p_mach, gp_p_mach, gt_p_mach, dm_p_mach, dp_p_mach, pm_p_mach
)
ref_p_temp, (gd_p_temp, gm_p_temp, gp_p_temp, gt_p_temp, dm_p_temp, dp_p_temp, pm_p_temp) = sort_and_reorder(
    ref_p_temp, gd_p_temp, gm_p_temp, gp_p_temp, gt_p_temp, dm_p_temp, dp_p_temp, pm_p_temp
)

# Function to create a parity plot
def create_parity_plot(ref_p, pred_values, labels, ylabel, filename):
    fig, ax = plt.subplots(figsize=(6, 6), dpi=300)

    # Reference parity line (y = x)
    ax.plot(ref_p, ref_p, 'k--', lw=1.5, label="Perfect Agreement ($y = x$)")

    # 10% Error Band
    lower_bound = ref_p * 0.9
    upper_bound = ref_p * 1.1
    ax.fill_between(ref_p, lower_bound, upper_bound, color='gray', alpha=0.2, label="±10% Error Band")

    # Scatter plots for each dataset
    colors = ['r', 'b', 'g', 'y', 'm', 'c', 'orange']
    markers = ['o', 'o', 'o', 'o', 'o', 'o', 'o']

    for p, label, color, marker in zip(pred_values, labels, colors, markers):
        ax.scatter(ref_p, p, color=color, label=label, marker=marker)

    # Labels and legend
    ax.set_xlabel("Reference Solution", fontsize=12)
    ax.set_ylabel(f"Predicted {ylabel}", fontsize=12)
    ax.legend(loc="best", fontsize=10)
    ax.grid(True, linestyle='--', linewidth=0.5)

    # Save and show the plot
    plt.savefig(filename, bbox_inches='tight')
    plt.show()

# Labels for legend
labels = [
    "$\\nabla \\rho$", "$\\nabla M$", "$\\nabla P$", "$\\nabla T$",
    "$\\nabla \\rho$ + $\\nabla M$", "$\\nabla \\rho$ + $\\nabla P$", "$\\nabla P$ + $\\nabla M$"
]

# Generate plots
create_parity_plot(ref_p_rho, [gd_p_rho, gm_p_rho, gp_p_rho, gt_p_rho, dm_p_rho, dp_p_rho, pm_p_rho], labels, "$\\rho/\\rho_s$", "parity_i_gra_d.pdf")
create_parity_plot(ref_p_mach, [gd_p_mach, gm_p_mach, gp_p_mach, gt_p_mach, dm_p_mach, dp_p_mach, pm_p_mach], labels, "Mach", "parity_i_gra_m.pdf")
create_parity_plot(ref_p_temp, [gd_p_temp, gm_p_temp, gp_p_temp, gt_p_temp, dm_p_temp, dp_p_temp, pm_p_temp], labels, "$T/T_s$", "parity_i_gra_t.pdf")
