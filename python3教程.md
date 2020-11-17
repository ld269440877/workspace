# python3教程

## python 基础

Python是一种通用的解释，交互式，面向对象和高级编程语言。它是由Guido van Rossum在1985 - 1990年创建的。像Perl一样，Python源代码也可以在GNU通用公共许可证(GPL)下获得。Python是以电视节目“**Monty Python`s Flying Circus**”来命名，并不是以莽蛇(Python)来命名的。

*Python 3.0*在2008年发布。虽然这个版本应该是不向后兼容的，但后来许多重要的功能已经被反映到兼容版本2.7中，本教程中是以*Python 3*版本来学习和演示Python编程。

Python的官方网站是：http://www.python.org/ ，可以从官方上找到大部分有关Python编程语言的相关资料，如：各种版本的安装包下载，文档，最新的Python资讯，社区以及教程等等。官方网站打开以后如下所示



![img](E:\git\python3-noteboook\python3教程.assets\925170623_77825.png)

### 初识Python程序

下面是一个简单的Python程序 - 

```python
##!/usr/bin/python3

print ("Hello, Python!")
Python
```

> 重要提示：本教程中，所以实例代码是基于 *Python 3* 来编写的，由于*Python 2*与*Python 3*代码不能兼容，所以希望所有学习本教程的读者安装好 *Python 3* 及以上版本。

### Python在线开发工具（免安装）

推荐你使用 [Coding Cloud Studio](https://studio.coding.net/) 这款在线云端开发工具编写并运行本教程内所有 Python 代码以及示例。Coding Cloud Studio 是基于腾讯云小主机的开发工作站，提供原生的在线 Linux 命令交互终端环境，同时集成了 Python 2 以及 Python 3，在线开发文本编辑器，你可以直接在工作站中创建 Python 文件并在 Cloud Studio 中运行你写的 Python 程序。无须在自己电脑上安装配置本地 Python 环境。

![img](E:\git\python3-noteboook\python3教程.assets\c2e566c7-7ebe-4266-b803-9d14c244c3b5.png)

# Python快速入门

Python是面向对象，高级语言，解释，动态和多用途编程语言。Python易于学习，而且功能强大，功能多样的脚本语言使其对应用程序开发具有吸引力。
Python的语法和动态类型具有其解释性质，使其成为许多领域的脚本编写和快速应用程序开发的理想语言。

Python支持多种编程模式，包括面向对象编程，命令式和函数式编程或过程式编程。

Python几乎无所不能，一些常用的开发领域，如Web编程。这就是为什么它被称为多用途，因为它可以用于网络，企业，3D CAD等软件和系统开发。

在Python中，不需要使用数据类型来声明变量，因为它是动态类型的，所以可以写一个如 `a=10` 来声明一个变量`a`中的值是一个整数类型。

Python使开发和调试快速，因为在python开发中没有包含编译步骤，并且编辑 <-> 测试 <-> 调试循环使用代码开发效率非常高。

Python是一种高级，解释，交互和面向对象的脚本语言。 Python被设计为高度可读性。 它使用英语关键字，而其他语言使用标点符号。它的语法结构比其他语言少。

- **Python是解释型语言** - Python代码在解释器中运行时处理，执行前不需要编译程序。 这与PERL和PHP类似。
- **Python是交动的** - 在Python提示符下面直接和解释器进行交互来编写程序。
- **Python是面向对象的** - Python支持面向对象的风格或编程技术，将代码封装在对象内。
- **Python是一门初学者的语言** - Python是初学者程序员的伟大语言，并支持从简单的文本处理到*WWW*浏览器到游戏的各种应用程序的开发。

### 第一节 Python 可以用来开发什么？

Python作为一个整体可以用于任何软件开发领域。下面来看看Python可以应用在哪些领域的开发。如下所列 - 

**1.基于控制台的应用程序**

Python可用于开发基于控制台的应用程序。 例如：*IPython*。

**2.基于音频或视频的应用程序**

Python在多媒体部分开发，证明是非常方便的。 一些成功的应用是：*TimPlayer*，*cplay*等。

**3.3D CAD应用程序**

*Fandango*是一个真正使用Python编写的应用程序，提供CAD的全部功能。

**4.Web应用程序**

Python也可以用于开发基于Web的应用程序。 一些重要的开发案例是：*PythonWikiEngines*，*Pocoo*，*PythonBlogSoftware*等，如国内的成功应用案例有：豆瓣，知乎等。

**5.企业级应用**

Python可用于创建可在企业或组织中使用的应用程序。一些实时应用程序是：*OpenErp*，*Tryton*，*Picalo*等。

**6.图像应用**

使用Python可以开发图像应用程序。 开发的应用有：VPython，Gogh，imgSeek等

### 第二节 Python安装和环境配置

*Python 3*适用于Windows，Mac OS和大多数Linux操作系统。即使*Python 2*目前可用于许多其他操作系统，有部分系统*Python 3*还没有提供支持或者支持了但被它们在系统上删除了，只保留旧的*Python 2*版本。

参考：http://www.yiibai.com/python/python_environment.html

### 第三节 Python命令行参数

Python提供了一个`getopt`模块，用于解析命令行选项和参数。

```shell
$ python test.py arg1 arg2 arg3
Shell
```

Python `sys`模块通过`sys.argv`提供对任何命令行参数的访问。主要有两个参数变量 -

- `sys.argv`是命令行参数的列表。
- `len(sys.argv)`是命令行参数的数量。

这里`sys.argv [0]`是程序名称，即脚本的名称。比如在上面示例代码中，`sys.argv [0]`的值就是 `test.py`。

#### 示例

看看以下脚本`command_line_arguments.py`的代码 -

```python
##!/usr/bin/python3

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
Python
```

现在运行上面的脚本，这将产生以下结果 -

```python
F:\>python F:\worksp\python\command_line_arguments.py
Number of arguments: 1 arguments.
Argument List: ['F:\\worksp\\python\\command_line_arguments.py']

F:\>python F:\worksp\python\command_line_arguments.py arg1 arg2 arg3 arg4
Number of arguments: 5 arguments.
Argument List: ['F:\\worksp\\python\\command_line_arguments.py', 'arg1', 'arg2', 'arg3', 'arg4']

F:\>
Python
```

> 注意 - 如上所述，第一个参数始终是脚本名称，它也被计入参数的数量。

### 解析命令行参数

Python提供了一个`getopt`模块，可用于解析命令行选项和参数。该模块提供了两个功能和异常，以启用命令行参数解析。

**getopt.getopt方法**

此方法解析命令行选项和参数列表。以下是此方法的简单语法 -

```python
getopt.getopt(args, options, [long_options])
Python
```

**getopt.GetoptError异常**

当在参数列表中有一个无法识别的选项，或者当需要一个参数的选项不为任何参数时，会引发这个异常。
异常的参数是一个字符串，指示错误的原因。 属性`msg`和`opt`给出错误消息和相关选项。

#### 示例

假设想通过命令行传递两个文件名，也想给出一个选项用来显示脚本的用法。脚本的用法如下 -

```shell
usage: file.py -i <inputfile> -o <outputfile>
Shell
```

以下是`command_line_usage.py`的以下脚本 -

```python
##!/usr/bin/python3

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('GetoptError, usage: command_line_usage.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('usage: command_line_usage.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is "', inputfile)
   print ('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
Python
```

现在，使用以下几种方式运行来脚本，输出如下所示：

```shell
F:\worksp\python>python command_line_usage.py -h
usage: command_line_usage.py -i <inputfile> -o <outputfile>

F:\worksp\python>python command_line_usage.py -i inputfile.txt -o
GetoptError, usage: command_line_usage.py -i <inputfile> -o <outputfile>

F:\worksp\python>python command_line_usage.py -i inputfile.txt -o outputfile.txt
Input file is " inputfile.txt
Output file is " outputfile.txt

F:\worksp\python>
Shell
```

### 第四节  Python变量类型

变量是保存存储值的内存位置。也就是说，当创建一个变量时，可以在内存中保留一些空间。

基于变量的数据类型，解释器分配内存并决定可以存储在保留的存储器中的内容。 因此，通过为变量分配不同的数据类型，可以在这些变量中存储的数据类型为整数，小数或字符等等。

#### 将值分配给变量

在Python中，变量不需要明确的声明类型来保留内存空间。当向变量分配值时，Python会自动发出声明。 等号(`=`)用于为变量赋值。

`=`运算符左侧的操作数是变量的名称，而`=`运算符右侧的操作数是将在存储在变量中的值。 例如 -

```python
##!/usr/bin/python3

counter = 100          # 一个整型数
miles   = 999.99       # 一个浮点数
name    = "Maxsu"       # 一个字符串
site_url  = "http://www.yiibai.com" # 一个字符串

print (counter)
print (miles)
print (name)
print (site_url)
Python
```

这里，`100`,`999.99`和“`Maxsu`”分别是分配给`counter`，`miles`和`name`变量的值。执行上面代码将产生以下结果 -

```shell
100
999.99 
Maxsu
http://www.yiibai.com
Shell
```

#### 多重赋值

Python允许同时为多个变量分配单个值。

例如 -

```python
a = b = c = 1
Python
```

这里，创建一个整数对象，其值为`1`，并且所有三个变量都分配给相同的内存位置。还可以将多个对象分配给多个变量。 例如 -

```python
a, b, c = 10, 20, "maxsu"
Python
```

这里，将两个值为`10`和`20`的整数对象分别分配给变量`a`和`b`，并将一个值为“`maxsu`”的字符串对象分配给变量`c`。

#### 标准数据类型

存储在内存中的数据可以是多种类型。 例如，一个人的年龄可存储为一个数字值，他的地址被存储为字母数字字符串。 Python具有各种标准数据类型，用于定义可能的操作以及每个标准数据类型的存储方法。

Python有五种标准数据类型 -

- **1.数字**
- **2.字符串**
- **3.列表**
- **4.元组**
- **5.字典**

##### 1.Python数字

数字数据类型存储数字值。当为其分配值时，将创建数字对象。 例如 -

```python
var1 = 10
var2 = 20
Python
```

可以使用`del`语句删除对数字对象的引用。 `del`语句的语法是 -

```python
del var1[,var2[,var3[....,varN]]]]
Python
```

可以使用`del`语句删除单个对象或多个对象。

例如 -

```python
del var
del var_a, var_b
Python
```

Python支持三种不同的数值类型 - 

- int(有符号整数)
- float(浮点实值)
- complex(复数)

Python3中的所有整数都表示为长整数。 因此，长整数没有单独的数字类型。

**例子**

以下是一些数字示例 -

| int    | float      | complex    |
| ------ | ---------- | ---------- |
| 10     | 0.0        | 3.14j      |
| 100    | 15.20      | 45.j       |
| -786   | -21.9      | 9.322e-36j |
| 080    | 32.3+e18   | .876j      |
| -0490  | -90.       | -.6545+0J  |
| -0x260 | -32.54e100 | 3e+26J     |
| 0x69   | 70.2-E12   | 4.53e-7j   |

复数是由`x + yj`表示的有序对的实数浮点数组成，其中`x`和`y`是实数，`j`是虚数单位。

##### 2.Python字符串

Python中的字符串被标识为在引号中表示的连续字符集。Python允许双引号或双引号。 可以使用片段运算符(`[]`和`[:]`)来获取字符串的子集(子字符串)，其索引从字符串开始处的索引`0`开始，并且以`-1`表示字符串中的最后一个字符。

加号(`+`)是字符串连接运算符，星号(`*`)是重复运算符。例如 -

```python
##!/usr/bin/python3
##coding=utf-8
## save file: variable_types_str1.py

str = 'yiibai.com'

print ('str = ', str)          # Prints complete string
print ('str[0] = ',str[0])       # Prints first character of the string
print ('str[2:5] = ',str[2:5])     # Prints characters starting from 3rd to 5th
print ('str[2:] = ',str[2:])      # Prints string starting from 3rd character
print ('str[-1] = ',str[-1])      # 最后一个字符，结果为：'!'
print ('str * 2 = ',str * 2)      # Prints string two times
print ('str + "TEST" = ',str + "TEST") # Prints concatenated string
Python
```

将上面代码保存到 `variable_types_str1.py` 文件中，执行将产生以下结果 -

```shell
F:\worksp\python>python variable_types_str1.py
str =  yiibai.com
str[0] =  y
str[2:5] =  iba
str[2:] =  ibai.com
str[-1] =  m
str * 2 =  yiibai.comyiibai.com
str + "TEST" =  yiibai.comTEST

F:\worksp\python>
Shell
```

##### 3.Python列表

列表是Python复合数据类型中最多功能的。 一个列表包含用逗号分隔并括在方括号(`[]`)中的项目。在某种程度上，列表类似于C语言中的数组。它们之间的区别之一是Python列表的所有项可以是不同的数据类型，而C语言中的数组只能是同种类型。

存储在列表中的值可以使用切片运算符(`[]`和`[]`)来访问，索引从列表开头的`0`开始，并且以`-1`表示列表中的最后一个项目。 加号(`+`)是列表连接运算符，星号(`*`)是重复运算符。例如 -

```python
##!/usr/bin/python3
##coding=utf-8
## save file: variable_types_str1.py
list = [ 'yes', 'no', 786 , 2.23, 'minsu', 70.2 ]
tinylist = [100, 'maxsu']

print ('list = ', list)          # Prints complete list
print ('list[0] = ',list[0])       # Prints first element of the list
print ('list[1:3] = ',list[1:3])     # Prints elements starting from 2nd till 3rd 
print ('list[2:] = ',list[2:])      # Prints elements starting from 3rd element
print ('list[-3:-1] = ',list[-3:-1])    
print ('tinylist * 2 = ',tinylist * 2)  # Prints list two times
print ('list + tinylist = ', list + tinylist) # Prints concatenated lists
Python
```

将上面代码保存到 `variable_types_str1.py` 文件中，执行将产生以下结果 -

```shell
F:\worksp\python>python variable_types_list.py
list =  ['yes', 'no', 786, 2.23, 'minsu', 70.2]
list[0] =  yes
list[1:3] =  ['no', 786]
list[2:] =  [786, 2.23, 'minsu', 70.2]
list[-3:-1] =  [2.23, 'minsu']
tinylist * 2 =  [100, 'maxsu', 100, 'maxsu']
list + tinylist =  ['yes', 'no', 786, 2.23, 'minsu', 70.2, 100, 'maxsu']

F:\worksp\python>
Shell
```

##### 4.Python元组

元组是与列表非常类似的另一个序列数据类型。元组是由多个值以逗号分隔。然而，与列表不同，元组被括在小括号内(`()`)。

列表和元组之间的主要区别是 - 列表括在括号(`[]`)中，列表中的元素和大小可以更改，而元组括在括号(`()`)中，无法更新。元组可以被认为是**只读**列表。 例如 -

```python
##!/usr/bin/python3
##coding=utf-8
## save file : variable_types_tuple.py
tuple = ( 'maxsu', 786 , 2.23, 'yiibai', 70.2  )
tinytuple = (999.0, 'maxsu')

## tuple[1] = 'new item value' 不能这样赋值

print ('tuple = ', tuple)           # Prints complete tuple
print ('tuple[0] = ', tuple[0])        # Prints first element of the tuple
print ('tuple[1:3] = ', tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print ('tuple[-3:-1] = ', tuple[-3:-1])       # 输出结果是什么？
print ('tuple[2:] = ', tuple[2:])       # Prints elements starting from 3rd element
print ('tinytuple * 2 = ',tinytuple * 2)   # Prints tuple two times
print ('tuple + tinytuple = ', tuple + tinytuple) # Prints concatenated tuple
Python
```

将上面代码保存到 `variable_types_tuple.py` 文件中，执行将产生以下结果 -

```shell
F:\worksp\python>python variable_types_tuple.py
tuple =  ('maxsu', 786, 2.23, 'yiibai', 70.2)
tuple[0] =  maxsu
tuple[1:3] =  (786, 2.23)
tuple[-3:-1] =  (2.23, 'yiibai')
tuple[2:] =  (2.23, 'yiibai', 70.2)
tinytuple * 2 =  (999.0, 'maxsu', 999.0, 'maxsu')
tuple + tinytuple =  ('maxsu', 786, 2.23, 'yiibai', 70.2, 999.0, 'maxsu')

F:\worksp\python>
Shell
```

以下代码对于元组无效，因为尝试更新元组，但是元组是不允许更新的。类似的情况可能与列表 -

```python
##!/usr/bin/python3

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
tuple[2] = 1000    # 无法更新值，程序出错
list[2] = 1000     # 有效的更新，合法
Python
```

#### Python字典

Python的字典是一种哈希表类型。它们像Perl中发现的关联数组或散列一样工作，由键值对组成。字典键几乎可以是任何Python数据类型，但通常为了方便使用数字或字符串。另一方面，值可以是任意任意的Python对象。

字典由大括号(`{}`)括起来，可以使用方括号(`[]`)分配和访问值。例如 -

```python
##!/usr/bin/python3
##coding=utf-8
## save file : variable_types_dict.py

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is my"

tinydict = {'name': 'maxsu', 'code' : 1024, 'dept':'IT Dev'}


print ("dict['one'] = ", dict['one'])       # Prints value for 'one' key
print ('dict[2] = ', dict[2])           # Prints value for 2 key
print ('tinydict = ', tinydict)          # Prints complete dictionary
print ('tinydict.keys() = ', tinydict.keys())   # Prints all the keys
print ('tinydict.values() = ', tinydict.values()) # Prints all the values
Python
```

将上面代码保存到 `variable_types_dict.py` 文件中，执行将产生以下结果 -

```shell
F:\worksp\python>python variable_types_dict.py
dict['one'] =  This is one
dict[2] =  This is my
tinydict =  {'name': 'maxsu', 'code': 1024, 'dept': 'IT Dev'}
tinydict.keys() =  dict_keys(['name', 'code', 'dept'])
tinydict.values() =  dict_values(['maxsu', 1024, 'IT Dev'])
Shell
```

字典中的元素没有顺序的概念。但是说这些元素是“乱序”是不正确的; 它们是无序的。

#### 数据类型转换

有时，可能需要在内置类型之间执行转换。要在类型之间进行转换，只需使用类型名称作为函数即可。

有以下几种内置函数用于执行从一种数据类型到另一种数据类型的转换。这些函数返回一个表示转换值的新对象。它们分别如下所示 -

| 编号 | 函数                    | 描述                                                   |
| ---- | ----------------------- | ------------------------------------------------------ |
| 1    | `int(x [,base])`        | 将`x`转换为整数。如果`x`是字符串，则要`base`指定基数。 |
| 2    | `float(x)`              | 将`x`转换为浮点数。                                    |
| 3    | `complex(real [,imag])` | 创建一个复数。                                         |
| 4    | `str(x)`                | 将对象`x`转换为字符串表示形式。                        |
| 5    | `repr(x)`               | 将对象`x`转换为表达式字符串。                          |
| 6    | `eval(str)`             | 评估求值一个字符串并返回一个对象。                     |
| 7    | `tuple(s)`              | 将`s`转换为元组。                                      |
| 8    | `list(s)`               | 将`s`转换为列表。                                      |
| 9    | `set(s)`                | 将`s`转换为集合。                                      |
| 10   | `dict(d)`               | 创建一个字典，`d`必须是`(key，value)`元组的序列        |
| 11   | `frozenset(s)`          | 将`s`转换为冻结集                                      |
| 12   | `chr(x)`                | 将整数`x`转换为字符                                    |
| 13   | `unichr(x)`             | 将整数`x`转换为Unicode字符。                           |
| 14   | `ord(x)`                | 将单个字符`x`转换为其整数值。                          |
| 15   | `hex(x)`                | 将整数`x`转换为十六进制字符串。                        |
| 16   | `oct(x)`                | 将整数`x`转换为八进制字符串。                          |

### 第五节 Python基本运算符

运算符是可以操纵操作数值的结构。如下一个表达式：`10 + 20 = 30`。这里，`10`和`20`称为操作数，`+`则被称为运算符。

### 运算符类型

Python语言支持以下类型的运算符 -

- 1.算术运算符
- 2.比较(关系)运算符
- 3.赋值运算符
- 4.逻辑运算符
- 5.按位运算符
- 6.成员运算符
- 7.身份运算符

下面让我们依次来看看所有的运算符。

#### 1.算术运算符

假设变量`a`的值是`10`，变量`b`的值是`21`，则 -

| 运算符 | 描述                                                         | 示例                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `+`    | 加法运算，将运算符两边的操作数增加。                         | `a + b = 31`                                                 |
| `-`    | 减法运算，将运算符左边的操作数减去右边的操作数。             | `a – b = -11`                                                |
| `*`    | 乘法运算，将运算符两边的操作数相乘                           | `a * b = 210`                                                |
| `/`    | 除法运算，用右操作数除左操作数                               | `b / a = 2.1`                                                |
| `%`    | 模运算，用右操作数除数左操作数并返回余数                     | `b % a = 1`                                                  |
| `**`   | 对运算符进行指数(幂)计算                                     | `a ** b`，表示`10`的`21`次幂                                 |
| `//`   | 地板除 - 操作数的除法，其结果是删除小数点后的商数。 但如果其中一个操作数为负数，则结果将被保留，即从零(向负无穷大)舍去 | `9//2 = 4` ， `9.0//2.0 = 4.0`, `-11//3 = -4`, `-11.0//3 = -4.0` |

有关算术运算符的示例代码，请参考：：http://www.yiibai.com/python/arithmetic_operators_example.html 

#### 2.比较(关系)运算符

比较(关系)运算符比较它们两边的值，并确定它们之间的关系。它们也称为关系运算符。假设变量`a`的值`10`，变量`b`的值是`20`，则 -

| 运算符 | 描述                                                   | 示例                         |
| ------ | ------------------------------------------------------ | ---------------------------- |
| `==`   | 如果两个操作数的值相等，则条件为真。                   | `(a == b)`求值结果为 `false` |
| `!=`   | 如果两个操作数的值不相等，则条件为真。                 | `(a != b)`求值结果为 `true`  |
| `>`    | 如果左操作数的值大于右操作数的值，则条件成为真。       | `(a > b)`求值结果为 `false`  |
| `<`    | 如果左操作数的值小于右操作数的值，则条件成为真。       | `(a < b)`求值结果为 `true`   |
| `>=`   | 如果左操作数的值大于或等于右操作数的值，则条件成为真。 | `(a >= b)`求值结果为 `false` |
| `<=`   | 如果左操作数的值小于或等于右操作数的值，则条件成为真。 | `(a <= b)`求值结果为 `true`  |

有关比较(关系)运算符的示例代码，请参考：http://www.yiibai.com/python/comparison_operators_example.html 

#### 3.赋值运算符

假设变量`a`的值`10`，变量`b`的值是`20`，则 -

| 运算符 | 描述                                                 | 示例                                  |
| ------ | ---------------------------------------------------- | ------------------------------------- |
| `=`    | 将右侧操作数的值分配给左侧操作数                     | `c = a + b`表示将`a + b`的值分配给`c` |
| `+=`   | 将右操作数相加到左操作数，并将结果分配给左操作数     | `c + = a`等价于`c = c + a`            |
| `-=`   | 从左操作数中减去右操作数，并将结果分配给左操作数     | `c -= a` 等价于 `c = c - a`           |
| `*=`   | 将右操作数与左操作数相乘，并将结果分配给左操作数     | `c *= a` 等价于 `c = c * a`           |
| `/=`   | 将左操作数除以右操作数，并将结果分配给左操作数       | `c /= a` 等价于 `c = c / a`           |
| `%=`   | 将左操作数除以右操作数的模数，并将结果分配给左操作数 | `c %= a` 等价于 `c = c % a`           |
| `**=`  | 执行指数(幂)计算，并将值分配给左操作数               | `c **= a` 等价于 `c = c ** a`         |
| `//=`  | 运算符执行地板除运算，并将值分配给左操作数           | `c //= a` 等价于 `c = c // a`         |

有关赋值运算符的示例代码，请参考：http://www.yiibai.com/python/assignment_operators_example.html 

#### 4.逻辑运算符

Python语言支持以下逻辑运算符。假设变量`a`的值为`True`，变量`b`的值为`False`，那么 -

| 运算符 | 描述                                           | 示例                            |
| ------ | ---------------------------------------------- | ------------------------------- |
| `and`  | 如果两个操作数都为真，则条件成立。             | `(a and b)`的结果为`False`      |
| `or`   | 如果两个操作数中的任何一个非零，则条件成为真。 | `(a or b)`的结果为`True`        |
| `not`  | 用于反转操作数的逻辑状态。                     | `not(a and b)` 的结果为`True`。 |

有关逻辑运算符的示例代码，请参考：http://www.yiibai.com/python/logical_operators_example.html 

#### 5.按位运算符

按位运算符执行逐位运算。 假设变量`a = 60`; 和变量`b = 13`; 现在以二进制格式，它们将如下 -

```shell
a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a = 1100 0011
Shell
```

Python的内置函数`bin()`可用于获取整数的二进制表示形式。

以下是Python语言支持位运算操作符 -

| 运算符                        | 描述                                                         | 示例                                                         |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `&`                           | 如果它存在于两个操作数中，则操作符复制位到结果中             | `(a & b)` 结果表示为 `0000 1100`                             |
| ![img](/static/images/or.png) | 如果它存在于任一操作数，则复制位。                           | (a ![img](/static/images/or.png) b) = 61 结果表示为 `0011 1101` |
| `^`                           | 二进制异或。如果它是一个操作数集合，但不是同时是两个操作数则将复制位。 | `(a ^ b) = 49` (结果表示为 `0011 0001`)                      |
| `~`                           | 二进制补码，它是一元的，具有“翻转”的效果。                   | `(~a ) = -61`有符号的二进制数，表示为`1100 0011`的补码形式。 |
| `<<`                          | 二进制左移，左操作数的值由右操作数指定的位数左移。           | `a << 2 = 240` (结果表示为 `1111 0000`)                      |
| `>>`                          | 二进制右移，左操作数的值由右操作数指定的位数右移。           | `a >> 2 = 15`(结果表示为`0000 1111`)                         |

有关按位运算符的示例代码，请参考：http://www.yiibai.com/python/bitwise_operators_example.html 

#### 6.成员运算符

Python成员运算符测试给定值是否为序列中的成员，例如字符串，列表或元组。 有两个成员运算符，如下所述 - 

| 运算符   | 描述                                                         | 示例 |
| -------- | ------------------------------------------------------------ | ---- |
| `in`     | 如果在指定的序列中找到一个变量的值，则返回`true`，否则返回`false`。 | -    |
| `not in` | 如果在指定序列中找不到变量的值，则返回`true`，否则返回`false`。 | -    |

有关成员运算符的示例代码，请参考：http://www.yiibai.com/python/membership_operators_example.html 

#### 7.身份运算符

身份运算符比较两个对象的内存位置。常用的有两个身份运算符，如下所述 -

| 运算符   | 描述                                                         | 示例 |
| -------- | ------------------------------------------------------------ | ---- |
| `is`     | 如果运算符任一侧的变量指向相同的对象，则返回`True`，否则返回`False`。 |      |
| `is not` | 如果运算符任一侧的变量指向相同的对象，则返回`True`，否则返回`False`。 | -    |

有关身份运算符的示例代码，请参考：http://www.yiibai.com/python/identity_operators_example.html 

#### 8. 运算符优先级

下表列出了从最高优先级到最低优先级的所有运算符，如下所示 - 

| 序号 | 运算符                                   | 描述                                           |
| ---- | ---------------------------------------- | ---------------------------------------------- |
| 1    | `**`                                     | 指数(次幂)运算                                 |
| 2    | `~` `+`  `-`                             | 补码，一元加减(最后两个的方法名称是`+@`和`-@`) |
| 3    | `*` `/` `%` `//`                         | 乘法，除法，模数和地板除                       |
| 4    | `+` `-`                                  |                                                |
| 5    | `>>` `<<`                                | 向右和向左位移                                 |
| 6    | `&`                                      | 按位与                                         |
| 7    | `^` ![img](/static/images/or.png)        | 按位异或和常规的“`OR`”                         |
| 8    | `<=` `<` `>` `>=`                        | 比较运算符                                     |
| 9    | `<>` `==` `!=`                           | 等于运算符                                     |
| 10   | `=` `%=` `/=` `//=` `-=` `+=` `*=` `**=` | 赋值运算符                                     |
| 11   | `is` `is not`                            | 身份运算符                                     |
| 12   | `in` `not in`                            | 成员运算符                                     |
| 13   | `not` `or` `and`                         | 逻辑运算符                                     |

有关运算符优先级的示例代码，请参考：http://www.yiibai.com/python/operators_precedence_example.html 

### 第六节 Python决策

决策是指在执行程序期间根据发生的情况并根据条件采取的具体操作(行动)。决策结构评估求值多个表达式，产生`TRUE`或`FALSE`作为结果。如果结果为`TRUE`或否则为`FALSE`，则需要确定要执行的操作和要执行的语句。

以下是大多数编程语言中的典型决策结构的一般形式 -

![img](E:\git\python3-noteboook\python3教程.assets\605220624_31440.jpg)

Python编程语言假定任何非零值和非空值都为`TRUE`值，而任何零值或空值都为`FALSE`值。

Python编程语言提供以下类型的决策语句。

| 编号 | 语句                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [if语句](http://www.yiibai.com/python/python_if_statement.html) | 一个if语句由一个布尔表达式，后跟一个或多个语句组成。         |
| 2    | [if…else语句](http://www.yiibai.com/python/python_if_else.html) | 一个`if`语句可以跟随一个可选的`else`语句，当`if`语句的布尔表达式为`FALSE`时，则`else`语句块将被执行。 |
| 3    | [嵌套if语句](http://www.yiibai.com/python/nested_if_statements_in_python.html) | 可以在一个`if`或`else`语句中使用一个`if`或`else if`语句。    |

下面我们快速地来了解每个决策声明。

### 单个语句套件

一个`if`子句套件可能只包含一行，它可能与头语句在同一行上。

**示例**

以下是一行`if`子句的示例 -

```python
##!/usr/bin/python3
var = 10
if ( var  == 10 ) : print ("Value of expression is 10")
print ("Good bye!")
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Value of expression is 100
Good bye!
Shell
```

### 第七节  Python循环

一般来说，语句依次执行 - 例如，函数中的第一个语句首先执行，然后是第二个语句，依次类推。但是有很多时候需要多次执行同一段代码，这就引入了循环的概念。

编程语言提供了允许更复杂的执行路径的各种控制结构。

循环语句允许多次执行语句或语句组。下图说明了一个循环语句流程结构 -

![img](E:\git\python3-noteboook\python3教程.assets\823080656_41224.jpg)

Python编程语言提供以下类型的循环来处理循环需求。

| 编号 | 循环                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [while循环](http://www.yiibai.com/python/python_while_loop.html) | 在给定条件为`TRUE`时，重复一个语句或一组语句。 它在执行循环体之前测试状态。 |
| 2    | [for循环](http://www.yiibai.com/python/python_for_loop.html) | 多次执行一系列语句，并缩写管理循环变量的代码。               |
| 3    | [嵌套循环](http://www.yiibai.com/python/python_nested_loops.html) | 可以使用一个或多个循环在`while`或`for`循环中。               |

### 循环控制语句

循环控制语句从正常顺序更改执行。 当执行离开范围时，在该范围内创建的所有自动对象都将被销毁。

Python支持以下控制语句。

| 编号 | 控制语句                                                     | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [break语句](http://www.yiibai.com/python/python_break_statement.html) | 终止循环语句并将执行转移到循环之后的语句。                   |
| 2    | [continue语句](http://www.yiibai.com/python/python_continue_statement.html) | 使循环跳过其主体的剩余部分，并立即重新测试其状态以进入下一次迭代。 |
| 3    | [pass语句](http://www.yiibai.com/python/python_pass_statement.html) | 当语法需要但不需要执行任何命令或代码时，Python中就可以使用`pass`语句，此语句什么也不做，用于表示“占位”的代码，有关实现细节后面再写 |

下面简单地看一下循环控制语句。

### 迭代器和生成器

迭代器(Iterator)是允许程序员遍历集合的所有元素的对象，而不管其具体实现。在Python中，迭代器对象实现了`iter()`和`next()`两种方法。

`String`，`List`或`Tuple`对象可用于创建`Iterator`。

```python
list = [1,2,3,4]
it = iter(list) # this builds an iterator object
print (next(it)) #prints next available element in iterator
## Iterator object can be traversed using regular for statement

for x in it:
   print (x, end=" ")
or using next() function
while True:
   try:
      print (next(it))
   except StopIteration:
      sys.exit() #you have to import sys module for this
Python
```

发生器(`generator`)是使用`yield`方法产生或产生一系列值的函数。

当一个生成器函数被调用时，它返回一个生成器对象，而不用执行该函数。 当第一次调用`next()`方法时，函数开始执行，直到它达到`yield`语句，返回`yielded`值。 `yield`保持跟踪，即记住最后一次执行，而第二个`next()`调用从前一个值继续。

#### 示例

以下示例定义了一个生成器，它为所有斐波纳契数字生成一个迭代器。

```python
##!usr/bin/python3
import sys
def fibonacci(n): #generator function
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n): 
         return
      yield a
      a, b = b, a + b
      counter += 1
f = fibonacci(5) #f is iterator object

while True:
   try:
      print (next(f), end=" ")
   except StopIteration:
      sys.exit()
Python
```

### 第八节  Python数字

数字数据类型用于存储数值。它们是不可变数据类型。这意味着，更改数字数据类型的值会导致新分配对象。

当为数字数据类型分配值时，Python将创建数字对象。 例如 -

```python
var1 = 1
var2 = 10
Python
```

可以使用`del`语句删除对数字对象的引用。`del`语句的语法是 -

```python
del var1[,var2[,var3[....,varN]]]]
Python
```

可以使用`del`语句一次删除单个对象或多个对象。 例如 -

```python
del var
del var_a, var_b
Python
```

Python支持不同的数值类型 -

- **int(有符号整数)** - 它们通常被称为整数或整数。它们是没有小数点的正或负整数。 *Python 3*中的整数是无限大小的。 *Python 2* 有两个整数类型 - `int`和`long`。 *Python 3*中没有“长整数”。
- **float(浮点实数值)** - 也称为浮点数，它们表示实数，并用小数点写整数和小数部分。 浮点数也可以是科学符号，`E`或`e`表示`10`的幂 - ![img](E:\git\python3-noteboook\python3教程.assets\520110614_90614.png)
- **complex(复数)** - 复数是以`a + bJ`的形式，其中`a`和`b`是浮点，`J`(或`j`)表示`-1`的平方根(虚数)。数字的实部是`a`，虚部是`b`。复数在Python编程中并没有太多用处。

可以以十六进制或八进制形式表示整数 - 

```python
>>> number = 0xA0F #Hexa-decimal
>>> number
2575

>>> number = 0o37 #Octal
>>> number
31
Python
```

**例子**

以下是一些数字值的示例 - 

| **int** | **float**  | **complex** |
| ------- | ---------- | ----------- |
| 10      | 0.0        | 3.14j       |
| 100     | 15.20      | 45.j        |
| -786    | -21.9      | 9.322e-36j  |
| 080     | 32.3+e18   | .876j       |
| -0490   | -90.       | -.6545+0J   |
| -0×260  | -32.54e100 | 3e+26J      |
| 0×69    | 70.2-E12   | 4.53e-7j    |

复数由一个`a + bj`来表示，它是由实际浮点数的有序对组成，其中`a`是实部，`b`是复数的虚部。

### 数字类型转换

Python可将包含混合类型的表达式内部的数字转换成用于评估求值的常用类型。 有时需要从一个类型到另一个类型执行明确数字转换，以满足运算符或函数参数的要求。

- `int(x)`将`x`转换为纯整数。
- `long(x)`将`x`转换为长整数。
- `float(x)`将`x`转换为浮点数。
- `complex(x)`将`x`转换为具有实部`x`和虚部`0`的复数。
- `complex(x, y)`将`x`和`y`转换为具有实部为`x`和虚部为`y`的复数。`x`和`y`是数字表达式。

### 数学函数

Python中包括执行数学计算的函数，如下列表所示 - 

| 编号 | 函数                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [abs(x)](http://www.yiibai.com/python/number_abs.html)       | `x`的绝对值，`x`与零之间的(正)距离。                         |
| 2    | [ceil(x)](http://www.yiibai.com/python/number_ceil.html)     | `x`的上限，不小于`x`的最小整数。                             |
| 3    | `cmp(x, y)`                                                  | 如果 `x < y` 返回 `-1`, 如果 `x == y` 返回 `0`, 或者 如果 `x > y` 返回 `1`。在*Python 3*中已经弃用，可使用`return (x>y)-(x<y)`代替。 |
| 4    | [exp(x)](http://www.yiibai.com/python/number_exp.html)       | `x`的指数，返回`e`的`x`次幂                                  |
| 5    | [fabs(x)](http://www.yiibai.com/python/number_fabs.html)     | `x`的绝对值。                                                |
| 6    | [floor(x)](http://www.yiibai.com/python/number_floor.html)   | 不大于`x`的最大整数。                                        |
| 7    | [log(x)](http://www.yiibai.com/python/number_log.html)       | `x`的自然对数(`x > 0`)。                                     |
| 8    | [log10(x)](http://www.yiibai.com/python/number_log10.html)   | 以基数为`10`的`x`的对数(`x > 0`)。                           |
| 9    | [max(x1, x2,…)](http://www.yiibai.com/python/number_max.html) | 给定参数中的最大值，最接近正无穷大值                         |
| 10   | [min(x1, x2,…)](http://www.yiibai.com/python/number_min.html) | 给定参数中的最小值，最接近负无穷小值                         |
| 11   | [modf(x)](http://www.yiibai.com/python/number_modf.html)     | 将`x`的分数和整数部分切成两项放入元组中，两个部分与`x`具有相同的符号。整数部分作为浮点数返回。 |
| 12   | [pow(x, y)](http://www.yiibai.com/python/number_pow.html)    | `x`的`y`次幂                                                 |
| 13   | [round(x [,n\])](http://www.yiibai.com/python/number_round.html) | `x`从小数点舍入到`n`位数。`round(0.5)`结果为 `1.0`， `round(-0.5)` 结果为 `-1.0` |
| 14   | [sqrt(x)](http://www.yiibai.com/python/number_sqrt.html)     | `x`的平方根(`x > 0`)。                                       |

### 随机数函数

随机数字用于游戏，模拟，测试，安全和隐私应用。 Python包括以下通常使用的函数。

| 编号 | 函数                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [choice(seq)](http://www.yiibai.com/python/number_choice.html) | 来自列表，元组或字符串的随机项目。                           |
| 2    | [randrange ([start,\] stop [,step])](http://www.yiibai.com/python/number_randrange.html) | 从范围(start, stop, step)中随机选择的元素。                  |
| 3    | [random()](http://www.yiibai.com/python/number_random.html)  | 返回随机浮点数`r`(`0 <= r < 1`)                              |
| 4    | [seed([x\])](http://www.yiibai.com/python/number_seed.html)  | 设置用于生成随机数的整数起始值。在调用任何其他随机模块功能之前调用此函数，返回`None`。 |
| 5    | [shuffle(lst)](http://www.yiibai.com/python/number_shuffle.html) | 将列表的项目随机化到位置。 返回`None`。                      |
| 6    | [uniform(x, y)](http://www.yiibai.com/python/number_uniform.html) | 返回随机浮点数 `r` (`x <= r < y`)。                          |

### 三角函数

随机数字用于游戏，模拟，测试，安全和隐私应用。 Python包括以下通常使用的函数。

| 编号 | 函数                                                         | 描述                                |
| ---- | ------------------------------------------------------------ | ----------------------------------- |
| 1    | [acos(x)](http://www.yiibai.com/python/number_acos.html)     | 返回`x`的弧余弦值，以弧度表示。     |
| 2    | [asin(x)](http://www.yiibai.com/python/number_asin.html)     | 返回`x`的弧线正弦，以弧度表示。     |
| 3    | [atan(x)](http://www.yiibai.com/python/number_atan.html)     | 返回`x`的反正切，以弧度表示。       |
| 4    | [atan2(y, x)](http://www.yiibai.com/python/number_atan2.html) | 返回`atan(y / x)`，以弧度表示。     |
| 5    | [cos(x)](http://www.yiibai.com/python/number_cos.html)       | 返回`x`弧度的余弦。                 |
| 6    | [hypot(x, y)](http://www.yiibai.com/python/number_hypot.html) | 返回欧几里得规范，`sqrt(x*x + y*y)` |
| 7    | [sin(x)](http://www.yiibai.com/python/number_sin.html)       | 返回`x`弧度的正弦。                 |
| 8    | [tan(x)](http://www.yiibai.com/python/number_tan.html)       | 返回`x`弧度的正切值。               |
| 9    | [degrees(x)](http://www.yiibai.com/python/number_degrees.html) | 将角度`x`从弧度转换为度。           |
| 10   | [radians(x)](http://www.yiibai.com/python/number_radians.html) | 将角度`x`从角度转换为弧度。         |

### 数学常数

该模块还定义了两个数学常数 -

| 编号 | 常量   | 描述         |
| ---- | ------ | ------------ |
| 1    | **pi** | 数学常数`pi` |
| 2    | **e**  | 数学常数`e`  |

### 第九节  Python字符串

字符串是Python中最受欢迎、最常使用的数据类型。可以通过用引号括起字符来创建它们。 Python将单引号与双引号相同。创建字符串和向一个变量赋值一样简单。 例如 -

```python
var1 = 'Hello World!'
var2 = "Python Programming"
Python
```

### 1.访问字符串中的值

Python不支持字符类型; 字符会被视为长度为`1`的字符串，因此也被认为是一个子字符串。要访问子串，请使用方括号的切片加上索引或直接使用索引来获取子字符串。 例如 -

```python
##!/usr/bin/python3

var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5]) # 切片加索引
Python
```

当执行上述代码时，会产生以下结果 -

```shell
var1[0]:  H
var2[1:5]:  ytho
Shell
```

### 2.更新字符串

可以通过将变量分配给另一个字符串来“更新”现有的字符串。 新值可以与其原值相关或完全不同的字符串。 例如 -

```python
##!/usr/bin/python3

var1 = 'Hello World!'

print ("Updated String :- ", var1[:6] + 'Python')
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Updated String :-  Hello Python
Shell
```

### 3.转义字符

下表是可以用反斜杠表示法表示转义或不可打印字符的列表。单引号以及双引号字符串的转义字符被解析。

| 反斜线符号 | 十六进制字符 | 描述/说明                                        |
| ---------- | ------------ | ------------------------------------------------ |
| `\a`       | `0x07`       | 铃声或警报                                       |
| `\b`       | `0x08`       | 退格                                             |
| `\cx`      |              | Control-x                                        |
| `\C-x`     |              | Control-x                                        |
| `\e`       | `0x1b`       | Escape                                           |
| `\f`       | `0x0c`       | 换页                                             |
| `\M-\C-x`  |              | Meta-Control-x                                   |
| `\n`       | `0x0a`       | 新一行                                           |
| `\nnn`     |              | 八进制符号，其中`n`在0.7范围内                   |
| `\r`       | `0x0d`       | 回车返回                                         |
| `\s`       | `0x20`       | 空格                                             |
| `\t`       | `0x09`       | 制表符                                           |
| `\v`       | `0x0b`       | 垂直制表符                                       |
| `\x`       |              | 字符`x`                                          |
| `\xnn`     |              | 十六进制符号，其中`n`在`0~9`，`a~f`或`A~F`范围内 |

### 4.字符串特殊运算符

假设字符串变量`a`保存字符串值’`Hello`‘，变量`b`保存字符串值’`Python`‘，那么 -

| 运算符   | 说明                                                         | 示例                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `+`      | 连接 - 将运算符的两边的值添加                                | `a + b` 结果为 `HelloPython`                                 |
| `*`      | 重复 - 创建新字符串，连接相同字符串的多个副本                | `a*2` 结果为 `HelloHello`                                    |
| `[]`     | 切片 - 给出指定索引中的字符串值，它是原字符串的子串。        | `a[1]` 结果为 `e`                                            |
| `[:]`    | 范围切片 - 给出给定范围内的子字符串                          | `a[1:4]` 结果为 `ell`                                        |
| `in`     | 成员关系 - 如果给定字符串中存在指定的字符，则返回`true`      | `'H' in a` 结果为 `1`                                        |
| `not in` | 成员关系 - 如果给定字符串中不存在指定的字符，则返回`true`    | `'Y' not in a` 结果为 `1`                                    |
| `r/R`    | 原始字符串 - 抑制转义字符的实际含义。原始字符串的语法与正常字符串的格式完全相同，除了原始字符串运算符在引号之前加上字母“`r`”。 “`r`”可以是小写(`r`)或大写(`R`)，并且必须紧靠在第一个引号之前。 | `print(r'\n')` 将打印 `\n` ，或者 `print(R'\n')` 将打印 `\n`，要注意的是如果不加`r`或`R`作为前缀，打印的结果就是一个换行。 |
| `%`      | 格式 - 执行字符串格式化                                      | 请参见本文第5节                                              |

### 5.字符串格式化运算符

Python最酷的功能之一是字符串格式运算符`％`。 这个操作符对于字符串是独一无二的，弥补了C语言中 `printf()`系列函数。 以下是一个简单的例子 -

```python
##!/usr/bin/python3

print ("My name is %s and weight is %d kg!" % ('Maxsu', 71))
Python
```

当执行上述代码时，会产生以下结果 -

```shell
My name is Maxsu and weight is 71 kg!
Shell
```

以下是可以与`%`符号一起使用的完整符号集列表 - 

| 编号 | 格式化符号 | 转换                                  |
| ---- | ---------- | ------------------------------------- |
| 1    | `%c`       | 字符                                  |
| 2    | `%s`       | 在格式化之前通过`str()`函数转换字符串 |
| 3    | `%i`       | 带符号的十进制整数                    |
| 4    | `%d`       | 带符号的十进制整数                    |
| 5    | `%u`       | 无符号十进制整数                      |
| 6    | `%o`       | 八进制整数                            |
| 7    | `%x`       | 十六进制整数(小写字母)                |
| 8    | `%X`       | 十六进制整数(大写字母)                |
| 9    | `%e`       | 指数符号(小写字母’`e`‘)               |
| 10   | `%E`       | 指数符号(大写字母’`E`‘                |
| 11   | `%f`       | 浮点实数                              |
| 12   | `%g`       | `％f`和`％e`                          |
| 13   | `%G`       | `％f`和`％E`                          |

其他支持的符号和功能如下表所列 - 

| 编号 | 符号    | 功能                                                         |
| ---- | ------- | ------------------------------------------------------------ |
| 1    | `*`     | 参数指定宽度或精度                                           |
| 2    | `-`     | 左对齐                                                       |
| 3    | `+`     | 显示标志或符号                                               |
| 4    | `<sp>`  | 在正数之前留空格                                             |
| 5    | `#`     | 根据是否使用“`x`”或“`X`”，添加八进制前导零(‘`0`‘)或十六进制前导’`0x`‘或’`0X`‘。 |
| 6    | `0`     | 使用零作为左边垫符(而不是空格)                               |
| 7    | `%`     | ‘`%%`‘留下一个文字“`%`”                                      |
| 8    | `(var)` | 映射变量(字典参数)                                           |
| 9    | `m.n.`  | `m`是最小总宽度，`n`是小数点后显示的位数(如果应用)           |

### 6.三重引号

Python中的三重引号允许字符串跨越多行，包括逐字记录的新一行，`TAB`和任何其他特殊字符。

三重引号的语法由三个连续的单引号或双引号组成。

```shell
##!/usr/bin/python3

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)
Shell
```

当执行上述代码时，会产生以下结果。注意每个单独的特殊字符如何被转换成其打印形式，它是直到最后一个`NEWLINEs`在“`up`”之间的字符串的末尾，并关闭三重引号。 另请注意，`NEWLINEs`可能会在一行或其转义码(`\n`)的末尾显式显示回车符 -

```shell
this is a long string that is made up of
several lines and non-printable characters such as
TAB (    ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [
 ], or just a NEWLINE within
the variable assignment will also show up.
Shell
```

原始字符串根本不将反斜杠视为特殊字符。放入原始字符串的每个字符都保持所写的方式 -

```python
##!/usr/bin/python3

print ('C:\\nowhere')
Python
```

当执行上述代码时，会产生以下结果 -

```shell
C:\nowhere
Shell
```

现在演示如何使用原始的字符串。将表达式修改为如下 -

```shell
##!/usr/bin/python3

print (r'C:\\nowhere')
Shell
```

当执行上述代码时，会产生以下结果 -

```shell
C:\\nowhere
Shell
```

### 7.Unicode字符串

在*Python 3*中，所有的字符串都用Unicode表示。在*Python 2*内部存储为`8`位ASCII，因此需要附加’`u`‘使其成为*Unicode*，而现在不再需要了。

**内置字符串方法**

Python包括以下内置方法来操作字符串 -

| 编号 | 方法                                                         | 说明                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [capitalize()](http://www.yiibai.com/python/string_capitalize.html) | 把字符串的第一个字母转为大写                                 |
| 2    | [center(width, fillchar)](http://www.yiibai.com/python/string_center.html) | 返回使用`fillchar`填充的字符串，原始字符串以总共`width`列为中心。 |
| 3    | [count(str, beg = 0,end = len(string))](http://www.yiibai.com/python/string_count.html) | 计算字符串中出现有多少次`str`或字符串的子字符串(如果开始索引`beg`和结束索引`end`,则在`beg`~`end`范围匹配)。 |
| 4    | [decode(encoding = ‘UTF-8’,errors = ‘strict’)](http://www.yiibai.com/python/string_decode.html) | 使用编码`encoding`解码该字符串。 编码默认为默认字符串`encoding`。 |
| 5    | [encode(encoding = ‘UTF-8’,errors = ‘strict’)](http://www.yiibai.com/python/string_encode.html) | 返回字符串的编码字符串版本; 在错误的情况下，默认是抛出`ValueError`，除非使用’`ignore`‘或’`replace`‘给出错误。 |
| 6    | [endswith(suffix, beg = 0, end = len(string))](http://www.yiibai.com/python/string_endswith.html "endswith(suffix, beg = 0, end = len(string) | 确定字符串或字符串的子字符串(如果启动索引结束和结束索引结束)都以后缀结尾; 如果是则返回`true`，否则返回`false`。 |
| 7    | [expandtabs(tabsize = 8)](http://www.yiibai.com/python/string_expandtabs.html) | 将字符串中的制表符扩展到多个空格; 如果没有提供`tabize`，则默认为每个制表符为`8`个空格。 |
| 8    | [find(str, beg = 0 end = len(string))](http://www.yiibai.com/python/string_find.html) | 如果索引`beg`和结束索引`end`给定，则确定`str`是否在字符串或字符串的子字符串中，如果找到则返回索引，否则为`-1`。 |
| 9    | [index(str, beg = 0, end = len(string))](http://www.yiibai.com/python/string_index.html) | 与`find()`相同，但如果没有找到`str`，则引发异常。            |
| 10   | [isalnum()](http://www.yiibai.com/python/string_isalnum.html) | 如果字符串至少包含`1`个字符，并且所有字符均为数字，则返回`true`，否则返回`false`。 |
| 11   | [isalpha()](http://www.yiibai.com/python/string_isalpha.html) | 如果字符串至少包含`1`个字符，并且所有字符均为字母，则返回`true`，否则返回`false`。 |
| 12   | [isdigit()](http://www.yiibai.com/python/string_isdigit.html) | 如果字符串只包含数字则返回`true`，否则返回`false`。          |
| 13   | [islower()](http://www.yiibai.com/python/string_islower.html) | 如果字符串至少包含`1`个字母，并且所有字符均为小写，则返回`true`，否则返回`false`。 |
| 14   | [isnumeric()](http://www.yiibai.com/python/string_isnumeric.html) | 如果`unicode`字符串只包含数字字符，则返回`true`，否则返回`false`。 |
| 15   | [isspace()](http://www.yiibai.com/python/string_isspace.html) | 如果字符串只包含空格字符，则返回`true`，否则返回`false`。    |
| 16   | [istitle()](http://www.yiibai.com/python/string_istitle.html) | 如果字符串正确“标题大小写”，则返回`true`，否则返回`false`。  |
| 17   | [isupper()](http://www.yiibai.com/python/string_isupper.html) | 如果字符串至少包含一个可变大小写字符，并且所有可变大小写字符均为大写，则返回`true`，否则返回`false`。 |
| 18   | [join(seq)](http://www.yiibai.com/python/string_join.html)   | 将序列`seq`中的元素以字符串表示合并(并入)到具有分隔符字符串的字符串中。 |
| 19   | [len(string)](http://www.yiibai.com/python/string_len.html)  | 返回字符串的长度                                             |
| 20   | [ljust(width[, fillchar\])](http://www.yiibai.com/python/string_ljust.html) | 返回一个空格填充的字符串，原始字符串左对齐到总共`width`列。  |
| 21   | [lower()](http://www.yiibai.com/python/string_lower.html)    | 将字符串中的所有大写字母转换为小写。                         |
| 22   | [lstrip()](http://www.yiibai.com/python/string_lstrip.html)  | 删除字符串中的所有前导空格                                   |
| 23   | [maketrans()](http://www.yiibai.com/python/string_maketrans.html) | 返回在`translate`函数中使用的转换表。                        |
| 24   | [max(str)](http://www.yiibai.com/python/string_max.html)     | 从字符串`str`返回最大字母字符。                              |
| 27   | [replace(old, new [, max\])](http://www.yiibai.com/python/string_replace.html) | 如果给定`max`值，则用`new`或最多最大出现替换字符串中所有出现的旧字符(`old`)。 |
| 28   | [rindex( str, beg = 0, end = len(string))](http://www.yiibai.com/python/string_rindex.html) | 与`index()`相同，但在字符串中向后搜索。                      |
| 29   | [rjust(width,[, fillchar\])](http://www.yiibai.com/python/string_rjust.html) | 返回一个空格填充字符串，原始字符串右对齐到总共宽度(`width`)列。 |
| 30   | [rstrip()](http://www.yiibai.com/python/string_rstrip.html)  | 删除字符串的所有尾随空格。                                   |
| 31   | [split(str=](http://www.yiibai.com/python/string_split.html) | 根据分隔符`str`(空格，如果没有提供)拆分字符串并返回子字符串列表; 如果给定，最多分割为`num`子串。 |
| 32   | [splitlines( num=string.count(‘\n’))](http://www.yiibai.com/python/string_startswith.html))”) | 全部拆分字符串(或`num`)新行符，并返回每行的列表，并删除新行符。 |
| 33   | [startswith(str, beg=0,end=len(string))](http://www.yiibai.com/python/string_startswith.html) | 确定字符串或字符串的子字符串(如果给定起始索引`beg`和结束索引`end`)以`str`开头; 如果是则返回`true`，否则返回`false`。 |
| 34   | [strip([chars\])](http://www.yiibai.com/python/string_strip.html) | 对字符串执行`lstrip()`和`rstrip()`                           |
| 35   | [swapcase()](http://www.yiibai.com/python/string_swapcase.html) | 反转在字符串中的所有字母大小写，即小写转大写，大写转小写。   |
| 36   | [title()](http://www.yiibai.com/python/string_title.html)    | 返回字符串的标题版本，即所有单词第一个字母都以大写开头，其余的都是小写的。 |
| 37   | [translate(table, deletechars=](http://www.yiibai.com/python/string_translate.html) | 根据转换表STR(256个字符)，除去那些在`del`字符串转换字符串。  |
| 38   | [upper()](http://www.yiibai.com/python/string_upper.html)    | 将字符串中的小写字母转换为大写。                             |
| 39   | [zfill(width)](http://www.yiibai.com/python/string_zfill.html) | 返回原始字符串，左边填充为零，总共有宽度(`width`)字符; 对于数字`zfill()`保留给定的任何符号(少于一个零)。 |
| 40   | [isdecimal() ](http://www.yiibai.com/python/string_isdecimal.html) | 如果unicode字符串只包含十进制字符，则返回`true`，否则返回`false`。 |

### 第十节 Python列表

Python中最基本的数据结构是列表。一个列表的每个元素被分配一个数字来表示它的位置或索引。 第一个索引为`0`，第二个索引为`1`，依此类推。

Python有六种内置的序列类型，但最常见的是列表和元组，将在本教程中看到。

可以在列表上执行各种类型操作。这些操作包括索引，切片，添加，乘法和检查成员身份。此外，Python还具有内置函数，用于查找序列的长度和查找其最大和最小的元素。

### 1.Python列表

列表是Python中最通用的数据类型，可以写成方括号之间的逗号分隔值(项)列表。列表中的项目不必是相同的类型，这一点和C语言中数组有差别。

创建列表就在方括号之间放置不同的逗号分隔值。 例如 -

```python
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];
Python
```

类似于字符串索引，列表索引从`0`开始，列表可以被切片，连接等等。

### 2.访问列表中的值

要访问列表中的值，使用方括号进行切片以及索引或索引，以获取该索引处可用的值。例如 -

```python
##!/usr/bin/python3

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
Python
```

当执行上述代码时，会产生以下结果 -

```python
list1[0]:  physics
list2[1:5]:  [2, 3, 4, 5]
Python
```

### 3.更新列表

可以通过在分配运算符左侧给出切片来更新列表的单个或多个元素，可以使用`append()`方法添加到列表中的元素。例如 -

```python
##!/usr/bin/python3

list = ['physics', 'chemistry', 1997, 2000]
print ("Value available at index 2 : ", list[2])

list[2] = 2001
print ("New value available at index 2 : ", list[2])
Python
```

> **注** - 在后续章节中讨论了`append()`方法。

当执行上述代码时，会产生以下结果 -

```shell
Value available at index 2 :  1997
New value available at index 2 :  2001
Shell
```

### 4.删除列表元素

要删除列表元素，并且如果确切知道要删除哪些元素可以使用`del`语句。如果不知道要删除哪些项目，可以使用`remove()`方法。 例如 -

```python
##!/usr/bin/python3
list = ['physics', 'chemistry', 1997, 2000]

print (list)
del list[2]
print ("After deleting value at index 2 : ", list)
Python
```

当执行上述代码时，会产生以下结果 -

```python
['physics', 'chemistry', 1997, 2000]
After deleting value at index 2 :  ['physics', 'chemistry', 2000]
Python
```

> 注 - `remove()`方法将在后续章节中讨论。

### 基本列表操作

列表响应`+`和`*`运算符，这与字符串十分类似; 它们也意味着这里的连接和重复，除了结果是新的列表，而不是字符串。

事实上，列表响应上一章中，在字符串上使用的所有常规序列操作。

| Python表达式                             | 结果                           | 描述       |
| ---------------------------------------- | ------------------------------ | ---------- |
| `len([1, 2, 3])`                         | 3                              | 列表的长度 |
| `[1, 2, 3] + [4, 5, 6]`                  | `[1, 2, 3, 4, 5, 6]`           | 联接       |
| `['Hi!'] * 4`                            | `['Hi!', 'Hi!', 'Hi!', 'Hi!']` | 重复       |
| `3 in [1, 2, 3]`                         | `True`                         |            |
| `for x in [1,2,3] : print (x,end = ' ')` | `1 2 3`                        | 迭代       |

### 索引，切片和矩阵

由于列表是序列，索引和切片的工作方式与列表一样，对于字符串。

假设以下输入 -

```python
L = ['C++'', 'Java', 'Python']
Python
```

| Python表达式 | 结果                 | 描述             |
| ------------ | -------------------- | ---------------- |
| `L[2]`       | `'Python'`           | 偏移量，从零开始 |
| `L[-2]`      | `'Java'`             | 负数：从右到右   |
| `L[1:]`      | `['Java', 'Python']` | 切片提取部分     |

### 内置列表函数和方法

Python包括以下列表函数功能 -

| 编号 | 方法                                                         | 描述                       |
| ---- | ------------------------------------------------------------ | -------------------------- |
| 1    | [cmp(list1, list2)](http://www.yiibai.com/python/list_cmp.html) | 在*Python 3*中不再可用。   |
| 2    | [len(list)](http://www.yiibai.com/python/list_len.html)      | 给出列表的总长度。         |
| 3    | [max(list)](http://www.yiibai.com/python/list_max.html)      | 从列表中返回最大值的项目。 |
| 4    | [min(list)](http://www.yiibai.com/python/list_min.html)      | 从列表中返回最小值的项目。 |
| 5    | [list(seq)](http://www.yiibai.com/python/list_list.html)     | 将元组转换为列表。         |

Python包括以下列表方法 -

| 编号 | 方法                                                         | 描述                                                 |
| ---- | ------------------------------------------------------------ | ---------------------------------------------------- |
| 1    | [list.append(obj)](http://www.yiibai.com/python/list_append.html) | 将对象`obj`追加到列表中                              |
| 2    | [list.count(obj)](http://www.yiibai.com/python/list_count.html) | 返回列表中出现多少次`obj`的计数                      |
| 3    | [list.extend(seq)](http://www.yiibai.com/python/list_count.html) | 返回列表中出现多少次`obj`的计数                      |
| 4    | [list.extend(seq)](http://www.yiibai.com/python/list_extend.html) | 将`seq`的内容附加到列表中                            |
| 5    | [list.insert(index, obj)](http://www.yiibai.com/python/list_insert.html) | 将对象`obj`插入到偏移索引的列表中                    |
| 6    | [list.pop(obj = list[-1\])](http://www.yiibai.com/python/list_pop.html) | 从列表中删除并返回最后一个对象或`obj`                |
| 7    | [list.remove(obj)](http://www.yiibai.com/python/list_remove.html) | 从列表中删除对象`obj`                                |
| 8    | [list.reverse()](http://www.yiibai.com/python/list_reverse.html) | 反转列表中的对象                                     |
| 9    | [list.sort([func\])](http://www.yiibai.com/python/list_sort.html) | 排序列表的对象，如果给出，则使用比较函数`func`来排序 |

### 第十一节 Python元组

元组是一系列不可变的Python对象。元组是一种序列，就像列表一样。元组和列表之间的主要区别是元组不能像列表那样改变元素的值，可以简单地理解为“只读列表”。 元组使用小括号 - `()`，而列表使用方括号 - `[]` 。

创建一个元组只需使用逗号分隔值放入小括号的一个序列。 或者，也可以将这些逗号分隔值放在括号之间。 例如 -

```python
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
Python
```

空的元组写成两个不含任何东西的小括号 -

```python
tup1 = ();
Python
```

要编写一个包含单个值的元组，必须包含一个逗号，即使只有一个值(这是规范写法) -

```python
tup1 = (50,)
### 也可以这样写
tup2 = (50)
Python
```

### 1.访问元组中的值

要访问元组中的值，请使用方括号进行指定索引切片或索引，以获取该索引处的值。 例如 -

```shell
##!/usr/bin/python3

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
Shell
```

当执行上述代码时，会产生以下结果 -

```python
tup1[0]:  physics
tup2[1:5]:  (2, 3, 4, 5)
Python
```

### 2.更新元组

元组是不可变的，这意味着我们无法更新或更改元组元素的值。 但是可以使用现有元组的一部分来创建新的元组，如下例所示：

```python
##!/usr/bin/python3

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

## Following action is not valid for tuples
## tup1[0] = 100;

## So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)
Python
```

当执行上述代码时，会产生以下结果 -

```shell
(12, 34.56, 'abc', 'xyz')
Shell
```

### 3.删除元组元素

删除单个元组元素是不可能的。 当然，将不必要的元素放在另一个元组中也没有什么错。

要显式删除整个元组，只需使用`del`语句。 例如 -

```python
##!/usr/bin/python3

tup = ('physics', 'chemistry', 1997, 2000);

print (tup)
del tup;
print "After deleting tup : "
print (tup)
Python
```

执行上面代码，将产生以下结果 - 

> 注 - 引发异常。这是因为在`del tup`之后，元组不再存在。

```shell
('physics', 'chemistry', 1997, 2000)
After deleting tup :
Traceback (most recent call last):
   File "test.py", line 9, in <module>
      print tup;
NameError: name 'tup' is not defined
Shell
```

### 4.基本元组操作

元组响应`+`和`*`运算符很像字符串; 它们执行连接和重复操作，但结果是一个新的元组，而不是一个字符串。

事实上，元组中类似字符串操作和使用的所有常规序列操作都有作了讲解。

| Python表达式                              | 结果                           | 描述     |
| ----------------------------------------- | ------------------------------ | -------- |
| `len((1, 2, 3))`                          | `3`                            | 长度     |
| `(1, 2, 3) + (4, 5, 6)`                   | `(1, 2, 3, 4, 5, 6)`           | 连接操作 |
| `('Hi!',) * 4`                            | `('Hi!', 'Hi!', 'Hi!', 'Hi!')` | 重复     |
| `3 in (1, 2, 3)`                          | `True`                         | 成员关系 |
| `for x in (1,2,3) : print (x, end = ' ')` | `1 2 3`                        | 迭代     |

### 5.索引，切片和矩阵

由于元组是序列，索引和切片的工作方式与列表的工作方式相同，假设输入以下值：

```python
T=('C++', 'Java', 'Python')
Python
```

那么 - 

| Python表达式 | 结果                 |                  |
| ------------ | -------------------- | ---------------- |
| `T[2]`       | `'Python'`           | 偏移量，从零开始 |
| `T[-2]`      | `'Java'`             | 负数：从右到左   |
| `T[1:]`      | `('Java', 'Python')` | 切片提取部分     |

### 6.内置元组函数功能

Python包括以下元组函数 -

| 编号 | 函数                                                         | 描述                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 1    | [cmp(tuple1, tuple2)](http://www.yiibai.com/python/tuple_cmp.html) | 比较两个元组的元素。 |
| 2    | [len(tuple)](http://www.yiibai.com/python/tuple_len.html)    | 给出元组的总长度。   |
| 3    | [max(tuple)](http://www.yiibai.com/python/tuple_max.html)    | 从元组返回最大值项。 |
| 4    | [min(tuple)](http://www.yiibai.com/python/tuple_min.html)    | 从元组返回最大值项   |
| 5    | [tuple(seq)](http://www.yiibai.com/python/tuple_tuple.html)  | 将列表转换为元组。   |

### 第十二节 Python字典

每个键与其值使用一个冒号(`:`)分开，这些键-值对是使用逗号分隔的，整个字典项目用大括号括起来。 没有任何项目的空字典只用两个花括号写成：`{}`

键在字典中是唯一的，而值可以不必是唯一的。字典的值可以是任何类型的，但是键必须是不可变的数据类型，例如字符串，数字或元组。

### 1.访问字典中的值

要访问字典元素，可以使用熟悉的中括号以及键来获取其值。 以下是一个简单的例子 -

```python
##!/usr/bin/python3

dict = {'Name': 'Maxsu', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
Python
```

当执行上述代码时，会产生以下结果 -

```shell
dict['Name']:  Maxsu
dict['Age']:  7
Shell
```

如果尝试使用键(不是字典的一部分)访问数据项，会收到以下错误，如下示例 -

```python
##!/usr/bin/python3

dict = {'Name': 'Maxsu', 'Age': 7, 'Class': 'First'}
print ("dict['Minsu']: ", dict['Minsu'])
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Minsu'
Shell
```

### 2.更新字典

可以通过添加新数据项或键值对，修改现有数据项或删除现有数据项来更新字典，如下面给出的简单示例所示。

```python
##!/usr/bin/python3

dict = {'Name': 'Maxsu', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
Python
```

当执行上述代码时，会产生以下结果 -

```shell
dict['Age']:  8
dict['School']:  DPS School
Shell
```

### 3.删除词典元素

可以删除单个字典元素或清除字典的全部内容。也可以在单个操作中删除整个字典。

要显式删除整个字典，只需使用`del`语句。 以下是一个简单的例子 -

```python
##!/usr/bin/python3

dict = {'Name': 'Maxsu', 'Age': 7, 'Class': 'First'}

del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict         # delete entire dictionary

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
Python
```

这产生以下结果：程序抛出了一个例外，因为在执行`del dict`之后，字典不再存在。

```shell
print ("dict['Age']: ", dict['Age'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
>>> print ("dict['School']: ", dict['School'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
Shell
```

> 注 - `del()`方法将在后续章节中讨论。

### 4. 字典键的属性

字典值没有限制。它们可以是任意任意的Python对象，标准对象或用户定义的对象。 但是，对于键来说也是如此。

关于字典的键有两个要点：

**(a)**. 不允许每键多于数据值。这意味着不允许重复的键。 在分配过程中遇到重复键时，则以最后一个赋值为准。 例如 -

```python
##!/usr/bin/python3

dict = {'Name': 'Maxsu', 'Age': 7, 'Name': 'Minlee'}
print ("dict['Name']: ", dict['Name'])
Python
```

当执行上述代码时，会产生以下结果 -

```shell
dict['Name']:  Minlee
Shell
```

**(b)**. 键必须是不可变的。 这意味着可以使用字符串，数字或元组作为字典键，但不允许使用`['key']`。 以下是一个简单的例子 -

```python
##!/usr/bin/python3

dict = {['Name']: 'Maxsu', 'Age': 7}
print ("dict['Name']: ", dict['Name'])
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Traceback (most recent call last):
   File "test.py", line 3, in <module>
      dict = {['Name']: 'Maxsu', 'Age': 7}
TypeError: list objects are unhashable
Shell
```

### 5.内置词典函数和方法

Python包括以下字典函数 -

| 编号 | 函数                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | cmp(dict1, dict2)                                            | 在*Python 3*中不再可用。                                     |
| 2    | [len(dict)](http://www.yiibai.com/python/dictionary_len.html) | 计算出字典的总长度。它将等于字典中的数据项数目。             |
| 3    | [str(dict)](http://www.yiibai.com/python3/dictionary_str.html) | 生成字典的可打印字符串表示形式                               |
| 4    | [type(variable)](http://www.yiibai.com/python/dictionary_type.html) | 返回传递变量的类型。如果传递变量是字典，那么它将返回一个字典类型。 |

Python包括以下字典方法 -

| 编号 | 函数                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [dict.clear()](http://www.yiibai.com/python/dictionary_clear.html) | 删除字典`dict`的所有元素                                     |
| 2    | [dict.copy()](http://www.yiibai.com/python/dictionary_copy.html) | 返回字典`dict`的浅拷贝                                       |
| 3    | [dict.fromkeys()](http://www.yiibai.com/python/dictionary_fromkeys.html) | 创建一个新的字典，其中包含`seq`的值和设置为`value`的值。     |
| 4    | [dict.get(key, default=None)](http://www.yiibai.com/python/dictionary_get.html) | 对于键(`key`)存在则返回其对应值，如果键不在字典中，则返回默认值 |
| 5    | [dict.has_key(key)](http://www.yiibai.com/python/dictionary_has_key.html) | 此方法已删除，使用`in`操作符代替                             |
| 6    | [dict.items()](http://www.yiibai.com/python/dictionary_items.html) | 返回字典`dict`的`(key，value)`元组对的列表                   |
| 7    | [dict.keys()](http://www.yiibai.com/python/dictionary_keys.html) | 返回字典`dict`的键列表                                       |
| 8    | [dict.setdefault(key, default = None)](http://www.yiibai.com/python/dictionary_setdefault.html) | 类似于`get()`，如果`key`不在字典`dict`中，则将执行赋值操作：`dict [key] = default` |
| 9    | [dict.update(dict2)](http://www.yiibai.com/python/dictionary_update.html) | 将字典`dict2`的键值对添加到字典`dict`                        |
| 10   | [dict.values()](http://www.yiibai.com/python/dictionary_values.html) | 返回字典`dict`的值列表                                       |

### 第十三节 Python日期和时间

Python程序可以通过多种方式处理日期和时间。日期格式之间的转换是计算机常见问题。Python的时间(`time`)和日历(`calendar`)模块可用于跟踪日期和时间。

#### 一些常用代码示例

- [获取当前时间和日期](http://www.yiibai.com/python/python_between_days.html)，如：2018-08-18 12：12：00
- [计算两个日期相差天数](http://www.yiibai.com/python/python_between_days.html)
- 计算程序运行的时间

```python
##!/usr/bin/python3
##coding=utf-8

import time  
import datetime  

starttime = datetime.datetime.now()  

time.sleep(5)  

endtime = datetime.datetime.now()  
print ((endtime - starttime).seconds )
Python
```

- 计算十天之后的日期时间

```python
##!/usr/bin/python3
##coding=utf-8

import time  
import datetime  

d1 = datetime.datetime.now()  
d3 = d1 + datetime.timedelta(days =10)  

print (str(d3))
print (d3.ctime())
Python
```

- 获取两个日期时间的时间差

```python
t = (datetime.datetime(2019,1,13,12,0,0) - datetime.datetime.now()).total_seconds()
print ("t = ", t)
### 输出结果
t = 49367780.076406
Python
```

Python中有提供与日期和时间相关的`4`个模块。它们分别是 - 

| 模块       | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| `time`     | `time`是一个仅包含与日期和时间相关的函数和常量的模块，在本模块中定义了`C/C++`编写的几个类。 例如，`struct_time`类。 |
| `datetime` | `datetime`是一个使用面向对象编程设计的模块，可以在Python中使用日期和时间。它定义了几个表示日期和时间的类。 |
| `calendar` | 日历是一个提供函数的模块，以及与`Calendar`相关的几个类，它们支持将日历映像生成为text，html，…. |
| `locale`   | 该模块包含用于格式化或基于区域设置分析日期和时间的函数。     |

### 1. 时间间隔

时间间隔是以秒为单位的浮点数。 从1970年1月1日上午12:00(*epoch*)，这是一种时间的特殊时刻表示。

在Python中，当前时刻与上述特殊的某个时间点之间以秒为单位的时间。这个时间段叫做Ticks。

![img](E:\git\python3-noteboook\python3教程.assets\700100641_71063.png)

`time`模块中的`time()`函数返回从1970年1月1日上午12点开始的秒数。

```python
## Import time module.
import time;

## Seconds
ticks = time.time()


print ("Number of ticks since 12:00am, January 1, 1970: ", ticks)
Python
```

执行上面代码，得到以下结果 - 

```shell
Number of ticks since 12:00am, January 1, 1970:  1497970093.6243818
Shell
```

但是，这个形式不能表示在时代(*1970年1月1日上午12:00*)之前的日期。在未来的日子也不能以这种方式表示 - 截止点是在`2038`年的UNIX和Windows的某个时刻。

### 2. 什么是TimeTuple？

许多Python时间函数将时间处理为`9`个数字的元组，如下所示：

| 索引 | 字段              | 值                        |
| ---- | ----------------- | ------------------------- |
| 0    | `4`位数，表示年份 | 2018，2019…               |
| 1    | 月份              | 1 ~ 12                    |
| 2    | 日期              | 1 ~ 31                    |
| 3    | 小时              | 0 ~ 23                    |
| 4    | 分钟              | 0 ~ 59                    |
| 5    | 秒                | 0 ~ 61(`60`或`61`是闰秒)  |
| 6    | 星期几            | 0 ~ 6(`0`是星期一)        |
| 7    | 一年的第几天      | 1 ~ 366(朱利安日)         |
| 8    | 夏令时            | -1，0，1，-1表示库确定DST |

**一个示例**

```python
import time
print (time.localtime());
Python
```

这将产生如下结果：

```shell
time.struct_time(tm_year = 2016, tm_mon = 2, tm_mday = 15, tm_hour = 9, 
   tm_min = 29, tm_sec = 2, tm_wday = 0, tm_yday = 46, tm_isdst = 0)
Shell
```

上面的元组相当于`struct_time`结构。此结构具有以下属性 -

| 索引 | 字段     | 值                        |
| ---- | -------- | ------------------------- |
| 0    | tm_year  | 2018，2019…               |
| 1    | tm_mon   | 1 ~ 12                    |
| 2    | tm_mday  | 1 ~ 31                    |
| 3    | tm_hour  | 0 ~ 23                    |
| 4    | tm_min   | 0 ~ 59                    |
| 5    | tm_sec   | 0 ~ 61(`60`或`61`是闰秒)  |
| 6    | tm_wday  | 0 ~ 6(`0`是星期一)        |
| 7    | tm_yday  | 1 ~ 366(朱利安日)         |
| 8    | tm_isdst | -1，0，1，-1表示库确定DST |

能用图片说明白的尽量用图片说明 - 

![img](E:\git\python3-noteboook\python3教程.assets\852100659_39889.png)

#### 2.1.获取当前时间

要将从时间浮点值开始的秒数瞬间转换为时间序列，将浮点值传递给返回具有所有有效九个项目的时间元组的函数(例如本地时间)。

```python
##!/usr/bin/python3
import time

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

## 当前时间
curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print (curtime)
Python
```

执行上面代码，这将产生如下结果 - 

```shell
Local current time : time.struct_time(tm_year=2017, tm_mon=6, tm_mday=20, tm_hour=23,
tm_min=9, tm_sec=36, tm_wday=1, tm_yday=171, tm_isdst=0)
Curtime is =>  2017-06-20 23:09:36
Shell
```

#### 2.2.获取格式化时间

可以根据需要格式化任何时间，但也可使用可读格式获取时间的简单方法是 - `asctime()` -

```python
##!/usr/bin/python3
import time

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
Python
```

执行上面代码，这将产生如下结果 - 

```shell
Local current time : Mon Feb 15 10:32:13 2018
Shell
```

#### 2.3.获取一个月的日历

`calendar`模块提供了广泛的方法来显示年历和月度日历。 在这里，将打印一个给定月份的日历(2021年11月) -

```python
##!/usr/bin/python3
import calendar

cal = calendar.month(2021, 11)
print ("Here is the calendar:")
print (cal)
Python
```

执行上面代码后，将输出以下结果 - 

```shell
   November 2021
Mo Tu We Th Fr Sa Su 
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
Shell
```

### 3.时间模块

Python中有一个受欢迎的时间(`time`)模块，它提供了处理时间和表示之间转换的功能。以下是所有时间(`time`)可用方法的列表。

| 编号 | 方法                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [time.altzone](http://www.yiibai.com/python/time_altzone.html) | 本地DST时区的偏移量(以秒为单位的UTC)，如果定义了有一个定义的话。 如果本地的DST时区是UTC的东部(如在西欧，包括英国)，那么它是负数值。 |
| 2    | [time.asctime([tupletime\])](http://www.yiibai.com/python/time_asctime.html) | 接受时间元组，并返回一个可读的`24`个字符的字符串，例如’Tue Dec 11 22:07:14 2019’。 |
| 3    | [time.clock( )](http://www.yiibai.com/python/time_clock.html) | 将当前CPU时间返回为浮点数秒。 为了测量不同方法的计算成本，`time.clock`的值比`time.time()`的值更有用。 |
| 4    | [time.ctime([secs\])](http://www.yiibai.com/python/time_ctime.html) | 类似于`asctime(localtime(secs))`，而没有参数就像`asctime()`  |
| 5    | [time.gmtime([secs\])](http://www.yiibai.com/python/time_gmtime.html) | 接受从时代(*epoch*)以秒为单位的瞬间，并返回与UTC时间相关的时间元组`t`。 注 - `t.tm_isdst`始终为`0` |
| 6    | [time.localtime([secs\])](http://www.yiibai.com/python/time_localtime.html) | 接受从时代(*epoch*)以秒为单位的瞬间，并返回与本地时间相关的时间`t`(`t.tm_isdst`为`0`或`1`，具体取决于DST是否适用于本地规则的瞬时秒)。 |
| 7    | [time.mktime(tupletime)](http://www.yiibai.com/python/time_mktime.html) | 接受在本地时间表示为时间元组的瞬间，并返回浮点值，该时间点以秒为单位表示。 |
| 8    | [time.sleep(secs)](http://www.yiibai.com/python/time_sleep.html) | 暂停调用线程`secs`秒。                                       |
| 9    | [time.strftime(fmt[,tupletime\])](http://www.yiibai.com/python/time_strftime.html) | 接受在本地时间表示为时间元组的瞬间，并返回一个表示由字符串`fmt`指定的时间的字符串。 |
| 10   | [time.strptime(str,fmt = ‘%a %b %d %H:%M:%S %Y’)](http://www.yiibai.com/python/time_strptime.html)“) | 根据格式字符串`fmt`解析`str`，并返回时间元组格式的时间。     |
| 11   | [time.time( )](http://www.yiibai.com/python/time_time.html)  | 返回当前时间时刻，即从时代(*epoch*)开始的浮点数秒数。        |
| 12   | [time.tzset()](http://www.yiibai.com/python/time_tzset.html) | 重置库例程使用的时间转换规则。环境变量`TZ`指定如何完成。     |

时间(`time`)模块有两个重要的属性可用。它们是 -

| 编号 | 属性            | 描述                                                         |
| ---- | --------------- | ------------------------------------------------------------ |
| 1    | `time.timezone` | 属性`time.timezone`是UTC和本地时区(不含DST)之间的偏移量(美洲为 > `0`，欧洲，亚洲，非洲大部分地区为 `0`)。 |
| 2    | `time.tzname`   | 属性`time.tzname`是一对与区域相关的字符串，它们分别是没有和具有DST的本地时区的名称。 |

### 4.日历模块

`calendar`模块提供与日历相关的功能，包括为给定的月份或年份打印文本日历的功能。

默认情况下，日历将星期一作为一周的第一天，将星期日作为最后一天。 如果想要更改这个，可调用`calendar.setfirstweekday()`函数设置修改。

以下是`calendar`模块可用的功能函数列表 -

| 编号 | 函数                                        | 描述                                                         |
| ---- | ------------------------------------------- | ------------------------------------------------------------ |
| 1    | `calendar.calendar(year,w = 2,l = 1,c = 6)` | 返回一个具有年份日历的多行字符串格式化为三列，以`c`个空格分隔。 `w`是每个日期的字符宽度; 每行的长度为`21 * w + 18 + 2 * c`，`l`是每周的行数。 |
| 2    | `calendar.firstweekday( )`                  | 返回当前设置每周开始的星期。默认情况下，当日历首次导入时设置为：`0`，表示为星期一。 |
| 3    | `calendar.isleap(year)`                     | 如果给定年份(`year`)是闰年则返回`True`; 否则返回：`False`。  |
| 4    | `calendar.leapdays(y1,y2)`                  | 返回在范围`(y1，y2)`内的年份中的闰年总数。                   |
| 5    | `calendar.month(year,month,w = 2,l = 1)`    | 返回一个多行字符串，其中包含年份月份的日历，每周一行和两个标题行。 `w`是每个日期的字符宽度; 每行的长度为`7 * w + 6`。 `l`是每周的行数。 |
| 6    | `calendar.monthcalendar(year,month)`        | 返回`int`类型的列表。每个子列表表示一个星期。年份月份以外的天数设置为`0`; 该月内的日期设定为月份的第几日：1 ~ 31。 |
| 7    | `calendar.monthrange(year,month)`           | 返回两个整数。第一个是年度月(`month`)的星期几的代码; 第二个是当月的天数。表示星期几为`0`(星期一)至`6`(星期日); 月份是`1`到`12`。 |
| 8    | `calendar.prcal(year,w = 2,l = 1,c = 6)`    | 类似于：`calendar.calendar(year，w，l，c)`的打印。           |
| 9    | `calendar.prmonth(year,month,w = 2,l = 1)`  | 类似于：`calendar.month(year,month,w,l)`的打印。             |
| 10   | `calendar.setfirstweekday(weekday)`         | 将每周的第一天设置为星期几的代码。 星期几的代码为`0`(星期一)至`6`(星期日)。 |
| 11   | `calendar.timegm(tupletime)`                | `time.gmtime`的倒数：以时间元组的形式接受时刻，并返回与从时代(`epoch`)开始的浮点数相同的时刻。 |
| 12   | `calendar.weekday(year,month,day)`          | 返回给定日期的星期几的代码。星期几的代码为`0`(星期一)至`6`(星期日); 月数是`1`(1月)到`12`(12月)。 |

### 5.其他模块和功能

如果您有兴趣，那么可以在Python中找到其他重要的模块和功能列表，其中包含日期和时间。以下列出其它有用的模块 -

- `datetime`模块
- `pytz`模块
- `dateutil`模块

### 第十四节  Python函数

函数是一个有组织，可重复使用的代码块，用于执行单个相关操作。 函数为应用程序提供更好的模块化和高度的代码重用。

我们知道，Python中也有给很多内置的函数，如`print()`等，但用户也可以创建自己的函数。这样的函数称为用户定义函数。

### 1.定义函数

可以定义提供所需函数的功能。 以下是在Python中定义函数的简单规则。

- 函数块以关键字`def`开头，后跟函数名和小括号(`()`)。
- 任何输入参数或参数应放置在这些小括号中。也可以在这些小括号内定义参数。
- 每个函数中的代码块以冒号(`:`)开始，并缩进。
- 函数内的第一个语句可以是可选语句 - 函数的文档或`docstring`字符串。
- 语句`return [expression]`用于退出一个函数，可选地将一个表达式传回给调用者。如果没有使用参数的`return`语句，则它与`return None`相同。

**语法**

```python
def functionname( parameters ):
    "function_docstring"
    function_suite
    return [expression]
Python
```

默认情况下，参数具有位置行为，您需要按照定义的顺序通知它们或调用它们。

**示例**

以下函数将字符串作为输入参数，并在标准屏幕上打印参数的值。

```python
def printme( str ):
    "This prints a passed string into this function"
    print (str)
    return
Python
```

### 2.调用函数

定义一个函数需要为它起一个名字，指定要包括在函数中的参数并构造代码块。
当函数的基本结构完成，可以通过从另一个函数调用它或直接从Python提示符执行它。 以下是一个调用`print_str()`函数的例子 -

```python
##!/usr/bin/python3

## Function definition is here
def print_str( str ):
   "This prints a passed string into this function"
   print (str)
   return

## Now you can call print_str function
print_str("This is first call to the user defined function!")
print_str("Again second call to the same function")
Python
```

当执行上述代码时，会产生以下结果 -

```shell
This is first call to the user defined function!
Again second call to the same function
Shell
```

### 3.通过引用与通过值传递

Python语言中的所有参数(参数)都将通过引用传递。如果在函数中更改参数所指的内容，则更改也会反映在调用函数的外部。 例如 -

```python
##!/usr/bin/python3

## Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   print ("Values inside the function before change: ", mylist)
   mylist[2]=50
   print ("Values inside the function after change: ", mylist)
   return

## Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)
Python
```

在这里，将保持对传递对象的引用并在相同的对象中赋值。 因此，这将产生以下结果 -

```shell
Values inside the function before change:  [10, 20, 30]
Values inside the function after change:  [10, 20, 50]
Values outside the function:  [10, 20, 50]
Shell
```

在上面的输出结果中，可以清楚地看到，`mylist[2]`的值原来只在函数内赋了一个值：`50`，但在函数外部的最后一个语句打出来的值是：`50`，这说明更改也会反映在调用函数的外部。

还有一个例子：参数通过引用传递，引用在被调用函数内被覆盖。

```python
##!/usr/bin/python3
##coding=utf-8

## Function definition is here
def changeme( mylist ):
    "This changes a passed list into this function"
    mylist = [1,2,3,4] # This would assi new reference in mylist
    print ("Values inside the function: ", mylist)
    return

## Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)
Python
```

参数`mylist`是`changeme()`函数的局部变量。在函数中更改`mylist`不影响`mylist`的值。函数执行完成后，最终将产生以下结果 -

```python
Values inside the function:  [1, 2, 3, 4]
Values outside the function:  [10, 20, 30]
Python
```

### 4.函数参数

可以使用以下类型的形式参数来调用函数 - 

- 必需参数
- 关键字参数
- 默认参数
- 可变长度参数

#### 4.1.必需参数

必需参数是以正确的位置顺序传递给函数的参数。这里，函数调用中的参数数量应与函数定义完全一致。

如下示例中，要调用`printme()`函数，则必需要传递一个参数，否则会出现如下语法错误 -

```python
##!/usr/bin/python3

## Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

## 现在要调用函数，但不提供参数
printme()
Python
```

当执行上述代码时，会产生以下结果 -

```python
Traceback (most recent call last):
   File "test.py", line 11, in <module>
      printme();
TypeError: printme() takes exactly 1 argument (0 given)
Python
```

> 提示：在调用 `printme()`函数时，提供一个参数就可以了。如：`printme('Maxsu')` 。

#### 4.2.关键字参数

关键字参数与函数调用有关。 在函数调用中使用关键字参数时，调用者通过参数名称来标识参数。

这允许跳过参数或将其置于无序状态，因为Python解释器能够使用提供的关键字将值与参数进行匹配。还可以通过以下方式对`printme()`函数进行关键字调用 -

```python
##!/usr/bin/python3
##coding=utf-8

## Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

## Now you can call printme function
printme( str = "My string")
Python
```

当执行上述代码时，会产生以下结果 -

```python
My string
Python
```

以下示例给出了更清晰的映射。请注意，参数的顺序并不重要。

```shell
##!/usr/bin/python3
##coding=utf-8

## Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name, "Age: ", age)
   return

## Now you can call printinfo function
printinfo( age = 25, name = "Maxsu" )
printinfo(name = "Minsu", age = 26 )
Shell
```

当执行上述代码时，会产生以下结果 -

```shell
Name:  Maxsu Age:  25
Name:  Minsu Age:  26
Shell
```

#### 4.3.默认参数

如果在该参数的函数调用中没有提供值，则默认参数是一个假设为默认值的参数。 以下示例给出了默认参数的想法，如果未通过，则打印默认年龄(`age`) -

```python
##!/usr/bin/python3
##coding=utf-8

## Function definition is here
def printinfo( name, age = 25 ):
   "This prints a passed info into this function"
   print ("Name: ", name, "Age ", age)
   return

## Now you can call printinfo function
printinfo( age = 22, name = "Maxsu" )
printinfo( name = "Minsu" )
Python
```

当执行上述代码时，会产生以下结果 - 

```shell
Name:  Maxsu Age  22
Name:  Minsu Age  25
Shell
```

#### 4.4.可变长度参数

在定义函数时，可能需要处理更多参数的函数。这些参数被称为可变长度参数，并且不像要求的和默认的参数那样在函数定义中命名。

具有非关键字变量参数的函数的语法如下：

```python
def functionname([formal_args,] *var_args_tuple ):
    "function_docstring"
    function_suite
    return [expression]
Python
```

星号(`*`)放在保存所有非关键字变量参数值的变量名之前。 如果在函数调用期间没有指定额外的参数，则此元组保持为空。以下是一个简单的例子 -

```python
##!/usr/bin/python3
##coding=utf-8

## Function definition is here
def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print ("Output is: ", arg1)
    for var in vartuple:
      print (var, )
    return

## Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Output is:  10
Output is:  70
60
50
Shell
```

### 5.匿名函数

这些函数被称为匿名的，因为它们没有使用`def`关键字以标准方式声明。可以使用`lambda`关键字创建小型匿名函数。

- `Lambda`表单可以接受任意数量的参数，但只能以表达式的形式返回一个值。它们不能包含命令或多个表达式。
- 匿名函数不能直接调用打印，因为`lambda`需要一个表达式。
- `Lambda`函数有自己的本地命名空间，不能访问其参数列表和全局命名空间中的变量。
- 虽然`lambdas`是一个单行版本的函数，但它们并不等同于`C`或`C++`中的内联语句，其目的是通过传递函数来进行堆栈分配。

**语法**

`lambda`函数的语法只包含一个语句，如下所示：

```python
lambda [arg1 [,arg2,.....argn]]:expression
Python
```

以下是一个示例，以显示`lambda`形式的函数如何工作 -

```python
##!/usr/bin/python3

## Function definition is here
sum = lambda arg1, arg2: arg1 + arg2


## Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))
Python
```

当执行上述代码时，会产生以下结果 -

```python
Value of total :  30
Value of total :  40
Python
```

### 6.return语句

`return [expression]`语句退出一个函数，可选地将一个表达式传回给调用者。没有参数的`return`语句与`return None`相同。

下面给出的所有例子都没有返回任何值。可以从函数返回值，如下所示：

```python
##!/usr/bin/python3
##coding=utf-8

## Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total

## Now you can call sum function
total = sum( 10, 20 )
print ("Outside the function : ", total )
Python
```

全部执行上述代码时，会产生以下结果 -

```shell
Inside the function :  30
Outside the function :  30
Shell
```

### 7.变量范围

程序中的所有变量在该程序的所有位置可能无法访问。这取决于在哪里声明一个变量。变量的范围决定了可以访问特定标识符的程序部分。Python中有两个变量的基本范围 -

- 全局变量
- 局部变量

### 8.全局与局部变量

在函数体内定义的变量具有局部作用域，外部定义的变量具有全局作用域。

局部变量只能在它们声明的函数内部访问，而全局变量可以通过所有函数在整个程序体中访问。 当调用一个函数时，它内部声明的变量被带入范围。 以下是一个简单的例子 -

```python
total = 0 # This is global variable.
## Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total

## Now you can call sum function
sum( 10, 20 )
print ("Outside the function global total : ", total )
Python
```

当执行上述代码时，会产生以下结果 -

```python
Inside the function local total :  30
Outside the function global total :  0
Python
```

### 第十五节 Python模块

模块允许逻辑地组织Python代码。 将相关代码分组到一个模块中，使代码更容易理解和使用。 模块是一个具有任意命名属性的Python对象，可以绑定和引用。

简单来说，模块是一个由Python代码组成的文件。模块可以定义函数，类和变量。 模块还可以包括可运行的代码。

**示例**

下面是一个名称为`aname`的模块的Python代码通常位于一个名称为`aname.py`的文件中。以下是一个简单模块的例子：`support.py` -

```python
def print_func( par ):
   print "Hello : ", par
   return
Python
```

### 1.import语句

可以通过在其他Python源文件中执行`import`语句来将任何Python源文件用作模块。导入具有以下语法 -

```python
import module1[, module2[,... moduleN]
Python
```

当解释器遇到导入语句时，如果模块存在于搜索路径中，则导入该模块。搜索路径是导入模块之前解释器搜索的目录的列表。例如，要导入模块`hello.py`，需要将以下命令放在脚本的顶部 -

```python
##!/usr/bin/python3

## Import module support
import support

## Now you can call defined function that module as follows
support.print_func("Maxsu")
Python
```

当执行上述代码时，会产生以下结果 -

```python
Hello : Maxsu
Python
```

不管模块被导入多少次，模块只能加载一次。这样可以防止模块执行重复发生，如果有多个导入。

### 2.from…import语句

Python `from`语句允许将模块中的特定属性导入到当前的命名空间中。 `from...import`具有以下语法 -

```python
from modname import name1[, name2[, ... nameN]]
Python
```

例如，要从模块 `fib` 导入函数`fibonacci`，请使用以下语句 -

```python
##!/usr/bin/python3

## Fibonacci numbers module

def fib(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result
>>> from fib import fib
>>> fib(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Python
```

此语句不会将整个模块`fib`导入到当前命名空间中; 它只是将`fibonacci`从模块`fib`引入导入模块的全局符号表。

### 3.from…import *语句

也可以使用以下`import`语句将模块中的所有名称导入到当前命名空间中 -

```python
from modname import *
Python
```

这提供了将所有项目从模块导入到当前命名空间中的简单方法; 但是，这个说法应该谨慎使用。

### 4.执行模块作为脚本

在模块中，模块的名称(作为字符串)可用作全局变量`__name__`的值。模块中的代码将被执行，就像您导入它一样，但是`__name__`设置为“`__main__`”。

在模块的最后添加这个代码 -

```python
##!/usr/bin/python3

## Fibonacci numbers module

def fib(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result
if __name__ == "__main__":
   f = fib(100)
   print(f)
Python
```

运行上述代码时，将显示以下输出。

```python
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Python
```

### 5.定位模块

当导入模块时，Python解释器将按以下顺序搜索模块 -

- 当前目录。
- 如果没有找到该模块，Python会在shell变量`PYTHONPATH`中搜索每个目录。
- 如果其他所有失败，Python将检查默认路径。 在UNIX上，此默认路径通常是`/usr/local/lib/python3/` 或者 `/usr/sbin/`

模块搜索路径作为`sys.path`变量存储在系统模块`sys`中。`sys.path`变量包含当前目录`PYTHONPATH`和依赖于安装的默认值。

### 6.PYTHONPATH变量

`PYTHONPATH`是一个环境变量，由目录列表组成。 `PYTHONPATH`的语法与shell变量`PATH```的语法相同。

这是一个典型的Windows系统上的`PYTHONPATH` -

```shell
set PYTHONPATH = c:\python34\lib;
Shell
```

这里是UNIX系统的典型`PYTHONPATH` -

```shell
set PYTHONPATH = /usr/local/lib/python
Shell
```

### 7.命名空间和范围

变量是映射到对象的名称(标识符)。 命名空间是变量名(键)及其对应对象(值)的字典。

- Python语句可以访问本地命名空间和全局命名空间中的变量。如果本地和全局变量具有相同的名称，则局部变量会影响全局变量。
- 每个函数都有自己的本地命名空间。 类方法遵循与普通函数相同的范围规则。
- Python对于变量是本地还是全局都进行了有根据的判断。它假定在函数中分配值的任何变量都是本地的。
- 因此，为了将值分配给函数内的全局变量，必须首先使用`global`语句。
- 语句`global VarName`告诉Python `VarName`是一个全局变量。Python停止搜索本地命名空间的变量。

例如，在全局命名空间中定义一个变量`Money`。 在函数`Money`中为`Money`赋值，因此Python将`Money`作为局部变量。

但是，如果在设置之前就访问了本地变量`Money`的值，它会产生一个错误：`UnboundLocalError`。 这里可以通过取消注释`global`语句来解决问题。如下示例代码 - 

```python
##!/usr/bin/python3

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   # global Money
   Money = Money + 1

print (Money)
AddMoney()
print (Money)
Python
```

### 8.dir( )函数

`dir()`内置函数返回一个包含由模块定义的名称的字符串的排序列表。这个列表包含模块中定义的所有模块，变量和函数的名称。 以下是一个简单的例子 -

```python
##!/usr/bin/python3

## Import built-in module math
import time

content = dir(time)

print (content)
Python
```

当执行上述代码时，会产生以下结果 -

```shell
['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__',
'altzone', 'asctime', 'clock', 'ctime', 'daylight', 'get_clock_info', 'gmtime',
'localtime', 'mktime', 'monotonic', 'perf_counter', 'process_time', 'sleep',
'strftime', 'strptime', 'struct_time', 'time', 'timezone', 'tzname']
Shell
```

这里，特殊的字符串变量`__name__`是模块的名称，`__file__`是加载模块的文件名。

### 9.globals()和locals()函数

`globals()`和`locals()`函数可用于返回全局和本地命名空间中的名称，具体取决于它们被调用的位置。

- 如果`locals()`从一个函数中调用，它将返回从该函数本地访问的所有名称。
- 如果从函数中调用`globals()`，它将返回从该函数全局访问的所有名称。

这两个函数的返回类型是字典。 因此，可以使用`keys()`函数提取名称。

### 10.reload()函数

当将模块导入到脚本中时，模块的顶级部分的代码只能执行一次。
因此，如果要重新执行模块中的顶级代码，可以使用`reload()`函数。`reload()`函数再次导入以前导入的模块。 `reload()`函数的语法是这样的 -

```shell
reload(module_name)
Shell
```

这里，`module_name`是要重新加载的模块的名称，而不是包含模块名称的字符串。 例如，要重新加载`hello`模块，请执行以下操作 -

```python
reload(hello)
Python
```

### 11.Python中的包

Python中的包是一个分层文件目录结构，它定义了一个由模块和子包和子子包组成的Python应用程序环境，等等。

在`package`目录中创建两个目录：`pkg`和`pkg2`， 然后分别在这两个目录中创建两个文件：`a.py`和`b.py`。该文件具有以下一行源代码 -

*文件： pkg/a.py* - 

```python
##!/usr/bin/python3
##coding=utf-8
## save file: pkg/a.py
def fun():
    print ("I'm pkg.a.fun() ")
Python
```

*文件： pkg/b.py* - 

```python
##!/usr/bin/python3
##coding=utf-8
## save file: pkg/b.py
def fun():
    print ("I'm pkg.b.fun() ")
Python
```

*文件： pkg2/a.py* - 

```python
##!/usr/bin/python3
##coding=utf-8
## save file: pkg2/a.py
def fun():
    print ("I'm pkg2.a.fun() ")
Python
```

*文件： pkg2/b.py* - 

```python
##!/usr/bin/python3
##coding=utf-8
## save file: pkg2/b.py
def fun():
    print ("I'm pkg2.b.fun() ")
Python
```

在`package`目录中创建一个主程序文件：`main.py`，用于演示如何调用包中的各个文件 - 

```python
##!/usr/bin/python3
##coding=utf-8
## save file: phone/pots.py

import pkg.a as a
import pkg.b as b

import pkg2.a as a2
import pkg2.b as b2

a.fun()
b.fun()

a2.fun()
b2.fun()

import pkg2.a
import pkg2.b

print('----------- another way -----------------')
pkg2.a.fun()
pkg2.b.fun()
Python
```

整个代码的目录如下所示 - 

```shell
package
  |- pkg
      |- __init__.py
      |- a.py
      |- b.py
  |- pkg2
      |- __init__.py
      |- a.py
      |- b.py
Shell
```

当执行上述代码时，会产生以下结果 -

```shell
I'm pkg.a.fun() 
I'm pkg.b.fun() 
I'm pkg2.a.fun() 
I'm pkg2.b.fun() 
----------- another way -----------------
I'm pkg2.a.fun() 
I'm pkg2.b.fun()
Shell
```

在上面的例子中，将每个文件中的一个函数作为示例，但是可以在文件中编写多个函数。还可以在这些文件中定义不同的Python类，然后可以使用这些类来创建包。

### 第十六节 Python文件读写

在本章中将介绍*Python 3*中可用的所有基本文件读取*I/O*功能。有关更多功能，请参考标准Python文档。

### 打印到屏幕

产生输出的最简单方法是使用`print`语句，可以传递零个或多个由逗号分隔的表达式。此函数将传递的表达式转换为字符串，并将结果写入标准输出，如下所示：

```python
##!/usr/bin/python3

print ("Python是世界上最牛逼的语言,", "难道不是吗?")
Python
```

执行上面代码后，将在标准屏幕上产生以下结果 -

```shell
Python是世界上最牛逼的语言, 难道不是吗?
Shell
```

### 从键盘读取输入

*Python 2*有两个内置的函数用于从标准输入读取数据，默认情况下来自键盘。这两个函数分别是：`input()`和`raw_input()`。

在*Python 3*中，不建议使用`raw_input()`函数。 `input()`函数可以从键盘读取数并作为字符串类型，而不管它是否用引号括起来(“或”“)。

```python
>>> x = input("input something:")
input something:yes,input some string
>>> x
'yes,input some string'
>>> x = input("input something:")
input something:1239900
>>> x
'1239900'
>>>
Python
```

### 打开和关闭文件

在前面我们学习读取和写入标准的输入和输出。 现在，来看看如何使用实际的数据文件。Python提供了默认操作文件所必需的基本功能和方法。可以使用文件对象执行大部分文件操作。

#### 打开文件

在读取或写入文件之前，必须使用Python的内置`open()`函数打开文件。此函数创建一个文件对象，该对象将用于调用与其相关联的其他支持方法。

**语法**

```python
file object = open(file_name [, access_mode][, buffering])
Python
```

这里是参数详细信息 -

- *file_name* - `file_name`参数是一个字符串值，指定要访问的文件的名称。
- *access_mode* - `access_mode`确定文件打开的模式，即读取，写入，追加等。可能的值的完整列表如下表所示。 这是一个可选参数，默认文件访问模式为(`r` - 也就是只读)。
- *buffering* - 如果`buffering`值设置为`0`，则不会发生缓冲。 如果缓冲值`buffering`为`1`，则在访问文件时执行行缓冲。如果将缓冲值`buffering`指定为大于`1`的整数，则使用指定的缓冲区大小执行缓冲操作。如果为负，则缓冲区大小为系统默认值(默认行为)。

以下是打开文件使用的模式的列表 -

| 编号 | 模式  | 描述                                                         |
| ---- | ----- | ------------------------------------------------------------ |
| 1    | `r`   | 打开的文件为只读模式。文件指针位于文件的开头，这是默认模式。 |
| 2    | `rb`  | 打开仅用二进制格式读取的文件。文件指针位于文件的开头，这是默认模式。 |
| 3    | `r+`  | 打开读写文件。文件指针放在文件的开头。                       |
| 4    | `rb+` | 以二进制格式打开一个用于读写文件。文件指针放在文件的开头。   |
| 5    | `w`   | 打开仅供写入的文件。 如果文件存在，则覆盖该文件。 如果文件不存在，则创建一个新文件进行写入。 |
| 6    | `wb`  | 打开仅用二进制格式写入的文件。如果文件存在，则覆盖该文件。 如果文件不存在，则创建一个新文件进行写入。 |
| 7    | `w+`  | 打开写入和取读的文件。如果文件存在，则覆盖现有文件。 如果文件不存在，创建一个新文件进行阅读和写入。 |
| 8    | `wb+` | 打开一个二进制格式的写入和读取文件。 如果文件存在，则覆盖现有文件。 如果文件不存在，创建一个新文件进行阅读和写入。 |
| 9    | `a`   | 打开一个文件进行追加。 如果文件存在，则文件指针位于文件末尾。也就是说，文件处于追加模式。如果文件不存在，它将创建一个新文件进行写入。 |
| 10   | `ab`  | 打开一个二进制格式的文件。如果文件存在，则文件指针位于文件末尾。 也就是说，文件处于追加模式。如果文件不存在，它将创建一个新文件进行写入。 |
| 11   | `a+`  | 打开一个文件，用于追加和阅读。 如果文件存在，则文件指针位于文件末尾。 文件以附加模式打开。 如果文件不存在，它将创建一个新文件进行阅读和写入。 |
| 12   | `ab+` | 打开一个二进制格式的附加和读取文件。 如果文件存在，则文件指针位于文件末尾。文件以附加模式打开。如果文件不存在，它将创建一个新文件进行读取和写入。 |

### 文件对象属性

打开一个文件并且有一个文件对象后，可以获得与该文件相关的各种信息。

以下是与文件对象相关的所有属性的列表 -

| 编号 | 属性          | 描述                                        |
| ---- | ------------- | ------------------------------------------- |
| 1    | `file.closed` | 如果文件关闭则返回`true`，否则返回`false`。 |
| 2    | `file.mode`   | 返回打开文件的访问模式。                    |
| 3    | `file.name`   | 返回文件的名称。                            |

> 注意 - *Python 3.x*中不支持`softspace`属性

**示例**

```python
##!/usr/bin/python3

## Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()
Python
```

执行上面代码，这产生以下结果 -

```shell
Name of the file:  foo.txt
Closed or not :  False
Opening mode :  wb
Shell
```

#### close()方法

文件对象的`close()`方法刷新任何未写入的信息并关闭文件对象，之后不能再进行写入操作。
当文件的引用对象重新分配给另一个文件时，Python也会自动关闭一个文件。但使用`close()`方法关闭文件是个好习惯。

**语法**

```python
fileObject.close();
Python
```

**示例**

```python
##!/usr/bin/python3

## Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)

## Close opened file
fo.close()
Python
```

执行上面代码，这产生以下结果 -

```shell
Name of the file:  foo.txt
Shell
```

### 读取和写入文件

文件对象提供了一组访问方法，使代码编写更方便。下面将演示如何使用`read()`和`write()`方法来读取和写入文件。

#### write()方法

`write()`方法将任何字符串写入打开的文件。 重要的是要注意，Python字符串可以是二进制数据，而不仅仅是文本。

`write()`方法不会在字符串的末尾添加换行符(‘`\n`‘)

**语法**

```python
fileObject.write(string);
Python
```

这里，传递参数 - `string` 是要写入打开文件的内容。

**示例**

```
##!/usr/bin/python3

## Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

## Close opend file
fo.close()
```

上述示例将创建一个`foo.txt`文件，并将给定的内容写入到该文件中，最后将关闭文件。 在执行上面语句后，如果打开文件(`foo.txt`)，它将应该以下内容 -

```shell
Python is a great language.
Yeah its great!!
Shell
```

#### read()方法

`read()`方法用于从打开的文件读取一个字符串。 重要的是要注意Python字符串除文本数据外可以是二进制数据。。

**语法**

```python
fileObject.read([count]);
Python
```

这里，传递参数 - `count`是从打开的文件读取的字节数。 该方法从文件的开始位置开始读取，如果`count`不指定值或丢失，则尽可能地尝试读取文件，直到文件结束。

**示例**

下面来一个文件`foo.txt`，这是上面示例中创建的。

```python
##!/usr/bin/python3

## Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

## Close opened file
fo.close()
Python
```

执行上面代码，这产生以下结果 -

```python
Read String is :  Python is
Python
```

### 文件位置

`tell()`方法用于获取文件中的当前位置; 换句话说，下一次读取或写入将发生在从文件开始处之后的多个字节数的位置。

`seek(offset [，from])`方法更改当前文件位置。 `offset`参数表示要移动的字节数。 `from`参数指定要移动字节的引用位置。

如果`from`设置为`0`，则将文件的开头作为参考位置。 如果设置为`1`，则将当前位置用作参考位置。 如果设置为`2`，则文件的末尾将被作为参考位置。

**示例**

下面来一个文件`foo.txt`，这是上面示例中创建的。

```python
##!/usr/bin/python3

## Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

## Check current position
position = fo.tell()
print ("Current file position : ", position)

## Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print ("Again read String is : ", str)

## Close opened file
fo.close()
Python
```

执行上面代码，这产生以下结果 -

```python
Read String is :  Python is
Current file position :  10
Again read String is :  Python is
Python
```

### 重命名和删除文件

Python os模块提供用于执行文件处理操作(如重命名和删除文件)的方法。要使用此模块，需要先将它导入，然后可以调用任何相关的函数。

#### rename()方法

`rename()`方法有两个参数，即当前的文件名和新的文件名。

**语法**

```python
os.rename(current_file_name, new_file_name)
Python
```

**示例**

以下是一个将现有文件`test1.txt`重命名为`test2.txt`的示例 -

```python
##!/usr/bin/python3
import os

## Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )
Python
```

#### remove()方法

使用`remove()`方法并通过提供要删除的文件的名称作为参数来删除文件。

**语法**

```python
os.remove(file_name)
Python
```

**示例**

以下是删除现有文件`test2.txt`的示例 -

```python
##!/usr/bin/python3
import os

## Delete file test2.txt
os.remove("text2.txt")
Python
```

### Python中的目录

所有文件都包含在各种目录中，Python处理目录问题也很容易。 `os`模块有几种方法可以用来创建，删除和更改目录。

#### mkdir()方法

使用`os`模块的`mkdir()`方法在当前目录中创建目录。需要为此方法提供一个参数，指定要创建的目录的名称。

**语法**

```python
os.mkdir("newdir")
Python
```

**示例**

以下是在当前目录中创建一个目录：`test` 的示例 -

```python
##!/usr/bin/python3
import os

## Create a directory "test"
os.mkdir("test")
Python
```

使用`chdir()`方法来更改当前目录。 `chdir()`方法接受一个参数，它是要选择作为当前目录的目录的名称。

**语法**

```python
os.chdir("newdir")
Python
```

**示例**

以下是进入“`/home/newdir`”目录的示例 -

```python
##!/usr/bin/python3
import os

## Changing a directory to "/home/newdir"
os.chdir("/home/newdir")
Python
```

#### getcwd()方法

`getcwd()`方法用于显示当前工作目录。

```python
os.getcwd()
Python
```

**示例**

以下是给出当前目录的一个例子 -

```python
##!/usr/bin/python3
import os

## This would give location of the current directory
os.getcwd()
Python
```

#### rmdir()方法

`rmdir()`方法删除该方法中作为参数传递的目录。删除目录之前，应删除其中的所有内容。

```python
os.rmdir('dirname')
Python
```

**示例**

以下是删除“`/tmp/test`”目录的示例。需要给出目录的完全限定名称，否则将在当前目录中搜索该目录。

```python
##!/usr/bin/python3
import os

## This would  remove "/tmp/test"  directory.
os.rmdir( "/tmp/test"  )
Python
```

### 文件和目录相关方法

有三个重要的来源，它们提供了广泛的实用方法来处理和操作Windows和Unix操作系统上的文件和目录。它们如下 -

- [文件对象和方法](http://www.yiibai.com/python/file_methods.html) - 文件对象提供了操作文件的功能。
- [OS对象和方法](http://www.yiibai.com/python/os_file_methods.html) - 这提供了处理文件和目录的方法。

## Python是什么？

ython是面向对象，高级语言，解释，动态和多用途编程语言。Python易于学习，而且功能强大，功能多样的脚本语言使其对应用程序开发具有吸引力。
Python的语法和动态类型具有其解释性质，使其成为许多领域的脚本编写和快速应用程序开发的理想语言。

Python支持多种编程模式，包括面向对象编程，命令式和函数式编程或过程式编程。

Python几乎无所不能，一些常用的开发领域，如Web编程。这就是为什么它被称为多用途，因为它可以用于网络，企业，3D CAD等软件和系统开发。

在Python中，不需要使用数据类型来声明变量，因为它是动态类型的，所以可以写一个如 `a=10` 来声明一个变量`a`中的值是一个整数类型。

Python使开发和调试快速，因为在python开发中没有包含编译步骤，并且编辑 <-> 测试 <-> 调试循环使用代码开发效率非常高。

Python是一种高级，解释，交互和面向对象的脚本语言。 Python被设计为高度可读性。 它使用英语关键字，而其他语言使用标点符号。它的语法结构比其他语言少。

- **Python是解释型语言** - Python代码在解释器中运行时处理，执行前不需要编译程序。 这与PERL和PHP类似。
- **Python是交动的** - 在Python提示符下面直接和解释器进行交互来编写程序。
- **Python是面向对象的** - Python支持面向对象的风格或编程技术，将代码封装在对象内。
- **Python是一门初学者的语言** - Python是初学者程序员的伟大语言，并支持从简单的文本处理到*WWW*浏览器到游戏的各种应用程序的开发。

## Python的历史

Python由*Guido van Rossum*在八十年代末期和九十年代初在荷兰的数学和计算机科学研究所开发的。

- Python源自许多其他编程语言，包括：*ABC*，*Modula-3*，*C*，*C++*，*Algol-68*，*SmallTalk*和*Unix shell*以及其他脚本语言。
- Python受版权保护。 像Perl一样，Python源代码现在可以在GNU通用公共许可证(GPL)下使用。
- Python现在由研究所的核心开发团队维护，*Guido van Rossum*在指导其进展方面仍然发挥至关重要的作用。
- *Python 1.0* 于1994年11月发布。在2000年，发布了*Python 2.0*。 *Python 2.7.11*是*Python 2*的最新版本。
- 在2008年发布了*Python 3.0*。*Python 3*不向后兼容*Python 2*。*Python 3*的重点是删除重复的编程结构和模块，以便“应该有一个 - 最好只有一个 - 明显的做法“。 在编写本教程时，*Python 3.6.1*是*Python 3*的最新版本。

## Python功能特点

Python编程语言提供了很多功能。Python的功能特点包括 -

- **易于学习** - Python的关键字很少，结构简单，语法清晰。这样可以让学习和使用者快速掌握这门语言。
- **易于阅读** - Python代码更清晰地定义和可见。
- **易于维护** - Python的源代码是相当容易维护的。
- **一个广泛的标准库** - Python的大部分库可在UNIX，Windows和Macintosh使用，它是非常便于移植和跨平台的。
- **交互模式** - Python支持交互式模式，允许交互式测试和调试代码段。
- **可移植** - Python可以在各种硬件平台上运行，并且在所有平台上具有相同的界面。
- **可扩展** - 可以添加低级别的模块到Python解释器。这些模块使程序员能够添加或定制他们的工具以提高效率。
- **数据库支持** - Python提供所有主要商业数据库的接口，可与数据库交互存储数据。
- **GUI编程** - Python支持可以创建和移植到许多系统调用，库和Windows系统的GUI应用程序，如Windows MFC，Macintosh和Unix的X Window系统。
- **可伸缩** - Python提供比shell脚本更好的结构和大型程序的支持。

除了上述功能之外，Python还有很多很好的功能。一些其它的功能特性如下所列 -

- 它支持功能和结构化编程方法以及面向对象编程。
- 它可以用作脚本语言，也可以编译成用于构建大型应用程序的字节码。
- 它提供非常高级的动态数据类型，并支持动态类型检查。
- 它支持自动垃圾收集。
- 它可以轻松地与[C语言](http://www.yiibai.com/cprogramming/)，[C++](http://www.yiibai.com/cplusplus/)，*COM*，*ActiveX*，*CORBA*和[Java](http://www.yiibai.com/java/)集成。

## Python可以开发哪些程序？

Python作为一个整体可以用于任何软件开发领域。下面来看看Python可以应用在哪些领域的开发。如下所列 - 

**1.基于控制台的应用程序**

Python可用于开发基于控制台的应用程序。 例如：*IPython*。

**2.基于音频或视频的应用程序**

Python在多媒体部分开发，证明是非常方便的。 一些成功的应用是：*TimPlayer*，*cplay*等。

**3.3D CAD应用程序**

*Fandango*是一个真正使用Python编写的应用程序，提供CAD的全部功能。

**4.Web应用程序**

Python也可以用于开发基于Web的应用程序。 一些重要的开发案例是：*PythonWikiEngines*，*Pocoo*，*PythonBlogSoftware*等，如国内的成功应用案例有：豆瓣，知乎等。

**5.企业级应用**

Python可用于创建可在企业或组织中使用的应用程序。一些实时应用程序是：*OpenErp*，*Tryton*，*Picalo*等。

**6.图像应用**

使用Python可以开发图像应用程序。 开发的应用有：VPython，Gogh，imgSeek等

## Python安装和环境配置

*Python 3*适用于Windows，Mac OS和大多数Linux操作系统。即使*Python 2*目前可用于许多其他操作系统，有部分系统*Python 3*还没有提供支持或者支持了但被它们在系统上删除了，只保留旧的*Python 2*版本。

在本教程中，我们重点讲解如何在 *Windows 10* 和 *Ubuntu* 系统上安装 *Python 3* 的最新版本(当前新版本：*Python 3.6.1*)。

### 在Windows 10上安装Python 3

最新版本的Python 3(Python 3.5.1)的二进制文件可从Python官方网站的下载页面： http://www.python.org/downloads/windows/ 下载，可以使用以下不同的安装选项 - 

![img](E:\git\python3-noteboook\python3教程.assets\861180608_42582.png)

这里选择： [下载Windows x86-64 executable installer](http://www.python.org/ftp/python/3.6.1/python-3.6.1-amd64.exe) 下载。下载完成后，双击 *python-3.6.1-amd64.exe* 可执行文件。

第一步：双击 *python-3.6.1-amd64.exe* 可执行文件，如下所示 - 

![img](E:\git\python3-noteboook\python3教程.assets\537080629_96562.png)

第二步：选择“**Cusomize installation**“，如下所示 -

![img](E:\git\python3-noteboook\python3教程.assets\732080631_37341.png)

第三步：选择“**Next>**“，这里选择安装在 **D:\Program Files\Python36**，如下所示 -

![img](E:\git\python3-noteboook\python3教程.assets\393080634_60369.png)

第四步：开始安装 “**Install**“ ，如下 - 

![img](E:\git\python3-noteboook\python3教程.assets\514080637_64478.png)

第五步：安装完成后选择关闭(**Close**)，如下所示 - 

![img](E:\git\python3-noteboook\python3教程.assets\909080640_42537.png)

**测试安装结果**

由于我们在安装的第一步中，已经选择了“Add Python 3.6 to PATH”了，所以这里不需要单独去设置环境变量了。如果没有选择此项，则应该需要将Python 3.6添加到环境变量。
假设您已经按照上面的步骤来安装完成，现在打开*命令提示符*，并在其中输入 `python`，然后回车 - 

![img](E:\git\python3-noteboook\python3教程.assets\402080649_54349.png)

到此，在 *Windows 10* 系统上安装 *Python 3.6* 已经完成了。

### 在Ubuntu上安装Python 3

首先来看看当 Ubuntu 系统上安装的是什么版本的 Python，在终端上输入 `python`，如下所示 - 

```shell
yiibai@ubuntu:~$ python -version
The program 'python' can be found in the following packages:
 * python-minimal
 * python3
Try: sudo apt install <selected package>
yiibai@ubuntu:~$
Shell
```

在上面显示结果中，还没有安装 Python 。

**第一种情况：**
如果使用的是*Ubuntu 14.04*或*16.04*，则可以使用J Fernyhough的PPA： http://launchpad.net/~jonathonf/+archive/ubuntu/python-3.6 来安装Python 3.6：

```shell
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
Shell
```

**第二种情况：**
如果使用的是*Ubuntu 16.10*或*17.04*，则*Python 3.6*位于Universe存储库中，直接升级 `apt-get`，然后再安装即可 - 

```shell
sudo apt-get update
sudo apt-get install python3.6
Shell
```

现在，查看 Ubuntu 的当前版本 - 

```shell
yiibai@ubuntu:~$ sudo lsb_release -a
[sudo] password for yiibai:
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.1 LTS
Release:        16.04
Codename:       xenial
yiibai@ubuntu:~$
Shell
```

> 提示：Ubuntu无法找到`add-apt-repository`问题的解决方法,执行安装命令：`apt-get install python-software-properties`，除此之外还要安装 `apt-get install software-properties-common`，然后就能用`add-apt-repository`了。

根据上面显示的系统信息，系统版本是：*Ubuntu 16.04.1 LTS*，所以属于第一种情况安装 *Python 3.6*，所以完整的安装步骤如下 - 

```shell
sudo apt-get install python-software-properties
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
Shell
```

> 注意，上面命令执行可能会出现中断或错误的情况，可尝试多执行几次。

当上面命令成功执行完成后，默认情况下，它也会安装了一个 Python 2.7，在命令行提示符下输入：`python`，那么它使用的是 *Python 2.7*，如果要使用 *Python 3.6*，那么可以直接输入：`python3.6`，验证安装结果如下所示 - 

![img](E:\git\python3-noteboook\python3教程.assets\201090651_39264.png)

**从源代码编译安装 Python 3.6**
或者，如果您有时间和精力，也可以尝试从源代码编译来安装 *Python 3.6* 。源代码下载地址：http://www.python.org/ftp/python/3.6.1/

首先，需要使用以下命令安装一些构建依赖项。

```shell
sudo apt install build-essential checkinstall

sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
Shell
```

然后，从python.org下载*Python 3.6*源代码。

```shell
wget http://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz
Shell
```

接下来，解压缩tarball。

```shell
tar xvf Python-3.6.0.tar.xz
Shell
```

现在`cd`进入源目录，配置构建环境并进行安装。

```shell
cd Python-3.6.0/

./configure

sudo make altinstall
Shell
```

使`altinstall`命令跳过创建符号链接，所以`/usr/bin/python`仍然指向旧版本的Python，保证`Ubuntu`系统将不会中断。

完成完成后，可以通过键入以下命令来使用Python 3.6：

```shell
$ python3.6
Shell
```

以下是所有可用命令行选项的列表 -

| 编号 | 选项     | 说明                                                         |
| ---- | -------- | ------------------------------------------------------------ |
| 1    | `-d`     | 提供调试输出                                                 |
| 2    | `-O`     | 生成优化的字节码(结果为`.pyo`文件)                           |
| 3    | `-S`     | 启动时不要运行导入站点来寻找Python路径                       |
| 4    | `-v`     | 详细输出(`import`语句的详细跟踪)                             |
| 5    | `-X`     | 禁用基于类的内置异常(仅使用字符串); 从版本`1.6`开始已经过时了 |
| 6    | `-c cmd` | 运行Python脚本作为`cmd`字符串发送                            |
| 7    | `file`   | 从给定运行的Python脚本文件                                   |

**命令行脚本**

通过在应用程序中调用解释器，可以在命令行中执行Python脚本，如以下示例所示。

```shell
$python  script.py          # Unix/Linux

or 

python% script.py           # Unix/Linux

or 

C:>python script.py         # Windows/DOS
Shell
```

> 注意 - 确保文件权限模式允许执行。

**集成开发环境**

如果您的系统上支持Python的GUI应用程序，也可以从图形用户界面(GUI)环境运行Python。

**Unix** - *IDLE*是第一个用于Python的Unix IDE。

**Windows** - PythonWin是Python的第一个Windows图形用户界面，是具有GUI的IDE。

**Macintosh** - Macintosh版本的Python以及*IDLE IDE*可从主网站获取，可作为MacBinary或BinHex’d文件下载。

如果您无法正确设置环境，则可以通过向系统管理员寻求帮助。确保Python环境设置正确，以正常工作。

> 注 - 后续章节中给出的所有示例都是使用*Windows 7*和*Ubuntu Linux*上提供的*Python 3.6.1*版本来执行。

## Python命令行参数

Python提供了一个`getopt`模块，用于解析命令行选项和参数。

```shell
$ python test.py arg1 arg2 arg3
Shell
```

Python `sys`模块通过`sys.argv`提供对任何命令行参数的访问。主要有两个参数变量 -

- `sys.argv`是命令行参数的列表。
- `len(sys.argv)`是命令行参数的数量。

这里`sys.argv [0]`是程序名称，即脚本的名称。比如在上面示例代码中，`sys.argv [0]`的值就是 `test.py`。

### 示例

看看以下脚本`command_line_arguments.py`的代码 -

```python
##!/usr/bin/python3

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
Python
```

现在运行上面的脚本，这将产生以下结果 -

```python
F:\>python F:\worksp\python\command_line_arguments.py
Number of arguments: 1 arguments.
Argument List: ['F:\\worksp\\python\\command_line_arguments.py']

F:\>python F:\worksp\python\command_line_arguments.py arg1 arg2 arg3 arg4
Number of arguments: 5 arguments.
Argument List: ['F:\\worksp\\python\\command_line_arguments.py', 'arg1', 'arg2', 'arg3', 'arg4']

F:\>
Python
```

> 注意 - 如上所述，第一个参数始终是脚本名称，它也被计入参数的数量。

### 解析命令行参数

Python提供了一个`getopt`模块，可用于解析命令行选项和参数。该模块提供了两个功能和异常，以启用命令行参数解析。

**getopt.getopt方法**

此方法解析命令行选项和参数列表。以下是此方法的简单语法 -

```python
getopt.getopt(args, options, [long_options])
Python
```

**getopt.GetoptError异常**

当在参数列表中有一个无法识别的选项，或者当需要一个参数的选项不为任何参数时，会引发这个异常。
异常的参数是一个字符串，指示错误的原因。 属性`msg`和`opt`给出错误消息和相关选项。

### 示例

假设想通过命令行传递两个文件名，也想给出一个选项用来显示脚本的用法。脚本的用法如下 -

```shell
usage: file.py -i <inputfile> -o <outputfile>
Shell
```

以下是`command_line_usage.py`的以下脚本 -

```python
##!/usr/bin/python3

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('GetoptError, usage: command_line_usage.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('usage: command_line_usage.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is "', inputfile)
   print ('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
Python
```

现在，使用以下几种方式运行来脚本，输出如下所示：

```shell
F:\worksp\python>python command_line_usage.py -h
usage: command_line_usage.py -i <inputfile> -o <outputfile>

F:\worksp\python>python command_line_usage.py -i inputfile.txt -o
GetoptError, usage: command_line_usage.py -i <inputfile> -o <outputfile>

F:\worksp\python>python command_line_usage.py -i inputfile.txt -o outputfile.txt
Input file is " inputfile.txt
Output file is " outputfile.txt

F:\worksp\python>
```

## Python变量类型

变量是保存存储值的内存位置。也就是说，当创建一个变量时，可以在内存中保留一些空间。

基于变量的数据类型，解释器分配内存并决定可以存储在保留的存储器中的内容。 因此，通过为变量分配不同的数据类型，可以在这些变量中存储的数据类型为整数，小数或字符等等。

### 将值分配给变量

在Python中，变量不需要明确的声明类型来保留内存空间。当向变量分配值时，Python会自动发出声明。 等号(`=`)用于为变量赋值。

`=`运算符左侧的操作数是变量的名称，而`=`运算符右侧的操作数是将在存储在变量中的值。 例如 -

```python
##!/usr/bin/python3

counter = 100          # 一个整型数
miles   = 999.99       # 一个浮点数
name    = "Maxsu"       # 一个字符串
site_url  = "http://www.yiibai.com" # 一个字符串

print (counter)
print (miles)
print (name)
print (site_url)
Python
```

这里，`100`,`999.99`和“`Maxsu`”分别是分配给`counter`，`miles`和`name`变量的值。执行上面代码将产生以下结果 -

```shell
100
999.99 
Maxsu
http://www.yiibai.com
Shell
```

### 多重赋值

Python允许同时为多个变量分配单个值。

例如 -

```python
a = b = c = 1
Python
```

这里，创建一个整数对象，其值为`1`，并且所有三个变量都分配给相同的内存位置。还可以将多个对象分配给多个变量。 例如 -

```python
a, b, c = 10, 20, "maxsu"
Python
```

这里，将两个值为`10`和`20`的整数对象分别分配给变量`a`和`b`，并将一个值为“`maxsu`”的字符串对象分配给变量`c`。

### 标准数据类型

存储在内存中的数据可以是多种类型。 例如，一个人的年龄可存储为一个数字值，他的地址被存储为字母数字字符串。 Python具有各种标准数据类型，用于定义可能的操作以及每个标准数据类型的存储方法。

Python有五种标准数据类型 -

- **1.数字**
- **2.字符串**
- **3.列表**
- **4.元组**
- **5.字典**

#### 1.Python数字

数字数据类型存储数字值。当为其分配值时，将创建数字对象。 例如 -

```python
var1 = 10
var2 = 20
Python
```

可以使用`del`语句删除对数字对象的引用。 `del`语句的语法是 -

```python
del var1[,var2[,var3[....,varN]]]]
Python
```

可以使用`del`语句删除单个对象或多个对象。

例如 -

```python
del var
del var_a, var_b
Python
```

Python支持三种不同的数值类型 - 

- int(有符号整数)
- float(浮点实值)
- complex(复数)

Python3中的所有整数都表示为长整数。 因此，长整数没有单独的数字类型。

**例子**

以下是一些数字示例 -

| int    | float      | complex    |
| ------ | ---------- | ---------- |
| 10     | 0.0        | 3.14j      |
| 100    | 15.20      | 45.j       |
| -786   | -21.9      | 9.322e-36j |
| 080    | 32.3+e18   | .876j      |
| -0490  | -90.       | -.6545+0J  |
| -0x260 | -32.54e100 | 3e+26J     |
| 0x69   | 70.2-E12   | 4.53e-7j   |

复数是由`x + yj`表示的有序对的实数浮点数组成，其中`x`和`y`是实数，`j`是虚数单位。

#### 2.Python字符串

Python中的字符串被标识为在引号中表示的连续字符集。Python允许双引号或双引号。 可以使用片段运算符(`[]`和`[:]`)来获取字符串的子集(子字符串)，其索引从字符串开始处的索引`0`开始，并且以`-1`表示字符串中的最后一个字符。

加号(`+`)是字符串连接运算符，星号(`*`)是重复运算符。例如 -

```python
##!/usr/bin/python3
##coding=utf-8
## save file: variable_types_str1.py

str = 'yiibai.com'

print ('str = ', str)          # Prints complete string
print ('str[0] = ',str[0])       # Prints first character of the string
print ('str[2:5] = ',str[2:5])     # Prints characters starting from 3rd to 5th
print ('str[2:] = ',str[2:])      # Prints string starting from 3rd character
print ('str[-1] = ',str[-1])      # 最后一个字符，结果为：'!'
print ('str * 2 = ',str * 2)      # Prints string two times
print ('str + "TEST" = ',str + "TEST") # Prints concatenated string
Python
```

将上面代码保存到 `variable_types_str1.py` 文件中，执行将产生以下结果 -

```shell
F:\worksp\python>python variable_types_str1.py
str =  yiibai.com
str[0] =  y
str[2:5] =  iba
str[2:] =  ibai.com
str[-1] =  m
str * 2 =  yiibai.comyiibai.com
str + "TEST" =  yiibai.comTEST

F:\worksp\python>
Shell
```

#### 2.Python列表

列表是Python复合数据类型中最多功能的。 一个列表包含用逗号分隔并括在方括号(`[]`)中的项目。在某种程度上，列表类似于C语言中的数组。它们之间的区别之一是Python列表的所有项可以是不同的数据类型，而C语言中的数组只能是同种类型。

存储在列表中的值可以使用切片运算符(`[]`和`[]`)来访问，索引从列表开头的`0`开始，并且以`-1`表示列表中的最后一个项目。 加号(`+`)是列表连接运算符，星号(`*`)是重复运算符。例如 -

```python
##!/usr/bin/python3
##coding=utf-8
## save file: variable_types_str1.py
list = [ 'yes', 'no', 786 , 2.23, 'minsu', 70.2 ]
tinylist = [100, 'maxsu']

print ('list = ', list)          # Prints complete list
print ('list[0] = ',list[0])       # Prints first element of the list
print ('list[1:3] = ',list[1:3])     # Prints elements starting from 2nd till 3rd 
print ('list[2:] = ',list[2:])      # Prints elements starting from 3rd element
print ('list[-3:-1] = ',list[-3:-1])    
print ('tinylist * 2 = ',tinylist * 2)  # Prints list two times
print ('list + tinylist = ', list + tinylist) # Prints concatenated lists
Python
```

将上面代码保存到 `variable_types_str1.py` 文件中，执行将产生以下结果 -

```shell
F:\worksp\python>python variable_types_list.py
list =  ['yes', 'no', 786, 2.23, 'minsu', 70.2]
list[0] =  yes
list[1:3] =  ['no', 786]
list[2:] =  [786, 2.23, 'minsu', 70.2]
list[-3:-1] =  [2.23, 'minsu']
tinylist * 2 =  [100, 'maxsu', 100, 'maxsu']
list + tinylist =  ['yes', 'no', 786, 2.23, 'minsu', 70.2, 100, 'maxsu']

F:\worksp\python>
Shell
```

#### 3.Python元组

元组是与列表非常类似的另一个序列数据类型。元组是由多个值以逗号分隔。然而，与列表不同，元组被括在小括号内(`()`)。

列表和元组之间的主要区别是 - 列表括在括号(`[]`)中，列表中的元素和大小可以更改，而元组括在括号(`()`)中，无法更新。元组可以被认为是**只读**列表。 例如 -

```python
##!/usr/bin/python3
##coding=utf-8
## save file : variable_types_tuple.py
tuple = ( 'maxsu', 786 , 2.23, 'yiibai', 70.2  )
tinytuple = (999.0, 'maxsu')

## tuple[1] = 'new item value' 不能这样赋值

print ('tuple = ', tuple)           # Prints complete tuple
print ('tuple[0] = ', tuple[0])        # Prints first element of the tuple
print ('tuple[1:3] = ', tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print ('tuple[-3:-1] = ', tuple[-3:-1])       # 输出结果是什么？
print ('tuple[2:] = ', tuple[2:])       # Prints elements starting from 3rd element
print ('tinytuple * 2 = ',tinytuple * 2)   # Prints tuple two times
print ('tuple + tinytuple = ', tuple + tinytuple) # Prints concatenated tuple
Python
```

将上面代码保存到 `variable_types_tuple.py` 文件中，执行将产生以下结果 -

```shell
F:\worksp\python>python variable_types_tuple.py
tuple =  ('maxsu', 786, 2.23, 'yiibai', 70.2)
tuple[0] =  maxsu
tuple[1:3] =  (786, 2.23)
tuple[-3:-1] =  (2.23, 'yiibai')
tuple[2:] =  (2.23, 'yiibai', 70.2)
tinytuple * 2 =  (999.0, 'maxsu', 999.0, 'maxsu')
tuple + tinytuple =  ('maxsu', 786, 2.23, 'yiibai', 70.2, 999.0, 'maxsu')

F:\worksp\python>
Shell
```

以下代码对于元组无效，因为尝试更新元组，但是元组是不允许更新的。类似的情况可能与列表 -

```python
##!/usr/bin/python3

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
tuple[2] = 1000    # 无法更新值，程序出错
list[2] = 1000     # 有效的更新，合法
Python
```

### Python字典

Python的字典是一种哈希表类型。它们像Perl中发现的关联数组或散列一样工作，由键值对组成。字典键几乎可以是任何Python数据类型，但通常为了方便使用数字或字符串。另一方面，值可以是任意任意的Python对象。

字典由大括号(`{}`)括起来，可以使用方括号(`[]`)分配和访问值。例如 -

```python
##!/usr/bin/python3
##coding=utf-8
## save file : variable_types_dict.py

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is my"

tinydict = {'name': 'maxsu', 'code' : 1024, 'dept':'IT Dev'}


print ("dict['one'] = ", dict['one'])       # Prints value for 'one' key
print ('dict[2] = ', dict[2])           # Prints value for 2 key
print ('tinydict = ', tinydict)          # Prints complete dictionary
print ('tinydict.keys() = ', tinydict.keys())   # Prints all the keys
print ('tinydict.values() = ', tinydict.values()) # Prints all the values
Python
```

将上面代码保存到 `variable_types_dict.py` 文件中，执行将产生以下结果 -

```shell
F:\worksp\python>python variable_types_dict.py
dict['one'] =  This is one
dict[2] =  This is my
tinydict =  {'name': 'maxsu', 'code': 1024, 'dept': 'IT Dev'}
tinydict.keys() =  dict_keys(['name', 'code', 'dept'])
tinydict.values() =  dict_values(['maxsu', 1024, 'IT Dev'])
Shell
```

字典中的元素没有顺序的概念。但是说这些元素是“乱序”是不正确的; 它们是无序的。

### 数据类型转换

有时，可能需要在内置类型之间执行转换。要在类型之间进行转换，只需使用类型名称作为函数即可。

有以下几种内置函数用于执行从一种数据类型到另一种数据类型的转换。这些函数返回一个表示转换值的新对象。它们分别如下所示 -

| 编号 | 函数                    | 描述                                                   |
| ---- | ----------------------- | ------------------------------------------------------ |
| 1    | `int(x [,base])`        | 将`x`转换为整数。如果`x`是字符串，则要`base`指定基数。 |
| 2    | `float(x)`              | 将`x`转换为浮点数。                                    |
| 3    | `complex(real [,imag])` | 创建一个复数。                                         |
| 4    | `str(x)`                | 将对象`x`转换为字符串表示形式。                        |
| 5    | `repr(x)`               | 将对象`x`转换为表达式字符串。                          |
| 6    | `eval(str)`             | 评估求值一个字符串并返回一个对象。                     |
| 7    | `tuple(s)`              | 将`s`转换为元组。                                      |
| 8    | `list(s)`               | 将`s`转换为列表。                                      |
| 9    | `set(s)`                | 将`s`转换为集合。                                      |
| 10   | `dict(d)`               | 创建一个字典，`d`必须是`(key，value)`元组的序列        |
| 11   | `frozenset(s)`          | 将`s`转换为冻结集                                      |
| 12   | `chr(x)`                | 将整数`x`转换为字符                                    |
| 13   | `unichr(x)`             | 将整数`x`转换为Unicode字符。                           |
| 14   | `ord(x)`                | 将单个字符`x`转换为其整数值。                          |
| 15   | `hex(x)`                | 将整数`x`转换为十六进制字符串。                        |
| 16   | `oct(x)`                | 将整数`x`转换为八进制字符串。                          |

## Python基本运算符

运算符是可以操纵操作数值的结构。如下一个表达式：`10 + 20 = 30`。这里，`10`和`20`称为操作数，`+`则被称为运算符。

### 运算符类型

Python语言支持以下类型的运算符 -

- 1.算术运算符
- 2.比较(关系)运算符
- 3.赋值运算符
- 4.逻辑运算符
- 5.按位运算符
- 6.成员运算符
- 7.身份运算符

下面让我们依次来看看所有的运算符。

#### 1.算术运算符

假设变量`a`的值是`10`，变量`b`的值是`21`，则 -

| 运算符 | 描述                                                         | 示例                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `+`    | 加法运算，将运算符两边的操作数增加。                         | `a + b = 31`                                                 |
| `-`    | 减法运算，将运算符左边的操作数减去右边的操作数。             | `a – b = -11`                                                |
| `*`    | 乘法运算，将运算符两边的操作数相乘                           | `a * b = 210`                                                |
| `/`    | 除法运算，用右操作数除左操作数                               | `b / a = 2.1`                                                |
| `%`    | 模运算，用右操作数除数左操作数并返回余数                     | `b % a = 1`                                                  |
| `**`   | 对运算符进行指数(幂)计算                                     | `a ** b`，表示`10`的`21`次幂                                 |
| `//`   | 地板除 - 操作数的除法，其结果是删除小数点后的商数。 但如果其中一个操作数为负数，则结果将被保留，即从零(向负无穷大)舍去 | `9//2 = 4` ， `9.0//2.0 = 4.0`, `-11//3 = -4`, `-11.0//3 = -4.0` |

有关算术运算符的示例代码，请参考：：http://www.yiibai.com/python/arithmetic_operators_example.html 

#### 2.比较(关系)运算符

比较(关系)运算符比较它们两边的值，并确定它们之间的关系。它们也称为关系运算符。假设变量`a`的值`10`，变量`b`的值是`20`，则 -

| 运算符 | 描述                                                   | 示例                         |
| ------ | ------------------------------------------------------ | ---------------------------- |
| `==`   | 如果两个操作数的值相等，则条件为真。                   | `(a == b)`求值结果为 `false` |
| `!=`   | 如果两个操作数的值不相等，则条件为真。                 | `(a != b)`求值结果为 `true`  |
| `>`    | 如果左操作数的值大于右操作数的值，则条件成为真。       | `(a > b)`求值结果为 `false`  |
| `<`    | 如果左操作数的值小于右操作数的值，则条件成为真。       | `(a < b)`求值结果为 `true`   |
| `>=`   | 如果左操作数的值大于或等于右操作数的值，则条件成为真。 | `(a >= b)`求值结果为 `false` |
| `<=`   | 如果左操作数的值小于或等于右操作数的值，则条件成为真。 | `(a <= b)`求值结果为 `true`  |

有关比较(关系)运算符的示例代码，请参考：http://www.yiibai.com/python/comparison_operators_example.html 

#### 3.赋值运算符

假设变量`a`的值`10`，变量`b`的值是`20`，则 -

| 运算符 | 描述                                                 | 示例                                  |
| ------ | ---------------------------------------------------- | ------------------------------------- |
| `=`    | 将右侧操作数的值分配给左侧操作数                     | `c = a + b`表示将`a + b`的值分配给`c` |
| `+=`   | 将右操作数相加到左操作数，并将结果分配给左操作数     | `c + = a`等价于`c = c + a`            |
| `-=`   | 从左操作数中减去右操作数，并将结果分配给左操作数     | `c -= a` 等价于 `c = c - a`           |
| `*=`   | 将右操作数与左操作数相乘，并将结果分配给左操作数     | `c *= a` 等价于 `c = c * a`           |
| `/=`   | 将左操作数除以右操作数，并将结果分配给左操作数       | `c /= a` 等价于 `c = c / a`           |
| `%=`   | 将左操作数除以右操作数的模数，并将结果分配给左操作数 | `c %= a` 等价于 `c = c % a`           |
| `**=`  | 执行指数(幂)计算，并将值分配给左操作数               | `c **= a` 等价于 `c = c ** a`         |
| `//=`  | 运算符执行地板除运算，并将值分配给左操作数           | `c //= a` 等价于 `c = c // a`         |

有关赋值运算符的示例代码，请参考：http://www.yiibai.com/python/assignment_operators_example.html 

#### 4.逻辑运算符

Python语言支持以下逻辑运算符。假设变量`a`的值为`True`，变量`b`的值为`False`，那么 -

| 运算符 | 描述                                           | 示例                            |
| ------ | ---------------------------------------------- | ------------------------------- |
| `and`  | 如果两个操作数都为真，则条件成立。             | `(a and b)`的结果为`False`      |
| `or`   | 如果两个操作数中的任何一个非零，则条件成为真。 | `(a or b)`的结果为`True`        |
| `not`  | 用于反转操作数的逻辑状态。                     | `not(a and b)` 的结果为`True`。 |

有关逻辑运算符的示例代码，请参考：http://www.yiibai.com/python/logical_operators_example.html 

#### 5.按位运算符

按位运算符执行逐位运算。 假设变量`a = 60`; 和变量`b = 13`; 现在以二进制格式，它们将如下 -

```shell
a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a = 1100 0011
Shell
```

Python的内置函数`bin()`可用于获取整数的二进制表示形式。

以下是Python语言支持位运算操作符 -

| 运算符                        | 描述                                                         | 示例                                                         |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `&`                           | 如果它存在于两个操作数中，则操作符复制位到结果中             | `(a & b)` 结果表示为 `0000 1100`                             |
| ![img](/static/images/or.png) | 如果它存在于任一操作数，则复制位。                           | (a ![img](/static/images/or.png) b) = 61 结果表示为 `0011 1101` |
| `^`                           | 二进制异或。如果它是一个操作数集合，但不是同时是两个操作数则将复制位。 | `(a ^ b) = 49` (结果表示为 `0011 0001`)                      |
| `~`                           | 二进制补码，它是一元的，具有“翻转”的效果。                   | `(~a ) = -61`有符号的二进制数，表示为`1100 0011`的补码形式。 |
| `<<`                          | 二进制左移，左操作数的值由右操作数指定的位数左移。           | `a << 2 = 240` (结果表示为 `1111 0000`)                      |
| `>>`                          | 二进制右移，左操作数的值由右操作数指定的位数右移。           | `a >> 2 = 15`(结果表示为`0000 1111`)                         |

有关按位运算符的示例代码，请参考：http://www.yiibai.com/python/bitwise_operators_example.html 

#### 6.成员运算符

Python成员运算符测试给定值是否为序列中的成员，例如字符串，列表或元组。 有两个成员运算符，如下所述 - 

| 运算符   | 描述                                                         | 示例 |
| -------- | ------------------------------------------------------------ | ---- |
| `in`     | 如果在指定的序列中找到一个变量的值，则返回`true`，否则返回`false`。 | -    |
| `not in` | 如果在指定序列中找不到变量的值，则返回`true`，否则返回`false`。 | -    |

有关成员运算符的示例代码，请参考：http://www.yiibai.com/python/membership_operators_example.html 

#### 7.身份运算符

身份运算符比较两个对象的内存位置。常用的有两个身份运算符，如下所述 -

| 运算符   | 描述                                                         | 示例 |
| -------- | ------------------------------------------------------------ | ---- |
| `is`     | 如果运算符任一侧的变量指向相同的对象，则返回`True`，否则返回`False`。 |      |
| `is not` | 如果运算符任一侧的变量指向相同的对象，则返回`True`，否则返回`False`。 | -    |

有关身份运算符的示例代码，请参考：http://www.yiibai.com/python/identity_operators_example.html 

#### 8. 运算符优先级

下表列出了从最高优先级到最低优先级的所有运算符，如下所示 - 

| 序号 | 运算符                                   | 描述                                           |
| ---- | ---------------------------------------- | ---------------------------------------------- |
| 1    | `**`                                     | 指数(次幂)运算                                 |
| 2    | `~` `+`  `-`                             | 补码，一元加减(最后两个的方法名称是`+@`和`-@`) |
| 3    | `*` `/` `%` `//`                         | 乘法，除法，模数和地板除                       |
| 4    | `+` `-`                                  |                                                |
| 5    | `>>` `<<`                                | 向右和向左位移                                 |
| 6    | `&`                                      | 按位与                                         |
| 7    | `^` ![img](/static/images/or.png)        | 按位异或和常规的“`OR`”                         |
| 8    | `<=` `<` `>` `>=`                        | 比较运算符                                     |
| 9    | `<>` `==` `!=`                           | 等于运算符                                     |
| 10   | `=` `%=` `/=` `//=` `-=` `+=` `*=` `**=` | 赋值运算符                                     |
| 11   | `is` `is not`                            | 身份运算符                                     |
| 12   | `in` `not in`                            | 成员运算符                                     |
| 13   | `not` `or` `and`                         | 逻辑运算符                                     |

有关运算符优先级的示例代码，请参考：http://www.yiibai.com/python/operators_precedence_example.html

## Python决策

决策是指在执行程序期间根据发生的情况并根据条件采取的具体操作(行动)。决策结构评估求值多个表达式，产生`TRUE`或`FALSE`作为结果。如果结果为`TRUE`或否则为`FALSE`，则需要确定要执行的操作和要执行的语句。

以下是大多数编程语言中的典型决策结构的一般形式 -

![img](E:\git\python3-noteboook\python3教程.assets\605220624_31440.jpg)

Python编程语言假定任何非零值和非空值都为`TRUE`值，而任何零值或空值都为`FALSE`值。

Python编程语言提供以下类型的决策语句。

| 编号 | 语句                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [if语句](http://www.yiibai.com/python/python_if_statement.html) | 一个if语句由一个布尔表达式，后跟一个或多个语句组成。         |
| 2    | [if…else语句](http://www.yiibai.com/python/python_if_else.html) | 一个`if`语句可以跟随一个可选的`else`语句，当`if`语句的布尔表达式为`FALSE`时，则`else`语句块将被执行。 |
| 3    | [嵌套if语句](http://www.yiibai.com/python/nested_if_statements_in_python.html) | 可以在一个`if`或`else`语句中使用一个`if`或`else if`语句。    |

下面我们快速地来了解每个决策声明。

### 单个语句套件

一个`if`子句套件可能只包含一行，它可能与头语句在同一行上。

**示例**

以下是一行`if`子句的示例 -

```python
##!/usr/bin/python3
var = 10
if ( var  == 10 ) : print ("Value of expression is 10")
print ("Good bye!")
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Value of expression is 100
Good bye!
```

## Python循环

一般来说，语句依次执行 - 例如，函数中的第一个语句首先执行，然后是第二个语句，依次类推。但是有很多时候需要多次执行同一段代码，这就引入了循环的概念。

编程语言提供了允许更复杂的执行路径的各种控制结构。

循环语句允许多次执行语句或语句组。下图说明了一个循环语句流程结构 -

![img](E:\git\python3-noteboook\python3教程.assets\823080656_41224.jpg)

Python编程语言提供以下类型的循环来处理循环需求。

| 编号 | 循环                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [while循环](http://www.yiibai.com/python/python_while_loop.html) | 在给定条件为`TRUE`时，重复一个语句或一组语句。 它在执行循环体之前测试状态。 |
| 2    | [for循环](http://www.yiibai.com/python/python_for_loop.html) | 多次执行一系列语句，并缩写管理循环变量的代码。               |
| 3    | [嵌套循环](http://www.yiibai.com/python/python_nested_loops.html) | 可以使用一个或多个循环在`while`或`for`循环中。               |

### 循环控制语句

循环控制语句从正常顺序更改执行。 当执行离开范围时，在该范围内创建的所有自动对象都将被销毁。

Python支持以下控制语句。

| 编号 | 控制语句                                                     | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [break语句](http://www.yiibai.com/python/python_break_statement.html) | 终止循环语句并将执行转移到循环之后的语句。                   |
| 2    | [continue语句](http://www.yiibai.com/python/python_continue_statement.html) | 使循环跳过其主体的剩余部分，并立即重新测试其状态以进入下一次迭代。 |
| 3    | [pass语句](http://www.yiibai.com/python/python_pass_statement.html) | 当语法需要但不需要执行任何命令或代码时，Python中就可以使用`pass`语句，此语句什么也不做，用于表示“占位”的代码，有关实现细节后面再写 |

下面简单地看一下循环控制语句。

### 迭代器和生成器

迭代器(Iterator)是允许程序员遍历集合的所有元素的对象，而不管其具体实现。在Python中，迭代器对象实现了`iter()`和`next()`两种方法。

`String`，`List`或`Tuple`对象可用于创建`Iterator`。

```python
list = [1,2,3,4]
it = iter(list) # this builds an iterator object
print (next(it)) #prints next available element in iterator
## Iterator object can be traversed using regular for statement

for x in it:
   print (x, end=" ")
or using next() function
while True:
   try:
      print (next(it))
   except StopIteration:
      sys.exit() #you have to import sys module for this
Python
```

发生器(`generator`)是使用`yield`方法产生或产生一系列值的函数。

当一个生成器函数被调用时，它返回一个生成器对象，而不用执行该函数。 当第一次调用`next()`方法时，函数开始执行，直到它达到`yield`语句，返回`yielded`值。 `yield`保持跟踪，即记住最后一次执行，而第二个`next()`调用从前一个值继续。

### 示例

以下示例定义了一个生成器，它为所有斐波纳契数字生成一个迭代器。

```python
##!usr/bin/python3
import sys
def fibonacci(n): #generator function
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n): 
         return
      yield a
      a, b = b, a + b
      counter += 1
f = fibonacci(5) #f is iterator object

while True:
   try:
      print (next(f), end=" ")
   except StopIteration:
      sys.exit()
```

## Python数字

数字数据类型用于存储数值。它们是不可变数据类型。这意味着，更改数字数据类型的值会导致新分配对象。

当为数字数据类型分配值时，Python将创建数字对象。 例如 -

```python
var1 = 1
var2 = 10
Python
```

可以使用`del`语句删除对数字对象的引用。`del`语句的语法是 -

```python
del var1[,var2[,var3[....,varN]]]]
Python
```

可以使用`del`语句一次删除单个对象或多个对象。 例如 -

```python
del var
del var_a, var_b
Python
```

Python支持不同的数值类型 -

- **int(有符号整数)** - 它们通常被称为整数或整数。它们是没有小数点的正或负整数。 *Python 3*中的整数是无限大小的。 *Python 2* 有两个整数类型 - `int`和`long`。 *Python 3*中没有“长整数”。
- **float(浮点实数值)** - 也称为浮点数，它们表示实数，并用小数点写整数和小数部分。 浮点数也可以是科学符号，`E`或`e`表示`10`的幂 - ![img](E:\git\python3-noteboook\python3教程.assets\520110614_90614.png)
- **complex(复数)** - 复数是以`a + bJ`的形式，其中`a`和`b`是浮点，`J`(或`j`)表示`-1`的平方根(虚数)。数字的实部是`a`，虚部是`b`。复数在Python编程中并没有太多用处。

可以以十六进制或八进制形式表示整数 - 

```python
>>> number = 0xA0F #Hexa-decimal
>>> number
2575

>>> number = 0o37 #Octal
>>> number
31
Python
```

**例子**

以下是一些数字值的示例 - 

| **int** | **float**  | **complex** |
| ------- | ---------- | ----------- |
| 10      | 0.0        | 3.14j       |
| 100     | 15.20      | 45.j        |
| -786    | -21.9      | 9.322e-36j  |
| 080     | 32.3+e18   | .876j       |
| -0490   | -90.       | -.6545+0J   |
| -0×260  | -32.54e100 | 3e+26J      |
| 0×69    | 70.2-E12   | 4.53e-7j    |

复数由一个`a + bj`来表示，它是由实际浮点数的有序对组成，其中`a`是实部，`b`是复数的虚部。

### 数字类型转换

Python可将包含混合类型的表达式内部的数字转换成用于评估求值的常用类型。 有时需要从一个类型到另一个类型执行明确数字转换，以满足运算符或函数参数的要求。

- `int(x)`将`x`转换为纯整数。
- `long(x)`将`x`转换为长整数。
- `float(x)`将`x`转换为浮点数。
- `complex(x)`将`x`转换为具有实部`x`和虚部`0`的复数。
- `complex(x, y)`将`x`和`y`转换为具有实部为`x`和虚部为`y`的复数。`x`和`y`是数字表达式。

### 数学函数

Python中包括执行数学计算的函数，如下列表所示 - 

| 编号 | 函数                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [abs(x)](http://www.yiibai.com/python/number_abs.html)       | `x`的绝对值，`x`与零之间的(正)距离。                         |
| 2    | [ceil(x)](http://www.yiibai.com/python/number_ceil.html)     | `x`的上限，不小于`x`的最小整数。                             |
| 3    | `cmp(x, y)`                                                  | 如果 `x < y` 返回 `-1`, 如果 `x == y` 返回 `0`, 或者 如果 `x > y` 返回 `1`。在*Python 3*中已经弃用，可使用`return (x>y)-(x<y)`代替。 |
| 4    | [exp(x)](http://www.yiibai.com/python/number_exp.html)       | `x`的指数，返回`e`的`x`次幂                                  |
| 5    | [fabs(x)](http://www.yiibai.com/python/number_fabs.html)     | `x`的绝对值。                                                |
| 6    | [floor(x)](http://www.yiibai.com/python/number_floor.html)   | 不大于`x`的最大整数。                                        |
| 7    | [log(x)](http://www.yiibai.com/python/number_log.html)       | `x`的自然对数(`x > 0`)。                                     |
| 8    | [log10(x)](http://www.yiibai.com/python/number_log10.html)   | 以基数为`10`的`x`的对数(`x > 0`)。                           |
| 9    | [max(x1, x2,…)](http://www.yiibai.com/python/number_max.html) | 给定参数中的最大值，最接近正无穷大值                         |
| 10   | [min(x1, x2,…)](http://www.yiibai.com/python/number_min.html) | 给定参数中的最小值，最接近负无穷小值                         |
| 11   | [modf(x)](http://www.yiibai.com/python/number_modf.html)     | 将`x`的分数和整数部分切成两项放入元组中，两个部分与`x`具有相同的符号。整数部分作为浮点数返回。 |
| 12   | [pow(x, y)](http://www.yiibai.com/python/number_pow.html)    | `x`的`y`次幂                                                 |
| 13   | [round(x [,n\])](http://www.yiibai.com/python/number_round.html) | `x`从小数点舍入到`n`位数。`round(0.5)`结果为 `1.0`， `round(-0.5)` 结果为 `-1.0` |
| 14   | [sqrt(x)](http://www.yiibai.com/python/number_sqrt.html)     | `x`的平方根(`x > 0`)。                                       |

### 随机数函数

随机数字用于游戏，模拟，测试，安全和隐私应用。 Python包括以下通常使用的函数。

| 编号 | 函数                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [choice(seq)](http://www.yiibai.com/python/number_choice.html) | 来自列表，元组或字符串的随机项目。                           |
| 2    | [randrange ([start,\] stop [,step])](http://www.yiibai.com/python/number_randrange.html) | 从范围(start, stop, step)中随机选择的元素。                  |
| 3    | [random()](http://www.yiibai.com/python/number_random.html)  | 返回随机浮点数`r`(`0 <= r < 1`)                              |
| 4    | [seed([x\])](http://www.yiibai.com/python/number_seed.html)  | 设置用于生成随机数的整数起始值。在调用任何其他随机模块功能之前调用此函数，返回`None`。 |
| 5    | [shuffle(lst)](http://www.yiibai.com/python/number_shuffle.html) | 将列表的项目随机化到位置。 返回`None`。                      |
| 6    | [uniform(x, y)](http://www.yiibai.com/python/number_uniform.html) | 返回随机浮点数 `r` (`x <= r < y`)。                          |

### 三角函数

随机数字用于游戏，模拟，测试，安全和隐私应用。 Python包括以下通常使用的函数。

| 编号 | 函数                                                         | 描述                                |
| ---- | ------------------------------------------------------------ | ----------------------------------- |
| 1    | [acos(x)](http://www.yiibai.com/python/number_acos.html)     | 返回`x`的弧余弦值，以弧度表示。     |
| 2    | [asin(x)](http://www.yiibai.com/python/number_asin.html)     | 返回`x`的弧线正弦，以弧度表示。     |
| 3    | [atan(x)](http://www.yiibai.com/python/number_atan.html)     | 返回`x`的反正切，以弧度表示。       |
| 4    | [atan2(y, x)](http://www.yiibai.com/python/number_atan2.html) | 返回`atan(y / x)`，以弧度表示。     |
| 5    | [cos(x)](http://www.yiibai.com/python/number_cos.html)       | 返回`x`弧度的余弦。                 |
| 6    | [hypot(x, y)](http://www.yiibai.com/python/number_hypot.html) | 返回欧几里得规范，`sqrt(x*x + y*y)` |
| 7    | [sin(x)](http://www.yiibai.com/python/number_sin.html)       | 返回`x`弧度的正弦。                 |
| 8    | [tan(x)](http://www.yiibai.com/python/number_tan.html)       | 返回`x`弧度的正切值。               |
| 9    | [degrees(x)](http://www.yiibai.com/python/number_degrees.html) | 将角度`x`从弧度转换为度。           |
| 10   | [radians(x)](http://www.yiibai.com/python/number_radians.html) | 将角度`x`从角度转换为弧度。         |

### 数学常数

该模块还定义了两个数学常数 -

| 编号 | 常量   | 描述         |
| ---- | ------ | ------------ |
| 1    | **pi** | 数学常数`pi` |
| 2    | **e**  | 数学常数`e`  |

## Python字符串

字符串是Python中最受欢迎、最常使用的数据类型。可以通过用引号括起字符来创建它们。 Python将单引号与双引号相同。创建字符串和向一个变量赋值一样简单。 例如 -

```python
var1 = 'Hello World!'
var2 = "Python Programming"
Python
```

### 1.访问字符串中的值

Python不支持字符类型; 字符会被视为长度为`1`的字符串，因此也被认为是一个子字符串。要访问子串，请使用方括号的切片加上索引或直接使用索引来获取子字符串。 例如 -

```python
##!/usr/bin/python3

var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5]) # 切片加索引
Python
```

当执行上述代码时，会产生以下结果 -

```shell
var1[0]:  H
var2[1:5]:  ytho
Shell
```

### 2.更新字符串

可以通过将变量分配给另一个字符串来“更新”现有的字符串。 新值可以与其原值相关或完全不同的字符串。 例如 -

```python
##!/usr/bin/python3

var1 = 'Hello World!'

print ("Updated String :- ", var1[:6] + 'Python')
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Updated String :-  Hello Python
Shell
```

### 3.转义字符

下表是可以用反斜杠表示法表示转义或不可打印字符的列表。单引号以及双引号字符串的转义字符被解析。

| 反斜线符号 | 十六进制字符 | 描述/说明                                        |
| ---------- | ------------ | ------------------------------------------------ |
| `\a`       | `0x07`       | 铃声或警报                                       |
| `\b`       | `0x08`       | 退格                                             |
| `\cx`      |              | Control-x                                        |
| `\C-x`     |              | Control-x                                        |
| `\e`       | `0x1b`       | Escape                                           |
| `\f`       | `0x0c`       | 换页                                             |
| `\M-\C-x`  |              | Meta-Control-x                                   |
| `\n`       | `0x0a`       | 新一行                                           |
| `\nnn`     |              | 八进制符号，其中`n`在0.7范围内                   |
| `\r`       | `0x0d`       | 回车返回                                         |
| `\s`       | `0x20`       | 空格                                             |
| `\t`       | `0x09`       | 制表符                                           |
| `\v`       | `0x0b`       | 垂直制表符                                       |
| `\x`       |              | 字符`x`                                          |
| `\xnn`     |              | 十六进制符号，其中`n`在`0~9`，`a~f`或`A~F`范围内 |

### 4.字符串特殊运算符

假设字符串变量`a`保存字符串值’`Hello`‘，变量`b`保存字符串值’`Python`‘，那么 -

| 运算符   | 说明                                                         | 示例                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `+`      | 连接 - 将运算符的两边的值添加                                | `a + b` 结果为 `HelloPython`                                 |
| `*`      | 重复 - 创建新字符串，连接相同字符串的多个副本                | `a*2` 结果为 `HelloHello`                                    |
| `[]`     | 切片 - 给出指定索引中的字符串值，它是原字符串的子串。        | `a[1]` 结果为 `e`                                            |
| `[:]`    | 范围切片 - 给出给定范围内的子字符串                          | `a[1:4]` 结果为 `ell`                                        |
| `in`     | 成员关系 - 如果给定字符串中存在指定的字符，则返回`true`      | `'H' in a` 结果为 `1`                                        |
| `not in` | 成员关系 - 如果给定字符串中不存在指定的字符，则返回`true`    | `'Y' not in a` 结果为 `1`                                    |
| `r/R`    | 原始字符串 - 抑制转义字符的实际含义。原始字符串的语法与正常字符串的格式完全相同，除了原始字符串运算符在引号之前加上字母“`r`”。 “`r`”可以是小写(`r`)或大写(`R`)，并且必须紧靠在第一个引号之前。 | `print(r'\n')` 将打印 `\n` ，或者 `print(R'\n')` 将打印 `\n`，要注意的是如果不加`r`或`R`作为前缀，打印的结果就是一个换行。 |
| `%`      | 格式 - 执行字符串格式化                                      | 请参见本文第5节                                              |

### 5.字符串格式化运算符

Python最酷的功能之一是字符串格式运算符`％`。 这个操作符对于字符串是独一无二的，弥补了C语言中 `printf()`系列函数。 以下是一个简单的例子 -

```python
##!/usr/bin/python3

print ("My name is %s and weight is %d kg!" % ('Maxsu', 71))
Python
```

当执行上述代码时，会产生以下结果 -

```shell
My name is Maxsu and weight is 71 kg!
Shell
```

以下是可以与`%`符号一起使用的完整符号集列表 - 

| 编号 | 格式化符号 | 转换                                  |
| ---- | ---------- | ------------------------------------- |
| 1    | `%c`       | 字符                                  |
| 2    | `%s`       | 在格式化之前通过`str()`函数转换字符串 |
| 3    | `%i`       | 带符号的十进制整数                    |
| 4    | `%d`       | 带符号的十进制整数                    |
| 5    | `%u`       | 无符号十进制整数                      |
| 6    | `%o`       | 八进制整数                            |
| 7    | `%x`       | 十六进制整数(小写字母)                |
| 8    | `%X`       | 十六进制整数(大写字母)                |
| 9    | `%e`       | 指数符号(小写字母’`e`‘)               |
| 10   | `%E`       | 指数符号(大写字母’`E`‘                |
| 11   | `%f`       | 浮点实数                              |
| 12   | `%g`       | `％f`和`％e`                          |
| 13   | `%G`       | `％f`和`％E`                          |

其他支持的符号和功能如下表所列 - 

| 编号 | 符号    | 功能                                                         |
| ---- | ------- | ------------------------------------------------------------ |
| 1    | `*`     | 参数指定宽度或精度                                           |
| 2    | `-`     | 左对齐                                                       |
| 3    | `+`     | 显示标志或符号                                               |
| 4    | `<sp>`  | 在正数之前留空格                                             |
| 5    | `#`     | 根据是否使用“`x`”或“`X`”，添加八进制前导零(‘`0`‘)或十六进制前导’`0x`‘或’`0X`‘。 |
| 6    | `0`     | 使用零作为左边垫符(而不是空格)                               |
| 7    | `%`     | ‘`%%`‘留下一个文字“`%`”                                      |
| 8    | `(var)` | 映射变量(字典参数)                                           |
| 9    | `m.n.`  | `m`是最小总宽度，`n`是小数点后显示的位数(如果应用)           |

### 6.三重引号

Python中的三重引号允许字符串跨越多行，包括逐字记录的新一行，`TAB`和任何其他特殊字符。

三重引号的语法由三个连续的单引号或双引号组成。

```shell
##!/usr/bin/python3

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)
Shell
```

当执行上述代码时，会产生以下结果。注意每个单独的特殊字符如何被转换成其打印形式，它是直到最后一个`NEWLINEs`在“`up`”之间的字符串的末尾，并关闭三重引号。 另请注意，`NEWLINEs`可能会在一行或其转义码(`\n`)的末尾显式显示回车符 -

```shell
this is a long string that is made up of
several lines and non-printable characters such as
TAB (    ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [
 ], or just a NEWLINE within
the variable assignment will also show up.
Shell
```

原始字符串根本不将反斜杠视为特殊字符。放入原始字符串的每个字符都保持所写的方式 -

```python
##!/usr/bin/python3

print ('C:\\nowhere')
Python
```

当执行上述代码时，会产生以下结果 -

```shell
C:\nowhere
Shell
```

现在演示如何使用原始的字符串。将表达式修改为如下 -

```shell
##!/usr/bin/python3

print (r'C:\\nowhere')
Shell
```

当执行上述代码时，会产生以下结果 -

```shell
C:\\nowhere
Shell
```

### 7.Unicode字符串

在*Python 3*中，所有的字符串都用Unicode表示。在*Python 2*内部存储为`8`位ASCII，因此需要附加’`u`‘使其成为*Unicode*，而现在不再需要了。

**内置字符串方法**

Python包括以下内置方法来操作字符串 -

| 编号 | 方法                                                         | 说明                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [capitalize()](http://www.yiibai.com/python/string_capitalize.html) | 把字符串的第一个字母转为大写                                 |
| 2    | [center(width, fillchar)](http://www.yiibai.com/python/string_center.html) | 返回使用`fillchar`填充的字符串，原始字符串以总共`width`列为中心。 |
| 3    | [count(str, beg = 0,end = len(string))](http://www.yiibai.com/python/string_count.html) | 计算字符串中出现有多少次`str`或字符串的子字符串(如果开始索引`beg`和结束索引`end`,则在`beg`~`end`范围匹配)。 |
| 4    | [decode(encoding = ‘UTF-8’,errors = ‘strict’)](http://www.yiibai.com/python/string_decode.html) | 使用编码`encoding`解码该字符串。 编码默认为默认字符串`encoding`。 |
| 5    | [encode(encoding = ‘UTF-8’,errors = ‘strict’)](http://www.yiibai.com/python/string_encode.html) | 返回字符串的编码字符串版本; 在错误的情况下，默认是抛出`ValueError`，除非使用’`ignore`‘或’`replace`‘给出错误。 |
| 6    | [endswith(suffix, beg = 0, end = len(string))](http://www.yiibai.com/python/string_endswith.html "endswith(suffix, beg = 0, end = len(string) | 确定字符串或字符串的子字符串(如果启动索引结束和结束索引结束)都以后缀结尾; 如果是则返回`true`，否则返回`false`。 |
| 7    | [expandtabs(tabsize = 8)](http://www.yiibai.com/python/string_expandtabs.html) | 将字符串中的制表符扩展到多个空格; 如果没有提供`tabize`，则默认为每个制表符为`8`个空格。 |
| 8    | [find(str, beg = 0 end = len(string))](http://www.yiibai.com/python/string_find.html) | 如果索引`beg`和结束索引`end`给定，则确定`str`是否在字符串或字符串的子字符串中，如果找到则返回索引，否则为`-1`。 |
| 9    | [index(str, beg = 0, end = len(string))](http://www.yiibai.com/python/string_index.html) | 与`find()`相同，但如果没有找到`str`，则引发异常。            |
| 10   | [isalnum()](http://www.yiibai.com/python/string_isalnum.html) | 如果字符串至少包含`1`个字符，并且所有字符均为数字，则返回`true`，否则返回`false`。 |
| 11   | [isalpha()](http://www.yiibai.com/python/string_isalpha.html) | 如果字符串至少包含`1`个字符，并且所有字符均为字母，则返回`true`，否则返回`false`。 |
| 12   | [isdigit()](http://www.yiibai.com/python/string_isdigit.html) | 如果字符串只包含数字则返回`true`，否则返回`false`。          |
| 13   | [islower()](http://www.yiibai.com/python/string_islower.html) | 如果字符串至少包含`1`个字母，并且所有字符均为小写，则返回`true`，否则返回`false`。 |
| 14   | [isnumeric()](http://www.yiibai.com/python/string_isnumeric.html) | 如果`unicode`字符串只包含数字字符，则返回`true`，否则返回`false`。 |
| 15   | [isspace()](http://www.yiibai.com/python/string_isspace.html) | 如果字符串只包含空格字符，则返回`true`，否则返回`false`。    |
| 16   | [istitle()](http://www.yiibai.com/python/string_istitle.html) | 如果字符串正确“标题大小写”，则返回`true`，否则返回`false`。  |
| 17   | [isupper()](http://www.yiibai.com/python/string_isupper.html) | 如果字符串至少包含一个可变大小写字符，并且所有可变大小写字符均为大写，则返回`true`，否则返回`false`。 |
| 18   | [join(seq)](http://www.yiibai.com/python/string_join.html)   | 将序列`seq`中的元素以字符串表示合并(并入)到具有分隔符字符串的字符串中。 |
| 19   | [len(string)](http://www.yiibai.com/python/string_len.html)  | 返回字符串的长度                                             |
| 20   | [ljust(width[, fillchar\])](http://www.yiibai.com/python/string_ljust.html) | 返回一个空格填充的字符串，原始字符串左对齐到总共`width`列。  |
| 21   | [lower()](http://www.yiibai.com/python/string_lower.html)    | 将字符串中的所有大写字母转换为小写。                         |
| 22   | [lstrip()](http://www.yiibai.com/python/string_lstrip.html)  | 删除字符串中的所有前导空格                                   |
| 23   | [maketrans()](http://www.yiibai.com/python/string_maketrans.html) | 返回在`translate`函数中使用的转换表。                        |
| 24   | [max(str)](http://www.yiibai.com/python/string_max.html)     | 从字符串`str`返回最大字母字符。                              |
| 27   | [replace(old, new [, max\])](http://www.yiibai.com/python/string_replace.html) | 如果给定`max`值，则用`new`或最多最大出现替换字符串中所有出现的旧字符(`old`)。 |
| 28   | [rindex( str, beg = 0, end = len(string))](http://www.yiibai.com/python/string_rindex.html) | 与`index()`相同，但在字符串中向后搜索。                      |
| 29   | [rjust(width,[, fillchar\])](http://www.yiibai.com/python/string_rjust.html) | 返回一个空格填充字符串，原始字符串右对齐到总共宽度(`width`)列。 |
| 30   | [rstrip()](http://www.yiibai.com/python/string_rstrip.html)  | 删除字符串的所有尾随空格。                                   |
| 31   | [split(str=](http://www.yiibai.com/python/string_split.html) | 根据分隔符`str`(空格，如果没有提供)拆分字符串并返回子字符串列表; 如果给定，最多分割为`num`子串。 |
| 32   | [splitlines( num=string.count(‘\n’))](http://www.yiibai.com/python/string_startswith.html))”) | 全部拆分字符串(或`num`)新行符，并返回每行的列表，并删除新行符。 |
| 33   | [startswith(str, beg=0,end=len(string))](http://www.yiibai.com/python/string_startswith.html) | 确定字符串或字符串的子字符串(如果给定起始索引`beg`和结束索引`end`)以`str`开头; 如果是则返回`true`，否则返回`false`。 |
| 34   | [strip([chars\])](http://www.yiibai.com/python/string_strip.html) | 对字符串执行`lstrip()`和`rstrip()`                           |
| 35   | [swapcase()](http://www.yiibai.com/python/string_swapcase.html) | 反转在字符串中的所有字母大小写，即小写转大写，大写转小写。   |
| 36   | [title()](http://www.yiibai.com/python/string_title.html)    | 返回字符串的标题版本，即所有单词第一个字母都以大写开头，其余的都是小写的。 |
| 37   | [translate(table, deletechars=](http://www.yiibai.com/python/string_translate.html) | 根据转换表STR(256个字符)，除去那些在`del`字符串转换字符串。  |
| 38   | [upper()](http://www.yiibai.com/python/string_upper.html)    | 将字符串中的小写字母转换为大写。                             |
| 39   | [zfill(width)](http://www.yiibai.com/python/string_zfill.html) | 返回原始字符串，左边填充为零，总共有宽度(`width`)字符; 对于数字`zfill()`保留给定的任何符号(少于一个零)。 |
| 40   | [isdecimal() ](http://www.yiibai.com/python/string_isdecimal.html) | 如果unicode字符串只包含十进制字符，则返回`true`，否则返回`false`。 |

## Python列表

Python中最基本的数据结构是列表。一个列表的每个元素被分配一个数字来表示它的位置或索引。 第一个索引为`0`，第二个索引为`1`，依此类推。

Python有六种内置的序列类型，但最常见的是列表和元组，将在本教程中看到。

可以在列表上执行各种类型操作。这些操作包括索引，切片，添加，乘法和检查成员身份。此外，Python还具有内置函数，用于查找序列的长度和查找其最大和最小的元素。

### 1.Python列表

列表是Python中最通用的数据类型，可以写成方括号之间的逗号分隔值(项)列表。列表中的项目不必是相同的类型，这一点和C语言中数组有差别。

创建列表就在方括号之间放置不同的逗号分隔值。 例如 -

```python
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];
Python
```

类似于字符串索引，列表索引从`0`开始，列表可以被切片，连接等等。

### 2.访问列表中的值

要访问列表中的值，使用方括号进行切片以及索引或索引，以获取该索引处可用的值。例如 -

```python
##!/usr/bin/python3

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
Python
```

当执行上述代码时，会产生以下结果 -

```python
list1[0]:  physics
list2[1:5]:  [2, 3, 4, 5]
Python
```

### 3.更新列表

可以通过在分配运算符左侧给出切片来更新列表的单个或多个元素，可以使用`append()`方法添加到列表中的元素。例如 -

```python
##!/usr/bin/python3

list = ['physics', 'chemistry', 1997, 2000]
print ("Value available at index 2 : ", list[2])

list[2] = 2001
print ("New value available at index 2 : ", list[2])
Python
```

> **注** - 在后续章节中讨论了`append()`方法。

当执行上述代码时，会产生以下结果 -

```shell
Value available at index 2 :  1997
New value available at index 2 :  2001
Shell
```

### 4.删除列表元素

要删除列表元素，并且如果确切知道要删除哪些元素可以使用`del`语句。如果不知道要删除哪些项目，可以使用`remove()`方法。 例如 -

```python
##!/usr/bin/python3
list = ['physics', 'chemistry', 1997, 2000]

print (list)
del list[2]
print ("After deleting value at index 2 : ", list)
Python
```

当执行上述代码时，会产生以下结果 -

```python
['physics', 'chemistry', 1997, 2000]
After deleting value at index 2 :  ['physics', 'chemistry', 2000]
Python
```

> 注 - `remove()`方法将在后续章节中讨论。

### 基本列表操作

列表响应`+`和`*`运算符，这与字符串十分类似; 它们也意味着这里的连接和重复，除了结果是新的列表，而不是字符串。

事实上，列表响应上一章中，在字符串上使用的所有常规序列操作。

| Python表达式                             | 结果                           | 描述       |
| ---------------------------------------- | ------------------------------ | ---------- |
| `len([1, 2, 3])`                         | 3                              | 列表的长度 |
| `[1, 2, 3] + [4, 5, 6]`                  | `[1, 2, 3, 4, 5, 6]`           | 联接       |
| `['Hi!'] * 4`                            | `['Hi!', 'Hi!', 'Hi!', 'Hi!']` | 重复       |
| `3 in [1, 2, 3]`                         | `True`                         |            |
| `for x in [1,2,3] : print (x,end = ' ')` | `1 2 3`                        | 迭代       |

### 索引，切片和矩阵

由于列表是序列，索引和切片的工作方式与列表一样，对于字符串。

假设以下输入 -

```python
L = ['C++'', 'Java', 'Python']
Python
```

| Python表达式 | 结果                 | 描述             |
| ------------ | -------------------- | ---------------- |
| `L[2]`       | `'Python'`           | 偏移量，从零开始 |
| `L[-2]`      | `'Java'`             | 负数：从右到右   |
| `L[1:]`      | `['Java', 'Python']` | 切片提取部分     |

### 内置列表函数和方法

Python包括以下列表函数功能 -

| 编号 | 方法                                                         | 描述                       |
| ---- | ------------------------------------------------------------ | -------------------------- |
| 1    | [cmp(list1, list2)](http://www.yiibai.com/python/list_cmp.html) | 在*Python 3*中不再可用。   |
| 2    | [len(list)](http://www.yiibai.com/python/list_len.html)      | 给出列表的总长度。         |
| 3    | [max(list)](http://www.yiibai.com/python/list_max.html)      | 从列表中返回最大值的项目。 |
| 4    | [min(list)](http://www.yiibai.com/python/list_min.html)      | 从列表中返回最小值的项目。 |
| 5    | [list(seq)](http://www.yiibai.com/python/list_list.html)     | 将元组转换为列表。         |

Python包括以下列表方法 -

| 编号 | 方法                                                         | 描述                                                 |
| ---- | ------------------------------------------------------------ | ---------------------------------------------------- |
| 1    | [list.append(obj)](http://www.yiibai.com/python/list_append.html) | 将对象`obj`追加到列表中                              |
| 2    | [list.count(obj)](http://www.yiibai.com/python/list_count.html) | 返回列表中出现多少次`obj`的计数                      |
| 3    | [list.extend(seq)](http://www.yiibai.com/python/list_count.html) | 返回列表中出现多少次`obj`的计数                      |
| 4    | [list.extend(seq)](http://www.yiibai.com/python/list_extend.html) | 将`seq`的内容附加到列表中                            |
| 5    | [list.insert(index, obj)](http://www.yiibai.com/python/list_insert.html) | 将对象`obj`插入到偏移索引的列表中                    |
| 6    | [list.pop(obj = list[-1\])](http://www.yiibai.com/python/list_pop.html) | 从列表中删除并返回最后一个对象或`obj`                |
| 7    | [list.remove(obj)](http://www.yiibai.com/python/list_remove.html) | 从列表中删除对象`obj`                                |
| 8    | [list.reverse()](http://www.yiibai.com/python/list_reverse.html) | 反转列表中的对象                                     |
| 9    | [list.sort([func\])](http://www.yiibai.com/python/list_sort.html) | 排序列表的对象，如果给出，则使用比较函数`func`来排序 |

## Python元组

元组是一系列不可变的Python对象。元组是一种序列，就像列表一样。元组和列表之间的主要区别是元组不能像列表那样改变元素的值，可以简单地理解为“只读列表”。 元组使用小括号 - `()`，而列表使用方括号 - `[]` 。

创建一个元组只需使用逗号分隔值放入小括号的一个序列。 或者，也可以将这些逗号分隔值放在括号之间。 例如 -

```python
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
Python
```

空的元组写成两个不含任何东西的小括号 -

```python
tup1 = ();
Python
```

要编写一个包含单个值的元组，必须包含一个逗号，即使只有一个值(这是规范写法) -

```python
tup1 = (50,)
### 也可以这样写
tup2 = (50)
Python
```

### 1.访问元组中的值

要访问元组中的值，请使用方括号进行指定索引切片或索引，以获取该索引处的值。 例如 -

```shell
##!/usr/bin/python3

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
Shell
```

当执行上述代码时，会产生以下结果 -

```python
tup1[0]:  physics
tup2[1:5]:  (2, 3, 4, 5)
Python
```

### 2.更新元组

元组是不可变的，这意味着我们无法更新或更改元组元素的值。 但是可以使用现有元组的一部分来创建新的元组，如下例所示：

```python
##!/usr/bin/python3

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

## Following action is not valid for tuples
## tup1[0] = 100;

## So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)
Python
```

当执行上述代码时，会产生以下结果 -

```shell
(12, 34.56, 'abc', 'xyz')
Shell
```

### 3.删除元组元素

删除单个元组元素是不可能的。 当然，将不必要的元素放在另一个元组中也没有什么错。

要显式删除整个元组，只需使用`del`语句。 例如 -

```python
##!/usr/bin/python3

tup = ('physics', 'chemistry', 1997, 2000);

print (tup)
del tup;
print "After deleting tup : "
print (tup)
Python
```

执行上面代码，将产生以下结果 - 

> 注 - 引发异常。这是因为在`del tup`之后，元组不再存在。

```shell
('physics', 'chemistry', 1997, 2000)
After deleting tup :
Traceback (most recent call last):
   File "test.py", line 9, in <module>
      print tup;
NameError: name 'tup' is not defined
Shell
```

### 4.基本元组操作

元组响应`+`和`*`运算符很像字符串; 它们执行连接和重复操作，但结果是一个新的元组，而不是一个字符串。

事实上，元组中类似字符串操作和使用的所有常规序列操作都有作了讲解。

| Python表达式                              | 结果                           | 描述     |
| ----------------------------------------- | ------------------------------ | -------- |
| `len((1, 2, 3))`                          | `3`                            | 长度     |
| `(1, 2, 3) + (4, 5, 6)`                   | `(1, 2, 3, 4, 5, 6)`           | 连接操作 |
| `('Hi!',) * 4`                            | `('Hi!', 'Hi!', 'Hi!', 'Hi!')` | 重复     |
| `3 in (1, 2, 3)`                          | `True`                         | 成员关系 |
| `for x in (1,2,3) : print (x, end = ' ')` | `1 2 3`                        | 迭代     |

### 5.索引，切片和矩阵

由于元组是序列，索引和切片的工作方式与列表的工作方式相同，假设输入以下值：

```python
T=('C++', 'Java', 'Python')
Python
```

那么 - 

| Python表达式 | 结果                 |                  |
| ------------ | -------------------- | ---------------- |
| `T[2]`       | `'Python'`           | 偏移量，从零开始 |
| `T[-2]`      | `'Java'`             | 负数：从右到左   |
| `T[1:]`      | `('Java', 'Python')` | 切片提取部分     |

### 6.内置元组函数功能

Python包括以下元组函数 -

| 编号 | 函数                                                         | 描述                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 1    | [cmp(tuple1, tuple2)](http://www.yiibai.com/python/tuple_cmp.html) | 比较两个元组的元素。 |
| 2    | [len(tuple)](http://www.yiibai.com/python/tuple_len.html)    | 给出元组的总长度。   |
| 3    | [max(tuple)](http://www.yiibai.com/python/tuple_max.html)    | 从元组返回最大值项。 |
| 4    | [min(tuple)](http://www.yiibai.com/python/tuple_min.html)    | 从元组返回最大值项   |
| 5    | [tuple(seq)](http://www.yiibai.com/python/tuple_tuple.html)  | 将列表转换为元组。   |

#### Python字典

每个键与其值使用一个冒号(`:`)分开，这些键-值对是使用逗号分隔的，整个字典项目用大括号括起来。 没有任何项目的空字典只用两个花括号写成：`{}`

键在字典中是唯一的，而值可以不必是唯一的。字典的值可以是任何类型的，但是键必须是不可变的数据类型，例如字符串，数字或元组。

### 1.访问字典中的值

要访问字典元素，可以使用熟悉的中括号以及键来获取其值。 以下是一个简单的例子 -

```python
##!/usr/bin/python3

dict = {'Name': 'Maxsu', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
Python
```

当执行上述代码时，会产生以下结果 -

```shell
dict['Name']:  Maxsu
dict['Age']:  7
Shell
```

如果尝试使用键(不是字典的一部分)访问数据项，会收到以下错误，如下示例 -

```python
##!/usr/bin/python3

dict = {'Name': 'Maxsu', 'Age': 7, 'Class': 'First'}
print ("dict['Minsu']: ", dict['Minsu'])
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Minsu'
Shell
```

### 2.更新字典

可以通过添加新数据项或键值对，修改现有数据项或删除现有数据项来更新字典，如下面给出的简单示例所示。

```python
##!/usr/bin/python3

dict = {'Name': 'Maxsu', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
Python
```

当执行上述代码时，会产生以下结果 -

```shell
dict['Age']:  8
dict['School']:  DPS School
Shell
```

### 3.删除词典元素

可以删除单个字典元素或清除字典的全部内容。也可以在单个操作中删除整个字典。

要显式删除整个字典，只需使用`del`语句。 以下是一个简单的例子 -

```python
##!/usr/bin/python3

dict = {'Name': 'Maxsu', 'Age': 7, 'Class': 'First'}

del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict         # delete entire dictionary

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
Python
```

这产生以下结果：程序抛出了一个例外，因为在执行`del dict`之后，字典不再存在。

```shell
print ("dict['Age']: ", dict['Age'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
>>> print ("dict['School']: ", dict['School'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
Shell
```

> 注 - `del()`方法将在后续章节中讨论。

### 4. 字典键的属性

字典值没有限制。它们可以是任意任意的Python对象，标准对象或用户定义的对象。 但是，对于键来说也是如此。

关于字典的键有两个要点：

**(a)**. 不允许每键多于数据值。这意味着不允许重复的键。 在分配过程中遇到重复键时，则以最后一个赋值为准。 例如 -

```python
##!/usr/bin/python3

dict = {'Name': 'Maxsu', 'Age': 7, 'Name': 'Minlee'}
print ("dict['Name']: ", dict['Name'])
Python
```

当执行上述代码时，会产生以下结果 -

```shell
dict['Name']:  Minlee
Shell
```

**(b)**. 键必须是不可变的。 这意味着可以使用字符串，数字或元组作为字典键，但不允许使用`['key']`。 以下是一个简单的例子 -

```python
##!/usr/bin/python3

dict = {['Name']: 'Maxsu', 'Age': 7}
print ("dict['Name']: ", dict['Name'])
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Traceback (most recent call last):
   File "test.py", line 3, in <module>
      dict = {['Name']: 'Maxsu', 'Age': 7}
TypeError: list objects are unhashable
Shell
```

### 5.内置词典函数和方法

Python包括以下字典函数 -

| 编号 | 函数                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | cmp(dict1, dict2)                                            | 在*Python 3*中不再可用。                                     |
| 2    | [len(dict)](http://www.yiibai.com/python/dictionary_len.html) | 计算出字典的总长度。它将等于字典中的数据项数目。             |
| 3    | [str(dict)](http://www.yiibai.com/python3/dictionary_str.html) | 生成字典的可打印字符串表示形式                               |
| 4    | [type(variable)](http://www.yiibai.com/python/dictionary_type.html) | 返回传递变量的类型。如果传递变量是字典，那么它将返回一个字典类型。 |

Python包括以下字典方法 -

| 编号 | 函数                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [dict.clear()](http://www.yiibai.com/python/dictionary_clear.html) | 删除字典`dict`的所有元素                                     |
| 2    | [dict.copy()](http://www.yiibai.com/python/dictionary_copy.html) | 返回字典`dict`的浅拷贝                                       |
| 3    | [dict.fromkeys()](http://www.yiibai.com/python/dictionary_fromkeys.html) | 创建一个新的字典，其中包含`seq`的值和设置为`value`的值。     |
| 4    | [dict.get(key, default=None)](http://www.yiibai.com/python/dictionary_get.html) | 对于键(`key`)存在则返回其对应值，如果键不在字典中，则返回默认值 |
| 5    | [dict.has_key(key)](http://www.yiibai.com/python/dictionary_has_key.html) | 此方法已删除，使用`in`操作符代替                             |
| 6    | [dict.items()](http://www.yiibai.com/python/dictionary_items.html) | 返回字典`dict`的`(key，value)`元组对的列表                   |
| 7    | [dict.keys()](http://www.yiibai.com/python/dictionary_keys.html) | 返回字典`dict`的键列表                                       |
| 8    | [dict.setdefault(key, default = None)](http://www.yiibai.com/python/dictionary_setdefault.html) | 类似于`get()`，如果`key`不在字典`dict`中，则将执行赋值操作：`dict [key] = default` |
| 9    | [dict.update(dict2)](http://www.yiibai.com/python/dictionary_update.html) | 将字典`dict2`的键值对添加到字典`dict`                        |
| 10   | [dict.values()](http://www.yiibai.com/python/dictionary_values.html) | 返回字典`dict`的值列表                                       |



## Python日期和时间

Python程序可以通过多种方式处理日期和时间。日期格式之间的转换是计算机常见问题。Python的时间(`time`)和日历(`calendar`)模块可用于跟踪日期和时间。

#### 一些常用代码示例

- [获取当前时间和日期](http://www.yiibai.com/python/python_between_days.html)，如：2018-08-18 12：12：00
- [计算两个日期相差天数](http://www.yiibai.com/python/python_between_days.html)
- 计算程序运行的时间

```python
##!/usr/bin/python3
##coding=utf-8

import time  
import datetime  

starttime = datetime.datetime.now()  

time.sleep(5)  

endtime = datetime.datetime.now()  
print ((endtime - starttime).seconds )
Python
```

- 计算十天之后的日期时间

```python
##!/usr/bin/python3
##coding=utf-8

import time  
import datetime  

d1 = datetime.datetime.now()  
d3 = d1 + datetime.timedelta(days =10)  

print (str(d3))
print (d3.ctime())
Python
```

- 获取两个日期时间的时间差

```python
t = (datetime.datetime(2019,1,13,12,0,0) - datetime.datetime.now()).total_seconds()
print ("t = ", t)
### 输出结果
t = 49367780.076406
Python
```

Python中有提供与日期和时间相关的`4`个模块。它们分别是 - 

| 模块       | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| `time`     | `time`是一个仅包含与日期和时间相关的函数和常量的模块，在本模块中定义了`C/C++`编写的几个类。 例如，`struct_time`类。 |
| `datetime` | `datetime`是一个使用面向对象编程设计的模块，可以在Python中使用日期和时间。它定义了几个表示日期和时间的类。 |
| `calendar` | 日历是一个提供函数的模块，以及与`Calendar`相关的几个类，它们支持将日历映像生成为text，html，…. |
| `locale`   | 该模块包含用于格式化或基于区域设置分析日期和时间的函数。     |

### 1. 时间间隔

时间间隔是以秒为单位的浮点数。 从1970年1月1日上午12:00(*epoch*)，这是一种时间的特殊时刻表示。

在Python中，当前时刻与上述特殊的某个时间点之间以秒为单位的时间。这个时间段叫做Ticks。

![img](E:\git\python3-noteboook\python3教程.assets\700100641_71063.png)

`time`模块中的`time()`函数返回从1970年1月1日上午12点开始的秒数。

```python
## Import time module.
import time;

## Seconds
ticks = time.time()


print ("Number of ticks since 12:00am, January 1, 1970: ", ticks)
Python
```

执行上面代码，得到以下结果 - 

```shell
Number of ticks since 12:00am, January 1, 1970:  1497970093.6243818
Shell
```

但是，这个形式不能表示在时代(*1970年1月1日上午12:00*)之前的日期。在未来的日子也不能以这种方式表示 - 截止点是在`2038`年的UNIX和Windows的某个时刻。

### 2. 什么是TimeTuple？

许多Python时间函数将时间处理为`9`个数字的元组，如下所示：

| 索引 | 字段              | 值                        |
| ---- | ----------------- | ------------------------- |
| 0    | `4`位数，表示年份 | 2018，2019…               |
| 1    | 月份              | 1 ~ 12                    |
| 2    | 日期              | 1 ~ 31                    |
| 3    | 小时              | 0 ~ 23                    |
| 4    | 分钟              | 0 ~ 59                    |
| 5    | 秒                | 0 ~ 61(`60`或`61`是闰秒)  |
| 6    | 星期几            | 0 ~ 6(`0`是星期一)        |
| 7    | 一年的第几天      | 1 ~ 366(朱利安日)         |
| 8    | 夏令时            | -1，0，1，-1表示库确定DST |

**一个示例**

```python
import time
print (time.localtime());
Python
```

这将产生如下结果：

```shell
time.struct_time(tm_year = 2016, tm_mon = 2, tm_mday = 15, tm_hour = 9, 
   tm_min = 29, tm_sec = 2, tm_wday = 0, tm_yday = 46, tm_isdst = 0)
Shell
```

上面的元组相当于`struct_time`结构。此结构具有以下属性 -

| 索引 | 字段     | 值                        |
| ---- | -------- | ------------------------- |
| 0    | tm_year  | 2018，2019…               |
| 1    | tm_mon   | 1 ~ 12                    |
| 2    | tm_mday  | 1 ~ 31                    |
| 3    | tm_hour  | 0 ~ 23                    |
| 4    | tm_min   | 0 ~ 59                    |
| 5    | tm_sec   | 0 ~ 61(`60`或`61`是闰秒)  |
| 6    | tm_wday  | 0 ~ 6(`0`是星期一)        |
| 7    | tm_yday  | 1 ~ 366(朱利安日)         |
| 8    | tm_isdst | -1，0，1，-1表示库确定DST |

能用图片说明白的尽量用图片说明 - 

![img](E:\git\python3-noteboook\python3教程.assets\852100659_39889.png)

#### 2.1.获取当前时间

要将从时间浮点值开始的秒数瞬间转换为时间序列，将浮点值传递给返回具有所有有效九个项目的时间元组的函数(例如本地时间)。

```python
##!/usr/bin/python3
import time

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

## 当前时间
curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print (curtime)
Python
```

执行上面代码，这将产生如下结果 - 

```shell
Local current time : time.struct_time(tm_year=2017, tm_mon=6, tm_mday=20, tm_hour=23, tm_min=9, tm_sec=36, tm_wday=1, tm_yday=171, tm_isdst=0)
Curtime is =>  2017-06-20 23:09:36
Shell
```

#### 2.2.获取格式化时间

可以根据需要格式化任何时间，但也可使用可读格式获取时间的简单方法是 - `asctime()` -

```python
##!/usr/bin/python3
import time

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
Python
```

执行上面代码，这将产生如下结果 - 

```shell
Local current time : Mon Feb 15 10:32:13 2018
Shell
```

#### 2.3.获取一个月的日历

`calendar`模块提供了广泛的方法来显示年历和月度日历。 在这里，将打印一个给定月份的日历(2021年11月) -

```python
##!/usr/bin/python3
import calendar

cal = calendar.month(2021, 11)
print ("Here is the calendar:")
print (cal)
Python
```

执行上面代码后，将输出以下结果 - 

```shell
   November 2021
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
Shell
```

### 3.时间模块

Python中有一个受欢迎的时间(`time`)模块，它提供了处理时间和表示之间转换的功能。以下是所有时间(`time`)可用方法的列表。

| 编号 | 方法                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [time.altzone](http://www.yiibai.com/python/time_altzone.html) | 本地DST时区的偏移量(以秒为单位的UTC)，如果定义了有一个定义的话。 如果本地的DST时区是UTC的东部(如在西欧，包括英国)，那么它是负数值。 |
| 2    | [time.asctime([tupletime\])](http://www.yiibai.com/python/time_asctime.html) | 接受时间元组，并返回一个可读的`24`个字符的字符串，例如’Tue Dec 11 22:07:14 2019’。 |
| 3    | [time.clock( )](http://www.yiibai.com/python/time_clock.html) | 将当前CPU时间返回为浮点数秒。 为了测量不同方法的计算成本，`time.clock`的值比`time.time()`的值更有用。 |
| 4    | [time.ctime([secs\])](http://www.yiibai.com/python/time_ctime.html) | 类似于`asctime(localtime(secs))`，而没有参数就像`asctime()`  |
| 5    | [time.gmtime([secs\])](http://www.yiibai.com/python/time_gmtime.html) | 接受从时代(*epoch*)以秒为单位的瞬间，并返回与UTC时间相关的时间元组`t`。 注 - `t.tm_isdst`始终为`0` |
| 6    | [time.localtime([secs\])](http://www.yiibai.com/python/time_localtime.html) | 接受从时代(*epoch*)以秒为单位的瞬间，并返回与本地时间相关的时间`t`(`t.tm_isdst`为`0`或`1`，具体取决于DST是否适用于本地规则的瞬时秒)。 |
| 7    | [time.mktime(tupletime)](http://www.yiibai.com/python/time_mktime.html) | 接受在本地时间表示为时间元组的瞬间，并返回浮点值，该时间点以秒为单位表示。 |
| 8    | [time.sleep(secs)](http://www.yiibai.com/python/time_sleep.html) | 暂停调用线程`secs`秒。                                       |
| 9    | [time.strftime(fmt[,tupletime\])](http://www.yiibai.com/python/time_strftime.html) | 接受在本地时间表示为时间元组的瞬间，并返回一个表示由字符串`fmt`指定的时间的字符串。 |
| 10   | [time.strptime(str,fmt = ‘%a %b %d %H:%M:%S %Y’)](http://www.yiibai.com/python/time_strptime.html)“) | 根据格式字符串`fmt`解析`str`，并返回时间元组格式的时间。     |
| 11   | [time.time( )](http://www.yiibai.com/python/time_time.html)  | 返回当前时间时刻，即从时代(*epoch*)开始的浮点数秒数。        |
| 12   | [time.tzset()](http://www.yiibai.com/python/time_tzset.html) | 重置库例程使用的时间转换规则。环境变量`TZ`指定如何完成。     |

时间(`time`)模块有两个重要的属性可用。它们是 -

| 编号 | 属性            | 描述                                                         |
| ---- | --------------- | ------------------------------------------------------------ |
| 1    | `time.timezone` | 属性`time.timezone`是UTC和本地时区(不含DST)之间的偏移量(美洲为 > `0`，欧洲，亚洲，非洲大部分地区为 `0`)。 |
| 2    | `time.tzname`   | 属性`time.tzname`是一对与区域相关的字符串，它们分别是没有和具有DST的本地时区的名称。 |

### 4.日历模块

`calendar`模块提供与日历相关的功能，包括为给定的月份或年份打印文本日历的功能。

默认情况下，日历将星期一作为一周的第一天，将星期日作为最后一天。 如果想要更改这个，可调用`calendar.setfirstweekday()`函数设置修改。

以下是`calendar`模块可用的功能函数列表 -

| 编号 | 函数                                        | 描述                                                         |
| ---- | ------------------------------------------- | ------------------------------------------------------------ |
| 1    | `calendar.calendar(year,w = 2,l = 1,c = 6)` | 返回一个具有年份日历的多行字符串格式化为三列，以`c`个空格分隔。 `w`是每个日期的字符宽度; 每行的长度为`21 * w + 18 + 2 * c`，`l`是每周的行数。 |
| 2    | `calendar.firstweekday( )`                  | 返回当前设置每周开始的星期。默认情况下，当日历首次导入时设置为：`0`，表示为星期一。 |
| 3    | `calendar.isleap(year)`                     | 如果给定年份(`year`)是闰年则返回`True`; 否则返回：`False`。  |
| 4    | `calendar.leapdays(y1,y2)`                  | 返回在范围`(y1，y2)`内的年份中的闰年总数。                   |
| 5    | `calendar.month(year,month,w = 2,l = 1)`    | 返回一个多行字符串，其中包含年份月份的日历，每周一行和两个标题行。 `w`是每个日期的字符宽度; 每行的长度为`7 * w + 6`。 `l`是每周的行数。 |
| 6    | `calendar.monthcalendar(year,month)`        | 返回`int`类型的列表。每个子列表表示一个星期。年份月份以外的天数设置为`0`; 该月内的日期设定为月份的第几日：1 ~ 31。 |
| 7    | `calendar.monthrange(year,month)`           | 返回两个整数。第一个是年度月(`month`)的星期几的代码; 第二个是当月的天数。表示星期几为`0`(星期一)至`6`(星期日); 月份是`1`到`12`。 |
| 8    | `calendar.prcal(year,w = 2,l = 1,c = 6)`    | 类似于：`calendar.calendar(year，w，l，c)`的打印。           |
| 9    | `calendar.prmonth(year,month,w = 2,l = 1)`  | 类似于：`calendar.month(year,month,w,l)`的打印。             |
| 10   | `calendar.setfirstweekday(weekday)`         | 将每周的第一天设置为星期几的代码。 星期几的代码为`0`(星期一)至`6`(星期日)。 |
| 11   | `calendar.timegm(tupletime)`                | `time.gmtime`的倒数：以时间元组的形式接受时刻，并返回与从时代(`epoch`)开始的浮点数相同的时刻。 |
| 12   | `calendar.weekday(year,month,day)`          | 返回给定日期的星期几的代码。星期几的代码为`0`(星期一)至`6`(星期日); 月数是`1`(1月)到`12`(12月)。 |

### 5.其他模块和功能

如果您有兴趣，那么可以在Python中找到其他重要的模块和功能列表，其中包含日期和时间。以下列出其它有用的模块 -

- `datetime`模块
- `pytz`模块
- `dateutil`模块


## Python函数

函数是一个有组织，可重复使用的代码块，用于执行单个相关操作。 函数为应用程序提供更好的模块化和高度的代码重用。

我们知道，Python中也有给很多内置的函数，如`print()`等，但用户也可以创建自己的函数。这样的函数称为用户定义函数。

### 1.定义函数

可以定义提供所需函数的功能。 以下是在Python中定义函数的简单规则。

- 函数块以关键字`def`开头，后跟函数名和小括号(`()`)。
- 任何输入参数或参数应放置在这些小括号中。也可以在这些小括号内定义参数。
- 每个函数中的代码块以冒号(`:`)开始，并缩进。
- 函数内的第一个语句可以是可选语句 - 函数的文档或`docstring`字符串。
- 语句`return [expression]`用于退出一个函数，可选地将一个表达式传回给调用者。如果没有使用参数的`return`语句，则它与`return None`相同。

**语法**

```python
def functionname( parameters ):
    "function_docstring"
    function_suite
    return [expression]
Python
```

默认情况下，参数具有位置行为，您需要按照定义的顺序通知它们或调用它们。

**示例**

以下函数将字符串作为输入参数，并在标准屏幕上打印参数的值。

```python
def printme( str ):
    "This prints a passed string into this function"
    print (str)
    return
Python
```

### 2.调用函数

定义一个函数需要为它起一个名字，指定要包括在函数中的参数并构造代码块。
当函数的基本结构完成，可以通过从另一个函数调用它或直接从Python提示符执行它。 以下是一个调用`print_str()`函数的例子 -

```python
##!/usr/bin/python3

## Function definition is here
def print_str( str ):
   "This prints a passed string into this function"
   print (str)
   return

## Now you can call print_str function
print_str("This is first call to the user defined function!")
print_str("Again second call to the same function")
Python
```

当执行上述代码时，会产生以下结果 -

```shell
This is first call to the user defined function!
Again second call to the same function
Shell
```

### 3.通过引用与通过值传递

Python语言中的所有参数(参数)都将通过引用传递。如果在函数中更改参数所指的内容，则更改也会反映在调用函数的外部。 例如 -

```python
##!/usr/bin/python3

## Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   print ("Values inside the function before change: ", mylist)
   mylist[2]=50
   print ("Values inside the function after change: ", mylist)
   return

## Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)
Python
```

在这里，将保持对传递对象的引用并在相同的对象中赋值。 因此，这将产生以下结果 -

```shell
Values inside the function before change:  [10, 20, 30]
Values inside the function after change:  [10, 20, 50]
Values outside the function:  [10, 20, 50]
Shell
```

在上面的输出结果中，可以清楚地看到，`mylist[2]`的值原来只在函数内赋了一个值：`50`，但在函数外部的最后一个语句打出来的值是：`50`，这说明更改也会反映在调用函数的外部。

还有一个例子：参数通过引用传递，引用在被调用函数内被覆盖。

```python
##!/usr/bin/python3
##coding=utf-8

## Function definition is here
def changeme( mylist ):
    "This changes a passed list into this function"
    mylist = [1,2,3,4] # This would assi new reference in mylist
    print ("Values inside the function: ", mylist)
    return

## Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)
Python
```

参数`mylist`是`changeme()`函数的局部变量。在函数中更改`mylist`不影响`mylist`的值。函数执行完成后，最终将产生以下结果 -

```python
Values inside the function:  [1, 2, 3, 4]
Values outside the function:  [10, 20, 30]
Python
```

### 4.函数参数

可以使用以下类型的形式参数来调用函数 - 

- 必需参数
- 关键字参数
- 默认参数
- 可变长度参数

#### 4.1.必需参数

必需参数是以正确的位置顺序传递给函数的参数。这里，函数调用中的参数数量应与函数定义完全一致。

如下示例中，要调用`printme()`函数，则必需要传递一个参数，否则会出现如下语法错误 -

```python
##!/usr/bin/python3

## Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

## 现在要调用函数，但不提供参数
printme()
Python
```

当执行上述代码时，会产生以下结果 -

```python
Traceback (most recent call last):
   File "test.py", line 11, in <module>
      printme();
TypeError: printme() takes exactly 1 argument (0 given)
Python
```

> 提示：在调用 `printme()`函数时，提供一个参数就可以了。如：`printme('Maxsu')` 。

#### 4.2.关键字参数

关键字参数与函数调用有关。 在函数调用中使用关键字参数时，调用者通过参数名称来标识参数。

这允许跳过参数或将其置于无序状态，因为Python解释器能够使用提供的关键字将值与参数进行匹配。还可以通过以下方式对`printme()`函数进行关键字调用 -

```python
##!/usr/bin/python3
##coding=utf-8

## Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

## Now you can call printme function
printme( str = "My string")
Python
```

当执行上述代码时，会产生以下结果 -

```python
My string
Python
```

以下示例给出了更清晰的映射。请注意，参数的顺序并不重要。

```shell
##!/usr/bin/python3
##coding=utf-8

## Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name, "Age: ", age)
   return

## Now you can call printinfo function
printinfo( age = 25, name = "Maxsu" )
printinfo(name = "Minsu", age = 26 )
Shell
```

当执行上述代码时，会产生以下结果 -

```shell
Name:  Maxsu Age:  25
Name:  Minsu Age:  26
Shell
```

#### 4.3.默认参数

如果在该参数的函数调用中没有提供值，则默认参数是一个假设为默认值的参数。 以下示例给出了默认参数的想法，如果未通过，则打印默认年龄(`age`) -

```python
##!/usr/bin/python3
##coding=utf-8

## Function definition is here
def printinfo( name, age = 25 ):
   "This prints a passed info into this function"
   print ("Name: ", name, "Age ", age)
   return

## Now you can call printinfo function
printinfo( age = 22, name = "Maxsu" )
printinfo( name = "Minsu" )
Python
```

当执行上述代码时，会产生以下结果 - 

```shell
Name:  Maxsu Age  22
Name:  Minsu Age  25
Shell
```

#### 4.4.可变长度参数

在定义函数时，可能需要处理更多参数的函数。这些参数被称为可变长度参数，并且不像要求的和默认的参数那样在函数定义中命名。

具有非关键字变量参数的函数的语法如下：

```python
def functionname([formal_args,] *var_args_tuple ):
    "function_docstring"
    function_suite
    return [expression]
Python
```

星号(`*`)放在保存所有非关键字变量参数值的变量名之前。 如果在函数调用期间没有指定额外的参数，则此元组保持为空。以下是一个简单的例子 -

```python
##!/usr/bin/python3
##coding=utf-8

## Function definition is here
def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print ("Output is: ", arg1)
    for var in vartuple:
      print (var, )
    return

## Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Output is:  10
Output is:  70
60
50
Shell
```

### 5.匿名函数

这些函数被称为匿名的，因为它们没有使用`def`关键字以标准方式声明。可以使用`lambda`关键字创建小型匿名函数。

- `Lambda`表单可以接受任意数量的参数，但只能以表达式的形式返回一个值。它们不能包含命令或多个表达式。
- 匿名函数不能直接调用打印，因为`lambda`需要一个表达式。
- `Lambda`函数有自己的本地命名空间，不能访问其参数列表和全局命名空间中的变量。
- 虽然`lambdas`是一个单行版本的函数，但它们并不等同于`C`或`C++`中的内联语句，其目的是通过传递函数来进行堆栈分配。

**语法**

`lambda`函数的语法只包含一个语句，如下所示：

```python
lambda [arg1 [,arg2,.....argn]]:expression
Python
```

以下是一个示例，以显示`lambda`形式的函数如何工作 -

```python
##!/usr/bin/python3

## Function definition is here
sum = lambda arg1, arg2: arg1 + arg2


## Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))
Python
```

当执行上述代码时，会产生以下结果 -

```python
Value of total :  30
Value of total :  40
Python
```

### 6.return语句

`return [expression]`语句退出一个函数，可选地将一个表达式传回给调用者。没有参数的`return`语句与`return None`相同。

下面给出的所有例子都没有返回任何值。可以从函数返回值，如下所示：

```python
##!/usr/bin/python3
##coding=utf-8

## Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total

## Now you can call sum function
total = sum( 10, 20 )
print ("Outside the function : ", total )
Python
```

全部执行上述代码时，会产生以下结果 -

```shell
Inside the function :  30
Outside the function :  30
Shell
```

### 7.变量范围

程序中的所有变量在该程序的所有位置可能无法访问。这取决于在哪里声明一个变量。变量的范围决定了可以访问特定标识符的程序部分。Python中有两个变量的基本范围 -

- 全局变量
- 局部变量

### 8.全局与局部变量

在函数体内定义的变量具有局部作用域，外部定义的变量具有全局作用域。

局部变量只能在它们声明的函数内部访问，而全局变量可以通过所有函数在整个程序体中访问。 当调用一个函数时，它内部声明的变量被带入范围。 以下是一个简单的例子 -

```python
total = 0 # This is global variable.
## Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total

## Now you can call sum function
sum( 10, 20 )
print ("Outside the function global total : ", total )
Python
```

当执行上述代码时，会产生以下结果 -

```python
Inside the function local total :  30
Outside the function global total :  0
```



## Python模块

模块允许逻辑地组织Python代码。 将相关代码分组到一个模块中，使代码更容易理解和使用。 模块是一个具有任意命名属性的Python对象，可以绑定和引用。

简单来说，模块是一个由Python代码组成的文件。模块可以定义函数，类和变量。 模块还可以包括可运行的代码。

**示例**

下面是一个名称为`aname`的模块的Python代码通常位于一个名称为`aname.py`的文件中。以下是一个简单模块的例子：`support.py` -

```python
def print_func( par ):
   print "Hello : ", par
   return
Python
```

### 1.import语句

可以通过在其他Python源文件中执行`import`语句来将任何Python源文件用作模块。导入具有以下语法 -

```python
import module1[, module2[,... moduleN]
Python
```

当解释器遇到导入语句时，如果模块存在于搜索路径中，则导入该模块。搜索路径是导入模块之前解释器搜索的目录的列表。例如，要导入模块`hello.py`，需要将以下命令放在脚本的顶部 -

```python
##!/usr/bin/python3

## Import module support
import support

## Now you can call defined function that module as follows
support.print_func("Maxsu")
Python
```

当执行上述代码时，会产生以下结果 -

```python
Hello : Maxsu
Python
```

不管模块被导入多少次，模块只能加载一次。这样可以防止模块执行重复发生，如果有多个导入。

### 2.from…import语句

Python `from`语句允许将模块中的特定属性导入到当前的命名空间中。 `from...import`具有以下语法 -

```python
from modname import name1[, name2[, ... nameN]]
Python
```

例如，要从模块 `fib` 导入函数`fibonacci`，请使用以下语句 -

```python
##!/usr/bin/python3

## Fibonacci numbers module

def fib(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result
>>> from fib import fib
>>> fib(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Python
```

此语句不会将整个模块`fib`导入到当前命名空间中; 它只是将`fibonacci`从模块`fib`引入导入模块的全局符号表。

### 3.from…import *语句

也可以使用以下`import`语句将模块中的所有名称导入到当前命名空间中 -

```python
from modname import *
Python
```

这提供了将所有项目从模块导入到当前命名空间中的简单方法; 但是，这个说法应该谨慎使用。

### 4.执行模块作为脚本

在模块中，模块的名称(作为字符串)可用作全局变量`__name__`的值。模块中的代码将被执行，就像您导入它一样，但是`__name__`设置为“`__main__`”。

在模块的最后添加这个代码 -

```python
##!/usr/bin/python3

## Fibonacci numbers module

def fib(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result
if __name__ == "__main__":
   f = fib(100)
   print(f)
Python
```

运行上述代码时，将显示以下输出。

```python
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Python
```

### 5.定位模块

当导入模块时，Python解释器将按以下顺序搜索模块 -

- 当前目录。
- 如果没有找到该模块，Python会在shell变量`PYTHONPATH`中搜索每个目录。
- 如果其他所有失败，Python将检查默认路径。 在UNIX上，此默认路径通常是`/usr/local/lib/python3/` 或者 `/usr/sbin/`

模块搜索路径作为`sys.path`变量存储在系统模块`sys`中。`sys.path`变量包含当前目录`PYTHONPATH`和依赖于安装的默认值。

### 6.PYTHONPATH变量

`PYTHONPATH`是一个环境变量，由目录列表组成。 `PYTHONPATH`的语法与shell变量`PATH```的语法相同。

这是一个典型的Windows系统上的`PYTHONPATH` -

```shell
set PYTHONPATH = c:\python34\lib;
Shell
```

这里是UNIX系统的典型`PYTHONPATH` -

```shell
set PYTHONPATH = /usr/local/lib/python
Shell
```

### 7.命名空间和范围

变量是映射到对象的名称(标识符)。 命名空间是变量名(键)及其对应对象(值)的字典。

- Python语句可以访问本地命名空间和全局命名空间中的变量。如果本地和全局变量具有相同的名称，则局部变量会影响全局变量。
- 每个函数都有自己的本地命名空间。 类方法遵循与普通函数相同的范围规则。
- Python对于变量是本地还是全局都进行了有根据的判断。它假定在函数中分配值的任何变量都是本地的。
- 因此，为了将值分配给函数内的全局变量，必须首先使用`global`语句。
- 语句`global VarName`告诉Python `VarName`是一个全局变量。Python停止搜索本地命名空间的变量。

例如，在全局命名空间中定义一个变量`Money`。 在函数`Money`中为`Money`赋值，因此Python将`Money`作为局部变量。

但是，如果在设置之前就访问了本地变量`Money`的值，它会产生一个错误：`UnboundLocalError`。 这里可以通过取消注释`global`语句来解决问题。如下示例代码 - 

```python
##!/usr/bin/python3

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   # global Money
   Money = Money + 1

print (Money)
AddMoney()
print (Money)
Python
```

### 8.dir( )函数

`dir()`内置函数返回一个包含由模块定义的名称的字符串的排序列表。这个列表包含模块中定义的所有模块，变量和函数的名称。 以下是一个简单的例子 -

```python
##!/usr/bin/python3

## Import built-in module math
import time

content = dir(time)

print (content)
Python
```

当执行上述代码时，会产生以下结果 -

```shell
['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'clock', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'perf_counter', 'process_time', 'sleep', 'strftime', 'strptime', 'struct_time', 'time', 'timezone', 'tzname']
Shell
```

这里，特殊的字符串变量`__name__`是模块的名称，`__file__`是加载模块的文件名。

### 9.globals()和locals()函数

`globals()`和`locals()`函数可用于返回全局和本地命名空间中的名称，具体取决于它们被调用的位置。

- 如果`locals()`从一个函数中调用，它将返回从该函数本地访问的所有名称。
- 如果从函数中调用`globals()`，它将返回从该函数全局访问的所有名称。

这两个函数的返回类型是字典。 因此，可以使用`keys()`函数提取名称。

### 10.reload()函数

当将模块导入到脚本中时，模块的顶级部分的代码只能执行一次。
因此，如果要重新执行模块中的顶级代码，可以使用`reload()`函数。`reload()`函数再次导入以前导入的模块。 `reload()`函数的语法是这样的 -

```shell
reload(module_name)
Shell
```

这里，`module_name`是要重新加载的模块的名称，而不是包含模块名称的字符串。 例如，要重新加载`hello`模块，请执行以下操作 -

```python
reload(hello)
Python
```

### 11.Python中的包

Python中的包是一个分层文件目录结构，它定义了一个由模块和子包和子子包组成的Python应用程序环境，等等。

在`package`目录中创建两个目录：`pkg`和`pkg2`， 然后分别在这两个目录中创建两个文件：`a.py`和`b.py`。该文件具有以下一行源代码 -

*文件： pkg/a.py* - 

```python
##!/usr/bin/python3
##coding=utf-8
## save file: pkg/a.py
def fun():
    print ("I'm pkg.a.fun() ")
Python
```

*文件： pkg/b.py* - 

```python
##!/usr/bin/python3
##coding=utf-8
## save file: pkg/b.py
def fun():
    print ("I'm pkg.b.fun() ")
Python
```

*文件： pkg2/a.py* - 

```python
##!/usr/bin/python3
##coding=utf-8
## save file: pkg2/a.py
def fun():
    print ("I'm pkg2.a.fun() ")
Python
```

*文件： pkg2/b.py* - 

```python
##!/usr/bin/python3
##coding=utf-8
## save file: pkg2/b.py
def fun():
    print ("I'm pkg2.b.fun() ")
Python
```

在`package`目录中创建一个主程序文件：`main.py`，用于演示如何调用包中的各个文件 - 

```python
##!/usr/bin/python3
##coding=utf-8
## save file: phone/pots.py

import pkg.a as a
import pkg.b as b

import pkg2.a as a2
import pkg2.b as b2

a.fun()
b.fun()

a2.fun()
b2.fun()

import pkg2.a
import pkg2.b

print('----------- another way -----------------')
pkg2.a.fun()
pkg2.b.fun()
Python
```

整个代码的目录如下所示 - 

```shell
package
  |- pkg
      |- __init__.py
      |- a.py
      |- b.py
  |- pkg2
      |- __init__.py
      |- a.py
      |- b.py
Shell
```

当执行上述代码时，会产生以下结果 -

```shell
I'm pkg.a.fun() 
I'm pkg.b.fun() 
I'm pkg2.a.fun() 
I'm pkg2.b.fun() 
----------- another way -----------------
I'm pkg2.a.fun() 
I'm pkg2.b.fun()
Shell
```

在上面的例子中，将每个文件中的一个函数作为示例，但是可以在文件中编写多个函数。还可以在这些文件中定义不同的Python类，然后可以使用这些类来创建包。



## Python文件读写

在本章中将介绍*Python 3*中可用的所有基本文件读取*I/O*功能。有关更多功能，请参考标准Python文档。

### 打印到屏幕

产生输出的最简单方法是使用`print`语句，可以传递零个或多个由逗号分隔的表达式。此函数将传递的表达式转换为字符串，并将结果写入标准输出，如下所示：

```python
##!/usr/bin/python3

print ("Python是世界上最牛逼的语言,", "难道不是吗?")
Python
```

执行上面代码后，将在标准屏幕上产生以下结果 -

```shell
Python是世界上最牛逼的语言, 难道不是吗?
Shell
```

### 从键盘读取输入

*Python 2*有两个内置的函数用于从标准输入读取数据，默认情况下来自键盘。这两个函数分别是：`input()`和`raw_input()`。

在*Python 3*中，不建议使用`raw_input()`函数。 `input()`函数可以从键盘读取数并作为字符串类型，而不管它是否用引号括起来(“或”“)。

```python
>>> x = input("input something:")
input something:yes,input some string
>>> x
'yes,input some string'
>>> x = input("input something:")
input something:1239900
>>> x
'1239900'
>>>
Python
```

### 打开和关闭文件

在前面我们学习读取和写入标准的输入和输出。 现在，来看看如何使用实际的数据文件。Python提供了默认操作文件所必需的基本功能和方法。可以使用文件对象执行大部分文件操作。

#### 打开文件

在读取或写入文件之前，必须使用Python的内置`open()`函数打开文件。此函数创建一个文件对象，该对象将用于调用与其相关联的其他支持方法。

**语法**

```python
file object = open(file_name [, access_mode][, buffering])
Python
```

这里是参数详细信息 -

- *file_name* - `file_name`参数是一个字符串值，指定要访问的文件的名称。
- *access_mode* - `access_mode`确定文件打开的模式，即读取，写入，追加等。可能的值的完整列表如下表所示。 这是一个可选参数，默认文件访问模式为(`r` - 也就是只读)。
- *buffering* - 如果`buffering`值设置为`0`，则不会发生缓冲。 如果缓冲值`buffering`为`1`，则在访问文件时执行行缓冲。如果将缓冲值`buffering`指定为大于`1`的整数，则使用指定的缓冲区大小执行缓冲操作。如果为负，则缓冲区大小为系统默认值(默认行为)。

以下是打开文件使用的模式的列表 -

| 编号 | 模式  | 描述                                                         |
| ---- | ----- | ------------------------------------------------------------ |
| 1    | `r`   | 打开的文件为只读模式。文件指针位于文件的开头，这是默认模式。 |
| 2    | `rb`  | 打开仅用二进制格式读取的文件。文件指针位于文件的开头，这是默认模式。 |
| 3    | `r+`  | 打开读写文件。文件指针放在文件的开头。                       |
| 4    | `rb+` | 以二进制格式打开一个用于读写文件。文件指针放在文件的开头。   |
| 5    | `w`   | 打开仅供写入的文件。 如果文件存在，则覆盖该文件。 如果文件不存在，则创建一个新文件进行写入。 |
| 6    | `wb`  | 打开仅用二进制格式写入的文件。如果文件存在，则覆盖该文件。 如果文件不存在，则创建一个新文件进行写入。 |
| 7    | `w+`  | 打开写入和取读的文件。如果文件存在，则覆盖现有文件。 如果文件不存在，创建一个新文件进行阅读和写入。 |
| 8    | `wb+` | 打开一个二进制格式的写入和读取文件。 如果文件存在，则覆盖现有文件。 如果文件不存在，创建一个新文件进行阅读和写入。 |
| 9    | `a`   | 打开一个文件进行追加。 如果文件存在，则文件指针位于文件末尾。也就是说，文件处于追加模式。如果文件不存在，它将创建一个新文件进行写入。 |
| 10   | `ab`  | 打开一个二进制格式的文件。如果文件存在，则文件指针位于文件末尾。 也就是说，文件处于追加模式。如果文件不存在，它将创建一个新文件进行写入。 |
| 11   | `a+`  | 打开一个文件，用于追加和阅读。 如果文件存在，则文件指针位于文件末尾。 文件以附加模式打开。 如果文件不存在，它将创建一个新文件进行阅读和写入。 |
| 12   | `ab+` | 打开一个二进制格式的附加和读取文件。 如果文件存在，则文件指针位于文件末尾。文件以附加模式打开。如果文件不存在，它将创建一个新文件进行读取和写入。 |

### 文件对象属性

打开一个文件并且有一个文件对象后，可以获得与该文件相关的各种信息。

以下是与文件对象相关的所有属性的列表 -

| 编号 | 属性          | 描述                                        |
| ---- | ------------- | ------------------------------------------- |
| 1    | `file.closed` | 如果文件关闭则返回`true`，否则返回`false`。 |
| 2    | `file.mode`   | 返回打开文件的访问模式。                    |
| 3    | `file.name`   | 返回文件的名称。                            |

> 注意 - *Python 3.x*中不支持`softspace`属性

**示例**

```python
##!/usr/bin/python3

## Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()
Python
```

执行上面代码，这产生以下结果 -

```shell
Name of the file:  foo.txt
Closed or not :  False
Opening mode :  wb
Shell
```

#### close()方法

文件对象的`close()`方法刷新任何未写入的信息并关闭文件对象，之后不能再进行写入操作。
当文件的引用对象重新分配给另一个文件时，Python也会自动关闭一个文件。但使用`close()`方法关闭文件是个好习惯。

**语法**

```python
fileObject.close();
Python
```

**示例**

```python
##!/usr/bin/python3

## Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)

## Close opened file
fo.close()
Python
```

执行上面代码，这产生以下结果 -

```shell
Name of the file:  foo.txt
Shell
```

### 读取和写入文件

文件对象提供了一组访问方法，使代码编写更方便。下面将演示如何使用`read()`和`write()`方法来读取和写入文件。

#### write()方法

`write()`方法将任何字符串写入打开的文件。 重要的是要注意，Python字符串可以是二进制数据，而不仅仅是文本。

`write()`方法不会在字符串的末尾添加换行符(‘`\n`‘)

**语法**

```python
fileObject.write(string);
Python
```

这里，传递参数 - `string` 是要写入打开文件的内容。

**示例**

```
##!/usr/bin/python3

## Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

## Close opend file
fo.close()
```

上述示例将创建一个`foo.txt`文件，并将给定的内容写入到该文件中，最后将关闭文件。 在执行上面语句后，如果打开文件(`foo.txt`)，它将应该以下内容 -

```shell
Python is a great language.
Yeah its great!!
Shell
```

#### read()方法

`read()`方法用于从打开的文件读取一个字符串。 重要的是要注意Python字符串除文本数据外可以是二进制数据。。

**语法**

```python
fileObject.read([count]);
Python
```

这里，传递参数 - `count`是从打开的文件读取的字节数。 该方法从文件的开始位置开始读取，如果`count`不指定值或丢失，则尽可能地尝试读取文件，直到文件结束。

**示例**

下面来一个文件`foo.txt`，这是上面示例中创建的。

```python
##!/usr/bin/python3

## Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

## Close opened file
fo.close()
Python
```

执行上面代码，这产生以下结果 -

```python
Read String is :  Python is
Python
```

### 文件位置

`tell()`方法用于获取文件中的当前位置; 换句话说，下一次读取或写入将发生在从文件开始处之后的多个字节数的位置。

`seek(offset [，from])`方法更改当前文件位置。 `offset`参数表示要移动的字节数。 `from`参数指定要移动字节的引用位置。

如果`from`设置为`0`，则将文件的开头作为参考位置。 如果设置为`1`，则将当前位置用作参考位置。 如果设置为`2`，则文件的末尾将被作为参考位置。

**示例**

下面来一个文件`foo.txt`，这是上面示例中创建的。

```python
##!/usr/bin/python3

## Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

## Check current position
position = fo.tell()
print ("Current file position : ", position)

## Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print ("Again read String is : ", str)

## Close opened file
fo.close()
Python
```

执行上面代码，这产生以下结果 -

```python
Read String is :  Python is
Current file position :  10
Again read String is :  Python is
Python
```

### 重命名和删除文件

Python os模块提供用于执行文件处理操作(如重命名和删除文件)的方法。要使用此模块，需要先将它导入，然后可以调用任何相关的函数。

#### rename()方法

`rename()`方法有两个参数，即当前的文件名和新的文件名。

**语法**

```python
os.rename(current_file_name, new_file_name)
Python
```

**示例**

以下是一个将现有文件`test1.txt`重命名为`test2.txt`的示例 -

```python
##!/usr/bin/python3
import os

## Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )
Python
```

#### remove()方法

使用`remove()`方法并通过提供要删除的文件的名称作为参数来删除文件。

**语法**

```python
os.remove(file_name)
Python
```

**示例**

以下是删除现有文件`test2.txt`的示例 -

```python
##!/usr/bin/python3
import os

## Delete file test2.txt
os.remove("text2.txt")
Python
```

### Python中的目录

所有文件都包含在各种目录中，Python处理目录问题也很容易。 `os`模块有几种方法可以用来创建，删除和更改目录。

#### mkdir()方法

使用`os`模块的`mkdir()`方法在当前目录中创建目录。需要为此方法提供一个参数，指定要创建的目录的名称。

**语法**

```python
os.mkdir("newdir")
Python
```

**示例**

以下是在当前目录中创建一个目录：`test` 的示例 -

```python
##!/usr/bin/python3
import os

## Create a directory "test"
os.mkdir("test")
Python
```

使用`chdir()`方法来更改当前目录。 `chdir()`方法接受一个参数，它是要选择作为当前目录的目录的名称。

**语法**

```python
os.chdir("newdir")
Python
```

**示例**

以下是进入“`/home/newdir`”目录的示例 -

```python
##!/usr/bin/python3
import os

## Changing a directory to "/home/newdir"
os.chdir("/home/newdir")
Python
```

#### getcwd()方法

`getcwd()`方法用于显示当前工作目录。

```python
os.getcwd()
Python
```

**示例**

以下是给出当前目录的一个例子 -

```python
##!/usr/bin/python3
import os

## This would give location of the current directory
os.getcwd()
Python
```

#### rmdir()方法

`rmdir()`方法删除该方法中作为参数传递的目录。删除目录之前，应删除其中的所有内容。

```python
os.rmdir('dirname')
Python
```

**示例**

以下是删除“`/tmp/test`”目录的示例。需要给出目录的完全限定名称，否则将在当前目录中搜索该目录。

```python
##!/usr/bin/python3
import os

## This would  remove "/tmp/test"  directory.
os.rmdir( "/tmp/test"  )
Python
```

### 文件和目录相关方法

有三个重要的来源，它们提供了广泛的实用方法来处理和操作Windows和Unix操作系统上的文件和目录。它们如下 -

- [文件对象和方法](http://www.yiibai.com/python/file_methods.html) - 文件对象提供了操作文件的功能。
- [OS对象和方法](http://www.yiibai.com/python/os_file_methods.html) - 这提供了处理文件和目录的方法。



# 面向对象

## Python面向对象（类和对象）

自从存在以来，Python一直是面向对象的语言。 因此，创建和使用类和对象是非常容易的。 本章将学习如何使用Python面向对象编程。

如果您以前没有面向对象(OO)编程的经验，可能需要查阅介绍面向对象(OO)编程课程或至少学习一些有关教程，以便掌握基本概念。

下面是面向对象编程(OOP)的一个小介绍，以帮助您快速入门学习 -

**OOP术语概述** 

- **类** - 用于定义表示用户定义对象的一组属性的原型。属性是通过点符号访问的数据成员(类变量和实例变量)和方法。
- **类变量** - 由类的所有实例共享的变量。 类变量在类中定义，但在类的任何方法之外。 类变量不像实例变量那样频繁使用。
- **数据成员** - 保存与类及其对象相关联的数据的类变量或实例变量。
- **函数重载** - 将多个行为分配给特定函数。 执行的操作因涉及的对象或参数的类型而异。
- **实例变量** - 在方法中定义并仅属于类的当前实例的变量。
- **继承** - 将类的特征传递给从其派生的其他类。
- **实例** - 某个类的单个对象。 例如，对象`obj`属于`Circle`类，它是`Circle`类的实例。
- **实例化** - 创建类的实例。
- **方法** - 在类定义中定义的一种特殊类型的函数。
- **对象** - 由其类定义的数据结构的唯一实例。对象包括数据成员(类变量和实例变量)和方法。
- **运算符重载** - 将多个函数分配给特定的运算符。

### 1.创建类

`class`语句创建一个新的类定义。 类的名称紧跟在`class`关键字之后，在类的名称之后紧跟冒号，如下 -

```python
class ClassName:
   'Optional class documentation string'
   class_suite
Python
```

- 该类有一个文档字符串，可以通过`ClassName.__doc__`访问。
- `class_suite`由定义类成员，数据属性和函数的所有组件语句组成。

**示例**

以下是一个简单的Python类的例子 -

```python
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
Python
```

- 变量`empCount`是一个类变量，其值在此类中的所有实例之间共享。 这可以从类或类之外的`Employee.empCount`访问。
- 第一个方法`__init __()`是一种特殊的方法，当创建此类的新实例时，该方法称为Python构造函数或初始化方法。
- 声明其他类方法，如正常函数，但每个方法的第一个参数是`self`。 Python将`self`参数添加到列表中; 调用方法时不需要包含它。

### 2.创建实例对象

要创建类的实例，可以使用类名调用该类，并传递其`__init__`方法接受的任何参数。

```python
### This would create first object of Employee class
emp1 = Employee("Maxsu", 2000)
### This would create second object of Employee class
emp2 = Employee("Kobe", 5000)
Python
```

### 3.访问属性

可以使用带有对象的点(`.`)运算符来访问对象的属性。 类变量将使用类名访问如下 -

```python
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
Python
```

现在把所有的概念放在一起 -

```python
##!/usr/bin/python3

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


##This would create first object of Employee class"
emp1 = Employee("Maxsu", 2000)
##This would create second object of Employee class"
emp2 = Employee("Kobe", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
Python
```

当执行上述代码时，会产生以下结果 -

```python
Name :  Maxsu ,Salary:  2000
Name :  Kobe ,Salary:  5000
Total Employee 2
Python
```

可以随时添加，删除或修改类和对象的属性 -

```python
emp1.salary = 7000  # Add an 'salary' attribute.
emp1.name = 'xyz'  # Modify 'age' attribute.
del emp1.salary  # Delete 'age' attribute.
Python
```

如果不是使用普通语句访问属性，可以使用以下函数 -

- `getattr(obj，name [，default])` - 访问对象的属性。
- `hasattr(obj，name)` - 检查属性是否存在。
- `setattr(obj，name，value)` - 设置一个属性。如果属性不存在，那么它将被创建。
- `delattr(obj，name)` - 删除一个属性。

下面是一此使用示例 - 

```python
hasattr(emp1, 'salary')    # Returns true if 'salary' attribute exists
getattr(emp1, 'salary')    # Returns value of 'salary' attribute
setattr(emp1, 'salary', 7000) # Set attribute 'salary' at 7000
delattr(emp1, 'salary')    # Delete attribute 'salary'
Python
```

### 3.内置类属性

每个Python类保持以下内置属性，并且可以像任何其他属性一样使用点运算符访问它们 -

- `__dict__` - 包含该类的命名空间的字典。
- `__doc__` - 类文档字符串或无，如果未定义。
- `__name__` - 类名。
- `__module__` - 定义类的模块名称。此属性在交互模式下的值为“**main**”。
- `__bases__` - 一个包含基类的空元组，按照它们在基类列表中出现的顺序。

对于上述类，尝试访问所有这些属性 -

```python
##!/usr/bin/python3

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Maxsu", 2000)
emp2 = Employee("Bryant", 5000)
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )
Python
```

当执行上述代码时，会产生以下结果 -

```python
Employee.__doc__: Common base class for all employees
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: (<class 'object'>,)
Employee.__dict__: {
   'displayCount': <function Employee.displayCount at 0x0160D2B8>, 
   '__module__': '__main__', '__doc__': 'Common base class for all employees', 
   'empCount': 2, '__init__': 
   <function Employee.__init__ at 0x0124F810>, 'displayEmployee': 
   <function Employee.displayEmployee at 0x0160D300>,
   '__weakref__': 
   <attribute '__weakref__' of 'Employee' objects>, '__dict__': 
   <attribute '__dict__' of 'Employee' objects>
}
Python
```

### 4.销毁对象(垃圾收集)

Python自动删除不需要的对象(内置类型或类实例)以释放内存空间。 Python定期回收不再使用的内存块的过程称为垃圾收集。

Python的垃圾收集器在程序执行期间运行，当对象的引用计数达到零时触发。 对象的引用计数随着指向它的别名数量而变化。

当对象的引用计数被分配一个新名称或放置在容器(列表，元组或字典)中时，它的引用计数会增加。 当用`del`删除对象的引用计数时，引用计数减少，其引用被重新分配，或者其引用超出范围。 当对象的引用计数达到零时，Python会自动收集它。

```python
a = 40      # Create object <40>
b = a       # Increase ref. count  of <40> 
c = [b]     # Increase ref. count  of <40> 

del a       # Decrease ref. count  of <40>
b = 100     # Decrease ref. count  of <40> 
c[0] = -1   # Decrease ref. count  of <40>
Python
```

通常情况下，垃圾回收器会销毁孤立的实例并回收其空间。 但是，类可以实现调用析构函数的特殊方法`__del__()`，该方法在实例即将被销毁时被调用。 此方法可能用于清理实例使用的任何非内存资源。

**示例**

这个`__del__()`析构函数打印要被销毁的实例的类名 -

```python
##!/usr/bin/python3

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3));   # prints the ids of the obejcts
del pt1
del pt2
del pt3
Python
```

当执行上述代码时，会产生以下结果 -

```python
3083401324 3083401324 3083401324
Point destroyed
Python
```

> 注意 - 理想情况下，应该在单独的文件中定义类，然后使用`import`语句将其导入主程序文件。

在上面的例子中，假定`Point`类的定义包含在`point.py`中，并且其中没有其他可执行代码。

```python
##!/usr/bin/python3
import point
p1 = point.Point()
Python
```

### 5.类继承

使用类继承不用从头开始构建代码，可以通过在新类名后面的括号中列出父类来从一个预先存在的类派生它来创建一个类。

子类继承其父类的属性，可以像子类中一样定义和使用它们。子类也可以从父类代替代数据成员和方法。

**语法**

派生类被声明为很像它们的父类; 然而，继承的基类的列表在类名之后给出 -

```python
class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite
Python
```

**示例**

```python
##!/usr/bin/python3

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
Python
```

当执行上述代码时，会产生以下结果 -

```python
Calling child constructor
Calling child method
Calling parent method
Parent attribute : 200
Python
```

以类似的方式，可以从多个父类来构建一个新的类，如下所示：

```python
class A:        # define your class A
.....

class B:         # define your calss B
.....

class C(A, B):   # subclass of A and B
.....
Python
```

可以使用`issubclass()`或`isinstance()`函数来检查两个类和实例之间的关系。

- `issubclass(sub，sup)`布尔函数如果给定的子类`sub`确实是超类`sup`的子类返回`True`。
- `isinstance(obj，Class)`布尔函数如果`obj`是类`Class`的一个实例，或者是类的一个子类的实例则返回`True`。

#### 重载方法

可以随时重载父类的方法。 重载父方法的一个原因是：您可能希望在子类中使用特殊或不同的方法功能。

**示例**

```python
##!/usr/bin/python3

class Parent:        # define parent class
   def myMethod(self):
      print ('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.myMethod()         # child calls overridden method
Python
```

当执行上述代码时，会产生以下结果 -

```python
Calling child method
Python
```

#### 基本重载方法

下表列出了可以在自己的类中覆盖的一些通用方法 -

| 编号 | 方法                           | 描述                     | 调用示例                |
| ---- | ------------------------------ | ------------------------ | ----------------------- |
| 1    | `__init__ ( self [,args...] )` | 构造函数(带任意可选参数) | `obj = className(args)` |
| 2    | `__del__( self )`              | 析构函数，删除一个对象   | `del obj`               |
| 3    | `__repr__( self )`             | 可评估求值的字符串表示   | `repr(obj)`             |
| 4    | `__str__( self )`              | 可打印的字符串表示       | `str(obj)`              |
| 5    | `__cmp__ ( self, x )`          | 对象比较                 | `cmp(obj, x)`           |

### 6.重载运算符

假设已经创建了一个`Vector`类来表示二维向量。当使用加号(`+`)运算符执行运算时，它们会发生什么？ 很可能Python理解不了你想要做什么。

但是，可以在类中定义`__add__`方法来执行向量加法，然后将按照期望行为那样执行加法运算 -

**示例**

```python
##!/usr/bin/python3

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
Python
```

当执行上述代码时，会产生以下结果 -

```python
Vector(7,8)
Python
```

### 7.数据隐藏

对象的属性在类定义之外可能或不可见。需要使用双下划线前缀命名属性，然后这些属性将不会直接对外部可见。

**示例**

```python
##!/usr/bin/python3

class JustCounter:
   __secretCount = 0

   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter.__secretCount)
Python
```

当执行上述代码时，会产生以下结果 -

```shell
1
2
Traceback (most recent call last):
   File "test.py", line 12, in <module>
      print counter.__secretCount
AttributeError: JustCounter instance has no attribute '__secretCount'
Shell
```

Python通过内部更改名称来包含类名称来保护这些成员。 可以访问`object._className__attrName`等属性。如果将最后一行替换为以下，那么它适用于 -

```python
.........................
print (counter._JustCounter__secretCount)
Python
```

当执行上述代码时，会产生以下结果 -

```shell
1
2
2
```



## Python构造函数

构造函数是一种特殊类型的方法(函数)，它在类的实例化对象时被调用。 构造函数通常用于初始化(赋值)给实例变量。 构造函数还验证有足够的资源来使对象执行任何启动任务。

**创建一个构造函数**

构造函数是以双下划线(`__`)开头的类函数。构造函数的名称是`__init__()`。

创建对象时，如果需要，构造函数可以接受参数。当创建没有构造函数的类时，Python会自动创建一个不执行任何操作的默认构造函数。

每个类必须有一个构造函数，即使它只依赖于默认构造函数。

**举一个例子：**

创建一个名为`ComplexNumber`的类，它有两个函数`__init__()`函数来初始化变量，并且有一个`getData()`方法用来显示数字。

看这个例子：

```python
##!/usr/bin/python3
##coding=utf-8

class ComplexNumber:

    def __init__(self, r = 0, i = 0):
        """"初始化方法"""
        self.real = r 
        self.imag = i 

    def getData(self):
        print("{0}+{1}j".format(self.real, self.imag))

if __name__ == '__main__':
    c = ComplexNumber(5, 6)
    c.getData()
Python
```

执行上面代码，得到以下结果 - 

```shell
5+6j
Shell
```

可以为对象创建一个新属性，并在定义值时进行读取。但是不能为已创建的对象创建属性。

看这个例子：

```python
##!/usr/bin/python3
##coding=utf-8

class ComplexNumber:

    def __init__(self, r = 0, i = 0):
        """"初始化方法"""
        self.real = r 
        self.imag = i 

    def getData(self):
        print("{0}+{1}j".format(self.real, self.imag))

if __name__ == '__main__':
    c = ComplexNumber(5, 6)
    c.getData()

    c2 = ComplexNumber(10, 20)
    # 试着赋值给一个未定义的属性
    c2.attr = 120
    print("c2 = > ", c2.attr)

    print("c.attr => ", c.attr)
Python
```

执行上面代码，得到以下结果 - 

```shell
5+6j
c2 = >  120
Traceback (most recent call last):
  File "D:\test.py", line 23, in <module>
    print("c.attr => ", c.attr)
AttributeError: 'ComplexNumber' object has no attribute 'attr'
```


## Python继承

**什么是继承？**

继承用于指定一个类将从其父类获取其大部分或全部功能。 它是面向对象编程的一个特征。 这是一个非常强大的功能，方便用户对现有类进行几个或多个修改来创建一个新的类。新类称为子类或派生类，从其继承属性的主类称为基类或父类。

子类或派生类继承父类的功能，向其添加新功能。 它有助于代码的可重用性。

下图表示：

![img](E:\git\python3-noteboook\python3教程.assets\955200640_89651.png)

![img](E:\git\python3-noteboook\python3教程.assets\847200644_72619.png)

**语法-1**

```python
class DerivedClassName(BaseClassName):  
    <statement-1>  
    .  
    .  
    .  
    <statement-N>
Python
```

**语法-2**

```python
class DerivedClassName(modulename.BaseClassName):  
    <statement-1>  
    .  
    .  
    .  
    <statement-N>
Python
```

**参数说明**

必须在包含派生类定义的范围中定义名称`BaseClassName`。还可以使用其他任意表达式代替基类名称。 当在另一个模块中定义基类时要指定模块的名称。

Python继承示例

我们来看一个简单的python继承示例，在这个示例中使用两个类：`Animal`和`Dog`。`Animal`是父类或基类，`Dog`是`Animal`的子类。

在这里，在`Animal`类中定义了`eat()`方法，`Dog`类中定义了`bark()`方法。 在这个例子中，我们创建`Dog`类的实例，并且仅通过子类的实例调用`eat()`和`bark()`方法。 由于父属性和行为自动继承到子对象，所以通过子实例也可以调用父类和子类的方法。

```python
class Animal:   
    def eat(self):  
      print 'Eating...'  
class Dog(Animal):     
   def bark(self):  
      print 'Barking...'  

d=Dog()  
d.eat()  
d.bark()
Python
```

执行上面代码，得到以下结果 - 

```python
Eating...  
Barking...
```


## Python多重继承

在本文中，您将了解Python中的多重继承以及如何在程序中使用它。还将了解多级继承和方法解析顺序。

![img](E:\git\python3-noteboook\python3教程.assets\451080631_51525.jpg)

与C++一样，一个类可以从Python中的多个基类派生出来。这被称为多重继承。

在多重继承中，所有基类的特征都被继承到派生类中。多重继承的语法类似于单继承。

**Python多重继承示例**

```python
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
Python
```

这里，`MultiDerived`派生自`Base1`和`Base2`类。

![img](E:\git\python3-noteboook\python3教程.assets\697080634_93411.jpg)

`MultiDerived`类从`Base1`和`Base2`继承。

### Python中的多层继承

另一方面，我们也可以继承一个派生类的形式。这被称为多级继承。 它可以在Python中有任何的深度(层级)。在多级继承中，基类和派生类的特性被继承到新的派生类中。
下面给出了具有相应可视化的示例。

```python
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass
Python
```

这里，`Derived1`派生自`Base`，`Derived2`派生自`Derived1`。

![img](E:\git\python3-noteboook\python3教程.assets\238080640_87576.jpg)

### Python中的方法解析顺序

Python中的每个类都派生自类:`object`。它是Python中最基础的类型。

所以在技术上，所有其他类，无论是内置还是用户定义，都是派生类，所有对象都是对象类的实例。

```python
## Output: True
print(issubclass(list,object))

## Output: True
print(isinstance(5.5,object))

## Output: True
print(isinstance("Hello",object))
Python
```

在多继承方案中，在当前类中首先搜索任何指定的属性。如果没有找到，搜索继续进入父类，深度优先，再到左右的方式，而不需要搜索相同的类两次。

所以在`MultiDerived`类的上面的例子中，搜索顺序是`[MultiDerived，Base1，Base2，object]`。 此顺序也称为`MultiDerived`类的线性化，用于查找此顺序的一组规则称为方法解析顺序(MRO)。

MRO必须防止本地优先排序，并提供单调性。它确保一个类总是出现在其父类之前，并且在多个父类的情况下，该顺序与基类的元组相同。

一个类的MRO可以被看作是`__mro__`属性或者`mro()`方法。前者返回一个元组，而后者返回一个列表。

```python
>>> MultiDerived.__mro__
(<class '__main__.MultiDerived'>,
 <class '__main__.Base1'>,
 <class '__main__.Base2'>,
 <class 'object'>)

>>> MultiDerived.mro()
[<class '__main__.MultiDerived'>,
 <class '__main__.Base1'>,
 <class '__main__.Base2'>,
 <class 'object'>]
Python
```

这里有一个更复杂的多重继承示例及其可视化图型。

![img](E:\git\python3-noteboook\python3教程.assets\470080646_77018.jpg)

```python
class X: pass
class Y: pass
class Z: pass

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z): pass

## Output:
## [<class '__main__.M'>, <class '__main__.B'>,
## <class '__main__.A'>, <class '__main__.X'>,
## <class '__main__.Y'>, <class '__main__.Z'>,
## <class 'object'>]

print(M.mro())
Python
```

参考这一点，进一步讨论MRO并了解实际算法如何计算。



## Python操作符重载

可以根据所使用的操作数更改Python中运算符的含义。这种做法被称为运算符重载。

Python操作系统适用于内置类。 但同一运算符的行为在不同的类型有所不同。 例如，`+`运算符将对两个数字执行算术加法，合并两个列表并连接两个字符串。

Python中的这个功能，允许相同的操作符根据上下文的不同，其含义称为运算符重载。

那么当将它们与用户定义的类的对象一起使用时会发生什么？ 考虑下面的类，它试图模拟二维坐标系中的一个点。

```python
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
Python
```

现在，运行代码，尝试在Python shell中添加两点。

```python
>>> p1 = Point(2,3)
>>> p2 = Point(-1,2)
>>> p1 + p2
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
Python
```

### Python中的特殊功能

以双下划线`__`开头的类函数在Python中称为特殊函数。 这是因为，它们是有特殊含义。 上面定义的`__init__()`函数是其中之一。 每次创建该类的新对象时都会调用它。 Python中有很多特殊功能。

使用特殊功能，可以使类与内置函数兼容。

```python
>>> p1 = Point(2,3)
>>> print(p1)
<__main__.Point object at 0x00000000031F8CC0>
Python
```

但是如果打印不好或不够美观。可以在类中定义`__str__()`方法，可以控制它如何打印。 所以，把它添加到类中，如下代码 - 

```python
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
Python
```

现在再试一次调用`print()`函数。

```shell
>>> p1 = Point(2,3)
>>> print(p1)
(2,3)
Shell
```

当使用内置函数`str()`或`format()`时，调用同样的方法。

```python
>>> str(p1)
'(2,3)'

>>> format(p1)
'(2,3)'
Python
```

所以，当执行`str(p1)`或`format(p1)`，Python在内部执行`p1.__str__()`。

### 在Python中重载+运算符

要重载`+`号，需要在类中实现`__add__()`函数。可以在这个函数里面做任何喜欢的事情。 但是返回`Point`对象的坐标之和是最合理的。

```python
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
Python
```

现在让我们再试一次运行上面的代码 - 

```shell
>>> p1 = Point(2,3)
>>> p2 = Point(-1,2)
>>> print(p1 + p2)
(1,5)
Shell
```

实际发生的是，当执行`p1 + p2`语句时，Python将调用`p1.__add__(p2)`，之后是`Point.__add__(p1，p2)`。 同样，也可以重载其他运算符。需要实现的特殊功能列在下面。

Python中的运算符重载特殊函数 - 

| 运算符      | 表达式     | 内置函数              |
| ----------- | ---------- | --------------------- |
| 加法        | `p1 + p2`  | `p1.__add__(p2)`      |
| 减法        | `p1 - p2`  | `p1.__sub__(p2)`      |
| 乘法        | p1 * p2    | p1.**mul**(p2)        |
| 次幂        | `p1 ** p2` | `p1.__pow__(p2)`      |
| 除法        | `p1 / p2`  | `p1.__truediv__(p2)`  |
| 地板除法    | `p1 // p2` | `p1.__floordiv__(p2)` |
| 模 (modulo) | `p1 % p2`  | `p1.__mod__(p2)`      |
| 按位左移    | `p1 << p2` | `p1.__lshift__(p2)`   |
| 按位右移    | `p1 >> p2` | `p1.__rshift__(p2)`   |
| 按位AND     | `p1 & p`   | `p1.__and__(p2)`      |
| 按位OR      | `p1 or p2` | `p1.__or__(p2)`       |
| 按位XOR     | `p1 ^ p2`  | `p1.__xor__(p2)`      |
| 按位NOT     | `~p1       | p1.**invert**() `     |

### 在Python中重载比较运算符

Python不会限制操作符重载算术运算符。也可以重载比较运算符。

假设想在`Point`类中实现小于符号`<`比较运算。

比较这些来自原点的数值，并为此返回结果。 可以实现如下。

```pythton
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __lt__(self,other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag
Pythton
```

在Python shell中尝试这些示例运行。

```pythton
>>> Point(1,1) < Point(-2,-3)
True

>>> Point(1,1) < Point(0.5,-0.2)
False

>>> Point(1,1) < Point(1,1)
False
Pythton
```

类似地，可以实现的特殊功能，以重载其他比较运算符，如下表所示。

| 运算符     | 表达式     | 内置函数        |
| ---------- | ---------- | --------------- |
| 小于       | `p1 < p2`  | `p1.__lt__(p2)` |
| 小于或等于 | `p1 <= p2` | `p1.__le__(p2)` |
| 等于       | `p1 == p2` | `p1.__eq__(p2)` |
| 不等于     | `p1 != p2` | `p1.__ne__(p2)` |
| 大于       | `p1 > p2`  | `p1.__gt__(p2)` |
| 大于或等于 | `p1 >= p2` | `p1.__ge__(p2)` |





# 高级部分

## Python异常处理

Python提供了两个非常重要的功能来处理Python程序中的异常和错误，并在其中添加调试的函数功能 -

- 异常处理 - 在本教程中介绍。这是一个列表标准Python中提供的异常 - 标准异常。
- 断言 - 在*Python 3*教程中的断言中介绍。

### 标准异常

以下是Python中可用的标准异常列表 -

| 编号 | 异常名称            | 描述                                                         |
| ---- | ------------------- | ------------------------------------------------------------ |
| 1    | Exception           | 所有异常的基类                                               |
| 2    | StopIteration       | 当迭代器的`next()`方法没有指向任何对象时引发。               |
| 3    | SystemExit          | 由`sys.exit()`函数引发。                                     |
| 4    | StandardError       | 除`StopIteration`和`SystemExit`之外的所有内置异常的基类。    |
| 5    | ArithmeticError     | 数据计算出现的所有错误的基类。                               |
| 6    | OverflowError       | 当计算超过数字类型的最大限制时引发。                         |
| 7    | FloatingPointError  | 当浮点计算失败时触发。                                       |
| 8    | ZeroDivisonError    | 对于所有的数字类型，当对零进行除数或模数时产生。             |
| 9    | AssertionError      | 在`Assert`语句失败的情况下引发。                             |
| 10   | AttributeError      | 在属性引用或分配失败的情况下引发。                           |
| 11   | EOFError            | 当没有来自`raw_input()`或`input()`函数的输入并且达到文件结尾时引发。 |
| 12   | ImportError         | 导入语句失败时引发。                                         |
| 13   | KeyboardInterrupt   | 当用户中断程序执行时，通常按`Ctrl + c`。                     |
| 14   | LookupError         | 所有查找错误的基类。                                         |
| 15   | IndexError          | 当序列中没有找到索引时引发。                                 |
| 16   | KeyError            | 当在字典中找不到指定的键时引发。                             |
| 17   | NameError           | 当在本地或全局命名空间中找不到标识符时引发。                 |
| 18   | UnboundLocalError   | 当尝试访问函数或方法中的局部变量但未分配值时引发。           |
| 19   | EnvironmentError    | 在Python环境之外发生的所有异常的基类。                       |
| 20   | IOError             | 在尝试打开不存在的文件时，输入/输出操作失败时触发，例如`print`语句或`open()`函数。 |
| 21   | OSError             | 引起操作系统相关的错误。                                     |
| 22   | SyntaxError         | 当Python语法有错误时引发。                                   |
| 23   | IndentationError    | 当缩进未正确指定时触发。                                     |
| 24   | SystemError         | 当解释器发现内部问题时引发，但遇到此错误时，Python解释器不会退出。 |
| 25   | SystemExit          | 当Python解释器通过使用`sys.exit()`函数退出时引发。 如果没有在代码中处理，导致解释器退出。 |
| 26   | TypeError           | 在尝试对指定数据类型无效的操作或函数时引发。                 |
| 27   | ValueError          | 当数据类型的内置函数具有有效参数类型时引发，但参数具有指定的无效值。 |
| 28   | RuntimeError        | 产生的错误不属于任何类别时引发。                             |
| 29   | NotImplementedError | 当需要在继承类中实现的抽象方法实际上没有实现时引发。         |

### Python中的断言

断言是一个健全检查，可以在完成对程序的测试后打开或关闭。

- 试想断言的最简单的方法就是将它与一个`raise-if`语句(或者更准确的说是一个加注`if`语句)相对应。测试表达式，如果结果为`false`，则会引发异常。
- 断言由版本`1.5`引入的`assert`语句来执行，它是Python的最新关键字。
- 程序员经常在函数开始时放置断言来检查有效的输入，并在函数调用后检查有效的输出。

#### assert语句

当它遇到一个`assert`语句时，Python会评估求值它的的表达式，是否为所希望的那样。 如果表达式为`false`，Python会引发`AssertionError`异常。

`assert`的语法是 -

```python
assert Expression[, Arguments]
Python
```

如果断言失败，Python将使用`ArgumentExpression`作为`AssertionError`的参数。 使用`try-except`语句可以像任何其他异常一样捕获和处理`AssertionError`异常。 如果没有处理，它们将终止程序并产生回溯。
**
示例**

这里将实现一个功能：将给定的温度从开尔文转换为华氏度。如果是负温度，该功能将退出 -

```python
##!/usr/bin/python3
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))
Python
```

当执行上述代码时，会产生以下结果 -

```python
32.0
451
Traceback (most recent call last):
File "test.py", line 9, in <module>
print KelvinToFahrenheit(-5)
File "test.py", line 4, in KelvinToFahrenheit
assert (Temperature >= 0),"Colder than absolute zero!"
AssertionError: Colder than absolute zero!
Python
```

### 什么是异常？

一个例外是在程序执行期间发生的一个事件，它破坏程序指令的正常流程。 一般来说，当Python脚本遇到无法应对的情况时，会引发异常。异常是一个表示错误的Python对象。

当Python脚本引发异常时，它必须立即处理异常，否则终止并退出。

### 处理异常

如果有一些可能引发异常的可疑代码，可以通过将可疑代码放在`try:`块中来保护您的程序。 在`try:`块之后，包括一个`except:`语句，然后是一个尽可能优雅地处理问题的代码块。

**语法**

下面是简单的语法`try .... except ... else`块 -

```python
try:
   You do your operations here
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.
Python
```

以下是上述语法的几个重点 -

- 一个`try`语句可以有多个`except`语句。 当`try`块包含可能引发不同类型的异常的语句时，这就很有用。
- 还可以提供一个通用的`except`子句，它处理任何异常。
- 在`except`子句之后，可以包含一个`else`子句。 如果`try:block`中的代码不引发异常，则`else`块中的代码将执行。
- `else-block`是一个不需要`try:block`保护的代码的地方。

**示例**

此示例打开一个文件，将内容写入文件，并且优雅地出现，因为完全没有问题 -

```python
##!/usr/bin/python3

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()
Python
```

这产生以下结果 -

```python
Written content in the file successfully
Python
```

**示例**

此示例尝试打开一个没有写入权限的文件，因此它引发了一个异常 -

```python
##!/usr/bin/python3

try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
Python
```

这产生以下结果 -

```shell
Error: can't find file or read data
Shell
```

#### except子句没有指定异常

也可以使用`except`语句，但不定义异常，如下所示 -

```shell
try:
   You do your operations here
   ......................
except:
   If there is any exception, then execute this block.
   ......................
else:
   If there is no exception then execute this block.
Shell
```

这种`try-except`语句捕获所有发生的异常。使用这种`try-except`语句不被认为是一个很好的编程实践，因为它捕获所有异常，但不会让程序员能更好地识别发生的问题的根本原因。

#### except子句指定多个异常

还可以使用相同的`except`语句来处理多个异常，如下所示：

```python
try:
   You do your operations here
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   If there is any exception from the given exception list, 
   then execute this block.
   ......................
else:
   If there is no exception then execute this block.
Python
```

#### try-finally子句

可以使用`finally：`块和`try：`块。 `finally：`块是放置必须执行代码的地方，无论`try`块是否引发异常。 `try-finally`语句的语法是这样的 -

```python
try:
   You do your operations here;
   ......................
   Due to any exception, this may be skipped.
finally:
   This would always be executed.
   ......................
Python
```

> 注意 - 可以提供`except`子句或`finally`子句，但不能同时提供。不能使用`else`子句以及`finally`子句。

**示例**

```python
##!/usr/bin/python3

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print ("Error: can\'t find file or read data")
   fh.close()
Python
```

如果没有以写入形式打开文件的权限，则会产生以下结果 -

```python
Error: can't find file or read data
Python
```

同样的例子可以写得更干净如下 -

```python
##!/usr/bin/python3

try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print ("Going to close the file")
      fh.close()
except IOError:
   print ("Error: can\'t find file or read data")
Python
```

当`try`块中抛出异常时，执行将立即传递给`finally`块。 在`finally`块中的所有语句都被执行之后，异常被再次引发，如果存在于`try-except`语句的下一个更高的层中，则在`except`语句中处理异常。

### 异常参数

一个异常可以有一个参数，参数它是一个值，它提供有关该问题的其他信息。 参数的内容因异常而异。 可以通过在`except`子句中提供变量来捕获异常的参数，如下所示：

```python
try:
   You do your operations here
   ......................
except ExceptionType as Argument:
   You can print value of Argument here...
Python
```

如果编写代码来处理单个异常，则可以在`except`语句中使用一个变量后跟异常的名称。 如果要捕获多个异常，可以使用一个变量后跟随异常的元组。

此变量接收大部分包含异常原因的异常值。 变量可以以元组的形式接收单个值或多个值。 该元组通常包含错误字符串，错误编号和错误位置。

**示例**

以下是一个例外 -

```python
##!/usr/bin/python3

## Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)

## Call above function here.
temp_convert("xyz")
Python
```

这产生以下结果 -

```python
The argument does not contain numbers
invalid literal for int() with base 10: 'xyz'
Python
```

### 抛出异常

可以通过使用`raise`语句以多种方式引发异常。`raise`语句的一般语法如下 -

**语法**

```python
raise [Exception [, args [, traceback]]]
Python
```

这里，`Exception`是异常的类型(例如，`NameError`)，`args`是异常参数的值。 参数是可选的; 如果没有提供，则异常参数为`None`。

最后一个参数`traceback`也是可选的(在实践中很少使用)，如果存在，则是用于异常的追溯对象。

**示例**

异常可以是字符串，类或对象。 Python核心引发的大多数异常都是类，一个参数是类的一个实例。 定义新的例外是非常容易的，可以做到如下 -

```python
def functionName( level ):
   if level <1:
      raise Exception(level)
      # The code below to this would not be executed
      # if we raise the exception
   return level
Python
```

> 注意 - 为了捕获异常，“`except`”子句必须引用与类对象或简单字符串相同的异常。例如，为了捕获上述异常，必须写出`except`子句如下：

```python
try:
   Business Logic here...
except Exception as e:
   Exception handling here using e.args...
else:
   Rest of the code here...
Python
```

以下示例说明了使用引发异常 -

```python
##!/usr/bin/python3
def functionName( level ):
   if level <1:
      raise Exception(level)
      # The code below to this would not be executed
      # if we raise the exception
   return level

try:
   l = functionName(-10)
   print ("level = ",l)
except Exception as e:
   print ("error in level argument",e.args[0])
Python
```

这将产生以下结果 - 

```shell
error in level argument -10
Shell
```

### 用户定义的异常

Python还允许通过从标准内置异常导出类来创建自己的异常。

这是一个与`RuntimeError`有关的示例。 在这里，从`RuntimeError`类创建一个子类。 当需要在捕获异常时显示更多具体信息时，这就很有用了。

在`try`块中，用户定义的异常被引发并被捕获在`except`块中。 变量`e`用于创建`Networkerror`类的实例。

```python
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
Python
```

所以当定义了上面的类以后，就可以使用以下命令抛出异常 -

```python
try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args
```



## Python正则表达式

正则表达式是一个特殊的字符序列，可以帮助您使用模式中保留的专门语法来匹配或查找其他字符串或字符串集。 正则表达式在UNIX世界中被广泛使用。

> 注：很多开发人员觉得正则表达式比较难以理解，主要原因是缺少使用或不愿意在这上面花时间。

`re`模块在Python中提供对Perl类正则表达式的完全支持。如果在编译或使用正则表达式时发生错误，则`re`模块会引发异常`re.error`。

在这篇文章中，将介绍两个重要的功能，用来处理正则表达式。 然而，首先是一件小事：有各种各样的字符，这些字符在正则表达式中使用时会有特殊的意义。 为了在处理正则表达式时避免混淆，我们将使用：`r'expression'`原始字符串。

**匹配单个字符的基本模式**

| 编号 | 表达式           | 描述                                               |
| ---- | ---------------- | -------------------------------------------------- |
| 1    | `a, X, 9, <`     | 普通字符完全匹配。                                 |
| 2    | `.`              | 匹配任何单个字符，除了换行符’`\n`‘                 |
| 3    | `\w`             | 匹配“单词”字符：字母或数字或下划线`[a-zA-Z0-9_]`。 |
| 4    | `\W`             | 匹配任何非字词。                                   |
| 5    | `\b`             | 字词与非字词之间的界限                             |
| 6    | `\s`             | 匹配单个空格字符 - 空格，换行符，返回，制表符      |
| 7    | `\S`             | 匹配任何非空格字符。                               |
| 8    | `\t`, `\n`, `\r` | 制表符，换行符，退格符                             |
| 9    | `\d`             | 十进制数`[0-9]`                                    |
| 10   | `^`              | 匹配字符串的开头                                   |
| 11   | `$`              | 匹配字符串的末尾                                   |
| 12   | `\`              | 抑制字符的“特殊性”，也叫转义字符。                 |

**编译标志**

编译标志可以修改正则表达式的某些方面。标志在`re`模块中有两个名称：一个很长的名称，如`IGNORECASE`，和一个简短的单字母形式，如`I`。

| 编号 | 标志                        | 含义                                                         |
| ---- | --------------------------- | ------------------------------------------------------------ |
| 1    | ASCII, A                    | 像`\w`，`\b`，`\s`和`\d`之间的几个转义只匹配ASCII字符与相应的属性。 |
| 2    | DOTALL, S                   | 匹配任何字符，包括换行符                                     |
| 3    | IGNORECASE, I               | 不区分大小写匹配                                             |
| 4    | LOCALE, L                   | 做一个区域感知的匹配                                         |
| 5    | MULTILINE, M                | 多行匹配，影响`^`和`$`                                       |
| 6    | VERBOSE, X (for ‘extended’) | 启用详细的`RE`，可以更干净，更容易理解                       |

### 1.match函数

此函数尝试将`RE`模式与可选标志的字符串进行匹配。

下面是函数的语法 -

```python
re.match(pattern, string, flags = 0)
Python
```

这里是参数的描述 -

- `pattern` - 这是要匹配的正则表达式。  
- `string` - 这是字符串，它将被搜索用于匹配字符串开头的模式。 |
- `flags` - 可以使用按位OR(`|`)指定不同的标志。 这些是修饰符，如下表所列。

`re.match`函数在成功时返回匹配对象，失败时返回`None`。使用`match(num)`或`groups()`函数匹配对象来获取匹配的表达式。

| 编号 | 匹配对象         | 描述                                                         |
| ---- | ---------------- | ------------------------------------------------------------ |
| 1    | `group(num = 0)` | 此方法返回整个匹配(或特定子组`num`)                          |
| 2    | `groups()`       | 此方法返回一个元组中的所有匹配子组(如果没有，则返回为`None`) |

**示例**

```python
##!/usr/bin/python3
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
Python
```

当执行上述代码时，会产生以下结果 -

```shell
matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
Shell
```

### 2.search函数

此函数尝试将`RE`模式与可选标志的字符串进行匹配。

下面是这个函数的语法 -

```python
re.match(pattern, string, flags = 0)
Python
```

这里是参数的描述 -

- `pattern` - 这是要匹配的正则表达式。  
- `string` - 这是字符串，它将被搜索用于匹配字符串开头的模式。 |
- `flags` - 可以使用按位OR(`|`)指定不同的标志。 这些是修饰符，如下表所列。

`re.search`函数在成功时返回匹配对象，否则返回`None`。使用`match`对象的`group(num)`或`groups()`函数来获取匹配的表达式。

| 编号 | 匹配对象         | 描述                                                         |
| ---- | ---------------- | ------------------------------------------------------------ |
| 1    | `group(num = 0)` | 此方法返回整个匹配(或特定子组`num`)                          |
| 2    | `groups()`       | 此方法返回一个元组中的所有匹配子组(如果没有，则返回为`None`) |

**示例**

```python
##!/usr/bin/python3
import re

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")
Python
```

当执行上述代码时，会产生以下结果 -

```python
matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
Python
```

### 3.匹配与搜索

Python提供基于正则表达式的两种不同的原始操作：`match`检查仅匹配字符串的开头，而`search`检查字符串中任何位置的匹配(这是Perl默认情况下的匹配)。

**示例**

```python
##!/usr/bin/python3
import re

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!")
Python
```

当执行上述代码时，会产生以下结果 -

```shell
No match!!
search --> matchObj.group() :  dogs
Shell
```

### 4.搜索和替换

使用正则表达式`re`模块中的最重要的之一是`sub`。

**模块**

```python
re.sub(pattern, repl, string, max=0)
Python
```

此方法使用`repl`替换所有出现在`RE`模式的字符串，替换所有出现，除非提供`max`。此方法返回修改的字符串。

**示例**

```python
##!/usr/bin/python3
import re

phone = "2018-959-559 # This is Phone Number"

## Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

## Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Phone Num :  2018-959-559
Phone Num :  2018959559
Shell
```

### 5.正则表达式修饰符：选项标志

正则表达式文字可能包含一个可选修饰符，用于控制匹配的各个方面。 修饰符被指定为可选标志。可以使用异或(`|`)提供多个修饰符，如前所示，可以由以下之一表示 -

| 编号 | 修辞符 | 描述                                                         |
| ---- | ------ | ------------------------------------------------------------ |
| 1    | `re.I` | 执行不区分大小写的匹配。                                     |
| 2    | `re.L` | 根据当前语言环境解释单词。这种解释影响字母组(`\w`和`\W`)以及字边界行为(`\b`和`\B`)。 |
| 3    | `re.M` | 使`$`匹配一行的结尾(而不仅仅是字符串的结尾)，并使`^`匹配任何行的开始(而不仅仅是字符串的开头)。 |
| 4    | `re.S` | 使一个句点(`.`)匹配任何字符，包括换行符。                    |
| 5    | `re.U` | 根据Unicode字符集解释字母。 此标志影响`\w`，`\W`，`\b`，`\B`的行为。 |
| 6    | `re.X` | 允许“cuter”正则表达式语法。 它忽略空格(除了一个集合`[]`内部，或者用反斜杠转义)，并将未转义的`#`作为注释标记。 |

### 6.正则表达模式

除了控制字符`(+ ? . * ^ $ ( ) [ ] { } | \)`，所有字符都与其自身匹配。 可以通过使用反斜杠将其转换为控制字符。

### 7.正则表达式示例

**字符常量**

| 编号 | 示例   | 说明           |
| ---- | ------ | -------------- |
| 1    | python | 匹配“python”。 |

**字符类**

| 编号 | 示例          | 说明                         |
| ---- | ------------- | ---------------------------- |
| 1    | `[Pp]ython`   | 匹配“Python”或“python”       |
| 2    | `rub[ye]`     | 匹配“ruby”或“rube”           |
| 3    | `[aeiou]`     | 匹配任何一个小写元音         |
| 4    | `[0-9]`       | 匹配任何数字; 如[0123456789] |
| 5    | `[a-z]`       | 匹配任何小写ASCII字母        |
| 6    | `[A-Z]`       | 匹配任何大写的ASCII字母      |
| 7    | `[a-zA-Z0-9]` | 匹配上述任何一个             |
| 8    | `[^aeiou]`    | 匹配除小写元音之外的任何东西 |
| 9    | `[^0-9]`      | 匹配数字以外的任何东西       |

**特殊字符类**

| 编号 | 示例 | 说明                            |
| ---- | ---- | ------------------------------- |
| 1    | `.`  | 匹配除换行符以外的任何字符      |
| 2    | `\d` | 匹配数字：`[0-9]`               |
| 3    | `\D` | 匹配非数字：`[^0-9]`            |
| 4    | `\s` | 匹配空格字符：`[\t\r\n\f]`      |
| 5    | `\S` | 匹配非空格：`[^\t\r\n\f]`       |
| 6    | `\w` | 匹配单字字符： `[A-Za-z0-9_]`   |
| 7    | `\W` | 匹配非单字字符： `[A-Za-z0-9_]` |

**重复匹配**

| 编号 | 示例      | 说明                           |
| ---- | --------- | ------------------------------ |
| 1    | `ruby?`   | 匹配“rub”或“ruby”：`y`是可选的 |
| 2    | `ruby*`   | 匹配“rub”加上`0`个以上的`y`    |
| 3    | `ruby+`   | 匹配“rub”加上`1`个或更多的`y`  |
| 4    | `\d{3}`   | 完全匹配`3`位数                |
| 5    | `\d{3,}`  | 匹配`3`位或更多位数字          |
| 6    | `\d{3,5}` | 匹配3，4或5位数                |

**非贪婪重复**

这匹配最小的重复次数 -

| 编号 | 示例    | 说明                                              |
| ---- | ------- | ------------------------------------------------- |
| 1    | `<.*>`  | 贪婪重复：匹配“`<python> perl>`”                  |
| 2    | `<.*?>` | 非贪婪重复：在“`<python> perl`”中匹配“`<python>`” |

**用圆括号分组**

| 编号 | 示例               | 说明                                     |
| ---- | ------------------ | ---------------------------------------- |
| 1    | `\D\d+`            | 没有分组：`+`重复`\d`                    |
| 2    | `(\D\d)+`          | 分组：`+`重复`\D\d`对                    |
| 3    | `([Pp]ython(,)?)+` | 匹配“Python”，“Python，python，python”等 |

**反向引用**

这与以前匹配的组再次匹配 -

| 编号 | 示例                 | 说明                                                         |
| ---- | -------------------- | ------------------------------------------------------------ |
| 1    | `([Pp])ython&\1ails` | 匹配python和pails或Python和Pails                             |
| 2    | `(['"])[^\1]*\1`     | 单引号或双引号字符串。`\1`匹配第一个分组匹配。 `\2`匹配任何第二个分组匹配等 |

**备择方案**

- `python|perl` - 匹配“python”或“perl”
- `rub(y|le)` - 匹配 “ruby” 或 “ruble”
- `Python(!+|\?)` - “Python”后跟一个或多个！ 还是一个？

**锚点**

这需要指定匹配位置。

| 编号 | 示例          | 说明                                                         |
| ---- | ------------- | ------------------------------------------------------------ |
| 1    | `^Python`     | 在字符串或内部行的开头匹配“Python”                           |
| 2    | `Python$`     | 在字符串或内部行的结尾匹配“Python”                           |
| 3    | `\APython`    | 在字符串的开头匹配“Python”                                   |
| 4    | `Python\Z`    | 在字符串的末尾匹配“Python”                                   |
| 5    | `\bPython\b`  | 在字词的边界匹配“Python”                                     |
| 6    | `\brub\B`     | `\B`是非字词边界：在“rube”和“ruby”中匹配“rub”，而不是单独匹配 |
| 7    | `Python(?=!)` | 匹配“Python”，如果跟着感叹号。                               |
| 8    | `Python(?!!)` | 匹配“Python”，如果没有感叹号后面。                           |

**带括号的特殊语法**

| 编号 | 示例           | 说明                    |                            |
| ---- | -------------- | ----------------------- | -------------------------- |
| 1    | `R(?#comment)` | 匹配“R”。其余的都是注释 |                            |
| 2    | `R(?i)uby`     | 匹配“uby”时不区分大小写 |                            |
| 3    | `R(?i:uby)`    | 同上                    |                            |
| 4    | `rub(?:y       | le))`                   | 仅组合而不创建`\1`反向引用 |


## Python+MySQL数据库操作（PyMySQL）

Python的数据库接口标准是Python DB-API。大多数Python数据库接口遵循这个标准。
可以为应用程序选择正确的数据库。Python数据库API支持广泛的数据库服务器，如 -

- GadFly
- mSQL
- [MySQL](http://www.yiibai.com/mysql)
- [PostgreSQL](http://www.yiibai.com/postgresql)
- Microsoft SQL Server 2000
- Informix
- Interbase
- [Oracle](http://www.yiibai.com/oracle)
- Sybase
- [SQLite](http://www.yiibai.com/sqlite)

以下是可用的Python数据库接口 - [Python数据库接口和API](http://wiki.python.org/moin/DatabaseInterfaces)的列表。需要为要访问的每种数据库下载一个单独的DB API模块。 例如，如果需要访问Oracle数据库和MySQL数据库，则必须同时下载Oracle和MySQL数据库模块。

DB API为尽可能使用Python结构和语法处理数据库提供了最低标准。API包括以下内容：

- 导入API模块。
- 获取与数据库的连接。
- 发出SQL语句和存储过程。
- 关闭连接

Python具有内置的SQLite支持。 在本节中，我们将学习使用MySQL的相关概念和知识。 在早期Python版本一般都使用MySQLdb模块，但这个MySQL的流行接口与*Python 3*不兼容。因此，在教程中将使用[PyMySQL模块](http://github.com/PyMySQL/PyMySQL/)。

### 1.什么是PyMySQL？

PyMySQL是从Python连接到MySQL数据库服务器的接口。 它实现了Python数据库API v2.0，并包含一个纯Python的MySQL客户端库。 PyMySQL的目标是成为MySQLdb的替代品。

PyMySQL参考文档：http://pymysql.readthedocs.io/

### 2.如何安装PyMySQL？

在使用PyMySQL之前，请确保您的机器上安装了PyMySQL。只需在Python脚本中输入以下内容即可执行它 -

```python
##!/usr/bin/python3

import PyMySQL
Python
```

在 Windows 系统上，打开命令提示符 - 

```shell
C:\Users\Administrator>python
Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import PyMySQL
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'PyMySQL'
>>>
Shell
```

如果产生如上结果，则表示`PyMySQL`模块尚未安装。

最后一个稳定版本可以在PyPI上使用，可以通过`pip`命令来安装-

```shell
:\Users\Administrator> pip install PyMySQL
Collecting PyMySQL
  Downloading PyMySQL-0.7.11-py2.py3-none-any.whl (78kB)
    51% |████████████████▋               | 
    40kB 109kB/s eta 0:0    64% |████████████████████▊       
    | 51kB 112kB/s eta    77% |█████████████████████████      | 61kB 135kB/s    90% |█████████████████████████████
    | 71kB 152    100% |████████████████████████████████| 81kB 163kB/s

Installing collected packages: PyMySQL
Successfully installed PyMySQL-0.7.11

C:\Users\Administrator>
Shell
```

或者(例如，如果pip不可用)，可以从GitHub下载tarball，并按照以下方式安装：

```shell
$ # X.X is the desired PyMySQL version (e.g. 0.5 or 0.6).
$ curl -L http://github.com/PyMySQL/PyMySQL/tarball/pymysql-X.X | tar xz
$ cd PyMySQL*
$ python setup.py install
$ # The folder PyMySQL* can be safely removed now.
Shell
```

> 注意 - 确保具有root权限来安装上述模块。

### 3.数据库连接

在连接到MySQL数据库之前，请确保以下几点：

- 已经创建了一个数据库：`test`。
- 已经在`test`中创建了一个表:`employee`。
- `employee`表格包含:`fist_name`，`last_name`，`age`，`sex`和`income`字段。
- MySQL用户“root”和密码“123456”可以访问：`test`。
- Python模块PyMySQL已正确安装在您的计算机上。
- 已经通过[MySQL教程](http://www.yiibai.com/mysql)了解MySQL基础知识。

创建表`employee`的语句为：

```sql
CREATE TABLE `employee` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` char(20) NOT NULL,
  `last_name` char(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `income` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
SQL
```

**实例**

以下是Python通过PyMySQL模块接口连接MySQL数据库“`test`”的示例 -

> 注意：在 Windows 系统上，`import PyMySQL` 和 `import pymysql` 有区别。

```python
##!/usr/bin/python3
##coding=utf-8

import pymysql

## Open database connection
db = pymysql.connect("localhost","root","123456","test" )

## prepare a cursor object using cursor() method
cursor = db.cursor()

## execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

## Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

## disconnect from server
db.close()
Python
```

运行此脚本时，会产生以下结果 - 

```shell
Database version : 5.7.14-log
Shell
```

如果使用数据源建立连接，则会返回连接对象并将其保存到`db`中以供进一步使用，否则将`db`设置为`None`。 接下来，`db`对象用于创建一个游标对象，用于执行SQL查询。 最后，在结果打印出来之前，它确保数据库连接关闭并释放资源。

### 4.创建数据库表

建立数据库连接后，可以使用创建的游标的`execute`方法将数据库表或记录创建到数据库表中。

**示例**

下面演示如何在数据库：`test`中创建一张数据库表：`employee` -

```python
##!/usr/bin/python3
##coding=utf-8

import pymysql

## Open database connection
db = pymysql.connect("localhost","root","123456","test" )

## prepare a cursor object using cursor() method
cursor = db.cursor()

## Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS employee")

## Create table as per requirement
sql = """CREATE TABLE `employee` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` char(20) NOT NULL,
  `last_name` char(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `income` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

cursor.execute(sql)
print("Created table Successfull.")
## disconnect from server
db.close()
Python
```

运行此脚本时，会产生以下结果 - 

```shell
Created table Successfull.
Shell
```

### 5.插入操作

当要将记录创建到数据库表中时，需要执行`INSERT`操作。

**示例**

以下示例执行SQL的`INSERT`语句以在`EMPLOYEE`表中创建一条(多条)记录 -

```python
##!/usr/bin/python3
##coding=utf-8

import pymysql

## Open database connection
db = pymysql.connect("localhost","root","123456","test" )

## prepare a cursor object using cursor() method
cursor = db.cursor()

## Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Su', 20, 'M', 5000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

### 再次插入一条记录
## Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Kobe', 'Bryant', 40, 'M', 8000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
print (sql)
print('Yes, Insert Successfull.')
## disconnect from server
db.close()
Python
```

运行此脚本时，会产生以下结果 - 

```shell
Yes, Insert Successfull.
Shell
```

上述插入示例可以写成如下动态创建SQL查询 -

```python
##!/usr/bin/python3
##coding=utf-8

import pymysql

## Open database connection
db = pymysql.connect("localhost","root","123456","test" )

## prepare a cursor object using cursor() method
cursor = db.cursor()

## Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
   LAST_NAME, AGE, SEX, INCOME) \
   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
   ('Max', 'Su', 25, 'F', 2800)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

## disconnect from server
db.close()
Python
```

**示例**

以下代码段是另一种执行方式，可以直接传递参数 -

```python
..................................
user_id = "test123"
password = "password"

con.execute('insert into Login values("%s", "%s")' % \
             (user_id, password))
..................................
Python
```

### 6.读取操作

任何数据库上的读操作表示要从数据库中读取获取一些有用的信息。

在建立数据库连接后，就可以对此数据库进行查询了。 可以使用`fetchone()`方法获取单条记录或`fetchall()`方法从数据库表中获取多个值。

- `fetchone()` - 它获取查询结果集的下一行。 结果集是当使用游标对象来查询表时返回的对象。
- `fetchall()` - 它获取结果集中的所有行。 如果已经从结果集中提取了一些行，则从结果集中检索剩余的行。
- `rowcount` - 这是一个只读属性，并返回受`execute()`方法影响的行数。

**示例**

以下过程查询`EMPLOYEE`表中所有记录的工资超过`1000`员工记录信息 -

```python
##!/usr/bin/python3
##coding=utf-8

import pymysql

## Open database connection
db = pymysql.connect("localhost","root","123456","test" )

## prepare a cursor object using cursor() method
cursor = db.cursor()
## 按字典返回 
## cursor = db.cursor(pymysql.cursors.DictCursor)

## Prepare SQL query to select a record from the table.
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %d" % (1000)
##print (sql)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      #print (row)
      fname = row[1]
      lname = row[2]
      age = row[3]
      sex = row[4]
      income = row[5]
      # Now print fetched result
      print ("name = %s %s,age = %s,sex = %s,income = %s" % \
             (fname, lname, age, sex, income ))
except:
   import traceback
   traceback.print_exc()

   print ("Error: unable to fetch data")

## disconnect from server
db.close()
Python
name = Mac Su,age = 20,sex = M,income = 5000.0
name = Kobe Bryant,age = 40,sex = M,income = 8000.0
Shell
```

### 7.更新操作

UPDATE语句可对任何数据库中的数据进行更新操作，它可用于更新数据库中已有的一个或多个记录。

以下程序将所有`SEX`字段的值为“`M`”的记录的年龄(`age`字段)更新为增加一年。

```python
##!/usr/bin/python3
##coding=utf-8

import pymysql

## Open database connection
db = pymysql.connect("localhost","root","123456","test" )

## prepare a cursor object using cursor() method
##cursor = db.cursor()
cursor = db.cursor(pymysql.cursors.DictCursor)
## prepare a cursor object using cursor() method
cursor = db.cursor()

## Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
                          WHERE SEX = '%c'" % ('M')
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

## disconnect from server
db.close()
Python
```

### 8.删除操作

当要从数据库中删除一些记录时，那么可以执行`DELETE`操作。 以下是删除`EMPLOYEE`中`AGE`超过`40`的所有记录的程序 -

```python
##!/usr/bin/python3
##coding=utf-8

import pymysql

## Open database connection
db = pymysql.connect("localhost","root","123456","test" )

## prepare a cursor object using cursor() method
cursor = db.cursor()

## Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (40)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

## disconnect from server
db.close()
Python
```

### 9.执行事务

事务是确保数据一致性的一种机制。事务具有以下四个属性 -

- **原子性** - 事务要么完成，要么完全没有发生。
- **一致性** - 事务必须以一致的状态开始，并使系统保持一致状态。
- **隔离性** - 事务的中间结果在当前事务外部不可见。
- **持久性** - 当提交了一个事务，即使系统出现故障，效果也是持久的。

Python DB API 2.0提供了两种提交或回滚事务的方法。

**示例**

已经知道如何执行事务。 这是一个类似的例子 -

```python
## Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
Python
```

#### 9.1.COMMIT操作

提交是一种操作，它向数据库发出信号以完成更改，并且在此操作之后，不会更改任何更改。

下面是一个简单的例子演示如何调用`commit()`方法。

```python
db.commit()
Python
```

#### 9.2.回滚操作

如果您对一个或多个更改不满意，并且要完全还原这些更改，请使用`rollback()`方法。

下面是一个简单的例子演示如何调用`rollback()`方法。

```python
db.rollback()
Python
```

### 10.断开数据库连接

要断开数据库连接，请使用`close()`方法。

```python
db.close()
Python
```

如果用户使用`close()`方法关闭与数据库的连接，则任何未完成的事务都将被数据库回滚。 但是，您的应用程序不会依赖于数据级别的实现细节，而是明确地调用提交或回滚。

### 11.处理错误

错误有很多来源。一些示例是执行的SQL语句中的语法错误，连接失败或为已取消或已完成语句句柄调用`fetch`方法等等。

DB API定义了每个数据库模块中必须存在的许多错误。下表列出了这些异常和错误 - 

| 编号 | 异常                | 描述                                                         |
| ---- | ------------------- | ------------------------------------------------------------ |
| 1    | *Warning*           | 用于非致命问题，是*StandardError*的子类。                    |
| 2    | *Error*             | 错误的基类，是*StandardError*的子类。                        |
| 3    | *InterfaceError*    | 用于数据库模块中的错误，但不是数据库本身，是*Error*的子类。  |
| 4    | *DatabaseError*     | 用于数据库中的错误，是*Error*的子类。                        |
| 5    | *DataError*         | *DatabaseError*的子类引用数据中的错误。                      |
| 6    | *OperationalError*  | *DatabaseError*的子类，涉及如丢失与数据库的连接等错误。 这些错误通常不在Python脚本程序的控制之内。 |
| 7    | *IntegrityError*    | *DatabaseError* 子类错误，可能会损害关系完整性，例如唯一性约束和外键。 |
| 8    | *InternalError*     | *DatabaseError*的子类，指的是数据库模块内部的错误，例如游标不再活动。 |
| 9    | *ProgrammingError*  | *DatabaseError*的子类，它引用错误，如错误的表名和其他安全。  |
| 10   | *NotSupportedError* | *DatabaseError*的子类，用于尝试调用不支持的功能。            |

Python脚本应该处理这些错误，但在使用任何上述异常之前，请确保您的PyMySQL支持该异常。 可以通过阅读DB API 2.0规范获得更多关于它们的信息。


## Python网络编程（Sockets）

Python提供了两个级别的访问网络服务。 在低级别，可以访问底层操作系统中的基本套接字支持，这允许您实现面向连接和无连接协议的客户端和服务器。

Python还具有提供对特定应用级网络协议(如FTP，HTTP等)的更高级别访问的库。

本章将了解和学习网络中最着名的概念 - 套接字编程。

### 1.什么是套接字？

套接字(Sockets)是双向通信信道的端点。 套接字可以在一个进程内，在同一机器上的进程之间，或者在不同主机的进程之间进行通信，主机可以是任何一台有连接互联网的机器。

套接字可以通过多种不同的通道类型实现：Unix域套接字，TCP，UDP等。 套接字库提供了处理公共传输的特定类，以及一个用于处理其余部分的通用接口。

套接字有自己的术语 -

- *domain* - 用作传输机制的协议族。这些值是常量，例如：`AF_INET`，`PF_INET`，`PF_UNIX`，`PF_X25`等。

- *type* - 两个端点之间的通信类型，通常用于面向连接的协议的`SOCK_STREAM`和用于无连接协议的`SOCK_DGRAM`。

- *protocol* - 通常为`0`，这可以用于标识域和类型中的协议的变体。

- hostname

   \- 网络接口的标识符 -

  - 一个字符串，可以是一个主机名，一个有四个点符号的IP地址，或一个冒号中的IPV6地址(可能是点)符号。
  - 一个字符串“`<broadcast>`”，它指定一个`INADDR_BROADCAST`地址。
  - 零长度字符串，指定`INADDR_ANY`，或
  - 整数，以主机字节顺序解释为二进制地址。

- *port* - 每个服务器监听一个或多个端口的客户端的调用。端口可能是`Fixnum`端口号，包含端口号的字符串或服务名称。

### 2. socket模块

要创建套接字，必须使用套接字模块中的`socket.socket()`函数，该函数具有一般语法 -

```python
s = socket.socket (socket_family, socket_type, protocol = 0)
Python
```

这里是上述参数的描述 -

- *socket_family* - 它的值可以是：`AF_UNIX`或`AF_INET`，如前所述。
- *socket_type* - 它的值可以是：`SOCK_STREAM`或`SOCK_DGRAM`。
- *protocol* - 这通常被省略，默认为`0`。

当创建了套接字对象这后，就可以使用所需的函数来创建客户端或服务器程序。 以下是所需函数的列表：

**服务器套接字方法**

| 编号 | 方法         | 描述                                                |
| ---- | ------------ | --------------------------------------------------- |
| 1    | `s.bind()`   | 此方法将地址(主机名，端口号对)绑定到套接字。        |
| 2    | `s.listen()` | 此方法设置并启动TCP侦听器。                         |
| 3    | `s.accept()` | 这被动地接受TCP客户端连接，等待直到连接到达(阻塞)。 |

**客户端套接字方法**

| 编号 | 方法          | 描述                          |
| ---- | ------------- | ----------------------------- |
| 1    | `s.connect()` | 此方法主动启动TCP服务器连接。 |

**通用套接字方法**

| 编号 | 方法                   | 描述                |
| ---- | ---------------------- | ------------------- |
| 1    | `s.recv()`             | 此方法接收TCP消息。 |
| 2    | `s.send()`             | 该方法发送TCP消息   |
| 3    | `s.recvfrom()`         | 此方法接收UDP消息   |
| 4    | `s.sendto()`           | 此方法发送UDP消息   |
| 5    | `s.close()`            | 此方法关闭套接字    |
| 6    | `socket.gethostname()` | 返回主机名          |

### 3.一个简单的服务器

要编写互联网服务器，可使用`socket`模块中可用的`socket()`来创建套接字对象。 然后使用套接字对象调用其他函数来设置套接字服务器。

现在调用`bind(hostname，port)`函数来指定主机上服务的端口。

接下来，调用返回对象的`accept()`方法。 此方法在您指定的端口等待客户端连接，连接成功后返回一个连接(`connection`)对象，该对象表示与该客户端的连接。

```python
##!/usr/bin/python3           # This is server.py file
import socket

## create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

## get local machine name
host = socket.gethostname()                           

port = 8088

## bind to the port
serversocket.bind((host, port))                                  
print("Server start at port: 8088")
## queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))

    msg='Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
Python
```

### 4.一个简单的客户端

下面接着编写一个非常简单的客户端程序，打开与给定端口`8088`与上面的服务器程序主机的连接。 使用Python的`socket`模块功能创建套接字客户端非常简单。

`socket.connect(hosname，port)`函数打开`hostname`上的`port`的TCP连接。当打开了一个套接字，就可以像任何IO对象一样读取它。 完成后，请记住关闭它，就像关闭文件一样。

**示例**

以下代码是连接到给定主机和端口的非常简单的客户端，从套接字读取任何可用数据，然后退出 -

```python
##!/usr/bin/python3           # This is client.py file

import socket

## create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

## get local machine name
host = socket.gethostname()

port = 8088

## connection to hostname on the port.
s.connect((host, port))

## Receive no more than 1024 bytes
msg = s.recv(1024)

s.close()

print (msg.decode('ascii'))
Python
```

现在在后台运行先运行：`server.py`，然后运行上面的`client.py`来查看结果，如果程序没有错误，那么应该得到类似以下以结果  -

![img](E:\git\python3-noteboook\python3教程.assets\928080651_52327.png)

### 5. Python互联网模块

Python网络/互联网编程中的一些重要模块的列表如下：

| 协议   | 通用功能     | 端口号 | 对应Python模块             |
| ------ | ------------ | ------ | -------------------------- |
| HTTP   | 网页服务     | 80     | httplib, urllib, xmlrpclib |
| NNTP   | Usenet新闻   | 119    | nntplib                    |
| FTP    | 文件传输     | 20     | ftplib, urllib             |
| SMTP   | 发送邮件     | 25     | smtplib                    |
| POP3   | 获取电子邮件 | 110    | poplib                     |
| IMAP4  | 获取电子邮件 | 143    | imaplib                    |
| Telnet | 命令行       | 23     | telnetlib                  |
| Gopher | 文档传输     | 70     | gopherlib, urllib          |

请检查上述所有库，以使用FTP，SMTP，POP和IMAP协议。

**进一步阅读**

这是Socket编程的一个快速开始。 这是一个广阔的话题。 建议通过以下链接查找更多详细信息 -

- [Unix套接字编程](http://www.yiibai.com/unix_sockets/index.html)。
- [Python套接字库和模块](http://docs.python.org/3.0/library/socket.html)。



## Python发送邮件

简单邮件传输协议(SMTP)是一种协议，用于在邮件服务器之间发送电子邮件和路由电子邮件。

Python提供`smtplib`模块，该模块定义了一个SMTP客户端会话对象，可用于使用SMTP或ESMTP侦听器守护程序向任何互联网机器发送邮件。

这是一个简单的语法，用来创建一个SMTP对象，稍后将演示如何用它来发送电子邮件 -

```python
import smtplib

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
Python
```

这里是上面语法的参数细节 -

- *host* - 这是运行SMTP服务器的主机。可以指定主机的IP地址或类似`yiibai.com`的域名。这是一个可选参数。
- *port* - 如果提供主机参数，则需要指定SMTP服务器正在侦听的端口。通常这个端口默认值是：`25`。
- *local_hostname* - 如果SMTP服务器在本地计算机上运行，那么可以只指定`localhost`选项。

SMTP对象有一个`sendmail`的实例方法，该方法通常用于执行邮件发送的工作。它需要三个参数 -

- *sender* - 具有发件人地址的字符串。
- *receivers* - 字符串列表，每个收件人一个。
- *message* - 作为格式如在各种RFC中指定的字符串。

### 1.使用Python发送纯文本电子邮件

**示例**

以下是使用Python脚本发送一封电子邮件的简单方法 -

```python
##!/usr/bin/python3

import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
Python
```

在这里，已经发送了一封基本的电子邮件，使用三重引号，请注意正确格式化标题。一封电子邮件需要一个`From`，`To`和一个`Subject`标题，与电子邮件的正文与空白行分开。

要发送邮件，使用`smtpObj`连接到本地机器上的SMTP服务器。 然后使用`sendmail`方法以及消息，从地址和目标地址作为参数(即使来自和地址在电子邮件本身内，这些并不总是用于路由邮件)。

如果没有在本地计算机上运行SMTP服务器，则可以使用`smtplib`客户端与远程SMTP服务器进行通信。除非您使用网络邮件服务(如gmail或Yahoo! Mail)，否则您的电子邮件提供商必须向您提供可以提供的邮件服务器详细信息。以腾讯QQ邮箱为例，具体如下：

```python
mail = smtplib.SMTP('smtp.qq.com', 587) # 端口465或587
Python
```

### 2.使用Python发送HTML电子邮件

当使用Python发送邮件信息时，所有内容都被视为简单文本。 即使在短信中包含HTML标签，它也将显示为简单的文本，HTML标签将不会根据HTML语法进行格式化。 但是，Python提供了将HTML消息作为HTML消息发送的选项。

发送电子邮件时，可以指定一个Mime版本，内容类型和发送HTML电子邮件的字符集。
以下是将HTML内容作为电子邮件发送的示例 - 

```python
##!/usr/bin/python3

import smtplib

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
Python
```

### 3.发送附件作为电子邮件

要发送具有混合内容的电子邮件，需要将Content-type标题设置为multipart / mixed。 然后，可以在边界内指定文本和附件部分。

一个边界以两个连字符开始，后跟一个唯一的编号，不能出现在电子邮件的消息部分。 表示电子邮件最终部分的最后一个边界也必须以两个连字符结尾。

所附的文件应该用包(“m”)功能编码，以便在传输之前具有基本的64编码。

### 4.发送示例

首先我们要知道用python代理登录qq邮箱发邮件，是需要更改自己qq邮箱设置的。在这里大家需要做两件事情：邮箱开启SMTP功能 、获得授权码。之后我们来看看如何更改模板代码，实现使用Python登录QQ邮箱发送QQ邮件。

> 注意：也可以使用其他服务商的 SMTP 访问(QQ、网易、Gmail等)。

使用QQ邮件发送邮件之前如何设置授权码，参考：

http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256

**4.1.发送一纯文本邮件到指定邮件**

```python
##! /usr/bin/env python
##coding=utf-8

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


##qq邮箱smtp服务器
host_server = 'smtp.qq.com'
##sender_qq为发件人的qq号码
sender_qq = '769728683@qq.com'
##pwd为qq邮箱的授权码
pwd = '****kenbb***' ## xh**********bdc
##发件人的邮箱
sender_qq_mail = '769728683@qq.com'
##收件人邮箱
receiver = 'yiibai.com@gmail.com'

##邮件的正文内容
mail_content = '你好，这是使用python登录qq邮箱发邮件的测试'
##邮件标题
mail_title = 'Maxsu的邮件'

##ssl登录
smtp = SMTP_SSL(host_server)
##set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = receiver
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
Python
```

执行上面代码后，登录接收邮件的邮件帐号，这里接收邮件的账号为：`yiibai.com@gmail.com`，登录 http://gmail.com 应该会看到有接收到邮件如下 - 

![img](E:\git\python3-noteboook\python3教程.assets\767100600_71168.png)

> 注意：有时可能被认为是垃圾邮件，如果没有找到可从“垃圾邮件”查找一下。

**4.2.给多个人发送邮件**

```python
##! /usr/bin/env python
##coding=utf-8

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


##qq邮箱smtp服务器
host_server = 'smtp.qq.com'
##sender_qq为发件人的qq号码
sender_qq = '769728683@qq.com'
##pwd为qq邮箱的授权码
pwd = 'h**********bdc' ## h**********bdc
##发件人的邮箱
sender_qq_mail = '769728683@qq.com'
##收件人邮箱
receivers = ['yiibai.com@gmail.com','****su@gmail.com']

##邮件的正文内容
mail_content = '你好，这是使用python登录qq邮箱发邮件的测试'
##邮件标题
mail_title = 'Maxsu的邮件'


##ssl登录
smtp = SMTP_SSL(host_server)
##set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = Header("接收者测试", 'utf-8') ## 接收者的别名
smtp.sendmail(sender_qq_mail, receivers, msg.as_string())
smtp.quit()
Python
```

执行上面代码后，登录接收邮件的邮件帐号，这里接收邮件的账号为：`yiibai.com@gmail.com`，登录 http://gmail.com 应该会看到有接收到邮件如下 - 

![img](E:\git\python3-noteboook\python3教程.assets\378110652_20832.png)

**4.3.使用Python发送HTML格式的邮件**

Python发送HTML格式的邮件与发送纯文本消息的邮件不同之处就是将MIMEText中`_subtype`设置为`html`。代码如下：

```python
##! /usr/bin/env python
##coding=utf-8

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


##qq邮箱smtp服务器
host_server = 'smtp.qq.com'
##sender_qq为发件人的qq号码
sender_qq = '769728683@qq.com'
##pwd为qq邮箱的授权码
pwd = '***bmke********' ##
##发件人的邮箱
sender_qq_mail = '769728683@qq.com'
##收件人邮箱
receiver = 'yiibai.com@gmail.com'

##邮件的正文内容
mail_content = "你好，<p>这是使用python登录qq邮箱发送HTML格式邮件的测试：</p><p><a href='http://www.yiibai.com'>易百教程</a></p>"
##邮件标题
mail_title = 'Maxsu的邮件'


##ssl登录
smtp = SMTP_SSL(host_server)
##set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEText(mail_content, "html", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = Header("接收者测试", 'utf-8') ## 接收者的别名

smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
Python
```

执行上面代码后，登录接收邮件的邮件帐号，这里接收邮件的账号为：`yiibai.com@gmail.com`，登录 http://gmail.com 应该会看到有接收到邮件如下 - 

![img](E:\git\python3-noteboook\python3教程.assets\599110651_72642.png)

**4.4.Python发送带附件的邮件**

要发送带附件的邮件，首先要创建`MIMEMultipart()`实例，然后构造附件，如果有多个附件，可依次构造，最后使用`smtplib.smtp`发送。

实现代码如下所示 - 

```python
##! /usr/bin/env python
##coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



##qq邮箱smtp服务器
host_server = 'smtp.qq.com'
##sender_qq为发件人的qq号码
sender_qq = '769728683@qq.com'
##pwd为qq邮箱的授权码
pwd = '*****mkenb****' ##
##发件人的邮箱
sender_qq_mail = '769728683@qq.com'
##收件人邮箱
receiver = 'yiibai.com@gmail.com'

##邮件的正文内容
mail_content = "你好，<p>这是使用python登录qq邮箱发送HTML格式邮件的测试：</p><p><a href='http://www.yiibai.com'>易百教程</a></p>"
##邮件标题
mail_title = 'Maxsu的邮件'

##邮件正文内容
msg = MIMEMultipart()
##msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = Header("接收者测试", 'utf-8') ## 接收者的别名

##邮件正文内容
msg.attach(MIMEText(mail_content, 'html', 'utf-8'))


## 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('attach.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
## 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="attach.txt"'
msg.attach(att1)

## 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('yiibai.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="yiibai.txt"'
msg.attach(att2)


##ssl登录
smtp = SMTP_SSL(host_server)
##set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
Python
```

执行上面代码后，登录接收邮件的邮件帐号，这里接收邮件的账号为：`yiibai.com@gmail.com`，登录 http://gmail.com 应该会看到有接收到邮件如下 - 

![img](E:\git\python3-noteboook\python3教程.assets\283120658_18531.png)

**4.5.在 HTML 文本中添加图片**

邮件的HTML文本中一般邮件服务商添加外链是无效的，所以要发送带图片的邮件内容，可以参考下面的实例代码实现：

```python
##! /usr/bin/env python
##coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


##qq邮箱smtp服务器
host_server = 'smtp.qq.com'
##sender_qq为发件人的qq号码
sender_qq = '769728683@qq.com'
##pwd为qq邮箱的授权码
pwd = 'h******mk*****' #
##发件人的邮箱
sender_qq_mail = '769728683@qq.com'
##收件人邮箱
receiver = ['yiibai.com@gmail.com','h****u@qq.com']

##邮件的正文内容
mail_content = ""
##邮件标题
mail_title = 'Maxsu的邮件'

##邮件正文内容
##msg = MIMEMultipart()
msg = MIMEMultipart('related')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = Header("接收者测试", 'utf-8') ## 接收者的别名

msgAlternative = MIMEMultipart('alternative')
msg.attach(msgAlternative)


##邮件正文内容
mail_body = """
 <p>你好，Python 邮件发送测试...</p>
 <p>这是使用python登录qq邮箱发送HTML格式和图片的测试邮件：</p>
 <p><a href='http://www.yiibai.com'>易百教程</a></p>
 <p>图片演示：</p>
 <p><img src="cid:send_image"></p>
"""

##msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
msgText = (MIMEText(mail_body, 'html', 'utf-8'))
msgAlternative.attach(msgText)


## 指定图片为当前目录
fp = open('my.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

## 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<send_image>')
msg.attach(msgImage)


##ssl登录
smtp = SMTP_SSL(host_server)
##set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
Python
```

执行上面代码后，登录接收邮件的邮件帐号，这里接收邮件的账号为：`yiibai.com@gmail.com`，登录 http://gmail.com 应该会看到有接收到邮件如下 - 

![img](E:\git\python3-noteboook\python3教程.assets\403140648_30653.png)



## Python多线程编程

同时运行多个线程类似于同时运行多个不同的程序，但具有以下好处 -

- 进程内的多个线程与主线程共享相同的数据空间，因此可以比单独的进程更容易地共享信息或彼此进行通信。
- 线程有时也被称为轻量级进程，它们不需要太多的内存开销; 它们比进程便宜。

线程有一个开始，执行顺序和终止。 它有一个指令指针，可以跟踪其上下文中当前运行的位置。

- 它可以被抢占(中断)。
- 当其他线程正在运行时，它可以临时保留(也称为睡眠) - 这称为让步。

有两种不同的线程 - 

- 内核线程
- 用户线程

内核线程是操作系统的一部分，而用户空间线程未在内核中实现。

有两个模块用于支持在*Python 3*中使用线程 -

- *_thread*
- *threading*

`thread`模块已被“不推荐”了很长一段时间。 鼓励用户使用`threading`模块。 因此，在*Python 3*中，`thread`模块不再可用。 但是，`thread`模块已被重命名为“`_thread`”，用于*Python 3*中的向后兼容性。

### 1.启动新线程

要产生/启动一个线程，需要调用`thread`模块中的以下方法 -

```python
_thread.start_new_thread ( function, args[, kwargs] )
Python
```

这种方法调用可以快速有效地在Linux和Windows中创建新的线程。

方法调用立即返回，子线程启动并使用传递的`args`列表调用函数。当函数返回时，线程终止。

在这里，`args`是一个元组的参数; 使用空的元组来调用函数表示不传递任何参数。 `kwargs`是关键字参数的可选字典。

**示例**

```python
##!/usr/bin/python3

import _thread
import time

## Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

## Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
Python
```

当执行上述代码时，会产生以下结果 -

```python
F:\worksp\python>python thread_start.py
Thread-1: Tue Jun 27 03:06:09 2018
Thread-2: Tue Jun 27 03:06:11 2018
Thread-1: Tue Jun 27 03:06:11 2018
Thread-1: Tue Jun 27 03:06:13 2018
Thread-2: Tue Jun 27 03:06:15 2018
Thread-1: Tue Jun 27 03:06:15 2018
Python
```

程序进入无限循环，可通过按ctrl-c停止或退出。虽然它对于低级线程非常有效，但与较新的线程模块相比，`thread`模块非常有限。

### 2. threading模块

Python 2.4中包含的较新的线程模块为线程提供了比上面讨论的线程模块更强大的高级支持。
线程模块公开了线程模块的所有方法，并提供了一些其他方法 -

- `threading.activeCount()` - 返回活动的线程对象的数量。
- `threading.currentThread()` - 返回调用者线程控件中线程对象的数量。
- `threading.enumerate()` - 返回当前处于活动状态的所有线程对象的列表。

除了这些方法之外，`threading`模块还有实现线程的`Thread`类。 `Thread`类提供的方法如下：

- `run()` - `run()`方法是线程的入口点。
- `start()` - `start()`方法通过调用`run()`方法启动一个线程。
- `join([time])` - `join()`等待线程终止。
- `isAlive()` - `isAlive()`方法检查线程是否仍在执行。
- `getName()` - `getName()`方法返回一个线程的名称。
- `setName()` - `setName()`方法设置线程的名称。

### 3.使用threading模块创建线程

要使用`threading`模块实现新线程，必须执行以下操作：

- 定义`Thread`类的新子类。
- 覆盖`__init __(self [，args])`方法添加其他参数。
- 然后，重写`run(self [，args])`方法来实现线程在启动时应该执行的操作。

当创建了新的`Thread`的子类之后，就可以创建一个实例，然后调用`start()`方法来调用`run()`方法来启动一个新的线程。

**示例**

```python
##!/usr/bin/python3

import threading
import time

exitFlag = 0

class MyThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

## Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

## Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")
Python
```

当运行上述程序时，它会产生以下结果 -

```shell
Starting Thread-1
Starting Thread-2
Thread-1: Tue Jun 27 03:19:43 2017
Thread-2: Tue Jun 27 03:19:44 2017
Thread-1: Tue Jun 27 03:19:44 2017
Thread-1: Tue Jun 27 03:19:45 2017
Thread-2: Tue Jun 27 03:19:46 2017
Thread-1: Tue Jun 27 03:19:46 2017
Thread-1: Tue Jun 27 03:19:47 2017
Exiting Thread-1
Thread-2: Tue Jun 27 03:19:48 2017
Thread-2: Tue Jun 27 03:19:50 2017
Thread-2: Tue Jun 27 03:19:52 2017
Exiting Thread-2
Exiting Main Thread
Shell
```

### 4.同步线程

Python提供的`threading`模块包括一个简单易用的锁定机制，允许同步线程。 通过调用`lock()`方法创建一个新的锁，该方法返回新的锁。

新锁对象的`acquire(blocking)`方法用于强制线程同步运行。可选的`blocking`参数能够控制线程是否要等待获取锁定。

如果`blocking`设置为`0`，则如果无法获取锁定，则线程将立即返回`0`值，如果锁定已获取，则线程返回`1`。 如果`blocking`设置为`1`，则线程将`blocking`并等待锁定被释放。

新的锁定对象的`release()`方法用于在不再需要锁定时释放锁。

**示例**

```python
##!/usr/bin/python3
## save file : MyThread2.py
import threading
import time

class MyThread2 (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      # Get lock to synchronize threads
      threadLock.acquire()
      print_time(self.name, self.counter, 3)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

## Create new threads
thread1 = MyThread2(1, "Thread-1", 1)
thread2 = MyThread2(2, "Thread-2", 2)

## Start new Threads
thread1.start()
thread2.start()

## Add threads to thread list
threads.append(thread1)
threads.append(thread2)

## Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Starting Thread-1
Starting Thread-2
Thread-1: Tue Jun 27 03:51:45 2017
Thread-1: Tue Jun 27 03:51:46 2017
Thread-1: Tue Jun 27 03:51:47 2017
Thread-2: Tue Jun 27 03:51:49 2017
Thread-2: Tue Jun 27 03:51:51 2017
Thread-2: Tue Jun 27 03:51:53 2017
Exiting Main Thread
Shell
```

### 5.多线程优先级队列

`queue`模块允许创建一个新的队列对象，可以容纳特定数量的项目。 有以下方法来控制队列 -

- `get()` - `get()`从队列中删除并返回一个项目。
- `put()` - `put()`将项添加到队列中。
- `qsize()` - `qsize()`返回当前队列中的项目数。
- `empty()` - 如果队列为空，则`empty()`方法返回`True`; 否则返回`False`。
- `full()` - 如果队列已满，则`full()`方法返回`True`; 否则返回`False`。

**示例**

```python
##!/usr/bin/python3
##coding=utf-8

import queue
import threading
import time

exitFlag = 0

class MyQueue (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      process_data(self.name, self.q)
      print ("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = q.get()
         queueLock.release()
         print ("%s processing %s" % (threadName, data))
      else:
         queueLock.release()
         time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

## Create new threads
for tName in threadList:
   thread = MyQueue(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

## Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

## Wait for queue to empty
while not workQueue.empty():
   pass

## Notify threads it's time to exit
exitFlag = 1

## Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")
Python
```

当执行上述代码时，会产生以下结果 -

```shell
Starting Thread-1
Starting Thread-2
Starting Thread-3
Thread-3 processing One
Thread-3 processing Two
Thread-3 processing Three
Thread-3 processing Four
Thread-3 processing Five
Exiting Thread-1
Exiting Thread-2
Exiting Thread-3
Exiting Main Thread
```


## Python XML解析和处理

XML是一种便携式的开源语言，允许程序员开发可由其他应用程序读取的应用程序，而不管操作系统和/或开发语言是什么。

### 1.什么是XML？

可扩展标记语言([XML](http://www.yiibai.com/xml/))是一种非常像HTML或SGML的标记语言。 这是由万维网联盟推荐的，可以作为开放标准。

XML对于存储小到中等数量的数据非常有用，而不需要使用SQL。

### 2.XML解析器体系结构和API

Python标准库提供了一组极少使用但有用的接口来处理XML。两个最基本和最广泛使用在XML数据的API是SAX和DOM接口。

- 简单XML API(SAX) - 在这里，注册感兴趣的事件回调，然后让解析器继续执行文档。 当文档较大或存在内存限制时，此功能非常有用，它会从文件读取文件时解析文件，并且整个文件不会存储在内存中。
- 文档对象模型(DOM)API - 这是一个万维网联盟的推荐，它将整个文件读入存储器并以分层(基于树)的形式存储，以表示XML文档的所有功能。

当处理大文件时，SAX显然无法与DOM一样快地处理信息。 另一方面，使用DOM专门可以真正地占用资源，特别是如果要加许多文件使用的时候。

SAX是只读的，而DOM允许更改XML文件。由于这两种不同的API相辅相成，在大型项目中一般根据需要使用它们。

对于我们所有的XML代码示例，使用一个简单的XML文件：`movies.xml`作为输入 -

```xml
<collection shelf = "New Arrivals">
<movie title = "Enemy Behind">
   <type>War, Thriller</type>
   <format>DVD</format>
   <year>2013</year>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Talk about a US-Japan war</description>
</movie>
<movie title = "Transformers">
   <type>Anime, Science Fiction</type>
   <format>DVD</format>
   <year>1989</year>
   <rating>R</rating>
   <stars>8</stars>
   <description>A schientific fiction</description>
</movie>
   <movie title = "Trigun">
   <type>Anime, Action</type>
   <format>DVD</format>
   <episodes>4</episodes>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Vash the Stampede!</description>
</movie>
<movie title = "Ishtar">
   <type>Comedy</type>
   <format>VHS</format>
   <rating>PG</rating>
   <stars>2</stars>
   <description>Viewable boredom</description>
</movie>
</collection>
XML
```

### 3.使用SAX API解析XML

SAX是事件驱动的XML解析的标准接口。 使用SAX解析XML通常需要通过子类化`xml.sax.ContentHandler`来创建自己的`ContentHandler`。
`ContentHandler`处理XML样式/风格的特定标签和属性。 `ContentHandler`对象提供了处理各种解析事件的方法。它拥有的解析器在解析XML文件时调用`ContentHandler`方法。
在XML文件的开头和结尾分别调用：`startDocument`和`endDocument`方法。 `characters(text)`方法通过参数`text`传递XML文件的字符数据。

`ContentHandler`在每个元素的开头和结尾被调用。如果解析器不在命名空间模式下，则调用`startElement(tag，attributes)`和`endElement(tag)`方法; 否则，调用相应的方法`startElementNS`和`endElementNS`方法。 这里，`tag`是元素标签，属性是`Attributes`对象。

以下是继续前面了解的其他重要方法 -

**make_parser()方法**

以下方法创建一个新的解析器对象并返回它。创建的解析器对象将是系统查找的第一个解析器类型。

```python
xml.sax.make_parser( [parser_list] )
Python
```

以下是参数的详细信息 - 

- *parser_list* - 可选参数，由使用哪个解析器的列表组成，必须全部实现`make_parser`方法。

**parse()方法**

以下方法创建一个SAX解析器并使用它来解析文档。

```python
xml.sax.parse( xmlfile, contenthandler[, errorhandler])
Python
```

以下是参数的详细信息 -

- *xmlfile* - 这是要读取的XML文件的名称。
- *contenthandler* - 这必须是`ContentHandler`对象。
- *errorhandler* - 如果指定，`errorhandler`必须是SAX ErrorHandler

**parseString方法**

还有一种方法来创建SAX解析器并解析指定的XML字符串。

```python
xml.sax.parseString(xmlstring, contenthandler[, errorhandler])
Python
```

以下是参数的详细信息 -

- *xmlstring* - 这是要读取的XML字符串的名称。
- *contenthandler* - 这必须是`ContentHandler`对象。
- *errorhandler* - 如果指定，`errorhandler`必须是SAX `ErrorHandler`对象。

**示例**

```python
##!/usr/bin/python3

import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "movie":
         print ("*****Movie*****")
         title = attributes["title"]
         print ("Title:", title)

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "type":
         print ("Type:", self.type)
      elif self.CurrentData == "format":
         print ("Format:", self.format)
      elif self.CurrentData == "year":
         print ("Year:", self.year)
      elif self.CurrentData == "rating":
         print ("Rating:", self.rating)
      elif self.CurrentData == "stars":
         print ("Stars:", self.stars)
      elif self.CurrentData == "description":
         print ("Description:", self.description)
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "type":
         self.type = content
      elif self.CurrentData == "format":
         self.format = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "rating":
         self.rating = content
      elif self.CurrentData == "stars":
         self.stars = content
      elif self.CurrentData == "description":
         self.description = content

if ( __name__ == "__main__"):

   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )

   parser.parse("movies.xml")
Python
```

这将产生以下结果 -

```python
*****Movie*****
Title: Enemy Behind
Type: War, Thriller
Format: DVD
Year: 2003
Rating: PG
Stars: 10
Description: Talk about a US-Japan war
*****Movie*****
Title: Transformers
Type: Anime, Science Fiction
Format: DVD
Year: 1989
Rating: R
Stars: 8
Description: A schientific fiction
*****Movie*****
Title: Trigun
Type: Anime, Action
Format: DVD
Rating: PG
Stars: 10
Description: Vash the Stampede!
*****Movie*****
Title: Ishtar
Type: Comedy
Format: VHS
Rating: PG
Stars: 2
Description: Viewable boredom
Python
```

有关SAX API文档的完整详细信息，请参阅[标准Python SAX API](http://docs.python.org/library/xml.sax.html)。

### 使用DOM API解析XML

文档对象模型(“DOM”)是来自万维网联盟(W3C)的跨语言API，用于访问和修改XML文档。

DOM对于随机访问应用非常有用。SAX只允许您一次查看文档的一部分。如果想要查看一个SAX元素，则无法访问另一个。

以下是快速加载XML文档并使用`xml.dom`模块创建minidom对象的最简单方法。 minidom对象提供了一个简单的解析器方法，可以从XML文件快速创建一个DOM树。

示例调用`minidom`对象的`parse(file [，parser])`函数来解析由文件指定为DOM树对象的XML文件。

**示例**

```python
##!/usr/bin/python3

from xml.dom.minidom import parse
import xml.dom.minidom

## Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print ("Root element : %s" % collection.getAttribute("shelf"))

## Get all the movies in the collection
movies = collection.getElementsByTagName("movie")

## Print detail of each movie.
for movie in movies:
   print ("*****Movie*****")
   if movie.hasAttribute("title"):
      print ("Title: %s" % movie.getAttribute("title"))

   type = movie.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)
   format = movie.getElementsByTagName('format')[0]
   print ("Format: %s" % format.childNodes[0].data)
   rating = movie.getElementsByTagName('rating')[0]
   print ("Rating: %s" % rating.childNodes[0].data)
   description = movie.getElementsByTagName('description')[0]
   print ("Description: %s" % description.childNodes[0].data)
Python
```

这将产生以下结果 -

```shell
Root element : New Arrivals
*****Movie*****
Title: Enemy Behind
Type: War, Thriller
Format: DVD
Rating: PG
Description: Talk about a US-Japan war
*****Movie*****
Title: Transformers
Type: Anime, Science Fiction
Format: DVD
Rating: R
Description: A schientific fiction
*****Movie*****
Title: Trigun
Type: Anime, Action
Format: DVD
Rating: PG
Description: Vash the Stampede!
*****Movie*****
Title: Ishtar
Type: Comedy
Format: VHS
Rating: PG
Description: Viewable boredom
Shell
```

有关DOM API文档的完整详细信息，请参阅[标准Python DOM API](http://docs.python.org/library/xml.dom.html)。



# 其他杂项



## Python文件对象方法

使用`open()`函数创建一个文件对象，这里是可以在这个对象上调用的函数的列表 -

| 编号 | 方法名称                                                     | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [file.close()](http://www.yiibai.com/python/file_close.html) | 关闭文件，无法读取或写入关闭的文件。                         |
| 2    | [file.flush()](http://www.yiibai.com/python/file_flush.html) | 清空内部缓冲区，类似于`stdio`的`fflush`。                    |
| 3    | [file.fileno()](http://www.yiibai.com/python/file_fileno.html) | 返回底层实现使用的整数文件描述符，以从操作系统请求`I/O`操作。 |
| 4    | [file.isatty()](http://www.yiibai.com/python/file_isatty.html) | 如果文件连接到tty(-like)设备，则返回`True`，否则返回`False`。 |
| 5    | [next(file)](http://www.yiibai.com/python/file_next.html)    | 每次调用时返回文件的下一行。                                 |
| 6    | [file.read([size\])](http://www.yiibai.com/python/file_read.html) | 从文件中读取最多为`size`个字节(如果在获取`size`字节之前读取命中EOF，则读取更少字节的数据)。 |
| 7    | [file.readline([size\])](http://www.yiibai.com/python/file_readline.html) | 从文件中读取一行，字符串中保留一个尾随的换行字符。           |
| 8    | [file.readlines([sizehint\])](http://www.yiibai.com/python/file_readlines.html) | 使用`readline()`读取并返回一个包含行的列表直到`EOF`。 如果可选的`sizehint`参数存在，而不是读取到`EOF`，则读取总共大约为`sizehint`字节的字符串(可能在舍入到内部缓冲区大小之后)的整行。 |
| 9    | [file.seek(offset[, whence\])](http://www.yiibai.com/python/file_seek.html) | 设置文件的当前位置                                           |
| 10   | [file.tell()](http://www.yiibai.com/python/file_tell.html)   | 返回文件的当前位置                                           |
| 11   | [file.truncate([size\])](http://www.yiibai.com/python/file_truncate.html) | 截断文件大小。如果可选的`size`参数存在，则该文件将被截断为`size`(最多)大小。 |
| 12   | [file.write(str)](http://www.yiibai.com/python/file_write.html) | 将一个字符串写入文件，无返回值。                             |
| 13   | [file.writelines(sequence)](http://www.yiibai.com/python/file_writelines.html) | 将一串字符串写入文件。 该序列可以是生成字符串的任何可迭代对象，通常 |


## Python os模块方法

`os`模块提供了大量有用的方法来处理文件和目录。本章节中的代码实例是在 Ubuntu Linux系统上运行来演示。

大多数有用的方法都列在这里 -

| 编号 | 方法                                                         | 描述/说明                                                    |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [os.access(path, mode)](http://www.yiibai.com/python/os_access.html) | 使用真正的`uid/gid`来测试访问指定的路径。                    |
| 2    | [os.chdir(path)](http://www.yiibai.com/python/os_chdir.html) | 将当前工作目录更改为指定路径。                               |
| 3    | [os.chflags(path, flags)](http://www.yiibai.com/python/os_chflags.html) | 将指定的路径的标志设置为数字标志。                           |
| 4    | [os.chmod(path, mode)](http://www.yiibai.com/python/os_chmod.html) | 将路径模式更改为数字模式。                                   |
| 5    | [os.chown(path, uid, gid)](http://www.yiibai.com/python/os_chown.html) | 将指定的路径的所有者和组ID更改为数字uid和gid。               |
| 6    | [os.chroot(path)](http://www.yiibai.com/python/os_chroot.html) | 将当前进程的根目录更改为指定的路径。                         |
| 7    | [os.close(fd)](http://www.yiibai.com/python/os_close.html)   | 关闭文件描述符`fd`。                                         |
| 8    | [os.closerange(fd_low, fd_high)](http://www.yiibai.com/python/os_closerange.html) | 将所有从`fd_low`(包括)到`fd_high`(不包括)的文件描述符关闭，并忽略错误。 |
| 9    | [os.dup(fd)](http://www.yiibai.com/python/os_dup.html)       | 返回文件描述符`fd`的副本。                                   |
| 10   | [os.dup2(fd, fd2)](http://www.yiibai.com/python/os_dup2.html) | 重复从`fd`到`fd2`的文件描述符，如果需要，首先关闭`fd2`。     |
| 11   | [os.fchdir(fd)](http://www.yiibai.com/python/os_fchdir.html) | 将当前工作目录更改为由文件描述符`fd`表示的目录。             |
| 12   | [os.fchmod(fd, mode)](http://www.yiibai.com/python/os_fchmod.html) | 将`fd`给出的文件的模式`mode`更改为数字模式。                 |
| 13   | [os.fchown(fd, uid, gid)](http://www.yiibai.com/python/os_fchown.html) | 将由`fd`提供的文件的所有者和组ID更改为数字`uid`和`gid`。     |
| 14   | [os.fdatasync(fd)](http://www.yiibai.com/python/os_fdatasync.html) | 强制将文件描述符`fd`写入磁盘。                               |
| 15   | [os.fdopen(fd[, mode[, bufsize\]])](http://www.yiibai.com/python/os_fdopen.html) | 返回连接到文件描述符`fd`的打开的文件对象。                   |
| 16   | [os.fpathconf(fd, name)](http://www.yiibai.com/python/os_fpathconf.html) | 返回与打开文件相关的系统配置信息。 `name`指定要检索的配置值。 |
| 17   | [os.fstat(fd)](http://www.yiibai.com/python/os_fstat.html)   | 返回文件描述符`fd`的状态，如`stat()`。                       |
| 18   | [os.fstatvfs(fd)](http://www.yiibai.com/python/os_fstatvfs.html) | 返回有关包含与文件描述符`fd`相关联的文件的文件系统的信息，如`statvfs()`。 |
| 19   | [os.fsync(fd)](http://www.yiibai.com/python/os_fsync.html)   | 强制将文件写入与文件描述符`fd`相关联的磁盘。                 |
| 20   | [os.ftruncate(fd, length)](http://www.yiibai.com/python/os_ftruncate.html) | 截断与文件描述符`fd`相对应的文件，使其大小最大为字节。       |
| 21   | [os.getcwd()](http://www.yiibai.com/python/os_getcwd.html)   | 返回一个表示当前工作目录的字符串。                           |
| 22   | [os.getcwdu()](http://www.yiibai.com/python/os_getcwdu.html) | 返回表示当前工作目录的`Unicode`对象。                        |
| 23   | [os.isatty(fd)](http://www.yiibai.com/python/os_isatty.html) | 如果文件描述符`fd`打开并连接到tty(-like)设备，则返回`True`，否则返回`False`。 |
| 24   | [os.lchflags(path, flags)](http://www.yiibai.com/python/os_lchflags.html) | 将路径(`path`)的标志设置为数字标志，如`chflags()`，但不要跟随符号链接。 |
| 25   | [os.lchmod(path, mode)](http://www.yiibai.com/python/os_lchmod.html) | 将路径模式更改为数字模式。                                   |
| 26   | [os.lchown(path, uid, gid)](http://www.yiibai.com/python/os_lchown.html) | 将路径的所有者和组ID更改为数字uid和gid。此功能不会遵循符号链接。 |
| 27   | [os.link(src, dst)](http://www.yiibai.com/python/os_link.html) | 创建一个指向`src`名为`dst`的硬链接。                         |
| 28   | [os.listdir(path)](http://www.yiibai.com/python/os_listdir.html) | 返回一个列表，其中包含由`path`指定的目录中的条目的名称。     |
| 29   | [os.lseek(fd, pos, how)](http://www.yiibai.com/python/os_lseek.html) | 将文件描述符`fd`的当前位置设置为位置`pos`，由`how`指定如何修改。 |
| 30   | [os.lstat(path)](http://www.yiibai.com/python/os_lstat.html) | 类似于`stat()`，但不遵循符号链接。                           |
| 31   | [os.major(device)](http://www.yiibai.com/python/os_major.html) | 从原始设备号中提取设备主体号码。                             |
| 32   | [os.makedev(major, minor)](http://www.yiibai.com/python/os_makedev.html) | 从主要和次要设备编号构成原始设备编号。                       |
| 33   | [os.makedirs(path[, mode\])](http://www.yiibai.com/python/os_makedirs.html) | 递归目录创建函数。                                           |
| 34   | [os.minor(device)](http://www.yiibai.com/python/os_minor.html) | 从原始设备号中提取设备次要号码。                             |
| 35   | [os.mkdir(path[, mode\])](http://www.yiibai.com/python/os_mkdir.html) | 以数字模式`mode`创建名为`path`的目录。                       |
| 36   | [os.mkfifo(path[, mode\])](http://www.yiibai.com/python/os_mkfifo.html) | 以数字模式模式创建名为`path`的FIFO(命名管道)。 默认模式为0666(八进制)。 |
| 37   | [os.mknod(filename[, mode = 0600, device\])](http://www.yiibai.com/python/os_mknod.html) | 创建名为`filename`的文件系统节点(文件，设备专用文件或命名管道)。 |
| 38   | [os.open(file, flags[, mode\])](http://www.yiibai.com/python/os_open.html) | 打开文件文件，并根据标志和可能的模式根据模式设置各种标志。   |
| 39   | [os.openpty()](http://www.yiibai.com/python/os_openpty.html) | 打开一个新的伪终端对。分别为pty和tty返回一对文件描述符(主，从)。 |
| 40   | [os.pathconf(path, name)](http://www.yiibai.com/python/os_pathconf.html) | 返回与命名文件相关的系统配置信息。                           |
| 41   | [os.pipe()](http://www.yiibai.com/python/os_pipe.html)       | 创建一个管道。分别返回一对可用于阅读和写入的文件描述符(r，w)。 |
| 42   | [os.popen(command[, mode[, bufsize\]])](http://www.yiibai.com/python/os_popen.html) | 打开或从命令打开管道。                                       |
| 43   | [os.read(fd, n)](http://www.yiibai.com/python/os_read.html)  | 从文件描述符`fd`读取最多`n`个字节。 返回一个包含读取字节的字符串。 如果`fd`引用的文件的末尾已经到达，则返回一个空字符串。 |
| 44   | [os.readlink(path)](http://www.yiibai.com/python/os_readlink.html) | 返回一个表示符号链接所指向的路径的字符串。                   |
| 45   | [os.remove(path)](http://www.yiibai.com/python/os_remove.html) | 删除文件路径。                                               |
| 46   | [os.removedirs(path)](http://www.yiibai.com/python/os_removedirs.html) | 递归删除目录。                                               |
| 47   | [os.rename(src, dst)](http://www.yiibai.com/python/os_rename.html) | 将文件或目录`src`重命名为`dst`。                             |
| 48   | [os.renames(old, new)](http://www.yiibai.com/python/os_renames.html) | 递归目录或文件重命名功能。                                   |
| 49   | [os.rmdir(path)](http://www.yiibai.com/python/os_rmdir.html) | 删除目录路径                                                 |
| 50   | [os.stat(path)](http://www.yiibai.com/python/os_stat.html)   | 在给定的路径上执行`stat`系统调用。                           |
| 51   | [os.stat_float_times([newvalue\])](http://www.yiibai.com/python/os_stat_float_times.html) | 确定`stat_result`是否将时间戳表示为浮点对象。                |
| 52   | [os.statvfs(path)](http://www.yiibai.com/python/os_statvfs.html) | 在给定路径上执行`statvfs`系统调用。                          |
| 53   | [os.symlink(src, dst)](http://www.yiibai.com/python/os_symlink.html) | 创建一个指向`src`的符号链接，命名为`dst`。                   |
| 54   | [os.tcgetpgrp(fd)](http://www.yiibai.com/python/os_tcgetpgrp.html) | 返回与`fd`(由`open()`返回的打开的文件描述符)给出的终端关联的进程组。 |
| 55   | [os.tcsetpgrp(fd, pg)](http://www.yiibai.com/python/os_tcsetpgrp.html) | 将与`fd`(`open()`返回的打开的文件描述符)给定的终端相关联的进程组`pg`。 |
| 56   | [os.tempnam([dir[, prefix\]])](http://www.yiibai.com/python/os_tempnam.html) | 返回创建临时文件的唯一路径名。                               |
| 57   | [os.tmpfile()](http://www.yiibai.com/python/os_tmpfile.html) | 返回以更新模式打开的新文件对象(`w+b`)。                      |
| 58   | [os.tmpnam()](http://www.yiibai.com/python/os_tmpnam.html)   | 返回创建临时文件的唯一路径名。                               |
| 59   | [os.ttyname(fd)](http://www.yiibai.com/python/os_ttyname.html) | 返回指定与文件描述符`fd`相关联的终端设备的字符串。 如果`fd`与终端设备没有关联，则会出现异常。 |
| 60   | [os.unlink(path)](http://www.yiibai.com/python/os_unlink.html) | 删除文件路径。                                               |
| 61   | [os.utime(path, times)](http://www.yiibai.com/python/os_utime.html) | 设置由`path`指定的文件的访问和修改时间。                     |
| 62   | [os.walk(top[, topdown = True[, onerror = None[, followlinks = False\]]])](http://www.yiibai.com/python3/os_walk.html) | 通过自上而下或自下而上地遍历树来生成目录树中的文件名。       |
| 63   | [os.write(fd, str)](http://www.yiibai.com/python/os_write.html) | 将字符串`str`写入文件描述符`fd`。 返回实际写入的字节数。     |


## Python迭代器

迭代器是可以迭代的对象。 在本教程中，您将了解迭代器的工作原理，以及如何使用`__iter__`和`__next__`方法构建自己的迭代器。

迭代器在Python中无处不在。 它们优雅地实现在循环，推导，生成器等中，但隐藏在明显的视觉中。

Python中的迭代器只是一个可以迭代的对象。一个将一次返回数据的对象或一个元素。

从技术上讲，Python迭代器对象必须实现两个特殊的方法`__iter__()`和`__next__()`，统称为迭代器协议。

如果我们从中获取一个迭代器，那么一个对象被称为`iterable`。 大多数Python中的内置容器是列表，元组，字符串等都是可迭代的。

`iter()`函数(这又调用`__iter__()`方法)返回一个迭代器。

### 通过Python中的迭代器迭代

使用`next()`函数来手动遍历迭代器的所有项目。当到达结束，没有更多的数据要返回时，它将会引发`StopIteration`。 以下是一个例子。

```python
## define a list
my_list = [4, 7, 0, 3]

## get an iterator using iter()
my_iter = iter(my_list)

### iterate through it using next() 

##prints 4
print(next(my_iter))

##prints 7
print(next(my_iter))

### next(obj) is same as obj.__next__()

##prints 0
print(my_iter.__next__())

##prints 3
print(my_iter.__next__())

### This will raise error, no items left
next(my_iter)
Python
```

更优雅的自动迭代方式是使用`for`循环。 使用`for`循环可以迭代任何可以返回迭代器的对象，例如列表，字符串，文件等。

```python
>>> for element in my_list:
...     print(element)
...     
4
7
0
3
Python
```

### 循环如何实际工作？

在上面的例子中看到的，`for`循环能够自动通过列表迭代。

事实上，`for`循环可以迭代任何可迭代对象。我们来仔细看一下在Python中是如何实现`for`循环的。

```python
for element in iterable:
    # do something with element
Python
```

实际上它是以类似下面的方式来实现的 - 

```python
## create an iterator object from that iterable
iter_obj = iter(iterable)

## infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
Python
```

所以在`for`的内部，`for`循环通过在可迭代的对象上调用`iter()`来创建一个迭代器对象`iter_obj`。

有意思的是，这个`for`循环实际上是一个无限循环~..~。

在循环中，它调用`next()`来获取下一个元素，并使用该值执行`for`循环的主体。 在所有对象耗尽后，引发`StopIteration`异常，内部被捕获从而结束循环。请注意，任何其他类型的异常都将正常通过。

### 在Python中构建自己的Iterator

构建迭代器在Python中很容易。只需要实现`__iter__()`和`__next__()`方法。

`__iter__()`方法返回迭代器对象本身。如果需要，可以执行一些初始化。

`__next__()`方法必须返回序列中的下一个项目(数据对象)。 在到达结束后，并在随后的调用中它必须引发`StopIteration`异常。

在这里，我们展示一个例子，在每次迭代中给出下一个`2`的几次方。 次幂指数从零开始到用户设定的数字。

```python
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
Python
```

现在可以创建一个迭代器，并通过它迭代如下 - 

```shell
>>> a = PowTwo(4)
>>> i = iter(a)
>>> next(i)
1
>>> next(i)
2
>>> next(i)
4
>>> next(i)
8
>>> next(i)
16
>>> next(i)
Traceback (most recent call last):
...
StopIteration
Shell
```

也可以使用`for`循环迭代那些迭代器类。

```shell
>>> for i in PowTwo(5):
...     print(i)
...     
1
2
4
8
16
32
Shell
```

### Python无限迭代器

迭代器对象中的项目不必都是可耗尽的，可以是无限迭代器(永远不会结束)。 处理这样的迭代器时一定要小心。

下面是用来演示无限迭代器的一个简单的例子。

内置的函数`iter()`可以用两个参数来调用，其中第一个参数必须是可调用对象(函数)，而第二个参数是标头。迭代器调用此函数，直到返回的值等于指定值。

```python
>>> int()
0

>>> inf = iter(int,1)
>>> next(inf)
0
>>> next(inf)
0
Python
```

可以看到，`int()函`数总是返回`0`，所以将它作为`iter(int，1)`传递将返回一个调用`int()`的迭代器，直到返回值等于`1`。这从来没有发生，所以这样就得到一个无限迭代器。

我们也可以建立自己的无限迭代器。 以下迭代器理论上将返回所有奇数。

```python
class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num
Python
```

示例运行如下 - 

```shell
>>> a = iter(InfIter())
>>> next(a)
1
>>> next(a)
3
>>> next(a)
5
>>> next(a)
7
Shell
```

当迭代这些类型的无限迭代器时，请注意指定终止条件。

使用迭代器的优点是它们可以节省资源。 如上所示，我们可以获得所有奇数，而不将整个系统存储在内存中。理论上，可以在有限的内存中计算有无限的项目。



## Python生成器

在本文中，将学习如何使用Python生成器来创建迭代，了解它与迭代器和常规函数有什么区别，以及为什么要使用它。

在Python中构建迭代器有很多开销; 必须使用`__iter__()`和`__next__()`方法实现一个类，跟踪内部状态，当没有值被返回时引发`StopIteration`异常。

Python生成器是创建迭代器的简单方法。上面提到的所有开销都由Python中的生成器自动处理。

简单来说，生成器是返回一个可以迭代的对象(迭代器)的函数(一次一个值)。

### 如何在Python中创建生成器？

在Python中创建生成器是相当简单的。 它使用`yield`语句而不是`return`语句来定义，与正常函数一样简单。

如果函数包含至少一个`yield`语句(它可能包含其他`yield`或`return`语句)，那么它将成为一个生成器函数。 `yield`和`return`都将从函数返回一些值。

不同的是，`return`语句完全终止函数，但`yield`语句会暂停函数保存其所有状态，并在以后的连续调用中继续执行(有点像线程挂起的意思)。

#### 生成器函数与正常函数的差异

下面列出的是生成器函数与正常函数的区别 - 

- 生成器函数包含一个或多个`yield`语句。
- 当被调用时，它返回一个对象(迭代器)，但不会立即开始执行。
- `__iter__()`和`__next__()`之类的方法将自动实现。所以可以使用`next()`迭代项目。
- 一旦函数退让(`yields`)，该函数将被暂停，并将该控制权交给调用者。
- 局部变量及其状态在连续调用之间被记住。
- 最后，当函数终止时，`StopIteration`会在进一步的调用时自动引发。

下面的例子用来说明上述所有要点。 我们有一个名为`my_gen()`的生成器函数和几个`yield`语句。

```python
##!/usr/bin/python3
##coding=utf-8

def my_gen():
    n = 1
    print('This is printed first, n= ', n)
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second, n= ', n)
    yield n

    n += 1
    print('This is printed at last, n= ', n)
    yield n
Python
```

下面给出了交互式运行结果。 在Python shell中运行它们以查看输出 - 

```shell
>>> # It returns an object but does not start execution immediately.
>>> a = my_gen()

>>> # We can iterate through the items using next().
>>> next(a)
This is printed first, n = 1
1
>>> # Once the function yields, the function is paused and the control is transferred to the caller.

>>> # Local variables and theirs states are remembered between successive calls.
>>> next(a)
This is printed second, n = 2
2

>>> next(a)
This is printed at last, n = 3
3

>>> # Finally, when the function terminates, StopIteration is raised automatically on further calls.
>>> next(a)
Traceback (most recent call last):
...
StopIteration
>>> next(a)
Traceback (most recent call last):
...
StopIteration
Shell
```

在上面的例子中需要注意的是，在每个调用之间函数会保持住变量`n`的值。
与正常函数不同，当函数产生时，局部变量不会被销毁。 此外，生成器对象只能重复一次。

要重新启动该过程，需要使用类似于`a = my_gen()`的方法创建另一个生成器对象。

> 注意：最后要注意的是，可以直接使用带有`for`循环的生成器。

这是因为，`for`循环需要一个迭代器，并使用`next()`函数进行迭代。 当`StopIteration`被引发时，它会自动结束。 请查看这里了解一个[for循环](http://www.yiibai.com/python/iterator.html#for-loop-working)是如何在Python中实际实现的。

```python
## A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

## Using for loop
for item in my_gen():
    print(item)
Python
```

当运行程序时，将输出结果为：

```python
This is printed first
1
This is printed second
2
This is printed at last
3
Python
```

### 具有循环的Python生成器

上面的例子没有什么用，我们研究它只是为了了解在后台发生了什么。通常，生成器功能用具有适当终止条件的循环实现。

我们举一个反转字符串的生成器的例子 - 

```python
 length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

## For loop to reverse the string
## Output:
## o
## l
## l
## e
## h
for char in rev_str("hello"):
     print(char)def rev_str(my_str):
Python
```

在这个例子中，使用`range()`函数使用`for`循环以相反的顺序获取索引。事实证明，这个生成函数不仅可以使用字符串，还可以使用其他类型的列表，元组等迭代。

### Python生成器表达式

使用生成器表达式，可以轻松创建简单的生成器。 它使构建生成器变得容易。

与`lambda`函数一样创建一个匿名函数，生成器表达式创建一个匿名生成函数。生成器表达式的语法与Python中的列表解析类似。 但方圆`[]`替换为圆括号`()`。

列表推导和生成器表达式之间的主要区别是：列表推导产生整个列表，生成器表达式一次生成一个项目。

它们是处理方式是懒惰的，只有在被要求时才能生产项目。 因此，生成器表达式的存储器效率高于等效列表的值。

```python
## Initialize the list
my_list = [1, 3, 6, 10]

## square each term using list comprehension
## Output: [1, 9, 36, 100]
[x**2 for x in my_list]

## same thing can be done using generator expression
## Output: <generator object <genexpr> at 0x0000000002EBDAF8>
(x**2 for x in my_list)
Python
```

我们可以看到，生成器表达式没有立即生成所需的结果。 相反，它返回一个发生器对象，并根据需要生成项目。

```python
## Intialize the list
my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
## Output: 1
print(next(a))

## Output: 9
print(next(a))

## Output: 36
print(next(a))

## Output: 100
print(next(a))

## Output: StopIteration
next(a)
Python
```

生成器表达式可以在函数内部使用。当以这种方式使用时，圆括号可以丢弃。

```shell
>>> sum(x**2 for x in my_list)
146

>>> max(x**2 for x in my_list)
100
Shell
```

### 为什么在Python中使用生成器？

有几个原因使得生成器成为有吸引力。

#### 1. 容易实现

与其迭代器类相比，发生器可以以清晰简洁的方式实现。 以下是使用迭代器类来实现`2`的幂次序的例子。

```python
class PowTwo:
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result
Python
```

上面代码有点长，可以使用一个生成器函数实现同样的功能。

```python
def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
Python
```

因为，生成器自动跟踪的细节，它更简洁，更干净。

#### 2.内存高效

返回序列的正常函数将在返回结果之前会在内存中的创建整个序列。如果序列中的项目数量非常大，这可是要消耗内存的。

序列的生成器实现是内存友好的，并且是推荐使用的，因为它一次仅产生一个项目。

#### 3. 表未无限流

生成器是表示无限数据流的绝佳媒介。 无限流不能存储在内存中，由于生成器一次只能生成一个项目，因此可以表示无限数据流。

以下示例可以生成所有偶数(至少在理论上)。

```python
def all_even():
    n = 0
    while True:
        yield n
        n += 2
Python
```

#### 4.管道生成器

生成器可用于管理一系列操作，下面使用一个例子说明。

假设我们有一个快餐连锁店的日志文件。 日志文件有一列(第`4`列)，用于跟踪每小时销售的比萨饼数量，我们想算出在`5`年内销售的总萨饼数量。

假设一切都是字符串，不可用的数字标记为“`N / A`”。 这样做的生成器实现可以如下。

```python
with open('sells.log') as file:
    pizza_col = (line[3] for line in file)
    per_hour = (int(x) for x in pizza_col if x != 'N/A')
    print("Total pizzas sold = ",sum(per_hour))
Python
```

这种管道的方式是更高效和易于阅读的。


## Python闭包

在本文中，您将了解什么是Python闭包，如何定义闭包以及应该如何使用闭包。

### 嵌套函数中的非局部变量

在进入闭包之前，我们必须先了解一个嵌套函数和非局部变量。

在函数中定义另一个函数称为嵌套函数。嵌套函数可以访问包围范围内的变量。

在Python中，这些非局部变量只能在默认情况下读取，我们必须将它们显式地声明为非局部变量(使用`nonlocal`关键字)才能进行修改。

以下是访问非局部变量的嵌套函数的示例。

```python
def print_msg(msg):
## This is the outer enclosing function

    def printer():
## This is the nested function
        print(msg)

    printer()

## We execute the function
## Output: Hello
print_msg("Hello")
Python
```

可以看到嵌套函数`printer()`能够访问封闭函数的非局部变量`msg`。

### 定义闭包函数

在上面的例子中，如果函数`print_msg()`的最后一行返回`printer()`函数而不是调用它，会发生什么？ 如该函数定义如下 - 

```python
def print_msg(msg):
## This is the outer enclosing function

    def printer():
## This is the nested function
        print(msg)

    return printer  # this got changed

## Now let's try calling this function.
## Output: Hello
another = print_msg("Hello")
another()
Python
```

这样是不寻常的。

`print_msg()`函数使用字符串“`Hello`”进行调用，返回的函数被绑定到另一个名称。 在调用`another()`时，尽管我们已经完成了`print_msg()`函数的执行，但仍然记住了这个消息。

一些数据(“`Hello`”)附加到代码中的这种技术在Python中称为闭包。

即使变量超出范围或函数本身从当前命名空间中删除，也会记住封闭范围内的值。

尝试在Python shell中运行以下内容以查看输出。

```python
>>> del print_msg
>>> another()
Hello
>>> print_msg("Hello")
Traceback (most recent call last):
...
NameError: name 'print_msg' is not defined
Python
```

### 什么时候闭包？

从上面的例子可以看出，当嵌套函数引用其封闭范围内的值时，在Python中有使用了一个闭包。

在Python中创建闭包必须满足的标准将在以下几点 - 

- 必须有一个嵌套函数(函数内部的函数)。
- 嵌套函数必须引用封闭函数中定义的值。
- 闭包函数必须返回嵌套函数。

### 何时使用闭包？

**那么闭包是什么好的？**

闭包可以避免使用全局值并提供某种形式的数据隐藏。它还可以提供面向对象的解决问题的解决方案。

当在类中几乎没有方法(大多数情况下是一种方法)时，闭包可以提供一个替代的和更优雅的解决方案。 但是当属性和方法的数量变大时，更好地实现一个类。

这是一个简单的例子，其中闭包可能比定义类和创建对象更为优先。

```python
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

## Multiplier of 3
times3 = make_multiplier_of(3)

## Multiplier of 5
times5 = make_multiplier_of(5)

## Output: 27
print(times3(9))

## Output: 15
print(times5(3))

## Output: 30
print(times5(times3(2)))
Python
```

Python中的装饰器也可以广泛使用闭包。值得注意的是，可以找到封闭函数中包含的值。

所有函数对象都有一个`__closure__`属性，如果它是一个闭包函数，它返回一个单元格对象的元组。 参考上面的例子，我们知道`times3`和`times5`是闭包函数。

```python
>>> make_multiplier_of.__closure__
>>> times3.__closure__
(<cell at 0x0000000002D155B8: int object at 0x000000001E39B6E0>,)
Python
```

单元格(`cell`)对象具有存储闭合值的属性：`cell_contents`。

```python
>>> times3.__closure__[0].cell_contents
3
>>> times5.__closure__[0].cell_contents
5
```


#### Python修饰器

装饰器接收一个功能，添加一些功能并返回。 在本文中，您将学习如何创建装饰器，以及为什么要使用装饰器。

Python有一个有趣的功能，称为装饰器，以便为现有代码添加功能。

这也称为元编程，作为程序的一部分，尝试在编译时修改程序的另一部分。

### 学习装修器之前需要了解什么？

为了了解装饰器，我们首先在Python中了解一些基本的东西。

Python中的一切(是的，甚至是类)都是对象。 我们定义的名称只是绑定到这些对象的标识符。 函数也不例外，它们也是对象(带有属性)。 各种不同的名称可以绑定到同一个功能对象。

看看下面一个示例 - 

```python
def first(msg):
    print(msg)    

first("Hello")

second = first
second("Hello")
Python
```

当运行代码时，`first`和`second`函数都提供相同的输出。 这里名称`first`和`second`引用相同的函数对象。

函数可以作为参数传递给另一个函数。

如果您在Python中使用了`map`，`filter`和`reduce`等功能，那么您就了解了。

将其他函数作为参数的函数也称为高阶函数。下面是这样子的一个函数的例子。

```python
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result
Python
```

我们调用函数如下 - 

```python
>>> operate(inc,3)
4
>>> operate(dec,3)
2
Python
```

此外，一个函数可以返回另一个函数。

```python
def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()

##Outputs "Hello"
new()
Python
```

这里，`is_returned()`是一个定义的嵌套函数，在每次调用`is_called()`时返回。

### 回到装饰器

实际上，实现特殊方法`__call__()`的任何对象都被称为可调用。 因此，在最基本的意义上，装饰器是可调用的，并且可以返回可调用。

基本上，装饰器接收一个函数，添加一些函数并返回。

```python
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")
Python
```

当在shell中运行以下代码时，如下 -

```python
>>> ordinary()
I am ordinary

>>> # let's decorate this ordinary function
>>> pretty = make_pretty(ordinary)
>>> pretty()
I got decorated
I am ordinary
Python
```

在上面的例子中，`make_pretty()`是一个装饰器。 在分配步骤。

```python
pretty = make_pretty(ordinary)
Python
```

函数`ordinary()`得到了装饰，返回函数的名字：`pretty`。

可以看到装饰函数为原始函数添加了一些新功能。这类似于包装礼物。 装饰器作为包装纸。 装饰物品的性质(里面的实际礼物)不会改变。 但现在看起来很漂亮(因为装饰了)。

一般来说，我们装饰一个函数并重新分配它，

```python
ordinary = make_pretty(ordinary).
Python
```

这是一个常见的结构，Python有一个简化的语法。

可以使用`@`符号和装饰器函数的名称，并将其放在要装饰的函数的定义之上。 例如，

```python
@make_pretty
def ordinary():
    print("I am ordinary")
Python
```

上面代码相当于 - 

```python
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)
Python
```

### 用参数装饰函数

上面的装饰器很简单，只适用于没有任何参数的函数。 如果有函数要接受如下的参数怎么办？

```python
def divide(a, b):
    return a/b
Python
```

该函数有两个参数`a`和`b`。 我们知道，如果将`b`的值设置为`0`并传递那么是会出错的。

```python
>>> divide(2,5)
0.4
>>> divide(2,0)
Traceback (most recent call last):
...
ZeroDivisionError: division by zero
Python
```

现在使用一个装饰器来检查这个错误。

```python
def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b
Python
```

如果发生错误，这个新的实现将返回`None`。

```python
>>> divide(2,5)
I am going to divide 2 and 5
0.4

>>> divide(2,0)
I am going to divide 2 and 0
Whoops! cannot divide
Python
```

以这种方式就可以装饰函数的参数了。

应该会注意到，装饰器中嵌套的`inner()`函数的参数与其装饰的函数的参数是一样的。 考虑到这一点，现在可以让一般装饰器使用任何数量的参数。

在Python中，这个由`function(* args，** kwargs)`完成。 这样，`args`将是位置参数的元组，`kwargs`将是关键字参数的字典。这样的装饰器的例子将是。

```python
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner
Python
```

### 在Python中链接装饰器

多个装饰器可以在Python中链接。

这就是说，一个函数可以用不同(或相同)装饰器多次装饰。只需将装饰器放置在所需函数之上。

```python
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hello")
Python
```

执行上面代码，将输出结果如下 - 

```python
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
Python
```

以上语法，

```python
@star
@percent
def printer(msg):
    print(msg)
Python
```

相当于以下 - 

```python
def printer(msg):
    print(msg)
printer = star(percent(printer))
Python
```

链装饰器的顺序是重要的。 所以如果把顺序颠倒了执行结果就不一样了，如下 - 

```python
@percent
@star
def printer(msg):
    print(msg)
Python
```

执行上面代码，将输出结果如下 - 

```python
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
Hello
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```

