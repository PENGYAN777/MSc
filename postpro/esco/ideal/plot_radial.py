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
gm= pd.read_csv("gra/m/radial.csv", ",", skiprows=0)
gp= pd.read_csv("gra/p/radial.csv", ",", skiprows=0)
gt= pd.read_csv("gra/t/radial.csv", ",", skiprows=0)
ge= pd.read_csv("gra/e/radial.csv", ",", skiprows=0)

D=6.5

fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(refer.iloc[:,7]/D , refer.iloc[:,0]/refer.iloc[0,0], 'k', lw=lwh, label="reference")
axes.plot(gd.iloc[:,7]/D , gd.iloc[:,0]/refer.iloc[0,0] , 'r', lw=lwh, label="$\\nabla \\rho$")
axes.plot(gm.iloc[:,7]/D , gm.iloc[:,0]/refer.iloc[0,0] , 'b', lw=lwh, label="$\\nabla M$")
axes.plot(gp.iloc[:,7]/D , gp.iloc[:,0]/refer.iloc[0,0] , 'g', lw=lwh, label="$\\nabla P$")
axes.plot(gt.iloc[:,7]/D , gt.iloc[:,0]/refer.iloc[0,0] , 'y', lw=lwh, label="$\\nabla T$")
axes.plot(ge.iloc[:,7]/D , ge.iloc[:,0]/refer.iloc[0,0] , 'm', lw=lwh, label="$\\nabla s$")

axes.set_xlabel('$X/D$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$\\rho/\\rho_t$',fontsize=12) 
# axes.set_aspect('equal', 'box')
axes.set_title('$\\rho/\\rho_t$ at $X=10[mm]$',fontsize=14)

axes.legend(loc=0 , prop={'size': 10}) # 
# axes.set_xlim(0,0.12)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("refer_ideal_gra_rho.pdf")

fig2 = plt.figure( dpi=300)
lwh = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(refer.iloc[:,7]/D , refer.iloc[:,1] , 'k', lw=lwh, label="reference")
axes.plot(gd.iloc[:,7]/D , gd.iloc[:,1], 'r', lw=lwh, label="$\\nabla \\rho$")
axes.plot(gm.iloc[:,7]/D , gm.iloc[:,1], 'b', lw=lwh, label="$\\nabla M$")
axes.plot(gp.iloc[:,7]/D , gp.iloc[:,1], 'g', lw=lwh, label="$\\nabla P$")
axes.plot(gt.iloc[:,7]/D , gt.iloc[:,1] , 'y', lw=lwh, label="$\\nabla T$")
axes.plot(ge.iloc[:,7]/D , ge.iloc[:,1] , 'm', lw=lwh, label="$\\nabla s$")

axes.set_xlabel('$X/D$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('Mach',fontsize=12) 
# axes.set_aspect('equal', 'box')
axes.set_title('Mach at $X=10[mm]$',fontsize=14)

axes.legend(loc=0 , prop={'size': 10}) # 
# axes.set_xlim(0,0.12)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig2.savefig("refer_ideal_gra_m.pdf")

fig3 = plt.figure( dpi=300)
lwh = 2
axes = fig3.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(refer.iloc[:,7]/D , refer.iloc[:,3]/refer.iloc[0,3] , 'k', lw=lwh, label="reference")
axes.plot(gd.iloc[:,7]/D , gd.iloc[:,3]/refer.iloc[0,3] , 'r', lw=lwh, label="$\\nabla \\rho$")
axes.plot(gm.iloc[:,7]/D , gm.iloc[:,3]/refer.iloc[0,3] , 'b', lw=lwh, label="$\\nabla M$")
axes.plot(gp.iloc[:,7]/D , gp.iloc[:,3]/refer.iloc[0,3] , 'g', lw=lwh, label="$\\nabla P$")
axes.plot(gt.iloc[:,7]/D , gt.iloc[:,3]/refer.iloc[0,3] , 'y', lw=lwh, label="$\\nabla T$")
axes.plot(ge.iloc[:,7]/D , ge.iloc[:,3]/refer.iloc[0,3] , 'm', lw=lwh, label="$\\nabla s$")

axes.set_xlabel('$X/D$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$T/T_t$',fontsize=12) 
# axes.set_aspect('equal', 'box')
axes.set_title('$T/T_t$ at $X=10[mm]$',fontsize=14)

axes.legend(loc=0 , prop={'size': 10}) # 
# axes.set_xlim(0,0.12)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig3.savefig("refer_ideal_gra_t.pdf")
