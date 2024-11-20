#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:05:08 2022

@author: yan

plot (P,T) diagram. show contour of compressibility factor Z and 
fundamental derivative of gasdynamics Gamma
"""

import matplotlib
import numpy as np
import CoolProp as CP
import matplotlib.pyplot as plt
import scipy.interpolate


# give fluid name
fluidname = "MM"

# update fluid
fluid = CP.AbstractState("HEOS", fluidname)

pc = fluid.keyed_output(CP.iP_critical)
Tc = fluid.keyed_output(CP.iT_critical)
ec = CP.CoolProp.PropsSI('Smass','T',Tc,'P',pc,fluidname)
Tmin =  CP.CoolProp.PropsSI("Ttriple",fluidname)
Tmax =  CP.CoolProp.PropsSI("Tmax",fluidname)
pmax = fluid.keyed_output(CP.iP_max)
pmin = fluid.keyed_output(CP.iP_min)
fillcolor = 'g'

# fig = plt.figure(figsize = (6,6))
# ax = fig.add_subplot(111)
fig = plt.figure(figsize=(6,5))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height]) 
lw = 3


# ----------------
# Saturation curve
# ----------------
Ts = np.linspace(Tmin, Tc, 1000)
es = CP.CoolProp.PropsSI('Smass','T',Ts,'Q',1,fluidname)

# ----------------
# Contour of Z and Gamma
# ----------------
n = 50 # number of points
y = np.linspace(400, Tmax,n)
x = np.linspace(600, 1600,n)
X,Y = np.meshgrid(x,y)
Z =  CP.CoolProp.PropsSI('Z','Smass',X,'T|gas',Y,fluidname)
Gamma =  CP.CoolProp.PropsSI('fundamental_derivative_of_gas_dynamics','Smass',X,'T',Y,fluidname)
#print(Z.shape)
levels = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
cp = plt.contour(X, Y, Z, levels, colors='black', linestyles='dashed')
plt.clabel(cp, inline=True,  fontsize=10)
plt.contourf(X, Y, Gamma, [0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4], cmap='rainbow')
plt.colorbar(label='$\Gamma$')
# ------
# Labels
# ------

plt.plot(es,Ts,'k',lw = lw, solid_capstyle = 'round', label = "LVS")
plt.plot(0,0,'k--',lw = lw/2, solid_capstyle = 'round', label = "Z")
# Critical lines
plt.axvline(ec, dashes = [2, 2])
plt.axhline(Tc, dashes = [2, 2])

"""
test points
"""
nc = 10
colors = plt.cm.tab20(np.linspace(0, 1, nc))

z_p = [ 4.4e5, ]
z_t = [ 500, ]
z_s = CP.CoolProp.PropsSI('Smass','P',z_p,'T',z_t,fluidname)
plt.plot(z_s,z_t,'ro' ,lw = lw,label = "working conditions")



ax.legend(loc=4) # 2 means left top

plt.ylim(400,Tmax)
# plt.gca().set_yscale('log')
plt.gca().set_xlim(600, 1600)
plt.xlabel('S [J/K]')
plt.ylabel('T [K]')
# plt.title('Contour of Z and $\Gamma$ for siloxane MM')
plt.tight_layout()
fig.savefig("files/mm_nicfd_Contour_TS.eps")
print("plotcontour.py called")