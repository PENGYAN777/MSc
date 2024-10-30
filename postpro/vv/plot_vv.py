#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:48:31 2024

@author: yan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 19:01:08 2022

@author: yan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:35:29 2022

@author: yan

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import os
import CoolProp as CP
from IPython import get_ipython;   
get_ipython().magic('reset -sf')
os.system('clear')


fluidname = "HEOS::Nitrogen"
# fluidname = "HEOS::D6"
Pc = CP.CoolProp.PropsSI('Pcrit',fluidname)
Tc = CP.CoolProp.PropsSI('Tcrit',fluidname)
dc = CP.CoolProp.PropsSI('rhocrit',fluidname)

P0 = 804804
D1=6.5
D2=0.0065


ex = pd.read_csv("ex.csv", ",", skiprows=0)
cfd = pd.read_csv("paper_cfd.csv", ",", skiprows=0)
euler = pd.read_csv("euler/cfd/m8new.csv", ",", skiprows=0)
rans = pd.read_csv("rans/cfd/m8new.csv", ",", skiprows=0)
# un = pd.read_csv("unstable/m1new.csv", ",", skiprows=0)

# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(ex.iloc[:,0] , ex.iloc[:,1], 'ko', lw=lwh, label="Katanoda et.al Ex")
# axes.plot(cfd.iloc[:,0] , cfd.iloc[:,1], 'k', lw=lwh, label="Katanoda et.al CFD $P_i$")
axes.plot(euler.iloc[:,-8]/D1 , euler.iloc[:,-4]/P0, 'b', lw=lwh, label="EULER")
axes.plot(rans.iloc[:,-8]/D2 , rans.iloc[:,-4]/P0, 'b--', lw=lwh, label="RANS")

# axes.plot(un.iloc[:,-5]/D , un.iloc[:,-2]/P0, 'k--', lw=lwh, label="Unstable")



# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

axes.set_xlabel('$X/D$',fontsize=12)
axes.set_ylabel('$P_i/P_t$',fontsize=12) 
axes.set_title('$P_i/P_t$ along centerline',fontsize=14)
axes.legend(loc=0) # 

axes.set_xlim([0, 10])
axes.set_ylim([0, 1])

fig1.savefig("vv_pt.pdf")

