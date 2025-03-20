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

refer= pd.read_csv("../ref/radial.csv", ",", skiprows=0)
gd= pd.read_csv("d/radial.csv", ",", skiprows=0)
gm= pd.read_csv("m/radial.csv", ",", skiprows=0)
gp= pd.read_csv("p/radial.csv", ",", skiprows=0)
gt= pd.read_csv("t/radial.csv", ",", skiprows=0)
dm= pd.read_csv("dm/radial.csv", ",", skiprows=0)
dp= pd.read_csv("dp/radial.csv", ",", skiprows=0)
pm= pd.read_csv("pm/radial.csv", ",", skiprows=0)

D = 6.5

fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(refer.iloc[:,-2]/D , refer.iloc[:,0]/refer.iloc[0,0], 'k', lw=lwh, label="reference")
axes.plot(gd.iloc[:,-2]/D , gd.iloc[:,0]/refer.iloc[0,0] , 'r', lw=lwh, label="$H(\\rho)$")
axes.plot(gm.iloc[:,-2]/D , gm.iloc[:,0]/refer.iloc[0,0] , 'b', lw=lwh, label="$H(M)$")
axes.plot(gp.iloc[:,-2]/D , gp.iloc[:,0]/refer.iloc[0,0] , 'g', lw=lwh, label="$H(P)$")
axes.plot(gt.iloc[:,-2]/D , gt.iloc[:,0]/refer.iloc[0,0] , 'y', lw=lwh, label="$H(T)$")
axes.plot(dm.iloc[:,-2]/D , dm.iloc[:,0]/refer.iloc[0,0] , 'm', lw=lwh, label="$H(\\rho)$ + $H(M)$")
axes.plot(dp.iloc[:,-2]/D , dp.iloc[:,0]/refer.iloc[0,0] , 'c', lw=lwh, label="$H(\\rho)$ + $H(P)$")
axes.plot(pm.iloc[:,-2]/D , pm.iloc[:,0]/refer.iloc[0,0] , 'orange', lw=lwh, label="$H(P)$ + $H(M)$")
# axes.set_xlabel('$Y/D$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$\\rho/\\rho_s$',fontsize=12) 
# axes.set_aspect('equal', 'box')
# axes.set_title('$\\rho/\\rho_s$ at $X/D=1.54$',fontsize=14)

axes.legend(loc=0 , prop={'size': 10}) # 
fig1.savefig("non_hes_rho.pdf")

fig2 = plt.figure( dpi=300)
lwh = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(refer.iloc[:,-2]/D , refer.iloc[:,5] , 'k', lw=lwh, label="reference")
axes.plot(gd.iloc[:,-2]/D , gd.iloc[:,5], 'r', lw=lwh, label="$H(\\rho)$")
axes.plot(gm.iloc[:,-2]/D , gm.iloc[:,5], 'b', lw=lwh, label="$H(M)$")
axes.plot(gp.iloc[:,-2]/D , gp.iloc[:,5], 'g', lw=lwh, label="$H(P)$")
axes.plot(gt.iloc[:,-2]/D , gt.iloc[:,5], 'y', lw=lwh, label="$H(T)$")
axes.plot(dm.iloc[:,-2]/D , dm.iloc[:,5], 'm', lw=lwh, label="$H(\\rho)$ + $H(M)$")
axes.plot(dp.iloc[:,-2]/D , dp.iloc[:,5], 'c', lw=lwh, label="$H(\\rho)$ + $H(P)$")
axes.plot(pm.iloc[:,-2]/D , pm.iloc[:,5], 'orange', lw=lwh, label="$H(P)$ + $H(M)$")

axes.set_xlabel('$Y/D$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('Mach',fontsize=12) 
# axes.set_aspect('equal', 'box')
# axes.set_title('Mach at $X/D=1.54$',fontsize=14)

axes.legend(loc=0 , prop={'size': 10}) # 
fig2.savefig("non_hes_m.pdf")

fig3 = plt.figure( dpi=300)
lwh = 2
axes = fig3.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(refer.iloc[:,-2]/D , refer.iloc[:,15]/refer.iloc[0,15] , 'k', lw=lwh, label="reference")
axes.plot(gd.iloc[:,-2]/D , gd.iloc[:,15]/refer.iloc[0,15] , 'r', lw=lwh, label="$H(\\rho)$")
axes.plot(gm.iloc[:,-2]/D , gm.iloc[:,15]/refer.iloc[0,15] , 'b', lw=lwh, label="$H(M)$")
axes.plot(gp.iloc[:,-2]/D , gp.iloc[:,15]/refer.iloc[0,15] , 'g', lw=lwh, label="$H(P)$")
axes.plot(gt.iloc[:,-2]/D , gt.iloc[:,15]/refer.iloc[0,15] , 'y', lw=lwh, label="$H(T)$")
axes.plot(dm.iloc[:,-2]/D , dm.iloc[:,15]/refer.iloc[0,15] , 'm', lw=lwh, label="$H(\\rho)$ + $H(M)$")
axes.plot(dp.iloc[:,-2]/D , dp.iloc[:,15]/refer.iloc[0,15] , 'c', lw=lwh, label="$H(\\rho)$ + $H(P)$")
axes.plot(pm.iloc[:,-2]/D , pm.iloc[:,15]/refer.iloc[0,15] , 'orange', lw=lwh, label="$H(P)$ + $H(M)$")

axes.set_xlabel('$Y/D$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$T/T_s$',fontsize=12) 
# axes.set_aspect('equal', 'box')
# axes.set_title('$T/T_s$ at $X/D=1.54$',fontsize=14)

axes.legend(loc=0 , prop={'size': 10}) # 
fig3.savefig("non_hes_t.pdf")
