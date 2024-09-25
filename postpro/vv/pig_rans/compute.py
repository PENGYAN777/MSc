#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:51:54 2024

@author: yan
"""

import numpy as np
import CoolProp as CP
import pandas as pd
import os
from IPython import get_ipython;   
get_ipython().magic('reset -sf')
os.system('clear')

fluidname = "HEOS::nitrogen"

Pt = 804804
Tt = 339.56
ht = CP.CoolProp.PropsSI('Hmass','T',Tt,'P',Pt,fluidname)

data = pd.read_csv("m8.csv", ",")
P = data.iloc[:,10] 
T = data.iloc[:,15] 
D = data.iloc[:,0] 
M = data.iloc[:,5] 
g = 1.4
print("size", P.index)

pt = np.zeros(P.size)
Pt = np.zeros(P.size)
Z = np.zeros(P.size)
# ht = np.zeros(P.size)
s = np.zeros(P.size)
f1 = np.zeros(P.size)
f2 = np.zeros(P.size)
for i in P.index:
    if M[i]>1:
        # G[i] = CP.CoolProp.PropsSI('fundamental_derivative_of_gas_dynamics',
        #                             'T',T[i],'P',P[i],fluidname)
        Z[i] =  CP.CoolProp.PropsSI('Z','T',T[i],'P',P[i],fluidname)
        s =  CP.CoolProp.PropsSI('Smass','T',T[i],'P',P[i],fluidname)
        h =  CP.CoolProp.PropsSI('Hmass','T',T[i],'P',P[i],fluidname)
        c =  CP.CoolProp.PropsSI('A','T',T[i],'P',P[i],fluidname)
        u = c*M[i] 
        Pt[i] = CP.CoolProp.PropsSI('P','Smass',s ,'Hmass',ht, fluidname)
        # normal shock realtion Pt1/Pt2
        f1[i] = ((g+1)*M[i]*M[i] / ( (g-1)*M[i]*M[i]+2 ))**(g/(g-1))
        f2[i] = ((g+1) / (2*g*M[i]*M[i] -g+1) )**(1/(g-1))
        pt[i] = Pt[i]*f1[i]*f2[i]
    else:
        Z[i] =  CP.CoolProp.PropsSI('Z','T',T[i],'P',P[i],fluidname)
        s =  CP.CoolProp.PropsSI('Smass','T',T[i],'P',P[i],fluidname)
        h =  CP.CoolProp.PropsSI('Hmass','T',T[i],'P',P[i],fluidname)
        c =  CP.CoolProp.PropsSI('A','T',T[i],'P',P[i],fluidname)
        u = c*M[i] 
        pt[i] = CP.CoolProp.PropsSI('P','Smass',s ,'Hmass',ht, fluidname)
# append new columns
# shG =pd.DataFrame({'G':G, })
shG =pd.DataFrame({'Ptot':pt, 'Z':Z, })
newData = pd.concat([data, shG], join = 'outer', axis = 1)
# save newData in csv file
# newData.to_csv("m4sh.csv")
newData.to_csv("m8new.csv")