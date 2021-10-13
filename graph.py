# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import Line
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] =False


data = pd.read_csv('./十元赌本进行无限轮游戏.csv',engine='python')
data_s = data.groupby('round').count()['person'].cumsum()

data_s.plot(kind='line',
       label = 'round',
       style = '-',
       color = 'black',
       alpha = 0.4,
       use_index = True,
       rot = 45,
       grid = True,
       xlim = [0,3500],
       figsize = (12,6),
       title = 'Game Over Round',
       linewidth=7,
       legend = True)
plt.axvline(data_s.mean(),color='red')
plt.text(100,20,'平均第{}轮破产'.format(int(data_s.mean())),color='blue')
plt.text(450,55,'在第256轮破产比例达到50％',color='blue')
plt.axhline(50,color='red')
plt.legend()
plt.savefig('./graph1.png',dpi=400)
plt.show()