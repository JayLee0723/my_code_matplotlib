# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 20:31:40 2023

@author: ajay0
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime as dtm
from matplotlib.pyplot import rcParams
from matplotlib.pyplot import rcParams


font_fam = 'Times New Roman'
rcParams['font.sans-serif'] = font_fam
rcParams['mathtext.fontset'] = 'custom'
rcParams['mathtext.rm'] = font_fam
rcParams['mathtext.it'] = f'{font_fam}:italic'
rcParams['mathtext.bf'] = f'{font_fam}:bold'

##############室內

# df = pd.read_csv(r"C:\Users\ajay0\Desktop\校正維護1230\csv\室內濃度五筆平均.csv")
# print(df)

# size = df['size']
# mean_tp = df['conc_tp']
# error_tp = df['error_tp']

# mean_zm = df['conc_zm']
# error_zm = df['error_zm']

# plt.Figure(dpi=150,figsize=(10,10))

# # Plot 改科學記號大小，俊發友情贊助
# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.size'] = 15
# plt.rcParams["mathtext.fontset"] = 'custom'

# plt.plot(size,mean_tp,color='#006400',label='Taipei')
# plt.fill_between(size,mean_tp-error_zm,mean_tp+error_zm,alpha=0.2,color='#006400')

# plt.plot(size,mean_zm,color='#FF0000',label='Zhongming')
# plt.fill_between(size,mean_zm-error_zm,mean_zm+error_zm,alpha=0.2,color='#FF0000')

# plt.legend(frameon=False,fontsize=16)

# # plt.tick_params(axis='both',pad=10)
# # plt.tick_params(which='minor', length = 6,pad=10)

# plt.xscale('log')


# plt.ylim(0,4000)

# plt.xlim(10,1000)

# plt.grid(which = 'minor')
# plt.grid(which = 'major')

# plt.title('',fontsize=25,fontweight='bold',pad=10)
# plt.xlabel('Diameter (nm)',fontsize=20,fontweight='bold')
# plt.ylabel('TNC (dN/dlogdp)',fontsize=20,fontweight='bold')

# yticks = [0,1000,2000,3000,4000]
# plt.xticks(fontsize=16)
# plt.yticks(yticks,fontsize=16)

# plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0),useMathText=True)

#####################SAMPLE1


# df = pd.read_csv(r"C:\Users\ajay0\Desktop\校正維護1230\csv\產生源1.csv")
# print(df)

# size = df['size']
# mean_tp = df['conc_tp']
# error_tp = df['error_tp']

# mean_zm = df['conc_zm']
# error_zm = df['error_zm']

# plt.Figure(dpi=150,figsize=(10,10))

# # Plot 改科學記號大小，俊發友情贊助
# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.size'] = 15
# plt.rcParams["mathtext.fontset"] = 'custom'

# plt.plot(size,mean_tp,color='#006400',label='Taipei')
# plt.fill_between(size,mean_tp-error_zm,mean_tp+error_zm,alpha=0.2,color='#006400')

# plt.plot(size,mean_zm,color='#FF0000',label='Zhongming')
# plt.fill_between(size,mean_zm-error_zm,mean_zm+error_zm,alpha=0.2,color='#FF0000')

# plt.legend(frameon=False,fontsize=16)

# # plt.tick_params(axis='both',pad=10)
# # plt.tick_params(which='minor', length = 6,pad=10)

# plt.xscale('log')


# plt.ylim(0,500000)

# plt.xlim(10,1000)

# plt.grid(which = 'minor')
# plt.grid(which = 'major')

# plt.title('',fontsize=25,fontweight='bold',pad=10)
# plt.xlabel('Diameter (nm)',fontsize=20,fontweight='bold')
# plt.ylabel('TNC (dN/dlogdp)',fontsize=20,fontweight='bold')

# yticks = [0,10000000,20000000,30000000,40000000,50000000]
# plt.xticks(fontsize=16)
# plt.yticks(yticks,fontsize=16)

# plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0),useMathText=True)

#####################SAMPLE2


# df = pd.read_csv(r"C:\Users\ajay0\Desktop\校正維護1230\csv\產生源2.csv")
# print(df)

# size = df['size']
# mean_tp = df['conc_tp']
# error_tp = df['error_tp']

# mean_zm = df['conc_zm']
# error_zm = df['error_zm']

# plt.Figure(dpi=150,figsize=(10,10))

# # Plot 改科學記號大小，俊發友情贊助
# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.size'] = 15
# plt.rcParams["mathtext.fontset"] = 'custom'

# plt.plot(size,mean_tp,color='#006400',label='Taipei')
# plt.fill_between(size,mean_tp-error_zm,mean_tp+error_zm,alpha=0.2,color='#006400')

# plt.plot(size,mean_zm,color='#FF0000',label='Zhongming')
# plt.fill_between(size,mean_zm-error_zm,mean_zm+error_zm,alpha=0.2,color='#FF0000')

# plt.legend(frameon=False,fontsize=16)

# # plt.tick_params(axis='both',pad=10)
# # plt.tick_params(which='minor', length = 6,pad=10)

# plt.xscale('log')


# plt.ylim(0,500000)

# plt.xlim(10,1000)

# plt.grid(which = 'minor')
# plt.grid(which = 'major')

# plt.title('',fontsize=25,fontweight='bold',pad=10)
# plt.xlabel('Diameter (nm)',fontsize=20,fontweight='bold')
# plt.ylabel('TNC (dN/dlogdp)',fontsize=20,fontweight='bold')

# yticks = [0,10000000,20000000,30000000,40000000,50000000]
# plt.xticks(fontsize=16)
# plt.yticks(yticks,fontsize=16)

# plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0),useMathText=True)

#####################鞘流


df = pd.read_csv(r"C:\Users\ajay0\Desktop\校正維護1230\csv\鞘流正常.csv")
print(df)

size = df['size']
mean_tp = df['conc_tp']
error_tp = df['error_tp']

mean_zm = df['conc_zm']
error_zm = df['error_zm']

plt.Figure(dpi=150,figsize=(10,10))

# Plot 改科學記號大小，俊發友情贊助
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 15
plt.rcParams["mathtext.fontset"] = 'custom'

plt.plot(size,mean_tp,color='#006400',label='Taipei')
plt.fill_between(size,mean_tp-error_zm,mean_tp+error_zm,alpha=0.2,color='#006400')

plt.plot(size,mean_zm,color='#FF0000',label='Zhongming')
plt.fill_between(size,mean_zm-error_zm,mean_zm+error_zm,alpha=0.2,color='#FF0000')

plt.legend(frameon=False,fontsize=16)

# plt.tick_params(axis='both',pad=10)
# plt.tick_params(which='minor', length = 6,pad=10)

plt.xscale('log')


plt.ylim(0,500000)

plt.xlim(10,1000)

plt.grid(which = 'minor')
plt.grid(which = 'major')

plt.title('',fontsize=25,fontweight='bold',pad=10)
plt.xlabel('Diameter (nm)',fontsize=20,fontweight='bold')
plt.ylabel('TNC (dN/dlogdp)',fontsize=20,fontweight='bold')

yticks = [0,10000000,20000000,30000000,40000000,50000000]
plt.xticks(fontsize=16)
plt.yticks(yticks,fontsize=16)

plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0),useMathText=True)