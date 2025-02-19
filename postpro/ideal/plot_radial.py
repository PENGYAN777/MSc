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

refer= pd.read_csv("ref/radial.csv", ",", skiprows=0)
gd= pd.read_csv("gra/d/radial.csv", ",", skiprows=0)


D = 6.5

fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(refer.iloc[:,-2]/D , refer.iloc[:,0]/refer.iloc[0,0], 'k', lw=lwh, label="reference")
axes.plot(gd.iloc[:,-2]/D , gd.iloc[:,0]/refer.iloc[0,0] , 'r', lw=lwh, label="$\\nabla \\rho$")


axes.set_xlabel('$Y/D$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$\\rho/\\rho_s$',fontsize=12) 
# axes.set_aspect('equal', 'box')
axes.set_title('$\\rho/\\rho_s$ at $X/D=1.54$',fontsize=14)

axes.legend(loc=0 , prop={'size': 10}) # 
fig1.savefig("ideal_gra_rho.pdf")

fig2 = plt.figure( dpi=300)
lwh = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(refer.iloc[:,-2]/D , refer.iloc[:,5] , 'k', lw=lwh, label="reference")
axes.plot(gd.iloc[:,-2]/D , gd.iloc[:,5], 'r', lw=lwh, label="$\\nabla \\rho$")


axes.set_xlabel('$Y/D$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('Mach',fontsize=12) 
# axes.set_aspect('equal', 'box')
axes.set_title('Mach at $X/D=1.54$',fontsize=14)

axes.legend(loc=0 , prop={'size': 10}) # 
fig2.savefig("ideal_gra_m.pdf")

fig3 = plt.figure( dpi=300)
lwh = 2
axes = fig3.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(refer.iloc[:,-2]/D , refer.iloc[:,15]/refer.iloc[0,15] , 'k', lw=lwh, label="reference")
axes.plot(gd.iloc[:,-2]/D , gd.iloc[:,15]/refer.iloc[0,15] , 'r', lw=lwh, label="$\\nabla \\rho$")


axes.set_xlabel('$Y/D$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$T/T_s$',fontsize=12) 
# axes.set_aspect('equal', 'box')
axes.set_title('$T/T_s$ at $X/D=1.54$',fontsize=14)

axes.legend(loc=0 , prop={'size': 10}) # 
fig3.savefig("ideal_gra_t.pdf")
