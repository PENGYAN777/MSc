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
D=6.5


ex = pd.read_csv("ex.csv", ",", skiprows=0)
cfd_p = pd.read_csv("cfd_p.csv", ",", skiprows=0)
cfd_m = pd.read_csv("cfd_m.csv", ",", skiprows=0)
euler = pd.read_csv("pig_euler/m10new.csv", ",", skiprows=0)
rans = pd.read_csv("pig_rans/m10new.csv", ",", skiprows=0)

# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(ex.iloc[:,0] , ex.iloc[:,1], 'ko', lw=lwh, label="Ex")
axes.plot(euler.iloc[:,-5]/D , euler.iloc[:,-2]/P0, 'k', lw=lwh, label="EULER")
axes.plot(rans.iloc[:,-5]/D*1e3 , rans.iloc[:,-2]/P0, 'k--', lw=lwh, label="RANS")


# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

axes.set_xlabel('$X/D$',fontsize=12)
axes.set_ylabel('$P_i/P_0$',fontsize=12) 
axes.set_title('$P_i/P_0$ along centerline',fontsize=14)
axes.legend(loc=0) # 

axes.set_xlim([0, 10])
axes.set_ylim([0, 1])

fig1.savefig("vv_pt.pdf")

# # fig 2
# fig2 = plt.figure( dpi=300)
# lwh = 2
# axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(cfd_p.iloc[:,0] , cfd_p.iloc[:,1], 'k', lw=lwh, label="Guardon et.al")
# axes.plot(euler.iloc[:,-5]/D , euler.iloc[:,7]/P0, 'k--', lw=lwh, label="EULER")
# axes.plot(rans.iloc[:,-5]/D*1e3 , rans.iloc[:,11]/P0, 'b', lw=lwh, label="RANS")


# # axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# axes.set_xlabel('$X/D$',fontsize=12)
# axes.set_ylabel('$P/P_0$',fontsize=12) 
# axes.set_title('$P/P_0$ along centerline',fontsize=14)
# axes.legend(loc=0) # 

# axes.set_xlim([0, 10])
# axes.set_ylim([0, 0.4])

# fig2.savefig("vv_p.pdf")


# # fig 3
# fig3 = plt.figure( dpi=300)
# lwh = 2
# axes = fig3.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(cfd_m.iloc[:,0] , cfd_m.iloc[:,1], 'k', lw=lwh, label="Guardon et.al")
# axes.plot(euler.iloc[:,-5]/D , euler.iloc[:,3], 'k--', lw=lwh, label="EULER")
# axes.plot(rans.iloc[:,-5]/D*1e3 , rans.iloc[:,6], 'b', lw=lwh, label="RANS")


# # axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# axes.set_xlabel('$X/D$',fontsize=12)
# axes.set_ylabel('Mach',fontsize=12) 
# axes.set_title('Mach number along centerline',fontsize=14)
# axes.legend(loc=0) # 

# axes.set_xlim([0, 10])
# # axes.set_ylim([0, 0.4])

# fig3.savefig("vv_m.pdf")