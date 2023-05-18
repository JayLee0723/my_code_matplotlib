# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 13:48:48 2022

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

##############春，smps

# df = pd.read_csv(r"C:\Users\ajay0\OneDrive\桌面\能見度其中進度改進_版本二\csv檔案\粒徑濃度折線圖SMPS春(含ERL).csv")
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

# ln1, = plt.plot(size,clean_mean,color='#006400',label='Clean')
# plt.fill_between(size,clean_mean-clean_std,clean_mean+clean_std,alpha=0.2,color='#006400')

# ln2, = plt.plot(size,event_mean,color='#FF0000',label='Event')
# plt.fill_between(size,event_mean-event_std,event_mean+event_std,alpha=0.2,color='#FF0000')



# # plt.tick_params(axis='both',pad=10)
# # plt.tick_params(which='minor', length = 6,pad=10)

# plt.xscale('log')


# plt.ylim(0,120000)

# plt.xlim(10,1000)


# plt.title('SMPS 2022 Spring',fontsize=25,fontweight='bold',pad=10)
# plt.xlabel('Electrical Mobility Diameter (nm)',fontsize=20,fontweight='bold')
# plt.ylabel('TNC (dN/dlogdp)',fontsize=20,fontweight='bold')

# yticks = [0,30000,60000,90000,120000]
# plt.xticks(fontsize=16)
# plt.yticks(yticks,fontsize=16)

# plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0),useMathText=True)

# #######嘗試看看竟然成功了!plt像是叫出最後一步的ax
# ax = plt.gca()
# ax3 = ax.twinx()

# ERL = df['Enhancement_rate']
# ln_t, = ax3.plot(size,ERL,ls='--',color='black',label = 'ERL')
# ax3.set_ylabel('Enhencement ratio',fontsize=20,fontweight='bold',rotation=270,labelpad = 20)
# ax3.set_ylim(0,30)

# plt.legend(handles=[ln1,ln2,ln_t],frameon=False,fontsize=16,loc='upper left')


##############春，aps

df = pd.read_csv(r"C:\Users\ajay0\OneDrive\桌面\能見度其中進度改進_版本二\csv檔案\粒徑濃度折線圖APS春(含ERL).csv")
print(df)

import pickle as pkl
with open(r"C:\Users\ajay0\OneDrive\桌面\能見度其中進度改進_版本二\aps_202204-06.pkl",'rb') as f:
	aps = pkl.load(f)['number_norm']
	
with open(r"C:\Users\ajay0\OneDrive\桌面\能見度其中進度改進_版本二\ext_spring_2022.pkl",'rb') as f:
	cla = pkl.load(f)
	
# df = pd.read_csv(r"C:\Users\ajay0\OneDrive\桌面\能見度其中進度改進_版本二\csv檔案\粒徑濃度折線圖APS春(含ERL).csv")

clean_mean = aps.loc[cla['clean']].mean()
clean_std = aps.loc[cla['clean']].std()
event_mean = aps.loc[cla['event']].mean()
event_std = aps.loc[cla['event']].std()
size = aps.keys()*1e3

# size = df['size']
# clean_mean = df['clean_mean']
# clean_std = df['clean_std']

# event_mean = df['event_mean']
# event_std = df['event_std']



plt.Figure(dpi=150,figsize=(10,10))

# Plot 改科學記號大小，俊發友情贊助
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20
plt.rcParams["mathtext.fontset"] = 'custom'



plt.plot(size,clean_mean,color='#006400',label='Clean')
plt.fill_between(size,clean_mean-clean_std,clean_mean+clean_std,alpha=0.2,color='#006400')

plt.plot(size,event_mean,color='#FF0000',label='Event')
plt.fill_between(size,event_mean-event_std,event_mean+event_std,alpha=0.2,color='#FF0000')


# plt.tick_params(axis='both',pad=10)
# plt.tick_params(which='minor', length = 6,pad=10)

plt.xscale('log')

plt.ylim(0,500)
plt.xlim(500,20000)

plt.grid(which = 'minor')
plt.grid(which = 'major')
plt.legend(frameon=False,fontsize=20)
plt.title('APS 2022 Spring',fontsize=25,fontweight='bold',pad=10)
plt.xlabel(r'Aerodynamic Diameter ($\bf \mu m$)',fontsize=20,fontweight='bold')
plt.ylabel('TNC (dN/dlogdp)',fontsize=20,fontweight='bold')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

# plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))

# ax = plt.gca()
# ax3 = ax.twinx()

# ERL = df['Enhancement_rate']
# ln_t, = ax3.plot(size,ERL,ls='--',color='black',label = 'ERL')
# ax3.set_ylabel('Enhencement ratio',fontsize=20,fontweight='bold',rotation=270,labelpad = 20)
# ax3.set_ylim(0,25)

# plt.legend(handles=[ln1,ln2,ln_t],frameon=False,fontsize=16,loc='upper right')


###############夏，smps

# df = pd.read_csv(r"C:\Users\ajay0\OneDrive\桌面\能見度其中進度改進_版本二\csv檔案\粒徑濃度折線圖SMPS夏(含ERL).csv")
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

# ln1, =  plt.plot(size,clean_mean,color='#006400',label='Clean')
# plt.fill_between(size,clean_mean-clean_std,clean_mean+clean_std,alpha=0.2,color='#006400')

# ln2, = plt.plot(size,event_mean,color='#FF0000',label='Event')
# plt.fill_between(size,event_mean-event_std,event_mean+event_std,alpha=0.2,color='#FF0000')

# # plt.legend(frameon=False,fontsize=16)

# # plt.tick_params(axis='both',pad=10)
# # plt.tick_params(which='minor', length = 6,pad=10)

# plt.xscale('log')

# plt.ylim(0,90000)
# plt.xlim(10,1000)


# plt.title('SMPS 2022 Summer',fontsize=25,fontweight='bold',pad=10)
# plt.xlabel('Electrical Mobility Diameter (nm)',fontsize=20,fontweight='bold')
# plt.ylabel('TNC (dN/dlogdp)',fontsize=20,fontweight='bold')

# yticks = [0,30000,60000,90000]
# plt.xticks(fontsize=16)
# plt.yticks(yticks,fontsize=16)


# plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0),useMathText=True)

# #######嘗試看看竟然成功了!plt像是叫出最後一步的ax
# # ax = plt.gca()
# # ax3 = ax.twinx()

# # ERL = df['Enhancement_rate']
# # ln_t, = ax3.plot(size,ERL,ls='--',color='black',label = 'ERL')
# # ax3.set_ylabel('Enhencement ratio',fontsize=20,fontweight='bold',rotation=270,labelpad = 20)
# # ax3.set_ylim(0,30)

# # plt.legend(handles=[ln1,ln2,ln_t],frameon=False,fontsize=16,loc='upper center')

##################aps，夏

# df = pd.read_csv(r"C:\Users\ajay0\OneDrive\桌面\能見度其中進度改進_版本二\csv檔案\粒徑濃度折線圖APS夏(含ERL).csv")
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



# ln1, = plt.plot(size,clean_mean,color='#006400',label='Clean')
# plt.fill_between(size,clean_mean-clean_std,clean_mean+clean_std,alpha=0.2,color='#006400')

# ln2, = plt.plot(size,event_mean,color='#FF0000',label='Event')
# plt.fill_between(size,event_mean-event_std,event_mean+event_std,alpha=0.2,color='#FF0000')



# # plt.tick_params(axis='both',pad=10)
# # plt.tick_params(which='minor', length = 6,pad=10)

# plt.xscale('log')

# plt.ylim(0,500)
# plt.xlim(500,20000)


# plt.title('APS 2022 Summer',fontsize=25,fontweight='bold',pad=10)
# plt.xlabel(r'Aerodynamic Diameter ($\bf \mu m$)',fontsize=20,fontweight='bold')
# plt.ylabel('TNC (dN/dlogdp)',fontsize=20,fontweight='bold')
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)

# # plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))

# # ax = plt.gca()
# # ax3 = ax.twinx()

# # ERL = df['Enhancement_rate']
# # ln_t, = ax3.plot(size,ERL,ls='--',color='black',label = 'ERL')
# # ax3.set_ylabel('Enhencement ratio',fontsize=20,fontweight='bold',rotation=270,labelpad = 20)
# # ax3.set_ylim(0,25)

# # plt.legend(handles=[ln1,ln2,ln_t],frameon=False,fontsize=16,loc='upper right')