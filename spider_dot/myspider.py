#!/usr/bin/python
# _*_ coding: UTF-8 _*_

"""
@project = spider_dot
@file = myspider.py
@author = Administrator
@create_time = 2019/10/18 10:02
software: PyCharm
"""
import requests
import re
# etree用于Xpath进行定位功能
from lxml import etree
# 贴吧网址以字符串格式赋值在变量url
url = "http://tieba.baidu.com/f?kw=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=50"
# 将获取到url网页源码保存在变量html
html = requests.get(url)
# 通过html的text的属性查看网页源代码
# print(html.text)
# 使用正则表达式实现翻页功能
for i in range(10):
    #re.sub()用于替换字符串中的匹配项
    new_url = re.sub("&pn=\d+","&pn=%d" % (i*50), url)

    # print(new_url)
    html = requests.get(new_url)

#%%
import re
# from re import sub
print(help(sub))

#%%
