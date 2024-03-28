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
D=6.5


mesh3 = pd.read_csv("m3new.csv", ",", skiprows=0)
mesh4 = pd.read_csv("m4new.csv", ",", skiprows=0)
mesh5 = pd.read_csv("m5new.csv", ",", skiprows=0)
mesh6 = pd.read_csv("m6new.csv", ",", skiprows=0)
mesh6s = pd.read_csv("m6news.csv", ",", skiprows=0)



# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(mesh3.iloc[:,-5]/D , mesh3.iloc[:,7]/P0, 'k', lw=lwh, label="25k")
axes.plot(mesh4.iloc[:,-5]/D , mesh4.iloc[:,7]/P0, 'r', lw=lwh, label="33k")
axes.plot(mesh5.iloc[:,-5]/D , mesh5.iloc[:,7]/P0, 'g', lw=lwh, label="42k")
axes.plot(mesh6.iloc[:,-5]/D , mesh6.iloc[:,7]/P0, 'b', lw=lwh, label="55k")
# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

axes.set_xlabel('$X/D$',fontsize=12)
axes.set_ylabel('$P/P_0$',fontsize=12) 
axes.set_title('$P/P_0$ along centerline',fontsize=14)
axes.legend(loc=0) # 

fig1.savefig("vv_pig_euler_p.pdf")

# fig 2
fig2 = plt.figure( dpi=300)
lwh = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(mesh3.iloc[:,-5]/D , mesh3.iloc[:,3], 'k', lw=lwh, label="25k")
axes.plot(mesh4.iloc[:,-5]/D , mesh4.iloc[:,3], 'r', lw=lwh, label="33k")
axes.plot(mesh5.iloc[:,-5]/D , mesh5.iloc[:,3], 'g', lw=lwh, label="42k")
axes.plot(mesh6.iloc[:,-5]/D , mesh6.iloc[:,3], 'b', lw=lwh, label="55k")
# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

axes.set_xlabel('$X/D$',fontsize=12)
axes.set_ylabel('Mach',fontsize=12) 
axes.set_title('Mach number along centerline',fontsize=14)
axes.legend(loc=0) # 

fig2.savefig("vv_pig_euler_m.pdf")


# fig 3
fig3 = plt.figure( dpi=300)
lwh = 2
axes = fig3.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(mesh6s.iloc[:,-5]/D , mesh6s.iloc[:,-2], 'b', lw=lwh, label="55k")
axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

axes.set_xlabel('$X/D$',fontsize=12)
axes.set_ylabel('S',fontsize=12) 
# axes.set_title('Mach number along centerline',fontsize=14)
axes.legend(loc=0) # 

# fig2.savefig("vv_pig_euler_m.pdf")





