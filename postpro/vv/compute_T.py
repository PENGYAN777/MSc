#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:35:29 2022

@author: yan

compute total temperature for given Reynold numbers

"""

from scipy.optimize import fsolve
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import CoolProp as CP

"""
0. fluid property
"""
fluidname = "nitrogen"
print("Fluid name:", fluidname)
R = CP.CoolProp.PropsSI("gas_constant",fluidname)
print("universal gas constant:  J/mol/K", R)
W = CP.CoolProp.PropsSI("molar_mass",fluidname)
print("molar mass: kg/mol", W)
Rs = R/W
print("spefific ags constant: J/Kg/K", Rs)
Tc =  CP.CoolProp.PropsSI("Tcrit",fluidname)
print("critical temperature[K]:", Tc)
Pc =  CP.CoolProp.PropsSI("pcrit",fluidname)
print("critical pressure[Pa]:", Pc)
"""
1. input total conditions
"""


Pt = 12e3

Tt=300

s = CP.CoolProp.PropsSI('Smass','P',Pt,'T',Tt,fluidname) 
ht = CP.CoolProp.PropsSI('Hmass','P',Pt,'T',Tt,fluidname) 

Red = 11.6e3
L = 7.8/1000
Md = 2
"""
2. compute isentropic relationship
"""

p = np.linspace(Pt*0.1,Pt,500) # P<Pc

p = pd.Series(p)
Z = np.zeros(p.size) # P/rho RT
h = np.zeros(p.size) # enthalpy
u = np.zeros(p.size) # velocity
v = np.zeros(p.size) # specific volume
c = np.zeros(p.size) # sound speed
m = np.zeros(p.size) # Mach number
d = np.zeros(p.size) # density
t = np.zeros(p.size) # temperature
g = np.zeros(p.size) # Gamma

for i in p.index:
    if abs(p[i]-Pc)<0.05*Pc:
        p[i] = 0.95*Pc
    d[i] = CP.CoolProp.PropsSI('Dmass','P',p[i],'Smass',s,fluidname) 
    v[i] = 1/d[i]
    t[i] = CP.CoolProp.PropsSI('T','P',p[i],'Smass',s,fluidname) 
    Z[i] = CP.CoolProp.PropsSI('Z','P',p[i],'Smass',s,fluidname) 
    # g[i] = CP.CoolProp.PropsSI('fundamental_derivative_of_gas_dynamics','P',p[i],'Smass',s,fluidname) 
    h[i] = CP.CoolProp.PropsSI('Hmass','Smass',s,'P',p[i],fluidname)
    u[i] = math.sqrt(abs(2*(ht-h[i])))
    c[i] = CP.CoolProp.PropsSI('A','P',p[i],'Smass',s,fluidname) 
    m[i] = u[i]/c[i] 

"""
3. find design condition at nozzle exit, Md = 2 
"""
print("index for design condition:",np.argmin(abs(m-2)))

dd = d[np.argmin(abs(m-2))]
vd = 1/dd
Td = t[np.argmin(abs(m-2))]
Pd = p[np.argmin(abs(m-2))]
ud = u[np.argmin(abs(m-2))]

"""
4. check Reynold number 
"""

mu = CP.CoolProp.PropsSI('viscosity','P',Pd,'T',Td,fluidname) 
Re = dd*ud*L/mu

print("Red, Re: ", Red, Re )
print("Pt[Pa], Tt[K]: ", Pt, Tt )
