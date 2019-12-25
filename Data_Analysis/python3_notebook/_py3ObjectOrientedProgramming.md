

⾯向对象编程

[Python3教程™](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/https://www.yiibai.com/python3)

[(Back to 面向过程编程)](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/#面向过程编程)

面向对象编程——Object Oriented Programming，简称OOP
：  一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

⾯向对象的设计思想是抽象出Class，根据Class创建Instance 。

> <font color = 'orange'>⾯向过程的程序设计 </font> 把计算机程序视为一系列的==命令集合==，即==一组函数的顺序执⾏==。为了简化程序设计，⾯向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。<font color='red'>命令顺序执行</font>

> <font color='orange'>⾯向对象的程序设计</font>把计算机程序视为==⼀组对象的集合==，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是==一系列消息在各个对象之间传递==。<font color='red'>对象传递消息处理</font>

- 在Python中，所有数据类型都可以视为对象，当然也可以⾃定义对象。⾃定义的对象数据类型就是面向对象中的类（Class）的概念。

---
我们以⼀个例子来说明⾯向过程和面向对象在程序流程上的不同之处。

> 假设我们要处理学生的成绩表，为了表示一个学⽣的成绩，⾯向过程的程序可以⽤一个dict 表示：
>
> ![面向过程](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/面向过程.jpg '面向过程')

> ```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' id = 'std' output='markdown'} ##hide  代码隐藏
> std1 = { 'name': 'Curry', 'score': 98 }
> std2 = { 'name': 'James', 'score': 81 }
> ```


> 而处理学⽣成绩可以通过函数实现，⽐如打印学⽣的成绩：
```python
std1 = { 'name': 'Curry', 'score': 98 }
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
print_score(std1)
```

> 如果采⽤⾯向对象的程序设计思想，我们⾸先思考的不是程序的执行流程，而是Student 这种数据类型应该被视为⼀个对象，这个对象拥有name 和score 这两个属性（Property）。如果要打印一个学生的成绩，⾸先必须创建出这个学生对应的对象，然后，给对象发一个print_score 消息，让对象⾃己把⾃己的数据打印出来。
>
> ![面向对象](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/面向对象.jpg '面向对象')
```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
'''
给对象发消息实际上就是调⽤对象对应的关联函数，我们称之为对象的方法（Method）。面向对象的
程序写出来就像这样：
'''
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

```

# 类和对象

面向对象编程的2个⾮常重要的概念：类和对象

对象是面向对象编程的核心，在使用对象的过程中，为了将具有共同特征和行为的一组对象抽象定义，提出了另外⼀个新的概念——类

## 类

具有相似内部状态和运动规律的实体的集合(或统称为抽象)。 具有相同属性和⾏为事物的统称,类是抽象的,在使用的时候通常会找到这个类的一个具体的存在,使用这个具体的存在。一个类可以找到多个对象

## 对象

某一个具体事物的存在 ,在现实世界中可以是看得见摸得着的。 可以是直接使用的
## 类和对象之间的关系

<!-- @import  "类和对象之间的关系.png" {title="类和对象之间的关系"}
![类和对象之间的关系](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/类和对象之间的关系.png  "类和对象之间的关系") -->

![类和对象之间的关系][scenery]

[scenery]:类和对象之间的关系.png  "类和对象之间的关系"

## 总结：类就是创建对象的模板

# 定义类和创建对象

## 定义类的格式为:

```python
class 类名:
'''方法列表'''
# class Hero: # 经典类（旧式类）定义形式
# class Hero():

class Hero(object): # 新式类定义形式
    def info(self):
       print("hero")
```

> 说明：
- 定义类时有2种形式：新式类和经典类，上面代码中的Hero为新式类，前两行注释部分则为经典类；
- object 是Python 里所有类的最顶级父类；
- <font color='red'>类名 的命名规则按照"⼤驼峰命名法"；</font>
- info 是⼀个实例⽅法，第一个参数一般是self ，表示实例对象本身，当然了可以将self换为其它的名字，其作用是⼀个变量 ,这个变量指向了实例对象.
- python中，可以根据已经定义的类去创建出一个或多个对象。

## 创建对象的格式为:

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
'''
对象名1 = 类名()
对象名2 = 类名()
对象名3 = 类名()
'''
class Hero(object): # 新式类定义形式
    """info 是一个实例方法，类对象可以调用实例方法，实例方法的第一个参数⼀定是self"""
    def info(self):
        """当对象调⽤实例⽅法时，Python会⾃动将对象本身的引⽤做为参数，传递到实例⽅法的第⼀个参数self⾥"""
        print(self)-->  <__main__.Hero object at 0x7f1dcc4f4c10>
        print("self各不同，对象是出处。")
# Hero这个类 实例化了⼀个对象
hero = Hero()
# 对象调⽤实例⽅法info()，执⾏info()⾥的代码
# . 表示选择属性或者⽅法
print(hero.info())  # 等同于在info方法中 print(self)
>>> <__main__.Hero object at 0x7f1dcc4f4c10>
print(hero) # 打印对象，则默认打印对象在内存的地址，结果等同于info里的print(self)
>>> <__main__.Hero object at 0x7f1dcc4f4c10>

```
## 对象的创建流程

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class Dog(object):
    # 初始化
    def __init__(self):

        print('__init__')


    # 创建的方法
    def __new__(cls):
        print('__new__')

        return object.__new__(cls)
print(Dog())

# __new__   # 使用Dog()类,首先调用__new__(cls)类方法,创建类
# __init__ # 其次调用__init__(self)方法,初始化实例方法
# <main.Dog object at 0x0000022A37464828>
```



# 对象的属性和⽅法

## 添加和获取对象的属性

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class Hero(object):
    """定义了⼀个英雄类，可以移动和攻击"""
    def move(self):
        """实例方法"""
        print("正在前往事发地点...")

# 实例化了⼀个英雄对象
hero = Hero()


# 给对象添加属性，以及对应的属性值
hero.name = "德玛⻄亚" # 姓名
hero.hp = 2600 # ⽣命值

# 通过.成员选择运算符，获取对象的属性值
print("英雄 %s 的⽣命值 :%d" % (hero.name, hero.hp))

# 通过.成员选择运算符，获取对象的实例方法 move()
hero.move()--> 正在前往事发地点...

print(hero)
```
### 通过self获取对象属性

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class Hero(object):
    """定义了一个英雄类，可以移动和攻击"""
    def move(self):
        """实例方法"""
        print("正在前往事发地点...")
    def info(self):
        """在类的实例⽅法中，通过self获取该对象的属性"""
        print("英雄 %s 的⽣命值 :%d" % (self.name, self.hp))
# 实例化了⼀个英雄对象
hero = Hero()
# 给对象添加属性，以及对应的属性值
hero.name = "德玛西亚" # 姓名
hero.hp = 2600 # ⽣命值
# 通过.成员选择运算符，获取对象的实例方法
hero.info() # 只需要调⽤实例方法info()，即可获取英雄的属性
>>> 英雄 德玛西亚 的⽣命值 :2600
hero.move()
>>> 正在前往事发地点...

```
### \_\_init\_\_魔法方法

- \_\_init\_\_方法
- ⼀个类里⽆论⾃己是否编写\_\_init\_\_方法 ⼀定有\_\_init\_\_方法。

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class Hero(object):
    """定义了⼀个英雄类，可以移动和攻击"""
# Python 的类里提供的，两个下划线开始，两个下划线结束的⽅法，就是魔法方法，__init__()就是一个魔法方法，通常⽤来做属性初始化 或 赋值 操作。
# 如果类面没有写__init__⽅法，Python会自动创建，但是不执行任何操作，
# 如果为了能够在完成⾃己想要的功能，可以⾃己定义__init__方法，
# 所以⼀个类里⽆论⾃己是否编写__init__方法 ⼀定有__init__方法。
    def __init__(self):
        """ 方法，⽤来做变量初始化 或 赋值 操作，在类实例化对象的时候，会被⾃动调⽤"""
        self.name = "hero" # 姓名
        self.hp = 2600 # ⽣命值
    def move(self):
        """实例⽅法"""
        print("正在前往事发地点...")
    def info(self):
        """在类的实例⽅法中，通过self获取该对象的属性"""
        print("英雄 %s 的⽣命值 :%d" % (self.name, self.hp))
# 实例化了⼀个英雄对象，并⾃动调⽤__init__()⽅法
hero = Hero()
# 通过.成员选择运算符，获取对象的实例方法
hero.info() # 只需要调⽤实例⽅法info()，即可获取英雄的属性
hero.move()

```
##### 总结：
- \_\_init\_\_() 方法，在创建⼀个对象时默认被调用，不需要手动调用
- \_\_init\_\_(self) 中的self参数，不需要开发者传递，python解释器会<font color='orange'>自动把当前的对象引⽤传递过去</font>。

### 有参数的\_\_init\_\_()⽅法

- 同一个<font color='orange'>类</font>的不同对象，==实例⽅法共享==
    - 不同<font color='red'>对象</font>的==属性值的单独保存==



```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class Hero(object):
    """定义了⼀个英雄类，可以移动和攻击"""
    def __init__(self, name, hp):
        """ __init__() ⽅法，⽤来做变量初始化 或 赋值 操作"""
        # 英雄名
        self.name = name
        # ⽣命值：
        self.hp = hp
    def move(self):
        """实例⽅法"""
        print("%s 正在前往事发地点..." % self.name)
    def info(self):
        print("英雄 %s 的⽣命值 :%d" % (self.name, self.hp))
# 实例化英雄对象时，参数会传递到对象的__init__()方法⾥
blind = Hero("瞎哥",2600,)
gailun = Hero("盖伦",4200)
print(gailun)--><__main__.Hero object at 0x7f1dcc4935d0>
print(blind)--><__main__.Hero object at 0x7f1dcc493550>
# 不同对象的属性值的单独保存
print('blind.name id:',id(blind.name))
>>> blind.name id: 139765958088048
print('gailun.name id:',id(gailun.name))
>>> gailun.name id: 139765958090640
# 同一个类的不同对象，实例⽅法共享
print('blind.move() id',id(blind.move()))
>>>
瞎哥 正在前往事发地点...
blind.move() id 94027489959824
print('gailun.move() id',id(gailun.move()))
>>>
盖伦 正在前往事发地点...
gailun.move() id 94027489959824

```
##### 注意：
- 通过一个类，可以创建多个对象，就好比 通过⼀个模具创建多个实体一样
\_\_init\_\_(self) 中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么\_\_init\_\_(self) 中除了self作为第一个形参外还需要2个形参，例如\_\_init\_\_(self,x,y)
- 在<font color='orange'>类内部</font>获取 属性 和 实例方法，通过==self获取==；
- 在<font color='red'>类外部</font>获取 属性 和 实例⽅法，通过==对象名获取==。
- 如果一个类有多个对象，<font color='red'>每个对象的属性是各自保存的，都有各自独立的地址</font>；
- 但是<font color='orange'>实例方法是所有对象共享的，只占⽤一份内存空间</font>。==类会通过self来判断是哪个对象调⽤了实例方法==。

### 继承

- 在程序中，继承描述的是多个类之间的所属关系。
- 如果⼀个类A里⾯的属性和⽅法可以复用，则可以通过继承的方式，传递到类B里。
- 那么类A就是基类，也叫做父类；类B就是派生类，也叫做子类。
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 父类
class A(object):
    def __init__(self):
        self.num = 10
    def print_num(self):
        print(self.num + 10)
    # 子类
class B(A):
    pass
b = B()
print(b.num)
b.print_num()

```
### 单继承

单继承
:   子类只继承一个父类。

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 定义一个Person类
class Person(object):
    def __init__(self):
        # 属性
        self.name = "女娲"
        # 实例方法
    def make_person(self):
        print(" <%s> 造了一个人..." % self.name)
    # 定义Teacher类，继承了 Person，则Teacher是子类，Person是父类。
class Teacher(Person):
    # ⼦类可以继承⽗类所有的属性和方法，哪怕子类没有⾃己的属性和方法，也可以使⽤⽗类的属性和⽅法。
    pass
panda = Teacher() # Teacher类创建实例对象panda
print(panda.name) # ⼦类对象可以直接使⽤父类的属性
panda.make_person() # ⼦类对象可以直接使用父类的方法
# 查看类的MRO(方法解析序列)的两种方法
Teacher().__class__.mro()-->[__main__.Teacher, __main__.Person, object]
Teacher.__mro__          -->(__main__.Teacher, __main__.Person, object)
```
- **总结**：

虽然⼦类没有定义\_\_init\_\_ 方法初始化属性，也没有定义实例方法，但是父类有。所以只要创建类的对象，就默认执行了那个继承过来的\_\_init\_\_ 方法,在定义类时，⼩括号()中为父类的名字父类的属性、方法，会被继承给子类

### 多继承

多继承
:   子类继承多个父类
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class Women(object):
    def __init__(self):
        self.name = "女娲" # 实例变量，属性
    def make_person(self): # 实例方法，方法
        print(" <%s> 造了⼀个人..." % self.name)
    def move(self):
         print("移动..")
class Man(object):
    def __init__(self):
        self.name = "亚当"
    def make_person(self):
        print("<%s> 造了⼀个人..." % self.name)
    def run(self):
        print("跑..")
class Person(Women, Man): # 多继承，继承了多个⽗类
    pass

ls = Person()
print(ls.name)
ls.make_person()

# ⼦类的魔法属性__mro__决定了属性和⽅法的查找顺序
print(Person.__mro__)
>>> (<class '__main__.Person'>, <class '__main__.Women'>, <class '__main__.Man'>, <class 'object'>)
print(Person().__class__.mro())
>>>[<class '__main__.Person'>, <class '__main__.Women'>, <class '__main__.Man'>, <class 'object'>]
```
- **结论**：
    - 多继承可以继承多个父类，也继承了所有父类的属性和方法
    - 注意：如果多个父类中有同名的 属性和⽅法，则默认使用第一个父类的属性和方法（根据类的魔法属性mro 的顺序来查找）
    - 多个父类中，不重名的属性和方法，不会有任何影响。

### 重写父类方法

- 重写：⼦类继承父类，父类的方法满⾜不了子类的需要可以对父类的方法进行重写
- 重写的特点:
    1. 继承关系，
    2. ⽅法名相同

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class Person(object):
    def run(self):
        print("跑起来了")
class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
# # 因为⽗类的⽅法满⾜足不了⼦类的需要，对其进⾏重写
    def run(self):
        print("%s跑起来了" % self.name)

stu = Student("王五", 10)
# 调⽤⽅法的时候先从本类去找，如果本来没有再去⽗类去找，会遵循mro的特点
stu.run()

```
### 属性方法

- <font color='orange'>类</font>属性和<font color='red'>实例</font>属性
类属性就是类对象所拥有的属性，它被所有类对象的实例对象所共有，在内存中只存在一个副本，这个和C++中类的静态成员变量有点类似。
对于公有的类属性，在类外可以通过类对象和实例对象访问

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class People(object):
    name = 'Tom' # 公有的类属性
    __age = 12 # 私有的类属性
p = People()
print(p.name) # 正确
print(People.name) # 正确
print(p.__age) # 错误，不能在类外通过实例对象访问私有的类属性
print(People.__age) # 错误，不能在类外通过类对象访问私有的类属性

```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class Person(object):
    def __init__(self):
        # 实例属性（公开的）
        self.name = 'zs'
        #私有属性（只能在类的内部使用，）
        self.__age=0

    # 设置私有属性值的方法
    def set_age(self,new_age):
        if new_age>0 and new_age<=100:

            self.__age = new_age
        else:
            self.__age = 0
    # 获取私有属性值的方法
    def get_age(self):

        return self.__age

    def show(self):
        print('Person')
        self.__test()

    # 私有方法
    def __test(self):
        pass

p = Person()

p.set_age(100)

print(p.get_age())-->100

```




2. 实例属性(对象属性)
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class People(object):
    address = '⼭东' # 类属性
    def __init__(self):
        self.name = 'xiaowang' # 实例属性
        self.age = 20 # 实例属性
p = People()
p.age = 12 # 实例属性
print(p.address) # 正确  在类外通过实例对象访问 类属性
print(p.name) # 正确     在类外通过实例对象访问 实例属性
print(p.age) # 正确
print(People.address) # 正确   在类外通过类对象访问 类属性
print(People.name) # 错误     不能在类外通过类对象访问 实例属性
print(People.age) # 错误
```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

#通过实例(对象)去修改类属性
class People(object):
    country = 'china' #类属性
print(People.country)-->'china' 
p = People()
print(p.country)-->'china' 
'''
添加实例p的country属性，而不是修改类Person的country属性
'''
p.country = 'japan'

print('p.country:',p.country)-->'japan' # 实例属性会屏蔽掉同名的类属性
print('People.country:',People.country)-->'china' 
del p.country # 删除实例属性
print(p.country)-->'china' 

```
- 总结
    - 如果需要==在类外<font color='red'>修改类属性</font>，必须通过类对象去引⽤然后进行修改==。
    - 如果通过实例对象去引用，会产⽣一个同名的实例属性，这种方式==<font color='orange'> 修改的是实例属性</font>==，不会影响到类属性，并且之后如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是实例属性，除⾮删除了该实例属性。

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
class Tool(object):
    # 类属性，计数
    num = 0
    print(num)  # 创建Tool类时,执行类属性 print(num)
    def __init__(self,name):
        self.name = name
        Tool.num += 1
        print('Tool.num',Tool.num)  # 类创建实例时,执行__init__方法(创建一次实例执行一次)
t1 = Tool('水桶') # Tool.num 1
t2 = Tool('垃圾桶') # Tool.num 2
t3 = Tool('锅') # Tool.num 3
print(Tool.num) # 3
```

## 静态⽅法和类方法

### 类⽅法

类⽅法
:   是类对象所拥有的方法，需要⽤修饰器@classmethod来标识其为类方法，对于类⽅法，第一个参数必是类对象，一般以cls作为第一个参数（当然可以⽤其他名称的变量作为其第一个参数，但是大部分人都习惯以'cls'作为第一个参数的名字，就最好用'cls'了），能够通过实例对象和类对象去访问类方法。

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class People(object):
    country = 'china'
    #类⽅法，⽤classmethod来进⾏修饰
    @classmethod
    def get_country(cls):
        return cls.country


p = People()
print(p.get_country()) #可以通过实例对象引⽤类方法
print(People.get_country()) #可以通过类对象引用类方法
```
- 类⽅法还有⼀个用途就是可以通过实例调用类方法对类属性进⾏修改：
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class People(object):
    country = 'china'
    #类⽅法，⽤classmethod来进⾏修饰
    @classmethod
    def get_country(cls):
        return cls.country
    @classmethod
    def set_country(cls,country):
        cls.country = country
p = People()
print(p.get_country()) #可以通过实例对象访问
print(People.get_country()) #可以通过类访问
#结果显示在用类⽅法对类属性修改之后，通过类对象和实例对象访问都发⽣了改变
p.set_country('japan') # 通过实例调用类方法对类属性进⾏修改
print(p.get_country())
print(People.get_country())

```
#### 静态⽅法
需要通过修饰器@staticmethod 来进⾏修饰，静态方法不需要多定义参数，可以通过对象和类来访问。
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

class People(object):
    country = 'china'
    #静态⽅法
    @staticmethod
    def get_country():
        return People.country
p = People()
# 通过对象访问静态方法
p.get_country()
# 通过类访问静态⽅法
print(People.get_country())
```
#### 总结
从类⽅法和实例方法以及静态方法的定义形式就可以看出来，
- <font color='red'>类⽅法</font>的第⼀个参数是类对象cls，那么通过cls引⽤的必定是类对象的属性和方法；
- <font color='orange'>实例方法</font>的第⼀个参数是实例对象self，那么通过self引用的可能是类属性、也有可能是实例属性（这个需要具体分析），不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。
- 静态⽅法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类实例对象来引⽤
## 多态

> - 多态, <font color='blue'>不同的 子类对象调⽤ 相同的 父类方法，产生 不同的 执行结果</font>，可以增加代码的外部 调⽤灵活度
> - ==多态==以 继承 和 重写 父类方法 为==前提==
> - 多态是调用⽅法的技巧，不会影响到类的内部设计



- 定义一个方法（参数必须传一个animal类型的对象）


```python {cmd = true matplotlib=true code_block=true class= &#39; line-numbers&#39;  continue=&#39;utf-8&#39; output=&#39;markdown&#39;} ##hide  代码隐藏
class Animal(object):
    def run(self):
    	 print('Animal is running...')
class Dog(object):
    def run(self):
        print('Dog is running...')
class Cat(object):
    def run(self):
        print('Cat is running...')
        
def run_twice(animal):
        animal.run()
        animal.run()
        
dog = Dog()
cat = Cat()

run_twice(dog)
run_twice(cat)

# 多态
# 继承和重写前提

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')



# 定义一个方法（参数必须传一个animal类型的对象）
def func(Animalbianliang):
    bianliang.run()


dog = Dog()

cat = Cat()
cat.run()
dog.run()


func(dog)
func(cat)


```

## 函数装饰器和类装饰器

[没看完这 11 条，别说你精通 Python 装饰器](https://mp.weixin.qq.com/s/uF9Gqk_NhCEBsuMV0IyNXw)

### 函数装饰器




### 类装饰器




# 捕获异常

[(Back to 面向过程编程)](#面向过程编程)

[(Back to 面向对象编程)](#⾯向对象编程)

[常⻅的错误类型和继承关系看这⾥](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

- ⼀旦出错，还要⼀级一级上报，直到某个函数可以处理该错误
- 所以⾼级语⾔通常都内置了一套try...except...finally... 的错误处理机制
    - try 来运行这段代码，如果执⾏出错，则后续代码不会继续执⾏，⽽是直接跳转⾄错误处理代码，即except 语句块
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
'''
当我们认为某些代码可能会出错时，就可以⽤try 来运行这段代码，如果执⾏出错，则后续代码不会继续执⾏，⽽是直接跳转⾄错误处理代码，即except 语句块，执⾏完except 后，如果有finally 语句块，则执⾏finally 语句块，⾄此，执行完毕。
'''
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
'''
由于没有错误发⽣，所以except 语句块不会被执行，但是finally 如果有，则⼀定会被执行（可以没有finally 语句）。

从输出可以看到，当错误发生时，后续语句print('result:', r) 不会被执行， except 由于捕获到ZeroDivisionError ，因此被执行。最后， finally 语句被执⾏。然后，程序继续按照流程往下走。
'''
```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
# 可以有多个except 来捕获不同类型的错误：
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
# 如果没有错误发⽣，可以在except 语句块后面加一个else ，当没有错误发⽣时，会⾃动执行else 语句：
else:
    print('no error!')
finally:
    print('finally...')
print('END')

```
## Python的错误其实也是class
所有的错误类型都继承⾃BaseException ，所以在使⽤except 时需要注意的是，它不但捕获该类型的错误，还把其⼦类也“⼀⽹打尽”。
比如：
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

# 第⼆个except 永远也捕获不到UnicodeError ，因为UnicodeError 是ValueError 的⼦类，如果有，也被第一个except 给捕获了。
```
- Python所有的错误都是从BaseException 类派⽣的，[常⻅的错误类型和继承关系看这⾥](#exception-hierarchy)
- 使⽤try...except 捕获错误还有⼀个巨大的好处，就是可以跨越多层调⽤，⽐如函数main() 调用foo() ， foo() 调用bar() ，结果bar() 出错了，这时，只要main() 捕获到了，就可以处理：
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
         print('finally...')
'''
也就是说，不需要在每个可能出错的地⽅去捕获错误，只要在合适的层次去捕获错误就可以了。
'''
```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  id='utf-8' continue:true output='markdown' } ##hide  代码隐藏
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
```

# 模块

[(Back to 面向过程编程)](#面向过程编程)

[(Back to 面向对象编程)](#⾯向对象编程)

- `help('modules')`# <font color='red'>查看所安装的模块</font>

    

「模块」、「常规包」与「命名空间包」是理解import机制绕不开的概念。

「模块」：一个以「.py」为后缀的文件就是一个模块 

「常规包」：「`__init__.py`」所在目录就是一个常规包 

「命名空间包」：命名空间包是一种虚拟的概念，它由多个子包构成，这些子包可以在任意位置，可以为 zip 中的文件或网络上的文件，这些子包在概念上是一个整体，这个整体就是一个命名空间包

「常规包」与「命名空间包」的概念在 PEP420 被提出，在 Python3.3 及之后的 Python 版本中实现，此前只有「常规包」这一种包。

模块
:   通俗理解⼀个.py⽂件就是⼀个模块，模块是管理功能代码的。

内置模块
:   就是python⾃⼰内部⾃带的不需要我们去下载的模块， ⽐如：time, random等。

>  **模块**是一个.py文件或以其他文件形式存在的可被引入的就是一个模块
>
>  **包**是一个装有多个.py文件 和 \_\_init\_\_.py文件的文件夹
>
>  **路径查找**：python解释器查找被安装的包或模块

## [模块搜索路径和包导入](https://www.cnblogs.com/ljhdo/p/10674242.html)



在导入自定义的模块时，除了指定==模块名==之外，也需要指定==目录==，由于Python把目录称作包，因此，这类导入被称为包导入。包导入把计算机上的目录变成Python的命名空间，而<font color='orange'>目录中所包含的子目录和模块文件则对应命名空间中的属性。</font>

- .py文件—模块
- 文件夹+\_\_init\_\_.py文件—包

import 语句做的是两个操作

- 搜索操作：在相应的路径中搜索指定名称的模块 
- 绑定操作：将搜索到的结果绑定到当前作用域对应的名称上(即创建module对象，并初始化)

通过阅读 Python 官方文档可知，import 的搜索操作通过` __import__() `方法实现，而绑定操作只有 import 语句才能做到。

### sys.modules和模块中的`__file__`变量的作用

Python<font color='red'>已经导入的模块保存在一个内置的sys.modules字典中</font>，以便记录哪些模块已经记录了。

- Python解释器启动之后，会把预先加载内置模块，可以通过`sorted(sys.modules)`验证。

- 通过`sys.modules`和`__file__`，可以动态获取所有已加载模块目录和路径。

    ```python
    # __file__是从中加载模块的文件的路径名（如果它是从文件加载的）
    sys.modules['os'].__file__
    >>> '/home/leung/anaconda3/lib/python3.7/os.py'
    os.path.realpath(sys.modules['os'].__file__)
    >>> '/home/leung/anaconda3/lib/python3.7/os.py'
    print(sys.argv[0]) #获取主入口执行文件
    >>>'/home/leung/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py'
    ```

### 模块搜索路径

导入过程首先需要定位导入文件的位置，也就是，告诉Python到何处去找到要导入的文件，因此，需要设置模块的搜索路径。在大多数情况下，Python会自动到默认的目录下去搜索模块；如果要在默认的目录之外导入模块，就需要知道Pyhon搜索模块路径的机制。

如果我们没有修改，sys.path 中默认的路径为：

- 1.当前目录的路径
- 2.环境变量 PYTHONPATH 中指定的路径列表
- 3.Python 安装路径的 lib 目录所在路径

要修改搜索路径有3种方式:

- 动态修改 sys.path，因为 sys.path 为 list，所以我们可以很轻松的操作 list 实现搜索路径的修改。这种方式只会对当前项目临时生效

- 修改 PYTHONPATH 环境变量，这种方式会永久生效，而且所有的 Python 项目都会受到影响，因为 Python 程序启动时会自动去读取该环境良好的值。

- 增加 .pth 后缀的文件。在 sys.path 已有的某一个目录下添加 .pth 后缀的配置文件，该文件的内容就是要添加的搜索路径，Python 在遍历已有目录的过程中，如果遇到 .pth 文件，就会将其中的路径添加到 sys.path 中。

    ```python
    import os
    from os.path import join
    import os.path.join
    >>>ModuleNotFoundError : No module named 'os.path.join'; 'os.path' is not a package
    第2行与第3行的区别在于是否使用 from，其背后的规则是：
    1.单独使用 import 时，import 后面只能接模块或包(常规包或命名空间包)
    2.使用 from xxx import xxx 时，from 后只能接模块或包，而此时 import 后可以接任何变量(模块、包或模块中具体的方法)
    ```

    

### 配置搜索路径

上述四种模块搜索路径，能够配置的选项只有==PYTHONPATH环境变量==和==路径文件==。例如，在Windows平台上，创建PYTHONPATH环境变量，设置变量的值，两个目录使用英文状态下半角分号隔开：

```sh
C:\pycode\utilities;D:\pycode\package1
```

也可以创建一个名为 C:\Python30\pydirs.pth的文本文件，其内容如下所示：

```sh
C:\pycode\utilities
D:\pycode\package1
```

### sys.path列表

如果想看模块搜索路径在机器上的实际配置，可以通过打印内置的sys.path列表来查看，这个列表是sys模块的path属性。

```python
import sys
print(sys.path)
```

其实，sys.path是模块搜索的路径，Pytho在程序启动时进行配置，自动把顶级文件的主目录，PYTHONPATH环境变量中配置的目录，.pth文件中目录以及标准连接库目录加载到sys.path列表中，Python每次导入一个新的模块，都是从sys.path列表中查找搜索目录。

- 查看
    - `sys.path`
- 修改
    - 临时
        - `sys.path = []` #赋值空列表后,只能检索到标准库,检索不到第三方库/模块
        - sys.path.insert(0,‘path’)
        - sys.path.append(‘path’)
    - 永久
        - PYTHONPATH=$PYTHONPATH:‘/path’
        - **推荐** 最好的方法，是在sys.path的某个目录下,路径配置文件的扩展名是”.pth”[修改python import包/模块搜索路径的几种方法 - 简书](https://www.jianshu.com/p/cc09c71f979d)

### 包导入基础

搜索路径是指Python搜索模块的路径前缀，在import 语句的路径上添加这些路径，以构成模块的绝对路径。通常把存储模块的根目录称作容器目录，记作dir0，容器目录dir0必须包含在搜索路径中。

例如，在dir0目录下，存在dri1/dir2/mod.py模块，那么导入该模块需要设置搜索路径为dir0，并使用import  和路径导入该模块：

```python
import dir1.dir2.modfrom dir1.dir2.mod import mod_fun
```

在import语句中列举目录名，以点号分隔，"."路径是对应于dir0内的目录，通过这个目录可以找到mod.py模块。

### __init__.py包文件

如果选择使用包导入，就必须多遵循一条约束：包导入语句的路径中，每个目录内都必须有\_\_init\_\_.py文件，否则包导入失败。

对于目录结构 dir0/dri1/dir2/mod.py 

```python
import dir1.dir2.mod
```

必须遵守以下规则：

- dir0是容器目录，不需要\_\_init\_\_.py文件，如果有，也会被忽略。
- dir0必须列在模块搜索路径列表中，也就是说，dir0必须是主目录，或者列在PYTHONPATH环境变量中等。
- dir1和dir2都必须包含一个\_\_init\_\_.py文件

\_\_init\_\_.py文件是当 import 第一次遍历一个包目录时所运行的文件，可以包含Python程序代码，也可以完全是空的。通常情况下，\_\_init\_\_.py文件扮演了包初始化的钩子，替目录产生模块命名空间以及使用目录导入时实现from*行为的角色。

**- 包的初始化**

Python在首先导入某个目录时，会自动执行该目录下的\_\_init\_\_.py文件中的所有程序代码。

- 模块命名空间的初始化**

在包导入模型中，脚本内的目录路径，在导入后会变成真实的对象路径，即，为目录创建的模块对象提供了命名空间。

**- from \*语句的行为**

[(To \_\_init\_\_ ⽂件写法)](###\_\_init\_\_ ⽂件写法)

在\_\_init\_\_.py文件内使用\_\_all\_\_列表，来定义目录以from * 语句形式导入时，需要导出的属性清单。如果没有设置\_\_all\_\_，from *语句不会自动加载该目录内的子模块，也就是说，只加载该目录下的\_\_init\_\_.py文件中罗列在\_\_all\_\_列表中的变量。 from 包名 import *, 默认不会导⼊包⾥面的所有模块，需要在init⽂件⾥面使⽤`__all__ = ["变量名", "函数名"]from . import 变量名,函数名`,

### 创建名为first_module的⾃定义模块

```python {cmd = true matplotlib=true code_block=true class= &#39; line-numbers&#39;  continue=&#39;utf-8&#39; output=&#39;markdown&#39;} ##hide  代码隐藏
# 指定__all__表示 from 模块名 import * 只能使⽤指定的功能代码，⽽不是所有的功能代码
__all__ = ["g_num", "show"]

# 定义全局变量
g_num = 10
# 定义函数
def show():
    print("我是⼀个函数")
    # 定义类
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_msg(self):
        print(self.name, self.age)
# 解决导⼊的模块中⽅法没有调⽤就会执行
if __name__ == '__main__':
    show()

'''
注意：使⽤ __name__ 查看模块名，执⾏哪个⽂件，哪个⽂件中的__name__ 输出 __main__ , 其他导
⼊模块中的__name__ 结果就是模块名字。
'''
```



## 自定义模块的使⽤

- 注意：⾃定义模块名字和变量名的定义很类似，都是由字⺟、数字、下划线组成，但是不能以数字开头，否则⽆法导⼊该模块。


```python
# 模块 .py文件
import random
import time

# import requests
# pip install requests
help('modules')# 查看所安装的模块
```

```python
# 自定义需要两步： 修改成 .py文件， first_module.py文件与当前导入的文件放在同一个目录下
import first_module

# 使用模块中的是方法
# print(first_module.g_num)
# first_module.show()
print(__name__)# __main__
```

### 使⽤⾃定义的模块
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 导⼊模块
import first_module
# 使⽤模块中的功能代码
print(first_module.g_num)
first_module.show()
stu = first_module.Student("李四", 20)
stu.show_msg()

```

- 模块导⼊的注意点：

1. ⾃定义的模块名不要和系统的模块名重名，
2. 导⼊的功能代码不要在当前模块定义否则使⽤不了导⼊模块的功能代码

### 包的介绍

包
:   通俗理解包就是⼀个⽂件夹，只不过⽂件夹⾥面有⼀个`__init__.py`⽂件
包是管理模块的， 模块是管理功能代码的。

 包-模块-代码：
![包-模块-代码](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/包-模块-代码.png)


```python

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

# -----import导⼊包⾥面的模块----
import first_package.first
#-----import导⼊包⾥面的模块设置别名----
import first_package.first as one
#----from导⼊包名 import 模块名----
from first_package import second
#--- from 包名.模块名 import 功能代码----
from first_package.first import show # 需要保证当前模块没有导⼊模块的功能代码
# --- from 包名 import *, 默认不会导⼊包⾥面的所有模块，需要在init⽂件⾥面使⽤__all__
'''
__all__ = ["g_num", "show"]
 '''
去指定导⼊的模块
from first_package import *
```
### `__init__` ⽂件写法

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 如果外界使⽤from 包名 import * 不会导⼊包⾥面的所有模块，需要使⽤__all__指定
__all__ = ["first", "second"]
# 从当前包导⼊对应的模块
from . import first
from . import second

```

# Python系统操作（sys、os）模块

[Python系统操作（sys、os）模块 - 知行流浪 - CSDN博客](https://blog.csdn.net/zengxiantao1994/article/details/58188527)

[Python3.5内置模块之os模块、sys模块、shutil模块用法实例分析_python_脚本之家](https://www.jb51.net/article/160327.htm)

## sys库

​        <font color='orange'>sys模块</font>包括了一组非常实用的服务，内含很多函数方法和变量，用来==处理Python运行时配置以及资源==，从而可以与前当程序之外的系统环境交互，如：python解释器。

- sys模块的常见函数列表(import sys)

| 函数                                    | 说明                                                         |
| --------------------------------------- | ------------------------------------------------------------ |
| dir(sys)                                | dir()方法查看模块中可用的方法。<br>注意：如果是在编辑器，一定要注意要事先声明代码的编码方式，否则中文会乱码。 |
| sys.argv                                | 实现从程序外部向程序传递参数<br>命令行参数List，第一个元素是程序本身路径 |
| sys.exit([arg])                         | 程序中间的退出，arg=0为正常退出                              |
| sys.getdefaultencoding()                | 获取系统当前编码，一般默认为ascii                            |
| sys.setdefaultencoding()                | 设置系统默认编码，<br>执行dir(sys)时不会看到这个方法，在解释器中执行不通过，<br>可以先执行reload(sys), 再执行setdefaultencoding('utf8')，将系统编码设置为utf8 |
| sys.getfilesystemencoding()             | 获取文件系统编码方式，Windows下返回'mbcs'，mac下返回'utf-8'  |
| print(sys.version)                      | 获取Python解释程序的版本信息                                 |
| sys.path                                | 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值<br>获取指定模块搜索路径的字符串集合，<br>可以将写好的模块(或包含模块路径的.pth文件)放在得到的某个路径下，就可以在程序中import时正确找到 |
| sys.platform                            | 获取当前系统平台。                                           |
| sys.stdin<br/>sys.stdout<br/>sys.stderr | stdin，stdout，以及stderr变量包含与标准I/O流对应的流对象。<br>如果需要更好地控制输出，而print不能满足要求，它们就是你所需要的。  你也可以替换它们，重定向输出和输入到其它设备(device)，或者以非标准的方式处理它们。<br>sys.stdout.write('please:')  #标准输出,写入字符串输出到屏幕>>>please:<br>val = sys.stdin.readline()[:-1]  #标准输入 |
| sys.modules                             | 是一个全局字典，该字典是python启动后就加载在内存中。<br>每当程序员导入新的模块，sys.modules将自动记录该模块。当第二次再导入该模块时，python会直接到字典中查找，从而加快程序运行的速度。它拥有字典所拥有的一切方法。 |
|                                         |                                                              |

## os库

​        <font color='red'>os模块</font>负责==程序与操作系统的交互==，提供了访问操作系统底层的接口。

- os模块的常见函数列表(import os)

| 函数                                                       | 说明                                                         |
| ---------------------------------------------------------- | ------------------------------------------------------------ |
| os.environ                                                 | (查看系统的环境变量)一个包含环境变量的映射关系的字典         |
| os.name                                                    | 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'        |
| print(os.stat(r"./Desktop/"))                              | 获取文件/目录信息                                            |
| print(os.system("dir"))                                    | 运行shell命令，直接显示                                      |
| os.sep                                                     | 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"       |
| os.linesep                                                 | 输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"      |
| print(os.pathsep)                                          | 输出用于分割文件路径的字符串,win下为";",Linux下为":"         |
| print(os.path.abspath(r".Untitled.ipynb"))                 | 返回path规范化的绝对路径<br>/home/leung/.Untitled.ipynb      |
| print(os.path.split(r"/home/leung/Untitled.ipynb"))        | 将path分割成目录和文件名<br>('/home/leung', 'Untitled.ipynb') |
| print(os.path.dirname(r"/home/leung/"))                    | 返回path的目录<br>/home/leung                                |
| print(os.path.basename(r"/home/leung/Untitled.ipynb"))     | 返回path最后的文件名<br>Untitled.ipynb                       |
| print(os.path.exists(r"F:\PythonCode\day5"))               | 如果path存在，返回True；                                     |
| print(os.path.isabs(r"F:\PythonCode\day5"))                | 如果path是绝对路径，返回True                                 |
| print(os.path.isfile(r"F:\PythonCode\day5\p_test.py"))     | 如果path是一个存在的文件，返回True                           |
| print(os.path.isdir(r"F:\PythonCode\day5"))                | 如果path是一个存在的目录，则返回True                         |
| print(os.path.join(r"/home/",r"leung/",r"Untitled.ipynb")) | /home/leung/Untitled.ipynb<br>将多个路径组合后返回           |
| print(os.path.getatime(r"F:\PythonCode\day5"))             | 返回path所指向的文件或者目录的最后access时间                 |
| os.remove('filename')                                      | 删除一个文件<br>`os.remove('/tmp/xx/b.txt')`                 |
| os.rename("oldname","newname")                             | 重命名文件<br>`os.rename('/tmp/xx/a.txt','/tmp/xx/b.txt')`   |
| os.getcwd()                                                | 显示当前python脚本工作路径                                   |
| print(os.curdir)                                           | 返回当前目录 '.'                                             |
| print(os.pardir)                                           | 获取当前目录的父目录字符串名 '..'                            |
| os.chdir(dir)                                              | 改变当前目录，注意windows下用到转义                          |
| os.listdir('dirname')                                      | 返回指定目录下的所有文件和目录名                             |
| os.makedirs(r"F:\a\b\c")                                   | 生成多层递归目录                                             |
| os.removedirs(r"F:\a\b\c")                                 | 清理空文件夹<br>若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推 |
| os.mkdir('dirname/dirname')                                | 生成单级目录，相当于shell中mkdir filename<br>`os.mkdir('/tmp/xx')` |
| os.rmdir('dirname')                                        | 删除单级空目录，若目录不为空，无法删除或报错<br>`os.rmdir('/tmp/xx')` |
| os.getlogin()                                              | 得到用户登录名称–'leung'                                     |
| os.getenv(‘key’)                                           | 得到环境变量配置                                             |
| os.putenv(‘key’)                                           | 设置环境变量                                                 |
| os.system(‘command’)                                       | 运行shell命令，注意：这里是打开一个新的shell，运行命令，当命令结束后，关闭shell。<br>`os.system("echo'hello' > /tmp/xx/a.txt")` |

### os.path

- os.path编写平台无关的程序

| 函数                                   | 说明                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| os.path.abspath()                      | 获取绝对路径<br>os.path.abspath("1.txt") == os.path.join(os.getcwd(),"1.txt") |
| os.path.split()                        | 用于分开一个目录名称中的目录部分和文件名称部分。             |
| os.pardir                              | 表示当前平台下上一级目录的字符 ..                            |
| os.path.splitext('Untitled.ipynb')     | 返回文件名和文件扩展名的元组<br>('Untitled', '.ipynb')       |
| os.path.join(path, name)               | 连接目录和文件名。                                           |
| os.path.basename(path)                 | 返回文件名                                                   |
| os.path.dirname(path)                  | 返回文件路径                                                 |
| os.path.getctime("/root/1.txt")        | 返回1.txt的ctime(创建时间)时间戳                             |
| os.path.exists(os.getcwd())            | 判断文件是否存在                                             |
| os.path.isfile(os.getcwd())            | 判断是否是文件名，1是0否                                     |
| os.path.isdir('c:\Python\temp')        | 判断是否是目录，1是0否                                       |
| os.path.islink('/home/111.sql')        | 是否是符号连接，windows下不可用                              |
| os.path.ismount(os.getcwd())           | 是否是文件系统安装点，windows下不可用                        |
| os.path.samefile(os.getcwd(), '/home') | 看看两个文件名是不是指的是同一个文件                         |
| os.walk()                              | 能够把给定的目录下的所有目录和文件遍历出来。<br>`next(os.walk(os.getcwd()))` |

```python
#coding=utf-8
'''
Created on 2017年3月4日
 
@author: zxt
'''
importos
 
# 当前平台上一级目录字符..
print(os.path.pardir)
 
os.path.abspath(__file__)  :绝对路径
# 获取绝对路径（目录加当前文件名）
print(os.path.abspath(__file__))
 
# os.path.split(os.getcwd()) 用于分开一个目录名称中的目录部分和文件名称部分。
# 获取绝对目录（没有文件名）
print(os.getcwd());
print(os.path.split(os.path.abspath(__file__))[0]) # 目录
print(os.path.dirname(os.path.abspath(__file__)))# 等价于上一句
 
# 拼接文件目录和文件名
print(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir) )
 
# 获取父目录
# 当前目录的路径名称，即父目录（os.path.dirname()：显示当前路径，不会显示当前文件名）
print(os.path.dirname(os.getcwd()));
print(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)) )
```



## shutil

[Python标准库shutil用法实例详解_python_脚本之家

[关于shutil的更多操作：https://docs.python.org/3/library/shutil.html](https://www.jb51.net/article/145522.htm)

- shutil模块：高级的文件、文件夹、压缩包处理模块

### **文件夹与文件操作**

**copyfileobj(fsrc, fdst, length=16\*1024)**： 将fsrc文件内容复制至fdst文件，length为fsrc每次读取的长度，用做缓冲区大小

- fsrc： 源文件
- fdst： 复制至fdst文件
- length： 缓冲区大小，即fsrc每次读取的长度

```python
import shutil
f1 = open("file.txt","r")
f2 = open("file_copy.txt","a+")
shutil.copyfileobj(f1,f2,length=1024)
```

**copyfile(src, dst)**： 将src文件内容复制至dst文件

- src： 源文件路径
- dst： 复制至dst文件，若dst文件不存在，将会生成一个dst文件；若存在将会被覆盖
- follow_symlinks：设置为True时，若src为软连接，则当成文件复制；如果设置为False，复制软连接。默认为True。Python3新增参数

```python
import shutil
shutil.copyfile("file.txt","file_copy.txt")
```

**copymode(src, dst)**： 将src文件权限复制至dst文件。文件内容，所有者和组不受影响

- src： 源文件路径
- dst： 将权限复制至dst文件，dst路径必须是真实的路径，并且文件必须存在，否则将会报文件找不到错误
- follow_symlinks：设置为False时，src, dst皆为软连接，可以复制软连接权限，如果设置为True，则当成普通文件复制权限。默认为True。Python3新增参数

```python
import shutil
shutil.copymode("file.txt","file_copy.txt")
```

**copystat(src, dst)**： 将权限，上次访问时间，上次修改时间以及src的标志复制到dst。文件内容，所有者和组不受影响

- src： 源文件路径
- dst： 将权限复制至dst文件，dst路径必须是真实的路径，并且文件必须存在，否则将会报文件找不到错误
- follow_symlinks：设置为False时，src, dst皆为软连接，可以复制软连接权限、上次访问时间，上次修改时间以及src的标志，如果设置为True，则当成普通文件复制权限。默认为True。Python3新增参数

```python
import shutil
shutil.copystat("file.txt","file_copy.txt")
```

**copy(src, dst)**： 将文件src复制至dst。dst可以是个目录，会在该目录下创建与src同名的文件，若该目录下存在同名文件，将会报错提示已经存在同名文件。权限会被一并复制。本质是先后调用了copyfile与copymode而已

- src：源文件路径
- dst：复制至dst文件夹或文件
- follow_symlinks：设置为False时，src, dst皆为软连接，可以复制软连接权限，如果设置为True，则当成普通文件复制权限。默认为True。Python3新增参数

```python
improt shutil,os
shutil.copy("file.txt","file_copy.txt")
# 或者
shutil.copy("file.txt",os.path.join(os.getcwd(),"copy"))
```

**copy2(src, dst)**： 将文件src复制至dst。dst可以是个目录，会在该目录下创建与src同名的文件，若该目录下存在同名文件，将会报错提示已经存在同名文件。权限、上次访问时间、上次修改时间和src的标志会一并复制至dst。本质是先后调用了copyfile与copystat方法而已

- src：源文件路径
- dst：复制至dst文件夹或文件
- follow_symlinks：设置为False时，src, dst皆为软连接，可以复制软连接权限、上次访问时间，上次修改时间以及src的标志，如果设置为True，则当成普通文件复制权限。默认为True。Python3新增参数

```python
improt shutil,os
shutil.copy2("file.txt","file_copy.txt")
# 或者
shutil.copy2("file.txt",os.path.join(os.getcwd(),"copy"))
```



**ignore_patterns(\*patterns)**： 忽略模式，用于配合`copytree()`方法，传递文件将会被忽略，不会被拷贝

- patterns：文件名称，元组



**copytree(src, dst, symlinks=False, ignore=None)**： 拷贝文档树，将src文件夹里的所有内容拷贝至dst文件夹

- src：源文件夹
- dst：复制至dst文件夹，该文件夹会自动创建，需保证此文件夹不存在，否则将报错
- symlinks：是否复制软连接，True复制软连接，False不复制，软连接会被当成文件复制过来，默认False
- ignore：忽略模式，可传入`ignore_patterns()`
- copy_function：拷贝文件的方式，可以传入一个可执行的处理函数，默认为copy2，Python3新增参数
- ignore_dangling_symlinks：sysmlinks设置为False时，拷贝指向文件已删除的软连接时，将会报错，如果想消除这个异常，可以设置此值为True。默认为False,Python3新增参数

```python
import shutil,os
folder1 = os.path.join(os.getcwd(),"aaa")
# bbb与ccc文件夹都可以不存在,会自动创建
folder2 = os.path.join(os.getcwd(),"bbb","ccc")
# 将"abc.txt","bcd.txt"忽略，不复制
shutil.copytree(folder1,folder2,ignore=shutil.ignore_patterns("abc.txt","bcd.tx
```

**rmtree(path, ignore_errors=False, onerror=None)**： 移除文档树，将文件夹目录删除

- ignore_errors：是否忽略错误，默认False
- onerror：定义错误处理函数，需传递一个可执行的处理函数，该处理函数接收三个参数：函数、路径和excinfo

```python
import shutil,os
folder1 = os.path.join(os.getcwd(),"aaa")
shutil.rmtree(folder1)
```

**move(src, dst)**： 将src移动至dst目录下。若dst目录不存在，则效果等同于src改名为dst。若dst目录存在，将会把src文件夹的所有内容移动至该目录下面

- src：源文件夹或文件
- dst：移动至dst文件夹，或将文件改名为dst文件。如果src为文件夹，而dst为文件将会报错
- copy_function：拷贝文件的方式，可以传入一个可执行的处理函数。默认为copy2，Python3新增参数

```python
import shutil,os
# 示例一，将src文件夹移动至dst文件夹下面，如果bbb文件夹不存在，则变成了重命名操作
folder1 = os.path.join(os.getcwd(),"aaa")
folder2 = os.path.join(os.getcwd(),"bbb")
shutil.move(folder1, folder2)
# 示例二，将src文件移动至dst文件夹下面，如果bbb文件夹不存在，则变成了重命名操作
file1 = os.path.join(os.getcwd(),"aaa.txt")
folder2 = os.path.join(os.getcwd(),"bbb")
shutil.move(file1, folder2)
# 示例三，将src文件重命名为dst文件(dst文件存在，将会覆盖)
file1 = os.path.join(os.getcwd(),"aaa.txt")
file2 = os.path.join(os.getcwd(),"bbb.txt")
shutil.move(file1, file2)
```

**disk_usage(path)**： 获取当前目录所在硬盘使用情况。Python3新增方法

- path：文件夹或文件路径。windows中必须是文件夹路径，在linux中可以是文件路径和文件夹路径

```python
import shutil.os
path = os.path.join(os.getcwd(),"aaa")
info = shutil.disk_usage(path)
print(info)   # usage(total=95089164288, used=7953104896, free=87136059392)
```

**chown(path, user=None, group=None)**： 修改路径指向的文件或文件夹的所有者或分组。Python3新增方法

- path：路径
- user：所有者，传递user的值必须是真实的，否则将报错no such user
- group：分组，传递group的值必须是真实的，否则将报错no such group

```python
import shutil,os
path = os.path.join(os.getcwd(),"file.txt")
shutil.chown(path,user="root",group="root")
```

**which(cmd, mode=os.F_OK | os.X_OK, path=None)**： 获取给定的cmd命令的可执行文件的路径。Python3新增方法

```python
import shutil
info = shutil.which("python3")
print(info)   # /usr/bin/python3
```

### **归档操作**



shutil还提供了创建和读取压缩和存档文件的高级使用程序。内部实现主要依靠的是zipfile和tarfile模块

**make_archive(base_name, format, root_dir, …)**： 生成压缩文件

- base_name：压缩文件的文件名，不允许有扩展名，因为会根据压缩格式生成相应的扩展名
- format：压缩格式
- root_dir：将制定文件夹进行压缩

```python
import shutil,os
base_name = os.path.join(os.getcwd(),"aaa")
format = "zip"
root_dir = os.path.join(os.getcwd(),"aaa")
# 将会root_dir文件夹下的内容进行压缩，生成一个aaa.zip文件
shutil.make_archive(base_name, format, root_dir)
```

**get_archive_formats()**： 获取支持的压缩文件格式。目前支持的有：tar、zip、gztar、bztar。在Python3还多支持一种格式xztar

**unpack_archive(filename, extract_dir=None, format=None)**： 解压操作。Python3新增方法

- filename：文件路径
- extract_dir：解压至的文件夹路径。文件夹可以不存在，会自动生成
- format：解压格式，默认为None，会根据扩展名自动选择解压格式

```python
import shutil,os
zip_path = os.path.join(os.getcwd(),"aaa.zip")
extract_dir = os.path.join(os.getcwd(),"aaa")
shutil.unpack_archive(zip_path, extract_dir)
```

**get_unpack_formats()**： 获取支持的解压文件格式。目前支持的有：tar、zip、gztar、bztar和xztar。Python3新增方法













### **归档操作**















# ⽂件基础操作

[Python文件操作详解 - 知行流浪 - CSDN博客](https://blog.csdn.net/zengxiantao1994/article/details/53784924)

[Python文件与目录操作_专题_脚本之家](https://www.jb51.net/Special/516.htm)
[Python文本文件操作技巧_专题_脚本之家](https://www.jb51.net/Special/672.htm)

[用python实现的去除win下文本文件头部BOM的代码_python_脚本之家](https://www.jb51.net/article/33999.htm)
[python文件读写操作与linux shell变量命令交互执行的方法_python_脚本之家](https://www.jb51.net/article/59857.htm)

[在Python中操作文件之truncate()方法的使用教程_python_脚本之家](https://www.jb51.net/article/66636.htm)
[python文件操作之目录遍历实例分析_python_脚本之家](https://www.jb51.net/article/66401.htm)

[Python遍历目录的4种方法实例介绍_python_脚本之家](https://www.jb51.net/article/63965.htm)

## ⽂件简介

⽂件包括 ⽂本文件和⼆进制文件（声⾳，图像，视频) 从存储⽅式来说，⽂件在磁盘上的存储方式都是二进制形式，所以，文本⽂件其实也应该算二进制文件。先从他们的区别来说，虽然都是二进制⽂件，但是二进制代表的意思不一样。打个比方，⼀个人，我们可以叫他的大名，以叫他的小名，但其实都是代表这个人。
二进制读写是将<font color='orange'>内存里面的数据</font>直接读写⼊文本中，
⽽⽂本，则是将<font color='red'>内存的数据先转换成了字符串</font>，再写⼊到文本中。

## 打开和关闭文件

### open 函数

先用Python内置的<font color='red'>open()函数打开一个文件，创建一个file对象</font>，相关的方法才可以调用它进行读写。语法：

`file object = open(file_name [, access_mode][, buffering])`

| file_name   | file_name变量是一个包含了你要访问的文件名称的字符串值。      |
| ----------- | ------------------------------------------------------------ |
| access_mode | access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。 |
| buffering   | 如果buffering的值被设为0，就不会有寄存。<br>如果buffering的值取1，访问文件时会寄存行。<br>如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。<br>如果取负值，寄存区的缓冲大小则为系统默认。 |

|                    模式                    |                             描述                             |
| :----------------------------------------: | :----------------------------------------------------------: |
|                     r                      | 以只读⽅式打开⽂件。⽂件的指针将会放在⽂件的开头。这是默认模式 |
|                     rb                     | 以⼆进制格式打开⼀个⽂件⽤于只读。⽂件指针将会放在⽂件的开头。 |
|                     r+                     | 打开⼀个⽂件⽤于读写。⽂件指针将会放在⽂件的开头。 r+:可读可写的操作，覆盖的形式写入   源内容:ABC 以r+模式写入:DE 得到的文件内容:DEC |
|                    rb+                     | 以⼆进制格式打开⼀个⽂件⽤于读写(具体见r+)。⽂件指针将会放在⽂件的开头。 |
|                     w                      | 打开⼀个⽂件只⽤于写⼊。如果该⽂件已存在则开⽂件，并从开头开始编辑 输入:f.write(‘abc’);f.write(‘DEF’) 输出:abcDEF |
| 容会被删除。如果该⽂件不存在，创建新⽂件。 |                                                              |
|                     wb                     | 以⼆进制格式打开⼀个⽂件只⽤于写⼊。如果该⽂件已存在则打开⽂件，并从开头开始编辑，即原有内容会被删除。如果该⽂件不存在，创建新⽂件。 |
|                     w+                     | 打开⼀个⽂件⽤于读写。如果该⽂件已存在则打开⽂件，并从开头开始编辑，即原有内容会被删除。如果该⽂件不存在，创建新⽂件。 |
|                    wb+                     | 以⼆进制格式打开⼀个⽂件⽤于读写。如果该⽂件已存在则打开⽂件，并从开头开始编辑，即原有内容会被删除。如果该⽂件不存在，创建新⽂件。 |
|                     a                      | 打开⼀个⽂件⽤于追加。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。也就是说，新的内容将会被写⼊到已有内容之后。如果该⽂件不存在，创建新⽂件进⾏写⼊。 |
|                     ab                     | 以⼆进制格式打开⼀个⽂件⽤于追加。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。也就是说，新的内容将会被写⼊到已有内容之后。如果该⽂件不存在，创建新⽂件进行写⼊。 |
|                     a+                     | 打开⼀个⽂件⽤于读写。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。⽂件打开时会是追加模式。如果该⽂件不存在，创建新⽂件⽤于读写。 |
|                    ab+                     | 以⼆进制格式打开⼀个⽂件⽤于追加。如果该⽂件已存在，⽂件指针将会放在⽂件的结尾。如果该⽂件不存在，创建新⽂件⽤于读写。 |



### File对象的属性

[Python3文件方法 - Python3教程™](https://www.yiibai.com/python3/file_methods.html)

<font color='red'>一个文件被打开后，你有一个file对象</font>，你可以得到有关该文件的各种信息。以下是和file对象相关的所有属性的列表：

| file方法                                                     | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| file.close()                                                 | 关闭文件。一个关闭的文件无法读取或写入任何东西。             |
| file.closed                                                  | 返回true如果文件已被关闭，否则返回false。                    |
| file.mode                                                    | 返回被打开文件的访问模式。                                   |
| file.name                                                    | 返回文件的名称。                                             |
| file.flush()                                                 | 刷新内部缓存，像标准输入fflush。这可能是一些类文件对象的一个空操作。 |
| file.fileno()                                                | 返回所使用的底层实现，从操作系统I/O操作的整数文件描述符。    |
| file.isatty()                                                | 如果文件被连接到一个tty(状)装置则返回True，否则返回False。   |
| next(file)                                                   | 返回每次被调用时文件中的下一行。                             |
| ==file.read([size])==                                        | 被传递的参数是要从已打开文件中读取的字节计数。<br>该方法从文件的开头开始读入，如果没有传入count，它会尝试尽可能多地读取更多的内容，很可能是直到文件的末尾。<br>read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。 |
| ==file.readline([size])==                                    | f.readline() 会从文件中读取单独的一行。<br>换行符为 '\n'。<br>f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。 |
| ==file.readlines([sizehint])==                               | f.readlines() 将以列表的形式返回该文件中包含的所有行，列表中的一项表示文件的一行。<br>如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。 |
| file.seek(offset[,whence])                                   | seek（offset [,from]）方法改变当前文件的位置。<br/>Offset变量表示要移动的字节数。<br/>From变量指定开始移动字节的参考位置。<br/>如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。<br/>如果设为1，则使用当前的位置作为参考位置。<br/>如果它被设为2，那么该文件的末尾将作为参考位置。 |
| [file.tell()](http://www.yiibai.com/python3/file_tell.html)  | 返回文件的当前位置                                           |
| file.truncate([size])                                        | 截断文件的大小。 如果size参数存在，则文件被截断为(至多)该尺寸。 |
| ==[file.write(str)](http://www.yiibai.com/python3/file_write.html)== | 将一个字符串写入该文件。没有返回值。                         |
| ==file.writelines(sequence)==                                | 写入字符串序列到文件。该序列可以是一个迭代对象的字符串 - 典型字符串列表。 |



## 文件的读写操作

- 要以读⽂件的模式打开⼀个⽂件对象，使⽤Python内置的open() 函数，传⼊⽂件名和标示符：
```python
#  打开文件
f = open('/Users/michael/test.txt', 'r')
#  读取
f.read()
'Hello, world!'
#  关闭
f.close()
````
如果⽂件不存在， open() 函数就会抛出⼀个IOError 的错误
由于⽂件读写时都有可能产⽣IOError ，一旦出错，后面的f.close() 就不会调⽤。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使⽤try ... finally 来实现：

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

```python

# f=open(‘1.txt’)
# # 读取或者写入
# f.close()

'''
r : 只读，文件如果不存在就会报错
w : 只写，会将原来的数据清空，在写入，如果文件不存在，会创建一个新的文件
a : 追加写入

rb: 以二进制形式读取文件
wb：以二进制形式写入文件
ab ：以二进制形式追加写入文件

r+:可读可写的操作，覆盖的形势写入  源内容:ABC 以r+模式写入:DE 得到的文件内容:DEC
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
# 1.txt
abc哈哈
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
# 1.txt
abc哈哈
```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# rb二进制形式读取数据
# 只要出现b,就不需要是encoding='utf-8'
file = open('1.txt','rb')

content = file.read()
print(content) # b'abc\xe5\x93\x88\xe5\x93\x88'

# 将二进制数据进行utf-8解码操作
result = content.decode('utf-8')
print(result)---> abc哈哈

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
>>> abc哈
file.close()


```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

file = open('1.txt','rb')

print(file.read(4))# 如果是rb这种方式，是以字节的个数为量值
>>> b'abc\xe5'
file.close()

```

## 字符编码
要读取⾮UTF-8编码的⽂本⽂件，需要给open() 函数传⼊encoding 参数，例如，读取GBK编码的⽂件：
```python
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'
​```python
遇到有些编码不规范的⽂件，你可能会遇到UnicodeDecodeError ，因为在⽂本⽂件中可能夹杂了⼀些⾮法编码的字符。遇到这种情况， open() 函数还接收⼀个errors 参数，表示如果遇到编码错误后如何处理。最简单的⽅式是直接忽略：
```
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk',errors='ignore')
```python
## 写⽂件  open()函数读写二进制文件,不需要encoding可选参数
写⽂件和读⽂件是⼀样的，唯⼀区别是调⽤open() 函数时，传⼊标识符'w' 或者'wb' 表示写⽂本⽂件或写⼆进制⽂件：

​```python
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
```

```python
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
```
---
---
## 爬去百度和妹子图网站的案例

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
#百度图片
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
```python
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
# 妹子图片
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

[(Back to 面向过程编程)](#面向过程编程)

[(Back to 面向对象编程)](#⾯向对象编程)

[Working with Jupyter Notebooks in Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support)

[Matplotlib: Python plotting — Matplotlib 3.1.1 documentation](https://matplotlib.org/)
什么是Matplotlib
:   Matplotlib是⼀个Python 2D绘图库，它可以在各种平台上以各种硬拷⻉格式和交互式环境⽣成出具有出版品质的图形。
Matplotlib试图让简单的事情变得更简单，让⽆法实现的事情变得可能实现。 只需⼏行代码即可⽣成绘图，直⽅图，功率谱，条形图，错误图，散点图等。

## 常⻅图形种类及意义

折线图 plot
:   以折线的上升或下降来表示统计数量的增减变化的统计图

特点
:   能够显示数据的变化趋势，反映事物的变化情况。(变化)

## Matplotlib画图的简单实现

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 导⼊模块
import matplotlib.pyplot as plt
# 在jupyter中执⾏的时候显示图⽚
# %matplotlib inline
# 传⼊x和y, 通过plot画图
plt.plot([1, 0, 9], [4, 5, 6])
# 在执⾏程序的时候展示图形
plt.show()
```


## 对Matplotlib图像结构的认识

![matplotlib图像结构的认识](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/matplotlib图像结构的认识.bmp "matplotlib图像结构的认识")

在 Matplotlib 中可以为图形添加多个轴域，具体而言，就是使用 pyplot 来创建多个轴域并改变其形状。

| Figure | Axes | Grid | Line     | Markers        | x,y axis label<br>x_ticks_label<br>y_ticks_label | x,y ticks<br>x_ticks<br>y_ticks  |
| ------ | ---- | ---- | -------- | -------------- | ------------------------------------------------ | -------------------------------- |
| 图形   | 轴域 | 网格 | 绘制的线 | 线折点上的标记 | x,y轴的刻度标签                                  | x,y轴刻度                        |
|        |      |      | Legend   | Title          | Major tick label                                 | Major tick<br>Minor tick         |
|        |      |      | 图例标注 | 整个图的标题   | 主线上刻度的标签                                 | 主线上的刻度<br>主线之间的小刻度 |



![FigureAxesAxis](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/FigureAxesAxis.webp '轴线-复数Axes轴域单数Axis轴-FigureAxesAxis.webp')

![matplotlib绘图](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/matplotlib绘图.bmp "matplotlib绘图")

## 绘制图像的常见步骤 

大多数时候，使用 Matplotlib 绘制数据的流程是类似的，虽然有些特殊的图像绘制需要一下特殊的操作，但大体流程都相似

- \1. 通过 Pandas 将要绘制图像的数据读入，如 pd.readcsv () 读入 csv 文件数据、pd.readexcel () 读取 Excel 文件数据
- \2. 导入 Matplotlib , 具体为: import matplotlib.pyplot as plt
- \3. 使用 plt.plot () 绘制折线图，不同的图使用不同的绘图函数，所有的绘图函数都需要传入相应的数据
- \4. 使用 plt.xlabel 与 plt.ylabel 定义 x 轴与 y 轴的标签，如定义标签字体样式、字体大小、字段位置等，如果不使用，Matplotlib 就会使用默认的样式将要显示的内容在标签处显示。需要注意的是，默认的样式是不支持显示中文的，如果此时你的标签要显示的内容是中文，那么 Matplotlib 生成的图像中，标签位置对应的内容会成为一个空方块，要显示中文，需要指定字体。
- \5. 使用 plt.xticks 与 plt.yticks 定义 x 轴与 y 轴上的标记点(刻度locations)，如定义标点的间隔, `xticks(locs, [labels], **kwargs) ` # Set locations and labels
- \6. 使用 plt.legend () 标注，如折线图中有 3 条不同颜色的折线，通过 legend () 方法就可以标注出不同折线的含义
- \7. 使用 plt.title () 定义图中的标题
- \8. 使用 plt.show () 将最终的图像展示出来。



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
![折线图的绘制](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/折线图的绘制.png '折线图的绘制')

### 折线的颜⾊和形状设置

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ####hide  代码隐藏

from matplotlib import pyplot as plt
x = range(1,8) ## x轴的位置
y = [17, 17, 18, 15, 11, 11, 13]
## 传⼊x和y, 通过plot画折线图
plt.plot(x, y, color='red',alpha=0.5,linestyle='--',linewidth=3)
plt.show()
'''基础属性设置
color='red' : 折线的颜⾊
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
![折线的颜⾊和形状设置](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/折线的颜⾊和形状设置.png '折线的颜⾊和形状设置')

### 折点样式

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ####hide  代码隐藏

from matplotlib import pyplot as plt
x = range(1,8) ## x轴的位置
y = [17, 17, 18, 15, 11, 11, 13]
## 传⼊x和y, 通过plot画折线图
plt.plot(x, y, marker='*')
plt.show()
```

![折点样式](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/折点样式.png '折点样式')

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
![线条所有样式设置](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/线条所有样式设置.png '线条所有样式设置')

### 设置的图⽚的⼤小和保存

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
from 包/模块 import 函数(方法)/变量(属性)
from matplotlib import pyplot as plt
import 包/模块
import random
x = range(2,26,2) # x轴的位置
y = [random.randint(15, 30) for i in x]
# 设置图⽚的大⼩
'''
figsize:指定figure的宽和⾼，单位为英⼨；
dpi参数指定绘图对象的分辨率，即每英⼨多少个像素，缺省值为80 1英⼨等于2.5cm,A4纸是
21*30cm的纸张
'''
# 根据画布对象
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y) # 传⼊x和y, 通过plot画图
plt.show()
# 保存(注意： 要放在绘制的下面,并且plt.show()会释放figure资源，如果在显示图像之后保存图⽚将只能保存空图⽚。)
plt.savefig('./t1.png')
# 图⽚的格式也可以保存为svg这种⽮量图格式，这种⽮量图放在⽹⻚页中放大后不会有锯⻮
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
# plt.xticks(x_ticks刻度int的列表,x_ticks_label标签str的列表,rotation=45)
plt.xticks(x,x_ticks_label,rotation=45)

# 设置一下y轴
y_ticks_label = ["{}°C".format(i) for i in range(min(y),max(y)+1)]
plt.yticks(range(min(y),max(y)+1),y_ticks_label)


plt.plot(x,y)
plt.show()
```
![绘制x轴和y轴的刻度](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/绘制x轴和y轴的刻度.png '绘制x轴和y轴的刻度')

### 设置显示中⽂

#### 标题、标签设置中文

- matplotlib只显示英⽂,⽆法显示中⽂，需要修改matplotlib的默认字体
- 通过matplotlib下的font_manager可以解决
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
设置字体属性默认参数的键不同fontproperties/prop
标题、标签设置中文 fontproperties
	# plt.title('每分钟跳动次数',color='orange',fontproperties=my_font)
    # plt.xlabel('时间',fontproperties=my_font,rotation=45)
图例设置中文  prop
    # plt.legend(prop=my_font,loc='upper left')

    
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
'查看Linux、Mac下⽀持的字体'
# 终端执⾏： fc-list
# 查看⽀持的中⽂（冒号前面有空格) fc-list :lang=zh
'查看Windows下的字体：“C:\Windows\Fonts” '
# 可以⾃⼰下载字体⽂件（xxx.ttf），然后双击安装即可
# my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=18)
# my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\SIMYOU.TTF',size=18)
my_font = font_manager.FontProperties(fname='/usr/share/fonts/wps-office/Fonts/微软雅黑/msyh.ttc',size=18)

# my_font1 = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=20)
# 设置图片标题
plt.title('每分钟跳动次数',color='orange',fontproperties=my_font)

# X轴的标题
plt.xlabel('时间',fontproperties=my_font,rotation=45)
# Y轴的标题
plt.ylabel('次数',fontproperties=my_font)
plt.show()


```
![标题、标签设置中文](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/标题、标签设置中文.png '标题、标签设置中文')

#### 图例设置中文

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
设置字体属性默认参数的键不同fontproperties/prop
标题、标签设置中文 fontproperties
	# plt.title('每分钟跳动次数',color='orange',fontproperties=my_font)
    # plt.xlabel('时间',fontproperties=my_font,rotation=45)
图例设置中文  prop
    # plt.legend(prop=my_font,loc='upper left')

from matplotlib import font_manager

y1 = [1,0,1,1,2,4,3,4,4,5,6,5,4,3,3,1,1,1,1,1]
y2 = [1,0,3,1,2,2,3,4,3,2,1,2,1,1,1,1,1,1,1,1]

x = range(11,31)
# 设置图形
plt.figure(figsize=(20,8),dpi=80)
# my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=18)
#my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=18)

fname='/usr/share/fonts/wps-office/Fonts/微软雅黑/msyh.ttc'
my_font = font_manager.FontProperties(fname=fname,size=18)

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

<img src="图例设置中文.png" alt="图例设置中文" title="图例设置中文" style="zoom:67%;" />

### ⼀图多线


```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 假设大家在30岁的时候，根据⾃⼰的实际情况，统计出来你和你同事各⾃从11岁到30岁每年年交的男/⼥女女朋友的数量如列表y1和y2，请在⼀个图中绘制出该数据的折线图，从⽽分析每年年交朋友的数量⾛走势。
from matplotlib import font_manager
y1 = [1,0,1,1,2,4,3,4,4,5,6,5,4,3,3,1,1,1,1,1]
y2 = [1,0,3,1,2,2,3,4,3,2,1,2,1,1,1,1,1,1,1,1]
x = range(11,31)
# 设置图形
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y1,color='red',label='⾃⼰')
plt.plot(x,y2,color='blue',label='同事')
# 设置x轴刻度
xtick_labels = ['{}岁'.format(i) for i in x]
#my_font =font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=18)
fname='/usr/share/fonts/wps-office/Fonts/微软雅黑/msyh.ttc'
my_font = font_manager.FontProperties(fname=fname,size=18)

plt.xticks(x,xtick_labels,fontproperties=my_font,rotation=45)
# 绘制⽹格（⽹格也是可以设置线的样式)
#alpha=0.4 设置透明度
plt.show()
```

<img src="图例设置中文.png" alt="图例设置中文" title="图例设置中文" style="zoom:67%;" />

###  ⼀图多个坐标系⼦图

[labels title用法 子图的pyplot轴标签 - Code Examples](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/https://code-examples.net/zh-CN/q/6a3f5b)

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# add_subplot⽅法----给figure新增⼦图
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1, 100)
#新建figure对象
fig=plt.figure(figsize=(20,10),dpi=80)
#新建⼦图1
ax1=fig.add_subplot(2,2,1)
ax1.plot(x, x)
#新建⼦图2
ax2=fig.add_subplot(2,2,2)
ax2.plot(x, x ** 2)
ax2.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
#新建⼦图3
ax3=fig.add_subplot(2,2,3)
ax3.plot(x, np.log(x))
plt.show()

```
![⼀图多个坐标系⼦图](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/⼀图多个坐标系⼦图.png "⼀图多个坐标系⼦图")

### 图中图

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
from matplotlib import pyplot as plt
# 定义画布大小
fig = plt.figure(figsize=(20,8))
# 多个轴域进行作图
ax1 = fig.add_axes([0,0,1,1]) # 添加轴域
ax2 = fig.add_axes([0.05,0.65,0.5,0.3]) # 添加轴域
# 设置标题
ax1.set_title('axes1',fontdict={'fontsize':20})
# 第一个轴域进行绘图
ax1.plot(range(5),[x**2 for x in range(5)],
        color='red')
# 设置标题
ax2.set_title('axes2',fontdict={'fontsize':20})
# 第二个轴域进行绘图
ax2.plot(range(10),[-x**2 for x in range(10)],
        color='green')
plt.show()
```

<img src="图中图.png" alt="图中图" title="图中图" style="zoom:67%;" />

### 设置坐标轴范围

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
import matplotlib.pyplot as plt
import numpy as np
x= np.arange(-10,11,1)
y = x**2
plt.plot(x,y)
# 可以调x轴的左右两边
# plt.xlim([-5,5])
# 只调⼀边
# plt.xlim(xmin=-4)
# plt.xlim(xmax=4)
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.show()

```

<img src="设置坐标轴范围.png" alt="设置坐标轴范围" title="设置坐标轴范围"  />

###  改变坐标轴的默认显示⽅式

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

![改变坐标轴spines的默认显示⽅式](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/改变坐标轴spines的默认显示⽅式.png '改变坐标轴spines的默认显示⽅式')

## 绘制散点图

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

'''题⼲
3⽉月份每天最⾼⽓温
a =
[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,2
2,22,22,23]
'''
from matplotlib import pyplot as plt
from matplotlib import font_manager

y = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
x = range(1,32)

# 设置图形大⼩
plt.figure(figsize=(20,8),dpi=80)
# 使⽤scatter绘制散点图
plt.scatter(x,y,label= '3月份')
# plt.plot()

#my_font =font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=10)

fname='/usr/share/fonts/wps-office/Fonts/微软雅黑/msyh.ttc'
my_font = font_manager.FontProperties(fname=fname,size=18)
# 调整x轴的刻度
x_ticks_labels = ['3月{}日'.format(i) for i in x]
plt.xticks(x[::3],x_ticks_labels[::3],fontproperties=my_font,rotation=45)
plt.xlabel('⽇期',fontproperties=my_font)
plt.ylabel('温度',fontproperties=my_font)
# 图例
plt.legend(prop=my_font)
plt.show()

```

![散点图scatter](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/散点图scatter.png '散点图scatter')

## 绘制条形图

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
'''http://58921.com/alltime
假设你获取到了2019年年内地电影票房前20的电影（列表a)和电影票房数据（列表b)，请展示该数据
a = ['流浪地球','疯狂的外星⼈人','⻜飞驰⼈人⽣','大⻩黄蜂','熊出没·原始时代','新喜剧之王']
b = ['38.13','19.85','14.89','11.36','6.47','5.93']
'''

from matplotlib import pyplot as plt
from matplotlib import font_manager
a = ['流浪地球','疯狂的外星⼈人','⻜飞驰⼈人⽣','大⻩黄蜂','熊出没·原始时代','新喜剧之王']
b = ['38.13','19.85','14.89','11.36','6.47','5.93']
# b =[38.13,19.85,14.89,11.36,6.47,5.93]
#my_font =font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=10)
fname='/usr/share/fonts/wps-office/Fonts/微软雅黑/msyh.ttc'
my_font = font_manager.FontProperties(fname=fname,size=18)
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
![条形图bar](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/条形图bar.png '条形图bar')

## 横向条形图


```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
'''http://58921.com/alltime
假设你获取到了2019年年内地电影票房前20的电影（列表a)和电影票房数据（列表b)，请展示该数据
a = ['流浪地球','疯狂的外星⼈人','⻜飞驰⼈人⽣','大⻩黄蜂','熊出没·原始时代','新喜剧之王']
b = ['38.13','19.85','14.89','11.36','6.47','5.93']
'''
# 横向柱状图
from matplotlib import pyplot as plt
from matplotlib import font_manager
a = ['流浪地球','疯狂的外星⼈人','⻜飞驰⼈人⽣','大⻩黄蜂','熊出没·原始时代','新喜剧之王']
b = ['38.13','19.85','14.89','11.36','6.47','5.93']
# b =[38.13,19.85,14.89,11.36,6.47,5.93]
#my_font =font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=10)
fname='/usr/share/fonts/wps-office/Fonts/微软雅黑/msyh.ttc'
my_font = font_manager.FontProperties(fname=fname,size=18)

plt.figure(figsize=(20,8),dpi=80)
# 绘制条形图的⽅法
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

![横向条形图barh](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/横向条形图barh.png '横向条形图barh')

## 并列和罗列条形图

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

import matplotlib.pyplot as plt
import numpy as np
index = np.arange(4)
BJ = [50,55,53,60]
Sh = [44,66,55,41]
# 并列
# plt.bar(x坐标列表，y坐标列表，条形宽度)
plt.bar(index,BJ,width=0.3)
plt.bar(index+0.3,Sh,width=0.3,color='green')
plt.xticks(index+0.3/2,index)
# 罗列
# plt.bar(x坐标列表，y坐标列表，条形底部值，条形宽度)
plt.bar(index,Sh,bottom=BJ,width=0.3,color='green')
plt.show()
```

![并列和罗列条形图bar](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/并列和罗列条形图bar.png '并列和罗列条形图bar')

## 直⽅图

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

'''
现有250部电影的时⻓长，希望统计出这些电影时⻓长的分布状态(⽐如时⻓长为100分钟到120分钟电影的数量，
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
#my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=10)
fname='/usr/share/fonts/wps-office/Fonts/微软雅黑/msyh.ttc'
my_font = font_manager.FontProperties(fname=fname,size=18)

# 2）创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 3）绘制直⽅图
# 设置组距
distance = 2
# 计算组数
group_num = int((max(time) - min(time)) / distance)
# 绘制直⽅图
plt.hist(time, bins=group_num)
# 修改x轴刻度显示
plt.xticks(range(min(time), max(time))[::2])
# 添加⽹格显示
plt.grid(linestyle="--", alpha=0.5)
# 添加x, y轴描述信息
plt.xlabel("电影时长⼤小",fontproperties=my_font)
plt.ylabel("电影的数据量",fontproperties=my_font)
# 4）显示图像
plt.show()

```

![直⽅图hist](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/直⽅图hist.png '直⽅图hist')

## 饼状图

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
#my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc',size=10)
fname='/usr/share/fonts/wps-office/Fonts/微软雅黑/msyh.ttc'
my_font = font_manager.FontProperties(fname=fname,size=18)

label_list = ["第一部分", "第二部分", "第三部分"] # 各部分标签
size = [55, 35, 10] # 各部分大⼩
color = ["red", "green", "blue"] # 各部分颜⾊
explode = [0, 0.05, 0] # 各部分突出值
"""
绘制饼图
explode：设置各部分突出
label:设置各部分标签
labeldistance:设置标签⽂本距圆⼼心位置，1.1表示1.1倍半径
autopct：设置圆⾥面⽂本
shadow：设置是否有阴影
startangle：起始⻆角度，默认从0开始逆时针转
pctdistance：设置圆内⽂本距圆⼼心距离


返回值:
patches : matplotlib.patches.Wedge列表(扇形实例)
l_text：label matplotlib.text.Text列表(标签实例)
p_text：label matplotlib.text.Text列表(百分⽐标签实例)
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

# l_text：label matplotlib.text.Text列表(标签实例)
for t in l_text:
    # print(dir(t))
    t.set_fontproperties(my_font)
# p_text：label matplotlib.text.Text列表(百分⽐标签实例)
for i,t in enumerate(p_text):
    t.set_size(30)
    if i ==1:
        t.set_color('orange')
# patches : matplotlib.patches.Wedge列表(扇形实例)
for i in patches:
    i.set_color('pink')
    break
plt.legend(prop=my_font)
plt.show()


```

![饼状图pie](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/饼状图pie.png '饼状图pie')

---


```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  id='utf-8' continue:true output='text' } ##hide  代码隐藏
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib.font_manager

```


# NumPy
[(Back to 面向过程编程)](#面向过程编程)

[(Back to 面向对象编程)](#⾯向对象编程)

[NumPy中文官网](https://www.numpy.org.cn/)
NumPy（Numerical Python）是一个开源的Python科学计算库，用于快速处理任意维度的数组。
NumPy支持常见的数组和矩阵操作。对于同样的数值计算任务，使用Numpy比直接使用Python要简洁
的多。
NumPy使用ndarray对象来处理多维数组，该对象是一个快速而灵活的大数据容器。

Numpy 是 Python 中用于数据分析、机器学习与科学计算的知名第三方库，它是 Python 中很多科学计算库的依赖包，如 sickit-learn、SciPy、Pandas 等

## NumPy的优势
- 对于同样的数值计算任务，使用NumPy要比直接编写Python代码便捷得多；
- NumPy中的数组的存储效率和输入输出性能均远远优于Python中等价的基本数据结构，且其能够
提升的性能是与数组中的元素成比例的；
- NumPy的大部分代码都是用C语言写的，其底层算法在设计时就有着优异的性能，这使得NumPy
比纯Python代码高效得多
### ndarray与Python原生list运算效率对比

![Numpy_structure](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/Numpy_structure.png "Numpy_structure")


```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

import random
import time
import numpy as np
 #测试Python执行时间
a = []
for i in range(100000000):
    a.append(random.random())
t1 = time.time()
sum1=sum(a)
t2=time.time()
# 测试numpy执行时间
b=np.array(a)
t4=time.time()
sum3=np.sum(b)
t5=time.time()
print(t2-t1, t5-t4)
0.610687255859375 0.16196393966674805
```
## NumPy 的Ndarray 对象
NumPy 最重要的一个特点是其 <font color="orange" >N 维</font>数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。ndarray 对象是用于<font color="orange" >存放同类型元素</font>的多维数组。
- 几个中括号<font color="orange" size=10>[</font>几维数组
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
import numpy as np
print('一维数组')
# list 转换成了 Numpy 中定义的 numpy.ndarray 类型
print(np.array([1,2,3,4,5],dtype='int8'))
'''
 [1 2 3]
 '''
print('二维数组')
print(np.array([[1,2,3],[4,5,6]],dtype=int))
'''
[[1 2 3]
 [4 5 6]]
'''
print('三维数组')
c = np.array([[[1, 2, 3],[1, 2, 3],[1, 2, 3]],[[1, 2, 3],[1, 2, 3],[1, 2, 3]],[[1, 2, 3],[1, 2, 3],[1, 2, 3]]])
print(c)
'''
[[[1 2 3]
  [1 2 3]
  [1 2 3]]

 [[1 2 3]
  [1 2 3]
  [1 2 3]]

 [[1 2 3]
  [1 2 3]
  [1 2 3]]]
'''
```

![Numpy三维数组的轴](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/Numpy三维数组的轴.png "Numpy三维数组的轴")

```python
axis=1是的运算
↓→
↓→
↓→
axis=0的运算
→ → → →
 ↓ ↓ ↓ ↓
```



### 创建一维数组

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
import numpy as np
list1 = [1,2,3,4]
oneArray = np.array(list1)
print(type(oneArray))
print(oneArray)
# 创建数组的多种形式
print('创建数组的多种形式')
# 1. 直接传入列表的方式
t1 = np.array([1,2,3])
print(t1)
print(type(t1))
'''
[1 2 3]
<class 'numpy.ndarray'>
'''
# 2. 传入range生成序列
t2 = np.array(range(10))
print(t2)
print(type(t2))
'''
[0 1 2 3 4 5 6 7 8 9]
<class 'numpy.ndarray'>
'''
# 3. 使用numpy自带的np.arange()生成数组
t3 = np.arange(0,10,2)
print(t3)
print(type(t3))
'''
[0 2 4 6 8]
<class 'numpy.ndarray'>
'''

```
### 创建二维数组

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

import numpy as np
list2 = [[1,2],[3,4],[5,6]]
twoArray = np.array(list2)
print(twoArray)
'''
[[1 2]
[3 4]
[5 6]]
'''

```

![创建二维数组](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/创建二维数组.png '创建二维数组')

![初始化数组onesZeros](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/初始化数组onesZeros.png '初始化数组onesZeros')

### 更多的维度

Numpy 可以创建任意维度的数组，这也是它的中心数据结构被称为 ndarray (n 维数组) 的原因。

创建方式类似，注意 list 的个数则可，<font color='orange' size=5>每一维对应着一个 list</font>

```python
np.array([ [[1,2],[3,4]],
		   [[5,6],[7,8]] ])
'''
array([[[1, 2],
        [3, 4]],

       [[5, 6],
        [7, 8]]])
'''
```

![三维数组222](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/三维数组222.png '三维数组222')

```python
np.ones((4,3,2))
'''
array([[[1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.]]])
'''
np.random.random((4,3,2))
'''
array([[[0.21262518, 0.66500693],
        [0.60590465, 0.92814057],
        [0.77847333, 0.01342307]],

       [[0.21397167, 0.48249745],
        [0.11794449, 0.66085362],
        [0.28495919, 0.60176893]],

       [[0.4428501 , 0.59052966],
        [0.15181462, 0.04649998],
        [0.26876344, 0.66480154]],

       [[0.99941113, 0.40857191],
        [0.37938112, 0.4343296 ],
        [0.93800699, 0.07120455]]])
'''
'''
np.ones((4,3,2))
如果我们打印多维数组，其打印的顺序与下面可视化显示的顺序是不同的，Numpy 会将最后一维优先打印出来
打印最后一维的2个元素，然后才是第二维的3个元素，最后才是第一维的4个元素
'''
```

![三维数组432](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/三维数组432.png '三维数组432')

### 常用属性

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
import numpy as np
list2 = [[1,2],[3,4],[5,6]]
twoArray = np.array(list2,dtype='int8')
# 获取数组的维度( 注意： 与函数的参数很像 list2[2:3]  function(*args,**kwargs))
print(twoArray.ndim)
'''2'''
# 形状（行，列）
print(twoArray.shape)
'''(3, 2)'''
# 有多少个元素
print(twoArray.size)
'''6'''
# 元素类型：'int8'
'''
在通过 list 创建 array 时，
如果没有指定 dtype (数组元素类型)， 那么就会以 list 中元素的类型而自动定义成对应的默认类型，
如果 list 中全为整型，则 dtype 默认为 int64，
如果 list 中存在浮点型，则 dtype 默认为 float64
'''
print(twoArray.dtype.name)
# 每个元素所占用的字节数目:1
print(twoArray.itemsize)


```

### 调整数组的形状

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='text'} ##hide  代码隐藏

four = np.array([[1,2,3],[4,5,6]])
print(id(four)) -->140601010855808
# 修改的是原有的
four.shape = (3,2)
print(id(four)) -->140601010855808
print(four)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
# 返回一个新的数组
four = four.reshape(3,2)
print(print(id(four))) -->140601010854368
print(four)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
# 将多维变成一维数组
five = four.reshape((6,),order='F')
print(five)
'''
[1 3 5 2 4 6]
'''
# 默认情况下‘C’以行为主的顺序展开，‘F’（Fortran风格）意味着以列的顺序展开
six = four.flatten(order='F')
print(six)
'''
[1 3 5 2 4 6]
'''
# 数组的形状
t = np.arange(24)
print(t)
print(t.shape)
'''
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
(24,)
'''
# 转换成二维
t1 = t.reshape((4,6))
print(t1)
print(t1.shape)
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]
(4, 6)
'''
# 转成三维
t2 = t.reshape((2,3,4))
print(t2)-->(2, 3, 4)
print(t2.shape)

'''
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
  '''
```
![数组形状重塑](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/数组形状重塑.png '数组形状重塑')

- ones () 方法会将数组元素全初始化为 1.，

- zeros () 与 random.random () 方法也都类似，
- 需注意，这 3 个方法生成的数组类型都为 float64

```python
n1 = np.ones(3)
print(n1)-->[1.,1.,1.]
n1.dtype-->dtype('float64')

n2=np.zeros(3)
print(n2)-->[0.,0.,0.]
n2.dtype-->dtype('float64')

n3 = np.random.random(3)
print(n3)-->[0.35102158 0.86681649 0.5869452 ]
```



### 将数组转成list

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 将数组转成list
a= np.array([9, 12, 88, 14, 25])
list_a = a.tolist()
print(list_a) -->[9, 12, 88, 14, 25]
print(type(list_a))--><class 'list'>

```


### NumPy的数据类型

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

f = np.array([1,2,3,4,5], dtype = np.int16)
# 返回数组中每个元素的字节单位长度
print(f.itemsize)
# 获取数据类型
print(f.dtype)
# 调整数据类型
f1 = f.astype(np.int64)
print(f1.dtype)
# 随机生成小数
# 使用python语法，保留两位
print(round(random.random(),2))-->0.53   # round圆整 向0截断
arr = np.array([random.random() for i in range(10)])
# 取小数点后两位
print(np.round(arr,2))
>>> [0.18 0.17 0.79 0.4  0.93 0.73 0.28 0.14 0.56 0.09]
```
- dtype是numpy.dtype类型，先看看对于数组来说都有哪些类型:
| 名称          | 描述                                              | 简写  |
| :------------ | :------------------------------------------------ | :---: |
| np.bool       | 用一个字节存储的布尔类型（True或False）           |  'b'  |
| np.int8       | 一个字节大小，-128 至 127 （一个字节）(2**7=128)  |  'i'  |
| np.int16      | 整数，-32768 至 32767 （2个字节）                 | 'i2'  |
| np.int32      | 整数，-2 31 至 2 32 -1 （4个字节）                | 'i4'  |
| np.int64      | 整数，-2 63 至 2 63 - 1 （8个字节）               | 'i8'  |
| np.uint8      | 无符号整数，0 至 255                              |  'u'  |
| np.uint16     | 无符号整数，0 至 65535                            | 'u2'  |
| np.uint32     | 无符号整数，0 至 2 ** 32 - 1                      | 'u4'  |
| np.uint64     | 无符号整数，0 至 2 ** 64 - 1                      | 'u8'  |
| np.float16    | 半精度浮点数：16位，正负号1位，指数5位，精度10位  | 'f2'  |
| np.float32    | 单精度浮点数：32位，正负号1位，指数8位，精度23位  | 'f4'  |
| np.float64    | 双精度浮点数：64位，正负号1位，指数11位，精度52位 | 'f8'  |
| np.complex64  | 复数，分别用两个32位浮点数表示实部和虚部          | 'c8'  |
| np.complex128 | 复数，分别用两个64位浮点数表示实部和虚部          | 'c16' |
| np.object_    | python对象                                        |  'O'  |
| np.string_    | 字符串                                            |  'S'  |
| np.unicode_   | unicode类型                                       |  'U'  |

## 数组的计算

### 数组和数的计算

- 由于numpy的广播机机制在运算过程中，加减乘除的值被广播到所有的元素上面。
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

t1 = np.arange(24).reshape((6,4))
print(t1)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
'''
print(t1+2)
'''
[[ 2  3  4  5]
 [ 6  7  8  9]
 [10 11 12 13]
 [14 15 16 17]
 [18 19 20 21]
 [22 23 24 25]]
'''
print(t1*2)
print(t1/2)

```

- ### 数组与数组之间的操作
1. 同种形状的数组(对应位置进行计算操作)
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

t1 = np.arange(24).reshape((6,4))
t2 = np.arange(100,124).reshape((6,4))
print(t1+t2)
print(t1*t2)

```

![相同形状的矩阵进行运算](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/相同形状的矩阵进行运算.png '相同形状的矩阵进行运算')

1. 行数或者列数相同的一维数组和多维数组可以进行计算：
    a. 行形状相同（会与每一行数组的对应位相操作)
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

t1 = np.arange(24).reshape((4,6))
t2 = np.arange(0,6)
print(t1-t2)
```
![列形状相同的数组运算](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/列形状相同的数组运算.png '列形状相同的数组运算')

b. 列形状相同（会与每一个相同维度的数组的对应位相操作)

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

t1 = np.arange(24).reshape((4,6))
t2 = np.arange(4).reshape((4,1))
print(t1-t2)
```

## 矩阵点积

```python
data = np.array([1,2,3])
powers_of_ten = np.array([[1,10],[100,1000],[10000,100000]])
data.dot(powers_of_ten)
'''
array([ 30201, 302010])
'''
```

![矩阵点积](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/矩阵点积.png '矩阵点积')





### 

## 数组中的轴

1. 什么是轴： 在numpy中可以理解为方向，使用0，1，2数字表示，对于一个一维数组，只有一个0
轴，
对于2维数组（shape（2，2))有0轴和1轴，
对于3维数组（shape（2，2，3））有0，1，2轴
2. 为什么要学习轴：有了轴的概念后，我们计算会更加方便，比如计算一个2维数组的平均值，必须指定是计算哪个方向上面的数字的平均值。
![NumPy二维数组的轴](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/Numpy二维数组的轴png.png "NumPy二维数组的轴")
![Numpy三维数组的轴](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/Numpy三维数组的轴.png "Numpy三维数组的轴")

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a)
'''
[[1 2 3]
 [4 5 6]]
 指定0轴方向,0轴上的每一个位置均为1轴的平行轴线,沿着1轴方向运动加和
 0轴方向---->------>-------->
 			时刻1  时刻2 ... 时刻n
 			1轴a   1轴b ...  1轴n
scratch编程 			
	基准(方向)
		节点(运动)
'''
'0轴方向上的每一个(刻度)瞬间,在1轴方向上的所有元素加和'
print(np.sum(a,axis=0)) # [5 7 9] 
'1轴方向上的每一个(刻度)瞬间,在0轴方向上的所有元素加和'
print(np.sum(a,axis = 1)) # [ 6 15]
print(np.sum(a))# 计算所有的值的和

#三维的数据
a = np.arange(27).reshape((3,3,3))
print(a)
'''
[[[ 0 1 2]
[ 3 4 5]
[ 6 7 8]]
[[ 9 10 11]
[12 13 14]
[15 16 17]]
[[18 19 20]
[21 22 23]
[24 25 26]]]
'''
b = np.sum(a, axis=0)
print(b)
'''
[[27 30 33]
[36 39 42]
[45 48 51]]
'''
c = np.sum(a, axis=1)
print(c)
'''
[[ 9 12 15]
[36 39 42]
[63 66 69]]
'''
c = np.sum(a, axis=2)
print(c)
'''
[[ 3 12 21]
[30 39 48]
[57 66 75]]
'''
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
data.prod()# 矩阵中所有元素相乘的值
>>> 362880
```
总结：<font color='red'> 在计算的时候可以想象成是每一个坐标轴，分别计算这个轴上面的每一个刻度上的值</font>，或者在二维数组中记住0表示列1表示行.

![多维度数组聚合](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/多维度数组聚合.png '多维度数组聚合')

## 数组的索引和切片

### 一维数组的操作方法

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

import numpy as np
a = np.arange(10)
# 冒号分隔切片参数 start:stop:step 来进行切片操作
print(a[2:7:2])# 从索引 2 开始到索引 7 停止，间隔为 2
'''
[2 4 6]
'''
# 如果只放置一个参数，如 [2]，将返回与该索引相对应的单个元素
print(a[2],a,sep='\n')
'''
2
[0 1 2 3 4 5 6 7 8 9]
'''
# 如果为 [2:]，表示从该索引开始以后的所有项都将被提取
print(a[2:])
'''
[2 3 4 5 6 7 8 9]
'''

```
![一维数组的索引和切片](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/一维数组的索引和切片.png '一维数组的索引和切片')

### 多维数组的操作方法

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='text'} ##hide  代码隐藏

import numpy as np

t1 = np.arange(24).reshape(4,6)
print(t1)
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]
'''
print('@'*20)
# 取一行  数组[行] 或 数组[行,所有列]
print(t1[1]) # 取一行(一行代表是一条数据，索引也是从0开始的)
>>> [ 6  7  8  9 10 11]
print(t1[1,:]) # 取一行
>>> [ 6  7  8  9 10 11]

## 取连续的多行  数组[行:行,列:列]
print(t1[1:])# 取连续的多行
'''
[[ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]
'''
print(t1[1:3,:])# 取连续的多行
'''
[[ 6  7  8  9 10 11]
 [12 13 14 15 16 17]]
'''


# 取不连续的多行 数组[行,行,行] 或 数组[[行,行,行],列:列]
print(t1[[0,2,3]])# 取不连续的多行
'''
[[ 0  1  2  3  4  5]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]
'''
print(t1[[0,2,3],:])# 取不连续的多行

# 取一列  数组[:,列]
print(t1[:,1])# 取一列
>>>[ 1  7 13 19]


# 连续的多列 数组[:,列:列]
print(t1[:,1:])# 连续的多列
'''
[[ 1  2  3  4  5]
 [ 7  8  9 10 11]
 [13 14 15 16 17]
 [19 20 21 22 23]]
'''


print(t1[:,[0,2,3]])# 取不连续的多列

print(t1[2,3])# # 取某一个值,三行四列



#  取多个不连续的值   数组[[行,行,行],[列,列,列]]
print(t1[[0,1,1],[0,1,3]])# 取多个不连续的值，[[行，行。。。],[列，列。。。]]
>>>[0 7 9]
```
![二维数组的索引和切片](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/二维数组的索引和切片.png '二维数组的索引和切片')

## 数组中的数值修改

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

t = np.arange(24).reshape(4,6)
t
'''
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]])
'''
# 修改某一行的值
t[1,:]=0
print(t)
'''
array([[ 0,  1,  2,  3,  4,  5],
       [ 0,  0,  0,  0,  0,  0],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]])
'''
# 修改某一列的值
t[:,1]=0
t
'''
array([[ 0,  0,  2,  3,  4,  5],
       [ 6,  0,  8,  9, 10, 11],
       [12,  0, 14, 15, 16, 17],
       [18,  0, 20, 21, 22, 23]])
'''
# 修改连续多行
t[1:3,:]=0
# 修改连续多列
t[:,1:4]=0
# 修改多行多列，取第二行到第四行，第三列到第五列
t[1:4,2:5]=0
# 修改多个不相邻的点
t[[0,1],[0,3]]=2000
t
'''
array([[2000,    1,    2,    3,    4,    5],
       [   6,    7,    8, 2000,   10,   11],
       [  12,   13,   14,   15,   16,   17],
       [  18,   19,   20,   21,   22,   23]])
'''


# 可以根据条件修改，比如将小于10的值改掉
t[t<10]='AA'
t
'''
array([[2000, 5000, 5000, 5000, 5000, 5000],
       [5000, 5000, 5000, 2000,   10,   11],
       [  12,   13,   14,   15,   16,   17],
       [  18,   19,   20,   21,   22,   23]])
'''
# 使用逻辑判断
# np.logical_and &
# np.logical_or |
# np.logical_not ~
t[(t>2)&(t<6)]=0 # 与
t
'''
array([[   0,    1,    2, 2600, 2600, 2600],
       [   6,    7,    8,    9,   10,   11],
       [  12,   13,   14,   15,   16,   17],
       [  18,   19,   20,   21,   22,   23]])
'''
t[(t<2)|(t>6)]=0 # 或

t[~(t>6)]=0 # 非

print(t)

# 三目运算（ np.where(condition, x, y)满足条件(condition)，输出x，不满足输出y。)）
score = np.array([[80,88],[82,81],[75,81]])
score
'''
array([[80, 88],
       [82, 81],
       [75, 81]])
'''
result = np.where(score>80,True,False)
result
'''
array([[False,  True],
       [ True,  True],
       [False,  True]])
'''
result = np.where(score>80,'A','B')
result 
'''
array([['B', 'A'],
       ['A', 'A'],
       ['B', 'A']], dtype='<U1')
'''
```
## 数组的添加、删除和去重

### 数组的添加

```python
help(np.append)
Signature: np.append(arr, values, axis=None)
Docstring:
# axis=0/1 时  在给定的轴向添加元素 arr 和 values 有相同的维数[[]]
np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)
'''
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
'''
 # axis=None  数组展开后,添加元素  ,If `axis` is None, `out` is a flattened array.
np.append([1, 2, 3], [[4, 5, 6], 2])
>>>array([1, 2, 3, list([4, 5, 6]), 2], dtype=object)    
Append values to the end of an array.

Parameters
----------
arr : array_like
    Values are appended to a copy of this array.
values : array_like
    These values are appended to a copy of `arr`.  It must be of the
    correct shape (the same shape as `arr`, excluding `axis`).  If
    `axis` is not specified, `values` can be any shape and will be
    flattened before use.
axis : int, optional
    The axis along which `values` are appended.  If `axis` is not
    given, both `arr` and `values` are flattened before use.

Returns
-------
append : ndarray
    A copy of `arr` with `values` appended to `axis`.  Note that
    `append` does not occur in-place: a new array is allocated and
    filled.  If `axis` is None, `out` is a flattened array.

See Also
--------
insert : Insert elements into an array.
delete : Delete elements from an array.

Examples
--------
>>> np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
array([1, 2, 3, 4, 5, 6, 7, 8, 9])

When `axis` is specified, `values` must have the correct shape.
# np.append([[我是两个[]的二维数组]],[[我是两个[]的二维数组]])
>>> np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
# np.append([[我是两个[]的二维数组]],[[我是一个[]的一维数组]])
>>> np.append([[1, 2, 3], [4, 5, 6]], [7, 8, 9], axis=0)
Traceback (most recent call last):
...
ValueError: arrays must have same number of dimensions
File:      ~/anaconda3/lib/python3.7/site-packages/numpy/lib/function_base.py
Type:      function
```



```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏
# 1. numpy.append 函数在数组的末尾添加值。 追加操作会分配整个数组，并把原来的数组复制到新数组中。 此外，输入数组的维度必须匹配否则将生成ValueError。
'''
参数说明：
arr：输入数组
values：要向arr添加的值，需要和arr形状相同（除了要添加的轴）
axis：默认为 None。当axis无定义时，是横向加成，返回总是为一维数组！当axis有定义的时候，分别为
0和1的时候。当axis有定义的时候，分别为0和1的时候（列数要相同）。当axis为1时，数组是加在右边
（行数要相同）。
'''
a = np.array([[1,2,3],[4,5,6]])
print ('第一个数组：')
print (a)
'''
[[1 2 3]
 [4 5 6]]
 '''
print ('\n')
print ('向数组添加元素：')
print (np.append(a, [7,8,9]))
'''
[1 2 3 4 5 6 7 8 9]
'''
print ('\n')
print ('沿轴 0 添加元素：')
print (np.append(a, [[7,8,9]],axis = 0))
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
 '''
print ('\n')
print ('沿轴 1 添加元素：')
print (np.append(a, [[5,5,5],[7,8,9]],axis = 1))
'''
[[1 2 3 5 5 5]
 [4 5 6 7 8 9]]
 '''

```
```python
help(np.insert)
Signature: np.insert(arr, obj, values, axis=None)
Docstring:
Insert values along the given axis before the given indices.

Parameters
----------
arr : array_like
    Input array.
obj : int, slice or sequence of ints
    Object that defines the index or indices before which `values` is
    inserted.

    .. versionadded:: 1.8.0

    Support for multiple insertions when `obj` is a single scalar or a
    sequence with one element (similar to calling insert multiple
    times).
values : array_like
    Values to insert into `arr`. If the type of `values` is different
    from that of `arr`, `values` is converted to the type of `arr`.
    `values` should be shaped so that ``arr[...,obj,...] = values``
    is legal.
axis : int, optional
    Axis along which to insert `values`.  If `axis` is None then `arr`
    is flattened first.

Returns
-------
out : ndarray
    A copy of `arr` with `values` inserted.  Note that `insert`
    does not occur in-place: a new array is returned. If
    `axis` is None, `out` is a flattened array.

See Also
--------
append : Append elements at the end of an array.
concatenate : Join a sequence of arrays along an existing axis.
delete : Delete elements from an array.

Notes
-----
Note that for higher dimensional inserts `obj=0` behaves very different
from `obj=[0]` just like `arr[:,0,:] = values` is different from
`arr[:,[0],:] = values`.

Examples
--------
>>> a = np.array([[1, 1], [2, 2], [3, 3]])
>>> a
array([[1, 1],
       [2, 2],
       [3, 3]])
>>> np.insert(a, 1, 5)
array([1, 5, 1, 2, 2, 3, 3])
'''
np.insert(arr[[]],obj,value,axis)
obj = int-->value=int
obj=[int]-->value=[[]]与arr维度的数组
'''
>>> np.insert(a, 1, 5, axis=1)
array([[1, 5, 1],
       [2, 5, 2],
       [3, 5, 3]])

Difference between sequence and scalars:

>>> np.insert(a, [1], [[1],[2],[3]], axis=1)
array([[1, 1, 1],
       [2, 2, 2],
       [3, 3, 3]])
>>> np.array_equal(np.insert(a, 1, [1, 2, 3], axis=1),
...                np.insert(a, [1], [[1],[2],[3]], axis=1))
True

>>> b = a.flatten()
>>> b
array([1, 1, 2, 2, 3, 3])
# 在[2,2]索引的位置插入[5,6]
>>> np.insert(b, [2, 2], [5, 6])
array([1, 1, 5, 6, 2, 2, 3, 3])
# 索引[2,4]的位置分别插入5,6
>>> np.insert(b, slice(2, 4), [5, 6])
array([1, 1, 5, 2, 6, 2, 3, 3])

# 在数组b中[2,2]索引的位置插入[7.13,Fals],后插入的元素数据类型默认转换为数组b的数据类型
>>> np.insert(b, [2, 2], [7.13, False]) # type casting
array([1, 1, 7, 0, 2, 2, 3, 3])

>>> x = np.arange(8).reshape(2, 4)
# axis=1,数组x的第一列和第三列插入999
'''
axis=1 方向 ↓
第一个时刻的 索引→  1 和 3的位置分别插入999 和 999
第二个时刻的 索引→  1 和 3的位置分别插入999 和 999
第三个时刻的 索引→  1 和 3的位置分别插入999 和 999
'''
>>> idx = (1, 3)
>>> np.insert(x, idx, 999, axis=1)
array([[  0, 999,   1,   2, 999,   3],
       [  4, 999,   5,   6, 999,   7]])
File:      ~/anaconda3/lib/python3.7/site-packages/numpy/lib/function_base.py
Type:      function
```



```python
# 2. numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值。
# 如果未提供轴，则输入数组会被展开。
a = np.array([[1,2],[3,4],[5,6]])
print ('第一个数组：')
print (a)
'''
[[1 2]
 [3 4]
 [5 6]]
 '''
print ('\n')
print ('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print (np.insert(a,3,[11,12]))
'''
[ 1  2  3 11 12  4  5  6]
'''
print ('\n')
print ('传递了 Axis 参数。 会广播值数组来配输入数组。')
print ('沿轴 0 广播：')
'''
 指定0轴方向,0轴上的每一个位置均为1轴的平行轴线,沿着1轴方向运动加和
 0轴方向---->------>-------->
 			时刻1  时刻2 ... 时刻n
 			1轴a   1轴b ...  1轴n
scratch编程 			
	基准(方向)
		节点(运动)
'''
print (np.insert(a,1,[11],axis = 0))
'''
[[ 1  2]
 [11 11]
 [ 3  4]
 [ 5  6]]
 '''
print ('\n')
print ('沿轴 1 广播：')
print (np.insert(a,1,11,axis = 1))
'''
[[ 1 11  2]
 [ 3 11  4]
 [ 5 11  6]]
 '''
print (np.insert(a,[1],[11,12],axis = 0))
'''
[[ 1  1]
 [11 12]
 [ 2  2]
 [ 3  3]]
'''
print (np.insert(a,[1],[[11],[12]],axis = 0))
'''
[[ 1  1]
 [11 11]
 [12 12]
 [ 2  2]
 [ 3  3]]
'''
```



### 数组中的删除

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

#numpy.delete 函数返回从输入数组中删除指定子数组的新数组。 与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开。
'''
参数说明：
arr：输入数组
obj：可以被切片，整数或者整数数组，表明要从输入数组删除的子数组
axis：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开
'''
a = np.arange(12).reshape(3,4)
print ('第一个数组：')
print (a)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
 '''
print ('\n')
print ('未传递 Axis 参数。 在删除之前输入数组会被展开。')
print (np.delete(a,5))
'''
[ 0  1  2  3  4  6  7  8  9 10 11]
'''
print ('\n')
print ('删除每一行中的第二列：')
print (np.delete(a,1,axis = 1))

'''
axis=1时的执行路径
↓一个方向
→多个时刻

[[ 0  2  3] 第一个时刻→012
 [ 4  6  7]第二个时刻→012
 [ 8 10 11]]第三个时刻→012
 '''
print ('\n')


```
### 数组去重

```python
Signature: np.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None)
Docstring:
Find the unique elements of an array.

Returns the sorted unique elements of an array. There are three optional
outputs in addition to the unique elements:

* the indices of the input array that give the unique values
* the indices of the unique array that reconstruct the input array
* the number of times each unique value comes up in the input array

Parameters
----------
ar : array_like
    Input array. Unless `axis` is specified, this will be flattened if it
    is not already 1-D.
return_index : bool, optional
    If True, also return the indices of `ar` (along the specified axis,
    if provided, or in the flattened array) that result in the unique array.
return_inverse : bool, optional
    If True, also return the indices of the unique array (for the specified
    axis, if provided) that can be used to reconstruct `ar`.
return_counts : bool, optional
    If True, also return the number of times each unique item appears
    in `ar`.

    .. versionadded:: 1.9.0

axis : int or None, optional
    The axis to operate on. If None, `ar` will be flattened. If an integer,
    the subarrays indexed by the given axis will be flattened and treated
    as the elements of a 1-D array with the dimension of the given axis,
    see the notes for more details.  Object arrays or structured arrays
    that contain objects are not supported if the `axis` kwarg is used. The
    default is None.

    .. versionadded:: 1.13.0

Returns
-------
unique : ndarray
    The sorted unique values.
unique_indices : ndarray, optional
    The indices of the first occurrences of the unique values in the
    original array. Only provided if `return_index` is True.
unique_inverse : ndarray, optional
    The indices to reconstruct the original array from the
    unique array. Only provided if `return_inverse` is True.
unique_counts : ndarray, optional
    The number of times each of the unique values comes up in the
    original array. Only provided if `return_counts` is True.

    .. versionadded:: 1.9.0

See Also
--------
numpy.lib.arraysetops : Module with a number of other functions for
                        performing set operations on arrays.

Notes
-----
When an axis is specified the subarrays indexed by the axis are sorted.
This is done by making the specified axis the first dimension of the array
and then flattening the subarrays in C order. The flattened subarrays are
then viewed as a structured type with each element given a label, with the
effect that we end up with a 1-D array of structured types that can be
treated in the same way as any other 1-D array. The result is that the
flattened subarrays are sorted in lexicographic order starting with the
first element.

Examples
--------
>>> np.unique([1, 1, 2, 2, 3, 3])
array([1, 2, 3])
>>> a = np.array([[1, 1], [2, 3]])
>>> np.unique(a)
array([1, 2, 3])

Return the unique rows of a 2D array

>>> a = np.array([[1, 0, 0], [1, 0, 0], [2, 3, 4]])
>>> np.unique(a, axis=0)
array([[1, 0, 0], [2, 3, 4]])

Return the indices of the original array that give the unique values:

>>> a = np.array(['a', 'b', 'b', 'c', 'a'])
>>> u, indices = np.unique(a, return_index=True)
>>> u
array(['a', 'b', 'c'],
       dtype='|S1')
>>> indices
array([0, 1, 3])
>>> a[indices]
array(['a', 'b', 'c'],
       dtype='|S1')

Reconstruct the input array from the unique values:

>>> a = np.array([1, 2, 6, 4, 2, 3, 2])
>>> u, indices = np.unique(a, return_inverse=True)
>>> u
array([1, 2, 3, 4, 6])
>>> indices
array([0, 1, 4, 3, 1, 2, 1])
>>> u[indices]
array([1, 2, 6, 4, 2, 3, 2])
File:      ~/anaconda3/lib/python3.7/site-packages/numpy/lib/arraysetops.py
Type:      function
```



```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# numpy.unique 函数用于去除数组中的重复元素。
'''
arr：输入数组，如果不是一维数组则会展开
return_index：如果为true，返回新列表元素在旧列表中的位置（下标），并以列表形式储
return_inverse：如果为true，返回旧列表元素在新列表中的位置（下标），并以列表形式储
return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数
'''
a = np.array([5,2,6,2,7,5,6,8,2,9])
print ('第一个数组：')
print (a)
'''
[5 2 6 2 7 5 6 8 2 9]
'''
print ('\n')
print ('第一个数组的去重值：')
u = np.unique(a)
print (u)
'''
[2 5 6 7 8 9]
'''
print ('\n')
print ('去重数组的索引数组：')
u,indices = np.unique(a, return_index = True)
print (indices)
'''
[1 0 2 4 7 9]
'''
print ('\n')
print ('我们可以看到每个和原数组下标对应的数值：')
print (a)
'''
[5 2 6 2 7 5 6 8 2 9]
'''
print ('\n')
print ('去重数组的下标：')
u,indices = np.unique(a,return_inverse = True)
print ('u','\n',u)
print ('indices','\n',indices)
'''
u
[2 5 6 7 8 9]
indices
[1 0 2 0 3 1 2 4 0 5]
'''
print ('\n')
print ('返回去重元素的重复数量：')
u,count_indices = np.unique(a,return_counts = True)
print ('u',u)
print ('count_indices',count_indices)

```
## numpy的计算

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

import numpy as np
score = np.array([[80,88],[82,81],[75,81]])
# 1. 获取所有数据最大值
result = np.max(score)
print(result)-->88
# 2. 获取某一个轴上的数据最大值
result = np.max(score,axis=0)
print(result)-->[82 88]
# 3. 获取最小值
result = np.min(score)
print(result)-->75
# 4. 获取某一个轴上的数据最小值
result = np.min(score,axis=0)
print(result)-->[75 81]
# 5. 数据的比较
result = np.maximum([-2, -1, 0, 1, 2], 0) # 第一个参数中的每一个数与第二个参数比较返回大的
print(result)-->[0 0 0 1 2]
result = np.minimum([-2, -1, 0, 1, 2], 0) # 第一个参数中的每一个数与第二个参数比较返回小的
print(result)-->[0 0 0 1 2]
result = np.maximum([-2, -1, 0, 1, 2], [1,2,3,4,5]) # 接受的两个参数，也可以大小一致;第二个参数只是一个单独的值时，其实是用到了维度的广播机制；
print(result)-->[0 0 0 1 2]
# 6. 求平均值
result = np.mean(score) # 获取所有数据的平均值
result = np.mean(score,axis=0) # 获取某一行或者某一列的平均值
# 7. 返回给定axis上的累计和
arr = np.array([[1,2,3], [4,5,6]])
print(arr)
print(arr.cumsum(0))
'''
[1, 2, 3]------> |1 |2 |3 |
[4, 5, 6]------> |5=1+4 |7=2+5 |9=3+6|
'''
print(arr.cumsum(1))
'''
↓→
[1, 2, 3]------> |1 |2+1 |3+2+1 |
[4, 5, 6]------> |4 |4+5 |4+5+6 |
'''
arr = np.array([[1,2,3], [4,5,6],[7,8,9]])
print(arr)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
print(arr.cumsum(0))
'''
→↓
[[ 1  2  3]
 [ 5  7  9]
 [12 15 18]]
'''
# 8. argmin求最小值索引
score = np.array([[80,88],[82,81],[75,81]])
result = np.argmin(score,axis=0)
print(result)
'''
[2 1]
'''
# 9. 求每一列的标准差
# 标准差是一组数据平均值分散程度的一种度量。一个较大的标准差，代表大部分数值和其平均值之间差异较大；
# 一个较小的标准差，代表这些数据较接近平均值反应出数据的波动稳定情况，越大表示波动越大，越不稳定。
result = np.std(score,axis=0)
print(result)
'''
[2.94392029 3.29983165]
'''
# 10. 极值
# np.ptp(t,axis=None)就是最大值和最小值的差
# 方差var, 协方差cov, 计算平均值 average, 计算中位数 median
```
### 数组的聚合

![数组的聚合](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/数组的聚合.png '数组的聚合')

### 通用函数



| 函数                                                         | 功能                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| numpy.sqrt(array)                                            | 平方根函数<br>arr = [9,0.81]<br>np.sqrt(arr)<br>>>>array([3. , 0.9]) |
| numpy.sign(array)                                            | 计算各元素正负号<br>arr = [-9,0.81]<br>np.sign(arr)<br>>>>array([-1.,  1.]) |
| numpy.isnan(array)                                           | 计算各元素是否为NaN                                          |
| numpy.isinf(array)                                           | 计算各元素是否为np.inf<br>arr = [np.inf,0.9]<br>np.isinf(arr)<br>>>>array([ True, False]) |
| numpy.cos/cosh/sin/sinh/tan/tanh(array)                      | 三角函数                                                     |
| numpy.modf(array)                                            | 将array中值得整数和小数分离，作两个数组返回                  |
| numpy.ceil(array)                                            | 向上取整,也就是取比这个数大的整数                            |
| numpy.floor(array)                                           | 向下取整,也就是取比这个数小的整数                            |
| numpy.rint(array)                                            | 四舍五入<br>np.rint(arr)<br>>>>array([1., 1.])               |
| numpy.trunc(array)                                           | 向0取整<br>np.trunc(arr)<br>>>>array([1., 0.])               |
| numpy.cos(array)                                             | 正弦值                                                       |
| numpy.sin(array)                                             | 余弦值                                                       |
| numpy.tan(array)                                             | 正切值                                                       |
| numpy.add(array1,array2)                                     | 元素级加法                                                   |
| numpy.subtract(array1,array2)                                | 元素级减法                                                   |
| numpy.multiply(array1,array2)                                | 元素级乘法                                                   |
| numpy.divide(array1,array2)                                  | 元素级除法 array1./array2                                    |
| numpy.power(array1,array2)                                   | 元素级指数 array1.^array2<br>arr1 = [1,2,3]<br/>arr2 = [2,2,2]<br>>>>array([1, 4, 9]) |
| numpy.maximum/minimum(array1,aray2)                          | 元素级最大值                                                 |
| numpy.fmax/fmin(array1,array2)                               | 元素级最大值，忽略NaN                                        |
| numpy.mod(array1,array2)                                     | 元素级求模                                                   |
| numpy.copysign(array1,array2)                                | 将第二个数组中值得符号复制给第一个数组中值                   |
| numpy.greater/greater_equal/less/less_equal/equal/not_equal(array1,array2) | 元素级比较运算，产生布尔数组                                 |
| numpy.logical_end/logical_or/logic_xor(array1,array2)        | 元素级的真值逻辑运算                                         |

## 数组的拼接

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 1. 根据轴连接的数组序列
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
# 要求a,b两个数组的维度相同
print ('沿轴 0 连接两个数组：')
print (np.concatenate((a,b),axis= 0))
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''
print ('\n')
print ('沿轴 1 连接两个数组：')
print (np.concatenate((a,b),axis = 1))
'''
[[1 2 5 6]
 [3 4 7 8]]
'''
# 2. 根据轴进行堆叠
print ('沿轴 0 连接两个数组：')
print (np.stack((a,b),axis= 0))
'''
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
'''
print ('\n')
print ('沿轴 1 连接两个数组：')
print (np.stack((a,b),axis = 1))
'''
[[[1 2]
  [5 6]]

 [[3 4]
  [7 8]]]
'''
# 3. 矩阵垂直拼接
v1 = [[0,1,2,3,4,5],
[6,7,8,9,10,11]]
v2 = [[12,13,14,15,16,17],
[18,19,20,21,22,23]]
result = np.vstack((v1,v2))
print(result)
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]
'''
# 4. 矩阵水平拼接
v1 = [[0,1,2,3,4,5],
[6,7,8,9,10,11]]
v2 = [[12,13,14,15,16,17],
[18,19,20,21,22,23]]
result = np.hstack((v1,v2))
print(result)
'''
[[ 0  1  2  3  4  5 12 13 14 15 16 17]
 [ 6  7  8  9 10 11 18 19 20 21 22 23]]
'''
```
## 数组的分割

```python
Signature: np.split(ary, indices_or_sections, axis=0)
Docstring:
Split an array into multiple sub-arrays.

Parameters
----------
ary : ndarray
    Array to be divided into sub-arrays.
indices_or_sections : int or 1-D array
    If `indices_or_sections` is an integer, N, the array will be divided
    into N equal arrays along `axis`.  If such a split is not possible,
    an error is raised.

    If `indices_or_sections` is a 1-D array of sorted integers, the entries
    indicate where along `axis` the array is split.  For example,
    ``[2, 3]`` would, for ``axis=0``, result in

      - ary[:2]
      - ary[2:3]
      - ary[3:]

    If an index exceeds the dimension of the array along `axis`,
    an empty sub-array is returned correspondingly.
axis : int, optional
    The axis along which to split, default is 0.

Returns
-------
sub-arrays : list of ndarrays
    A list of sub-arrays.

Raises
------
ValueError
    If `indices_or_sections` is given as an integer, but
    a split does not result in equal division.

See Also
--------
array_split : Split an array into multiple sub-arrays of equal or
              near-equal size.  Does not raise an exception if
              an equal division cannot be made.
hsplit : Split array into multiple sub-arrays horizontally (column-wise).
vsplit : Split array into multiple sub-arrays vertically (row wise).
dsplit : Split array into multiple sub-arrays along the 3rd axis (depth).
concatenate : Join a sequence of arrays along an existing axis.
stack : Join a sequence of arrays along a new axis.
hstack : Stack arrays in sequence horizontally (column wise).
vstack : Stack arrays in sequence vertically (row wise).
dstack : Stack arrays in sequence depth wise (along third dimension).

Examples
--------
>>> x = np.arange(9.0)
>>> np.split(x, 3)
[array([ 0.,  1.,  2.]), array([ 3.,  4.,  5.]), array([ 6.,  7.,  8.])]

>>> x = np.arange(8.0)
>>> np.split(x, [3, 5, 6, 10])
[array([ 0.,  1.,  2.]),
 array([ 3.,  4.]),
 array([ 5.]),
 array([ 6.,  7.]),
 array([], dtype=float64)]
File:      ~/anaconda3/lib/python3.7/site-packages/numpy/lib/shape_base.py
Type:      function
```



```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 1. 将一个数组分割为多个子数组
'''
参数说明：
ary：被分割的数组
indices_or_sections：如果是一个整数，就用该数平均切分，如果是一个数组，为沿轴切分的位置（左开右
闭）
axis：沿着哪个维度进行切向，默认为0，横向切分。为1时，纵向切分
'''
arr = np.arange(9).reshape(3,3)
print(arr)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
print ('将数组分为三个大小相等的子数组：')
b = np.split(arr,3)
print (b)

c = np.split(arr,[1])
print (c)
'''
[array([[0, 1, 2]]), array([[3, 4, 5],[6, 7, 8]])]
'''

'''
[array([[0, 1, 2]]), array([[3, 4, 5]]), array([[6, 7, 8]])]
'''
# 2.numpy.hsplit 函数用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组。
# floor() 返回数字的下舍整数。
harr = np.floor(10 * np.random.random((2, 6)))
print ('原array：')
print(harr)
'''
[[8. 8. 5. 3. 0. 3.]
 [5. 6. 8. 8. 2. 2.]]
'''
print ('拆分后：')
print(np.hsplit(harr, 3))
'''
[array([[8., 8.],
       [5., 6.]]), 
  array([[5., 3.],
       [8., 8.]]), 
  array([[0., 3.],
       [2., 2.]])]
'''
np.split(harr,3,axis=1)
'''
[array([[8., 8.],
        [5., 6.]]), 
 array([[5., 3.],
        [8., 8.]]), 
 array([[0., 3.],
        [2., 2.]])]

'''
# 3.numpy.vsplit 沿着垂直轴分割
a = np.arange(16).reshape(4,4)
print ('第一个数组：')
print (a)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
'''
print ('\n')
print ('竖直分割：')
b = np.vsplit(a,2)
print (b)
'''
[array([[0, 1, 2, 3],
       [4, 5, 6, 7]]), 
array([[ 8,  9, 10, 11],
       [12, 13, 14, 15]])]
'''

```

## 数组中nan和inf
- inf 表示无穷大，需要使用 float(‘inf’) 函数来转化，那么对应的就有 float('-inf') 表示无穷小了。
- 在 pandans 中常见，表示缺失的数据，所以一般用 nan 来表示。任何与其做运算结果都是 nan。
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

# 创建一个nan和inf
a = np.nan
b = np.inf
print(a,type(a))-->nan <class 'float'>
print(b,type(b))-->inf <class 'float'>
# --判断数组中为nan的个数(注意：float类型的数据才能赋值nan)
t = np.arange(24,dtype=float).reshape(4,6)
t
'''
array([[ 0.,  1.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10., 11.],
       [12., 13., 14., 15., 16., 17.],
       [18., 19., 20., 21., 22., 23.]])
'''
# 可以使用np.count_nonzero() 来判断非零的个数
print(np.count_nonzero(t)) -->23
# 将三行四列的数改成nan
t[3,4] = np.nan
# 并且 np.nan != np.nan 结果 是TRUE,每一个Nan都不相等
np.nan != np.nan -->True

# 所以我们可以使用这两个结合使用判断nan的个数,count_nonzero返回的个数就是nan的个数
print(np.count_nonzero(t != t))
# 注意： nan和任何数计算都为nan
print(np.sum(t,axis=0))
>>>[36. 40. 44. 48. nan 56.]
# 将nan替换为0
t[np.isnan(t)] = 0
print(t)
'''
[[ 0.  1.  2.  3.  4.  5.]
 [ 6.  7.  8.  9. 10. 11.]
 [12. 13. 14. 15. 16. 17.]
 [18. 19. 20. 21.  0. 23.]]
'''
#----------练习： 处理数组中nan
t = np.arange(24).reshape(4,6).astype('float')
# 将数组中的一部分替换nan
t[1,3:] = np.nan
print(t)
'''
[[ 0.  1.  2.  3.  4.  5.]
 [ 6.  7.  8. nan nan nan]
 [12. 13. 14. 15. 16. 17.]
 [18. 19. 20. 21. 22. 23.]]
'''
# 遍历每一列，然后判断每一列是否有nan

for i in range(t.shape[1]):
    #获取当前列数据
    temp_col = t[:,i]
    # 判断当前列的数据中是否含有nan
    nan_num = np.count_nonzero(temp_col != temp_col)  # 不等与本身的元素即为Nan
    if nan_num != 0: # 条件成立说明含有nan
        # 将这一列不为nan的数据拿出来
        temp_col_not_nan = temp_col[temp_col==temp_col] # 等于自身的元素即非Nan
        # 将nan替换成这一列的平均值
        temp_col[np.isnan(temp_col)] = np.mean(temp_col_not_nan)
print(t)

```
## 二维数组的转置

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers'  continue='utf-8' output='markdown'} ##hide  代码隐藏

#对换数组的维度
a = np.arange(12).reshape(3,4)
print ('原数组：')
print (a )
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
print ('\n')
print ('对换数组：')
print (np.transpose(a))
'''
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
'''
# 与transpose一致
a = np.arange(12).reshape(3,4)
print ('原数组：')
print (a)
print ('\n')
print ('转置数组：')
print (a.T)
'''
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
'''
# 函数用于交换数组的两个轴
t1 = np.arange(24).reshape(4,6)
re = t1.swapaxes(1,0)
print ('原数组：')
print (t1)
'''
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]])
'''
print ('\n')
print ('调用 swapaxes 函数后的数组：')
print (re)
'''
[[ 0  6 12 18]
 [ 1  7 13 19]
 [ 2  8 14 20]
 [ 3  9 15 21]
 [ 4 10 16 22]
 [ 5 11 17 23]]
'''
```

![数组的转置transpose](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/数组的转置transpose.png  '数组的转置transpose')

# pandas

[(Back to 面向过程编程)](#面向过程编程)

[(Back to 面向对象编程)](#⾯向对象编程)

- Pandas 是基于NumPy 的⼀种⼯具，该⼯具是为了解决数据分析任务⽽创建的。Pandas 纳⼊了大量库和⼀些标准的数据模型，提供了⾼效地操作大型数据集所需的⼯具。pandas提供了大量能使我们快速便捷地处理数据的函数和⽅法。

- Pandas基于两种数据类型：series与dataframe。

    > 文中大部分图片出自 A Gentle Visual Intro to Data Analysis in Python Using Pandas
    >
    > 通过 pandas 的 readxxx () 方法可以从对应的数据文件中读取数据，如从 csv 文件中读取数据，使用 readcsv ()，从 Excel 文件中读取数据，使用 read_excel ()，需注意，Pandas 读取 Excel 前需要安装 xlrd 与 xlwt。
## Series对象
Series
: 是Pandas中最基本的对象，Series类似⼀种⼀维数组。事实上，Series 基本上就是基于 NumPy的数组对象来的。和 NumPy 的数组不同，Series 能为数据⾃定义标签，也就是索引（index），然后通过索引来访问数组中的数据。

Dataframe是一个二维的表结构。Pandas的dataframe可以存储许多种不同的数据类型，并且每⼀个坐标轴都有⾃己的标签。你可以把它想象成⼀个series的字典项。

![DataFrame&Series](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/DataFrame&Series.png 'DataFrame&Series')

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8' } ##hide  代码隐藏  output='markdown'
# 创建Series对象并省略索引
'''
index 参数是可省略的，你可以选择不输⼊这个参数。
如果不带 index 参数，Pandas 会⾃动⽤默认 index 进行索引，类似数组，索引值是 [0, ...,len(data) - 1]
'''
sel = Series([1,2,3,4])
print(sel)
# 通常我们会⾃⼰创建索引
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
# Series对象同时⽀持位置和标签两种⽅式获取数据
print('索引下标',sel['c'])
'索引下标 3'
print('位置下标',sel[2])
'位置下标 3'
# 获取不连续的数据
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
# 可以使⽤切⽚或取数据
print('位置切⽚',sel[1:3])# 左包含右不包含
'''
位置切⽚
b 2
c 3
dtype: int64
'''
print('索引切⽚',sel['b':'d'])# 左右都包含
'''
索引切⽚
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
# ReIndex重新索引,会返回⼀个新的Series(调⽤reindex将会重新排序，
# 缺失值则⽤NaN填补)   NaN的数据类型默认为float类型
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
我们可以⽤加减乘除（+ - * /）这样的运算符对两个 Series 进行运算，
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
# 同样也⽀持numpy的数组运算
sel = Series(data = [1,6,3,5], index = list('abcd'))
print(sel[sel>3]) # 布尔数组过滤
'''
b 6
d 5
dtype: int64
'''

print(sel*2) # 标量乘法
'''
a 2
b 12
c 6
d 10
dtype: int64
'''
print(np.square(sel)) # 可以直接加⼊到numpy的数学函数
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
:   （数据表）是一种 2 维数据结构，数据以表格的形式存储，分成若⼲行行和列。
通过DataFrame，你能很⽅便地处理数据。常⻅的操作⽐如选取、替换⾏或列的数据，还能重组数据表、修改索引、多重筛选等。我们基本上可以把 DataFrame 理解成⼀组采⽤同样索引的 Series 的集合。
调⽤DataFrame()可以将多种格式的数据转换为DataFrame对象，它的的三个参数data、index和columns分别为数据、⾏索引和列索引

### DataFrame的创建

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

# 1. 创建DataFrame
# 使⽤二维数组
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
# 使⽤字典创建(行索引由index决定，列索引由字典的键决定)
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

# 使⽤from_dict
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
# to_dict()⽅法将DataFrame对象转换为字典
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
### 读取数据

通过 pandas 的 readxxx () 方法可以从对应的数据文件中读取数据，如从 csv 文件中读取数据，使用 readcsv ()，从 Excel 文件中读取数据，使用 read_excel ()，需注意，Pandas 读取 Excel 前需要安装 xlrd 与 xlwt。

以读入 csv 文件为例:

```python
import pandas as pd
df = pd.read_csv('**.csv')
#pandas 的 read_xxx () 方法会将数据文件中的数据读取进内存并转为 DataFrame
```

![read_csv](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/read_csv.png 'read_csv')

### 选择数据

![df](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/df.png 'df')



#### 列名取数据

![列名取数据](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/列名取数据.png '列名取数据')

#### 切片取多行数据

![切片取多行数据](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/切片取多行数据.png '切片取多行数据')

####  loc 方法同时使用行号与列标签选择 DataFrame 中的任意数据片段



![loc 方法同时使用行号与列标签](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/loc 方法同时使用行号与列标签.png 'loc 方法同时使用行号与列标签')

### 过滤数据

Pandas 的 Series 与 DataFrame 都可以通过简单的比较运算过滤数据

![比较字符串过滤](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/比较字符串过滤.png '比较字符串过滤')

![判断值的大小过滤](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/判断值的大小过滤.png '判断值的大小过滤')

### 处理缺失数据

![pd处理缺失数据](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/pd处理缺失数据.png 'pd处理缺失数据')

### 分组数据

Pandas 提供 groupby () 方法方便我们对数据进行分组处理，groupby () 方法要对数据进行分组需要传入的列名，然后以该列数据为基准进行分组。

这就带了一个问题，基准列被分组其实就是对该列中的数据去重，留下不重复的数据作为不同的类别，但这就让行数变少了，那如何处理多出的数据呢？

正是因为这样的原因，直接调用 groupby () 方法并不能直接获取分组结果，还需要定义如何处理多出数据的逻辑，如采用 sum () 方法，会将基准列中相同元素对应行的其他列数据进行累加

![分组数据](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/分组数据.png '分组数据')

### 创建新列

创建新的列对 Pandas 而言是非常简单的，直接为新列名赋值就好了。

![创建新列](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/创建新列.png '创建新列')

### DataFrame对象常⽤属性

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
# 获取⾏数和列数
# print(df.shape)
'''
(3,3)
'''

# # 获取⾏索引
# print(df.index.tolist())
'''
[‘0’, ‘1’, ‘2’]
'''
# # 获取列索引
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
# 显示头⼏⾏,默认显示5⾏

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
#因为我们只获取⼀列，所以返回的就是⼀个 Series
# print(type(df['name']))
'''
<class 'pandas.core.series.Series'>
'''
# 如果获取多个列，那返回的就是⼀个 DataFrame 类型：
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
# 获取⼀⾏
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
# 注意： df[]只能进⾏选择，或列选择，不能同时多行多列选择。
'''
df.loc 通过标签索引行数据
df.iloc 通过位置获取行数据
'''
# 获取某⼀行某⼀列的数据
# print(df.loc['0','name'])
'''
James
'''
# ⼀⾏所有列
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
# 选择间隔的多⾏多列
# print(df.loc[['0','2'],['name','national']])
'''
       name national
0     James       us
2  Iversion       us
'''
# 选择连续的多⾏和间隔的多列
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

# 取某一列
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

### dataframe修改index、columns

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
# 自定义map函数(x是原有的行列值)
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
# 同时,rename 还可以传入字典,为某个 index 单独修改名称
df3 = df1.rename(index={'bj':'beijing'}, columns = {'a':'aa'})
# print(df3)
'''
         aa  b  c
beijing   0  1  2
sh        3  4  5
gz        6  7  8
'''
# 列转化为行索引
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
# 指定一列为列索行引 (drop=False 指定同时保留作为索引的列)
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
# 在数据框最后加上score一列
# 增加列的元素个数要跟原数据列的个数一样
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
# 语法格式:列表.insert(index, obj)
# index --->对象 obj 需要插入的索引位置。
# obj ---> 要插入列表中的对象(列名)
col_name=df1.columns.tolist()
# 将数据框的列名全部提取出来存放在列表里
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
# 先创建一个DataFrame,用来增加进数据框的最后一行
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
axis:0表示删除行,1表示删除列,默认0
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
# 传入axis=1滤除列:
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
# 用常数填充fillna
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
//TODO数据合并还不太理解 要看视频和赵网页上的案例解析
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
# 使用merge,着重关注的是列的合并
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
# 连接方式,根据左侧为准
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
### concat 
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
# 用内连接求交集(连接方式,共有’inner’,’left’,right’,’outer’)
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
#当纵向连接时keys为列名
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
# 用字典的方式连接同样可以创建层次化列索引
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
### 多层索引
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
# loc方法取值
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
# iloc方法取值(iloc计算的事最内层索引)
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
# 获取列
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
# 一级索引
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
# 取一值
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
时间序列频率:
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
# utc是协调世界时,时区是以UTC的偏移量量的形式表示的,但是注意设置utc=True,是让pandas对象具有时区性质,对于一列进行转换的,会造成转换错误
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
# 可自定义函数,传入agg方法中 grouped.agg(func)
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
#### apply()函数
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

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

# python案例
//TODOpython案例还没看视频
## 2018年北京积分落户数据分析
[北京落户](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/bj_luohu.csv '北京落户')
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 读取文件
luohu_data = pd.read_csv('./bj_luohu.csv', index_col = 'id')
# describe()展示一些基本信息
luohu_data.describe()
# 按照company分组并计算每组个数
# groupby默认会把by的这个列作为索引列返回，可以设置下as_index=False
company_data = luohu_data.groupby('company', as_index=False).count()[['company','name']]
# 重命名列名称
company_data.rename(columns={'name':'people_count'}, inplace=True)
# 按照某一列排序
company_sorted_data = company_data.sort_values('people_count', ascending=False)
company_sorted_data
# 按条件过滤
# 只有一人的公司
company_sorted_data[company_sorted_data['people_count'] == 1]
# 人数前50的公司
company_sorted_data.head(50)
# 分数分布
# 按照步长5分桶统计下分数的分布
bins = np.arange(90, 130, 5)
bins = pd.cut(luohu_data['score'], bins)
bin_counts = luohu_data['score'].groupby(bins).count()
# 处理index
bin_counts.index = [ str(x.left) + '~' + str(x.right) for x in bin_counts.index]
bin_counts.plot(kind='bar', alpha=1, rot=0)
plt.show()
# 年龄分布
# 出生日期转为年龄
luohu_data['age'] = ((pd.to_datetime('2019-07') -
pd.to_datetime(luohu_data['birthday'])) / pd.Timedelta('365 days'))
luohu_data.describe()
bins = np.arange(20, 70, 5)
bins = pd.cut(luohu_data['age'], bins)
bin_counts = luohu_data['age'].groupby(bins).count()
bin_counts.index = [ str(x.left) + '~' + str(x.right) for x in bin_counts.index]
bin_counts.plot(kind='bar', alpha=1, rot=0)
plt.show()

```

- 练习题
    - 对招聘网站上“数据分析”这一职位的招聘情况做分析
    - 提示：
      - 职位地区分布
      - 工资待遇
      - 工作年限要求
      - 技术能力要求

## 阿里巴巴股票行情数据分析

[阿里巴巴股票行情数据](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/BABA_stock.csv '阿里巴巴股票行情数据')

### 2-1 简单分析

```python
# 阿里股票历史数据下载：https://www.nasdaq.com/symbol/baba/historical
# 也可以抓取雪球等股票app的数据
# 阿里股票走势图：https://xueqiu.com/S/BABA
# 道琼斯走势：https://xueqiu.com/S/.DJI
```
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

import numpy as np
from dateutil.parser import parse
# 指定打开的文件名
# 不需要的行需要skip掉
# 默认没有分隔符，所以需要指定delimiter
# 不加载全部的情况下需要指定加载哪些列usecols
# 希望把每一列加载到单独的数组中需要设置unpack=True，并指定对应的变量名，列举下有unpack和没有的区别
# stock_info = np.loadtxt('./BABA_stock.csv', delimiter=',', usecols=(1, 2, 3,4, 5),skiprows=1)
stock_info = np.loadtxt('./BABA_stock.csv', delimiter=',', usecols=(1, 2, 3, 4,5), skiprows=1, unpack=True)
stock_info.shape
stock_info = stock_info[:, ::-1]
stock_info
# 上涨下跌的天数
close_info = stock_info[0]
open_info = stock_info[2]
# 上涨
rise_count = len(close_info[open_info - close_info > 0])
# rise_count = close_info[open_info - close_info > 0].size
print('rise count:' + str(rise_count))
# 下跌
fail_count = len(close_info[open_info - close_info <= 0])
print('fail count:' + str(fail_count))
# 上张天数占比
rise_count / close_info.size
close_info
# 日线转换为周线
# 什么是周线
high_info = stock_info[3]
low_info = stock_info[4]
# loadtxt方法有一个converters参数，可以利用自定义的函数把string做转换
def convert_date(d):
    return parse(d).weekday()
stock_info = np.loadtxt('./BABA_stock.csv', delimiter=',', usecols=(0, 1, 3, 4,5),skiprows=1, dtype='S', converters={0: convert_date})
#print(stock_info)
# 倒序排列
stock_info = stock_info[::-1, :].astype('f8')
# 需要按照每周去分组
# 先找到星期一的数据的索引
week_split = np.where(stock_info[:, 0] == 0)[0]
# 按照周一去分组，split返回给定索引的分组
# 可以指定任意间隔的索引，所以split以一个list的形式返回
week_infos_temp = np.split(stock_info, week_split)
print(type(week_infos_temp))
# 为了简单起见，我们这里只使用一周数据有五天的，
week_infos_temp
week_info = [ x for x in week_infos_temp if len(x) == 5 ]
# 每个星期的数据都是一样的了，我们在把他转换成ndarray
w = np.array(week_info)
print(w.shape)
print(w[:3])
week_open = w[:, 0, 3]
print(week_open[:3])
week_close = w[:, -1, 1]
print(week_close[:3])
week_high = w[:, :, 3].max(axis=1)
print(week_high[:3])
week_low = w[:, :, 4].min(axis=1)
print(week_low[:3])
w_info = np.array([week_open, week_close, week_high, week_close])
#print(w_info[:3])
# 一周的数据放到一行，可以直接用转置矩阵
print('result:', w_info.T)
# 结果保存到文件
np.savetxt('./week_info_baba.cvs', w_info.T, header='open, close, high, low',
delimiter=',', fmt='%.2f')
```
### 2-2 股票买卖策略评估

- 策略：股价超出10日均线买入，跌破十日均线卖出
- 策略二：十日线上穿60日线买入，下穿60日线卖出（练习）
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'
# 加载数据，把date这一列设置为索引，简单起见，只用收盘价进行分析
import numpy as np
import pandas as pd
df = pd.read_csv('./BABA_stock.csv', index_col='date', usecols=[0, 1])
# 先查看以下数据
df.head()
# 将索引转换为datetime形式
df.index = pd.DatetimeIndex(df.index.str.strip("'"))
df.index
# 数据中最近的日期排在前面，按照日期重新排序
df.sort_index(inplace=True)
print(df.head())
df.describe()
```
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'
# 策略一：股价超出10日均线买入，跌破十日均线卖出
# 先计算10日均线数据
ma10 = df.rolling(10).mean().dropna()
# 买点
ma10_model = df['close'] - ma10['close'] > 0
ma10_model

```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'
# 第一个值False，第二个值是True，在True的时候买入，需要自定义一个移动窗口处理函数
# 因为卖的时候还需要定义类似的函数，所以这里把这两个函数放在一起
# 可以在自定义函数中print一些信息，例如w值，以方便调试---这也是调试的一种方式
def get_deal_date(w, is_buy=True):
    if is_buy == True:
        return True if w[0] == False and w[1] == True else False
    else :
        return True if w[0] == True and w[1] == False else False
# raw=False没有的话会有警告信息
# 如果删除Na值，会有缺失，所以这里用0填充，转换为bool值方便后面取值
se_buy = ma10_model.rolling(2).apply(get_deal_date,
raw=False).fillna(0).astype('bool')
# apply的args接受数组或者字典给自定义函数传参
se_sale = ma10_model.rolling(2).apply(get_deal_date, raw=False, args=
[False]).fillna(0).astype('bool')
# 具体的买卖点
buy_info = df[se_buy.values]
sale_info = df[se_sale.values]
# print(buy_info.head())
# print(sale_info.head())
# 买和卖的索引值不一样，不过数据都有63条，所以删除时间索引信息
no_index_buy_info = buy_info.reset_index(drop=True)
no_index_sale_info = sale_info.reset_index(drop=True)
# print(no_index_buy_info.head())
# print(no_index_sale_info.head())
# 每次交易的盈利情况
profit = no_index_sale_info - no_index_buy_info
print(profit)
# 大体数据
profit.describe()
# 总利润是36.07，注意这是每次买和卖一股的利润（买固定的股数），三年的时间交易了63次
# 最多投入210.86，平均投入143.366954，按最高投入算利润率(36.07 / 210.860000)，年化差不多
5%，按平均投入算0.2515，年化将近8%，当然还有手续费没有算
profit.sum()

```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'
# 假如有1w美元，最终盈利是多少
all_money = 10000
remain = all_money
for i in range(len(no_index_buy_info)):
    buy_count = remain / no_index_buy_info.iloc[i]
    remain = buy_count * no_index_sale_info.iloc[i]
    # all_money = sale_total - all_money
    print(remain)
# 最后剩下13799.294014，年化10%多点，还不错
# 如果加上每次交易金额的万分之三手续费
all_money = 10000
remain = all_money
fee = 0.0003
for i in range(len(no_index_buy_info)):
    buy_count = remain / no_index_buy_info.iloc[i]
    remain = buy_count * no_index_sale_info.iloc[i] * (1 - fee)
    # all_money = sale_total - all_money
    print(remain)
# 最终金额13540.898129，少了一点，不过也还不错

```

```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'
# 将10日线改为60日线试试
# 考虑一种边界情况，买了之后卖点到现在还没有出现（因为是先买的，所以不可能买点比卖点多）
# 这种情况我们把当前的股价加到卖点数据中（也可以把买点数据删除）
print(len(no_index_buy_info))
print(len(no_index_sale_info))
if (len(no_index_buy_info) > len(no_index_sale_info)):
    # no_index_buy_info.drop(no_index_buy_info.index[-1], inplace=True)
    no_index_sale_info.loc[len(no_index_sale_info)] = [df.iloc[-1, 0]]
# 在看下250天，也是盈利的，不是策略多牛逼，而是这个统计区间是在美股大的上升趋势中
# 从五日线一直到250日线，都回测下，然后找出最高的


```

## google play store的app数据分析

[google play store的app数据](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/googleplaystore.csv 'google play store的app数据')



```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 加载文件
# 这次只分析'App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type'
df = pd.read_csv('./googleplaystore.csv', usecols=(0, 1, 2, 3, 4, 5, 6))
# 简单浏览下数据
df.head()
# 查看行列数量
df.shape
# 查看各个列的非空数据量
df.count()
# 有很多缺失值，需要清洗
# App处理
# 查看有没有重复值
# 也可以：df['App'].value_counts()
pd.unique(df['App']).size
# 有重复值，先不着急删除重复值，为了不把其他列的异常值留下，先处理数值异常的列
# Category处理
df['Category'].value_counts(dropna=False)
# 有一条异常值
df[df['Category'] == '1.9']
# Rating处理
df['Rating'].value_counts(dropna=False)
# 用平均值填充
df['Rating'].fillna(value=df['Rating'].mean(), inplace=True)
# 有一条值是19的异常记录，和Category的异常是同一条记录
# Reviews清洗
# 用value_counts看数据分布挺广，看起来都是数字
df['Reviews'].value_counts(dropna=False)
df['Reviews'].str.isnumeric().sum()
# 查看有问题的那一行数据
df[~df['Reviews'].str.isnumeric()]
# 异常值和其他的一样，删除这条记录
df.drop(index=10472, inplace=True)
df['Reviews'] = df['Reviews'].astype('i8')
# Size的清洗处理
df['Size'].value_counts()
df['Size'] = df['Size'].str.replace('M', 'e+6')
df['Size'] = df['Size'].str.replace('k', 'e+3')
# 尝试转换，此时转换报错，还有字符串
# df['Size'].astype('f8')
# 定义一个字符串判断是否可以转换
def is_convertable(v):
    try:
        float(v)
        return True
    except ValueError:
        return False
# 查看不能转换的字符串分布
temp = df['Size'].apply(is_convertable)
df['Size'][~temp].value_counts()
# 转换剩下的字符串
df['Size'] = df['Size'].str.replace('Varies with device', '0')
# 在看下是不是还有没转换的字符串
temp = df['Size'].apply(is_convertable)
df['Size'][~temp].value_counts()
# 转换类型
# e+5这种格式使用astype直接转为int有问题，如果想转成int，可以先转成f8，再转i8
# df['Size'] = df['Size'].astype('f8').astype('i8')
df['Size'] = df['Size'].astype('f8')
# 将Size为0的填充为平均数
df['Size'].replace(0, df['Size'].mean(), inplace=True)
df.describe()
# Installs数据清洗
# 先查看分布
df['Installs'].value_counts()
# 分布比较少，直接替换
df['Installs'] = df['Installs'].str.replace('+', '')
df['Installs'] = df['Installs'].str.replace(',', '')
# 转换
df['Installs'] = df['Installs'].astype('i8')
df.describe()
# Type处理
# df.info()查看到有na值，这里需要dropna参数
df['Type'].value_counts(dropna=False)
df[df['Type'].isnull()]
# 删除这条数据
df.drop(index=9148, inplace=True)
# 删除App重复的行
df.drop_duplicates('App', inplace=True)
# 数据清洗完毕，可以开始分析了
# 整体情况
df.describe()
# 分Category的数据
# 分类的个数
df.Category.unique().size
# 每个分类的App数量，排序，可以得出哪些分类的app最受开发者欢迎
df.groupby('Category').count().sort_values('App', ascending=False)
# 分类的安装量排序：娱乐社交类最被用户所需要
df.groupby('Category').mean().sort_values('Installs', ascending=False)
# 分类的评论数据：社交游戏视频评论多
df.groupby('Category').mean().sort_values('Reviews', ascending=False)
# 分类的打分数据，和其他数据不太一致，需要进一步分析
df.groupby('Category').mean().sort_values('Rating', ascending=False)
# 分Type数据
# 免费占比大，付费占比小，免费仍然是主流
df.groupby('Type').count()
# 只有两个类型，且数据量差别很大，没必要继续对比了
df.groupby('Type').sum().sort_values('Installs', ascending=False)
# Category和Type一起分析
# 可以和上面一样分析，不多说了
df.groupby(['Type', 'Category']).mean().sort_values('Reviews', ascending=False)
# 评论安装比
# 收费的app评论比率更高
g = df.groupby(['Type', 'Category']).mean()
(g['Reviews'] / g['Installs']).sort_values(ascending=False)
# 相关性：评论数和安装数强相关，其他的连0.1都不到，可以认为是不相关的（0.5以上可以认为是相关的，0.3以上可以认为是弱相关）
df.corr()
```

## 电商交易数据分析

[电商交易数据](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/order_info_2016.csv '电商交易数据')
[device_type](https://raw.githubusercontent.com/ld269440877/images/master/Py3Notebook/device_type.txt 'device_type')
```python {cmd = true matplotlib=true code_block=true class= ' line-numbers' continue='utf-8'  } ##hide  代码隐藏 output='markdown'

# 加载数据分析需要使用的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 加载数据，加载之前先用文本编辑器看下数据的格式，首行是什么，分隔符是什么等
df = pd.read_csv('./order_info_2016.csv', index_col='id')
df.head()
# 加载好数据之后，第一步先分别使用describe和info方法看下数据的大概分布
# 这两个方法放到两个cell中
df.describe()
# 加载device_type
device_type = pd.read_csv('./device_type.txt')
device_type
df.info()
# 首先要做一个数据的清洗
# order_id
# 我们都知道order_id在一个系统里是唯一值
# 先看下有没有重复值
# 注意：当我们对一列取size属性的时候，返回的是行数，如果对于dataframe使用size，返回的是行乘以列的结果，也就是总的元素数
df.orderId.unique().size
df.orderId.size
# 如果有重复值，我们一般最后处理，因为其他的列可能会影响到删除哪一条重复的记录
# 先处理其他的列
# userId
# userId我们只要从上面的describe和info看下值是不是在正常范围就行了
# 对于订单数据，一个用户有可能有多个订单，重复值是合理的
df.userId.unique().size
# productId
# productId最小值是0，先来看下值为0的记录数量
df.productId[(df.productId == 0)].size
# 177条记录，数量不多，可能是因为商品的上架下架引起的，处理完其他值的时候我们把这些删掉
# cityId
# cityId类似于userId，值都在正常范围，不需要处理
df.cityId.unique().size
# price
# price没有空值，且都大于0，注意单位是分，我们把它变成元
df.price = df.price / 100
# payMoney
# payMoney有负值，我们下单不可能是负值，所以这里对于负值的记录要删除掉
# 展示负值的记录
df[df.payMoney < 0]

# 删除负值的记录
df.drop(index=df[df.payMoney < 0].index, inplace=True)
# 在看下，已经没有了
df[df.payMoney < 0].index
# 变成元
df.payMoney = df.payMoney / 100
# channelId
# channelId根据info的结果，有些null的数据，可能是端的bug等原因，在下单的时候没有传
channelId字段
# 数据量大的时候，删掉少量的null记录不会影响统计结果，这里我们直接删除
# 展示
df[df.channelId.isnull()]
# 删除
df.drop(index=df[df.channelId.isnull()].index, inplace=True)
# 在查看
df[df.channelId.isnull()]
# deviceType的取值可以看device_type.txt文件，没有问题，不需要处理
# createTime和payTime都没有null，不过我们是要统计2016年的数据，所以把非2016年的删掉
# payTime类似，这里只按创建订单的时间算，就不处理了
# 先把createTime和payTime转换成datetime格式
df.createTime = pd.to_datetime(df.createTime)
df.payTime = pd.to_datetime(df.payTime)
df.dtypes
import datetime
startTime = datetime.datetime(2016, 1, 1)
endTime = datetime.datetime(2016, 12, 31, 23, 59, 59)
# 有16年之前的数据，需要删掉
df[df.createTime < startTime]
df.drop(index=df[df.createTime < startTime].index, inplace=True)
df[df.createTime < startTime]
# payTime早于createTime的也需要删掉
df.drop(index=df[df.createTime > df.payTime].index, inplace=True)
# 处理16年之后的数据
df[df.createTime > endTime]
# 看下支付时间有没有16年以前的，支付时间在16年之后的这里就不处理了
df[df.payTime < startTime]
# 回过头来我们把orderId重复的记录删掉
df.orderId.unique().size
df.orderId.size
df.drop(index=df[df.orderId.duplicated()].index, inplace=True)
df.orderId.unique().size
# 把productId为0的也删除掉
df.drop(index=df[df.productId==0].index, inplace=True)
# 数据清洗完毕，可以开始分析了
# 一般都是先看下数据的总体情况总体情况
# 总订单数，总下单用户，总销售额，有流水的商品数
print(df.orderId.count())
print(df.userId.unique().size)
print(df.payMoney.sum()/100)


print(df.productId.unique().size)
# 分析数据可以从两方面开始考虑，一个是维度，一个是指标，维度可以看做x轴，指标可以看成是y轴，同一个维度可以分析多个指标，同一个维度也可以做降维升维。
# 按照商品的productId
# 先看下商品销量的前十和后十个
productId_orderCount = df.groupby('productId').count()
['orderId'].sort_values(ascending=False)
print(productId_orderCount.head(10))
print(productId_orderCount.tail(10))
# 销售额
productId_turnover = df.groupby('productId').sum()
['payMoney'].sort_values(ascending=False)
print(productId_turnover.head(10))
print(productId_turnover.tail(10))
# 看下销量和销售额最后100个的交集，如果销量和销售额都不行，这些商品需要看看是不是要优化或者下架
problem_productIds =
productId_turnover.tail(100).index.intersection(productId_orderCount.tail(100).i
ndex)
# 城市的分析可以和商品维度类似
cityId_orderCount = df.groupby('cityId').count()
['orderId'].sort_values(ascending=False)
cityId_payMoney = df.groupby('cityId').sum()
['payMoney'].sort_values(ascending=False)
# price
# 对于价格，可以看下所有商品价格的分布，这样可以知道什么价格的商品卖的最好
# 先按照100的区间取分桶，价格是分，这里为了好看把他转成元
bins = np.arange(0, 25000, 100)
pd.cut(df.price, bins).value_counts()
# 直方图
# 觉得尺寸小的话可以先设置下figsize，觉得后面的值没有必要展示，可以不用25000，改成10000：
plt.figure(figsize=(16, 16))
plt.hist(df['price'], bins)
# 很多价格区间没有商品，如果有竞争对手的数据，可以看看是否需要补商品填充对应的价格区间
price_cut_count = pd.cut(df.price, bins).value_counts()
zero_cut_result = (price_cut_count == 0)
zero_cut_result[zero_cut_result.values].index
# 按照1000分桶在看下
bins = np.arange(0, 25000, 1000)
price_cut = pd.cut(df.price, bins).value_counts()
# 看看1000分桶的时候5000以下的饼图
m = plt.pie(x=price_cut.values, labels=price_cut.index, autopct='%d%%',
shadow=True)
# channelId
# 渠道的分析类似于productId，可以给出成交量最多的渠道，订单数最多的渠道等，渠道很多时候是需要花钱买流量的，所以还需要根据渠道的盈利情况和渠道成本进行综合比较，同时也可以渠道和商品等多个维度综合分析，看看不同的卖的最好的商品是否相同
# 下单时间分析
# 按小时的下单量分布，可以按时间做推广
# 中午12， 13， 14点下单比较多，应该是午休的时候，然后是晚上20点左右，晚上20点左右几乎是所有互联网产品的一个高峰，下单高峰要注意网站的稳定性、可用性
df['orderHour'] = df.createTime.dt.hour


df.groupby('orderHour').count()['orderId'].plot()
# 按照星期来看，周六下单最多，其次是周四周五
df['orderWeek'] = df.createTime.dt.dayofweek
df.groupby('orderWeek').count()['orderId']
# 下单后多久支付
def get_seconds(x):
return x.total_seconds()
df['payDelta'] = (df['payTime'] - df['createTime']).apply(get_seconds)
bins = [0, 50, 100, 1000, 10000, 100000]
pd.cut(df.payDelta, bins).value_counts()
# 饼图看下，有重合的话可以改下bins
# 绝大部分都在十几分钟之内支付完成，说明用户基本很少犹豫，购买的目的性很强
pd.cut(df.payDelta, bins).value_counts().plot(kind='pie', autopct='%d%%',
shadow=True, figsize=(10, 10))
# 月成交额
# 先把创建订单的时间设置为索引
df.set_index('createTime', inplace=True)
turnover = df.resample('M').sum()['payMoney']
order_count = df.resample('M').count()['orderId']
turnover.plot()
```

