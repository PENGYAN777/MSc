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
fluidname = "PR::MM"
# fluidname = "HEOS::D6"
Pc = CP.CoolProp.PropsSI('Pcrit',fluidname)
Tc = CP.CoolProp.PropsSI('Tcrit',fluidname)
dc = CP.CoolProp.PropsSI('rhocrit',fluidname)
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
# cv = CP.CoolProp.PropsSI('CVMASS','T', T, 'P', P,  fluidname)
# cp = CP.CoolProp.PropsSI('CPMASS','T', T, 'P', P,  fluidname)
# g = cp/cv
# Z = CP.CoolProp.PropsSI('Z', 'P',P,'T', T,fluidname)

Zt = 0.9
Tt = 500

Pt, Gt = PGfromZT(Zt,Tt)


