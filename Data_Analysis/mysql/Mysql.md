/**
* @module Mysql
* @Version :
* @Author: Dillon
* @Contact: aa269440877@outlook.com
* @WebSite    :   https://github.com/ld269440877/
* @description:
**/

# 软件安装

## MySQL 8.0

- [安装MySQL预安装](MySQL预安装说明-必读.txt)

[数据库的官网](http://www.mysql.com)下载MySQL
- [Windows安装mysql.pdf](Windows安装mysql.pdf)
- [mysql添加环境变量windows.pdf](mysql添加环境变量windows.pdf)
- [Windows10系统下，彻底删除卸载MySQL.pdf](Windows10系统下，彻底删除卸载MySQL.pdf)

## Navicat 安装

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
## 新建数据库  

- 新建的数据库是demo
![新建数据库](新建数据库.png '新建数据库')
utf8通用字符集，utf8mb4是utf8的扩展支持emoji，用于社交产品
![设置MySQL数据库编码规则](设置MySQL数据库编码规则.png '设置MySQL数据库编码规则')

## 新建数据表

[数据库三范式 - - SegmentFault 思否](https://segmentfault.com/a/1190000020754804)

### 新建字段
![识别号id主键](识别号id主键.png '识别号id主键')

|  名   |          类型           |           长度           |          小数点           |           不是null           |            虚拟            |                  键                  |       注释       |
| :---: | :---------------------: | :----------------------: | :-----------------------: | :--------------------------: | :------------------------: | :----------------------------------: | :--------------: |
|  id   |           int           |    0 (代表自适应长度)    | 0（一般不会去设置小数点） | id不是null空值（必须有数据） | 不勾选虚拟 567版本中不常用 | 选择键 小钥匙代表标识本字段名id为唯一标识符，数据不能出现重复  | 注释字段名id属性 |
| name  | varchar（不定长字符串） | 10 （字符串长度为10   ） |        0（小数点）        |          bushinull           |       虚拟默认不勾选       | 键不勾选（因已选择id作为唯一标识符） |     注释姓名     |
|       |        |       |        |            |         |    |       |

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

