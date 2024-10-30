#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:40:12 2024

@author: yan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import os
import CoolProp as CP
from IPython import get_ipython;   
get_ipython().magic('reset -sf')
os.system('clear')




h6 = pd.read_csv("history.csv", ",", skiprows=0)

nc = 10
colors = plt.cm.tab20(np.linspace(0, 1, nc))


# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# fig 2
fig2 = plt.figure( dpi=300)
lw = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(h6.iloc[:,2] ,h6.iloc[:,3] , color=colors[0], lw=lw, label="$\\rho$")
axes.plot(h6.iloc[:,2] ,h6.iloc[:,4] , color=colors[1], lw=lw, label="$\\rho u$")
axes.plot(h6.iloc[:,2] ,h6.iloc[:,5] , color=colors[2], lw=lw, label="$\\rho v$")
axes.plot(h6.iloc[:,2] ,h6.iloc[:,6] , color=colors[3], lw=lw, label="$\\rho e$")





# axes.set_xlim([40, 160])
# axes.set_ylim([0,1])
axes.set_xlabel('Number of iteration',fontsize=12)
axes.set_ylabel('Residuals',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=0) # 

fig2.savefig("vv_pig_euler_resudial.pdf")




