#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 11:18:57 2022

@author: P.Yan

main function of CoolProp extensions
"""
import os
import CoolProp as CP
import math
from newIOpairs import TGfromZP, PGfromZT, PTfromZG, ZPfromTG, ZTfromPG, ZGfromPT

# compute active degree of freedom
print("------------compute N-----------")
fluidname = "HEOS::MM"
# fluidname = "HEOS::D6"
Pc = CP.CoolProp.PropsSI('Pcrit',fluidname)
Tc = CP.CoolProp.PropsSI('Tcrit',fluidname)
dc = CP.CoolProp.PropsSI('rhocrit',fluidname)
ec = CP.CoolProp.PropsSI('Umass','P', Pc , 'T', Tc ,fluidname)
vc = 1/dc
w = CP.CoolProp.PropsSI('ACENTRIC',fluidname)
print("fluid name:", fluidname)
R = CP.CoolProp.PropsSI('GAS_CONSTANT',fluidname)
print("Universal gas constant:", R)
MW = CP.CoolProp.PropsSI('M',fluidname)
print("molar mass:", MW)
Rs = R/MW
print("specific gas constant:", Rs)
CP.CoolProp.get_global_param_string("HOME")
# fluidname = "PR::MD4M"
# G = CP.CoolProp.PropsSI('fundamental_derivative_of_gas_dynamics', 'P',P,'T', T,fluidname)
# print("G = :", G)  

"""
1. input total conditions
"""

# # pt = 1.55e6 # total pressure
# # pt = 2.13e6 # total pressure
# pt = 2.32e6 # total pressure
# zt = 0.5
# tt,gt = TGfromZP(zt,pt)

# cp = CP.CoolProp.PropsSI('Cpmass','P',pt*0.2,'T',tt*0.95,fluidname)
# cv = CP.CoolProp.PropsSI('Cvmass','P',pt*0.2,'T',tt*0.95,fluidname)
# gamma = cp/cv

# Secant reached maximum number of iterations example
# x = CP.CoolProp.PropsSI('P','Umass',392617, 'Dmass', 268.92+0.01 ,fluidname)
# print(x)

# # Secant reached maximum number of iterations example
# x = CP.CoolProp.PropsSI('P','Umass',2.29588e+06, 'Dmass', 5.75102 ,fluidname)
# print(x)

p = 1.64798e+06
t = 503.712
x = CP.CoolProp.PropsSI('Dmass','P',p, 'T', t ,fluidname)
print(x)

