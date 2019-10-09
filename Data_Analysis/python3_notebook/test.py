#!/home/leung/anaconda3/bin/python
# -*- encoding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
import sys

#%%
# 标题、标签设置中文
from matplotlib import pyplot as plt
import matplotlib
import random
x = range(0,120)
y = [random.randint(10,30) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y)

from matplotlib import font_manager
# 加载系统字体
'查看Linux、Mac下⽀持的字体'
# 终端执⾏： fc-list
# 查看⽀持的中⽂（冒号前面有空格) fc-list :lang=zh
'查看Windows下的字体：“C:\Windows\Fonts” '
# 可以⾃⼰下载字体⽂件（xxx.ttf），然后双击安装即可
# my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=18)
# my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\SIMYOU.TTF',size=18)
my_font = font_manager.FontProperties(fname='/usr/share/fonts/wps-office/Fonts/微软雅黑/msyh.ttc',size=18)

# my_font1 = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=20)
# 设置图片标题
plt.title('每分钟跳动次数',color='orange',fontproperties=my_font)

# X轴的标题
plt.xlabel('时间',fontproperties=my_font,rotation=45)
# Y轴的标题
plt.ylabel('次数',fontproperties=my_font)
plt.show()

#%%
