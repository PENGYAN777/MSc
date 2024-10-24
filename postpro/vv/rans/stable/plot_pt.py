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


rd00= pd.read_csv("rd00new.csv", ",", skiprows=0)
rd02= pd.read_csv("rd02new.csv", ",", skiprows=0)
rd035= pd.read_csv("rd035new.csv", ",", skiprows=0)




# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(rd00.iloc[:,-7]/D , rd00.iloc[:,-4]/P0, 'k', lw=lwh, label="r/D=0")
axes.plot(rd02.iloc[:,-7]/D , rd02.iloc[:,-4]/P0, 'k--', lw=lwh, label="r/D=0.2")
axes.plot(rd035.iloc[:,-7]/D , rd035.iloc[:,-4]/P0, 'k-.', lw=lwh, label="r/D=0.35")
# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

axes.set_xlabel('$X/D$',fontsize=12)
axes.set_ylabel('$P_t/P_0$',fontsize=12) 
axes.set_title('$P_t/P_0$ along centerline',fontsize=14)
axes.legend(loc=0) # 

# fig1.savefig("vv_euler_stable_p.pdf")


