# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:05:43 2023

@author: ajay0
"""

from pathlib import Path
import pandas as pd
from datetime import datetime as dtm

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots, close, show, rcParams

import matplotlib.dates as mdates


font_fam = 'Times New Roman'
rcParams['font.sans-serif'] = font_fam
rcParams['mathtext.fontset'] = 'custom'
rcParams['mathtext.rm'] = font_fam
rcParams['mathtext.it'] = f'{font_fam}:italic'
rcParams['mathtext.bf'] = f'{font_fam}:bold'

#讀檔
df = pd.read_csv(r'ethylene.csv')

df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)

df_mean = df.resample('MS').mean()
df_std = df.resample('MS').std()

time = df_mean.index

###繪圖
fig, ax = plt.subplots(figsize=(12,4),dpi=300)

ax.plot(time,df_mean['萬華'],color='#54478c',label=r'Wanhua',marker='.')
# ax.fill_between(time,df_mean['萬華'] - df_std['萬華'],df_mean['萬華'] + df_std['萬華'],alpha=0.2,color='#54478c')

ax.plot(time,df_mean['土城'],color='#2c699a',label=r'Tucheng',marker='.')
# ax.fill_between(time,df_mean['土城'] - df_std['土城'],df_mean['土城'] + df_std['土城'],alpha=0.2,color='#2c699a')

ax.plot(time,df_mean['平鎮'],color='#048ba8',label=r'Pingzhen',marker='.')
# ax.fill_between(time,df_mean['平鎮'] - df_std['平鎮'],df_mean['平鎮'] + df_std['萬華'],alpha=0.2,color='#048ba8')

ax.plot(time,df_mean['忠明'],color='#e01e37',label=r'Zhongming',marker='.')
# ax.fill_between(time,df_mean['平鎮'] - df_std['平鎮'],df_mean['平鎮'] + df_std['萬華'],alpha=0.2,color='#048ba8')

ax.plot(time,df_mean['大城'],color='#16db93',label=r'Dacheng',marker='.')
# ax.fill_between(time,df_mean['平鎮'] - df_std['平鎮'],df_mean['平鎮'] + df_std['萬華'],alpha=0.2,color='#048ba8')

ax.plot(time,df_mean['臺西'],color='#83e377',label=r'Taixi',marker='.')

ax.plot(time,df_mean['朴子'],color='#b9e769',label=r'Puzi',marker='.')

ax.plot(time,df_mean['臺南'],color='#efea5a',label=r'Tainan',marker='.')

ax.plot(time,df_mean['橋頭'],color='#f1c453',label=r'Qiaotou',marker='.')

ax.plot(time,df_mean['小港'],color='#f29e4c',label=r'Xiaogang',marker='.')

ax.plot(time,df_mean['潮州'],color='#ff6000',label=r'Chaozhou',marker='.')

ax.set_ylim(0,6)

ax.set_xticks(time)
ax.set_xticklabels(time.strftime('%Y-%m'))

plt.ylabel('Ethylene (ppb)',fontsize=14)
plt.yticks(fontsize=12)

ax.legend(ncol=6,frameon=False,fontsize=12)

#資料輸出
df_std.reset_index(inplace=True)
df_std.to_csv("標準差.csv", index=False)

df_mean.reset_index(inplace=True)
df_mean.to_csv("濃度.csv", index=False)