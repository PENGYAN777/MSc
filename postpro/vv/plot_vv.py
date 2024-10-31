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


P0 = 1.2e4
D=0.0078


ex = pd.read_csv("ex.csv", ",", skiprows=0)
euler = pd.read_csv("euler/m9new.csv", ",", skiprows=0)
rans = pd.read_csv("rans/m3new.csv", ",", skiprows=0)

"""
1. plot
"""

# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(ex.iloc[:,0] , ex.iloc[:,1], 'ko', lw=lwh, label="Katanoda et.al Ex")
axes.plot(euler.iloc[:,-8]/D , euler.iloc[:,-4]/P0, 'b', lw=lwh, label="EULER")
axes.plot(rans.iloc[:,-8]/D , rans.iloc[:,-4]/P0, 'b--', lw=lwh, label="RANS")


# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

axes.set_xlabel('$X/D$',fontsize=12)
axes.set_ylabel('$P_i/P_t$',fontsize=12) 
axes.set_title('$P_i/P_t$ along centerline',fontsize=14)
axes.legend(loc=0) # 

axes.set_xlim([0, 8])
axes.set_ylim([0, 0.8])

fig1.savefig("vv_pt.pdf")

"""
2. compute the average difference
"""
n = 11
diff = np.zeros(n)
x = np.zeros(n)
x1 = np.zeros(n)
y = np.zeros(n)
for i in range(0,n,1):
    x[i] = ex.iloc[i,0]
    x1[i] = np.argmin(abs(rans.iloc[:,-8]/D-x[i]))
    y[i] = rans.iloc[:,-4][x1[i]]/P0
    diff[i] =  (y[i] - ex.iloc[i,1])/ex.iloc[i,1]*100
    # diff[i] =  (y[i] - ex.iloc[i,1])/y[i]*100

diff_ave = sum(diff)/n
print('average diff:',diff_ave)
