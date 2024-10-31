#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:51:54 2024

@author: yan
"""

import numpy as np
import CoolProp as CP
import pandas as pd
import math

fluidname = "PR::nitrogen"
data = pd.read_csv("m8.csv", ",")
g = 1.4
R = 297
cp = g*R/(g-1)
# data = pd.read_csv("rd035.csv", ",")
P = data.iloc[:,10] 
T = data.iloc[:,15] 
D = data.iloc[:,0] 
M = data.iloc[:,5]  

# P = data.iloc[:,8] 
# T = data.iloc[:,13] 
# D = data.iloc[:,0] 
# M = data.iloc[:,4]  

################# find location of Mach disk
max_index = np.argmax(M)


print("size", P.index)

PT = 1.2e4
TT = 300
# ht = CP.CoolProp.PropsSI('Hmass','T',TT,'P',PT,fluidname)
s = np.zeros(P.size)
ht = np.zeros(P.size)
for i in P.index:                       
        # h = CP.CoolProp.PropsSI('Hmass','T',T[i],'P',P[i],fluidname)
        h = cp*T[i]
        # ux = data.iloc[i,5]/data.iloc[i,0]    
        # uy = data.iloc[i,6]/data.iloc[i,0]  
        ux = data.iloc[i,6]/data.iloc[i,0]    
        uy = data.iloc[i,7]/data.iloc[i,0]  
        uu = ux*ux + uy*uy
        ht[i] = h +0.5*uu
        # s[i] = CP.CoolProp.PropsSI('Smass','T',T[i],'P',P[i],fluidname)
        s[i] = cp*np.log(T[i]) -R*np.log(P[i])

s0 = min(s)
s1 = max(s)

pt = np.zeros(P.size)
pi = np.zeros(P.size)
f1 = np.zeros(P.size)
f2 = np.zeros(P.size)
Z = np.zeros(P.size)
for i in P.index:
    # if i<= max_index:
    #     s[i] = s0
    # else:
    #     s[i] = s1
    Z[i] =  CP.CoolProp.PropsSI('Z','T',T[i],'P',P[i],fluidname)
    pt[i] =  math.exp(( cp*np.log(ht[i]/cp) - s[i] ) / R)
    # pt[i] = CP.CoolProp.PropsSI('P','Smass',s[i],'Hmass',ht[i],fluidname)
    if M[i]>1:
        # G[i] = CP.CoolProp.PropsSI('fundamental_derivative_of_gas_dynamics',
        #                             'T',T[i],'P',P[i],fluidname)
        # normal shock realtion Pt1/Pt2
        f1[i] = ((g+1)*M[i]*M[i] / ( (g-1)*M[i]*M[i]+2 ))**(g/(g-1))
        f2[i] = ((g+1) / (2*g*M[i]*M[i] -g+1) )**(1/(g-1))
        pi[i] = pt[i]*f1[i]*f2[i]
    else:
        pi[i] = pt[i]
        
# append new columns
# shG =pd.DataFrame({'G':G, })
shG =pd.DataFrame({'pt':pt, 'pi':pi,'s':s, 'ht':ht,  'Z':Z, })
newData = pd.concat([data, shG], join = 'outer', axis = 1)
# save newData in csv file
newData.to_csv("m8new.csv")
# newData.to_csv("rd035new.csv")