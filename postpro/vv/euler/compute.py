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
data = pd.read_csv("m10.csv", ",")
g = 1.4
R = 297
cp = g*R/(g-1)
# data = pd.read_csv("rd035.csv", ",")
P = data.iloc[:,6] 
T = data.iloc[:,8] 
D = data.iloc[:,0] 
M = data.iloc[:,2]  

################# find location of Mach disk
max_index = np.argmax(M)
# pre Mach disk entropy
s0 = cp*np.log(T[0]) -R*np.log(P[0]) 
# s0 = CP.CoolProp.PropsSI('Smass','T',T[0],'P',P[0],fluidname)
# post Mach disk entropy
# s1 = cp*np.log(T[ P.size-1 ]) -R*np.log(P[ P.size-1 ]) 
s1 = cp*np.log(T[ max_index+1 ]) -R*np.log(P[ max_index+1 ]) 
# s1 = CP.CoolProp.PropsSI('Smass','T',T[T.size-1],'P',P[P.size-1],fluidname)



print("size", P.index)

PT = 1.2e4
TT = 300
ht = CP.CoolProp.PropsSI('Hmass','T',TT,'P',PT,fluidname)
s = np.zeros(P.size)
# ht = np.zeros(P.size)
for i in P.index:                       
        # Z[i] =  CP.CoolProp.PropsSI('Z','T',T[i],'P',P[i],fluidname)
        # s[i] =  CP.CoolProp.PropsSI('Smass','T',T[i],'P',P[i],fluidname)
        # h = CP.CoolProp.PropsSI('Hmass','T',T[i],'P',P[i],fluidname)
        # c = CP.CoolProp.PropsSI('A','T',T[i],'P',P[i],fluidname)
        # u = c*M[i]
        # ht[i] = h +0.5*u*u
        s[i] = cp*np.log(T[i]) -R*np.log(P[i])

pt = np.zeros(P.size)
pi = np.zeros(P.size)
f1 = np.zeros(P.size)
f2 = np.zeros(P.size)
Z = np.zeros(P.size)
for i in P.index:
    if i<= max_index:
        s[i] = s0
    else:
        s[i] = s1
    Z[i] =  CP.CoolProp.PropsSI('Z','T',T[i],'P',P[i],fluidname)
    pt[i] =  math.exp(( cp*np.log(ht/cp) - s[i] ) / R)
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
newData.to_csv("m10new.csv")
# newData.to_csv("rd035new.csv")