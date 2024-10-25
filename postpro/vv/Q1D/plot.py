#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:59:53 2023

@author: yan
"""
import CoolProp as CP
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
"""
read csv file
"""
nozzle= pd.read_csv("nozzle.csv", ",", skiprows=0)

"""
1. plot 
"""
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(nozzle.iloc[:,-2] , nozzle.iloc[:,6] , 'k', lw=lwh, label="$Z_t = 1.0$")


axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('$M$',fontsize=12) 
axes.set_title('Mach number vs $X$',fontsize=14)
axes.legend(loc=0 , prop={'size': 10}) # 
# fig1.savefig("M.pdf")


"""
2. compute Re 
"""

fluidname = "nitrogen"
L = 7.8/1000
Red = 11.6e3


dd = nozzle.iloc[-1,3]
pd = nozzle.iloc[-1,2]
td = nozzle.iloc[-1,4]



mu = CP.CoolProp.PropsSI('viscosity','P',pd,'T',td,fluidname) 
ud = nozzle.iloc[-1,5]*nozzle.iloc[-1,6]

Re = dd*ud*L/mu
print("Red, Re: ", Red, Re )
