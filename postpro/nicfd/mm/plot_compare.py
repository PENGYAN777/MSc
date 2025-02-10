#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025 Feb 04

@author: yan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

D = 6.5
z = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4,   ]


x = [9.15/D, 9.06/D, 8.98/D,  8.90/D, 8.89/D, 8.87/D, ]

r = [1.02/D,1.28/D,  1.54/D,  1.73/D, 1.99/D, 2.30/D,  ]





fig1 = plt.figure( dpi=300)
lwh = 2
ax1 = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
ax1.plot(z, x, 'ko', lw=lwh, label="X/D")
ax1.plot(z, x, 'k', lw=lwh)


ax1.set_xlabel('$Z_t$',fontsize=12)
ax1.set_ylabel('$X/D$',fontsize=12) 
ax1.legend(loc=6 , prop={'size': 10}) #
plt.xticks(z)
# ax1.set_ylim(1,2)

ax2 = ax1.twinx()
ax2.plot(z, r, 'bo', lw=lwh, label="r/D")
ax2.plot(z, r, 'b', lw=lwh)

ax2.set_ylabel('$r/D$',fontsize=12) 
ax2.legend(loc=5 , prop={'size': 10}) #
 
# axes.set_xlim(0,0.12)

#axes.legend(loc=2) # 2 means left top
fig1.savefig("nicfd_mm.pdf")