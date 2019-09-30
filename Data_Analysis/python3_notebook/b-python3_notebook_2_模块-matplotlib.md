```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  id='utf-8' continue:true output='markdown' } ##hide  代码隐藏 
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
```

# 模块

模块
:   通俗理理解⼀个.py⽂文件就是⼀一个模块，模块是管理理功能代码的。

内置模块
:   就是python⾃自⼰己内部⾃自带的不不需要我们去下载的模块， ⽐比如：time, random等。
>  模块是一个.py文件
> 包是一个装有多个.py文件的文件夹

## 自定义模块的使⽤
- 注意：⾃定义模块名字和变量量名的定义很类似，都是由字⺟母、数字、下划线组成，但是不不能以数字开头，否则⽆无法导⼊入该模块。


```
# 模块 .py文件
import random
import time

# import requests
# pip install requests
help('modules')# 查看所安装的模块
```

```
# 自定义需要两步： 修改成 .py文件， first_module.py文件与当前导入的文件放在同一个目录下
import first_module 

# 使用模块中的是方法
# print(first_module.g_num)
# first_module.show()
print(__name__)# __main__
```






### 创建名为first_module的⾃自定义模块
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

__all__ = ["g_num", "show"]
# 指定__all__表示 from 模块名 import * 只能使⽤用指定的功能代码，⽽而不不是所有的功能代码
# 定义全局变量量
g_num = 10
# 定义函数
def show():
    print("我是⼀一个函数")
    # 定义类
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_msg(self):
        print(self.name, self.age)
# 解决导⼊入的模块中⽅方法没有调⽤用就会执行
if __name__ == '__main__':
    show()

'''
注意：使⽤用 __name__ 查看模块名，执⾏行行哪个⽂文件，哪个⽂文件中的__name__ 输出 __main__ , 其他导
⼊入模块中的__name__ 结果就是模块名字。
'''

```

### 使⽤用⾃自定义的模块
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 导⼊入模块
import first_module
# 使⽤用模块中的功能代码
print(first_module.g_num)
first_module.show()
stu = first_module.Student("李李四", 20)
stu.show_msg()

```

模块导⼊入的注意点：
1. ⾃自定义的模块名不不要和系统的模块名重名，
2. 导⼊入的功能代码不不要在当前模块定义否则使⽤用不不了了导⼊入模块的功能代码

### 包的介绍
包
:   通俗理理解包就是⼀一个⽂文件夹，只不不过⽂文件夹⾥里里⾯面有⼀一个init.py⽂文件
包是管理理模块的， 模块是管理理功能代码的。

 包-模块-代码：
![包-模块-代码](包-模块-代码.png)


```
# 模块的导入
# 1. import 直接导入
import first_module 
first_module.show()

# 给模块起别名
import first_module as first
first.show()


# 2.从first_module这个模块中导入名字叫做show的方法
from first_module import show 

# 给模块中的方法起别名（避免多个模块中有一样的名字）
from second_module import show as second_show
# show()

# 导入一个模块的多个方法
from first_module import show,Student

# 导入一个模块的多个方法
from first_module import *
```


```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# -----import导⼊入包⾥里里⾯面的模块----
import first_package.first
#-----import导⼊入包⾥里里⾯面的模块设置别名----
import first_package.first as one
#----from导⼊入包名 import 模块名----
from first_package import second
#--- from 包名.模块名 import 功能代码----
from first_package.first import show # 需要保证当前模块没有导⼊入模块的功能代码
# --- from 包名 import *, 默认不不会导⼊入包⾥里里⾯面的所有模块，需要在init⽂文件⾥里里⾯面使⽤用__all__
'''
__all__ = ["g_num", "show"]
 '''
去指定导⼊入的模块
from first_package import *
```
### \_\_init\_\_ ⽂件写法
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 如果外界使⽤用from 包名 import * 不不会导⼊入包⾥里里⾯面的所有模块，需要使⽤用__all__指定
__all__ = ["first", "second"]
# 从当前包导⼊入对应的模块
from . import first
from . import second

```

# ⽂件基础操作
## ⽂件简介
⽂件包括 ⽂本文件和⼆进制文件（声⾳音，图像，视频) 从存储⽅方式来说，⽂件在磁盘上的存储方式都是二进制形式，所以，文本⽂件其实也应该算二进制文件。先从他们的区别来说，虽然都是二进制⽂件，但是二进制代表的意思不一样。打个比方，⼀个人，我们可以叫他的大名，以叫他的小名，但其实都是代表这个人。
二进制读写是将内存里面的数据直接读写⼊文本中，
⽽⽂本，则是将数据先转换成了字符串，再写⼊到文本中。
## 读⽂件
- 要以读⽂文件的模式打开⼀一个⽂文件对象，使⽤用Python内置的open() 函数，传⼊入⽂文件名和标示符：
```python
#  打开文件
f = open('/Users/michael/test.txt', 'r')
#  读取
f.read()
'Hello, world!'
#  关闭
f.close()


````
如果⽂文件不不存在， open() 函数就会抛出⼀一个IOError 的错误
由于⽂文件读写时都有可能产⽣生IOError ，一旦出错，后面的f.close() 就不会调⽤用。所以，为了了保证无论是否出错都能正确地关闭文件，我们可以使⽤用try ... finally 来实现：

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
         f.close()
```
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

with open('/path/to/file', 'r') as f:
    print(f.read())

```

## 文件的打开方式

```
# f=open(‘1.txt’)
# # 读取或者写入
# f.close()

'''
r : 只读，文件如果不存在就会报错
w : 只写，会将原来的数据清空，在写入，如果文件不存子在，会创建一个新的文件
a : 追加写入

rb: 以二进制形式读取文件
wb：以二进制形式写入文件
ab ：以二进制形式追加写入文件

r+:可读可写的操作，覆盖的形势写入  ABC DE DEC
'''
```
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# w模式 hello  GBK   utf-8 
# windows : GBK
# mac linux  : utf-8

file = open('1.txt','w',encoding='utf-8')
print(file.encoding)
# # 写入数据
file.write('a')
file.write('b')  #打开文件后，多次file.write()写入，是追加

file.close()

#  the content of 1.txt
# ab
```
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

file = open('1.txt','w',encoding='utf-8')
# print(file.encoding)
# # 写入数据
file.write('abc')
file.write('哈哈')
file.close()

```
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# r
file = open('1.txt','r',encoding='utf-8')

# 不能写入数据  --'r'模式
# file.write('abc')

# 读取数据
content = file.read()
print(content)

file.close()


```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# rb二进制形式读取数据
# 只要出现b,就不需要是encoding='utf-8'
file = open('1.txt','rb')

content = file.read()
print(content) # b'fafda'

# 将二进制数据进行utf-8解码操作
result = content.decode('utf-8')
print(result)

# 编码-->二进制
print(result.encode('utf-8'))

file.close()
# \xe5\x93\x88  哈

# b’abc\xe5\x93\x88\xe5\x93\x88’
# abc哈哈
# b’abc\xe5\x93\x88\xe5\x93\x88’
```
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 文件的不同读取方式
file = open('1.txt','r',encoding='utf-8')
# 英文只占一个字节，中文占三个字节
print(file.read(4))# 如果是r这种方式， 并不是以字节的个数为量值，是字符数
file.close()


```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

file = open('1.txt','rb')

print(file.read(4))# 如果是rb这种方式，是以字节的个数为量值

file.close()

```


|                     模式                      |                                                                                     描述                                                                                      |
| :-------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                       r                       |                                                      以只读⽅方式打开⽂文件。⽂文件的指针将会放在⽂文件的开头。这是默认模式                                                       |
|                      rb                       |                                                     以⼆二进制格式打开⼀一个⽂文件⽤用于只读。⽂文件指针将会放在⽂文件的开头。                                                      |
|                      r+                       |                                                            打开⼀一个⽂文件⽤用于读写。⽂文件指针将会放在⽂文件的开头。                                                            |
|                      rb+                      |                                                     以⼆二进制格式打开⼀一个⽂文件⽤用于读写。⽂文件指针将会放在⽂文件的开头。                                                      |
|                       w                       |                                             打开⼀一个⽂文件只⽤用于写⼊入。如果该⽂文件已存在则打开⽂文件，并从开头开始编辑，即原有内                                              |
| 容会被删除。如果该⽂文件不不存在，创建新⽂文件。 |
|                      wb                       |                以⼆二进制格式打开⼀一个⽂文件只⽤用于写⼊入。如果该⽂文件已存在则打开⽂文件，并从开头开始编辑，即原有内容会被删除。如果该⽂文件不不存在，创建新⽂文件。                 |
|                      w+                       |                        打开⼀一个⽂文件⽤用于读写。如果该⽂文件已存在则打开⽂文件，并从开头开始编辑，即原有内容会被删除。如果该⽂文件不不存在，创建新⽂文件。                         |
|                      wb+                      |                  以⼆二进制格式打开⼀一个⽂文件⽤用于读写。如果该⽂文件已存在则打开⽂文件，并从开头开始编辑，即原有内容会被删除。如果该⽂文件不不存在，创建新⽂文件。                  |
|                       a                       |       打开⼀一个⽂文件⽤用于追加。如果该⽂文件已存在，⽂文件指针将会放在⽂文件的结尾。也就是说，新的内容将会被写⼊入到已有内容之后。如果该⽂文件不不存在，创建新⽂件进⾏行行写⼊入。       |
|                      ab                       | 以⼆二进制格式打开⼀一个⽂文件⽤用于追加。如果该⽂文件已存在，⽂文件指针将会放在⽂文件的结尾。也就是说，新的内容将会被写⼊入到已有内容之后。如果该⽂文件不不存在，创建新⽂文件进行写⼊入。 |
|                      a+                       |                 打开⼀一个⽂文件⽤用于读写。如果该⽂文件已存在，⽂文件指针将会放在⽂文件的结尾。⽂文件打开时会是追加模式。如果该⽂文件不不存在，创建新⽂文件⽤用于读写。                 |
|                      ab+                      |                       以⼆二进制格式打开⼀一个⽂文件⽤用于追加。如果该⽂文件已存在，⽂文件指针将会放在⽂文件的结尾。如果该⽂文件不不存在，创建新⽂文件⽤用于读写。                       |

## 字符编码
要读取⾮非UTF-8编码的⽂文本⽂文件，需要给open() 函数传⼊入encoding 参数，例例如，读取GBK编码的⽂文件：
```
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'
```
遇到有些编码不不规范的⽂文件，你可能会遇到UnicodeDecodeError ，因为在⽂文本⽂文件中可能夹杂了了⼀一些⾮非法编码的字符。遇到这种情况， open() 函数还接收⼀一个errors 参数，表示如果遇到编码错误后如何处理理。最简单的⽅方式是直接忽略略：
```
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk',errors='ignore')
```
## 写⽂文件
写⽂文件和读⽂文件是⼀一样的，唯⼀一区别是调⽤用open() 函数时，传⼊入标识符'w' 或者'wb' 表示写⽂文本⽂文件或写⼆二进制⽂文件：

```
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
```

```
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
```
---
---
## Demonstration
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# <html>
#     <div></div>
#     <div></div>
#     <div></div>

# </html>
# http://www.baidu.com/img/bd_logo1.png?where=super

import requests
# pip install requests
url = 'http://www.baidu.com/img/bd_logo1.png?where=super'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
# 发送网络请求(get,post),模仿了浏览器的请求
response = requests.get(url=url,headers=headers)
# print(response.content)# 是以二进制的形势返回的内容，获取response中的内容使用content
# print(response.text) # 是以文本形势返回来的

# 保存内容
# file = open('./baidu.png','wb')
# file.write(response.content)
# file.close()

with open('./baidu.png','wb') as file:
    file.write(response.content)


```
```
# [statues：200，
#     code:{
#         'name':'zs'
#     }
# ]
# json

# 138  \d\d\d
# import re # python中的正则模块

# - BeautifulSoup
# - PyQuery
# 如果使用这两个模块，需要了解 css 选择器

//*[@id="s_lg_img_new"]
```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

from lxml import etree
import requests
base_url = 'https://www.mzitu.com/jiepai/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
response = requests.get(url=base_url,headers=headers)
# print(response.text)
# 使用Xpath进行解析数据
html = etree.HTML(response.text)
ul_list = html.xpath('//*[@id="comments"]/ul/li')
# print(ul_list)

num = 0
for li in ul_list:
    num += 1
    img_url = li.xpath('./div/p/img/@data-original')[0]
    print(img_url)
    
    # 发送请求下载图片
    img_response = requests.get(url=img_url,headers=headers)
    with open('./results/{}.jpg'.format(num),'wb') as f:
        f.write(img_response.content)
        
# C:   /User/mac/destop

```

# matplotlib
[Matplotlib: Python plotting — Matplotlib 3.1.1 documentation](https://matplotlib.org/)
什么是Matplotlib
:   Matplotlib是⼀一个Python 2D绘图库，它可以在各种平台上以各种硬拷⻉贝格式和交互式环境⽣生成出具有
出版品质的图形。
Matplotlib试图让简单的事情变得更更简单，让⽆无法实现的事情变得可能实现。 只需⼏代码即可⽣生成绘图，直⽅方图，功率谱，条形图，错误图，散点图等。

## 常⻅见图形种类及意义
折线图
:   以折线的上升或下降来表示统计数量量的增减变化的统计图

特点
:   能够显示数据的变化趋势，反映事物的变化情况。(变化)

## Matplotlib画图的简单实现

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 导⼊入模块
import matplotlib.pyplot as plt
# 在jupyter中执⾏行行的时候显示图⽚片
# %matplotlib inline
# 传⼊入x和y, 通过plot画图
plt.plot([1, 0, 9], [4, 5, 6])
# 在执⾏行行程序的时候展示图形
plt.show()


```
## 对Matplotlib图像结构的认识

![matplotlib图像结构的认识](matplotlib图像结构的认识.bmp "matplotlib图像结构的认识")
![matplotlib绘图](matplotlib绘图.bmp "matplotlib绘图")

## 折线图的绘制
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 导入
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt

x = range(1,8) # x轴的位置
y = [17, 17, 18, 15, 11, 11, 13]
# 传入x和y, 通过plot画折线图
plt.plot(x,y)
plt.show()
```
### 折线的颜⾊色和形状设置
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ####hide  代码隐藏

from matplotlib import pyplot as plt
x = range(1,8) ## x轴的位置
y = [17, 17, 18, 15, 11, 11, 13]
## 传⼊入x和y, 通过plot画折线图
plt.plot(x, y, color='red',alpha=0.5,linestyle='--',linewidth=3)
plt.show()
'''基础属性设置
color='red' : 折线的颜⾊色
alpha=0.5 : 折线的透明度(0-1)
linestyle='--' : 折线的样式
linewidth=3 : 折线的宽度
'''
'''线的样式
- 实线(solid)
-- 短线(dashed)
-. 短点相间线(dashdot)
： 虚点线(dotted)
'''


```
### 折点样式
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ####hide  代码隐藏

from matplotlib import pyplot as plt
x = range(1,8) ## x轴的位置
y = [17, 17, 18, 15, 11, 11, 13]
## 传⼊入x和y, 通过plot画折线图
plt.plot(x, y, marker='*')
plt.show()


```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 折线图
from matplotlib import pyplot as plt

# 1.x y x轴的位置
x = range(1,8) 
y = [17, 17, 18, 15, 11, 11, 13]


# 2. 传入x和y, 通过plot画折线图
plt.plot(x,y,color= 'red',alpha = 0.5,linestyle='--',linewidth=3,marker='o',
         markersize='20',markeredgecolor='green',markeredgewidth=5)
# alpha 透明度  0-1
# 3. 显示
plt.show()

```
### 设置的图⽚片的⼤小和保存

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

from matplotlib import pyplot as plt
import random
x = range(2,26,2) # x轴的位置
y = [random.randint(15, 30) for i in x]
# 设置图⽚片的⼤大⼩小
'''
figsize:指定figure的宽和⾼高，单位为英⼨寸；
dpi参数指定绘图对象的分辨率，即每英⼨寸多少个像素，缺省值为80 1英⼨寸等于2.5cm,A4纸是
21*30cm的纸张
'''
# 根据画布对象
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y) # 传⼊入x和y, 通过plot画图
plt.show()
# 保存(注意： 要放在绘制的下⾯面,并且plt.show()会释放figure资源，如果在显示图像之后保存图⽚片将只能保存空图⽚片。)
plt.savefig('./t1.png')
# 图⽚片的格式也可以保存为svg这种⽮矢量量图格式，这种⽮矢量量图放在⽹网⻚页中放⼤大后不不会有锯⻮齿
# plt.savefig('./t1.svg')
```

### 绘制x轴和y轴的刻度
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 绘制xy刻度
from matplotlib import pyplot as plt
import random
x = range(2,26,2) # x轴的位置
y = [random.randint(15, 30) for i in x]

plt.figure(figsize=(20,8),dpi=80)

# 设置x轴的刻度的疏密程度
# plt.xticks(x)
# plt.xticks(range(1,25))
# 设置y轴的刻度
# plt.yticks(y)
# plt.yticks(range(min(y),max(y)+1))

# 构造了x轴的刻度标签

x_ticks_label = ["{}:00".format(i) for i in x]
# plt.xticks(x刻度的列表,x_ticks_label标签的列表,rotation=45)
plt.xticks(x,x_ticks_label,rotation=45)

# 设置一下y轴
y_ticks_label = ["{}°C".format(i) for i in range(min(y),max(y)+1)]
plt.yticks(range(min(y),max(y)+1),y_ticks_label)


plt.plot(x,y)
plt.show()


```
### 设置显示中⽂
#### 标题、标签设置中文
- matplotlib只显示英⽂文,⽆无法显示中⽂文，需要修改matplotlib的默认字体
- 通过matplotlib下的font_manager可以解决
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

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
'查看Linux、Mac下⽀支持的字体'
# 终端执⾏行行： fc-list
# 查看⽀支持的中⽂文（冒号前⾯面有空格) fc-list :lang=zh
'查看Windows下的字体：“C:\Windows\Fonts” '
# 可以⾃自⼰己下载字体⽂文件（xxx.ttf），然后双击安装即可
# my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=18)
# my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\SIMYOU.TTF',size=18)
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=18)

# my_font1 = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=20)
# 设置图片标题
plt.title('每分钟跳动次数',color='orange',fontproperties=my_font)

# X轴的标题
plt.xlabel('时间',fontproperties=my_font,rotation=45)
# Y轴的标题
plt.ylabel('次数',fontproperties=my_font)
plt.show()


```
#### 图例设置中文
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏


from matplotlib import font_manager

y1 = [1,0,1,1,2,4,3,4,4,5,6,5,4,3,3,1,1,1,1,1]
y2 = [1,0,3,1,2,2,3,4,3,2,1,2,1,1,1,1,1,1,1,1]

x = range(11,31)
# 设置图形
plt.figure(figsize=(20,8),dpi=80)
# my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=18)
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=18)
# 设置x轴刻度
xtick_labels = ['{}岁'.format(i) for i in x]
plt.xticks(x,xtick_labels,fontproperties=my_font,rotation=45)


plt.plot(x,y1,color = 'red',label='自己')
plt.plot(x,y2,color = 'blue',label='朋友')

# 绘制网格
plt.grid(alpha=0.3)

# 绘制图例
# 设置位置loc : upper left、 lower left、 center left、 upper center
plt.legend(prop=my_font,loc='upper left')

plt.show()
# 设置x轴刻度
# xtick_labels = ['{}岁'.format(i) for i in x]
# my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=18)

# plt.xticks(x,xtick_labels,fontproperties=my_font,rotation=45)

# 绘制网格（网格也是可以设置线的样式)
#alpha=0.4 设置透明度
# plt.grid(alpha=0.4)

# 添加图例(注意：只有在这里需要添加prop参数是显示中文，其他的都用fontproperties)
# 设置位置loc : upper left、 lower left、 center left、 upper center
# plt.legend(prop=my_font,loc='upper right')

#展示
# plt.show()
```

###  ⼀一图多线


```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 假设⼤大家在30岁的时候，根据⾃自⼰己的实际情况，统计出来你和你同事各⾃自从11岁到30岁每年年交的男/⼥女女朋友的数量量如列列表y1和y2，请在⼀一个图中绘制出该数据的折线图，从⽽而分析每年年交朋友的数量量⾛走势。
from matplotlib import font_manager
y1 = [1,0,1,1,2,4,3,4,4,5,6,5,4,3,3,1,1,1,1,1]
y2 = [1,0,3,1,2,2,3,4,3,2,1,2,1,1,1,1,1,1,1,1]
x = range(11,31)
# 设置图形
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y1,color='red',label='⾃自⼰己')
plt.plot(x,y2,color='blue',label='同事')
# 设置x轴刻度
xtick_labels = ['{}岁'.format(i) for i in x]
my_font =font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=18)
plt.xticks(x,xtick_labels,fontproperties=my_font,rotation=45)
# 绘制⽹网格（⽹网格也是可以设置线的样式)
#alpha=0.4 设置透明度
plt.show()
```

### 拓拓展⼀一（⼀一图多个坐标系⼦子图）

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# add_subplot⽅方法----给figure新增⼦子图
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1, 100)
#新建figure对象
fig=plt.figure(figsize=(20,10),dpi=80)
#新建⼦子图1
ax1=fig.add_subplot(2,2,1)
ax1.plot(x, x)
#新建⼦子图2
ax2=fig.add_subplot(2,2,2)
ax2.plot(x, x ** 2)
ax2.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
#新建⼦子图3
ax3=fig.add_subplot(2,2,3)
ax3.plot(x, np.log(x))
plt.show()


```
### 拓拓展⼆二（设置坐标轴范围）

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏


import matplotlib.pyplot as plt
import numpy as np
x= np.arange(-10,11,1)
y = x**2
plt.plot(x,y)
# 可以调x轴的左右两边
# plt.xlim([-5,5])
# 只调⼀一边
# plt.xlim(xmin=-4)
# plt.xlim(xmax=4)
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.show()

```

### 拓拓展三（改变坐标轴的默认显示⽅方式）

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

import matplotlib.pyplot as plt
import numpy as np
y = range(0,14,2) # x轴的位置
x = [-3,-2,-1,0,1,2,3]
# plt.figure(figsize=(20,8),dpi=80)
# 获得当前图表的图像
ax = plt.gca()
# 设置图型的包围线
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('red')
# 设置底边的移动范围，移动到y轴的0位置,'data':移动轴的位置到交叉轴的指定坐标
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.plot(x,y)
plt.show()


```

## 绘制散点图

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

'''题⼲干
3⽉月份每天最⾼高⽓气温
a =
[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,2
2,22,22,23]
'''
from matplotlib import pyplot as plt
from matplotlib import font_manager

y = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
x = range(1,32)

# 设置图形⼤大⼩小
plt.figure(figsize=(20,8),dpi=80)
# 使⽤用scatter绘制散点图
plt.scatter(x,y,label= '3月份')
# plt.plot()
# 调整x轴的刻度
my_font =font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=10)
x_ticks_labels = ['3月{}日'.format(i) for i in x]
plt.xticks(x[::3],x_ticks_labels[::3],fontproperties=my_font,rotation=45)
plt.xlabel('⽇期',fontproperties=my_font)
plt.ylabel('温度',fontproperties=my_font)
# 图例
plt.legend(prop=my_font)
plt.show()

```

## 绘制条形图

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
'''http://58921.com/alltime
假设你获取到了了2019年年内地电影票房前20的电影（列列表a)和电影票房数据（列列表b)，请展示该数据
a = ['流浪地球','疯狂的外星⼈人','⻜飞驰⼈人⽣生','⼤大⻩黄蜂','熊出没·原始时代','新喜剧之王']
b = ['38.13','19.85','14.89','11.36','6.47','5.93']
'''

from matplotlib import pyplot as plt
from matplotlib import font_manager
a = ['流浪地球','疯狂的外星⼈人','⻜飞驰⼈人⽣生','⼤大⻩黄蜂','熊出没·原始时代','新喜剧之王']
b = ['38.13','19.85','14.89','11.36','6.47','5.93']
# b =[38.13,19.85,14.89,11.36,6.47,5.93]
my_font =font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=10)
plt.figure(figsize=(20,8),dpi=80)
# 绘制条形图
rects = plt.bar(range(len(a)),[float(i) for i in b],width=0.3,color=['r','g','b','r','g','b'])
plt.xticks(range(len(a)),a,fontproperties=my_font)
plt.yticks(range(0,41,5),range(0,41,5))
# 在条形图上加标注(⽔水平居中)
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+0.3,
    str(height),ha="center")

plt.show()

```
## 横向条形图


```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
'''http://58921.com/alltime
假设你获取到了了2019年年内地电影票房前20的电影（列列表a)和电影票房数据（列列表b)，请展示该数据
a = ['流浪地球','疯狂的外星⼈人','⻜飞驰⼈人⽣生','⼤大⻩黄蜂','熊出没·原始时代','新喜剧之王']
b = ['38.13','19.85','14.89','11.36','6.47','5.93']
'''
# 横向柱状图
from matplotlib import pyplot as plt
from matplotlib import font_manager
a = ['流浪地球','疯狂的外星⼈人','⻜飞驰⼈人⽣生','⼤大⻩黄蜂','熊出没·原始时代','新喜剧之王']
b = ['38.13','19.85','14.89','11.36','6.47','5.93']
# b =[38.13,19.85,14.89,11.36,6.47,5.93]
my_font =font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=10)
plt.figure(figsize=(20,8),dpi=80)
# 绘制条形图的⽅方法
'''
height=0.3 条形的宽度
'''
# 绘制横向的条形图
# plt.bar(y,x)
rects = plt.barh(range(len(a)),b,height=0.3,color='r')
plt.yticks(range(len(a)),a,fontproperties=my_font,rotation=45)
# 在条形图上加标注(竖直居中)
for rect in rects:
# print(rect.get_x())
    width = rect.get_width()
    plt.text(width+0.1, rect.get_y()+0.3/2, str(width),va="center")
plt.show()

```

## 并列列和罗列列条形图

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

import matplotlib.pyplot as plt
import numpy as np
index = np.arange(4)
BJ = [50,55,53,60]
Sh = [44,66,55,41]
# 并列列
# plt.bar(x坐标列表，y坐标列表，条形宽度)
plt.bar(index,BJ,width=0.3)
plt.bar(index+0.3,Sh,width=0.3,color='green')
plt.xticks(index+0.3/2,index)
# 罗列列
# plt.bar(x坐标列表，y坐标列表，条形底部值，条形宽度)
plt.bar(index,Sh,bottom=BJ,width=0.3,color='green')
plt.show()


```

## 直⽅方图

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

'''
现有250部电影的时⻓长，希望统计出这些电影时⻓长的分布状态(⽐比如时⻓长为100分钟到120分钟电影的数量量，
出现的频率)等信息，你应该如何呈现这些数据？
'''
from matplotlib import pyplot as plt
from matplotlib import font_manager
# 1）准备数据
time = [131, 98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102,
107, 114,
119, 128, 121, 142, 127, 130, 124, 101, 110, 116, 117, 110, 128, 128,
115, 99,
136, 126, 134, 95, 138, 117, 111,78, 132, 124, 113, 150, 110, 117,
86, 95, 144,
105, 126, 130,126, 130, 126, 116, 123, 106, 112, 138, 123, 86, 101,
99, 136,123,
117, 119, 105, 137, 123, 128, 125, 104, 109, 134, 125, 127,105, 120,
107, 129, 116,
108, 132, 103, 136, 118, 102, 120, 114,105, 115, 132, 145, 119, 121,
112, 139, 125,
138, 109, 132, 134,156, 106, 117, 127, 144, 139, 139, 119, 140, 83,
110, 102,123,
107, 143, 115, 136, 118, 139, 123, 112, 118, 125, 109, 119, 133,112,
114, 122, 109,
106, 123, 116, 131, 127, 115, 118, 112, 135,115, 146, 137, 116, 103,
144, 83, 123,
111, 110, 111, 100, 154,136, 100, 118, 119, 133, 134, 106, 129, 126,
110, 111, 109,
141,120, 117, 106, 149, 122, 122, 110, 118, 127, 121, 114, 125,
126,114, 140, 103,
130, 141, 117, 106, 114, 121, 114, 133, 137, 92,121, 112, 146, 97,
137, 105, 98,
117, 112, 81, 97, 139, 113,134, 106, 144, 110, 137, 137, 111, 104,
117, 100, 111,
101, 110,105, 129, 137, 112, 120, 113, 133, 112, 83, 94, 146, 133,
101,131, 116,
111, 84, 137, 115, 122, 106, 144, 109, 123, 116, 111,111, 133, 150]
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=10)
# 2）创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 3）绘制直⽅方图
# 设置组距
distance = 2
# 计算组数
group_num = int((max(time) - min(time)) / distance)
# 绘制直⽅方图
plt.hist(time, bins=group_num)
# 修改x轴刻度显示
plt.xticks(range(min(time), max(time))[::2])
# 添加⽹网格显示
plt.grid(linestyle="--", alpha=0.5)
# 添加x, y轴描述信息
plt.xlabel("电影时长⼤小",fontproperties=my_font)
plt.ylabel("电影的数据量",fontproperties=my_font)
# 4）显示图像
plt.show()

```

## 饼状图

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=10)
label_list = ["第一部分", "第二部分", "第三部分"] # 各部分标签
size = [55, 35, 10] # 各部分⼤大⼩小
color = ["red", "green", "blue"] # 各部分颜⾊色
explode = [0, 0.05, 0] # 各部分突出值
"""
绘制饼图
explode：设置各部分突出
label:设置各部分标签
labeldistance:设置标签⽂文本距圆⼼心位置，1.1表示1.1倍半径
autopct：设置圆⾥里里⾯面⽂文本
shadow：设置是否有阴影
startangle：起始⻆角度，默认从0开始逆时针转
pctdistance：设置圆内⽂文本距圆⼼心距离


返回值:
patches : matplotlib.patches.Wedge列列表(扇形实例例)
l_text：label matplotlib.text.Text列列表(标签实例例)
p_text：label matplotlib.text.Text列列表(百分⽐比标签实例例)
"""
plt.figure(figsize=(20, 8), dpi=100)
patches, l_text, p_text = plt.pie(size,
    explode=explode,
    colors=color,
    labels=label_list,
    labeldistance=1.1,
    autopct="%1.1f%%",
    shadow=False,
    startangle=90,
    pctdistance=0.6)

# l_text：label matplotlib.text.Text列列表(标签实例例)
for t in l_text:
    # print(dir(t))
    t.set_fontproperties(my_font)
# p_text：label matplotlib.text.Text列列表(百分⽐比标签实例例)
for i,t in enumerate(p_text):
    t.set_size(30)
    if i ==1:
        t.set_color('orange')
# patches : matplotlib.patches.Wedge列列表(扇形实例例)
for i in patches:
    i.set_color('pink')
    break
plt.legend(prop=my_font)
plt.show()


```

