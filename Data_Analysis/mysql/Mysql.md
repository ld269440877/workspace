/**
* @module Mysql
* @Version :
* @Author: Dillon
* @Contact: aa269440877@outlook.com
* @WebSite    :   https://github.com/ld269440877/
* @description:
**/
[(Forward to 总结)](#总结)
[(Forward to SQL查询语言-基础)](#SQL查询语言-基础)
[(Forward to SQL基础查询语言-高阶)](#SQL查询语言-高阶)

![数据分析知识参考体系](数据分析知识参考体系.png '数据分析知识参考体系')

![MySQL思维导图](MySQL思维导图.png)

# 软件安装

## MySQL 8.0

- [安装MySQL预安装](MySQL预安装说明-必读.txt)

[数据库的官网](http://www.mysql.com)下载MySQL
- [Windows安装mysql.pdf](Windows安装mysql.pdf)
- [mysql添加环境变量windows.pdf](mysql添加环境变量windows.pdf)
- [Windows10系统下，彻底删除卸载MySQL.pdf](Windows10系统下，彻底删除卸载MySQL.pdf)


[MySQL数据库安装与配置详解 - daixinet.com - 博客园](https://www.cnblogs.com/sshoub/p/4321640.html)

## Navicat 安装

[Navicat | 产品](https://www.navicat.com.cn/products)
- [Navicat安装.pdf](Navicat安装.pdf)

# MySQL 基础

[一张图带你过SQL基础知识(思维导图) - chenbifeng的专栏 - CSDN博客](https://blog.csdn.net/chenbifeng/article/details/65936304)

关系数据库（Relational database）
:   是创建在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据。

现实世界中的各种实体以及实体之间的各种联系均用关系模型来表示。关系模型是由埃德加·科德于1970年首先提出的，并配合“科德十二定律”。
**标准数据查询语言SQL**就是一种基于关系数据库的语言，这种语言执行对关系数据库中数据的检索和操作。
> SQL是结构化查询语言，是一种用来操作RDBMS的数据库语言，当前关系型数据库都支持使用SQL语言进行操作，也就是说可以通过SQL操作oracle、sql server、mysql、sqlite等等所有的关系型的数据库
**关系模型**由关系数据结构、==关系操作集合==、关系完整性约束三部分组成。
![模板Database](模板Database.png "模板Database")
[模板:Database - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/Template:Database)

## ==关系操作==
关系模块中常用的操作包括：

| <font color='red'>数据查询</font> |  DQL  | 数据查询语言 |       |
| :-------------------------------: | :---: | :----------: | :---: |
|               选择                | 投影  |     连接     |       |
|                并                 |  交   |      差      |  除   |

| <font color='color'>数据操作</font> |  DML  | 数据操作语言 |       |
| :---------------------------------: | :---: | :----------: | :---: |
|                插入                 | 删除  |     修改     | 查询  |

表（关系Relation）
表（关系Relation）是以列（属性Attribute）和行（值组Tuple）的形式组织起来的数据的集合。
一个数据库包括一个或多个表（关系Relation）。
> 列：表中的一个字段
行：表中的一个记录
表：表是结构化的信息；行和列组成表；

例如，可能有一个有关作者信息的名为authors的表（关系Relation）。每行（属性Attribute）都包含特定类型的信息，如作者的姓氏。每列（值组Tuple）都包含有关特定作者的所有信息：姓、名、住址等等。在关系型数据库当中一个表（关系Relation）就是一个关系，一个关系数据库可以包含多个表（关系Relation）
![表Relation](表Relation.png '表Relation')
> 通过客户端RDBMS-client给数据库的服务器RDBMS-server发送SQL 指令，完成数据库、数据表和数据的基本操作
数据库（就是文件）是数据表的集合，数据表是数据的集合，数据包含很多列
==RDBMS==：Relational Database Management System
![(客户端通过SQL语言服务器](客户端通过SQL语言服务器.png '客户端通过SQL语言服务器')
- SQL语句主要分为：
    - DQL：数据查询语言，用于对数据进行查询，如select
    - DML：数据操作语言，对数据进行增加、修改、删除，如insert、update、delete
    - TPL： 事务处理语言，对事物进行处理，包括begin transaction、commit、rollback
    - DCL：数据控制语言，进行授权与权限回收，如grant、revoke
    - DDL：数据定义语言，进行数据库、表的管理等，如create、drop
    - CCL：指针控制语言，通过控制指针完成表的操作，如declare cursor
- 对于web程序员，重点是数据的crud（增删改查），必须熟练编写DQL、DML，能编写DDL完成数据库、表的操作，其他语言如TPL、DCL、CCL了解即可
- SQL是一门特殊的语言，专门用来操作关系数据库
- ==SQL关键字、对象名、和列名不区分大小写==
SQL语言按照实现的功能不同，主要分为3类：数据操纵语言（DML），数据定义语言（DDL）,数据控制语言（DCL）。
> ==数据操纵语言（DML）==：主要用来处理数据库中的数据内容。允许用户对数据库中的数据进行查询 ，插入，更新和删除等操作
DML is Data Manipulation Language statements. Some examples:数据操作语言，SQL中处理数据等操作统称为数据操纵语言

| DML语句  |                 功能说明                 |                                                                                  |
| :------: | :--------------------------------------: | :------------------------------------------------------------------------------: |
|  SELECT  |          从表或视图中检索数据行          |                 SELECT - retrieve data from the a database 查询                  |
|  INSERT  |            插入数据到表或视图            |                      INSERT - insert data into a table 添加                      |
|  UPDATE  |                 更新数据                 |                UPDATE - updates existing data within a table 更新                |
|  DELETE  |                 删除数据                 | DELETE - deletes all records from a table, the space for the records remain 删除 |
|   CALL   |                 调用过程                 |                     CALL - call a PL/SQL or Java subprogram                      |
|  MERGE   |            合并（插入或修改）            |                                                                                  |
|  COMMIT  | 将当前事务所做的更改永久化（写入数据库） |                           COMMIT - save work done 提交                           |
| ROLLBACK |        取消上次提交以来的所有操作        |        ROLLBACK - restore database to original since the last COMMIT 回滚        |

> 数据定义语言（DDL）:是一组SQL命令，用于创建和定义数据库对象，并且将对这些对象的定义保存到数据字典中。通过DDL语句可以创建数据库对象，修改数据库对象和删除数据库对象等。
DDL is Data Definition Language statements. Some examples:数据定义语言，用于定义和管理 SQL 数据库中的所有对象的语言
注：每一条DDL语句执行后，Oracle都将提交当前事务。

| DDL语句  |       功能说明       |                                                                                                                                            |       |
| :------: | :------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: | :---: |
|  CREATE  |    创建数据库结构    |                                              CREATE - to create objects in the database 创建                                               |
|  ALTER   |    修改数据库结构    |                                             ALTER - alters the structure of the database 修改                                              |
|   DROP   |    删除数据库结构    |                                                DROP - delete objects from the database 删除                                                |
|  RENAME  | 更改数据库对象的名称 |                                                                                                                                            |
| TRUNCATE |   删除表的全部内容   | TRUNCATE - remove all records from a table, including all spaces **allocated** for the records are removed **TRUNCATE** TABLE [Table Name] |

> 数据控制语言（DCL）：数据控制语言用于修改数据库结构的操作权限
DCL is Data Control Language statements. Some examples:数据控制语言，用来授予或回收访问数据库的某种特权，并控制数据库操纵事务发生的时间及效果，对数据库实行监视等

| DCL语句 |              功能说明              |                                                                                     |
| :-----: | :--------------------------------: | :---------------------------------------------------------------------------------: |
|  CRANT  | 授予其他用户对数据库结构的访问权限 |               GRANT - gives user's access privileges to database 授权               |
| REVOKE  |    收回用户访问数据库结构的权限    | REVOKE - withdraw access privileges given with the GRANT command 收回已经授予的权限 |

## SQL语句规范
CSV可能会乱码，MySQL导出Excel格式解决乱码问题
SQL语言执行顺序跟书写顺序不一致
1. SQL关键字、对象名、和列名不区分大小写。
2. 字符值和日期值要区分大小写。
3. 在应用程序中如果SQL语句文本很长，可以将语句分布到多行上，并且可以通过使用跳格和缩进提高代码的可读性
4. SQL*Plus中的SQL语句以分号（;）结束。

# Navicat SQL图形化界面操作

## 启动/退出RDBMS服务

- 本机启动  服务（本地） 启动MySQL服务
- 终端  连接sql服务 `mysql -u账号  -p密码`
- 退出MySQL `exit` 或 `quit`
- 登录成功后


## 连接RDBMS

- Navicat连接
- 新建的连接名是数据分析
    - Navicat 充当MySQL客户端的角色，localhost=127.0.01
![启动Navicat连接MySQL](启动Navicat连接MySQL.png '启动Navicat连接MySQL')
![Navicat-MySQL](Navicat-MySQL.png 'Navicat-MySQL')
- 上一步设置的双击连接名 绿色为当前连接的数据库，灰色为未连接
    - 不要删除系统级别的数据库，否则只能重新安装数据库

## 数据导入

![Navicat数据导入导出](Navicat数据导入导出.png 'Navicat数据导入导出')
- 根据“导入向导”和“导出向导”来导入/导出数据
-选择导入格式—选择文件—附加选项—选择目标表(或将原表重命名）—表结构—导入模式—开始导入—导入成功
    - 选择导入格式
![Navicat数据导入选择导入格式](Navicat数据导入选择导入格式.png 'Navicat数据导入选择导入格式')
    - 选择文件
    ![Navicat数据导入选择文件](Navicat数据导入选择文件.png 'Navicat数据导入选择文件')
- 附加选项
    ![Navicat数据导入附加选项](Navicat数据导入附加选项.png 'Navicat数据导入附加选项')
    - 选择目标表
    ![Navicat数据导入选择目标表](Navicat数据导入选择目标表.png 'Navicat数据导入选择目标表')
    - 表结构
    ![Navicat数据导入表结构.](Navicat数据导入表结构.png 'Navicat数据导入表结构.')
    - 导入模式
    ![Navicat数据导入导入模式](Navicat数据导入导入模式.png 'Navicat数据导入导入模式')
    - 开始导入
    - 导入成功==Finished successfully==

## 数据导出
- 选择导出格式——选择导出的文件——选择导出字段——附加选项——开始导出——导出成功
    - 选择导出格式
    ![Navicat数据导出选择导出格式](Navicat数据导出选择导出格式.png 'Navicat数据导出选择导出格式')
    - 选择导出的文件
    ![Navicat数据导出选择导出的文件](Navicat数据导出选择导出的文件.png 'Navicat数据导出选择导出的文件')
    - 选择导出字段
    ![Navicat数据导出选择导出字段](Navicat数据导出选择导出字段.png 'Navicat数据导出选择导出字段')
    - 附加选项
    ![Navicat数据导出附加选项](Navicat数据导出附加选项.png 'Navicat数据导出附加选项')
    - 开始导出
    - 导出成功==Finished successfully==

## 新建数据库  

![数据库-表](数据库-表.png '数据库-表')
![数据库-表-查询](数据库-表-查询.png '数据库-表-查询' )

- 新建的数据库是demo
![新建数据库](新建数据库.png '新建数据库')
utf8通用字符集，utf8mb4是utf8的扩展支持emoji，用于社交产品
![设置MySQL数据库编码规则](设置MySQL数据库编码规则.png '设置MySQL数据库编码规则')

## 新建数据表

[数据库三范式 - - SegmentFault 思否](https://segmentfault.com/a/1190000020754804)

### 新建字段
![识别号id主键](识别号id主键.png '识别号id主键')

|  名   |          类型           |           长度           |          小数点           |           不是null           |            虚拟            |                              键                               |       注释       |
| :---: | :---------------------: | :----------------------: | :-----------------------: | :--------------------------: | :------------------------: | :-----------------------------------------------------------: | :--------------: |
|  id   |           int           |    0 (代表自适应长度)    | 0（一般不会去设置小数点） | id不是null空值（必须有数据） | 不勾选虚拟 567版本中不常用 | 选择键 小钥匙代表标识本字段名id为唯一标识符，数据不能出现重复 | 注释字段名id属性 |
| name  | varchar（不定长字符串） | 10 （字符串长度为10   ） |        0（小数点）        |          bushinull           |       虚拟默认不勾选       |             键不勾选（因已选择id作为唯一标识符）              |     注释姓名     |
|       |                         |                          |                           |                              |                            |                                                               |                  |

### 保存表
![新建id字段为唯一标识](新建id字段为唯一标识.png '新建id字段为唯一标识')
![新建name字段](新建name字段.png '新建name字段')
![新建表classes保存](新建表classes保存.png '新建表classes保存')
![修改classes表字段名属性](修改classes表字段名属性.png '修改classes表字段名属性')
### 添加数据

![classes表添加数据](classes表添加数据.png 'classes表添加数据')

### 新建-保存查询
![新建保存查询](新建保存查询.png '新建保存查询')

# 常用数据类型

## 数据完整性
> - 一个数据库就是一个完整的业务单元，可以包含多张表，数据被存储在表中
> - 在表中为了更加准确的存储数据，保证数据的正确有效，可以在创建表的时候，为表添加一些强制性的验证，包括数据字段的类型、约束

### 数据类型

- 可以通过查看帮助文档查看所有支持的数据类型
- 使用数据类型的原则：==够用就行，尽量使用取值范围小的，儿不用大的，节省内存==
- 重用的数据类型如下：
    - 整数： int，bit
    - 小数： decimal
    - 字符串： varchar，char
    - 日期时间： date，time，datetime
    - 枚举类型：（enum）
- 特别说明的类型如下
    - decimal标识浮点数，如decimal（5,2）标识共存5位数，小数站2位
    - char标识固定长度的字符串，如char（3），如果填充‘ab'时会补充一个空格为’ab ‘
    - varchar标识可变长度的字符串，如varchar（3），填充’ab'时就会存储ab
    - 字符串text标识存储大文本，当字符大于4000时推荐使用
    - 对于图片、音频、视频等文件，不存储在数据库中，而是上传到某个服务器上，人后在表中存储这个文件的保存路径
- 更全的数据类型可以参考[MySQL 中的数据类型介绍 - anxpp的博客 - CSDN博客](https://blog.csdn.net/anxpp/article/details/51284106)
![(数值类型常用](数值类型常用.png '(数值类型常用')
![字符串](字符串.png '字符串')
![日期时间类型](日期时间类型.png '日期时间类型')

### 约束

- 主键primary key：物理上存储的顺序
- 非空not null：此字段的值不允许填写空值
- 唯一unique：此字段的值不允许重复
- 默认default：当不填写时会使用默认值，如果填写以填写为准
- 外键foreign key：对关系字段进行约束，当为关系字段填写值时，会到关联的表中查询此值是否存在，如果存在则填写成功，如果不存在则填写失败并抛出异常
- 说明：虽然外键约束可以保证数据的有效性，但是在进行数据crud（增加、修改、删除、查询）时。都会降低数据库的性能，所以不推荐使用，那么数据的有效性怎么保证呢？答：可以在逻辑层进行控制

# 数据库常见操作

## ==数据库==操作
```mysql {class= ' line-numbers'}
# 数据库操作
<!-- 连接数据库 -->
mysql -uroot -p123456

#查看版本
SELECT version();

<!-- 显示当前时间 -->
SELECT now();

<!-- 修改输入提示符 -->
prompt python> 
>>> python>

prompt \U-\D> 
>>>root@localhost-Tue Oct 22 13:15:07 2019>
'''
\D 完整日期
\U 使用用户
'''

<!-- 查看已创建的数据库-->
show databases; #database 复数-s

<!-- 查看当前正在使用的数据库 -->
SELECT database(); # 数据库单数 输出NULL指当前没有数据库被操作

<!-- 使用指定的数据库 -->
use demo; # use 存在的数据库名称

<!-- 创建数据库 -->
create database 数据库名;

<!-- 创建数据库并指定字符集utf8 -->
create database 数据库名 charset=utf8; # 必须是utf8字符集 社交是utf8mb4字符集

<!-- 查看数据库的创建语句 -->
show create database 要查看的数据库名;

<!-- 删除数据库 -->
drop database 数据库名;
```

## ==数据表==的操作

```mysql { class=' line-numbers'}
# 数据表的操作
<!-- 查看当前数据库中所有表 -->
show tables;

<!-- 创建表 -->
    unsigned 没有符号，无负数
    auto_increment标识自动增长
    创建一个学生的数据表（id、name、age、high、gender、cls_id）
    createtable 数据表名字（字段 类型 约束[,字段 类型 约束]；
    多个约束 部分先后顺序
    enum 表示枚举
    最后一个字段不要添加逗号

create table students (字段名  字段类型    字段约束)
create table students (
    id              int unsigned           primary key     auto_increment,
    name        varchar(15)             not null,
    age           tinyint  unsigned    default 0,
    high          decimal(5,2)            default  0.0,
    gender      enum('男','女','中性','保密'),      #枚举值默认从1开始 ，枚举值（’1‘，’2‘，’3’，‘4’）与原始值('男','女','中性','保密')在使用上是等价的
    cls_id         int unsigned             not null
    );

CREATE TABLE `teachers` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  `age` tinyint(3) unsigned DEFAULT '0',
  `high` decimal(5,2) DEFAULT '0.00',
  `gender` enum('男','女','中性','保密') DEFAULT NULL,
  `cls_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

<!-- 查看表的创建语句 -->
show create table students;

<!-- 查看表结构 describe/description 描述-->
desc students;

<!-- 修改表结构  alter （add/modify/change）-->
    修改表--添加字段
    alter table 表名 add 列名 类型/约束;
    生日信息
alter table students add birthday datetime default "2011-11-11 11:11:11";

<!-- 修改表-修改字段：不重命名版 -->  字段类型
    alter table 表名 modify 列名 类型及约束； #修改字段类型datetime to date
    alter table students modify birthday date default "2011-11-11";

<!-- 修改表-修改字段名：重命名版 --> 字段名
    alter table 表名 change 原列名 新列名 类型及约束； # 修改字段名birthday to birth
    alter table students change birthday birth date default "2011-11-11";

<!-- 修改表-删除字段 -->
alter table students drop birth;

<!-- 删除表 -->
drop table students;

```

## ==数据==增删改查(crud)

### 增加 insert

> insert [into] 表名 values （值1，值2, ...)
全列插入 值和表的字段顺序一一对应
占位符：只有主键字段才有占位符概念 0，default， NULL
全列插入在实际开发中用的不多，如果表结构一旦发生变化，全列插入就会报错
```mysql { class= ' line-numbers'}
# 全列插入
insert into students values (0,'小乔',18, 180.00, '女', 2);
# 查看 表students
SELECT * from students;
DESC students;

insert into students values (default, '大乔', 19, 180.00, '女', 2);
```

> 指定列插入
值和列一一对应 (没有默认值的字段必须添加，类似函数的参数)
insert into 表名 (列1, 列2，...), (值1，值2，...)

```mysql { class= ' line-numbers'}
insert into students (name, high, gender, cls_id) values ('张飞', 190.00, '保密', 1); # gender使用枚举原始值 ’保密‘

insert into students (name, high, gender, cls_id) values ('鲁班', 150.00, '1', 1); # gender使用枚举的枚举值 ’1‘
insert into students (name, high, gender, cls_id) values ('静香', 160.00, '2', 1); # gender使用枚举的枚举值 ’2‘

```

> 多行插入   批量插入
- 指定列的方式，多行（批量）插入
    - insert into  表名 （列1，列2，...） values (值1，值2，...)， (值1，值2，...)， ...
    - ` insert into students (name, high, gender, cls_id) values ('张飞', 190.00, '保密', 1), ('关羽', 190.00, '2', 1); `
- 全列的方式，多行（批量）插入
    - insert [into] 表名 values （值1，值2, ...），（值1，值2, ...）
    -` insert into students values (0, '孙尚香', 18, 180.00, '女', 2), (0, '甄姬', 20, 170.00, '女',3);`

### 修改 update
> where 表示修改的范围
update 表名 set 列1=值1， 列2=值2, ...[where 条件]
没有where 进行条件限制就是全表更新
```mysql { class= ' line-numbers'}
-- 横线横线空格 代表注释
= 代表等于
：= 代表赋值
#无where限制，全表更新
 update students set age=20; 
#有where限制，部分更新
update students set age=25 where id=4; 
```

### 删除 delete
> 物理删除
DELETE FROM tbname [where 条件判断]
```mysql { class= ' line-numbers'}
delete from students where id =5 ;

```
> 逻辑删除
查询哪些学生没有被删除

### 查询基本使用 select
> - 查询所有列
    - select * from 表名；
> - 指定字段查询
    - select 字段 from 表名;
> - 指定条件查询

> - 查询指定列

> - 字段的顺序

> 可以使用as为列或表指定别名

# SQL查询语言-基础
[(Back to 软件安装)](#软件安装)
## SQL 简介
![SQL语言框架](SQL语言框架.png 'SQL语言框架')

## SQL常用命令及顺序

```mysql { class= ' line-numbers'}
select *（必须） 
from 表1 
join 表2
where 条件 
group by 字段
having 条件
order by 字段
limit...

#顺序
from-where-groupby-having-select-orderby-limit
注：SQL对大小写不敏感；命令一般大写，表名、字段名一般小写
```

## SQL基础查询语言

### 检索数据（select 语句）

```mysql { class= ' line-numbers'}
<!-- 常用命令 -->
select *
from 表名
```
- 检索单列：检索出“订单表”中的“订单ID”列
```mysql { class= ' line-numbers'}
select order_id
from spm_order
```
- 检索多列：检索出“订单表”中的“订单ID”和“产品ID”列 ==检索多列时，用“逗号”隔开==
```mysql { class= ' line-numbers'}
select order_id,product_id 
from spm_order
```
- 检索所有列：检索出“订单表”中的所有列检 ==索所有列时，用“*”==；
```mysql { class= ' line-numbers'}
select *
from spm_order
```
- 去重检索：“订单表”里面的销售人员有哪些去重用distinct
```mysql { class= ' line-numbers'}
select distinct sales_name 
from spm_order
```
- 限制检索结果  ==限制检索用limit==  看一下“订单表”前100行的所有数据
```mysql { class= ' line-numbers'}
select *
from spm_order 
limit 100
```
### 限定条件（where 语句）

```mysql { class= ' line-numbers'}
<!-- 基本结构 -->
select *
from 表名
where 条件
```
- 判断条件常用命令：
```mysql { class= ' line-numbers'}
数值判断：
大于(>)、小于(<)、等于(=)、不等于(<>)、大于等于(>=)、小于等于(<=)、范围(between)
逻辑判断：AND、OR、NOT、IN（）
模糊判断：like 、%、_(下划线)等like "%笔%"
```
练习：从订单表中筛选出“北上广深杭”这五个城市，利润大于等于0，并且产品名称包含“笔”的所有订单like "%笔%"
中性笔\笔记本 like "笔%"--> 笔记本
like "%笔" --> 毛笔\铅笔
```mysql { class= ' line-numbers'}
select *
from spm_order
where city in ('北京','上海','广州','深圳','杭州')
    and profit >0
    and product_name like "%笔%"
```
### SQL创建计算字段
```mysql { class= ' line-numbers'}
注：
1、计算：+、-、*、/(加减乘除)
2、创建的新字段可以使用别名：as 新字段名
```
- 计算字段（加减乘除）
```mysql { class= ' line-numbers'}
select
    字段1+字段2 as '合计',     
    字段1-字段2 as '相差',     
    字段1*字段2 as '乘积',     
    字段1/字段2 as '除以'
from 表名
where 条件（非必须）
```
练习：在订单表中加如新字段：平均销售额（销售额/数量）
```mysql { class= ' line-numbers'}
select *,sales/quantity as '平均销售额' 
from spm_order;
```
- 拼接字段（concat）

```mysql { class= ' line-numbers'}
select concat(字段1,字段2) as '新字段名' 
from 表名
```
练习：在订单表中加入新拼接字段，把城市和销售拼接起来作为新拼接字段
```mysql { class= ' line-numbers'}
select *,concat(city,sales_name) 
from spm_order;

select concat(city,"-",sales_name) AS "城市-姓名"
from spm_order;
```

![SQLconcat字段1字段2](SQLconcat字段1字段2.png 'SQLconcat字段1字段2')


![SQLconcat字段1字段2AS字段1-字段2](SQLconcat字段1字段2AS字段1-字段2.png 'SQLconcat字段1字段2AS字段1-字段2')

### 数据分组、过滤与排序
- 数据分组（group by）
```mysql { class= ' line-numbers'}
语法结构：
SELECT 字段,计算字段
FROM 表名
where 条件
group by 字段
```
练习：计算销售人员在2018年的销售额和利润
```mysql { class= ' line-numbers'}
select sales_name,sum(sales) AS "总销售额",sum(profit)
from spm_order
where order_date between "2018-01-01" and "2018-12-31" 
group by sales_name;
```
![SQL数据分组groupby](SQL数据分组groupby.png 'SQL数据分组groupby')

- 数据过滤（having）
```mysql { class= ' line-numbers'}
语法结构：
SELECT 字段,计算字段FROM 表名
where 条件
group by 字段having 条件
```
练习：计算销售人员在2018年的销售额和利润，并且只显示利润大于10万的销售人员
```mysql { class= ' line-numbers'}
select sales_name,sum(sales),sum(profit)
from spm_order
where order_date between "2018-01-01" and "2018-12-31" 
group by sales_name
having sum(profit) >100000
```
![SQL数据过滤having](SQL数据过滤having.png 'SQL数据过滤having')

[正确理解MySQL中的where和having的区别 -SegmentFault 思否](https://segmentfault.com/a/1190000008284099)
> where和having都可以使用的场景
>- select goods_price,goods_name from sw_goods where goods_price > 100
>- select goods_price,goods_name from sw_goods having goods_price > 100
解释：上面的having可以用的前提是我已经筛选出了goods_price字段，在这种情况下和where的效果是等效的，但是如果我没有select goods_price 就会报错！！因为having是==从前面筛选的字段再筛选==，而where是<font color='red'>从数据表中的字段直接进行的筛选的</font>。

>只可以用where，不可以用having的情况
>- select goods_name,goods_number from sw_goods where goods_price > 100
>- select goods_name,goods_number from sw_goods having goods_price > 100 //报错！！！因为前面并没有筛选出goods_price 字段

> 只可以用having，不可以用where情况
查询每种goods_category_id商品的价格平均值，获取平均价格大于1000元的商品信息
>- select goods_category_id , avg(goods_price) as ag from sw_goods group by goods_category having ag > 1000
>- select goods_category_id , avg(goods_price) as ag from sw_goods where ag>1000 group by goods_category //报错！！因为from sw_goods 这张数据表里面没有ag这个字段
注意:where 后面要跟的是数据表里的字段，如果我把ag换成avg(goods_price)也是错误的！因为表里没有该字段。而having只是根据前面查询出来的是什么就可以后面接什么

- 结果排序（order by .....desc）

```mysql { class= ' line-numbers'}
语法结构：
SELECT 字段,计算字段
FROM 表名
where 条件 (非必须) 
group by 字段
having 条件 (非必须) 
order by 字段

<!-- 排序： -->
升序：默认
降序：DESC
```
练习：计算销售人员在2018年的销售额和利润，只显示利润大于10万的销售人员，并按销售额从高到低降序排列
```mysql { class= ' line-numbers'}
select sales_name,sum(sales),sum(profit)  AS "利润"
from spm_order
where order_date between "2018-01-01" and "2018-12-31"
group by sales_name
having 利润 >100000
order by sum(sales) desc;
```
![SQL结果排序orderByDesc](SQL结果排序orderByDesc.png 'SQL结果排序orderByDesc')

# 数据类型与SQL函数

## 数据类型
```mysql { class= ' line-numbers'}
最常用的数据类型：
int 整数 
ﬂoat 小数 浮点数
varchar 文本
date 日期
```
- 数值型
最常用的是int（整数）和ﬂoat（小数）

|      类型       | 描述                                                                                                       |
| :-------------: | :--------------------------------------------------------------------------------------------------------- |
|  TINYINT(size)  | -128 到 127 $2^7$ 常规。0 到 255 无符号*。在括号中规定最大位数。                                           |
| SMALLINT(size)  | -32768 到 32767 $2^{15}$ 常规。0 到 65535 无符号*。在括号中规定最大位数。                                  |
| MEDIUMINT(size) | -8388608 到 8388607 $2^{23}$ 普通。0 to 16777215 无符号*。在括号中规定最大位数。                           |
|    INT(size)    | -2147483648 到 2147483647 常规。0 到 4294967295 无符号*。在括号中规定最大位数。例如：int(10)               |
|  BIGINT(size)   | -9223372036854775808 到 9223372036854775807 常规。0 到18446744073709551615 无符号*。在括号中规定最大位数。 |
|  FLOAT(size,d)  | 带有浮动小数点的小数字。在括号中规定最大位数。<br>在 d 参数中规定小数点右侧的最大位数。例如：float(10,2)   |
| DOUBLE(size,d)  | 带有浮动小数点的大数字。在括号中规定最大位数。<br>在 d 参数中规定小数点右侧的最大位数。例如：double(10,2)  |
| DECIMAL(size,d) | 作为字符串存储的 DOUBLE 类型，允许固定的小数点。                                                           |

- 日期型

|    类型     | 描述                                                                                                                                                                                  |
| :---------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   DATE()    | 日期。格式：YYYY-MM-DD注释：支持的范围是从 '1000-01-01' 到 '9999-12-31'                                                                                                               |
| DATETIME()  | *日期和时间的组合。格式：YYYY-MM-DD HH:MM:SS注释：支持的范围是从'1000-01-01 00:00:00' 到 '9999-12-31 23:59:59'                                                                        |
| TIMESTAMP() | *时间戳。TIMESTAMP 值使用 Unix 纪元('1970-01-01 00:00:00' UTC) 至今的描述来存储。格式：YYYY-MM-DD HH:MM:SS注释：支持的范围是从 '1970-01-01 00:00:01' UTC 到 '2038-01-09 03:14:07' UTC |
|   TIME()    | 时间。格式：HH:MM:SS 注释：支持的范围是从 '-838:59:59' 到 '838:59:59'                                                                                                                 |
|   YEAR()    | 2 位或 4 位格式的年。<br>4 位格式所允许的值：1901 到 2155。<br>2 位格式所允许的值：70 到 69，表示从 1970 到 2069。                                                                    |

- 文本型
最常用的是char和varchar，两者区别：

|            类型            | 描述                                                                                                                                                            |
| :------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    char(n)类型（定长）     | 当定义的是char(10)，输入的是"abc"这三个字符时，它们占的空间一样是10个字节，包括7个空字节;当输入的字符长度超过指定的数时，char会截取超出的字符;例如：6位数的密码 |
| varchar(n)类型（可变长度） | 比如varchar(10), 然后输入abc三个字符，那么实际存储大小为3个字节                                                                                                 |

|       类型       | 描述                                                                                                                                                                                                                                    |
| :--------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    CHAR(size)    | 保存固定长度的字符串（可包含字母、数字以及特殊字符）。在括号中指定字符串的长度。最多 255 个字符。char(10)                                                                                                                               |
|  VARCHAR(size)   | 保存可变长度的字符串（可包含字母、数字以及特殊字符）。在括号中指定字符串的最大长度。最多 255 个字符。注释：如果值的长度大于 255，则被转换为 TEXT 类型。                                                                                 |
|     TINYTEXT     | 存放最大长度为 255 个字符的字符串。                                                                                                                                                                                                     |
|       TEXT       | 存放最大长度为 65,535 个字符的字符串。                                                                                                                                                                                                  |
|       BLOB       | 用于 BLOBs (Binary Large OBjects)。存放最多 65,535 字节的数据。                                                                                                                                                                         |
|    MEDIUMTEXT    | 存放最大长度为 16,777,215 个字符的字符串。                                                                                                                                                                                              |
|    MEDIUMBLOB    | 用于 BLOBs (Binary Large OBjects)。存放最多 16,777,215 字节的数据。                                                                                                                                                                     |
|     LONGTEXT     | 存放最大长度为 4,294,967,295 个字符的字符串。                                                                                                                                                                                           |
|     LONGBLOB     | 用于 BLOBs (Binary Large OBjects)。存放最多 4,294,967,295 字节的数据。                                                                                                                                                                  |
| ENUM(x,y,z,etc.) | 允许你输入可能值的列表。可以在 ENUM 列表中列出最大 65535 个值。如果列表中不存在插入的值，则插入空值。注释：这些值是按照你输入的顺序存储的。可以按照此格式输入可能的值：ENUM('X','Y','Z') 枚举原始值('X','Y','Z')，枚举值（‘1’,‘2’,‘3’） |
|       SET        | 与 ENUM 类似，SET 最多只能包含 64 个列表项，不过 SET 可存储一个以上的值。                                                                                                                                                               |

## SQL函数

### 数值型函数

|         函数         | 描述                           |
| :------------------: | :----------------------------- |
|      SUM(列名)       | 返回某列的总和                 |
|      AVG(列名)       | 返回某列的平均值               |
|      MIN(列名)       | 返回某列的最低值               |
|      MAX(列名)       | 返回某列的最高值               |
|     COUNT(列名)      | 返回某列的行数（不包括NULL值） |
|       COUNT(*)       | 返回被选行数                   |
| COUNT(distinct 列名) | 返回相异结果的数目             |
|      ABS(列名)       | 返回绝对值                     |
|      SQRT(列名)      | 返回平方                       |
练习1：
订单表共有多少行？
产品名称有多少行？
订单表里面有多少个城市？
```mysql { class= ' line-numbers'}
select count(*)
from spm_order;

select count(product_name)
from spm_order;
'''
count(product_name)
                            9959
'''
select count(distinct city)
from spm_order
'''
count(distinct city)
                        573
'''
```
练习2：
在订单表中计算以下值：总销售额、总利润、产品平均数量、最低利润值、最高利润值
```mysql { class= ' line-numbers'}
select sum(sales),sum(profit),avg(quantity),min(profit),max(profit)
from spm_order
```
![SQL总和sum平均avg最小min最大max](SQL总和sum平均avg最小min最大max.png 'SQL总和sum平均avg最小min最大max')
练习3：
查看订单表中的利润和利润的绝对值
```mysql { class= ' line-numbers'}
select sales,abs(profit)
from spm_order
```
![SQL绝对值abs](SQL绝对值abs.png 'SQL绝对值abs')

### 时间日期型函数

|     函数      | 描述                                |
| :-----------: | :---------------------------------- |
|     NOW()     | 返回当前的日期和时间                |
|   CURDATE()   | 返回当前的日期                      |
|   CURTIME()   | 返回当前的时间                      |
|    DATE()     | 提取日期或日期/时间表达式的日期部分 |
|   EXTRACT()   | 返回日期/时间按的单独部分           |
|  DATE_ADD()   | 给日期添加指定的时间间隔            |
|  DATE_SUB()   | 从日期减去指定的时间间隔            |
|  DATEDIFF()   | 返回两个日期之间的天数              |
| DATE_FORMAT() | 用不同的格式显示日期/时间           |

- 时间格式
    - DATETIME - 格式: YYYY-MM-DD HH:MM:SS
    - DATE - 格式 YYYY-MM-DD
    - YEAR - 格式 YYYY 或 YY

```mysql { class= ' line-numbers'}
常见日期命令：
SELECT
NOW(),#返回当前日期和时间
DATE(now()),#日期格式
MONTH(NOW()),#月份
YEAR(NOW()),#年份
DATE_FORMAT(NOW(),'%Y-%m-%d'), --年月日格式
DATE_FORMAT(NOW(),'%Y-%m'),#年月格式 大写为英文，小写为汉字
DATE_ADD(NOW(),INTERVAL 1 DAY),#日期相加 加一天 加一周 减一周
DATE_SUB(NOW(),INTERVAL 1 DAY);#日期相减 减一天

SELECT
DATEDIFF('2019-08-31','2019-01-01')#日期间隔多少天
'''
DATEDIFF('2019-08-31','2019-01-01')
                                                        242
'''
```
![SQL常见时间命令](SQL常见时间命令.png 'SQL常见时间命令')

练习1：
查看现在的日期和时间？
查看现在的日期？
```mysql { class= ' line-numbers'}
select now();
select CURDATE();
```
练习2：
在订单表中增加一个“送货天数”的新字段
```mysql { class= ' line-numbers'}
select order_date, ship_date, datediff(ship_date,order_date) as '送货天数'
from spm_order
```
练习3：
在订单表中增加一个“订单月份”的新字段
```mysql { class= ' line-numbers'}
select order_date,DATE_FORMAT(order_date,'%Y-%m') as '订单月份'
from spm_order
```
![SQL订单月份DATE_FORMAT](SQL订单月份DATE_FORMAT.png 'SQL订单月份DATE_FORMAT')
练习4：
在订单表中筛选出订单日期在2018年的所有订单
```mysql { class= ' line-numbers'}
select *
from spm_order
where order_date between "2018-01-01" and "2018-12-31"
```
![SQL_SELECT星号](SQL_SELECT星号.png 'SQL_SELECT星号')
![SQL_SELECT字段](SQL_SELECT字段.png 'SQL_SELECT字段')

- 文本型函数

|    函数     | 描述             |
| :---------: | :--------------- |
| LEFT(列名)  | 返回左边的字符   |
| RIGHT(列名) | 返回右边的字符   |
|  LEN(列名)  | 返回某字段的长度 |

资料推荐
《MySQL必知必会》：知识点全、适合入门、短时间内可以看完（200页）
推荐网站
[w3school](https://www.w3school.com.cn/sql/index.asp)
[菜鸟教程](https://www.runoob.com/mysql/mysql-tutorial.html)
刷题必备
[题库 - 力扣 (LeetCode) 全球极客挚爱的技术成长平台](https://leetcode-cn.com/problemset/database/?utm_source=LCUS&utm_medium=ip_redirect_o_uns&utm_campaign=transfer2china)

# 总结

1.  总结快速掌握一门软件的方法：构建学习框架，再学具体内容
先系统化学习（构建学习框架和知识体系），
再碎片化学习（具体内容、实际工作中遇到的问题）；
不要想一口气学完
2.  本节课讲了哪些SQL命令、SQL的基本语法结构及顺序
3.  多写、多刷题、孰能生巧

[(Back to 软件安装)](#软件安装)

```mysql { class= ' line-numbers'}
select *（必须）
from 表
where 条件
group by 字段
having 条件
order by 字段
limit...
```
![SQL作业1](SQL作业1.png 'SQL作业1')

# SQL查询语言-高阶
![SQL查询语言-高阶](SQL查询语言-高阶.png 'SQL查询语言-高阶')

## SQL多表联结查询

### 联结的类型
- JOIN: 如果表中有至少一个匹配，则返回行
- LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行
- RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行
```mysql { class= ' line-numbers'}
语法结构：
SELECT 列名
FROM 表1  JOIN 表2  ON 表1.列名=表2.列名
```
![SQL-表联结Joins](SQL-表联结Joins.png 'SQL-表联结Joins')
#TODO
- join练习
练习：将订单表、地区表、产品类别表联结成一张表
```mysql { class= ' line-numbers'}
SELECT a.*,b.`省/自治区`,b.地区 ,c.类别,c.子类别, d.月份,d.年份 from  订单表 a 
LEFT JOIN 地区 b on a.城市 = b.城市 
LEFT JOIN 产品类别 c on a.`产品 ID` = c.`产品 ID` 
```

## SQL复杂查询

### 条件函数（case when）
```mysql { class= ' line-numbers'}
语法结构：
case when 条件 then '结果'  
        when 条件 then '结果'  
        when 条件 then '结果'
        ......
         else '默认值' 
end as '新字段名'
```
练习：计算出盈利订单、不盈利订单和不盈不亏订单的销售额结果示例：
结果示例：
| 订单类型 | 销售额 |
| :------: | :----- |
|   盈利   | 1600   |
| 不盈不亏 | 12     |
|   亏损   | 1000   |
```mysql { class= ' line-numbers'}
select
case when profit>0 then '盈利'
        when profit=0 then '不盈不亏'
        else '亏损'
end as '订单类型'
,sum(sales) as '销售额'
from spm_order
group by
case when profit>0 then '盈利'
        when profit=0 then '不盈不亏'
        else '亏损'
end
```
![SQL条件函数case-when](SQL条件函数case-when.png 'SQL条件函数case-when')

### 分组排序函数（Row_number）

```mysql { class= ' line-numbers'}
语法结构：
用法1：无分组排序
Row_number() OVER(ORDER BY 字段 DESC)
用法2：分组排序
ROW_NUMBER() OVER(PARTITION BY 字段1 ORDER BY 字段2 DESC)
表示根据字段1分组，在分组内部根据字段2排序，这个函数计算的值就表示每组内部排序后的顺序编号
解释：
ROW_NUMBER( ) 起到了编号的功能
partition by 将相同数据进行分区
order by 使得数据按一定顺序排序
```
练习1：计算销售人员的销售额,结果按从高到低排序，查询结果中要包含销售的排名
```mysql { class= ' line-numbers'}
select sales_name,sum(sales),Row_number() OVER(ORDER BY sum(sales) DESC) as 'rank'
from spm_order
group by sales_name
```
![SQL分组排序函数Row_number练习1](SQL分组排序函数Row_number练习1.png 'SQL分组排序函数Row_number练习1')
练习2：计算销售人员在不同城市的销售额；
要求：结果根据销售人员在不同城市的销售额进行分组排序（降序），并且查询结果要包含分组排名
```mysql { class= ' line-numbers'}
select sales_name,city,sum(sales),ROW_NUMBER() OVER(PARTITION BY sales_name
ORDER BY sum(sales) DESC) as 'rank'
from spm_order
group by sales_name,city
```
![SQL分组排序函数Row_number练习2](SQL分组排序函数Row_number练习2.png 'SQL分组排序函数Row_number练习2')

### 嵌套查询（t1/t2）
```mysql { class= ' line-numbers'}
语法结构：
SELECT t1.*
from
(select 字段 from 表名)t1
```
练习：计算每个销售人员销售额排名top5的城市？
>思路解析：
1）计算销售人员在不同城市的销售额；
2）结果根据销售人员进行分组排序；
3）选每个销售人员销售额top5的城市；

```mysql { class= ' line-numbers'}
select t1.sales_name,t1.city,t1.sales,t1.rank
from
(select sales_name,city,sum(sales) as 'sales',ROW_NUMBER() OVER(PARTITION BY
sales_name ORDER BY sum(sales) DESC) as 'rank'
from spm_order
group by sales_name,city)t1
where t1.rank<=5
```
![SQL嵌套查询t1](SQL嵌套查询t1.png 'SQL嵌套查询t1')

### 子查询（IN）
```mysql { class= ' line-numbers'}
语法结构：
SELECT 字段
FROM 表名
where 字段 in (SELECT 字段 FROM 表名 where 条件)
```

### 组合查询（union）
```mysql { class= ' line-numbers'}
语法结构：
SELECT 字段
FROM 表名
union
SELECT 字段
FROM 表名
union
SELECT 字段
FROM 表名
```
>union与union all的区别;
union:去重，返回去重后的结果
union all:不去重，返回所有

练习：
查询利润大于0的订单；
查询城市在“北上广深杭”的订单；
并将两个查询结果合并(不去重)；
```mysql { class= ' line-numbers'}
select *
from spm_order
where profit>0

union all

select *
from spm_order
where city in ('北京','上海','广州','深圳','杭州');
```
![SQL组合查询unionAll](SQL组合查询unionAll.png 'SQL组合查询unionAll')

# SQL定义和操作语言

## 创建表/数据库（create)

### 创建数据库
```mysql { class= ' line-numbers'}
语法结构
create database 数据库名;
或者
手动创建
```
>练习：创建名字为'learning'的数据库
`CREATE database learning;`

### 创建表
```mysql { class= ' line-numbers'}
语法结构
CREATE TABLE 表名
(
字段1 数据类型,
字段2 数据类型,
.......,
PRIMARY KEY (字段)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='表里面的内容'
注：
PRIMARY KEY (字段) #主键
ENGINE=InnoDB #引擎类型（事务处理引擎）
AUTO_INCREMENT=1 #每增加一行时自动增量
CHARSET=utf8 #编码格式
```

### 主键与外键

- 主键
    - primary key，是一列；它的值能够唯一区分表中的每个行；
    - 是表中的唯一标识（身份证号）；
规则：
1）主键值必须唯一，任意两行都不具有相同的主键值；
2）每个行都必须有一个主键值，主键列不允许出现NULL值；
3）不能修改，不能更新；已经删除的主键不能再重复使用
4）表的主键不做强制要求，但建议设立
例子：订单表中的订单ID、顾客表中的顾客ID、产品表中的产品ID等

- 外键
    - 外键用于与另一张表的关联；
    - 是能确定另一张表记录的字段，用于保持数据的一致性；
例子：A表中的一个字段，是B表的主键，那他就可以是A表的外键
![SQL主键与外键](SQL主键与外键.png 'SQL主键与外键')

- 主键和外键的区别

|       | 主键                                       | 外键                                                   |
| :---: | :----------------------------------------- | :----------------------------------------------------- |
| 定义  | 唯一标识一条记录，不能有重复的，不允许为空 | 表的外键是另一个表的主键，外键可以有重复的，可以是空值 |
| 作用  | 用来保证数据完整性                         | 用来和其他表建立联系用的                               |
| 个数  | 主键只能有一个                             | 一个表可以有多个外键                                   |
## 插入数据(insert into)
```mysql { class= ' line-numbers'}
<!-- 插入一行： 全列插入-->
INSERT INTO 表名
VALUES
(值1, 值2,....)

<!-- 插入一行：字段-值 -->
INSERT INTO 表名
(字段1, 字段2,...)
VALUES
(值1, 值2,....)

<!-- 插入多行： 字段-值-->
INSERT INTO 表名
(字段1, 字段2,...)
VALUES
(值1, 值2,....)
(值1, 值2,....)
(值1, 值2,....)
(值1, 值2,....)
<!-- 插入多行： 全列插入-->
```
练习：创建如下表格“order_2017”
![SQL插入数据insertInto练习](SQL插入数据insertInto练习.png 'SQL插入数据insertInto练习')
```mysql { class= ' line-numbers'}
#创建一个空表
CREATE TABLE order_2017
(
`order_id`varchar(20) NOT NULL DEFAULT '' '唯一的订单编号',
`cust_id` varchar(20) NOT NULL DEFAULT '' COMMENT '顾客ID',
`date` date DEFAULT NULL COMMENT '交易日期',
`original_value` double(10,2) DEFAULT '0.00' COMMENT '订单原始金额',
`discount` double(10,2) DEFAULT '0.00' COMMENT '订单折扣金额',
`items` int(11) NOT NULL DEFAULT '0' COMMENT '订单购买的商品数量',
PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='2017年订单表'
;
#在表order_2017插入值
INSERT INTO order_2017
(`order_id`,`cust_id`,`date`,`original_value`,`discount`,`items`)
VALUES
('0001','C1','2017/1/1','199','99','1'),
('0002','C2','2017/1/1','30.7','0','3'),
('0003','C3','2017/1/3','49.9','19','1'),
('0004','C4','2017/2/19','125','0','5'),
('0005','C2','2017/3/5','499','100','4'),
('0006','C4','2017/11/11','273.5','23.5','11')
;
```
![SQL插入数据insertInto练习结果](SQL插入数据insertInto练习结果.png 'SQL插入数据insertInto练习结果')

## 更新表内数据(update)
```mysql { class= ' line-numbers'}
语法结构
UPDATE 表名 #要更新的表
SET 字段=新值 #字段和新的值
WHERE 字段=旧值 #更新的条件
```
练习：把订单ID为'0002'的订单中，日期改成'2017/4/1'
```mysql { class= ' line-numbers'}
update order_2017
set date = '2017/4/1'
where order_id = '0002'
```
## 更新表结构(alter)

### 增加列ADD
```mysql { class= ' line-numbers'}
语法结构
ALTER TABLE 表名
ADD 列名 数据类型
```
练习1：在'order_2017'表中，增加订单的实付金额“spend”列
```mysql { class= ' line-numbers'}
ALTER TABLE order_2017
ADD spend double(10,2) #定义字段数据类型
```
### 删除列Drop
```mysql { class= ' line-numbers'}
语法结构
#删除列Drop
ALTER TABLE 表名
DROP 列名
```
练习1：在'order_2017'表中，删除订单的实付金额“spend”列
```mysql { class= ' line-numbers'}
ALTER TABLE order_2017
DROP spend
```
## 删除数据库/表/某列（delete/drop）
### 删除行
```mysql { class= ' line-numbers'}
语法结构
删除特定行：
delete from 表名 #从哪张表中删除
where 条件 #删除的条件
```
练习：在'order_2017'表中，删除订单ID为'0002'的订单
```mysql { class= ' line-numbers'}
delete from order_2017
where order_id = '0002'
```
### 删除表
```mysql { class= ' line-numbers'}
语法结构
drop table 表名
或者
手动删除
```
练习：删除名字为'order_2017'的表
`DROP table order_2017;`

### 删除数据库
```mysql { class= ' line-numbers'}
语法结构：
drop database 数据库名;
或者
手动删除
```
练习：删除名字为'learning'的数据库
`DROP database learning;`
### delete 与 drop 的区别
- delete删除表中的内容，不删除表；（砍树枝、砍树叶）
```mysql
删除特定行：
delete from 表名 #从哪张表中删除
where 条件 #删除的条件


```

- drop删除表或者数据库；（将树连根拔起）

```mysql { class= ' line-numbers'}
drop database 数据库名;
drop table 表名
#删除列Drop
ALTER TABLE 表名
DROP 列名

```
## 总结
多刷题，多练习，多总结思路，多总结写某一类查询的模板，孰能生巧
1、case when函数怎么用？
2、分组排序取top值怎么写？
3、union和union all有什么区别？
4、对表的一些操作命令：创建、更新、插入、删除
5、join的类型有哪些？join的语法结构持


# 刷题
