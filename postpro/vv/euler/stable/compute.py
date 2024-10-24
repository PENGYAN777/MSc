#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:51:54 2024

@author: yan
"""

import numpy as np
import CoolProp as CP
import pandas as pd

fluidname = "HEOS::nitrogen"
data = pd.read_csv("m8.csv", ",")
# data = pd.read_csv("rd035.csv", ",")
P = data.iloc[:,6] 
T = data.iloc[:,8] 
D = data.iloc[:,0] 
M = data.iloc[:,2] 

################# find location of Mach disk
max_index = np.argmax(M)
# pre Mach disk entropy
s0 = CP.CoolProp.PropsSI('Smass','T',T[max_index],'P',P[max_index],fluidname)
# post Mach disk entropy
s1 = CP.CoolProp.PropsSI('Smass','T',T[T.size-1],'P',P[P.size-1],fluidname)


g = 1.4
R = 297
print("size", P.index)

PT = 804804
TT = 339.56
# ht = CP.CoolProp.PropsSI('Hmass','T',TT,'P',PT,fluidname)
s = np.zeros(P.size)
ht = np.zeros(P.size)
for i in P.index:                       
        # Z[i] =  CP.CoolProp.PropsSI('Z','T',T[i],'P',P[i],fluidname)
        s[i] =  CP.CoolProp.PropsSI('Smass','T',T[i],'P',P[i],fluidname)
        h = CP.CoolProp.PropsSI('Hmass','T',T[i],'P',P[i],fluidname)
        c = CP.CoolProp.PropsSI('A','T',T[i],'P',P[i],fluidname)
        u = c*M[i]
        ht[i] = h +0.5*u*u
        # s[i] = R/(g-1)*np.log(T[i]) + R*np.log(1/D[i] )

pt = np.zeros(P.size)
pi = np.zeros(P.size)
Z = np.zeros(P.size)
# s = np.zeros(P.size)
f1 = np.zeros(P.size)
f2 = np.zeros(P.size)
for i in P.index:
    # if i<= max_index:
    #     s[i] = s0
    # else:
    #     s[i] = s1
    if M[i]>1:
        # G[i] = CP.CoolProp.PropsSI('fundamental_derivative_of_gas_dynamics',
        #                             'T',T[i],'P',P[i],fluidname)
        Z[i] =  CP.CoolProp.PropsSI('Z','T',T[i],'P',P[i],fluidname)
        pt[i] = CP.CoolProp.PropsSI('P','Smass',s[i] ,'Hmass',ht[i], fluidname)
        # normal shock realtion Pt1/Pt2
        f1[i] = ((g+1)*M[i]*M[i] / ( (g-1)*M[i]*M[i]+2 ))**(g/(g-1))
        f2[i] = ((g+1) / (2*g*M[i]*M[i] -g+1) )**(1/(g-1))
        pi[i] = pt[i]*f1[i]*f2[i]
    else:
        Z[i] =  CP.CoolProp.PropsSI('Z','T',T[i],'P',P[i],fluidname)
        pt[i] = CP.CoolProp.PropsSI('P','Smass',s[i] ,'Hmass',ht[i], fluidname)
        pi[i] = pt[i]
        
# append new columns
# shG =pd.DataFrame({'G':G, })
shG =pd.DataFrame({'pt':pt, 'pi':pi,'s':s, 'Z':Z, })
newData = pd.concat([data, shG], join = 'outer', axis = 1)
# save newData in csv file
newData.to_csv("m8new.csv")
# newData.to_csv("rd035new.csv")