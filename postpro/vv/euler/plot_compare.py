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

P0 = 1.2e4
D=0.0078

mesh3 = pd.read_csv("m3new.csv", ",", skiprows=0)






# # fig 1
# fig1 = plt.figure( dpi=300)
# lwh = 2
# axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(mesh6.iloc[:,-7]/D , mesh6.iloc[:,7]/P0, 'r', lw=lwh, label="166k")
# axes.plot(mesh7.iloc[:,-7]/D , mesh7.iloc[:,7]/P0, 'g', lw=lwh, label="213k")
# axes.plot(mesh8.iloc[:,-7]/D , mesh8.iloc[:,7]/P0, 'b', lw=lwh, label="272k")
# # axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# axes.set_xlabel('$X/D$',fontsize=12)
# axes.set_ylabel('$P/P_0$',fontsize=12) 
# axes.set_title('$P/P_0$ along centerline',fontsize=14)
# axes.legend(loc=0) # 

# fig1.savefig("vv_euler_stable_p.pdf")

# # fig 2
# fig2 = plt.figure( dpi=300)
# lwh = 2
# axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(mesh6.iloc[:,-7]/D , mesh6.iloc[:,3], 'r', lw=lwh, label="166k")
# axes.plot(mesh7.iloc[:,-7]/D , mesh7.iloc[:,3], 'g', lw=lwh, label="213k")
# axes.plot(mesh8.iloc[:,-7]/D , mesh8.iloc[:,3], 'b', lw=lwh, label="272k")
# # axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# axes.set_xlabel('$X/D$',fontsize=12)
# axes.set_ylabel('Mach',fontsize=12) 
# axes.set_title('Mach number along centerline',fontsize=14)
# axes.legend(loc=0) # 

# fig2.savefig("vv_euler_stable_m.pdf")


# fig 3
fig3 = plt.figure( dpi=300)
lwh = 2
axes = fig3.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure

axes.plot(mesh3.iloc[:,-6]/D , mesh3.iloc[:,-2], 'b', lw=lwh, label="lvl 10")
# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

axes.set_xlabel('$X/D$',fontsize=12)
axes.set_ylabel('s',fontsize=12) 
axes.set_title('Entropy along centerline',fontsize=14)
axes.legend(loc=0) # 
# fig3.savefig("vv_euler_stable_s.pdf")
