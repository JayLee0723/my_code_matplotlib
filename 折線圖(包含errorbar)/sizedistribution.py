# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 21:24:11 2022

@author: User
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

##############春，smps

df = pd.read_csv(r"C:\Users\ajay0\Desktop\能見度期中進度改進QQ\期中正式csv\粒徑濃度折線圖SMPS春.csv")
print(df)

size = df['size']
clean_mean = df['clean_mean']
clean_std = df['clean_std']

event_mean = df['event_mean']
event_std = df['event_std']

plt.Figure(dpi=150,figsize=(10,10))

# Plot 改科學記號大小，俊發友情贊助
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20
plt.rcParams["mathtext.fontset"] = 'custom'

plt.plot(size,clean_mean,color='#006400',label='Clean')
plt.fill_between(size,clean_mean-clean_std,clean_mean+clean_std,alpha=0.2,color='#006400')

plt.plot(size,event_mean,color='#FF0000',label='Event')
plt.fill_between(size,event_mean-event_std,event_mean+event_std,alpha=0.2,color='#FF0000')

plt.legend(frameon=False,fontsize=16)

# plt.tick_params(axis='both',pad=10)
# plt.tick_params(which='minor', length = 6,pad=10)

plt.xscale('log')


plt.ylim(0,120000)

plt.xlim(10,1000)

plt.grid(which = 'minor')
plt.grid(which = 'major')

plt.title('SMPS 2022 Spring',fontsize=25,fontweight='bold',pad=10)
plt.xlabel('Diameter (nm)',fontsize=20,fontweight='bold')
plt.ylabel('TNC (dN/dlogdp)',fontsize=20,fontweight='bold')

yticks = [0,30000,60000,90000,120000]
plt.xticks(fontsize=16)
plt.yticks(yticks,fontsize=16)

plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0),useMathText=True)





##############春，aps

# df = pd.read_csv(r"C:\Users\ajay0\OneDrive\桌面\能見度期中進度改進QQ\期中正式csv\粒徑濃度折線圖APS春.csv")
# print(df)

# size = df['size']
# clean_mean = df['clean_mean']
# clean_std = df['clean_std']

# event_mean = df['event_mean']
# event_std = df['event_std']

# plt.Figure(dpi=150,figsize=(10,10))

# # Plot 改科學記號大小，俊發友情贊助
# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.size'] = 20
# plt.rcParams["mathtext.fontset"] = 'custom'

# plt.plot(size,clean_mean,color='#006400',label='Clean')
# plt.fill_between(size,clean_mean-clean_std,clean_mean+clean_std,alpha=0.2,color='#006400')

# plt.plot(size,event_mean,color='#FF0000',label='Event')
# plt.fill_between(size,event_mean-event_std,event_mean+event_std,alpha=0.2,color='#FF0000')

# plt.legend(frameon=False,fontsize=20)

# # plt.tick_params(axis='both',pad=10)
# # plt.tick_params(which='minor', length = 6,pad=10)

# plt.xscale('log')

# plt.ylim(0,500)
# plt.xlim(500,20000)

# plt.title('APS 2022 Spring',fontsize=25,fontweight='bold',pad=10)
# plt.xlabel('Diameter (nm)',fontsize=20,fontweight='bold')
# plt.ylabel('TNC (dN/dlogdp)',fontsize=20,fontweight='bold')

# plt.grid(which='major')
# plt.grid(which='minor')
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)

# # plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))

###############夏，smps

# df = pd.read_csv(r"C:\Users\ajay0\OneDrive\桌面\能見度期中進度改進QQ\期中正式csv\粒徑濃度折線圖SMPS夏.csv")
# print(df)

# size = df['size']
# clean_mean = df['clean_mean']
# clean_std = df['clean_std']

# event_mean = df['event_mean']
# event_std = df['event_std']

# plt.Figure(dpi=150,figsize=(10,10))

# # Plot 改科學記號大小，俊發友情贊助
# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.size'] = 20
# plt.rcParams["mathtext.fontset"] = 'custom'

# plt.plot(size,clean_mean,color='#006400',label='Clean')
# plt.fill_between(size,clean_mean-clean_std,clean_mean+clean_std,alpha=0.2,color='#006400')

# plt.plot(size,event_mean,color='#FF0000',label='Event')
# plt.fill_between(size,event_mean-event_std,event_mean+event_std,alpha=0.2,color='#FF0000')

# plt.legend(frameon=False,fontsize=16)

# # plt.tick_params(axis='both',pad=10)
# # plt.tick_params(which='minor', length = 6,pad=10)

# plt.xscale('log')

# plt.ylim(0,120000)
# plt.xlim(10,1000)


# plt.title('SMPS 2022 Summer',fontsize=25,fontweight='bold',pad=10)
# plt.xlabel('Diameter (nm)',fontsize=20,fontweight='bold')
# plt.ylabel('TNC (dN/dlogdp)',fontsize=20,fontweight='bold')

# yticks = [0,30000,60000,90000,120000]
# plt.xticks(fontsize=16)
# plt.yticks(yticks,fontsize=16)

# plt.grid(which='major')
# plt.grid(which='minor')
# plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0),useMathText=True)



##################aps，夏

# df = pd.read_csv(r"C:\Users\ajay0\OneDrive\桌面\能見度期中進度改進QQ\期中正式csv\粒徑濃度折線圖APS夏.csv")
# print(df)

# size = df['size']
# clean_mean = df['clean_mean']
# clean_std = df['clean_std']

# event_mean = df['event_mean']
# event_std = df['event_std']



# plt.Figure(dpi=150,figsize=(10,10))

# # Plot 改科學記號大小，俊發友情贊助
# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.size'] = 20
# plt.rcParams["mathtext.fontset"] = 'custom'



# plt.plot(size,clean_mean,color='#006400',label='Clean')
# plt.fill_between(size,clean_mean-clean_std,clean_mean+clean_std,alpha=0.2,color='#006400')

# plt.plot(size,event_mean,color='#FF0000',label='Event')
# plt.fill_between(size,event_mean-event_std,event_mean+event_std,alpha=0.2,color='#FF0000')

# plt.legend(frameon=False,fontsize=20)

# # plt.tick_params(axis='both',pad=10)
# # plt.tick_params(which='minor', length = 6,pad=10)

# plt.xscale('log')

# plt.ylim(0,500)
# plt.xlim(500,20000)

# plt.grid(which='major')
# plt.grid(which='minor')

# plt.title('APS 2022 Summer',fontsize=25,fontweight='bold',pad=10)
# plt.xlabel('Diameter (nm)',fontsize=20,fontweight='bold')
# plt.ylabel('TNC (dN/dlogdp)',fontsize=20,fontweight='bold')
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)

# # plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))