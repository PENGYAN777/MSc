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

refer= pd.read_csv("../ref/axis.csv", ",", skiprows=0)
gd= pd.read_csv("d/axis.csv", ",", skiprows=0)
gm= pd.read_csv("m/axis.csv", ",", skiprows=0)
gp= pd.read_csv("p/axis.csv", ",", skiprows=0)
gt= pd.read_csv("t/axis.csv", ",", skiprows=0)
ge= pd.read_csv("e/axis.csv", ",", skiprows=0)


D=6.5

fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(refer.iloc[:,6]/D , refer.iloc[:,2]/refer.iloc[0,2] , 'k', lw=lwh, label="reference")
axes.plot(gd.iloc[:,6]/D , gd.iloc[:,2]/gd.iloc[0,2] , 'r', lw=lwh, label="$\\nabla \\rho$")
axes.plot(gm.iloc[:,6]/D , gm.iloc[:,2]/gm.iloc[0,2] , 'b', lw=lwh, label="$\\nabla M$")
axes.plot(gp.iloc[:,6]/D , gp.iloc[:,2]/gp.iloc[0,2] , 'g', lw=lwh, label="$\\nabla P$")
axes.plot(gt.iloc[:,6]/D , gt.iloc[:,2]/gt.iloc[0,2] , 'y', lw=lwh, label="$\\nabla T$")
axes.plot(ge.iloc[:,6]/D , ge.iloc[:,2]/gt.iloc[0,2] , 'm', lw=lwh, label="$\\nabla s$")




axes.set_xlabel('$X/D$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$P/P_t$',fontsize=12) 
# axes.set_aspect('equal', 'box')
# axes.set_title('$P/P_t$ along symmetry axis',fontsize=14)

axes.legend(loc=0 , prop={'size': 10}) # 
# axes.set_xlim(0,0.12)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("refer_nn_gra_p.pdf")
