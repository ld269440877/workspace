```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  id='utf-8' continue:true output='markdown' } ##hide  代码隐藏 
import pandas as pd
from pandas import Series,DataFrame
import numpy as np

import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

```


# pandas

- Pandas 是基于NumPy 的⼀一种⼯工具，该⼯工具是为了了解决数据分析任务⽽而创建的。Pandas 纳⼊入了了⼤大量量库和⼀一些标准的数据模型，提供了了⾼高效地操作⼤大型数据集所需的⼯工具。pandas提供了了⼤大量量能使我们快速便便捷地处理理数据的函数和⽅方法。
- Pandas基于两种数据类型：series与dataframe。
## Series对象
Series
: 是Pandas中最基本的对象，Series类似⼀一种⼀一维数组。事实上，Series 基本上就是基于 NumPy的数组对象来的。和 NumPy 的数组不不同，Series 能为数据⾃自定义标签，也就是索引（index），然后通过索引来访问数组中的数据。

Dataframe是一个二维的表结构。Pandas的dataframe可以存储许多种不同的数据类型，并且每⼀个坐标轴都有⾃己的标签。你可以把它想象成⼀个series的字典项。

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8' } ##hide  代码隐藏  output='markdown'
# 创建Series对象并省略略索引
'''
index 参数是可省略略的，你可以选择不不输⼊入这个参数。
如果不不带 index 参数，Pandas 会⾃自动⽤用默认 index 进行索引，类似数组，索引值是 [0, ...,len(data) - 1]
'''
sel = Series([1,2,3,4])
print(sel)
# 通常我们会⾃自⼰己创建索引
# sel = Series(data = [1,2,3,4], index = ['a','b','c','d'])
sel = Series(data = [1,2,3,4], index = list('abcd'))
'''
a 1
b 2
c 3
d 4
dtype: int64
'''
print(sel)
# 获取内容
print(sel.values)
'[1 2 3 4]'
# 获取索引
print(sel.index)
'''
Index([‘a’, ‘b’, ‘c’, ‘d’], dtype=‘object’)
'''
# 获取索引和值对
print(list(sel.iteritems()))
'''
[(‘a’, 1), (‘b’, 2), (‘c’, 3), (‘d’, 4)]
'''
```
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

# 将字典转换为Series
dict={"red":100,"black":400,"green":300,"pink":900}
se3=Series(dict)
print(se3)
'''
red 100
black 400
green 300
pink 900
dtype: int64
'''

```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

# Series数据获取
sel = Series(data = [1,2,3,4], index = list('abcd'))
print(sel)
'''
a 1
b 2
c 3
d 4
dtype: int64
'''
# Series对象同时⽀支持位置和标签两种⽅方式获取数据
print('索引下标',sel['c'])
'索引下标 3'
print('位置下标',sel[2])
'位置下标 3'
# 获取不不连续的数据
print('索引下标',sel[['a','c']])
'''
索引下标
a 1
c 3
dtype: int64
'''
print('位置下标',sel[[1,3]])
'''
位置下标 
b 2
d 4
dtype: int64
'''
# 可以使⽤用切⽚片或取数据
print('位置切⽚片',sel[1:3])# 左包含右不不包含
'''
位置切⽚片 
b 2
c 3
dtype: int64
'''
print('索引切⽚片',sel['b':'d'])# 左右都包含
'''
索引切⽚片 
b 2
c 3
d 4
dtype: int64
'''

# 重新赋值索引的值
sel.index = list('dcba')
print(sel)
'''
d 1
c 2
b 3
a 4
dtype: int64
'''
# ReIndex重新索引,会返回⼀一个新的Series(调⽤用reindex将会重新排序，
# 缺失值则⽤用NaN填补)   NaN的数据类型默认为float类型
print(sel.reindex(['b','a','c','d','e']))
'''
b 3.0
a 4.0
c 2.0
d 1.0
e NaN
dtype: float64
'''
# Drop丢弃指定轴上的项
se1=pd.Series(range(10,15))
print(se1)
'''
0 10
1 11
2 12
3 13
4 14
dtype: int64
'''
print(se1.drop([2,3]))
'''
0 10
1 11
4 14
dtype: int64
'''
```

### Series 进行算术运算操作

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

'''
对 Series 的算术运算都是基于 index 进行的。
我们可以⽤用加减乘除（+ - * /）这样的运算符对两个 Series 进行运算，
Pandas 将会根据索引 index，对响应的数据进行计算，结果将会以浮点数的形式存储，以避免丢失精度。
如果 Pandas 在两个 Series 里找不到相同的 index，对应的位置就返回⼀个空值 NaN
'''
series1 = pd.Series([1,2,3,4],['London','HongKong','Humbai','lagos'])
series2 = pd.Series([1,3,6,4],['London','Accra','lagos','Delhi'])
print(series1-series2)
'''
Accra NaN
Delhi NaN
HongKong NaN
Humbai NaN
London 0.0
lagos -2.0
dtype: float64
'''
print(series1+series2)
'''
Accra NaN
Delhi NaN
HongKong NaN
Humbai NaN
London 2.0
lagos 10.0
dtype: float64
'''
print(series1*series2)
'''
Accra NaN
Delhi NaN
HongKong NaN
Humbai NaN
London 1.0
lagos 24.0
dtype: float64
'''
# 同样也⽀支持numpy的数组运算
sel = Series(data = [1,6,3,5], index = list('abcd'))
print(sel[sel>3]) # 布尔数组过滤
'''
b 6
d 5
dtype: int64
'''

print(sel*2) # 标量量乘法
'''
a 2
b 12
c 6
d 10
dtype: int64
'''
print(np.square(sel)) # 可以直接加⼊入到numpy的数学函数
'''
a 2
b 12
c 6
d 10
dtype: int64
'''

```
## DataFrame
DataFrame
:   （数据表）是一种 2 维数据结构，数据以表格的形式存储，分成若⼲行行和列列。
通过DataFrame，你能很⽅方便便地处理理数据。常⻅见的操作⽐比如选取、替换⾏行行或列列的数据，还能重组数据表、修改索引、多重筛选等。我们基本上可以把 DataFrame 理理解成⼀一组采⽤用同样索引的 Series 的集合。
调⽤用DataFrame()可以将多种格式的数据转换为DataFrame对象，它的的三个参数data、index和columns分别为数据、⾏行行索引和列列索引

### DataFrame的创建

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

# 1. 创建DataFrame
# 使⽤用二维数组
df1 = DataFrame(np.random.randint(0,10,(4,4)),index=[1,2,3,4],columns=
['a','b','c','d'])
df1.index.name = 'index'
df1.columns.name = 'columns'
# print(df1)
'''
columns a b c d
index
1        7 3 5 0
2        9 7 2 2
3        4 3 8 9
4        3 1 1 9
4        8 2 8 4
'''
# 使⽤用字典创建(行索引由index决定，列列索引由字典的键决定)
dict={
'Province': ['Guangdong', 'Beijing', 'Qinghai', 'Fujian'],
'pop': [1.3, 2.5, 1.1, 0.7],
'year': [2018, 2018, 2018, 2018]}
df2=pd.DataFrame(dict,index=[1,2,3,4])
# print(df2)
'''
    Province pop year
1 Guangdong 1.3 2018
2 Beijing   2.5 2018
3 Qinghai   1.1 2018
4 Fujian    0.7 2018
'''

# 使⽤用from_dict
dict2={"a":[1,2,3],"b":[4,5,6]}
df6=pd.DataFrame.from_dict(dict2)
# print(df6)
'''
  a b
0 1 4
1 2 5
2 3 6
'''
#索引相同的情况下，相同索引的值会相对应，缺少的值会添加NaN
data = {
'Name':pd.Series(['zs','ls','we'],index=['a','b','c']),
'Age':pd.Series(['10','20','30','40'],index=['a','b','c','d']),
'country':pd.Series(['中国','⽇日本','韩国'],index=['a','c','b'])
}
df = pd.DataFrame(data)
# print(df)
'''
Name Age country
a zs 10 中国
b ls 20 韩国
c we 30 ⽇日本
d NaN 40 NaN
'''
# to_dict()⽅方法将DataFrame对象转换为字典
dict = df.to_dict()
# print(dict)
'''
{
‘Name’: {‘a’: ‘zs’, ‘b’: ‘ls’, ‘c’: ‘we’, ‘d’: nan},
‘Age’: {‘a’: ‘10’, ‘b’: ‘20’, ‘c’: ‘30’, ‘d’: ‘40’},
‘country’: {‘a’: ‘中国’, ‘b’: ‘韩国’, ‘c’: ‘⽇日本’, ‘d’: nan}
}
'''
```
### DataFrame对象常⽤用属性
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

# dataframe常用属性
df_dict = {
'name':['James','Curry','Iversion'],
'age':['18','20','19'],
'national':['us','China','us']
}
df = pd.DataFrame(data=df_dict,index=['0','1','2'])
# print(df)
'''
 name age national
0 James 18 us
1 Curry 20 China
2 Iversion 19 us
'''
# 获取⾏行行数和列列数
# print(df.shape)
'''
(3,3)
'''

# # 获取⾏行行索引
# print(df.index.tolist())
'''
[‘0’, ‘1’, ‘2’]
'''
# # 获取列列索引
# print(df.columns.tolist())
'''
[‘name’, ‘age’, ‘national’]
'''
# 获取数据的类型
# print(df.dtypes)
'''
name object
age object
national object
dtype: object
'''
# 获取数据的维度
# print(df.ndim)
'''
2
'''

# values属性也会以二维ndarray的形式返回DataFrame的数据
print(df.values)
'''
[['James' '18' 'us']
 ['Curry' '20' 'China']
 ['Iversion' '19' 'us']]
 '''
# 展示df的概览

print(df.info())
'''
<class 'pandas.core.frame.DataFrame’>
Index: 3 entries, 0 to 2
Data columns (total 3 columns):
name 3 non-null object
age 3 non-null object
national 3 non-null object
dtypes: object(3)
memory usage: 96.0+ bytes
None
'''
# 显示头⼏几⾏行行,默认显示5⾏行行

# print(df.head(2))
'''
name age national
0 James 18 us
1 Curry 20 China
'''
# 显示后⼏行

# print(df.tail(1))
'''
       name age national
2  Iversion  19       us
'''
# 获取DataFrame的列
# print(df['name'])
'''
0       James
1       Curry
2    Iversion
Name: name, dtype: object
'''
#因为我们只获取⼀一列列，所以返回的就是⼀一个 Series
# print(type(df['name']))
'''
<class 'pandas.core.series.Series'>
'''
# 如果获取多个列列，那返回的就是⼀一个 DataFrame 类型：
# print(df[['name','age']])
'''
       name age
0     James  18
1     Curry  20
2  Iversion  19
'''
# print(type(df[['name','age']]))
'''
<class 'pandas.core.frame.DataFrame'>
'''
# 获取⼀一⾏行行
# print(df[0:1])
'''
    name age national
0  James  18       us
'''
# 取多行
# print(df[1:3])
'''
       name age national
1     Curry  20    China
2  Iversion  19       us
'''
# 取多行里⾯的某一列（不能进行多行多列的选择）
# print(df[1:3][['name','age']])
'''
       name age
1     Curry  20
2  Iversion  19
'''
# 注意： df[]只能进⾏行选择，或列选择，不能同时多行多列选择。
'''
df.loc 通过标签索引行数据
df.iloc 通过位置获取行数据
'''
# 获取某⼀行某⼀列的数据
# print(df.loc['0','name'])
'''
James
'''
# ⼀一⾏所有列
# print(df.loc['0',:])
'''
name        James
age            18
national       us
Name: 0, dtype: object
'''
# 某⼀行多列的数据
# print(df.loc['0',['name','age']])
'''
name    James
age        18
Name: 0, dtype: object
'''
# 选择间隔的多⾏行行多列列
# print(df.loc[['0','2'],['name','national']])
'''
       name national
0     James       us
2  Iversion       us
'''
# 选择连续的多⾏行行和间隔的多列列
# print(df.loc['0':'2',['name','national']])
'''
       name national
0     James       us
1     Curry    China
2  Iversion       us
'''

# 取一行
print(df.iloc[1])
'''
name        Curry
age            20
national    China
Name: 1, dtype: object
'''
# 取连续多行
print(df.iloc[0:2])
'''
    name age national
0  James  18       us
1  Curry  20    China
'''
# 取间断的多行
print(df.iloc[[0,2],:])
'''
       name age national
0     James  18       us
2  Iversion  19       us
'''

# 取某一列1
print(df.iloc[:,1])
'''
0    18
1    20
2    19
Name: age, dtype: object
'''
# 某一个值
print(df.iloc[1,0])
'''
Curry
'''
# 修改值
df.iloc[0,0]='panda'
print(df)
'''
       name age national
0     panda  18       us
1     Curry  20    China
2  Iversion  19       us
'''
# dataframe中的排序方法
df = df.sort_values(by='age',ascending=False)
# ascending=False 降序排列，默认是升序
print(df)
'''
       name age national
1     Curry  20    China
2  Iversion  19       us
0     panda  18       us
'''

```

### dataframex修改index、columns

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'
df1 = pd.DataFrame(np.arange(9).reshape(3, 3), index = ['bj', 'sh', 'gz'],columns=['a', 'b', 'c'])
# print(df1)
'''
    a  b  c
bj  0  1  2
sh  3  4  5
gz  6  7  8
'''
# 修改 df1 的 index
# print(df1.index) # 可以打印出print的值,同时也可以为其赋值
'''
Index([‘bj’, ‘sh’, ‘gz’], dtype=‘object’)
'''
df1.index = ['beijing', 'shanghai', 'guangzhou']
# print(df1)
'''
a b c
beijing 0 1 2
shanghai 3 4 5
guangzhou 6 7 8
'''
# 自自定义map函数(x是原有的行行行列列值)
def test_map(x):
    return x+'_ABC'
# inplace:布尔值,默认为False。指定是否返回新的DataFrame。如果为True,则在原df上修改,返回值为None。
# print(df1.rename(index=test_map, columns=test_map, inplace=True))
'''
None
'''
# print(df1.rename(index=test_map, columns=test_map, inplace=False))
'''
        a_ABC  b_ABC  c_ABC
bj_ABC      0      1      2
sh_ABC      3      4      5
gz_ABC      6      7      8
'''
# 同时,rename 还可以传入入字典,为某个 index 单独修改名称
df3 = df1.rename(index={'bj':'beijing'}, columns = {'a':'aa'})
# print(df3)
'''
         aa  b  c
beijing   0  1  2
sh        3  4  5
gz        6  7  8
'''
# 列列转化为索引
df1=pd.DataFrame({'X':range(5),'Y':range(5),'S':list("abcde"),'Z':[1,1,2,2,2]})
# print(df1)
'''
   X  Y  S  Z
0  0  0  a  1
1  1  1  b  1
2  2  2  c  2
3  3  3  d  2
4  4  4  e  2
'''
# 指定一列为列索列引 (drop=False 指定同时保留作为索引的列)
result = df1.set_index('S',drop=False)
result.index.name=None
# print(result)
'''
   X  Y  S  Z
a  0  0  a  1
b  1  1  b  1
c  2  2  c  2
d  3  3  d  2
e  4  4  e  2
'''
# 行转为列索引
result = df1.set_axis(df1.iloc[0],axis=1,inplace=False)
result.columns.name=None
# print(result)
'''
   0  0  a  1
0  0  0  a  1
1  1  1  b  1
2  2  2  c  2
3  3  3  d  2
4  4  4  e  2
'''
```
### 添加数据
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

# 增加数据
df1 = pd.DataFrame([['Snow','M',22],['Tyrion','M',32],['Sansa','F',18],
['Arya','F',14]],columns=['name','gender','age'])
# 在数据框最后加上score一一列列
# 增加列列的元素个数要跟原数据列列的个数一一样
# print(df1)
'''
     name gender  age
0    Snow      M   22
1  Tyrion      M   32
2   Sansa      F   18
3    Arya      F   14
'''
df1['score']=[80,98,67,90]
# print(df1)
'''
     name gender  age  score
0    Snow      M   22     80
1  Tyrion      M   32     98
2   Sansa      F   18     67
3    Arya      F   14     90
'''
# 在数据框删除score一列
df1.drop(['score'],axis=1,inplace=True)
print(df1)
'''
     name gender  age
0    Snow      M   22
1  Tyrion      M   32
2   Sansa      F   18
3    Arya      F   14
'''
# 在具体某个位置插入一列可以用insert的方法
# 语法格式:列列表.insert(index, obj)
# index --->对象 obj 需要插入入的索引位置。
# obj ---> 要插入入列列表中的对象(列列名)
col_name=df1.columns.tolist()
# 将数据框的列列名全部提取出来存放在列表里
col_name.insert(2,'city')
# 在列索引为2的位置插入一列,列名为:city,刚插入时不会有值,整列都是NaN
df1=df1.reindex(columns=col_name)
# DataFrame.reindex() 对原行/列索引重新构建索引值
# print(df1)
df1['city']=['北京','山西','湖北','澳⻔']
# 给city列赋值
# print(df1)
'''
    name gender  city  age
0   Snow      M   NaN   22
1    111    222   NaN  333
2  Sansa      F   NaN   18
3   Arya      F   NaN   14
'''
df1.drop(['city'],axis=1,inplace=True)
# df中的insert,插入一列
'''
df.insert(iloc,column,value)
iloc:要插入的位置
colunm:列名
value:值
'''
# df1.insert(2,'score',[80,98,67,90])
print(df1)
# 插入一行
row=['111','222','333']
df1.iloc[1]=row
print(df1)
'''
    name gender  age
0   Snow      M   22
1    111    222  333
2  Sansa      F   18
3   Arya      F   14
'''
# 增加数据
df1 = pd.DataFrame([['Snow','M',22],['Tyrion','M',32],['Sansa','F',18],
['Arya','F',14]],columns=['name','gender','age'])
# print(df1)
'''
     name gender  age
0    Snow      M   22
1  Tyrion      M   32
2   Sansa      F   18
3    Arya      F   14
'''
# 先创建一一个DataFrame,用用来增加进数据框的最后一一行行行
new=pd.DataFrame({'name':'lisa',
'gender':'F',
'age':19
},index=[0])
print(new)
'''
   name gender  age
0  lisa      F   19
'''
print("-------在原数据框df1最后一行新增一行,用append方法------------")
df1=df1.append(new,ignore_index=True)
# ignore_index=False,表示不按原来的索引,从0开始自动递增
print(df1)
'''
     name gender  age
0    Snow      M   22
1  Tyrion      M   32
2   Sansa      F   18
3    Arya      F   14
4    lisa      F   19
'''
# 合并

'''
objs:合并对象
axis:合并方式,默认0表示按列合并,1表示按行合并
ignore_index:是否忽略略索引
'''

'''
第一个DataFrame数据（df1）为基准将数据进行合并
'''

df1 = pd.DataFrame(np.arange(6).reshape(3,2),columns=['four','five'])
# print(df1)
'''
   four  five
0     0     1
1     2     3
2     4     5
'''
df2 = pd.DataFrame(np.arange(6).reshape(2,3),columns=['one','two','three'])
# print(df2)
'''
   one  two  three
0    0    1      2
1    3    4      5
'''
# # 按行合并
result = pd.concat([df1,df2],join='outer',axis=1)
# print(result)
'''
   four  five  one  two  three
0     0     1  0.0  1.0    2.0
1     2     3  3.0  4.0    5.0
2     4     5  NaN  NaN    NaN
'''
# # 按列合并
result = pd.concat([df1,df2],join='outer',axis=0,ignore_index=True)
# print(result)
'''
   five  four  one  three  two
0   1.0   0.0  NaN    NaN  NaN
1   3.0   2.0  NaN    NaN  NaN
2   5.0   4.0  NaN    NaN  NaN
3   NaN   NaN  0.0    2.0  1.0
4   NaN   NaN  3.0    5.0  4.0
'''
# DataFrame的删除
'''
lables:要删除数据的标签
axis:0表示删除行,1表示删除列列,默认0
inplace:是否在当前df中执行此操作
'''
df2 = pd.DataFrame(np.arange(9).reshape(3,3),columns=['one','two','three'])
# print(df2)
'''
   one  two  three
0    0    1      2
1    3    4      5
2    6    7      8
'''
df3=df2.drop(['one'],axis=1, inplace=True)

print(df2)
'''
   two  three
0    1      2
1    4      5
2    7      8
'''
print(df3)
'''
None
'''
df3=df2.drop([0,1],axis=0, inplace=False)
print(df2)
'''
   two  three
0    1      2
1    4      5
2    7      8
'''
print(df3)
'''
   two  three
2    7      8
'''
```
### 数据处理
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

from numpy import nan as NaN
# 通过**dropna()**滤除缺失数据:
se=pd.Series([4,NaN,8,NaN,5])
# print(se)
'''
0    4.0
1    NaN
2    8.0
3    NaN
4    5.0
dtype: float64
'''
# print(se.dropna())
'''
0    4.0
2    8.0
4    5.0
dtype: float64
'''
# print(se.notnull())
'''
0     True
1    False
2     True
3    False
4     True
dtype: bool
'''
# print(se.isnull())
'''
0    False
1     True
2    False
3     True
4    False
dtype: bool
'''
# # 通过布尔序列也能滤除:
# print(se[se.notnull()])
'''
0    4.0
2    8.0
4    5.0
dtype: float64
'''
# 2.2 处理DataFrame对象
df1=pd.DataFrame([[1,2,3],[NaN,NaN,2],[NaN,NaN,NaN],[8,8,NaN]])
# print(df1)
'''
     0    1    2
0  1.0  2.0  3.0
1  NaN  NaN  2.0
2  NaN  NaN  NaN
3  8.0  8.0  NaN
'''

# 默认滤除所有包含NaN:
# print(df1.dropna())
'''
     0    1    2
0  1.0  2.0  3.0
'''
# 传入how=‘all’滤除全为NaN的行:
# print(df1.dropna(how='all')) # 默认情况下是how='any',只要有nan就删除
'''
     0    1    2
0  1.0  2.0  3.0
1  NaN  NaN  2.0
3  8.0  8.0  NaN
'''
# 传入入axis=1滤除列:
# print(df1.dropna(axis=1,how="all"))
'''
     0    1    2
0  1.0  2.0  3.0
1  NaN  NaN  2.0
2  NaN  NaN  NaN
3  8.0  8.0  NaN
'''
#df1.dropna()默认删除包含nan的行，传入thresh=n保留至少有n个非NaN数据的行:
# print(df1.dropna(thresh=1))
'''
     0    1    2
0  1.0  2.0  3.0
1  NaN  NaN  2.0
3  8.0  8.0  NaN
'''
# 2.3 填充缺失数据
df1=pd.DataFrame([[1,2,3],[NaN,NaN,2],[NaN,NaN,NaN],[8,8,NaN]])
# print(df1)
'''
     0    1    2
0  1.0  2.0  3.0
1  NaN  NaN  2.0
2  NaN  NaN  NaN
3  8.0  8.0  NaN
'''
# 用用常数填充fillna
# print(df1.fillna(0))
'''
     0    1    2
0  1.0  2.0  3.0
1  0.0  0.0  2.0
2  0.0  0.0  0.0
3  8.0  8.0  0.0
'''

#传入inplace=True直接修改原对象:
# df1.fillna(0,inplace=True)
# print(df1)
'''
     0    1    2
0  1.0  2.0  3.0
1  0.0  0.0  2.0
2  0.0  0.0  0.0
3  8.0  8.0  0.0
'''
# 通过字典填充不同的常数  ???
# print(df1.fillna({0:10,1:20,2:30}))
'''
      0     1     2
0   1.0   2.0   3.0
1  10.0  20.0   2.0
2  10.0  20.0  30.0
3   8.0   8.0  30.0
'''
# 填充平均值
print(df1.fillna(df1.mean()))
'''
     0    1    2
0  1.0  2.0  3.0
1  4.5  5.0  2.0
2  4.5  5.0  2.5
3  8.0  8.0  2.5
'''
# 如果只填充一列
print(df1.iloc[:,1].fillna(5,inplace = True))
'''
None
'''
print(df1)
'''
     0    1    2
0  1.0  2.0  3.0
1  NaN  5.0  2.0
2  NaN  5.0  NaN
3  8.0  8.0  NaN
'''
# 传入method=” “改变插值方式:
df2=pd.DataFrame(np.random.randint(0,10,(5,5)))
df2.iloc[1:4,3]=NaN
df2.iloc[2:4,4]=NaN
# print(df2)
'''
   0  1  2    3    4
0  0  8  0  6.0  8.0
1  8  1  9  NaN  9.0
2  1  9  6  NaN  NaN
3  3  0  0  NaN  NaN
4  2  7  8  4.0  8.0
'''

#用前面的值来填充ffill,用后面的值来填充bfill
# print(df2.fillna(method='ffill'))
'''
   0  1  2    3    4
0  0  8  0  6.0  8.0
1  8  1  9  6.0  9.0
2  1  9  6  6.0  9.0
3  3  0  0  6.0  9.0
4  2  7  8  4.0  8.0
'''
# 传入limit=” “限制填充行数:
# print(df2.fillna(method='bfill',limit=1))
'''
   0  1  2    3    4
0  0  8  0  6.0  8.0
1  8  1  9  NaN  9.0
2  1  9  6  NaN  NaN
3  3  0  0  4.0  8.0
4  2  7  8  4.0  8.0
'''
# 传入axis=” “修改填充方向:
# print(df2.fillna(method="ffill",limit=1,axis=1))
'''
     0    1    2    3    4
0  0.0  8.0  0.0  6.0  8.0
1  8.0  1.0  9.0  9.0  9.0
2  1.0  9.0  6.0  6.0  NaN
3  3.0  0.0  0.0  0.0  NaN
4  2.0  7.0  8.0  4.0  8.0
'''
# 2.4 移除重复数据
'''
DataFrame中经常会出现重复行,利用duplicated()函数返回每一行判断是否重复的结果(重复则为
True)
'''
df1=pd.DataFrame({'A':[1,1,1,2,2,3,1],'B':list("aabbbca")})
print(df1)
'''
   A  B
0  1  a
1  1  a
2  1  b
3  2  b
4  2  b
5  3  c
6  1  a
'''
# 判断每一行是否重复(结果是bool值,TRUE代表重复的)
# Return boolean Series denoting duplicate rows, optionally only considering certain columns
# print(df1.duplicated())
'''
0    False
1     True
2    False
3    False
4     True
5    False
6     True
dtype: bool
'''
# 去除全部的重复行
# print(df1.drop_duplicates())
'''
   A  B
0  1  a
2  1  b
3  2  b
5  3  c
'''
# # 指定列去除重复行
# print(df1.drop_duplicates(['A']))
'''
   A  B
0  1  a
3  2  b
5  3  c
'''
# 保留重复行中的最后一行
# print(df1.drop_duplicates(['A'],keep='last'))
'''
   A  B
4  2  b
5  3  c
6  1  a
'''
# 去除重复的同时改变DataFrame对象
# df1.drop_duplicates(['A','B'],inplace=True)
# print(df1)
'''
   A  B
0  1  a
2  1  b
3  2  b
5  3  c
'''
```
### 数据合并
#### join
Join columns with other DataFrame either on index or on a key
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

# 使用join合并,着重关注的是行的合并
import pandas as pd
df3=pd.DataFrame({'Red':[1,3,5],'Green':[5,0,3]},index=list('abc'))
df4=pd.DataFrame({'Blue':[1,9,8],'Yellow':[6,6,7]},index=list('cde'))
print(df3)
'''
   Red  Green
a    1      5
b    3      0
c    5      3
'''
print(df4)
'''
   Blue  Yellow
c     1       6
d     9       6
e     8       7
'''
# 简单合并(默认是left左连接,以左侧df3为基础)
df3.join(df4,how='left')
'''

Red	Green	Blue	Yellow
a	1	5	NaN	NaN
b	3	0	NaN	NaN
c	5	3	1.0	6.0
'''

# 右链接
print(df3.join(df4,how='right'))
'''
   Red  Green  Blue  Yellow
c  5.0    3.0     1       6
d  NaN    NaN     9       6
e  NaN    NaN     8       7
'''
# 外链接
df3.join(df4,how='outer')
'''
   Red  Green  Blue  Yellow
a  1.0    5.0   NaN     NaN
b  3.0    0.0   NaN     NaN
c  5.0    3.0   1.0     6.0
d  NaN    NaN   9.0     6.0
e  NaN    NaN   8.0     7.0
'''
# 合并多个DataFrame对象
df5=pd.DataFrame({'Brown':[3,4,5],'White':[1,1,2]},index=list('aed'))
# df3.join([df4,df5])
'''
   Red  Green  Blue  Yellow  Brown  White
a    1      5   NaN     NaN    3.0    1.0
b    3      0   NaN     NaN    NaN    NaN
c    5      3   1.0     6.0    NaN    NaN
'''
```
#### merge
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'
# 使用用merge,着重关注的是列列的合并
df1=pd.DataFrame({'名字':list('ABCDE'),'性别':['男','女','男','男','女'],'职称':
['副教授','讲师','助教','教授','助教']},index=range(1001,1006))
df1.columns.name='学院老师'
df1.index.name='编号'
print(df1)
'''
学院老师 名字 性别   职称
编号             
1001     A  男   副教授
1002     B  女   讲师
1003     C  男   助教
1004     D  男   教授
1005     E  女   助教
'''
df2=pd.DataFrame({'名字':list('ABDAX'),'课程':['C++','计算机导论','汇编','数据结构','⻢克思原理'],'职称':['副教授','讲师','教授','副教授','讲师']},index=
[1001,1002,1004,1001,3001])
df2.columns.name='课程'
df2.index.name='编号'
print(df2)
'''
课程   名字     课程       职称
编号                 
1001    A     C++        副教授
1002    B     计算机导论   讲师
1004    D     汇编        教授
1001    A     数据结构     副教授
3001    X     ⻢克思原理   讲师
'''
# 默认下是根据左右对象中出现同名的列作为连接的键,且连接方式是how=’inner’
#df1和df2根据列名（名字）取交集后的数据（AABD）
# print(pd.merge(df1,df2))# 返回匹配的
'''
  名字 性别   职称     课程
0  A  男  副教授    C++
1  A  男  副教授   数据结构
2  B  女   讲师  计算机导论
3  D  男   教授     汇编
'''
# 指定列名合并
pd.merge(df1,df2,on='名字',suffixes=['_1','_2'])# 返回匹配的
'''

      名字	性别	 职称_1   课程	职称_2
0	A	男	副教授	  C++	     副教授
1	A	男	副教授	  数据结构	副教授
2	B	女	讲师	  计算机导论	讲师
3	D	男	教授	  汇编	      教授
'''
# 连接方方式,根据左侧为准
pd.merge(df1,df2,how='left')
'''

       名字	性别	职称	课程
0	A	男	副教授	C++
1	A	男	副教授	数据结构
2	B	女	讲师	计算机导论
3	C	男	助教	NaN
4	D	男	教授	汇编
5	E	女	助教	NaN
'''
# 根据右侧为准
pd.merge(df1,df2,how='right')
'''
名字	性别	职称	课程
0	A	男	副教授	C++
1	A	男	副教授	数据结构
2	B	女	讲师	计算机导论
3	D	男	教授	汇编
4	X	NaN	讲师	⻢克思原理
'''
# 所有
# pd.merge(df1,df2,how='outer')
'''

名字	性别	职称	课程
0	A	男	副教授	C++
1	A	男	副教授	数据结构
2	B	女	讲师	计算机导论
3	C	男	助教	NaN
4	D	男	教授	汇编
5	E	女	助教	NaN
6	X	NaN	讲师	⻢克思原理
'''
# 根据多个键进行连接
pd.merge(df1,df2,on=['职称','名字'])
'''

名字	性别	职称	课程
0	A	男	副教授	C++
1	A	男	副教授	数据结构
2	B	女	讲师	计算机导论
3	D	男	教授	汇编
'''
```
### concat 拓展
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

# 轴向连接-Concat
# 1. Series对象的连接
s1=pd.Series([1,2],index=list('ab'))
s2=pd.Series([3,4,5],index=list('bde'))
# print(s1)
'''
a    1
b    2
dtype: int64
'''
# print(s2)
'''
b    3
d    4
e    5
dtype: int64
'''
pd.concat([s1,s2])
'''
a    1
b    2
b    3
d    4
e    5
dtype: int64
'''
#横向连接
pd.concat([s1,s2],axis=1)
'''
   0  	1
a	1.0	NaN
b	2.0	3.0
d	NaN	4.0
e	NaN	5.0
'''
# 用用内连接求交集(连接方方式,共有’inner’,’left’,right’,’outer’)
pd.concat([s1,s2],axis=1,join='inner')
'''
	0	1
b	2	3
'''
# 指定部分索引进行连接
pd.concat([s1,s2],axis=1,join_axes=[list('abc')])
'''
   0	   1
a	1.0	NaN
b	2.0	3.0
c	NaN	NaN
'''
pd.concat([s1,s2],axis=1,join_axes=[list('abde')])
'''
   0	   1
a	1.0	NaN
b	2.0	3.0
d	NaN	4.0
e	NaN	5.0
'''
# 创建层次化索引
pd.concat([s1,s2],keys=['A','B'])
'''
A  a    1
   b    2
B  b    3
   d    4
   e    5
dtype: int64
'''
#当纵向连接时keys为列列名
pd.concat([s1,s2],keys=['A','D'],axis=1)
'''
	A	   D
a	1.0	NaN
b	2.0	3.0
d	NaN	4.0
e	NaN	5.0
'''
# 2. DataFrame对象的连接
df3=pd.DataFrame({'Red':[1,3,5],'Green':[5,0,3]},index=list('abd'))
df4=pd.DataFrame({'Blue':[1,9],'Yellow':[6,6]},index=list('ce'))
print(df3)
'''
   Red  Green
a    1      5
b    3      0
d    5      3
'''
print(df4)
'''
   Blue  Yellow
c     1       6
e     9       6
'''
pd.concat([df3,df4])
'''
   Blue	Green	Red	Yellow
a	NaN	5.0	1.0	NaN
b	NaN	0.0	3.0	NaN
d	NaN	3.0	5.0	NaN
c	1.0	NaN	NaN	6.0
e	9.0	NaN	NaN	6.0
'''
pd.concat([df3,df4],axis=1,keys=['A','B'])
'''
	A	         B
   Red	Green	Blue	Yellow
a	1.0	5.0	NaN	NaN
b	3.0	0.0	NaN	NaN
c	NaN	NaN	1.0	6.0
d	5.0	3.0	NaN	NaN
e	NaN	NaN	9.0	6.0
'''
# 用用字典的方方式连接同样可以创建层次化列列索引
pd.concat({'A':df3,'B':df4},axis=1)
'''
	A	         B
   Red	Green	Blue	Yellow
a	1.0	5.0	NaN	NaN
b	3.0	0.0	NaN	NaN
c	NaN	NaN	1.0	6.0
d	5.0	3.0	NaN	NaN
e	NaN	NaN	9.0	6.0
'''

```
### 多层索引(拓拓展)
#### 创建多层索引
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
# Series也可以创建多层索引
s = Series(np.random.randint(0,150,size=6),index=list('abcdef'))
print(s)
'''
a     15
b     29
c     57
d    110
e     22
f    120
dtype: int64
'''
s = Series(np.random.randint(0,150,size=6),index=[['a','a','b','b','c','c'],['期中','期末','期中','期末','期中','期末']])
print(s)
'''
a  期中    109
   期末     74
b  期中     59
   期末     68
c  期中     68
   期末    117
dtype: int64
'''
# DataFrame创建多层索引
df1 = DataFrame(np.random.randint(0,150,size=(6,4)),
columns = ['zs','ls','ww','zl'],
index = [['python','python','math','math','En','En'],['期中','期末','期中','期末','期中','期末']])
print(df1)
'''
            zs   ls   ww   zl
python 期中   47   73   94   83
       期末   61   20   44   18
math   期中   77   27  143   37
       期末  135   86  119  119
En     期中  141  115   15  120
       期末   69   79   13   37
'''
# 2. 特定结构
class1=['python','python','math','math','En','En']
class2=['期中','期末','期中','期末','期中','期末']
m_index2=pd.MultiIndex.from_arrays([class1,class2])
df2=DataFrame(np.random.randint(0,150,(6,4)),index=m_index2)
print(df2)
'''
             0    1    2    3
python 期中   82    2   72   34
       期末  106   88  143   25
math   期中   40    0  111  112
       期末  126    9  147  147
En     期中  104  135   23   66
       期末   55   37  125    0
'''
class1=['期中','期中','期中','期末','期末','期末']
class2=['python','math','En','python','math','En']
m_index2=pd.MultiIndex.from_arrays([class1,class2])
df2=DataFrame(np.random.randint(0,150,(6,4)),index=m_index2)
print(df2)
'''

            0  	1	2	3
期中	python	109	4	44	144
      math	21	61	52	74
      En	136	57	50	8
期末	python	31	130	9	109
      math	94	109	114	68
      En	32	54	98	88
'''
# 3. product构造
class1=['python','math','En']
class2=['期中','期末']
m_index2=pd.MultiIndex.from_product([class1,class2])
df2=DataFrame(np.random.randint(0,150,(6,4)),index=m_index2)
print(df2)
'''
             0    1    2    3
python 期中  103  102    8  116
       期末  134  139  116  115
math   期中    5   31   87   24
       期末   48    0   64   46
En     期中   83   84  117   71
       期末   94   31   75   40
'''

```
#### 多层索引对象的索引
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

#多层索引对象的索引操作
# series
s = Series(np.random.randint(0,150,size=6),index=[['a','a','b','b','c','c'],['期中','期末','期中','期末','期中','期末']])
print(s)
'''
a  期中    136
   期末    105
b  期中     56
   期末     68
c  期中     79
   期末    124
dtype: int64
'''
# 取一个第一级索引
print(s['a'])
'''
期中    136
期末    105
dtype: int64
'''
# 取多个第一级索引
print(s[['a','b']])
'''
a  期中    136
   期末    105
b  期中     56
   期末     68
dtype: int64
'''
# 根据索引获取值
# print(s['a','期末'])
'''
105
'''
# loc方方法取值
print(s.loc['a'])
'''
期中    136
期末    105
dtype: int64
'''
print(s.loc[['a','b']])
'''
a  期中    136
   期末    105
b  期中     56
   期末     68
dtype: int64
'''
print(s.loc['a','期末'])
'''
105
'''
# iloc方方法取值(iloc计算的事最内层索引)
print(s.iloc[1])
'''
105
'''
print(s.iloc[1:4])
'''
a  期末    105
b  期中     56
   期末     68
dtype: int64
'''
# dataframe
class1=['python','math','En']
class2=['期中','期末']
m_index2=pd.MultiIndex.from_product([class1,class2])
df2=DataFrame(np.random.randint(0,150,(6,4)),index=m_index2)
print(df2)
'''
             0    1   2    3
python 期中  111  139  80  146
       期末    9   60  72  122
math   期中   73   81  33   30
       期末  123  130   1   66
En     期中  136   85  59   43
       期末  134   57  63   40
'''
# 获取列列
print(df2[0])
'''
python  期中    111
        期末      9
math    期中     73
        期末    123
En      期中    136
        期末    134
Name: 0, dtype: int64
'''
# 一一级索引
print(df2.loc['python'])
'''
      0    1   2    3
期中  111  139  80  146
期末    9   60  72  122
'''
# 多个一级索引
print(df2.loc[['python','math']])
'''
             0    1   2    3
python 期中  111  139  80  146
       期末    9   60  72  122
math   期中   73   81  33   30
       期末  123  130   1   66
'''
# 取一行
print(df2.loc['python','期末'])
'''
0      9
1     60
2     72
3    122
Name: (python, 期末), dtype: int64
'''
# 取一一值
# print(df2.loc['python','期末'][0])
'''
9
'''
# iloc是只取最内层的索引的
#print(df2.iloc[0])
'''
0    111
1    139
2     80
3    146
Name: (python, 期中), dtype: int64
'''
```
### 时间序列
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'
import pandas as pd
import numpy as np
# 1. 生成一段时间范围
'''
该函数主要用于生成一个固定频率的时间索引,在调用构造方法时,必须指定start、end、periods中的两个参数值,否则报错。
时间序列列频率:
D 日历的每天
B 工作日的每天
H 每小时
T或min 每分钟
S 每秒
L或ms 每毫秒
U 每微秒
M 日历月底日期
工作日的月底日期
BM
MS 日历月初日期
BMS 工作日的月初日期
'''
date = pd.date_range(start='20190501',end='20190530')
# print(date)
'''
DatetimeIndex(['2019-05-01', '2019-05-02', '2019-05-03', '2019-05-04',
               '2019-05-05', '2019-05-06', '2019-05-07', '2019-05-08',
               '2019-05-09', '2019-05-10', '2019-05-11', '2019-05-12',
               '2019-05-13', '2019-05-14', '2019-05-15', '2019-05-16',
               '2019-05-17', '2019-05-18', '2019-05-19', '2019-05-20',
               '2019-05-21', '2019-05-22', '2019-05-23', '2019-05-24',
               '2019-05-25', '2019-05-26', '2019-05-27', '2019-05-28',
               '2019-05-29', '2019-05-30'],
              dtype='datetime64[ns]', freq='D')
'''
# freq:日期偏移量,取值为string, 默认为'D',
freq='1h30min'
freq='10D'
# periods:固定时期,取值为整数或None
date = pd.date_range(start='20190501',periods=10,freq='10D')
# print(date)
'''
DatetimeIndex(['2019-05-01', '2019-05-11', '2019-05-21', '2019-05-31',
               '2019-06-10', '2019-06-20', '2019-06-30', '2019-07-10',
               '2019-07-20', '2019-07-30'],
              dtype='datetime64[ns]', freq='10D')
'''

'''
根据closed参数选择是否包含开始和结束时间closed=None,left包含开始时间,不包含结束时间,
right与之相反。
'''
data_time =pd.date_range(start='2019-01-09',end='2019-01-14',closed='left')
print(data_time)
'''
DatetimeIndex(['2019-01-09', '2019-01-10', '2019-01-11', '2019-01-12',
               '2019-01-13'],
              dtype='datetime64[ns]', freq='D')
'''

# 2. 时间序列在dataFrame中的作用
# 可以将时间作为索引
index = pd.date_range(start='20190101',periods=10)
df = pd.Series(np.random.randint(0,10,size = 10),index=index)
print(df)
'''
2019-01-01    4
2019-01-02    9
2019-01-03    1
2019-01-04    3
2019-01-05    5
2019-01-06    7
2019-01-07    6
2019-01-08    2
2019-01-09    6
2019-01-10    5
Freq: D, dtype: int64
'''

# truncate这个函数将before指定日期之前的值全部过滤出去,after指定日期之前的值全部过滤出去.
after = df.truncate(after='2019-01-8')
print(after)
'''
2019-01-01    4
2019-01-02    9
2019-01-03    1
2019-01-04    3
2019-01-05    5
2019-01-06    7
2019-01-07    6
2019-01-08    2
Freq: D, dtype: int64
'''
long_ts = pd.Series(np.random.randn(10),index=pd.date_range('1/1/2019',periods=10))
# print(long_ts)
'''
2019-01-01   -0.926230
2019-01-02    1.364737
2019-01-03   -1.361901
2019-01-04   -0.475589
2019-01-05   -0.149766
2019-01-06   -0.107419
2019-01-07    2.025332
2019-01-08    0.784505
2019-01-09   -0.672272
2019-01-10   -1.341834
Freq: D, dtype: float64
'''

# 根据年份获取
# result = long_ts['2019']
# print(result)
'''
2019-01-01   -0.926230
2019-01-02    1.364737
2019-01-03   -1.361901
2019-01-04   -0.475589
2019-01-05   -0.149766
2019-01-06   -0.107419
2019-01-07    2.025332
2019-01-08    0.784505
2019-01-09   -0.672272
2019-01-10   -1.341834
Freq: D, dtype: float64
'''


# 年份和日期获取
result = long_ts['2019-01']
# print(result)
'''
2019-01-01   -0.926230
2019-01-02    1.364737
2019-01-03   -1.361901
2019-01-04   -0.475589
2019-01-05   -0.149766
2019-01-06   -0.107419
2019-01-07    2.025332
2019-01-08    0.784505
2019-01-09   -0.672272
2019-01-10   -1.341834
Freq: D, dtype: float64
'''

# 使用切片
result = long_ts['2019-01-01':'2019-01-06']
# print(result)
'''
2019-01-01   -0.926230
2019-01-02    1.364737
2019-01-03   -1.361901
2019-01-04   -0.475589
2019-01-05   -0.149766
2019-01-06   -0.107419
Freq: D, dtype: float64
'''

# 通过between_time()返回位于指定时间段的数据集
index=pd.date_range("2018-03-17","2018-03-18",freq="2H")
print(len(index))
'''
13
'''
ts = pd.Series(np.random.randn(13),index=index)
print(ts.between_time("7:00","17:00"))
'''
2018-03-17 08:00:00    0.810209
2018-03-17 10:00:00    0.910479
2018-03-17 12:00:00   -0.319812
2018-03-17 14:00:00   -0.009239
2018-03-17 16:00:00    1.193648
Freq: 2H, dtype: float64
'''

# 这些操作也都适用于dataframe
index=pd.date_range('1/1/2019',periods=3)
df = pd.DataFrame(np.random.randn(3,4),index=index)
print(df.loc['2019-01'])

'''
                   0         1         2         3
2019-01-01 -0.293386 -1.654920  2.103502  0.007126
2019-01-02 -0.080693 -0.587984 -0.293842  0.524302
2019-01-03  0.627220  0.725538  0.226107  1.421071
'''

# 6. 移位日期
ts = pd.Series(np.random.randn(10),index=pd.date_range('1/1/2019',periods=10))
print(ts)
# 移动数据,索引不变,默认由NaN填充
# periods: 移动的位数 负数是向上移动
# fill_value: 移动后填充数据
# freq: 日期偏移量
ts.shift(periods=2,fill_value=100,freq='D')
# 通过tshift()将索引移动指定的时间:
ts.tshift(2)
# 将时间戳转化成时间根式
pd.to_datetime(1554970740000,unit='ms')
# utc是协调世界时,时区是以UTC的偏移量量的形式表示的,但是注意设置utc=True,是让pandas对象具有时区性质,对于一一列进行转换的,会造成转换错误
# unit='ms' 设置粒度是到毫秒级别的
# 时区名字
# import pytz
# print(pytz.common_timezones)
2019-5-1
pd.to_datetime(1554970740000,unit='ms').tz_localize('UTC').tz_convert('Asia/Sh
anghai')
# 处理一列
df = pd.DataFrame([1554970740000, 1554970800000, 1554970860000],columns =
['time_stamp'])
pd.to_datetime(df['time_stamp'],unit='ms').dt.tz_localize('UTC').dt.tz_convert
('Asia/Shanghai')#先赋予标准时区,再转换到东八区
# 处理中文
pd.to_datetime('2019年年10月月10日日',format='%Y年年%m月月%d日日')
```
### 分组聚合
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

# 分组
import pandas as pd
import numpy as np
df=pd.DataFrame({
'name':['BOSS','Lilei','Lilei','Han','BOSS','BOSS','Han','BOSS'],
'Year':[2016,2016,2016,2016,2017,2017,2017,2017],
'Salary':[999999,20000,25000,3000,9999999,999999,3500,999999],
'Bonus':[100000,20000,20000,5000,200000,300000,3000,400000]
})
# print(df)
# 根据name这一列进行分组
# group_by_name=df.groupby('name')
# print(type(group_by_name))
# 查看分组
# print(group_by_name.groups)
# 分组后的数量
# print(group_by_name.count())
# 产看分组的情况
# for name,group in group_by_name:
# print(name)# 组的名字
# print(group)# 组具体内容
# 可以选择分组
# print(group_by_name.get_group('BOSS'))
# 按照某一列进行分组, 将name这一列作为分组的键,对year进行分组
# group_by_name=df['Year'].groupby(df['name'])
# print(group_by_name.count())
# 按照多列进行分组
# group_by_name_year=df.groupby(['name','Year'])
# for name,group in group_by_name_year:
# print(name)# 组的名字
# print(group)# 组具体内容
# 可以选择分组
# print(group_by_name_year.get_group(('BOSS',2016)))
# 将某列数据按数据值分成不同范围段进行分组(groupby)运算

df = pd.DataFrame({'Age': np.random.randint(20, 70, 100),
'Sex': np.random.choice(['M', 'F'], 100),
})
age_groups = pd.cut(df['Age'], bins=[19,40,65,100])
# print(age_groups)
print(df.groupby(age_groups).count())
# 按‘Age’分组范围和性别(sex)进行制作交叉表
pd.crosstab(age_groups, df['Sex'])
## 聚合
'''聚合函数
mean 计算分组平均值
count 分组中非NA值的数量
sum 非NA值的和
median 非NA值的算术中位数
std 标准差
var 方差
min 非NA值的最小值
max 非NA值的最大值
prod 非NA值的积
first 第一个非NA值
last 最后一个非NA值
mad
mode
平均绝对偏差
模
绝对值
abs
sem 平均值的标准误差
skew 样品偏斜度(三阶矩)
kurt 样品峰度(四阶矩)
样本分位数(百分位上的值)
quantile
cumsum
累积总和
cumprod 累积乘积
cummax 累积最大值
cummin 累积最小值
'''
df1=pd.DataFrame({'Data1':np.random.randint(0,10,5),
'Data2':np.random.randint(10,20,5),
'key1':list('aabba'),
'key2':list('xyyxy')})
print(df1)
# 按key1分组,进行聚合计算
# 注意:当分组后进行数值计算时,不是数值类的列(即麻烦列)会被清除
print(df1.groupby('key1').sum())
# 只算data1
# print(df1['Data1'].groupby(df1['key1']).sum())
# print(df1.groupby('key1')['Data1'].sum())
# 使用agg()函数做聚合运算

# print(df1.groupby('key1').agg('sum'))
# 可以同时做多个聚合运算
# print(df1.groupby('key1').agg(['sum','mean','std']))
# 可自自定义函数,传入agg方法中 grouped.agg(func)
def peak_range(df):
"""
返回数值范围
"""
return df.max() - df.min()
# print(df1.groupby('key1').agg(peak_range))
# 同时应用多个聚合函数
# print(df1.groupby('key1').agg(['mean', 'std', 'count', peak_range])) # 默认列名为函数名
# print(df1.groupby('key1').agg(['mean', 'std', 'count', ('range',peak_range)])) # 通过元组提供新的列名
# 给每列作用不同的聚合函数
dict_mapping = {
'Data1':['mean','max'],
'Data2':'sum'
}
df1.groupby('key1').agg(dict_mapping)
```
#### 拓展apply()函数
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'
# 拓拓展apply函数
# apply函数是pandas里面所有函数中自由度最高的函数
df1=pd.DataFrame({'sex':list('FFMFMMF'),'smoker':list('YNYYNYY'),'age':
[21,30,17,37,40,18,26],'weight':[120,100,132,140,94,89,123]})
print(df1)
def bin_age(age):
if age >=18:
return 1
else:
return 0
# 抽烟的年龄大于等18的
# print(df1['age'].apply(bin_age))
# df1['age'] = df1['age'].apply(bin_age)
# print(df1)
# 取出抽烟和不抽烟的体重前二
def top(smoker,col,n=5):
       return smoker.sort_values(by=col)[-n:]
df1.groupby('smoker').apply(top,col='weight',n=2)

```

### 分组案例
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

# 读取数据
data = pd.read_csv('movie_data.csv')
# print('数据的形状:', data.shape)
'''
数据的形状: (5043, 28)
'''

print(data.head())
'''
   color      director_name  num_critic_for_reviews  duration  \
0  Color      James Cameron                   723.0     178.0   
1  Color     Gore Verbinski                   302.0     169.0   
2  Color         Sam Mendes                   602.0     148.0   
3  Color  Christopher Nolan                   813.0     164.0   
4    NaN        Doug Walker                     NaN       NaN   

   director_facebook_likes  actor_3_facebook_likes      actor_2_name  \
0                      0.0                   855.0  Joel David Moore   
1                    563.0                  1000.0     Orlando Bloom   
2                      0.0                   161.0      Rory Kinnear   
3                  22000.0                 23000.0    Christian Bale   
4                    131.0                     NaN        Rob Walker   

   actor_1_facebook_likes        gross                           genres  \
0                  1000.0  760505847.0  Action|Adventure|Fantasy|Sci-Fi   
1                 40000.0  309404152.0         Action|Adventure|Fantasy   
2                 11000.0  200074175.0        Action|Adventure|Thriller   
3                 27000.0  448130642.0                  Action|Thriller   
4                   131.0          NaN                      Documentary   

          ...          num_user_for_reviews language  country  content_rating  \
0         ...                        3054.0  English      USA           PG-13   
1         ...                        1238.0  English      USA           PG-13   
2         ...                         994.0  English       UK           PG-13   
3         ...                        2701.0  English      USA           PG-13   
4         ...                           NaN      NaN      NaN             NaN   

        budget  title_year actor_2_facebook_likes imdb_score  aspect_ratio  \
0  237000000.0      2009.0                  936.0        7.9          1.78   
1  300000000.0      2007.0                 5000.0        7.1          2.35   
2  245000000.0      2015.0                  393.0        6.8          2.35   
3  250000000.0      2012.0                23000.0        8.5          2.35   
4          NaN         NaN                   12.0        7.1           NaN   

  movie_facebook_likes  
0                33000  
1                    0  
2                85000  
3               164000  
4                    0  

[5 rows x 28 columns]
'''

# 2、处理理缺失值
data = data.dropna(how='any')
# print(data.head())
'''
   color      director_name  num_critic_for_reviews  duration  \
0  Color      James Cameron                   723.0     178.0   
1  Color     Gore Verbinski                   302.0     169.0   
2  Color         Sam Mendes                   602.0     148.0   
3  Color  Christopher Nolan                   813.0     164.0   
5  Color     Andrew Stanton                   462.0     132.0   

   director_facebook_likes  actor_3_facebook_likes      actor_2_name  \
0                      0.0                   855.0  Joel David Moore   
1                    563.0                  1000.0     Orlando Bloom   
2                      0.0                   161.0      Rory Kinnear   
3                  22000.0                 23000.0    Christian Bale   
5                    475.0                   530.0   Samantha Morton   

   actor_1_facebook_likes        gross                           genres  \
0                  1000.0  760505847.0  Action|Adventure|Fantasy|Sci-Fi   
1                 40000.0  309404152.0         Action|Adventure|Fantasy   
2                 11000.0  200074175.0        Action|Adventure|Thriller   
3                 27000.0  448130642.0                  Action|Thriller   
5                   640.0   73058679.0          Action|Adventure|Sci-Fi   

          ...          num_user_for_reviews language  country  content_rating  \
0         ...                        3054.0  English      USA           PG-13   
1         ...                        1238.0  English      USA           PG-13   
2         ...                         994.0  English       UK           PG-13   
3         ...                        2701.0  English      USA           PG-13   
5         ...                         738.0  English      USA           PG-13   

        budget  title_year actor_2_facebook_likes imdb_score  aspect_ratio  \
0  237000000.0      2009.0                  936.0        7.9          1.78   
1  300000000.0      2007.0                 5000.0        7.1          2.35   
2  245000000.0      2015.0                  393.0        6.8          2.35   
3  250000000.0      2012.0                23000.0        8.5          2.35   
5  263700000.0      2012.0                  632.0        6.6          2.35   

  movie_facebook_likes  
0                33000  
1                    0  
2                85000  
3               164000  
5                24000  

[5 rows x 28 columns]
'''

# 查看票房收入统计
# 导演vs票房总收入
group_director = data.groupby(by='director_name')['gross'].sum()
# ascending升降序排列,True升序
result = group_director.sort_values()
print(type(result))
'''
<class 'pandas.core.series.Series'>
'''
print(result.head())
'''
director_name
Ekachai Uekrongtham     162.0
Frank Whaley            703.0
Ricki Stern            1111.0
Alex Craig Mann        1332.0
Paul Bunnell           2436.0
Name: gross, dtype: float64
'''
# 电影产量年份趋势
from matplotlib import pyplot as plt
import random
from matplotlib import font_manager
movie_years = data.groupby('title_year')['movie_title']
print(movie_years.count().index.tolist()[:5])
'''
[1927.0, 1929.0, 1933.0, 1935.0, 1936.0]
'''
print(movie_years.count().values[:5])
'''
[1 1 1 1 1]
'''
x = movie_years.count().index.tolist()
y = movie_years.count().values
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y)
plt.show()
```
