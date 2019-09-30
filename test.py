# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2019/09/16 14:13:07
@Author  :   Leung
@Version :   3.6.x
@Contact :   aa269440877@outlook.com
@WebSite :   https://github.com/ld269440877/
'''

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import io
import sys
# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# here put the import lib
fname="/usr/share/fonts/truetype/arphic/uming.ttc"
my_font = plt.font_manager.FontProperties(fname=fname,size=18)
plt.plot([0, 3, -1, -10, 10], [0, 1, 2, 3, 4])
plt.title('您好', fontProperties=my_font)

plt.show()

import os 
print(os.getcwd())