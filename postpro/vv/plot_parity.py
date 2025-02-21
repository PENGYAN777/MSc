import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import CoolProp as CP
from IPython import get_ipython  

# Reset the workspace
get_ipython().magic('reset -sf')
os.system('clear')

# Load experimental and numerical data
ex = pd.read_csv("ex.csv", ",", skiprows=0)
euler = pd.read_csv("euler/cfd/m8new.csv", ",", skiprows=0)
m1 = pd.read_csv("rans/cfd/m1new.csv", ",", skiprows=0)
m2 = pd.read_csv("rans/cfd/m2new.csv", ",", skiprows=0)

# Define scaling factors
P0 = 804804
D1 = 6.5

# Process numerical data
xd = np.concatenate([
    np.array(m1.iloc[0:270, -8] / D1), 
    np.array(m2.iloc[300:-1, -8] / D1)
])
yd = np.concatenate([
    m1.iloc[0:270, -4] / P0, 
    m2.iloc[300:-1, -4] / P0
])

# Interpolate numerical values at experimental x-locations
n = len(ex)
y_pred = np.zeros(n)  # Numerical values (predictions)
x_exp = ex.iloc[:, 1]  # Experimental values (ground truth)
for i in range(n):
    idx = np.argmin(abs(xd - ex.iloc[i, 0]))  # Find closest numerical data point
    y_pred[i] = yd[idx]

# Compute the average percentage difference
diff = (y_pred - x_exp) / x_exp * 100
diff_ave = np.mean(abs(diff))
print(f'Average Difference: {diff_ave:.2f}%')

# === PLOT: Parity Plot with 5% Band ===
fig1 = plt.figure( dpi=300)
lwh = 2
ax = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure

# Plot numerical vs. experimental data
ax.scatter(x_exp, y_pred, color='b', label="Numerical vs. Experimental", alpha=0.7)

# Parity line (y = x)
min_val = min(min(x_exp), min(y_pred))
max_val = max(max(x_exp), max(y_pred))
ax.plot([min_val, max_val], [min_val, max_val], 'k--', lw=1.5, label="Parity Line (y=x)")

# 10% Error Band
upper_band = 1.10 * np.array([min_val, max_val])
lower_band = 0.90 * np.array([min_val, max_val])
ax.fill_between([min_val, max_val], lower_band, upper_band, color='gray', alpha=0.3, label="±10% Error Band")

# Formatting
ax.set_xlabel("Experimental Data", fontsize=12)
ax.set_ylabel("Numerical Prediction", fontsize=12)
ax.set_title("Parity Plot: Numerical vs. Experimental", fontsize=14)
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)

# Save the figure
fig1.savefig("parity_plot.pdf")

