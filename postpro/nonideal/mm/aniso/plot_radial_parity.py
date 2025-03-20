#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modified: Parity Plots for Density, Mach, and Temperature with 5% and 10% Error Bands
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
axial_positions = np.arange(0, 2.6, 0.2)
ref_x = refer.iloc[:, -2] / D
selected_indices = [np.abs(ref_x - x).idxmin() for x in axial_positions]

def extract_values(df, col):
    return df.iloc[selected_indices, col] / df.iloc[0, col]

# Extract data
ref_p_rho = extract_values(refer, 0)
ref_p_mach = refer.iloc[selected_indices, 5]
ref_p_temp = extract_values(refer, 15)

gd_p_rho, gd_p_mach, gd_p_temp = extract_values(gd, 0), gd.iloc[selected_indices, 5], extract_values(gd, 15)
gm_p_rho, gm_p_mach, gm_p_temp = extract_values(gm, 0), gm.iloc[selected_indices, 5], extract_values(gm, 15)
gp_p_rho, gp_p_mach, gp_p_temp = extract_values(gp, 0), gp.iloc[selected_indices, 5], extract_values(gp, 15)
gt_p_rho, gt_p_mach, gt_p_temp = extract_values(gt, 0), gt.iloc[selected_indices, 5], extract_values(gt, 15)
dm_p_rho, dm_p_mach, dm_p_temp = extract_values(dm, 0), dm.iloc[selected_indices, 5], extract_values(dm, 15)
dp_p_rho, dp_p_mach, dp_p_temp = extract_values(dp, 0), dp.iloc[selected_indices, 5], extract_values(dp, 15)
pm_p_rho, pm_p_mach, pm_p_temp = extract_values(pm, 0), pm.iloc[selected_indices, 5], extract_values(pm, 15)

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

def create_parity_plot(ref_p, pred_values, labels, ylabel, filename, xlim=None, ylim=None):
    fig, ax = plt.subplots(figsize=(6, 6), dpi=300)
    ax.plot(ref_p, ref_p, 'k--', lw=1.5, label="Perfect Agreement ($y = x$)")
    
    # Error bands
    ax.fill_between(ref_p, ref_p * 0.95, ref_p * 1.05, color='lightgreen', alpha=0.3, label="±5% Error Band")
    ax.fill_between(ref_p, ref_p * 0.90, ref_p * 1.10, color='gray', alpha=0.2, label="±10% Error Band")
    
    colors = ['r', 'b', 'g', 'y', 'm', 'c', 'orange']
    for p, label, color in zip(pred_values, labels, colors):
        ax.scatter(ref_p, p, color=color, label=label, marker='o')
    
    # Set axis limits from 0 to 1 (or to the passed xlim and ylim)
    ax.set_aspect('equal')
    ax.set_xlabel("Reference Solution", fontsize=12)
    ax.set_ylabel(f"Predicted {ylabel}", fontsize=12)
    
    # Set custom axis limits if provided
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)
    
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, linestyle='--', linewidth=0.5)
    plt.savefig(filename, bbox_inches='tight')
    plt.show()

# Define axis limits for each plot
rho_xlim = (1.0, 5.5)
rho_ylim = (1.0, 5.5)  # Example limit for rho plot

mach_xlim = (0, 2.6)
mach_ylim = (0, 2.6)  # Example limit for Mach plot

temp_xlim = (1.0, 1.07)
temp_ylim = (1.0, 1.07)  # Example limit for Temperature plot

# Create parity plots with different axis limits
labels = [
    "$\\nabla \\rho$", "$\\nabla M$", "$\\nabla P$", "$\\nabla T$",
    "$\\nabla \\rho$ + $\\nabla M$", "$\\nabla \\rho$ + $\\nabla P$", "$\\nabla P$ + $\\nabla M$"
]

create_parity_plot(ref_p_rho, [gd_p_rho, gm_p_rho, gp_p_rho, gt_p_rho, dm_p_rho, dp_p_rho, pm_p_rho], 
                   labels, "$\\rho/\\rho_s$", "parity_non_aniso_d.pdf", xlim=rho_xlim, ylim=rho_ylim)

create_parity_plot(ref_p_mach, [gd_p_mach, gm_p_mach, gp_p_mach, gt_p_mach, dm_p_mach, dp_p_mach, pm_p_mach], 
                   labels, "Mach", "parity_non_aniso_m.pdf", xlim=mach_xlim, ylim=mach_ylim)

create_parity_plot(ref_p_temp, [gd_p_temp, gm_p_temp, gp_p_temp, gt_p_temp, dm_p_temp, dp_p_temp, pm_p_temp], 
                   labels, "$T/T_s$", "parity_non_aniso_t.pdf", xlim=temp_xlim, ylim=temp_ylim)
