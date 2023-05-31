# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:23:52 2023

@author: ajay0
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime as dtm
from matplotlib.pyplot import subplots, close, show, rcParams

font_fam = 'Times New Roman'
rcParams['font.sans-serif'] = font_fam
rcParams['mathtext.fontset'] = 'custom'
rcParams['mathtext.rm'] = font_fam
rcParams['mathtext.it'] = f'{font_fam}:italic'
rcParams['mathtext.bf'] = f'{font_fam}:bold'


df1 = pd.read_csv(r"C:\Users\ajay0\Desktop\碩論參考文獻\會議新思維\忠明總數據.csv",parse_dates=['time']).set_index('time')
df2 = pd.read_csv(r"C:\Users\ajay0\Desktop\碩論參考文獻\會議新思維\東海總數據.csv",parse_dates=['time']).set_index('time')

start = dtm(2017,1,1)
end = dtm(2022,12,31,23)

# TIME = df['time']
# first = df['O3']

df_monthly1 = df1.resample('M').mean()
df_monthly2 = df2.resample('M').mean()

TIME = df_monthly1.index
first = df_monthly1['Ox']
second = df_monthly2['Ox']

fig, ax = plt.subplots(figsize=(12,4),dpi=300)

ax.plot(TIME,first,color='red',label='ZM')
ax.plot(TIME,second,color='#0000FF',label='TH')

ax.set_ylabel(r'$\bf O_{x}$ (ppb)', fontsize=20, fontweight='bold')


ax.set_xticks((pd.date_range(start, end, freq='6MS')))
ax.set_xticklabels(pd.date_range(start, end, freq='6MS').strftime('%Y-%m'), fontsize=12,  fontweight='bold')
ax.tick_params(axis='both', pad=10)

ax.set_yticks([20, 40, 60, 80])
ax.set_yticklabels([20, 40, 60, 80],fontsize=12)

ax.set_xlim(start, end)
ax.set_ylim(20, 80)

ax.legend()
# 添加趋势线
x = np.arange(len(TIME))
y1 = first.values
coefficients1 = np.polyfit(x, y1, 1)
trendline1 = np.polyval(coefficients1, x)
ax.plot(TIME, trendline1, color='#FF8888', label='ZM')

# y2 = second.values
# coefficients2 = np.polyfit(x, y2, 1)
# trendline2 = np.polyval(coefficients2, x)
# ax.plot(TIME, trendline2, color='#5555FF', label='TH')