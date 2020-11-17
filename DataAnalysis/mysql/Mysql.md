[(Forward to 总结)](#总结)
[(Forward to SQL查询语言-基础)](#SQL查询语言-基础)
[(Forward to SQL基础查询语言-高阶)](#SQL查询语言-高阶)

![数据分析知识参考体系](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/数据分析知识参考体系.png '数据分析知识参考体系')

# MySQL思维导图

![MySQL思维导图](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/MySQL思维导图.png)

# 软件安装

## Windows MySQL 8.0

- [安装MySQL预安装](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/MySQL预安装说明-必读.txt)

[数据库的官网](http://www.mysql.com)下载MySQL
- [Windows安装mysql.pdf](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Windows安装mysql.pdf)
- [mysql添加环境变量windows.pdf](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/mysql添加环境变量windows.pdf)
- [Windows10系统下，彻底删除卸载MySQL.pdf](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Windows10系统下，彻底删除卸载MySQL.pdf)

[MySQL数据库安装与配置详解 - daixinet.com - 博客园](https://www.cnblogs.com/sshoub/p/4321640.html)

## sign in mysql  on windows by cmd

```bash
#C:\Users\Dillon>
mysql -u root -h localhost -p
# Enter password: Aaqq
#Welcome to the MySQL monitor.  Commands end with ; or \g.
#Your MySQL connection id is 20
#Server version: 8.0.22 MySQL Community Server - GPL

#Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

#Oracle is a registered trademark of Oracle Corporation and/or its
#affiliates. Other names may be trademarks of their respective
#owners.

#Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
退出MySQL 
mysql>`exit` 或 `quit`
```

##  CentOS7 安装Mysql

[Failed to start mysqld.service: Unit not found - Jefsky-程序猿甜品店](https://www.jefsky.com/archives/506.html)

###  安装mysql

```sh
yun install mysql
```

### 启动mysql

```sh
systemctl start mysql.service
```

###  出现以下提示

```sh
# Failed to start mysqld.service: Unit not found
```



###  解决

```sh
# 安装mariadb-server
yum install -y mariadb-server

# 启动服务
systemctl start mariadb.service

# 开机启动
systemctl enable mariadb.service

# 进行一些安全设置，以及修改数据库管理员密码

# mysql安全配置及修改数据库管理员密码
mysql_secure_installation

# Thanks for using MariaDB!


# start MariaDB
mysql -u root -h localhost -p

# Welcome to the MariaDB monitor.  Commands end with ; or \g.
# Your MariaDB connection id is 28
# Server version: 10.3.17-MariaDB MariaDB Server

# Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# MariaDB [(none)]> help 
```

```mysql
# 开启远程访问权限
MariaDB [(none)]> use mysql;
# Database changed

MariaDB [mysql]> show databases;

+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.000 sec)

# 开启远程访问权限--------   报错：语法错误 
select User,authentication_string,Host from user；
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456';
flush privileges;
```

 ##  Mysql 服务器 Ubuntu 端安装

- 安装服务器端：在终端中输入如下命令，回车后，然后按照提示输入

```
sudo apt-get install mysql-server
```

- 当前使用的ubuntu镜像中已经安装好了mysql服务器端，无需再安装，并且设置成了开机自启动
- 服务器用于接收客户端的请求、执行sql语句、管理数据库
- 服务器端一般以服务方式管理，名称为mysql
- 启动服务

```
sudo service mysql start
```

- 查看进程中是否存在mysql服务

```
ps ajx|grep mysql
```

![image-20201115190714590](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115203212.png)

- 停止服务

```
sudo service mysql stop
```

- 重启服务

```
sudo service mysql restart
```

### 配置

- 配置文件目录为`/etc/mysql/mysql.cnf`

![image-20201115190759568](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115203213.png)

- 进入conf.d目录，打开mysql.cnf，发现并没有配置
- 进入mysql.conf.d目录，打开mysql.cnf，可以看到配置项

![image-20201115190827565](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115190827.png)

- 主要配置项如下

```
bind-address表示服务器绑定的ip，默认为127.0.0.1

port表示端口，默认为3306

datadir表示数据库目录，默认为/var/lib/mysql

general_log_file表示普通日志，默认为/var/log/mysql/mysql.log

log_error表示错误日志，默认为/var/log/mysql/error.log
```

##  navicat 客户端 Ubuntu 安装

- 客户端为开发人员与dba使用，通过socket方式与服务端通信，常用的有navicat、命令行mysql

### 图形化界面客户端navicat

- 可以到[Navicat官网](https://www.navicat.com.cn/)下载
- 将压缩文件拷贝到ubuntu虚拟机中，放到桌面上，解压

```bash
tar zxvf navicat112_mysql_cs_x64.tar.gz
```

- 进入解压的目录，运行如下命令

```bash
./start_navicat
```

- 启动如下图，详细功能见下节

![image-20201115190955148](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115203214.png)



- 点击两次“取消”按钮后如下图

![image-20201115191014275](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191014.png)

- 点击“试用”按钮后如下图

![image-20201115191033249](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191033.png)

- 问题一：中文乱码
- 解决：打开start_navicat文件

```
将export LANG="en_US.UTF-8"改为export LANG="zh_CN.UTF-8"
```

- 问题二：试用期
- 解决：删除用户目录下的.navicat64目录

```
cd ~
rm -r .navicat64
```

#### 命令行客户端

- 在终端运行如下命令，按提示填写信息

```
sudo apt-get install mysql-client
```

- 当前使用的ubuntu镜像中已经安装好了mysql客户端，无需再安装
- 详细连接的命令可以查看帮助文档

```
mysql --help
```

- 最基本的连接命令如下，输入后回车

```
mysql -u root -pmysql
```

- 连接成功后提示如下图

![image-20201115191113737](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191113.png)

- 按ctrl+d或输入如下命令退出

```mysql
quit 或者 exit
```

###  Navicat连接 Ubuntu

- 打开navicat，点击工具栏的“连接”，选择“mysql”，弹出窗口如下图
- ![image-20201115191334986](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191335.png)

- 在弹出的窗口中填写名称、主机ip、端口、用户名、密码，如下图

- 密码为mysql

  ![image-20201115191406882](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191407.png)

- 点击确定，在左侧栏会看到刚才填写的名称，双击打开连接，如下图

![image-20201115191425313](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191425.png)



### 创建数据库

- 在左侧栏空白处右击，选择“新建数据库”，点击

![image-20201115191518142](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191518.png)

- 点击后弹出新窗口，填写数据库名称并选择语言如下图

![image-20201115191542559](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191542.png)

- 填写完成后点击“确定”创建数据库，在左侧会出现刚才创建的数据库，双击打开

![image-20201115191601843](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191601.png)

###  编辑数据库

- 在左侧栏数据库上右击，弹出菜单，如下图

![image-20201115191623823](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191623.png)

- 选择“编辑数据库”，可以修改字符集、排序规则，如下图

![image-20201115191641458](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115203215.png)

- 选择“转储sql文件”，可以完成结构和数据的备份，如下图：

![image-20201115191657254](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115203216.png)

- 选择“删除数据库”，可以将数据库删除

###  创建数据表

- 点击工具栏“表”，在第二行显示关于表的命令，点击“创建表”

![image-20201115191729977](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191730.png)



- 弹出新窗口，按照上节的设计，创建班级表，填写各字段，选择相应的类型

![image-20201115191746353](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191746.png)

- 对于id字段，需要设置为int类型，无符号，自动增长，主键，非空
- 对于字符串类型，必须指定包含字符个数，还需要指定字符集、排序规则，默认与数据库的一致
- datetime的默认值可以设置成now(),也可以是一个具体值，如'2000-1-1'
- 按照同样的方式创建学生表students

![image-20201115191808222](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191808.png)

### 编辑数据表

- 选择一张表后，工具栏的第二行“打开表”、“设计表”、“删除表”都变的可用

![image-20201115191831419](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115191831.png)

- 打开表会查看表的当前数据，可以在这个窗口中增加、修改、删除数据
- 设计表和创建表的窗口一样，可以增加、修改、删除字段，或编辑字段的类型、约束
- 删除表会将表物理删除

### 查看数据

- 双击表，或者选择表后，点击工具栏第二行的“打开表”，可以查看表的数据

![image-20201115191916713](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115203217.png)

### 增加数据

- 默认没有数据，可以在对应的列中填写数据，点击底部的对勾完成添加
- 注意：自动增长的主键列不需要填写值

![image-20201115191934817](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115203218.png)

### 增加数据

- 默认没有数据，可以在对应的列中填写数据，点击底部的对勾完成添加
- 注意：自动增长的主键列不需要填写值

<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115192033.png" alt="20201115192033"  title="20201115192033" width="600" height="" /><figcaption><font color=green>20201115192033</font></figcaption></center></figure>

- 如果需要继续添加数据，点击询问的加号，会出现一个新的空白行，填写数据即可

![image-20201115192115437](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115192115.png)

### 修改数据

- 点击某个单元格，即可编辑值，修改完后，点击底部的勾生效

![image-20201115192139176](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115203219.png)



### 删除数据

- 点击某个单元格，再点击询问的减号，可以删除

![image-20201115192159086](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115203220.png)

- 说明：对于重要数据，推荐将isdelete属性改为1，而不是进行物理删除

## 命令行连接

- 在工作中主要使用命令操作方式，要求熟练编写
- 打开终端，运行命令

```mysql
mysql -uroot -p
回车后输入密码，当前设置的密码为mysql
```

- 连接成功后如下图

![image-20201115192302725](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115192302.png)

- 退出登录

```
quit 和 exit
或
ctrl+d
```

- 登录成功后，输入如下命令查看效果

```
查看版本：select version();
显示当前时间：select now();
```

### 修改输入提示符

```
prompt python>
```

- \D 完整日期
- \U 使用用户



## Navicat windows 安装

[Navicat | 产品](https://www.navicat.com.cn/products)

- [Navicat安装.pdf](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat安装.pdf)



# MySQL 基础

[一张图带你过SQL基础知识(思维导图) - chenbifeng的专栏 - CSDN博客](https://blog.csdn.net/chenbifeng/article/details/65936304)

关系数据库（Relational database）
:   是创建在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据。

现实世界中的各种实体以及实体之间的各种联系均用关系模型来表示。关系模型是由埃德加·科德于1970年首先提出的，并配合“科德十二定律”。
**标准数据查询语言SQL**就是一种基于关系数据库的语言，这种语言执行对关系数据库中数据的检索和操作。
> SQL是结构化查询语言，是一种用来操作RDBMS的数据库语言，当前关系型数据库都支持使用SQL语言进行操作，也就是说可以通过SQL操作oracle、sql server、mysql、sqlite等等所有的关系型的数据库
**关系模型**由关系数据结构、==关系操作集合==、关系完整性约束三部分组成。
![模板Database](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/模板Database.png "模板Database")
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

![表Relation](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/表Relation.png '表Relation')

> 通过客户端RDBMS-client给数据库的服务器RDBMS-server发送SQL 指令，完成数据库、数据表和数据的基本操作
数据库（就是文件）是数据表的集合，数据表是数据的集合，数据包含很多列
==RDBMS==：Relational Database Management System
![(客户端通过SQL语言服务器](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/客户端通过SQL语言服务器.png '客户端通过SQL语言服务器')
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

## 启动/退出关系数据库管理系统(**RDBMS**)服务

- 本机启动  服务（本地） 启动MySQL服务
- 终端  连接sql服务 `mysql -u账号  -p密码`
- 退出MySQL `exit` 或 `quit`
- 登录成功后


## 连接关系数据库管理系统(**RDBMS**)

- Navicat连接
- 新建的连接名是数据分析
    - Navicat 充当MySQL客户端的角色，localhost=127.0.01
![启动Navicat连接MySQL](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/启动Navicat连接MySQL.png '启动Navicat连接MySQL')
![Navicat-MySQL](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat-MySQL.png 'Navicat-MySQL')
- 上一步设置的双击连接名 绿色为当前连接的数据库，灰色为未连接
    - 不要删除系统级别的数据库，否则只能重新安装数据库

## 数据导入

![Navicat数据导入导出](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat数据导入导出.png 'Navicat数据导入导出')
- 根据“导入向导”和“导出向导”来导入/导出数据
-选择导入格式—选择文件—附加选项—选择目标表(或将原表重命名）—表结构—导入模式—开始导入—导入成功
    - 选择导入格式
![Navicat数据导入选择导入格式](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat数据导入选择导入格式.png 'Navicat数据导入选择导入格式')
    - 选择文件
      ![Navicat数据导入选择文件](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat数据导入选择文件.png 'Navicat数据导入选择文件')
- 附加选项
    ![Navicat数据导入附加选项](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat数据导入附加选项.png 'Navicat数据导入附加选项')
    - 选择目标表
    ![Navicat数据导入选择目标表](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat数据导入选择目标表.png 'Navicat数据导入选择目标表')
    - 表结构
    ![Navicat数据导入表结构.](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat数据导入表结构.png 'Navicat数据导入表结构.')
    - 导入模式
    ![Navicat数据导入导入模式](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat数据导入导入模式.png 'Navicat数据导入导入模式')
    - 开始导入
    - 导入成功==Finished successfully==

## 数据导出
- 选择导出格式——选择导出的文件——选择导出字段——附加选项——开始导出——导出成功
    - 选择导出格式
    ![Navicat数据导出选择导出格式](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat数据导出选择导出格式.png 'Navicat数据导出选择导出格式')
    - 选择导出的文件
    ![Navicat数据导出选择导出的文件](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat数据导出选择导出的文件.png 'Navicat数据导出选择导出的文件')
    - 选择导出字段
    ![Navicat数据导出选择导出字段](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat数据导出选择导出字段.png 'Navicat数据导出选择导出字段')
    - 附加选项
    ![Navicat数据导出附加选项](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/Navicat数据导出附加选项.png 'Navicat数据导出附加选项')
    - 开始导出
    - 导出成功==Finished successfully==

## 新建数据库  

![数据库-表](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/数据库-表.png '数据库-表')
![数据库-表-查询](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/数据库-表-查询.png '数据库-表-查询' )

- 新建的数据库是demo
![新建数据库](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/新建数据库.png '新建数据库')
utf8通用字符集，utf8mb4是utf8的扩展支持emoji，用于社交产品
![设置MySQL数据库编码规则](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/设置MySQL数据库编码规则.png '设置MySQL数据库编码规则')

## 新建数据表

[数据库三范式 - - SegmentFault 思否](https://segmentfault.com/a/1190000020754804)

### 新建字段
![识别号id主键](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/识别号id主键.png '识别号id主键')

|  名   |          类型           |           长度           |          小数点           |           不是null           |            虚拟            |                              键                               |       注释       |
| :---: | :---------------------: | :----------------------: | :-----------------------: | :--------------------------: | :------------------------: | :-----------------------------------------------------------: | :--------------: |
|  id   |           int           |    0 (代表自适应长度)    | 0（一般不会去设置小数点） | id不是null空值（必须有数据） | 不勾选虚拟 567版本中不常用 | 选择键 小钥匙代表标识本字段名id为唯一标识符，数据不能出现重复 | 注释字段名id属性 |
| name  | varchar（不定长字符串） | 10 （字符串长度为10   ） |        0（小数点）        |          bushinull           |       虚拟默认不勾选       |             键不勾选（因已选择id作为唯一标识符）              |     注释姓名     |
|       |                         |                          |                           |                              |                            |                                                               |                  |

### 保存表
![新建id字段为唯一标识](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/新建id字段为唯一标识.png '新建id字段为唯一标识')
![新建name字段](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/新建name字段.png '新建name字段')
![新建表classes保存](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/新建表classes保存.png '新建表classes保存')
![修改classes表字段名属性](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/修改classes表字段名属性.png '修改classes表字段名属性')
### 添加数据

![classes表添加数据](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/classes表添加数据.png 'classes表添加数据')

### 新建-保存查询
![新建保存查询](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/新建保存查询.png '新建保存查询')

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
![(数值类型常用](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/数值类型常用.png '(数值类型常用')
![字符串](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/字符串.png '字符串')
![日期时间类型](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/日期时间类型.png '日期时间类型')

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

# 备份

- 运行mysqldump命令

```sql
mysqldump –uroot –p 数据库名 > python.sql;

# 按提示输入mysql的密码
```

# 恢复

- 连接mysql，创建新的数据库
- 退出连接，执行如下命令

```sql
mysql -uroot –p 新数据库名 < python.sql

# 根据提示输入mysql密码
```

# SQL查询语言-基础

[spm_order](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/spm_order.xlsx)
[spm_product](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/spm_product.xlsx)
[spm_area](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/spm_area.xlsx)

[(Back to 软件安装)](#软件安装)
## SQL 简介
![SQL语言框架](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL语言框架.png 'SQL语言框架')

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

![SQLconcat字段1字段2](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQLconcat字段1字段2.png 'SQLconcat字段1字段2')


![SQLconcat字段1字段2AS字段1-字段2](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQLconcat字段1字段2AS字段1-字段2.png 'SQLconcat字段1字段2AS字段1-字段2')

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
![SQL数据分组groupby](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL数据分组groupby.png 'SQL数据分组groupby')

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
![SQL数据过滤having](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL数据过滤having.png 'SQL数据过滤having')

[正确理解MySQL中的where和having的区别 -SegmentFault 思否](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/https://segmentfault.com/a/1190000008284099)
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
![SQL结果排序orderByDesc](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL结果排序orderByDesc.png 'SQL结果排序orderByDesc')

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
![SQL总和sum平均avg最小min最大max](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL总和sum平均avg最小min最大max.png 'SQL总和sum平均avg最小min最大max')
练习3：
查看订单表中的利润和利润的绝对值
```mysql { class= ' line-numbers'}
select sales,abs(profit)
from spm_order
```
![SQL绝对值abs](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL绝对值abs.png 'SQL绝对值abs')

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
![SQL常见时间命令](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL常见时间命令.png 'SQL常见时间命令')

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
![SQL订单月份DATE_FORMAT](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL订单月份DATE_FORMAT.png 'SQL订单月份DATE_FORMAT')
练习4：
在订单表中筛选出订单日期在2018年的所有订单
```mysql { class= ' line-numbers'}
select *
from spm_order
where order_date between "2018-01-01" and "2018-12-31"
```
![SQL_SELECT星号](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL_SELECT星号.png 'SQL_SELECT星号')
![SQL_SELECT字段](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL_SELECT字段.png 'SQL_SELECT字段')

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
![SQL作业1](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL作业1.png 'SQL作业1')

# SQL查询语言-高阶
![SQL查询语言-高阶](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL查询语言-高阶.png 'SQL查询语言-高阶')

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
![SQL-表联结Joins](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL-表联结Joins.png 'SQL-表联结Joins')
#TODO SQL-表联结Join还没看视频  要找网页上的案例解析

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
![SQL条件函数case-when](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL条件函数case-when.png 'SQL条件函数case-when')

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
![SQL分组排序函数Row_number练习1](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL分组排序函数Row_number练习1.png 'SQL分组排序函数Row_number练习1')
练习2：计算销售人员在不同城市的销售额；
要求：结果根据销售人员在不同城市的销售额进行分组排序（降序），并且查询结果要包含分组排名

```mysql { class= ' line-numbers'}
select sales_name,city,sum(sales),ROW_NUMBER() OVER(PARTITION BY sales_name
ORDER BY sum(sales) DESC) as 'rank'
from spm_order
group by sales_name,city
```
![SQL分组排序函数Row_number练习2](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL分组排序函数Row_number练习2.png 'SQL分组排序函数Row_number练习2')

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
![SQL嵌套查询t1](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL嵌套查询t1.png 'SQL嵌套查询t1')

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
![SQL组合查询unionAll](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL组合查询unionAll.png 'SQL组合查询unionAll')

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
![SQL主键与外键](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL主键与外键.png 'SQL主键与外键')

- 主键和外键的区别

|       | 主键                                       | 外键                                                   |
| :---: | :----------------------------------------- | :----------------------------------------------------- |
| 定义  | 唯一标识一条记录，不能有重复的，不允许为空 | 表的外键是另一个表的主键，外键可以有重复的，可以是空值 |
| 作用  | 用来保证数据完整性                         | 用来和其他表建立联系用的                               |
| 个数  | 主键只能有一个                             | 一个表可以有多个外键                                   |
### 索引类型及实例
```mysql { class= ' line-numbers'}
CREATE TABLE `test` (
    `a` int(10) NOT NULL AUTO_INCREMENT,
    `b` int(10) NOT NULL,
    `c` int(10) NOT NULL,
    `d` varchar(32) NOT NULL,
    `e` varchar(64) NOT NULL,
-- 指定`a`是主键索引（唯一且不为空）
    PRIMARY KEY (`a`),
-- 指定`inx_bc`为普通索引，因为索引了两列（`b`和`c`），所以`inx_bc`是组合索引
    KEY `idx_bc` (`b`,`c`),
-- 指定`idx_e`是唯一索引
    UNIQUE KEY `idx_e` (`e`)
) ENGINE=InnoDB AUTO_INCREMENT=20000001 DEFAULT CHARSET=utf8
```
![索引类型及实例下](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/索引类型及实例下.png '索引类型及实例下')

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
![SQL插入数据insertInto练习](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL插入数据insertInto练习.png 'SQL插入数据insertInto练习')

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
![SQL插入数据insertInto练习结果](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL插入数据insertInto练习结果.png 'SQL插入数据insertInto练习结果')

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

# 数据库设计

- 关系型数据库建议在E-R模型的基础上，我们需要根据产品经理的设计策划，抽取出来模型与关系，制定出表结构，这是项目开始的第一步
- 在开发中有很多设计数据库的软件，常用的如power designer，db desinger等，这些软件可以直观的看到实体及实体间的关系
- 设计数据库，可能是由专门的数据库设计人员完成，也可能是由开发组成员完成，一般是项目经理带领组员来完成
- 现阶段不需要独立完成数据库设计，但是要注意积累一些这方面的经验

#### 三范式

- 经过研究和对使用中问题的总结，对于设计数据库提出了一些规范，这些规范被称为范式(Normal Form)

- 目前有迹可寻的共有8种范式，一般需要遵守3范式即可

- ◆ 第一范式（1NF）：强调的是列的原子性，即列不能够再分成其他几列。

  > 考虑这样一个表：【联系人】（姓名，性别，电话） 如果在实际场景中，一个联系人有家庭电话和公司电话，那么这种表结构设计就没有达到 1NF。要符合 1NF 我们只需把列（电话）拆分，即：【联系人】（姓名，性别，家庭电话，公司电话）。1NF 很好辨别，但是 2NF 和 3NF 就容易搞混淆。

- ◆ 第二范式（2NF）：首先是 1NF，另外包含两部分内容，一是表必须有一个主键；二是没有包含在主键中的列必须完全依赖于主键，而不能只依赖于主键的一部分。

  > 考虑一个订单明细表：【OrderDetail】（OrderID，ProductID，UnitPrice，Discount，Quantity，ProductName）。 因为我们知道在一个订单中可以订购多种产品，所以单单一个 OrderID 是不足以成为主键的，主键应该是（OrderID，ProductID）。显而易见 Discount（折扣），Quantity（数量）完全依赖（取决）于主键（OderID，ProductID），而 UnitPrice，ProductName 只依赖于 ProductID。所以 OrderDetail 表不符合 2NF。不符合 2NF 的设计容易产生冗余数据。
  >
  > 可以把【OrderDetail】表拆分为【OrderDetail】（OrderID，ProductID，Discount，Quantity）和【Product】（ProductID，UnitPrice，ProductName）来消除原订单表中UnitPrice，ProductName多次重复的情况。

- ◆ 第三范式（3NF）：首先是 2NF，另外非主键列必须直接依赖于主键，不能存在传递依赖。即不能存在：非主键列 A 依赖于非主键列 B，非主键列 B 依赖于主键的情况。

  > 考虑一个订单表【Order】（OrderID，OrderDate，CustomerID，CustomerName，CustomerAddr，CustomerCity）主键是（OrderID）。 其中 OrderDate，CustomerID，CustomerName，CustomerAddr，CustomerCity 等非主键列都完全依赖于主键（OrderID），所以符合 2NF。不过问题是 CustomerName，CustomerAddr，CustomerCity 直接依赖的是 CustomerID（非主键列），而不是直接依赖于主键，它是通过传递才依赖于主键，所以不符合 3NF。 通过拆分【Order】为【Order】（OrderID，OrderDate，CustomerID）和【Customer】（CustomerID，CustomerName，CustomerAddr，CustomerCity）从而达到 3NF。 *第二范式（2NF）和第三范式（3NF）的概念很容易混淆，区分它们的关键点在于，2NF：非主键列是否完全依赖于主键，还是依赖于主键的一部分；3NF：非主键列是直接依赖于主键，还是直接依赖于非主键列。

### 不遵循1NF

![image-20201115192603971](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115192604.png)

### 不遵循2NF

![image-20201115192625364](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115192625.png)

### 不遵循3NF

![image-20201115192645853](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115192646.png)

### 最终表

![image-20201115192703669](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115192703.png)

#### E-R模型

- E表示entry，实体，设计实体就像定义一个类一样，指定从哪些方面描述对象，一个实体转换为数据库中的一个表
- R表示relationship，关系，关系描述两个实体之间的对应规则，关系的类型包括包括一对一、一对多、多对多
- 关系也是一种数据，需要通过一个字段存储在表中
- 实体A对实体B为1对1，则在表A或表B中创建一个字段，存储另一个表的主键值

![image-20201115192723988](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115192724.png)

- 实体A对实体B为1对多：在表B中创建一个字段，存储表A的主键值

![image-20201115192740490](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115192740.png)

- 实体A对实体B为多对多：新建一张表C，这个表只有两个字段，一个用于存储A的主键值，一个用于存储B的主键值

![image-20201115192755228](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115192755.png)

- 想一想：举些例子，满足一对一、一对多、多对多的对应关系

#### 逻辑删除

- 对于重要数据，并不希望物理删除，一旦删除，数据无法找回
- 删除方案：设置isDelete的列，类型为bit，表示逻辑删除，默认值为0
- 对于非重要数据，可以进行物理删除
- 数据的重要性，要根据实际开发决定

#### 示例

- 设计两张表：班级表、学生表
- 班级表classes
  - id
  - name
  - isdelete
- 学生表students
  - id
  - name
  - birthday
  - gender
  - clsid
  - isdelete

#### 扩展阅读

- 看看别人家设计的规范
- [58到家数据库30条军规解读](http://mp.weixin.qq.com/s/Yjh_fPgrjuhhOZyVtRQ-SA)









# MySQL优化项目课件 python操作MySQL
//TODO python操作MySQL  查找网页上的案例解析 掘进或Segmentfault思否
## 不同职位对MySQL的技术要求

- 数据分析
    - 偏重于查询
    - 复杂查询的写法

- 程序员
    - 表的设计
    - 增删改查
    - 注重SQL性能

- ＤＢＡ
    - ＭｙＳＱＬ服务器配置
    - ＳＱＬ＼服务性能＼稳定性
    - 数据一致性

## Python操作MySQL

<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115192952.png" alt="Python 中操作 MySQL 步骤"  title="Python 中操作 MySQL 步骤" width="600" height="" /><figcaption><font color=green>Python 中操作 MySQL 步骤</font></figcaption></center></figure>

- Python DB-API

### 常用模块

- MySQLdb
    - 也就是MySQL-python
    - 底层C实现
- mysql-connector
    - MySQL官方提供
- pymysql
    - Python实现
    - Python Version 3+

### 基本操作

```markdown
# 引入模块
- 在py文件中引入pymysql模块
`from pymysql import *`
# Connection 对象
- 用于建立与数据库的连接
- 创建对象：调用connect()方法
`conn=connect(参数列表)`

- 参数host：连接的mysql主机，如果本机是'localhost'
- 参数port：连接的mysql主机的端口，默认是3306
- 参数database：数据库的名称
- 参数user：连接的用户名
- 参数password：连接的密码
- 参数charset：通信采用的编码方式，推荐使用utf8
## 对象的方法
- close()关闭连接
- commit()提交
- cursor()返回Cursor对象，用于执行sql语句并获得结果
# Cursor对象
- 用于执行sql语句，使用频度最高的语句为select、insert、update、delete
- 获取Cursor对象：调用Connection对象的cursor()方法
`cs1=conn.cursor()`
## 对象的方法
- close()关闭
- execute(operation [, parameters ])执行语句，返回受影响的行数，主要用于执行insert、update、delete语句，也可以执行create、alter、drop等语句
- fetchone()执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
- fetchall()执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
## 对象的属性
- rowcount只读属性，表示最近一次execute()执行后受影响的行数
- connection获得当前连接对象
```



```python
# 连接数据库
import pymysql
db = pymysql.connect(host='127.0.0.1', port=3306)
# 获取游标
cs = db.cursor()
# 选择数据库
db.select_db('test')
# 执行SQL
sql = 'show databases'
result = cs.execute(sql)
dbs = cs.fetchall()
# 关闭数据库连接
db.close()
```



### ORM

- ORM：object relational mapping，对象映射关系
- 使用对象模型而不是sql来操作数据库
- sqlalchemy

### 练习

- 将抓取的数据导入到mysql中
- 编写一个DB类，封装好常用的MySQL操作

## 索引

- 对标中一列或多列的值进行排序
- 定义一种存储结构
- 快速检索到数据
- 村塾引擎级实现

### 索引类型

- 普通索引：MSQL中基本索引类型，没有什么限制，允许在定义索引的列中插入重复值和空值，纯粹为了查询数据快一点
- 唯一索引：索引列中的值必须唯一，但是允许为空值
- 主键索引：是一种特殊的唯一索引，不允许有空值
- 组合索引：在表中的多个字段组合上创建的索引，只有在查询条件中使用了这些字段的左边字段时，索引才会被使用，使用组合索引时遵循遵循最左前缀集合
- 全文索引：通过大文本中的某个关键字，就能找到该字段所属的记录行
- 空间索引：空间索引是对空间数据的类型的字段建立的索引。
    - MySQL中的空间数据类型：
        - GEOMETRY
        - POINT
        - LINESTRING
        - POLYGON
相関概念：
    - 非聚簇索引：索引树的叶子节点存储数据的位置信息
    - 聚簇索引：数据存储在索引树的叶子节点
    - 覆盖索引：索引包含了（或覆盖了）查询语句中的字段与条件的数据
注意事项：
    - 执行查询时，MySQL只能使用一个索引
    - 提高了查询速度，降低了更新速度
    - 不要使用like“%aaa%”操作
    - 越小的数据类型通常更好
    - 简单的数据类型更好
    -尽量避免NULL
    - 最左前缀：组合索引中的左边列
### InnoDB 及MyISAM索引结构

- MyISAM引擎：使用b+tree作为索引，叶子节点data存放的是吉利地址。MyISAM中柱索引与辅索引形式是一样，主索引要求key不能重复，附注索引key可以重复
- InnoDB引擎：与MyISAM索引和数据分开存放不同的是，InnoDB引擎数据文件本身就是一个索引，InnoDB引擎数据是按b+tree结构组织存放的，叶子节点包含全部的数据信息，InnoDB引擎辅助索引叶子节点存放的是主键，所以，InnoDB的普通索引，实际上会扫描两遍：
    - 第一遍，有普通索引找到PK；
    - 第二遍，有PK找到行记录‘

![InnoDB%20及MyISAM索引结构](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQLInnoDB%20及MyISAM索引结构.png 'InnoDB%20及MyISAM索引结构')

```mysql { class= ' line-numbers'}
mysql> select * from tb;
+----+-----+-------+
| id | age | name |
+----+-----+-------+
| 15 | 34 | Bob |
| 18 | 77 | Alice |
| 20 | 5 | Jim |
| 30 | 91 | Eric |
| 49 | 22 | Tom |
| 50 | 89 | Rose |
+----+-----+-------+

# idx_name

CREATE TABLE `tb` (
`id` int(10) NOT NULL auto_increment,
`age` int(10) NOT NULL,
`name` varchar(32) NOT NULL,
PRIMARY KEY (`id`),
KEY `idx_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
 ![InnoDB及MyISAM索引结构-主键primarykey-idx_name](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQLInnoDB及MyISAM索引结构-主键primarykey.png 'InnoDB及MyISAM索引结构-主键primarykey-idx_name')
![InnoDB及MyISAM索引结构-辅键secondarykey-idx_name](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQLInnoDB及MyISAM索引结构-辅键secondarykey.png 'InnoDB及MyISAM索引结构-辅键secondarykey-idx_name')


```mysql { class= ' line-numbers'}

# idx_age

CREATE TABLE `tb` (
`id` int(10) NOT NULL auto_increment,
`age` int(10) NOT NULL,
`name` varchar(32) NOT NULL,
PRIMARY KEY (`id`),
KEY `idx_age` (`age`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

```
![InnoDB及MyISAM索引结构-主键primarykey-idx_age](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQLInnoDB及MyISAM索引结构-主键primarykey-idx_age.png 'InnoDB及MyISAM索引结构-主键primarykey-idx_age')
![InnoDB及MyISAM索引结构-辅键secondarykey-idx_age](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQLInnoDB及MyISAM索引结构-辅键secondarykey-idx_age.png 'InnoDB及MyISAM索引结构-辅键secondarykey-idx_age')


### 事务

- 原子性 atomicity
- 一致性 consistency
- 隔离性 isolation
- 持久性 durability

## 实战案例

### 设计一个应用商店的数据库
- APP信息表
- APP扩展信息表
- APP分类表
- APP分类关系表
- APP评论表
- 用户安装信息表
- APP评分
### SQL优化

#### 一般的优化原则

一般来说，查询性能低，原因是访问了太多的数据
- 是否请求了不需要的数据
- 不需要的列不提取，不需要的行不取
- 对索引查找使用where子句消除不匹配的行
- 使用覆盖索引（Extra列是Using Index）避免访问的行
- 从表中检索出数据，过滤掉不匹配的行（Extra列是Using Where）
- 更改架构，例如使用汇总表，将分析的结果进行汇总
- 将一个复杂的查询分解成多个简单的查询
- 批量处理法
    - 对于需要处理大量数据的语句，批量进行处理

#### 索引的优化

- 使用自增ID做主键primary key，业务逐渐做unique key
- 一般来说，status，type这类枚举值很少的字段，不适合单独作为索引字段
-索引并不是越多越好，无用、冗余的索引要删除
- 不要使用%XXX%这种模糊匹配，会导致全表扫描/索引全扫描

# MySQL 性能优化神器 Explain 使用分析
[MySQL 性能优化神器 Explain 使用分析 -  SegmentFault 思否](https://segmentfault.com/a/1190000008131735)
[MySQL优化学习笔记之explain - 掘金](https://juejin.im/post/5bd11e0651882529306e0546)

## 简介
MySQL 提供了一个 EXPLAIN 命令, 它可以对 SELECT 语句进行分析, 并输出 SELECT 执行的详细信息, 以供开发人员针对性优化.
EXPLAIN 命令用法十分简单, 在 SELECT 语句前加上 Explain 就可以了, 例如:
`EXPLAIN SELECT * from user_info WHERE  id < 300;`
## 准备
为了接下来方便演示 EXPLAIN 的使用, 首先我们需要建立user_info和order_info两个测试用的表, 并添加相应的数据:
```mysql { class= ' line-numbers'}

<!-- user_info -->


CREATE TABLE `user_info` (
  `id`   BIGINT(20)  NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL DEFAULT '',
  `age`  INT(11)              DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `name_index` (`name`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8

# 先创建表user_info 然后在表user_info 中插入数据

INSERT INTO user_info (name, age) VALUES ('xys', 20);
INSERT INTO user_info (name, age) VALUES ('a', 21);
INSERT INTO user_info (name, age) VALUES ('b', 23);
INSERT INTO user_info (name, age) VALUES ('c', 50);
INSERT INTO user_info (name, age) VALUES ('d', 15);
INSERT INTO user_info (name, age) VALUES ('e', 20);
INSERT INTO user_info (name, age) VALUES ('f', 21);
INSERT INTO user_info (name, age) VALUES ('g', 23);
INSERT INTO user_info (name, age) VALUES ('h', 50);
INSERT INTO user_info (name, age) VALUES ('i', 15);

<!-- order_info -->


CREATE TABLE `order_info` (
  `id`           BIGINT(20)  NOT NULL AUTO_INCREMENT,
  `user_id`      BIGINT(20)           DEFAULT NULL,
  `product_name` VARCHAR(50) NOT NULL DEFAULT '',
  `productor`    VARCHAR(30)          DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_product_detail_index` (`user_id`, `product_name`, `productor`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8

# 先创建表order_info  然后在表order_info  中插入数据

INSERT INTO order_info (user_id, product_name, productor) VALUES (1, 'p1', 'WHH');
INSERT INTO order_info (user_id, product_name, productor) VALUES (1, 'p2', 'WL');
INSERT INTO order_info (user_id, product_name, productor) VALUES (1, 'p1', 'DX');
INSERT INTO order_info (user_id, product_name, productor) VALUES (2, 'p1', 'WHH');
INSERT INTO order_info (user_id, product_name, productor) VALUES (2, 'p5', 'WL');
INSERT INTO order_info (user_id, product_name, productor) VALUES (3, 'p3', 'MA');
INSERT INTO order_info (user_id, product_name, productor) VALUES (4, 'p1', 'WHH');
INSERT INTO order_info (user_id, product_name, productor) VALUES (6, 'p1', 'WHH');
INSERT INTO order_info (user_id, product_name, productor) VALUES (9, 'p8', 'TE');

```
## Explain的作用:

- 表的读取顺序
- 数据读取操作的操作类型
- 哪些索引可以使用
- 哪些索引被实际使用
- 表之间的引用
- 每张表有多少行被优化器查询

## EXPLAIN 输出格式

EXPLAIN 命令的输出内容大致如下:
```mysql { class= ' line-numbers'}
 explain select * from user_info where id = 2
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: user_info
   partitions: NULL
         type: const
possible_keys: PRIMARY
          key: PRIMARY
      key_len: 8
          ref: const
         rows: 1
     filtered: 100.00
        Extra: NULL
1 row in set, 1 warning (0.00 sec)
```

> 各列的含义如下:
>- id: SELECT 查询的标识符. 每个 SELECT 都会自动分配一个唯一的标识符.
>- select_type: SELECT 查询的类型.
>- table: 查询的是哪个表
>- partitions: 匹配的分区
>- type: join 类型
>- possible_keys: 此次查询中可能选用的索引
>- key: 此次查询中确切使用到的索引.
>- ref: 哪个字段或常数与 key 一起被使用
>- rows: 显示此查询一共扫描了多少行. 这个是一个估计值.
>- filtered: 表示此查询条件所过滤的数据的百分比
>- extra: 额外的信息

## 查询结果返回字段分析：

### id

select查询的序列号，包含一组数字，表示查询中执行select子句或操作表的顺序。id如果相同，可以认为是一个分组，从上往下顺序执行。id不同，id值越大，优先级越高，越先执行。
### select_type字段
- select_type 表示查询的类型，主要用于区别普通查询、联合查询、子查询等的复杂查询, 它的常用取值有:

|  id   |    select_type     | remark                                                                                        |
| :---: | :----------------: | :-------------------------------------------------------------------------------------------- |
|   1   |       SIMPLE       | 简单的select查询，查询中不包含子查询或UNION                                                   |
|   2   |      PRIMARY       | 查询中如果包含任何复杂的子部分，最外层查询则标记为PRIMARY                                     |
|   3   |       UNION        | 表示此查询是 UNION 的第二或随后的查询                                                         |
|   4   |  DEPENDENT UNION   | UNION 中的第二个或后面的查询语句, 取决于外面的查询                                            |
|   5   |      DERIVED       | 在FROM列表中包含的子查询被标记为DERIVED(衍生),MySQL会递归执行这些子查询，把结果放在临时表里。 |
|   6   |    UNION RESULT    | UNION 的结果                                                                                  |
|   7   |      SUBQUERY      | 在SELECT或WHERE列表中包含了子查询，子查询中的第一个 SELECT                                    |
|   8   | DEPENDENT SUBQUERY | 子查询中的第一个 SELECT, 取决于外面的查询. 即子查询依赖于外层查询的结果.                      |

最常见的查询类别应该是 SIMPLE 了, 比如当我们的查询没有子查询, 也没有 UNION 查询时, 那么通常就是 SIMPLE 类型, 例如:
```mysql { class= ' line-numbers'}
mysql> explain select * from user_info where id = 2
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: user_info
   partitions: NULL
         type: const
possible_keys: PRIMARY
          key: PRIMARY
      key_len: 8
          ref: const
         rows: 1
     filtered: 100.00
        Extra: NULL
1 row in set, 1 warning (0.00 sec)
```
如果我们使用了 UNION 查询, 那么 EXPLAIN 输出 的结果类似如下:
```mysql { class= ' line-numbers'}
mysql> EXPLAIN (SELECT * FROM user_info  WHERE id IN (1, 2, 3))
    -> UNION
    -> (SELECT * FROM user_info WHERE id IN (3, 4, 5));
+----+--------------+------------+------------+-------+---------------+---------+---------+------+------+----------+-----------------+
| id | select_type  | table      | partitions | type  | possible_keys | key     | key_len | ref  | rows | filtered | Extra           |
+----+--------------+------------+------------+-------+---------------+---------+---------+------+------+----------+-----------------+
|  1 | PRIMARY      | user_info  | NULL       | range | PRIMARY       | PRIMARY | 8       | NULL |    3 |   100.00 | Using where     |
|  2 | UNION        | user_info  | NULL       | range | PRIMARY       | PRIMARY | 8       | NULL |    3 |   100.00 | Using where     |
| NULL | UNION RESULT | <union1,2> | NULL       | ALL   | NULL          | NULL    | NULL    | NULL | NULL |     NULL | Using temporary |
+----+--------------+------------+------------+-------+---------------+---------+---------+------+------+----------+-----------------+
3 rows in set, 1 warning (0.00 sec)
```
### table字段
table: 显示这一行数据是关于哪张表的。
表示查询涉及的表或衍生表

### type字段
type 字段比较重要,  显示访问类型,它提供了判断查询是否高效的重要依据依据. 通过 ==type 字段==, 我们判断此次查询是 ==全表扫描== 还是 ==索引扫描== 等.
type 常用类型
type 常用的取值有:

id|type|remark
|:-:|:-:|:-|
1|system|表只有一行记录(等于系统表),这是const类型的特列，平时不会出现，这个也可以忽略不计
2|const|表示通过索引一次就找到了,const用于比较primary key或者unique索引。因为只匹配一行数据，所以很快。如将主键置于where列表中，MySQL就能将该查询转换为一个常量
3|eq_ref|唯一性索引扫描，对于每个索引键，表中只有一条记录与之匹配。常见于主键或唯一索引扫描
4|ref|非唯一性索引扫描，返回匹配某个单独值的所有行。本质上也是一宗索引访问，它返回所有匹配某个单独值的行，然而它可能会找到多个符合条件的行，所以他应该属于查找和扫描的混合体
5|range|只检索给定范围的行，使用一个索引来选择行。key列显示使用了哪个索引。一般就是在where语句中出现了between、<、>、in等的查询。这种范围扫描索引比权标扫描要好，因为它只需要开始于索引的某一点，而结束于另一点，不用扫描全部索引。
6|index|Full Index Scan, index与ALL区别为index类型只遍历索引数。这通常比ALL快，因为索引文件通常比数据文件小。(虽然all和index都是读全表，但index是从索引中读取，而all是从硬盘中读取)
7|all|Full Table Scan，将遍历全表以找到匹配的行

> 显示查询使用了何种类型,从最好到最差依次是： system>const>eq_ref>ref>range>index>ALL
一般来说，得保证查询至少达到range级别，最好能达到ref。

- system: 表中只有一条数据. 这个类型是特殊的 const 类型.
- const: 针对主键或唯一索引的等值查询扫描, 最多只返回一行数据. const 查询速度非常快, 因为它仅仅读取一次即可.

例如下面的这个查询, 它使用了主键索引, 因此 type 就是 const 类型的.
```mysql { class= ' line-numbers'}
mysql> explain select * from user_info where id = 2
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: user_info
   partitions: NULL
         type: const
possible_keys: PRIMARY
          key: PRIMARY
      key_len: 8
          ref: const
         rows: 1
     filtered: 100.00
        Extra: NULL
1 row in set, 1 warning (0.00 sec)

```
- eq_ref: 此类型通常出现在多表的 join 查询, 表示对于前表的每一个结果, 都只能匹配到后表的一行结果. 并且查询的比较操作通常是 =, 查询效率较高. 例如:

```mysql { class= ' line-numbers'}
mysql> EXPLAIN SELECT * FROM user_info, order_info WHERE user_info.id = order_info.user_id\G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: order_info
   partitions: NULL
         type: index
possible_keys: user_product_detail_index
          key: user_product_detail_index
      key_len: 314
          ref: NULL
         rows: 9
     filtered: 100.00
        Extra: Using where; Using index
*************************** 2. row ***************************
           id: 1
  select_type: SIMPLE
        table: user_info
   partitions: NULL
         type: eq_ref
possible_keys: PRIMARY
          key: PRIMARY
      key_len: 8
          ref: test.order_info.user_id
         rows: 1
     filtered: 100.00
        Extra: NULL
2 rows in set, 1 warning (0.00 sec)
```
- ref: 此类型通常出现在多表的 join 查询, 针对于非唯一或非主键索引, 或者是使用了 最左前缀 规则索引的查询.
例如下面这个例子中, 就使用到了 ref 类型的查询:
```mysql { class= ' line-numbers'}
mysql> EXPLAIN SELECT * FROM user_info, order_info WHERE user_info.id = order_info.user_id AND order_info.user_id = 5\G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: user_info
   partitions: NULL
         type: const
possible_keys: PRIMARY
          key: PRIMARY
      key_len: 8
          ref: const
         rows: 1
     filtered: 100.00
        Extra: NULL
*************************** 2. row ***************************
           id: 1
  select_type: SIMPLE
        table: order_info
   partitions: NULL
         type: ref
possible_keys: user_product_detail_index
          key: user_product_detail_index
      key_len: 9
          ref: const
         rows: 1
     filtered: 100.00
        Extra: Using index
2 rows in set, 1 warning (0.01 sec)
```
- range: 表示使用索引范围查询, 通过索引字段范围获取表中部分数据记录. 这个类型通常出现在 =, <>, >, >=, <, <=, IS NULL, <=>, BETWEEN, IN() 操作中.
当 type 是 range 时, 那么 EXPLAIN 输出的 ref 字段为 NULL, 并且 key_len 字段是此次查询中使用到的索引的最长的那个.

例如下面的例子就是一个范围查询:
```mysql { class= ' line-numbers'}
mysql> EXPLAIN SELECT *
    ->         FROM user_info
    ->         WHERE id BETWEEN 2 AND 8 \G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: user_info
   partitions: NULL
         type: range
possible_keys: PRIMARY
          key: PRIMARY
      key_len: 8
          ref: NULL
         rows: 7
     filtered: 100.00
        Extra: Using where
1 row in set, 1 warning (0.00 sec)

```
- index: 表示全索引扫描(full index scan), 和 ALL 类型类似, 只不过 ALL 类型是全表扫描, 而 index 类型则仅仅扫描所有的索引, 而不扫描数据.
index 类型通常出现在: 所要查询的数据直接在索引树中就可以获取到, 而不需要扫描数据. 当是这种情况时, Extra 字段 会显示 Using index.

例如:
```mysql { class= ' line-numbers'}
mysql> EXPLAIN SELECT name FROM  user_info \G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: user_info
   partitions: NULL
         type: index
possible_keys: NULL
          key: name_index
      key_len: 152
          ref: NULL
         rows: 10
     filtered: 100.00
        Extra: Using index
1 row in set, 1 warning (0.00 sec)
```
上面的例子中, 我们查询的 name 字段恰好是一个索引, 因此我们直接从索引中获取数据就可以满足查询的需求了, 而不需要查询表中的数据. 因此这样的情况下, type 的值是 index, 并且 Extra 的值是 Using index.

- ALL: 表示全表扫描, 这个类型的查询是性能最差的查询之一. 通常来说, 我们的查询不应该出现 ALL 类型的查询, 因为这样的查询在数据量大的情况下, 对数据库的性能是巨大的灾难. 如一个查询是 ALL 类型查询, 那么一般来说可以对相应的字段添加索引来避免.
下面是一个全表扫描的例子, 可以看到, 在全表扫描时, possible_keys 和 key 字段都是 NULL, 表示没有使用到索引, 并且 rows 十分巨大, 因此整个查询效率是十分低下的.
```mysql { class= ' line-numbers'}
mysql> EXPLAIN SELECT age FROM  user_info WHERE age = 20 
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: user_info
   partitions: NULL
         type: ALL
possible_keys: NULL
          key: NULL
      key_len: NULL
          ref: NULL
         rows: 10
     filtered: 10.00
        Extra: Using where
1 row in set, 1 warning (0.00 sec)
```
#### type 类型的性能比较

通常来说, 不同的 type 类型的性能关系如下:
`ALL < index < range ~ index_merge < ref < eq_ref < const < system`
`ALL` 类型因为是全表扫描, 因此在相同的查询条件下, 它是速度最慢的.
而 `index` 类型的查询虽然不是全表扫描, 但是它扫描了所有的索引, 因此比 ALL 类型的稍快.
后面的几种类型都是利用了索引来查询数据, 因此可以过滤部分或大部分数据, 因此查询效率就比较高了.

### possible_keys

`possible_keys` 表示 MySQL 在查询时, 能够使用到的索引. 注意, 即使有些索引在 `possible_keys` 中出现, 但是并不表示此索引会真正地被 MySQL 使用到. MySQL 在查询时具体使用了哪些索引, 由 `key` 字段决定.

### key

key字段是 MySQL 在当前查询时所真正使用到的索引.如果为NULL，则没有使用索引。查询中若使用了覆盖索引，则该索引仅出现在key列表中。

### key_len

表示索引中使用的字节数，可通过该列计算查询中使用的索引长度。评估组合索引是否完全被使用, 或只有最左部分字段被使用到。在不损失精确性的情况下，长度越短越好。key_len显示的值为索引字段的最大可能长度，并非实际使用长度，即key_len是根据表定义计算而得，不是通过表内检索出的。

key_len 的计算规则如下:
- 字符串
    - char(n): n 字节长度
    - varchar(n): 如果是 utf8 编码, 则是 3 n + 2字节; 如果是 utf8mb4 编码, 则是 4 n + 2 字节.

- 数值类型:
    - TINYINT: 1字节
    - SMALLINT: 2字节
    - MEDIUMINT: 3字节
    - INT: 4字节
    - BIGINT: 8字节

- 时间类型
    - DATE: 3字节
    - TIMESTAMP: 4字节
    - DATETIME: 8字节

- 字段属性: NULL 属性 占用一个字节. 如果一个字段是 NOT NULL 的, 则没有此属性.
我们来举两个简单的栗子
```mysql { class= ' line-numbers'}
mysql> EXPLAIN SELECT * FROM order_info WHERE user_id < 3 AND product_name = 'p1' AND productor = 'WHH' \G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: order_info
   partitions: NULL
         type: range
possible_keys: user_product_detail_index
          key: user_product_detail_index
      key_len: 9
          ref: NULL
         rows: 5
     filtered: 11.11
        Extra: Using where; Using index
1 row in set, 1 warning (0.00 sec)

```
上面的例子是从表 order_info 中查询指定的内容, 而我们从此表的建表语句中可以知道, 表 order_info 有一个联合索引:
```mysql { class= ' line-numbers'}
KEY `user_product_detail_index` (`user_id`, `product_name`, `productor`)
```
不过此查询语句 `WHERE user_id < 3 AND product_name = 'p1' AND productor = 'WHH'` 中, 因为先进行 user_id 的范围查询, 而根据 `最左前缀`匹配 原则, 当遇到范围查询时, 就停止索引的匹配, 因此实际上我们使用到的索引的字段只有 `user_id`, 因此在 `EXPLAIN` 中, 显示的 key_len 为 9. 因为 user_id 字段是 BIGINT, 占用 8 字节, 而 NULL 属性占用一个字节, 因此总共是 9 个字节. 若我们将user_id 字段改为 `BIGINT(20) NOT NULL DEFAULT '0'`, 则 key_length 应该是8.

上面因为 `最左前缀`匹配 原则, 我们的查询仅仅使用到了联合索引的 `user_id` 字段, 因此效率不算高.

接下来我们来看一下下一个例子:
```mysql { class= ' line-numbers'}
mysql> EXPLAIN SELECT * FROM order_info WHERE user_id = 1 AND product_name = 'p1' \G;
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: order_info
   partitions: NULL
         type: ref
possible_keys: user_product_detail_index
          key: user_product_detail_index
      key_len: 161
          ref: const,const
         rows: 2
     filtered: 100.00
        Extra: Using index
1 row in set, 1 warning (0.00 sec)
```
这次的查询中, 我们没有使用到范围查询, key_len 的值为 161. 为什么呢? 因为我们的查询条件 `WHERE user_id = 1 AND product_name = 'p1'` 中, 仅仅使用到了联合索引中的前两个字段, 因此 `keyLen(user_id) + keyLen(product_name) = 9 + 50 * 3 + 2 = 161`

### ref

显示索引的哪一列被使用了，如果可能的话，是一个常数。哪些列表或常量被用于查找索引列上的值。
### rows

rows 也是一个重要的字段. MySQL 查询优化器根据统计信息及索引选用情况, 估算 SQL 要查找到结果记录集需要扫描读取的数据行数.
这个值非常直观显示 SQL 的效率好坏, 原则上 rows 越少越好.

### Extra
EXplain 包含不适合再其他列中显示但十分重要的额外信息会在 Extra 字段显示, 常见的有以下几种内容:



id|type|remark|
| :-:  | :-:  | :-   |
| ---- | ---- | ---- |
|      |      |      |
1|Using filesort|说明MySQL会对数据使用一个外部的索引排序，而不是按照表内的索引顺序进行读取。MySQL中无法利用索引完成的排序操作称为“文件排序”
2|Using Temporary|使用了临时表保存中间结果，MySQL在对查询结果排序时使用临时表。常见于排序 order by 和分组查询 group by
3|USING index|表示相应的select操作中使用了覆盖索引(Covering Index),避免访问了表的数据行，效率不错。如果同时出现using where，表明索引被用用来执行索引键值的查找；如果没有同时出现using where，表明索引用来读取数据而非执行查找动作。
4|Using where|表使用了where过滤
5|using join buffer|使用了连接缓存
6|impossible were|where子句的值总是false，不能用来获取任何元祖
7|select tables optimized away|在没有GROUPBY子句的情况下，基于索引优化MIN/MAX操作或者对于MyISAM存储引擎优化COUNT(*)操作，不必等到执行阶段再进行计算，查询执行计划生成的阶段完成优化。
8|distinct|优化distinct操作，在找到第一匹配的元祖后即停止找同样值的动作




- Using filesort
当 Extra 中有 Using filesort 时, 表示 MySQL 需额外的排序操作, 不能通过索引顺序达到排序效果. 一般有 Using filesort, 都建议优化去掉, 因为这样的查询 CPU 资源消耗大.

例如下面的例子:
```mysql { class= ' line-numbers'}
mysql> EXPLAIN SELECT * FROM order_info ORDER BY product_name \G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: order_info
   partitions: NULL
         type: index
possible_keys: NULL
          key: user_product_detail_index
      key_len: 253
          ref: NULL
         rows: 9
     filtered: 100.00
        Extra: Using index; Using filesort
1 row in set, 1 warning (0.00 sec)

```
我们的索引是
```mysql
KEY `user_product_detail_index` (`user_id`, `product_name`, `productor`)
```
但是上面的查询中根据 `product_name` 来排序, 因此不能使用索引进行优化, 进而会产生 `Using filesort`.
如果我们将排序依据改为 `ORDER BY user_id, product_name`, 那么就不会出现 `Using filesort` 了. 例如:
```mysql { class= ' line-numbers'}
mysql> EXPLAIN SELECT * FROM order_info ORDER BY user_id, product_name \G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: order_info
   partitions: NULL
         type: index
possible_keys: NULL
          key: user_product_detail_index
      key_len: 253
          ref: NULL
         rows: 9
     filtered: 100.00
        Extra: Using index
1 row in set, 1 warning (0.00 sec)
```

- Using index
"覆盖索引扫描", 表示查询在索引树中就可查找所需数据, 不用扫描表数据文件, 往往说明性能不错
- Using temporary
查询有使用临时表, 一般出现于排序, 分组和多表 join 的情况, 查询效率不高, 建议优化.

## 参考资料及推荐阅读

- [MySQL官网手册](https://dev.mysql.com/doc/refman/5.6/en/)
-《高性能MySQL》
- 《高可用MySQL》
- 《深入理解MySQL核心技术》
- MySQL的源码

## 课后练习

设计一个直播系统（例如斗鱼直播）的数据库

# Mysql 高级

## 视图

### 1. 问题

对于复杂的查询，往往是有多个数据表进行关联查询而得到，如果数据库因为需求等原因发生了改变，为了保证查询出来的数据与之前相同，则需要在多个地方进行修改，维护起来非常麻烦

解决办法：定义视图

### 2. 视图是什么

通俗的讲，视图就是一条SELECT语句执行后返回的结果集。所以我们在创建视图的时候，主要的工作就落在创建这条SQL查询语句上。

视图是对若干张基本表的引用，一张虚表，查询语句执行的结果，不存储具体的数据（基本表数据发生了改变，视图也会跟着改变）；

方便操作，特别是查询操作，减少复杂的SQL语句，增强可读性；

### 3. 定义视图

建议以v_开头

```sql
create view 视图名称 as select语句;
```

### 4. 查看视图

查看表会将所有的视图也列出来

```sql
show tables;
```

### 5. 使用视图

视图的用途就是查询

```sql
select * from v_stu_score;
```

### 6. 删除视图

```sql
drop view 视图名称;
例：
drop view v_stu_sco;
```

### 7. 视图demo

![image-20201115193713232](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202925.png)

![image-20201115193723830](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202917.png)

![image-20201115193741248](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202909.png)

![image-20201115193814278](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115193814.png)

### 8. 视图的作用

1. 提高了重用性，就像一个函数
2. 对数据库重构，却不影响程序的运行
3. 提高了安全性能，可以对不同的用户
4. 让数据更加清晰

## 事务

### 1. 为什么要有事务

事务广泛的运用于订单系统、银行系统等多种场景

例如：

> A用户和B用户是银行的储户，现在A要给B转账500元，那么需要做以下几件事：
>
> 1. 检查A的账户余额>500元；
> 2. A 账户中扣除500元;
> 3. B 账户中增加500元;

正常的流程走下来，A账户扣了500，B账户加了500，皆大欢喜。

那如果A账户扣了钱之后，系统出故障了呢？A白白损失了500，而B也没有收到本该属于他的500。

以上的案例中，隐藏着一个前提条件：A扣钱和B加钱，要么同时成功，要么同时失败。事务的需求就在于此

所谓事务,它是一个操作序列，这些操作要么都执行，要么都不执行，它是一个不可分割的工作单位。

例如，银行转帐工作：从一个帐号扣款并使另一个帐号增款，这两个操作要么都执行，要么都不执行。所以，应该把他们看成一个事务。事务是数据库维护数据一致性的单位，在每个事务结束时，都能保持数据一致性

### 事务四大特性(简称ACID)

- 原子性(Atomicity)
- 一致性(Consistency)
- 隔离性(Isolation)
- 持久性(Durability)

以下内容出自《高性能MySQL》第三版，了解事务的ACID及四种隔离级有助于我们更好的理解事务运作。

下面举一个银行应用是解释事务必要性的一个经典例子。假如一个银行的数据库有两张表：支票表（checking）和储蓄表（savings）。现在要从用户Jane的支票账户转移200美元到她的储蓄账户，那么至少需要三个步骤：

1. 检查支票账户的余额高于或者等于200美元。
2. 从支票账户余额中减去200美元。
3. 在储蓄帐户余额中增加200美元。

上述三个步骤的操作必须打包在一个事务中，任何一个步骤失败，则必须回滚所有的步骤。

可以用START TRANSACTION语句开始一个事务，然后要么使用COMMIT提交将修改的数据持久保存，要么使用ROLLBACK撤销所有的修改。事务SQL的样本如下：

1. start transaction;
2. select balance from checking where customer_id = 10233276;
3. update checking set balance = balance - 200.00 where customer_id = 10233276;
4. update savings set balance = balance + 200.00 where customer_id = 10233276;
5. commit;

一个很好的事务处理系统，必须具备这些标准特性：

- 原子性（atomicity）

> 一个事务必须被视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交成功，要么全部失败回滚，对于一个事务来说，不可能只执行其中的一部分操作，这就是事务的原子性

- 一致性（consistency）

> 数据库总是从一个一致性的状态转换到另一个一致性的状态。（在前面的例子中，一致性确保了，即使在执行第三、四条语句之间时系统崩溃，支票账户中也不会损失200美元，因为事务最终没有提交，所以事务中所做的修改也不会保存到数据库中。）

- 隔离性（isolation）

> 通常来说，一个事务所做的修改在最终提交以前，对其他事务是不可见的。（在前面的例子中，当执行完第三条语句、第四条语句还未开始时，此时有另外的一个账户汇总程序开始运行，则其看到支票帐户的余额并没有被减去200美元。）

- 持久性（durability）

> 一旦事务提交，则其所做的修改会永久保存到数据库。（此时即使系统崩溃，修改的数据也不会丢失。）

### 事务命令

表的引擎类型必须是innodb类型才可以使用事务，这是mysql表的默认引擎

#### 查看表的创建语句，可以看到engine=innodb

```sql
-- 选择数据库
use jing_dong;
-- 查看goods表
show create table goods;
```

#### 开启事务，命令如下：

- 开启事务后执行修改命令，变更会维护到本地缓存中，而不维护到物理表中

```sql
begin;
或者
start transaction;
```

#### 提交事务，命令如下

- 将缓存中的数据变更维护到物理表中

```sql
commit;
```

#### 回滚事务，命令如下：

- 放弃缓存中变更的数据

```sql
rollback;
```

#### 注意

1. 修改数据的命令会自动的触发事务，包括insert、update、delete
2. 而在SQL语句中有手动开启事务的原因是：可以进行多次数据的修改，如果成功一起成功，否则一起会滚到之前的数据

# 提交

- 为了演示效果，需要打开两个终端窗口，使用同一个数据库，操作同一张表（用到之前的jing_dong数据，可以回到mysql第3天中查看）

#### step1：连接

- 终端1：查询商品分类信息

```sql
select * from goods_cates;
```

#### step2：增加数据

- 终端2：开启事务，插入数据

```sql
begin;
insert into goods_cates(name) values('小霸王游戏机');
```

- 终端2：查询数据，此时有新增的数据

```sql
select * from goods_cates;
```

#### step3：查询

- 终端1：查询数据，发现并没有新增的数据

```sql
select * from goods_cates;
```

#### step4：提交

- 终端2：完成提交

```sql
commit;
```

#### step5：查询

- 终端1：查询，发现有新增的数据

```sql
select * from goods_cates;
```

## 回滚

- 为了演示效果，需要打开两个终端窗口，使用同一个数据库，操作同一张表

#### step1：连接

- 终端1

```sql
select * from goods_cates;
```

#### step2：增加数据

- 终端2：开启事务，插入数据

```sql
begin;
insert into goods_cates(name) values('小霸王游戏机');
```

- 终端2：查询数据，此时有新增的数据

```sql
select * from goods_cates;
```

#### step3：查询

- 终端1：查询数据，发现并没有新增的数据

```sql
select * from goods_cates;
```

#### step4：回滚

- 终端2：完成回滚

```sql
rollback;
```

#### step5：查询

- 终端1：查询数据，发现没有新增的数据

```sql
select * from goods_cates;
```

## 索引

### 1. 思考

> 在图书馆中是如何找到一本书的？

一般的应用系统对比数据库的读写比例在10:1左右(即有10次查询操作时有1次写的操作)，

而且插入操作和更新操作很少出现性能问题，

遇到最多、最容易出问题还是一些复杂的查询操作，所以查询语句的优化显然是重中之重

### 2. 解决办法

当数据库中数据量很大时，查找数据会变得很慢

优化方案：索引

### 3. 索引是什么

索引是一种特殊的文件(InnoDB数据表上的索引是表空间的一个组成部分)，它们包含着对数据表里所有记录的引用指针。

更通俗的说，数据库索引好比是一本书前面的目录，能加快数据库的查询速度

### 4. 索引目的

索引的目的在于提高查询效率，可以类比字典，如果要查“mysql”这个单词，我们肯定需要定位到m字母，然后从下往下找到y字母，再找到剩下的sql。如果没有索引，那么你可能需要把所有单词看一遍才能找到你想要的，如果我想找到m开头的单词呢？或者ze开头的单词呢？是不是觉得如果没有索引，这个事情根本无法完成？

### 5. 索引原理

除了词典，生活中随处可见索引的例子，如火车站的车次表、图书的目录等。它们的原理都是一样的，通过不断的缩小想要获得数据的范围来筛选出最终想要的结果，同时把随机的事件变成顺序的事件，也就是我们总是通过同一种查找方式来锁定数据。

数据库也是一样，但显然要复杂许多，因为不仅面临着等值查询，还有范围查询(>、<、between、in)、模糊查询(like)、并集查询(or)等等。数据库应该选择怎么样的方式来应对所有的问题呢？我们回想字典的例子，能不能把数据分成段，然后分段查询呢？最简单的如果1000条数据，1到100分成第一段，101到200分成第二段，201到300分成第三段……这样查第250条数据，只要找第三段就可以了，一下子去除了90%的无效数据。

![image-20201115193936707](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115193936.png)

### 6. 索引的使用

- 查看索引

```sql
show index from 表名;
```

- 创建索引
  - 如果指定字段是字符串，需要指定长度，建议长度与定义字段时的长度一致
  - 字段类型如果不是字符串，可以不填写长度部分

```sql
create index 索引名称 on 表名(字段名称(长度))
```

- 删除索引：

```sql
drop index 索引名称 on 表名;
```

### 7. 索引demo

#### 7.1. 创建测试表testindex

```sql
create table test_index(title varchar(10));
```

#### 7.2 使用python程序（ipython也可以）通过pymsql模块 向表中加入十万条数据

```python
from pymysql import connect

def main():
    # 创建Connection连接
    conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='mysql',charset='utf8')
    # 获得Cursor对象
    cursor = conn.cursor()
    # 插入10万次数据
    for i in range(100000):
        cursor.execute("insert into test_index values('ha-%d')" % i)
    # 提交数据
    conn.commit()

if __name__ == "__main__":
    main()
```

#### 7.3. 查询

- 开启运行时间监测：

```sql
set profiling=1;
```

- 查找第1万条数据ha-99999

```sql
select * from test_index where title='ha-99999';
```

- 查看执行的时间：

```sql
show profiles;
```

- 为表title_index的title列创建索引：

```sql
create index title_index on test_index(title(10));
```

- 执行查询语句：

```sql
select * from test_index where title='ha-99999';
```

- 再次查看执行的时间

```sql
show profiles;
```

### 8. 注意：

> 要注意的是，建立太多的索引将会影响更新和插入的速度，因为它需要同样更新每个索引文件。对于一个经常需要更新和插入的表格，就没有必要为一个很少使用的where字句单独建立索引了，对于比较小的表，排序的开销不会很大，也没有必要建立另外的索引。
>
> 建立索引会占用磁盘空间

## 账户管理

- 在生产环境下操作数据库时，绝对不可以使用root账户连接，而是创建特定的账户，授予这个账户特定的操作权限，然后连接进行操作，主要的操作就是数据的crud
- MySQL账户体系：根据账户所具有的权限的不同，MySQL的账户可以分为以下几种
  - 服务实例级账号：，启动了一个mysqld，即为一个数据库实例；如果某用户如root,拥有服务实例级分配的权限，那么该账号就可以删除所有的数据库、连同这些库中的表
  - 数据库级别账号：对特定数据库执行增删改查的所有操作
  - 数据表级别账号：对特定表执行增删改查等所有操作
  - 字段级别的权限：对某些表的特定字段进行操作
  - 存储程序级别的账号：对存储程序进行增删改查的操作
- 账户的操作主要包括创建账户、删除账户、修改密码、授权权限等

注意：

1. 进行账户操作时，需要使用root账户登录，这个账户拥有最高的实例级权限
2. 通常都使用数据库级操作权限

## 授予权限

需要使用实例级账户登录后操作，以root为例

主要操作包括：

- 查看所有用户
- 修改密码
- 删除用户

### 1. 查看所有用户

- 所有用户及权限信息存储在mysql数据库的user表中
- 查看user表的结构

```sql
desc user;
```

- 主要字段说明：
  - Host表示允许访问的主机
  - User表示用户名
  - authentication_string表示密码，为加密后的值

查看所有用户

```sql
select host,user,authentication_string from user;
```

结果

```sql
mysql> select host,user,authentication_string from user;
+-----------+------------------+-------------------------------------------+
| host      | user             | authentication_string                     |
+-----------+------------------+-------------------------------------------+
| localhost | root             | *E74858DB86EBA20BC33D0AECAE8A8108C56B17FA |
| localhost | mysql.sys        | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| localhost | debian-sys-maint | *EFED9C764966EDB33BB7318E1CBD122C0DFE4827 |
+-----------+------------------+-------------------------------------------+
3 rows in set (0.00 sec)
```

### 2. 创建账户、授权

- 需要使用实例级账户登录后操作，以root为例
- 常用权限主要包括：create、alter、drop、insert、update、delete、select
- 如果分配所有权限，可以使用all privileges

#### 2.1 创建账户&授权

```sql
grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';
```

#### 2.2 示例1

创建一个`laowang`的账号，密码为`123456`，只能通过本地访问, 并且只能对`jing_dong`数据库中的所有表进行`读`操作

##### step1：使用root登录

```sql
mysql -uroot -p
回车后写密码，然后回车
```

##### step2：创建账户并授予所有权限

```sql
grant select on jing_dong.* to 'laowang'@'localhost' identified by '123456';
```

说明

- 可以操作python数据库的所有表，方式为:`jing_dong.*`
- 访问主机通常使用 百分号% 表示此账户可以使用任何ip的主机登录访问此数据库
- 访问主机可以设置成 localhost或具体的ip，表示只允许本机或特定主机访问

- 查看用户有哪些权限

```sql
show grants for laowang@localhost;
```

##### step3：退出root的登录

```sql
quit
```

##### step4：使用laowang账户登录

```sql
mysql -ulaowang -p
回车后写密码，然后回车
```

- 登录后效果如下图

![image-20201115194037940](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202842.png)

![image-20201115194048569](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202723.png)

#### 2.3 示例2

创建一个`laoli`的账号，密码为`12345678`，可以任意电脑进行链接访问, 并且对`jing_dong`数据库中的所有表拥有所有权限

```sql
grant all privileges on jing_dong.* to "laoli"@"%" identified by "12345678"
```

![image-20201115194112245](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202712.png)

![image-20201115194125108](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202704.png)

![image-20201115194144081](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202654.png)

## 账户操作

### 1. 修改权限

```sql
grant 权限名称 on 数据库 to 账户@主机 with grant option;
```

![image-20201115194204983](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202642.png)

![image-20201115194214430](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115194214.png)

![image-20201115194233815](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115194234.png)

### 2. 修改密码

使用root登录，修改mysql数据库的user表

- 使用password()函数进行密码加密

  ```sql
  update user set authentication_string=password('新密码') where user='用户名';
  例：
  update user set authentication_string=password('123') where user='laowang';
  ```

- 注意修改完成后需要刷新权限

  ```sql
  刷新权限：flush privileges
  ```

### 3. 远程登录（危险慎用）

如果向在一个Ubuntu中使用msyql命令远程连接另外一台mysql服务器的话，通过以下方式即可完成，但是此方法仅仅了解就好了，不要在实际生产环境中使用

修改 /etc/mysql/mysql.conf.d/mysqld.cnf 文件

```bash
vim /etc/mysql/mysql.conf.d/mysqld.cnf
```

![image-20201115194305532](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115194305.png)

然后重启msyql

```sql
service mysql restart
```

在另外一台Ubuntu中进行连接测试

![image-20201115194332050](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115194332.png)

如果依然连不上，可能原因：

1) 网络不通

> 通过 ping xxx.xxx.xx.xxx可以发现网络是否正常

2)查看数据库是否配置了bind_address参数

> 本地登录数据库查看my.cnf文件和数据库当前参数show variables like 'bind_address';
>
> 如果设置了bind_address=127.0.0.1 那么只能本地登录

3)查看数据库是否设置了skip_networking参数

> 如果设置了该参数，那么只能本地登录mysql数据库

4)端口指定是否正确

### 4. 删除账户

- 语法1：使用root登录

```sql
drop user '用户名'@'主机';
例：
drop user 'laowang'@'%';
```

- 语法2：使用root登录，删除mysql数据库的user表中数据

```sql
delete from user where user='用户名';
例：
delete from user where user='laowang';

-- 操作结束之后需要刷新权限
flush privileges
```

- 推荐使用语法1删除用户, 如果使用语法1删除失败，采用语法2方式

### 3. 忘记 root 账户密码怎么办 !!

- 一般也轮不到我们来管理 root 账户,所以别瞎卖白粉的心了
- 万一呢? 到时候再来查http://blog.csdn.net/lxpbs8851/article/details/10895085

## MySQL主从同步配置

### 1. 主从同步的定义

主从同步使得数据可以从一个数据库服务器复制到其他服务器上，在复制数据时，一个服务器充当主服务器（master），其余的服务器充当从服务器（slave）。因为复制是异步进行的，所以从服务器不需要一直连接着主服务器，从服务器甚至可以通过拨号断断续续地连接主服务器。通过配置文件，可以指定复制所有的数据库，某个数据库，甚至是某个数据库上的某个表。

使用主从同步的好处：

- 通过增加从服务器来提高数据库的性能，在主服务器上执行写入和更新，在从服务器上向外提供读功能，可以动态地调整从服务器的数量，从而调整整个数据库的性能。
- 提高数据安全，因为数据已复制到从服务器，从服务器可以终止复制进程，所以，可以在从服务器上备份而不破坏主服务器相应数据
- 在主服务器上生成实时数据，而在从服务器上分析这些数据，从而提高主服务器的性能

### 2. 主从同步的机制

![image-20201115194414584](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115194414.png)



Mysql服务器之间的主从同步是基于二进制日志机制，主服务器使用二进制日志来记录数据库的变动情况，从服务器通过读取和执行该日志文件来保持和主服务器的数据一致。

在使用二进制日志时，主服务器的所有操作都会被记录下来，然后从服务器会接收到该日志的一个副本。从服务器可以指定执行该日志中的哪一类事件（譬如只插入数据或者只更新数据），默认会执行日志中的所有语句。

每一个从服务器会记录关于二进制日志的信息：文件名和已经处理过的语句，这样意味着不同的从服务器可以分别执行同一个二进制日志的不同部分，并且从服务器可以随时连接或者中断和服务器的连接。

主服务器和每一个从服务器都必须配置一个唯一的ID号（在my.cnf文件的[mysqld]模块下有一个server-id配置项），另外，每一个从服务器还需要通过CHANGE MASTER TO语句来配置它要连接的主服务器的ip地址，日志文件名称和该日志里面的位置（这些信息存储在主服务器的数据库里）

### 3. 配置主从同步的基本步骤

有很多种配置主从同步的方法，可以总结为如下的步骤：

1. 在主服务器上，必须开启二进制日志机制和配置一个独立的ID
2. 在每一个从服务器上，配置一个唯一的ID，创建一个用来专门复制主服务器数据的账号
3. 在开始复制进程前，在主服务器上记录二进制文件的位置信息
4. 如果在开始复制之前，数据库中已经有数据，就必须先创建一个数据快照（可以使用mysqldump导出数据库，或者直接复制数据文件）
5. 配置从服务器要连接的主服务器的IP地址和登陆授权，二进制日志文件名和位置

### 4. 详细配置主从同步的方法

主和从的身份可以自己指定，我们将虚拟机Ubuntu中MySQL作为主服务器，将Windows中的MySQL作为从服务器。 在主从设置前，要保证Ubuntu与Windows间的网络连通。

#### 4.1 备份主服务器原有数据到从服务器

如果在设置主从同步前，主服务器上已有大量数据，可以使用mysqldump进行数据备份并还原到从服务器以实现数据的复制。

#### 4.1.1 在主服务器Ubuntu上进行备份，执行命令：

```bash
mysqldump -uroot -pmysql --all-databases --lock-all-tables > ~/master_db.sql
```

![image-20201115194455134](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202616.png)

说明

- -u ：用户名
- -p ：示密码
- --all-databases ：导出所有数据库
- --lock-all-tables ：执行操作时锁住所有表，防止操作时有数据修改
- ~/master_db.sql :导出的备份数据（sql文件）位置，可自己指定

#### 4.1.2 在从服务器Windows上进行数据还原

找到Windows上mysql命令的位置

![image-20201115194515357](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202542.png)

新打开的命令窗口，在这个窗口中可以执行类似在Ubuntu终端中执行的mysql命令

将从主服务器Ubuntu中导出的文件复制到从服务器Windows中，可以将其放在上面mysql命令所在的文件夹中，方便还原使用

![image-20201115194733549](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115194733.png)

在刚打开的命令黑窗口中执行还原操作:

```cmd
mysql –uroot –pmysql < master_db.sql
```

![image-20201115194806948](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115194807.png)

#### 4.2 配置主服务器master（Ubuntu中的MySQL）

#### 4.2.1 编辑设置mysqld的配置文件，设置log_bin和server-id

```bash
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```

![image-20201115194852650](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115194852.png)

#### 4.2.2 重启mysql服务

```bash
sudo service mysql restart
```

![image-20201115194913776](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115194915.png)

#### 4.2.3 登入主服务器Ubuntu中的mysql，创建用于从服务器同步数据使用的帐号

```sql
mysql –uroot –pmysql
GRANT REPLICATION SLAVE ON *.* TO 'slave'@'%' identified by 'slave';
FLUSH PRIVILEGES;
```

![image-20201115194945096](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115194945.png)

#### 4.2.4 获取主服务器的二进制日志信息

```sql
SHOW MASTER STATUS;
```

![image-20201115195025475](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115195025.png)

File为使用的日志文件名字，Position为使用的文件位置，这两个参数须记下，配置从服务器时会用到

#### 4.3 配置从服务器slave（Windows中的MySQL）

#### 4.3.1 找到Windows中MySQL的配置文件

![image-20201115195042821](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202520.png)

#### 4.3.2 编辑my.ini文件，将server-id修改为2，并保存退出。

![image-20201115195101033](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115195101.png)

#### 4.3.3 打开windows服务管理

可以在开始菜单中输入services.msc找到并运行

![image-20201115195134115](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115195134.png)



#### 4.3.4 在打开的服务管理中找到MySQL57，并重启该服务

![image-20201115195152821](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115195153.png)

### 5. 进入windows的mysql，设置连接到master主服务器

```
change master to master_host='10.211.55.5', master_user='slave', master_password='slave',master_log_file='mysql-bin.000006', master_log_pos=590;
```

注：

- master_host：主服务器Ubuntu的ip地址
- master_log_file: 前面查询到的主服务器日志文件名
- master_log_pos: 前面查询到的主服务器日志文件位置

![image-20201115195212862](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202353.png)

### 6. 开启同步，查看同步状态

![image-20201115195228786](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202325.png)

### 7. 测试主从同步

在Ubuntu的MySQL中（主服务器）创建一个数据库

![image-20201115195243282](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115202331.png)

在Windows的MySQL中（从服务器）查看新建的数据库是否存在

![image-20201115195256229](https://raw.githubusercontent.com/ld269440877/images/master/3CRTR/20201115195256.png)





# 刷题

## LeetCode

[175. 组合两个表 - 力扣（LeetCode）](https://leetcode-cn.com/problems/combine-two-tables/)

> 表1: Person
+-------------+---------+
| 列名         | 类型     |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId 是上表主键
表2: Address
+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId 是上表主键
编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，都需要基于上述两表提供 person 的以下信息：
FirstName, LastName, City, State

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combine-two-tables
考点解析：
join两张表：
person表中有FirstName和 LastName；Address表中有City和State；
两张表的共同字段（关联字段）：PersonId
```mysql { class= ' line-numbers'}
select a.FirstName,a.LastName,b.City,b.State
from person a
left join address b
on a.PersonId = b.PersonId
```

## w3school

[w3school SQL 测验](https://www.w3school.com.cn/quiz/quiz.asp?quiz=sql)

## 面试题

### 面试题1
第一题
- 新建一个order_new表，包含三个字段：
    - order_id（订单编号）
    - spend（每一个订单的实付金额）
    - discount_flag（当订单的折扣金额大于0时为1，折扣金额等于0时为0）
考点
```mysql { class= ' line-numbers'}
创建新表：
创建计算字段：加减乘除
SQL基础语句：select * from 表 where 条件 group by ....having......order by ....
limit...
CASE WHEN用法：CASE WHEN THEN ELSE END


CREATE TABLE order_new
SELECT order_id, original_value - discount AS spend,
CASE WHEN discount >0 THEN 1
WHEN discount =0 THEN 0
ELSE '其他'
END AS 'discount_flag'
FROM order_2017
```
第二题
找到2017年11月11日当天订单实付金额最大的订单编号
考点
```mysql { class= ' line-numbers'}
创建计算字段：加减乘除
where 条件
函数：MAX最大值


SELECT order_id, max(original_value - discount)
FROM order_2017
WHERE date IN ('2017/11/11')
```
第三题
计算每个月每个顾客等级平均每单购买商品的数量
月份 顾客等级 订单ID 商品数量items
考点
```mysql { class= ' line-numbers'}
join两张表：
创建中间表：
创建计算字段：加减乘除
时间函数：DATE_FORMAT(date,format)


SELECT t1.new_month,t1.cust_level,sum(t1.items)/count(t1.order_id) AS avg_items
FROM
(
SELECT DATE_FORMAT(a.date,'%Y/%m') AS new_month,b.cust_level,a.order_id,a.items
FROM order_2017 a
LEFT JOIN cust_info b ON a.cust_id = b.cust_id
)t1
GROUP BY t1.new_month,t1.cust_level
```

### 面试真题2
示例表
创建表
```mysql { class= ' line-numbers'}

#创建一个空表product
CREATE TABLE product
(
`product`varchar(30) NOT NULL DEFAULT '' '产品',
`category` varchar(30) NOT NULL DEFAULT '' COMMENT '种类',
`color` varchar(30) NOT NULL DEFAULT '' COMMENT '颜色',
`weight` float(10,2) DEFAULT '0.00' COMMENT '重量',
`price` int(20) NOT NULL DEFAULT '0' COMMENT '价格',
PRIMARY KEY (`product`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='产品表'
;
#在表product插入值
INSERT INTO product
(product,category,color,weight,price)
VALUES
('productA','categoryA','yellow','5.6','100'),
('productB','categoryB','red','3.7','200'),
('productC','categoryC','blue','10.3','300'),
('productD','categoryD','black','7.8','400')
;
#创建一个空表 order_2018
CREATE TABLE order_2018
(
`orderid`varchar(20) NOT NULL DEFAULT '' '订单编号',
`name` varchar(20) NOT NULL DEFAULT '' COMMENT '顾客ID',
`orderdate` date DEFAULT NULL COMMENT '交易日期',
`store` varchar(20) NOT NULL DEFAULT '' COMMENT '店铺',
`product`varchar(30) NOT NULL DEFAULT '' '产品',
`quantity` int(11) NOT NULL DEFAULT '0' COMMENT '商品数量',
`amount` int(20) NOT NULL DEFAULT '0' COMMENT '价格'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='2018年订单表'
;
#在表order_2018插入值
INSERT INTO order_2018
(`orderid`,`name`,`orderdate`,`store`,`product`,`quantity`,`amount`)
VALUES
('1','customerA','2018-01-01','storeA','productA','1','100'),
('1','customerA','2018-01-01','storeA','productB','1','200'),
('1','customerA','2018-01-01','storeA','productC','1','300'),
('2','customerB','2018-01-12','storeB','productB','1','200'),
('2','customerB','2018-01-12','storeB','productD','1','400'),
('3','customerC','2018-01-12','storeC','productB','1','200'),
('3','customerC','2018-01-12','storeC','productC','1','300'),
('3','customerC','2018-01-12','storeC','productD','1','400'),
('4','customerA','2018-01-01','storeD','productD','2','800'),
('5','customerB','2018-01-23','storeB','productA','1','100')
;
#创建一个空表 store
CREATE TABLE store
(
`store` varchar(20) NOT NULL DEFAULT '' COMMENT '店铺',
`city`varchar(20) NOT NULL DEFAULT '' '城市'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='店铺表'
;
#在表store插入值
INSERT INTO store
(`store`,`city`)
VALUES
('storeA','cityA'),
('storeB','cityA'),
('storeC','cityB'),
('storeD','cityC'),
('storeE','cityD'),
('storeF','cityB')
;
```
2.1第一题
请查找符合以下要求的产品，并按照产品价格降序排列：
category为categoryA且颜色为yellow，或者weight大于5
考点解析：
```mysql { class= ' line-numbers'}
select语句
where条件
and和OR的用法、先后顺序
降序:order by .... desc

select product
from product
where (category IN ('categoryA') and color IN ('yellow')) or weight >5
order by price desc
```
2.2第二题
请计算每一位客人的总购买金额（amount），总购买订单数，总购买产品件数（quantity），同一个
客人同一天的订单算作一单，并筛选出总购买金额大于等于800的客人，按金额降序排列。
考点解析：
```mysql { class= ' line-numbers'}
SQL函数：sum、count(distinct)
查询结果过滤：having
降序:order by .... desc


select order_2018.`name`,sum(amount) AS '总购买金额',count(distinct
order_2018.`name`,orderdate) AS '总购买订单数',sum(quantity) AS '总购买产品件数'
from order_2018
GROUP BY order_2018.`name`
HAVING sum(amount)>800
ORDER BY sum(amount) DESC
```
2.3第三题
请给出每个城市（city）的总店铺数，总购买人数和总购买金额（amount），包含无购买记录的城市
考点解析：
```mysql { class= ' line-numbers'}
join两张表：谁是主表
SQL函数：sum、count(distinct)


SELECT t1.city,count(DISTINCT t1.store),count( DISTINCT t1.`name`),sum(amount)
FROM
(SELECT a.store,a.city,b.`name`,b.amount
FROM store a LEFT JOIN order_2018 b on a.store=b.store)t1
GROUP BY t1.city
```
2.4第四题
请查找购买过categoryA产品的客人，并计算每一位客人的平均订单金额（amount），一个订单编号
（orderid）算作一单
考点解析：
```mysql { class= ' line-numbers'}
先查找购买过categoryA产品的客人；
再计算每一位客人的平均订单金额
子查询：in
SQL函数与计算字段：sum()/count(distinct )



SELECT order_2018 .`name`,sum(amount)/count(DISTINCT orderid) AS '平均订单'
FROM order_2018
WHERE order_2018.`name` IN
(SELECT a.`name` FROM order_2018 a LEFT JOIN product b ON
a.product=b.product WHERE b.category IN ('categoryA'))
GROUP BY order_2018 .`name`
```
2.5第五题
5.请查找每个城市（city）购买金额排名第二的客人，列出其购买城市，姓名和购买金额
考点解析：
```mysql { class= ' line-numbers'}
分组top值问题：
分组排序函数：ROW_NUMBER() OVER(PARTITION BY .... ORDER BY ...... DESC)
嵌套查询：
两表join：


SELECT t1.city,t1.`name`,t1.amount_all
FROM
(SELECT a.city,b.`name`,sum(b.amount) AS 'amount_all',ROW_NUMBER()
OVER(PARTITION BY a.city ORDER BY sum(b.amount) DESC) AS 'rank'
FROM store a LEFT JOIN order_2018 b on a.store=b.store
GROUP BY a.city,b.`name`)t1
WHERE t1.rank =2
```
### 面试真题3
3.1第一题
查询2017年上半年（1-6月），上海地区销售额排名前10的商品ID，需要的字段：商品ID
```mysql { class= ' line-numbers'}
SELECT a.pid,sum(a.saleamount)
FROM tbl_order a LEFT JOIN tbl_user b ON a.userid=b.userid
WHERE a.order_date BETWEEN "2017/1/1" AND "2017/6/30" AND b.procince LIKE "%上
海%"
GROUP BY a.pid
order by sum(a.saleamount) desc
LIMIT 10
```
3.2第二题
查询2017年7月的所有订单中，有且仅有轮胎和保养两个品类的订单数
```mysql { class= ' line-numbers'}
SELECT count(t2.orderid)
FROM
(SELECT t1.orderid,sum(t1.flag)
FROM
(SELECT orderid,
CASE WHEN category IN ('轮胎') OR category IN ('保养') THEN 1 ELSE 0 END AS
'flag'
FROM tbl_order
WHERE order_date BETWEEN "2017/7/1" AND "2017/7/31")t1
HAVING sum(t1.flag) = 2)t2
```

### 面试题拓展资料

- SQL数据库面试题以及答案（50例题）：https://blog.csdn.net/hundan_520520/article/details/54881208
- 常见的SQL面试题经典50题：https://zhuanlan.zhihu.com/p/38354000
- SQL面试题练习：https://zhuanlan.zhihu.com/p/37815261
- 2020学霸批拼多多数据分析笔试总结：https://zhuanlan.zhihu.com/p/75704180
- leetcode我们必知必会的SQL面试题：https://juejin.im/post/5c3820436fb9a049f15469d5
- 10道mysql查询语句面试题：https://www.yanxurui.cc/posts/mysql/2016-11-10-10-sql-interview-questions/
- 数据分析面试必备——SQL你准备好了吗？：https://zhuanlan.zhihu.com/p/61805956
- 数据分析之SQL面试题：https://www.jianshu.com/p/77597eadd3cc
SQL面经汇总：https://www.nowcoder.com/discuss/95812

# 串讲MySQL
//TODO 串讲MySQL
[tbl_user](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/tbl_user.xlsx)
[tbl_order](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/tbl_order.xlsx)

## 复习MySQL

[MySQL思维导图](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/MySQL思维导图.xmind)

### SQL知识回顾xmind

[(Back to MySQL思维导图)](#MySQL思维导图)

### SQL书写顺序

SQL完整的数据格式, 不要被吓到, 其实很简单
```mysql { class= ' line-numbers'}
语法结构：
SELECT select_expr [,select_expr,...] [
FROM tb_name
[WHERE 条件判断]
[GROUP BY {col_name|postion} [ASC|DESC], ...]
[HAVING WHERE 条件判断]
[ORDER BY {col_name|expr|postion} [ASC|DESC], ...
[LIMIT {[offset,]rowcount|row_count OFFSET offset}] ]


可以归纳为：
select distinct *
from 表名
where ....
group by ... having ...
order by ...
limit start,count
```

### SQL执行顺序

```mysql { class= ' line-numbers'}
from 表名
where ....
group by ...
having ...
select distinct *
order by ...
limit start,count
实际使用中，只是语句中某些部分的组合，而不是全部
```

## 分组排序函数（Row_number）问题

### 分组排序函数（Row_number）

```mysql { class= ' line-numbers'}
语法结构：

用法1：无分组排序
Row_number() OVER(ORDER BY 字段 DESC)
例如：Row_number() OVER(ORDER BY 学生成绩 DESC)
表示不分班级，所有学生的成绩从高到低排序


用法2：分组排序
ROW_NUMBER() OVER(PARTITION BY 字段1 ORDER BY 字段2 DESC)
表示根据字段1分组，在分组内部根据字段2排序，这个函数计算的值就表示每组内部排序后的顺序编号
例如：ROW_NUMBER() OVER(PARTITION BY 班级 ORDER BY 学生成绩 DESC)
表示根据“班级”分组，在每个“班级”内部根据“学生成绩”排序，这个函数计算的值就表示每组内部排序后的顺序编号
解释：
ROW_NUMBER( ) 起到了编号的功能
partition by 将相同数据进行分区
order by 使得数据按一定顺序排序
```
练习1：计算销售人员的销售额,结果按从高到低排序，查询结果中要包含销售的排名
```mysql { class= ' line-numbers'}
参考答案MySQL8.0 ：
select sales_name,sum(sales),Row_number() OVER(ORDER BY sum(sales) DESC) as
'rank'
from spm_order
group by sales_name


参考答案MySQL5.7 ：
SET @rank= 0;
select A.* , @rank:=@rank + 1 AS rank_no from (
select sales_name,sum(sales)
from spm_order
group by sales_name
order by sum(sales) DESC) A
```

![SQL分组排序函数80-57版本问题](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL分组排序函数80-57版本问题.png 'SQL分组排序函数80-57版本问题')

练习2：计算销售人员在不同城市的销售额；
要求：结果根据销售人员在不同城市的销售额进行分组排序（降序），并且查询结果要包含分组排名
```mysql { class= ' line-numbers'}
参考答案MySQL8.0 ：
select sales_name,city,sum(sales),ROW_NUMBER() OVER(PARTITION BY sales_name
ORDER BY sum(sales) DESC) as 'rank'
from spm_order
group by sales_name,city


参考答案MySQL5.7 ：
SELECT
@r:= case when @type=a.sales_name then @r+1 else 1 end as rowNum,
@type:=a.sales_name as type,
a.*
from
(select sales_name,city,sum(sales)
from spm_order
group by sales_name,city
ORDER BY sales_name , sum(sales) desc)a,(select @r:=0, @type:='' ) b;
```
![SQL分组排序函数80-57版本问题练习2](https://raw.githubusercontent.com/ld269440877/images/master/MySQLNotebook/SQL分组排序函数80-57版本问题练习2.png 'SQL分组排序函数80-57版本问题练习2')

## 面试真题
3.1第一题
查询2017年上半年（1-6月），上海地区销售额排名前10的商品ID，需要的字段：商品ID
```mysql { class= ' line-numbers'}
SELECT tbl_order.pid,sum(tbl_order.salesamout)
FROM tbl_order LEFT JOIN tbl_user ON tbl_order.userid=tbl_user.userid
WHERE tbl_order.orderdate BETWEEN "2017/1/1" AND "2017/6/30" AND
tbl_user.province LIKE "%上海%"
GROUP BY tbl_order.pid
order by sum(tbl_order.salesamout) desc
LIMIT 10
```
3.2第二题
查询2017年7月的所有订单中，有且仅有轮胎和保养两个品类的订单数
```mysql { class= ' line-numbers'}
SELECT count(t2.orderid)
FROM
(SELECT t1.orderid,sum(t1.flag)
FROM
(SELECT orderid,
CASE WHEN category IN ('轮胎') OR category IN ('保养') THEN 1 ELSE 1000000 END
AS 'flag'
FROM tbl_order
WHERE orderdate BETWEEN "2017/1/1" AND "2017/7/31")t1
GROUP BY orderid
HAVING sum(t1.flag) = 2)t2
```
## 京东小案例
-  创建数据库,导入数据表
    创建数据库为jingdong, 导入goods数据表
- SQL语句强化
    - 查询类型cate_name为 '超极本' 的商品名称、价格
` select name,price from goods where cate_name = '超级本'; `
    - 显示商品的种类
`select cate_name from goods group by cate_name;`
    - 求所有电脑产品的平均价格,并且保留两位小数
`select round(avg(price),2) as avg_price from goods;`
    - 显示每种商品的平均价格
`select cate_name,avg(price) from goods group by cate_name`
    - 查询每种类型的商品中 最贵、最便宜、平均价、数量
```mysql
select cate_name,max(price),min(price),avg(price),count(*) from goods
group
```
    - 查询所有价格􀀀于平均价格的商品，并且按价格降序排序
```mysql { class= ' line-numbers'}
select id,name,price from goods
where price > (select round(avg(price),2) as avg_price from goods)
order by price desc;
```
    - 查询每种类型中最贵的电脑信息
```mysql { class= ' line-numbers'}
select * from goods
inner join
(
select
cate_name,
max(price) as max_price,
min(price) as min_price,
avg(price) as avg_price,
count(*) from goods group by cate_name
) as goods_new_info on goods.cate_name=goods_new_info.cate_name and
goods.price=goods_new_info.max
```
## 总结
1. MySQL语句, 多总结, 多查询
2. 多总结解题思路

