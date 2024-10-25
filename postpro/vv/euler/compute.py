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

fluidname = "HEOS::nitrogen"
data = pd.read_csv("m3.csv", ",")
# data = pd.read_csv("rd035.csv", ",")
P = data.iloc[:,6] 
T = data.iloc[:,8] 
D = data.iloc[:,0] 
M = data.iloc[:,2] 



g = 1.4
R = 297
cv = R/(g-1)
cp = R*g/(g-1)
print("size", P.index)

PT = 1.2e4
TT = 300
s = np.zeros(P.size)
h = np.zeros(P.size)
ht = np.zeros(P.size)
pt = np.zeros(P.size)
for i in P.index:                       
        s[i] = cp*np.log(T[i]) - R*np.log(P[i] )
        h[i] = cp*T[i]
        ux = data.iloc[i,3]/data.iloc[i,0]  
        uy = data.iloc[i,4]/data.iloc[i,0]  
        uu = ux*ux + uy*uy
        ht[i] = h[i] + 0.5*uu
        pt[i] = math.exp(cp/R*np.log(ht[i]/cp) -  s[i]/R )
        
pi = np.zeros(P.size)
f1 = np.zeros(P.size)
f2 = np.zeros(P.size)
for i in P.index:
    if M[i]>1:
        # normal shock realtion Pt1/Pt2
        f1[i] = ((g+1)*M[i]*M[i] / ( (g-1)*M[i]*M[i]+2 ))**(g/(g-1))
        f2[i] = ((g+1) / (2*g*M[i]*M[i] -g+1) )**(1/(g-1))
        pi[i] = pt[i]*f1[i]*f2[i]
    else:
        pi[i] = pt[i]
        
# append new columns
# shG =pd.DataFrame({'G':G, })
shG =pd.DataFrame({'pt':pt, 'pi':pi,'s':s,})
newData = pd.concat([data, shG], join = 'outer', axis = 1)
# save newData in csv file
newData.to_csv("m3new.csv")
newData.to_csv("rd035new.csv")