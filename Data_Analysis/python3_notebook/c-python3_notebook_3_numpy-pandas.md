# NumPy
[NumPy中文官网](https://www.numpy.org.cn/)
NumPy（Numerical Python）是一个开源的Python科学计算库，用于快速处理任意维度的数组。
NumPy支持常见的数组和矩阵操作。对于同样的数值计算任务，使用Numpy比直接使用Python要简洁
的多。
NumPy使用ndarray对象来处理多维数组，该对象是一个快速而灵活的大数据容器。
## NumPy的优势
- 对于同样的数值计算任务，使用NumPy要比直接编写Python代码便捷得多；
- NumPy中的数组的存储效率和输入输出性能均远远优于Python中等价的基本数据结构，且其能够
提升的性能是与数组中的元素成比例的；
- NumPy的大部分代码都是用C语言写的，其底层算法在设计时就有着优异的性能，这使得NumPy
比纯Python代码高效得多
### ndarray与Python原生list运算效率对比
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

import random
import time
import numpy as np
a = []
for i in range(100000000):
a.append(random.random())
t1 = time.time()
sum1=sum(a)
t2=time.time()

b=np.array(a)
t4=time.time()
sum3=np.sum(b)
t5=time.time()
print(t2-t1, t5-t4)

```
## NumPy 的Ndarray 对象
NumPy 最重要的一个特点是其 <font color="orange" >N 维</font>数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。ndarray 对象是用于<font color="orange" >存放同类型元素</font>的多维数组。
### 创建一维数组
