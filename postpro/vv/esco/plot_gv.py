#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 19:20:51 2022

@author: yan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

n0= pd.read_csv("n0.csv", ",", skiprows=0)
n4= pd.read_csv("n4.csv", ",", skiprows=0)
n6= pd.read_csv("../euler/cfd/m6.csv", ",", skiprows=0)
n8= pd.read_csv("../euler/cfd/m7.csv", ",", skiprows=0)
n10= pd.read_csv("../euler/cfd/m8.csv", ",", skiprows=0)


D=6.5

fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(n0.iloc[:,1]/D , n0.iloc[:,0]/n0.iloc[0,0] , 'k', lw=lwh, label="$n=0$")
axes.plot(n4.iloc[:,1]/D , n4.iloc[:,0]/n4.iloc[0,0] , 'g', lw=lwh, label="$n=4$")
axes.plot(n6.iloc[:,-3]/D , n6.iloc[:,6]/n6.iloc[0,6] , 'b', lw=lwh, label="$n=6$")
axes.plot(n8.iloc[:,-3]/D , n8.iloc[:,6]/n8.iloc[0,6] , 'y', lw=lwh, label="$n=8$")
axes.plot(n10.iloc[:,-3]/D , n10.iloc[:,6]/n10.iloc[0,6] , 'r', lw=lwh, label="$n=10$")





axes.set_xlabel('$X/D$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$P/P_t$',fontsize=12) 
# axes.set_aspect('equal', 'box')
axes.set_title('$P/P_t$ along symmetry axis',fontsize=14)

axes.legend(loc=0 , prop={'size': 10}) # 
# axes.set_xlim(0,0.12)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("gv.pdf")
