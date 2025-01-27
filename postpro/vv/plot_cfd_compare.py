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



cfd = pd.read_csv("cfd_p.csv", ",", skiprows=0)
euler = pd.read_csv("euler/cfd/m8.csv", ",", skiprows=0)


# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure

axes.plot(cfd.iloc[:,0] , cfd.iloc[:,1], 'k', lw=lwh, label="Guardone et.al")
axes.plot(euler.iloc[:,-3]/D1 , euler.iloc[:,6]/P0, 'r', lw=lwh, label="EULER")




# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

axes.set_xlabel('$X/D$',fontsize=12)
axes.set_ylabel('$P/P_t$',fontsize=12) 
axes.set_title('$P/P_t$ along centerline',fontsize=14)
axes.legend(loc=0) # 

# axes.set_xlim([0, 10])
# axes.set_ylim([0, 1])

fig1.savefig("vv_p.pdf")

