#!/usr/bin/python
# _*_ coding: UTF-8 _*_

"""
@project = spider_dot
@file = 爬虫_单词翻译.py
@author = Administrator
@create_time = 2019/10/18 10:36
software: PyCharm

"""
import requests
from bs4 import BeautifulSoup

# 输入单词
word = input("Enter a word(enter 'q'to exit):")
# main body
while word != 'q': # 'q'to exit
    # 利用requests.get获取输入单词的网页信息
    r = requests.get(url = 'http://dict.youdao.com/w/%25s/#keyfrom=dict2.top'%word)
    # 利用BeautifulSoup将获取到的文本解析成HTML
    soup = BeautifulSoup(r.text, "lxml")
    # 获取字典的标签内容
    s = soup.find(class_="trans-container")('ul')[0]('li')
    # 输出字典的具体内容
    print(s)
    for item in s:
        if item.text:
            print(item.text)
    print('='*40+'\n')
#TODO
    word = input("Enter a word(enter 'q' to exit):")

