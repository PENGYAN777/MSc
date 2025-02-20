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

D=6.5

refer= pd.read_csv("../ref/axis.csv", ",", skiprows=0)
gd= pd.read_csv("d/axis.csv", ",", skiprows=0)
gm= pd.read_csv("m/axis.csv", ",", skiprows=0)
gp= pd.read_csv("p/axis.csv", ",", skiprows=0)
gt= pd.read_csv("t/axis.csv", ",", skiprows=0)
ge= pd.read_csv("e/axis.csv", ",", skiprows=0)



fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(refer.iloc[:,-3]/D , refer.iloc[:,10]/refer.iloc[0,10] , 'k', lw=lwh, label="reference")
axes.plot(gd.iloc[:,-3]/D , gd.iloc[:,10]/gd.iloc[0,10] , 'r', lw=lwh, label="$\\nabla \\rho$")
axes.plot(gm.iloc[:,-3]/D , gm.iloc[:,10]/gm.iloc[0,10] , 'b', lw=lwh, label="$\\nabla M$")
axes.plot(gp.iloc[:,-3]/D , gp.iloc[:,10]/gp.iloc[0,10] , 'g', lw=lwh, label="$\\nabla P$")
axes.plot(gt.iloc[:,-3]/D , gt.iloc[:,10]/gt.iloc[0,10] , 'y', lw=lwh, label="$\\nabla T$")
axes.plot(ge.iloc[:,-3]/D , ge.iloc[:,11]/ge.iloc[0,11] , 'm', lw=lwh, label="$\\nabla s$")




axes.set_xlabel('$X/D$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$P/P_t$',fontsize=12) 
# axes.set_aspect('equal', 'box')
# axes.set_title('$P/P_t$ along symmetry axis',fontsize=14)

axes.legend(loc=0 , prop={'size': 10}) # 
fig1.savefig("ideal_gra_p.pdf")
