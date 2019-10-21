#!/usr/bin/python
# _*_ coding: UTF-8 _*_

"""
@project = spider_dot
@file = 爬虫下载.py
@author = Administrator
@create_time = 2019/10/18 10:31
software: PyCharm
"""
import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/200/300")
cat_img = response.read()

with open("cat_200_300.jpg",'wb') as f:
    f.write(cat_img)
