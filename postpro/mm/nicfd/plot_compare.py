#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:48:31 2024

@author: yan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import os
import CoolProp as CP
from IPython import get_ipython;   
get_ipython().magic('reset -sf')
os.system('clear')

"""
0. empirical formulation for ideal under-expanded sonic jet
"""

# Define the range for x
x = np.linspace(0, 20, 500)  # pt/pa

# Define the function y = 0.645 * sqrt(x)
y1 = 0.645 * np.sqrt(x)

# # Define the function y = 0.36 * sqrt(x-3.9)
# y2 = 0.36 * np.sqrt(x-3.9)


"""
1. CFD results for non-ideal flow
"""
z9_pr = [15,  ]
z9_x = [2.98, ]
# z9_r = [0.56, ]

De = 0.0039*2
"""
2.1 plot Mach disk position
"""
nc = 10
colors = plt.cm.tab20(np.linspace(0, 1, nc))

# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(x, y1, 'k', lw=lwh, label="Ideal")
axes.plot(z9_pr  , z9_x ,'o', color=colors[0], lw=lwh, label="$Z_t = 0.9$")

# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

axes.set_xlabel('$P_t/P_a$',fontsize=12)
axes.set_ylabel('$X/D_e$',fontsize=12) 
# axes.set_title('$P_i/P_t$ along centerline',fontsize=14)
axes.legend(loc=0) # 

# axes.set_xlim([0, 8])
# axes.set_ylim([0, 0.8])

fig1.savefig("files/nicfd_position.pdf")

# """
# 2.1 plot Mach disk position
# """
# nc = 10
# colors = plt.cm.tab20(np.linspace(0, 1, nc))

# # fig 2
# fig2 = plt.figure( dpi=300)
# lwh = 2
# axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(x, y2, 'k', lw=lwh, label="Ideal")
# axes.plot(z9_pr  , z9_r ,'o', color=colors[0], lw=lwh, label="$Z_t = 0.9$")

# axes.set_xlabel('$P_t/P_a$',fontsize=12)
# axes.set_ylabel('$D/D_e$',fontsize=12) 
# # axes.set_title('$P_i/P_t$ along centerline',fontsize=14)
# axes.legend(loc=0) # 


# fig2.savefig("files/nicfd_diameter.pdf")

