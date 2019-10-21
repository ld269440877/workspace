# -*- coding:utf-8 -*-
'''
抓图的基本流程就是： requests发送网页请求 --> 使用get获取response
--> 利用 正则表达式 对response进行文本筛选，抓取图片链接
---> 新建一个图片存放的文件夹 ---> 下载图片保存到文件夹
'''
import re
import requests

def dowmloadPic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  #根据图片在网页中的格式用正则表示匹配想要的图片
    print(pic_url[:5],len(pic_url))  #查看抓取的网页数据格式和长度
    waiting_input = input('暂停等待')
    i = 1
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue
        #保存抓取到的图片
        dir = './img/' + keyword + '_' + str(i) + '.jpg'  #设置图片路径和名称
        fp = open(dir, 'wb')   #图片写入
        fp.write(pic.content)
        fp.close() #完成后关闭写入
        i += 1   # 图片计数


if __name__ == '__main__':
    word = input("Input key word: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
    result = requests.get(url)
    dowmloadPic(result.text, word)
    
# 查看本地图片
from PIL import Image
im = Image.open('./img/和平精英_1.jpg')
im.show()
