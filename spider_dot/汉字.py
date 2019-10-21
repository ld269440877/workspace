#!/usr/bin/python
# _*_ coding: UTF-8 _*_

"""
@project = spider_dot
@file = 汉字.py
@author = Administrator
@create_time = 2019/10/19 15:27
software: PyCharm
"""
#%%
# http请求库
import requests
# 正则匹配的库
import re
# 抓取到网页的源代码 post
html_result = requests.get('https://www.zdic.net/zd/zb/cc1/')
# print(html_result.text)
# 书写正则表达式来获取到网页源代码中的所有汉字
reg = "href='/hans/(.*)' "
print(re.findall(reg,html_result.text)[:5])
# hans_list 当中就是包含了我们想要的2500个常用汉字
hans_list = re.findall(reg, html_result.text)
# 输入汉字
input_message = '我爱中国共产党'
# 输出input_message中每一个汉字和它在hans_list中的索引
for hans in input_message:
    for index, element in enumerate(hans_list):
        if hans == element:
            print(index,element)
# 格式化输出hans_list中的2500个汉字，每行10个汉字
'''
方法一
''' 
i = 0
for hans in hans_list[:20]:
    print(hans, end='\t')
    i +=1
    if i %10 ==0:
        print()
print('#'*20)
'''‘
方法二
'''
for index , element in enumerate(hans_list[:20]):
    print(element, end='\t')
    if (index+1)%10 == 0:
        print()

#%%
