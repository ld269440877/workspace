
/**
* @module hive
* @Version :  
* @Author: Dillon
* @Contact: aa269440877@outlook.com
* @WebSite    :   https://github.com/ld269440877/
* @description: 
* @since: 2019-10-27 20:08:23
**/

<font color="red">hive元数据在derby中</font>，只能在hive的安装目录下启动hive
<font color="orange">hive的元数据在mysql中</font>，可以在任意位置启动hive

mysql和hive都实现了SQL标准

hive处理一条sql语句：sql   解析和转换 任务

- 我和李老师的hive可以在任何目录下启动，但是大家的只能在hive的安装目录下启动。
  原因就是：你们的hive元数据是存在derby中，我和李老师的hive元数据是存在mysql中。

mysql和hive都是实现了sql标准

- hive处理一条sql语句
  sql->解析和转换->任务

- 执行引擎：
  hive可以是mapreduce，tez，spark

- hadoop和hive
  hadoop的存储系统hdfs有100g，hive占用hadoop 20g内存
  HDFS的/目录和本地文件系统的/是不一样。

[idea DataGrip 使用图解教程 - Bingo - CSDN博客](https://blog.csdn.net/kl28978113/article/details/80136981)

[数据库管理工具DataGrip使用总结(一) - 掘金](https://juejin.im/post/5c9643faf265da611c5574f5)

伪分布式和完全分布式的区别？
伪分布式：用一个虚拟机，安装并启动hadoop集群。所有的服务都在这一个虚拟机上运行。
完全分布式通常是3个节点以上。hadoop除了运行hive，zookeeper（通常要求节点数为奇数），hbase，spark，kylin

hive的文件存储在hadoop file system上
load把已有数据加载非分区表中
向表中插入数据insert into
分区表：每一分区就对应一个文件夹 将本地文件使用hadoop命令-put传到hive的分区表，手动修复分区表，才可以识别出来


内部表通常都是一些中间表，有中间文件才有中间表。不能直接产生结果就需要中间表过度，我们需要最终的结果
删除中间表，就会删除源数据

hive可以切换计算引擎 mr tez spark、、、计算方式不同单计算结果不会变

# 第3节
# Hive数据定义与操作
# 数据库相关
## 创建数据库
```mysql { class= ' line-numbers'}
CREATE (DATABASE/SCHEMA) [IF NOT EXISTS] database_name
[COMMENT database_comment]
[LOCATION hdfs_path]
[WITH DBPROPERTIES (property_name=property_value,...)];

案例演示：
create database if not exists kaikeba;
拓展1：在Hive中使用Hadoop的dfs命令
hive> dfs -ls /;
拓展2：在Hive中查看本地文件系统
hive> !ls /opt/module;
```
## 查看数据库信息
查看数据库信息 `desc database extended 数据库名;`
## 删除数据库
```mysql { class= ' line-numbers'}
drop database if exists kaikeba;
drop database if exists kaikeba cascade;强制删除数据库
```
## 修改数据库
```mysql { class= ' line-numbers'}
ALTER (DATABASE/SCHEMA) database_name SET LOCATION hdfs_path;
```
# 数据表相关
## 创建数据表
```mysql { class= 'line-numbers'}
create [external] table if not exists 表名
(列名 数据类型 [comment 本列注释],...)
[comment 表注释]
[partitioned by (列名 数据类型 [comment 本列注释],...)]
[clustered by(列名,列名,...)]
[sorted by (列名 [asc|desc],...)] info num_buckets buckets]
[row format row_format]
[stored as file_format]
[location hdfs_path]
[tblproperties (property_name=property_value,...)]
[as select_statement]
说明：
①external表示创建外部表；hive在创建内部表时，会将数据移动到数据仓库指向的路径；若创建外部表，
仅记录数据所在的路径，不对数据的位置做任何改变
②partitioned by表示创建分区表
③clustered by创建分桶表
④sorted by 不常用
⑤row format delimited [fields terminated by char] [collection items terminated
by char] [map keys terminated by char] [line terminated by char]
⑥stored as 指定文件存储类型(sequencefile二进制文件、textfile文本文件、rcfile列式存储格式)
⑦location 指定表在hdfs上的存储位置
⑧like 允许用户复制现有的表结构，但是不复制数据
⑨as 后跟查询语句，根据查询结果创建表
```


```bash{class="line-numbers"}
# 在hadoop用户的家目录下新建一个目录datas：
mkdir datas
# 通过xftp将数据源文件传到datas中

# 启动hadoop（任意位置均可以启动）
start-all.sh
# 访问hadoop file system 的资源管理器地址，图像界面查看hadoop fs下的文件
192.168.5.100:50070
# 本地local host
# hadoop命令在hadoop file system的根目录下创建datas文件夹
hadoop fs -mkdir /datas
# 默认权限和所属组
drwxr-xr-x	hadoop	supergroup	0 B	2019/11/2 下午6:13:27	0	0 B	datas
# 添加写权限
hadoop fs -chmod g+w /datas
# 添加写权限后修改后
drwxrwxr-x	hadoop	supergroup	0 B	2019/11/2 下午6:13:27	0	0 B	datas
```

- 本地文件上传到hadoop

- hadoop命令将本地data下的文件上传到hadoop文件系统
  `hadoop fs -put /home/hadoop/datas/* /datas`

## 创建静态表与动态表的步骤

  | 静态表                                                                                                                                                                                                                                                                                                                                                           | 动态表                                                                                                                                                                                                                                                                                                                                                                                                            |
  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | create database if not exists base_name;  # 创建数据库base_name                                                                                                                                                                                                                                                                                                  | same with the left                                                                                                                                                                                                                                                                                                                                                                                                |
  | use base_name; #选择数据库                                                                                                                                                                                                                                                                                                                                       | same with the left                                                                                                                                                                                                                                                                                                                                                                                                |
  | \# 在数据库base_name下创建table_name表<br>`create table if not exists table_name ( 字段名  数据类型；)`                                                                                                                                                                                                                                                          | `create table if not exists table_name (    # 在数据库base_name下创建table_name表<br/>字段名  数据类型；)`<br>#执行如下命令以设置动态分区：<br/>`set hive.exec.dynamic.partition=true;`<br/>`set hive.exec.dynamic.partition.mode=nonstrict;`<br/>`set hive.exec.max.dynamic.partitions=10000;`<br/>`set hive.exec.max.dynamic.partitions.pernode=10000;`                                                         |
  | <font color='red'>hive命令</font>从本地加载一个file中的数据到已经创建的hive表<br>`hive> load data inpath '/datas/user_info/user_info.txt' overwrite into table table_name;`<br># 加载本地数据源到hive的user_info表<br>要保证创建的表的格式要和数据文件中的格式一样，例如字段间的间隔符是什么行与行间的间隔符都要进行限定 ![user_info](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/user_info.png "user_info") | <font color='orange'>hadoop命令</font>从本地上传所有分区表file<font color="red">s</font>到已经创建的在hadoop fs中表<br>\# 将本地数据源文件上传到HDFS上 <br/>`hdfs dfs -put /home/hadoop/datas/user_trade/* /user/hive/warehouse/kaikeba.db/user_trade`<br># 修复分区表 user_trade：<br/>>`use base_name;` #使用数据库base_name<br/>hive>`msck repair table user_trade;`![user_trade](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/user_trade.png "user_trade") |
  | \# 查看user_info表<br/>hive> `select * from user_info limit 5;`<br/># 查看user_info表结构信息<br/>hive> `desc formatted user_info;`                                                                                                                                                                                                                              | \# 取消严格模式：<br/>`set hive.mapred.mode=nonstrict;`<br># 查询：<br/>`select * from user_trade limit 6;`<br># 设置严格模式：<br/>`set hive.mapred.mode=strict;`<br/>`select * from user_trade where dt='2017-01-12';`                                                                                                                                                                                          |


```mysql { class= ' line-numbers'}
# 创建kaikeba库
create database if not exists kaikeba;

# 使用kaikeba库
use kaikeba;

# 在数据库kaikeba下创建user_info表
hive> create table if not exists user_info (
user_id  string,
user_name  string,
sex  string,
age  int,
city  string,
firstactivetime  string,
level  int,
extra1  string,
extra2  map<string,string>)
row format delimited fields terminated by '\t'
collection items terminated by ','
map keys terminated by ':'
lines terminated by '\n'
stored as textfile;

# 加载本地数据源到hive的user_info表
hive>load data inpath '/datas/user_info/user_info.txt' overwrite into table user_info;

# 查看user_info表
hive> select * from user_info limit 5;
# 查看user_info表结构信息
hive> desc formatted user_info;
"
# Detailed Table Information	
Table Type:  MANAGED_TABLE 也叫内部表
"
hive (kaikeba)> select * from user_info limit 1;
'
user_info.user_id	user_info.user_name	user_info.sex	user_info.age	user_info.city	user_info.firstactivetime	user_info.level	user_info.extra1	user_info.extra2

10001	Abby	female	38	hangzhou	2018-04-13 01:06:07	2	{"systemtype": "android", "education": "doctor", "marriage_status": "1", "phonebrand": "VIVO"}	{"systemtype":"android","education":"doctor","marriage_status":"1","phonebrand":"VIVO"}
'






#动态分区表
# 在数据库开课吧下创建user_trade表
create table if not exists user_trade (
user_name  string,
piece  int,
price  double,
pay_amount  double,
goods_category  string,
pay_time  bigint)  
partitioned by (dt string)
row format delimited fields terminated by '\t';

# 执行如下命令以设置动态分区：
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;
set hive.exec.max.dynamic.partitions=10000;
set hive.exec.max.dynamic.partitions.pernode=10000;

# 将数据源文件上传到HDFS上 hadoop命令
"hdfs dfs -put /home/hadoop/datas/user_trade/* /user/hive/warehouse/kaikeba.db/user_trade"

# 修复分区表 user_trade：
>use kaikeba;# 使用数据库kaikeba
hive>msck repair table user_trade;

# 查询：
select * from user_trade limit 6;
hive (kaikeba)> select * from user_trade limit 1;
"
user_trade.user_name	user_trade.piece	user_trade.price	user_trade.pay_amount	user_trade.goods_category	user_trade.pay_time	user_trade.dt
Allison	4	688.8	2755.2	shoes	1483822729	2017-01-07
"
# 设置严格模式：
set hive.mapred.mode=strict;
select * from user_trade where dt='2017-01-12';
select * from user_trade limit 6;  # 没有根据字段筛选，会报错
FAILED: SemanticException [Error 10056]: Queries against partitioned tables without a partition filter are disabled for safety reasons. If you know what you are doing, please set hive.strict.checks.no.partition.filter to false and make sure that hive.mapred.mode is not set to 'strict' to proceed. Note that you may get errors or incorrect results if you make a mistake while using some of the unsafe features. No partition predicate for Alias "user_trade" Table "user_trade"


# 取消严格模式：
set hive.mapred.mode=nonstrict;

# 创建trade_2017表
hive>create table if not exists trade_2017 (
user_name string, 
amount double, 
trade_time string)
row format delimited fields terminated by '\t';

hive>load data inpath '/datas/trade_2017/000000_0' overwrite into table trade_2017;

# 创建trade_2018表
create table if not exists trade_2018 (
user_name string, 
amount double, 
trade_time string)
row format delimited fields terminated by '\t';

load data inpath '/datas/trade_2018/000000_0' overwrite into table trade_2018;

# 创建trade_2019表
create table if not exists trade_2019 (
user_name string, 
amount double, 
trade_time string)
row format delimited fields terminated by '\t';

load data inpath '/datas/trade_2019/000000_0' overwrite into table trade_2019;


# 创建user_list_1表
create table if not exists user_list_1(
user_id string, 
user_name string)
row format delimited fields terminated by '\t'
collection items terminated by ','
map keys terminated by ':';

load data inpath '/datas/user_list_1/list1' overwrite into table user_list_1;

# 创建user_list_2表
create table if not exists user_list_2(
user_id string, 
user_name string)
row format delimited fields terminated by '\t'
collection items terminated by ','
map keys terminated by ':';

load data inpath '/datas/user_list_2/list2' overwrite into table user_list_2;




# 创建user_list_3表
create table if not exists user_list_3(
user_id string, 
user_name string)
row format delimited fields terminated by '\t'
collection items terminated by ','
map keys terminated by ':';

load data inpath '/datas/user_list_3/list3' overwrite into table user_list_3;
hive (kaikeba)> select * from user_list_3 limit 1;
"
user_list_3.user_id	user_list_3.user_name
10290	Michael
"


# 创建user_fefund表
create table if not exists user_refund(
user_name string, 
refund_piece int, 
refund_amount double, 
refund_time string)
partitioned by ( 
dt string)
row format delimited fields terminated by '\t';

# 执行如下命令以设置动态分区：
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;    
set hive.exec.max.dynamic.partitions=10000;
set hive.exec.max.dynamic.partitions.pernode=10000;
# 退出hive
`quit;`
#将数据源文件上传到HDFS上
"hdfs dfs -put /home/hadoop/datas/user_refund/* /user/hive/warehouse/kaikeba.db/user_refund"
# 启动hive
`cd /opt/module/hive安装目录`
`bin/hive`
# use数据库kaikeba
`use kaikeba;`
#修复分区表user_refund：
msck repair table user_refund;


hive (kaikeba)> set hive.mapred.mode=nonstrict; #取消hadoop用户家目录下.hiverc文件中默认的严格模式
hive (kaikeba)> select * from user_refund limit 1;
"
user_refund.user_name	user_refund.refund_piece	user_refund.refund_amount	user_refund.refund_time	user_refund.dt
Carroll	43	8600.0	2017-01-13 02:27:59	2017-01-12
"




#创建user_trade_bak表
create table user_trade_bak(
user_name string, 
piece int, 
price double, 
pay_amount double, 
goods_category string, 
pay_time timestamp)
partitioned by( 
dt string)
row format delimited fields terminated by '\t';

#执行如下命令以设置动态分区：
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;    
set hive.exec.max.dynamic.partitions=10000;
set hive.exec.max.dynamic.partitions.pernode=10000;

#将数据源文件上传到HDFS上
"hdfs dfs -put /home/hadoop/datas/user_trade_bak/* /user/hive/warehouse/kaikeba.db/user_trade_bak"

# 启动hive
`cd /opt/module/hive安装目录`
`bin/hive`
# use数据库kaikeba
`use kaikeba;`
# 修复分区表：
msck repair table user_trade_bak;
# 查看数据库kaikeba中user_trade_bak表的数据
hive (kaikeba)> set hive.mapred.mode=nonstrict; #取消hadoop用户家目录下.hiverc文件中默认的严格模式
hive (kaikeba)> select * from user_trade_bak limit 1;
"
user_trade_bak.user_name	user_trade_bak.piece	user_trade_bak.price	user_trade_bak.pay_amount	user_trade_bak.goods_category	user_trade_bak.pay_time	user_trade_bak.dt
Allison	4	688.8	2755.2	shoes	2017-01-07 20:58:49	2017-01-07
"




# 创建user_goods_category表
create table user_goods_category(
user_name string, 
category_detail string)
row format delimited fields terminated by '\t';

load data inpath '/datas/user_goods_category/000000_0' overwrite into table user_goods_category;

hive (kaikeba)> select * from user_goods_category limit 3;
'''
user_goods_category.user_name	user_goods_category.category_detail
Abby	clothes,food,electronics
Ailsa	book,clothes,food
Albert	clothes,electronics,computer
'''
```
```bash {class= ' line-numbers'}
- 在hadoop用户家目录下创建.hiverc文件  
`cd /home/hadoop`
# 添加下列三行内容到.hiverc文件
`vim .hiverc`
#在命令行中显示当前数据库名
set hive.cli.print.current.db=true; 
#查询出来的结果显示列的名称
set hive.cli.print.header=true;
#设置hive执行的严格模式
set hive.mapred.mode=strict;
```

- <font color="red">严格模式</font>：(限制3种查询) 防止用户执行那些可能产生意想不到的不好的影响的查询。

1. 分区表在查询时必须写分区条件
2. 笛卡尔积不能查询 （进行表关联的时候不写关联条件）
3. 使用order by进行排序的时候，必须加limit语句。

## 查看数据表结构
`desc formatted table_name;`

## 内部表和外部表的区别
- 内部表
    - 目前所创建的表都是所谓的管理表，有时也被称为内部表，因为这种表，Hive会（或多或少地）控制着数据的生命周期。<font color="red">当删除一个管理表时，Hive也会删除这个表中数据</font>，管理表不方便和其他工作共享数据。
- 外部表
    - 用关键字external说明
  - 指定外部表存放的数据的路径
  - 如果不指定外部表的存放路径，Hive将在HDFS上的/user/hive/warehouse文件夹下以外部表名创建一个文件夹，并且将属于这个表的数据都存放在这里
  - <font color='red'>当删除一个外部表时，只会删除表的元数据信息，而不会删除数据。</font>
  - 在生产中一般创建外部表来存储数据
  
  多部门同时操作同一个表的备份即外部表，增删改查互不影响，user文件 分析部门（user_fenxi），测试部门(user_ceshi)，用户画像部门(user_huaxiang)
  
  <font color="orange">元数据信息</font>:表名、列名、数据、存储位置等信息
  
  元数据信息是存在derby或mysql中的
  
  
## 修改表
```mysql { class= ' line-numbers'}
修改表名
ALTER TABLE log_messages RENAME TO logmsgs;
向表中添加列
ALTER TABLE log_messages ADD COLUMNS (
app_name STRING COMMENT ' Application name ' ,
session_id LONG COMMENT ' The current session id');
修改列名
ALTER TABLE table_name change column_name new_column_name new_type;
```
## 删除表
`drop table if exists table_name;`
## 清空表
`truncate table employee;`
## 分区表
> hive中有分区表的概念，我们可以看到分区具重要性能优势，而且分区表还可以将数据以一种符
> 合逻辑的方式进行组织，比如分层存储 分区表分别有静态分区和动态分区，那么它们有什么区别
> 呢？ 
>
> - 静态分区与动态分区的主要区别在于静态分区是手动指定，
> 而动态分区是通过数据来进行判断。
>     - 静态分区的列是在编译时期，通过用户传递列名来决定的；
>     - 动态分区只有在SQL执行时自动
>   - 分区表：分成了不同的文件夹  日志文件 每天都存储当天的日志并以当天日期为文件名，每一天的文件就是一个区
>     2019.10.27
>     2019.10.28

```mysql { class= ' line-numbers'}
静态分区
create table test
(name string,age int)
partitioned by (country string)
row format delimited fields terminated by '\t'
lines terminated by '\n'
stored as textfile;
在一个分区表执行hivesql，除非where语句中包含分区字段过滤条件来显示数据范围，否则不允许执行。换
句话说，就是用户不允许扫描所有的分区。进行这个限制的原因是，通常分区表都拥有非常大的数据集，而且
数据增加迅速。如果没有进行分区限制的查询可能会消耗令人不可接受的巨大资源来处理这个表。
向分区表中插入数据
insert into table test partition(country="china") values("zhangsan",1);
insert into table test partition(country="usa") values("James",34);
insert into table test partition(country="usa") values("tom",2);
查询分区表的数据
select * from test where country="china";
删除分区
alter table test drop partition(country="china");
```

```mysql { class= ' line-numbers'}
动态分区
set hive.exec.dynamic.partition=true;(可通过这个语句查看：set
hive.exec.dynamic.partition;)
set hive.exec.dynamic.partition.mode=nonstrict;
SET hive.exec.max.dynamic.partitions=100000;(如果自动分区数大于这个参数，将会报错)
SET hive.exec.max.dynamic.partitions.pernode=100000;
如何创建分区表？
create table if not exists user_trade (
user_name string,
piece int,
price double,
pay_amount double,
goods_category string,
pay_time bigint)
partitioned by (dt string)
row format delimited fields terminated by '\t';
怎么向分区表中添加数据？
显示分区数
show partitions order_part;
查询分区表中的数据
select * from user_trade limit 6;
严格模式：
set hive.mapred.mode=strict;
select * from user_trade limit 6;
select * from user_trade where dt='2017-01-12';
```
# 数据的导入和导出
```python { class= ' line-numbers'}
1.从本地导入到表中
load data local inpath '本地路径' overwrite into table sogou
[partition(partcol1=val1,....)];
2.从HDFS导入到表中
load data inpath 'HDFS上的路径' into table 表名 [partition(partcol1=val1,....)];
3.将Hive表中的数据导出到本地
insert overwrite local directory '本地路径' 查询语句;
4.将Hive表中的数据导出到HDFS
insert overwrite directory 'HDFS路径' 查询语句
```

# 作业
1. 熟悉Hive的基本概念，并总结成笔记。
2. 熟练使用HiveSQL来进行数据库和数据表的操作。
3. 总结HiveSQL和MySQL在语法上有什么不同？

# 动态分区功能示例

```mysql { class= ' line-numbers'}
第4节 test
# 动态分区功能示例：
create table pz_business_search (
interface_name     string comment'接口名称',
interface_param_in string comment'接口入参',
interface_type string comment'接口类型',
invoke_time        string comment'调用时间'
)
ROW FORMAT DELIMITED 
 FIELDS TERMINATED BY ','---数据列分隔符 
STORED AS TEXTFILE;

# 其基本数据如下：
interface1  param1  1 2018-12-19
interface2  param2  1 2018-12-19
interface3  param3  1 2018-12-19
interface4  param4  1 2018-12-19
interface1  param1  1 2018-12-20
interface2  param2  1 2018-12-20
interface3  param3  1 2018-12-20
interface4  param4  1 2018-12-20

create table pz_business_search_partition (
interface_name     string comment'接口名称',
interface_param_in string comment'接口入参'
)
partitioned by (interface_type string, invoke_time string)
ROW FORMAT DELIMITED 
 FIELDS TERMINATED BY ','---数据列分隔符 
STORED AS TEXTFILE;

# 实现动态分区：
insert overwrite table pz_business_search_partition partition (interface_type='1',invoke_time)
select interface_name,interface_param_in,invoke_time from pz_business_search;
```

# HiveSQL基础
第5节
# HiveSQL基础技能1

# HIVE简介

- HIVE是基于Hadoop的开源数据仓库工具，用于存储和处理海量结构化数据
- Hive把HDFS中结构化的数据映射成表。
- Hive通过把HiveSQL进行解析和转换，最终生成一系列基于hadoop的map/reduce任务，通过执行这些任务完成数据处理。

HiveSQL与传统SQL的对⽐：

|   查询语⾔    |          HQL          | SQL                                    |
| :----------: | :-------------------: | :------------------------------------- |
| 数据存储位置 |         HDFS          | 块设备或者本地⽂件                      |
|   数据格式   |        ⽤户定义        | 系统决定(不同的数据库有不同的存储引擎) |
|   数据更新   |         不⽀持         | ⽀持                                    |
|     索引     |           ⽆           | 有                                     |
|     执⾏      |       MapReduce       | Executor                               |
|   执⾏延迟    |           ⾼           | 低                                     |
|   可扩展性   |           ⾼           | 低                                     |
|   数据规模   |           ⼤           | ⼩                                      |
|     索引     | 0.8版本后加入位图索引 | 有复杂的索引                           |
PS：块设备是i/o设备中的⼀类，是将信息存储在固定⼤⼩的块中，每个块都有⾃⼰的地址，还可以在设备的任意位置读取⼀定⻓度的数据，例如硬盘,U盘，SD卡等。

- Hive的优势

- 把海量数据存储于 hadoop 文件系统，而不是数据库，但提供了一套类数据库的数据存储和处理机制，并采用 HQL （类 SQL ）语言对这些数据进行自动化处理
- 不仅提供了一个熟悉SQL的用户所能熟悉的编程模型，还消除了大量的通用代码，甚至那些有时是不得不使用Java编写的令人棘手的代码
- 学习成本低，可以通过类SQL语句快速实现简单的MapReduce统计，不必开发专门的MapReduce应用，十分适合数据仓库的统计分析，应用开发灵活而高效

- Hive的数据类型
  - Hive支持多种不同长度的整型和浮点型数据类型，支持布尔类型，也支持无长度限制的字符串类型。
  - Hive v0.8.0版本中增加了时间戳数据类型和二进制数组数据类型。下面列举了Hive所支持的基本数据类型。
> 注意： 所有的这些数据类型都是对Java中的接口的实现，因此这些类型的具体行为细节和Java中
对应的类型是完全一致的。例如，STRING类型实现的是Java中的String，FLOAT实现的是Java中
的float，等等。
![Hive的数据类型](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/Hive的数据类型.png "Hive的数据类型")
    - 复杂数据类型
![复杂数据类型](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/复杂数据类型.png "复杂数据类型")
```mysql { class= ' line-numbers'}
-- 案例演示：--
-- 有一个本地文件test.txt，其内容如下--
songsong,bingbing_lili,xiao song:18_xiaoxiao song:19,hui long guan_beijing
yangyang,caicai_susu,xiao yang:18_xiaoxiao yang:19,chao yang_beijing
-- 在hive中创建表test --
create table test(name string,friend array<string>,children
map<string,int>,address struct<street:string,city:string>)
row format delimited fields terminated by ',' #列分隔符
collection items terminated by '_' #map、array、struct的元素分隔符
map keys terminated by ':' #map的key与value的分隔符
lines terminated by '\n'; #行分隔符
```

- MapReduce简介

![MapReduce简介](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/MapReduce简介.png "MapReduce简介")

![MapReduce](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/MapReduce.png "MapReduce")

# 基础语法
## SELECT …A… FROM …B… WHERE …C…
```mysql { class= ' line-numbers'}
SELECT …A… FROM …B… WHERE …C…
A：列名
B：表名
C：筛选条件
```

|    user_info    | 列名举例                                                                                                        |
| :-------------: | :-------------------------------------------------------------------------------------------------------------- |
|     user_id     | 10001,10002(唯⼀的)                                                                                              |
|    user_name    | Amy, Dennis(唯⼀的)                                                                                              |
|       sex       | [male, female]                                                                                                  |
|       age       | [13,70]                                                                                                         |
|      city       | beijing, shanghai                                                                                               |
| firstactivetime | 2019-04-19 15:40:00                                                                                             |
|      level      | [1,10]                                                                                                          |
|     extra1      | string类型：{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"}             |
|     extra2      | map<string,string>类型：{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"} |

![description_tablename](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/description_tablename.png "description_tablename")

```mysql { class= ' line-numbers'}
--选出城市在北京，性别为⼥的10个⽤户名--
SELECT user_name 
FROM user_info 
WHERE city='beijing' and sex='female' 
limit 10;
```
![select_tablename_where_limit](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/select_tablename_where_limit.png "select_tablename_where_limit")



| user_trade列名 | 举例                                              |
| :------------: | :------------------------------------------------ |
|   user_name    | Amy, Dennis                                       |
|     piece      | 购买数量                                          |
|     price      | 价格                                              |
|   pay_amount   | ⽀付⾦额                                            |
| goods_category | food, clothes, book, computer, electronics, shoes |
|    pay_time    | 1323308943，时间戳                                |
|       dt       | partition，‘yyyy-mm-dd’                           |
注意：如果该表是⼀个分区表，则WHERE条件中必须对分区字段进⾏限制。
![description_tablename_partition](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/description_tablename_partition.png "description_tablename_partition")

```mysql { class= ' line-numbers'}
--选出在2019年4⽉9⽇，购买的商品品类是food的⽤户名、购买数量、⽀付⾦额--
SELECT user_name,
       piece,
       pay_amount 
FROM user_trade 
WHERE dt='2019-04-09' and goods_category='food' ;
```
<font color="red">未对分区进⾏限制的报错：</font>
```mysql { class= ' line-numbers'}
SELECT user_name,
       piece,
       pay_amount 
FROM user_trade 
WHERE goods_category='food' ;
# No partition predicate for Alias "user_trade" Table "user_trade"
# 注意！分区表必须限制分区字段！
```
#### GROUP BY

```mysql { class= ' line-numbers'}
--2019年⼀⽉到四⽉，每个品类有多少⼈购买，累计⾦额是多少--
SELECT goods_category,
       count(distinct user_name) as user_num,
       sum(pay_amount) as total_amount
FROM user_trade 
WHERE dt between '2019-01-01' and '2019-04-30'
GROUP BY goods_category;
```
GROUP BY 的作⽤：分类汇总
常⽤聚合函数：
1. count()：计数 count(distinct ……) 去重计数
2. sum()：求和
3. avg()：平均值
4. max()：最⼤值
5. min()：最⼩值

## GROUP BY …… HAVING
```mysql { class= ' line-numbers'}
--2019年4⽉，⽀付⾦额超过5万元的⽤户--
SELECT user_name,
       sum(pay_amount) as total_amount
FROM user_trade 
WHERE dt between '2019-04-01' and '2019-04-30'
GROUP BY user_name 
HAVING sum(pay_amount)>50000;
```
HAVING：对GROUP BY的对象进⾏筛选,仅返回符合HAVING条件的结果

![having_return_result](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/having_return_result.png "having_return_result")

## ORDER BY
```mysql { class= ' line-numbers'}
--2019年4⽉，⽀付⾦额最多的TOP5⽤户--
SELECT user_name,
       sum(pay_amount) as total_amount
FROM user_trade 
WHERE dt between '2019-04-01' and '2019-04-30'
GROUP BY user_name 
ORDER BY total_amount DESC  limit 5;
```
ASC：升序(默认)
DESC：降序
对多个字段进⾏排序：ORDER BY A ASC , B DESC
ORDER BY A DESC , B DESC
![order_by](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/order_by.png "order_by")
为什么ORDER BY 后⾯不直接写sum(pay_amount)⽽是⽤total_amount？
```mysql { class= ' line-numbers'}
SELECT user_name,
       sum(pay_amount) as total_amount
FROM user_trade 
WHERE dt between '2019-04-01' and '2019-04-30'
GROUP BY user_name 
ORDER BY sum(pay_amount) DESC  limit 5;   ##错误写法##
```
不可以写：ORDER BY sum(pay_amount) DESC
——原因：执⾏顺序！！！ORDER BY的执⾏顺序在SELECT之后，所以需使⽤重新定义的列名进⾏排
序。

## 执⾏顺序 

FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
![执⾏顺序](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/执⾏顺序.png "执⾏顺序") 
# 常⽤函数
## 时间戳转化为⽇期
```mysql { class= ' line-numbers'}
SELECT pay_time,
       from_unixtime(pay_time,'yyyy-MM-dd hh:mm:ss')
FROM user_trade 
WHERE dt='2019-04-09';
```

![from_unixtime_fn](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/from_unixtime_fn.png "from_unixtime_fn")

from_unixtime(bigint unixtime, string format)
format：

1. yyyy-MM-dd hh:mm:ss
2. yyyy-MM-dd hh
3. yyyy-MM-dd hh:mm
4. yyyyMMdd

拓展：把⽇期转化为时间戳——unix_timestamp
课后练习：unix_timestamp(string date)
## 计算⽇期间隔
```mysql { class= ' line-numbers'}
--⽤户的⾸次激活时间，与2019年5⽉1⽇的⽇期间隔--
SELECT user_name,
       datediff('2019-05-01',to_date(firstactivetime))
FROM user_info 
limit 10;
```
![datediff_fn](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/datediff_fn.png "datediff_fn")
datediff(string enddate, string startdate)：结束⽇期减去开始⽇期的天数

拓展：⽇期增加函数、减少函数——date_add、date_sub
date_add(string startdate, int days)
date_sub (string startdate, int days)
## 条件函数
- case when
统计以下四个年龄段20岁以下、20-30岁、30-40岁、40岁以上的⽤户数：
```mysql { class= ' line-numbers'}
--统计以下四个年龄段20岁以下、20-30岁、30-40岁、40岁以上的⽤户数--
SELECT case when age<20 then '20岁以下'
            when age>=20 and age<30 then '20-30岁'
            when age>=30 and age<40 then '30-40岁'
            else '40岁以上' end as age_type,
       count(distinct user_id) user_num
FROM user_info 
GROUP BY case when age<20 then '20岁以下'
            when age>=20 and age<30 then '20-30岁'
            when age>=30 and age<40 then '30-40岁'
            else '40岁以上' end;
```
![条件函数case_when](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/条件函数case_when.png "条件函数case_when")
- if
统计每个性别⽤户等级⾼低的分布情况：
```mysql { class= ' line-numbers'}
--统计每个性别⽤户等级⾼低的分布情况(level⼤于5为⾼级)--
SELECT sex,
       if(level>5,'高','低') as level_type,
       count(distinct user_id) user_num
FROM user_info 
GROUP BY sex,
         if(level>5,'高','低');
```
![条件函数if](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/条件函数if.png "条件函数if")
## 字符串函数
每个⽉新激活的⽤户数：
```mysql { class= ' line-numbers'}
--每个⽉新激活的⽤户数--
SELECT substr(firstactivetime,1,7) as month,
       count(distinct user_id) user_num
FROM user_info 
GROUP BY substr(firstactivetime,1,7);
```
substr(string A, int start, int len)
备注：如果不指定截取⻓度，则从起始位⼀直截取到最后。
![字符串函数subst](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/字符串函数substr.png "字符串函数subst")

不同⼿机品牌的⽤户数：
extra1(string)：
{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"}
extra2(map<string,string>)：
{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"}
```mysql { class= ' line-numbers'}
--不同⼿机品牌的⽤户数--
##第⼀种情况
SELECT get_json_object(extra1, '$.phonebrand') as phone_brand,
       count(distinct user_id) user_num
FROM user_info 
GROUP BY get_json_object(extra1, '$.phonebrand');


##第⼆种情况
SELECT extra2['phonebrand'] as phone_brand,
       count(distinct user_id) user_num
FROM user_info 
GROUP BY extra2['phonebrand'];
```
get_json_object(string json_string, string path)
param1：需要解析的json字段
param2：⽤.key取出想要获取的value
![extra12_get_json_object](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/extra12.png "extra12_get_json_object")
## 聚合统计函数
ELLA⽤户的2018年的平均⽀付⾦额，以及2018年最⼤的⽀付⽇期与最⼩的⽀付⽇期的间隔：

```mysql{ class= ' line-numbers'}
--ELLA⽤户的2018年的平均⽀付⾦额，以及2018年最⼤的⽀付⽇期与最⼩的⽀付⽇期的间隔--
SELECT avg(pay_amount) as avg_amount,
       datediff(max(from_unixtime(pay_time,'yyyy-MM-dd')),min(from_unixtime(pay_time,'yyyy-MM-dd')))
FROM user_trade 
WHERE year(dt)='2018'
      and user_name='ELLA';
```
max(from_unixtime(pay_time,'yyyy-MM-dd'))= from_unixtime(max(pay_time),'yyyy-MM-dd'))
datediff(max(pay_time),min(pay_time))
<font color="red">注意：不许嵌套组合avg(count(*))</font>
### 重点练习
- 2018年购买的商品品类在两个以上的⽤户数
```mysql { class= ' line-numbers'}
--2018年购买的商品品类在两个以上的⽤户数--
SELECT count(a.user_name)
FROM
    (SELECT user_name,
           count(distinct goods_category) as category_num
    FROM user_trade 
    WHERE year(dt)='2018'
    GROUP BY user_name HAVING count(distinct goods_category)>2)a;
```
三步⾛：
第⼀步：先求出每个⼈购买的商品品类数
第⼆步：筛选出购买商品品类数⼤于2的⽤户
第三步：统计符合条件的⽤户有多少个
- ⽤户激活时间在2018年，年龄段在20-30岁和30-40岁的婚姻状况分布
审题——拆解
第⼀步：先选出激活时间在2018年的⽤户，并把他们所在的年龄段计算好，并提取出婚姻状况
第⼆步：取出年龄段在20-30岁和30-40岁的⽤户，把他们的婚姻状况转义成可理解的说明
第三步：聚合计算，针对年龄段、婚姻状况的聚合
```mysql { class= ' line-numbers'}
--⽤户激活时间在2018年，年龄段在20-30岁和30-40岁的婚姻状况分布--
SELECT a.age_type,
       if(a.marriage_status=1,'已婚','未婚'),
       count(distinct a.user_id)
FROM 

    (SELECT case when age<20 then '20岁以下'
                when age>=20 and age<30 then '20-30岁'
                when age>=30 and age<40 then '30-40岁'
                else '40岁以上' end  as age_type,
           get_json_object(extra1, '$.marriage_status') as marriage_status,
           user_id
    FROM user_info 
    WHERE to_date(firstactivetime) between '2018-01-01' and '2018-12-31')a
    
WHERE a.age_type in ('20-30岁','30-40岁')
GROUP BY a.age_type,
         if(a.marriage_status=1,'已婚','未婚');
```

![练习婚姻状况](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/练习婚姻状况.png "练习婚姻状况")

# 常⻅错误及处理办法
## 标点符号错误
使⽤全⻆符号：
![使⽤全⻆符号错误](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/使⽤全⻆符号错误.png "使⽤全⻆符号错误")

## 没有对⼦查询的表进⾏重命名
错误实例：
```mysql { class= ' line-numbers'}
SELECT count(user_name)
FROM
    (SELECT user_name,
           count(distinct goods_category) as category_num
    FROM user_trade 
    WHERE year(date)='2019'
    GROUP BY user_name HAVING count(distinct goods_category)>2);
```
## 使⽤错误的字段名
![(使⽤错误的字段名](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/使⽤错误的字段名.png "(使⽤错误的字段名")
## 丢了逗号分隔符
![丢了逗号分隔符](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/丢了逗号分隔符.png "丢了逗号分隔符")
# 总结
1. 利⽤GROUP BY做聚合计算
2. 利⽤ORDER BY做排序
3. 牢记SQL执⾏顺序
4. 常⽤函数组合使⽤
5. 避免常⻅错误
# 作业
作业1：激活天数距今超过300天的男⼥分布情况(使⽤user_info)
作业2：不同性别、教育程度的分布情况(使⽤user_info)
作业3：2019年1⽉1⽇到2019年4⽉30⽇，每个时段的不同品类购买⾦额分布(使⽤user_trade)

# HiveSQL基础技能2
第6节
# 表连接
## INNER JOIN
![inner_join返回两个标的交集](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/inner_join返回两个标的交集.png "inner_join返回两个标的交集")
举例说明：
表1：user_list1
| user_id | user_name |
| ------- | --------- |
| 10001   | Abby      |
| 10002   | Ailsa     |
| 10003   | Alice     |
| 10004   | Alina     |
| 10005   | Allison   |
| 10006   | Angelia   |

表2：user_list2
| user_id | user_name |
| ------- | --------- |
| 10001   | Abby      |
| 10003   | Alice     |
| 10004   | Alina     |
| 10007   | Amanda    |
| 10008   | Anne      |
| 10009   | Ann       |

```mysql { class= ' line-numbers'}
--找出既在user_list_1也在user_list_2的用户--
SELECT *
FROM user_list_1 a JOIN user_list_2 b ON a.user_id=b.user_id;

# 注意：
- 表连接是，必须对表名进行重命名
- on后面使用的连接条件必须起到唯一键值的作用
- join inner中inner可省略不写，效果一样
```
![join_inner举例1](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/join_inner举例1.png "join_inner举例1")

练习：

| user_trade列名 | 举例                                              |
| -------------- | ------------------------------------------------- |
| user_name      | Amy, Dennis                                       |
| piece          | 购买数量                                          |
| price          | 价格                                              |
| pay_amount     | 支付金额                                          |
| goods_category | food, clothes, book, computer, electronics, shoes |
| pay_time       | 1323308943，时间戳                                |
| dt             | partition，‘yyyy-mm-dd’                           |

| user_refund列名 | 举例                    |
| --------------- | ----------------------- |
| user_name       | Amy, Dennis             |
| refund_piece    | 退款件数                |
| refund_amount   | 退款金额                |
| refund_time     | 1323308943，时间戳      |
| dt              | partition，‘yyyy-mm-dd’ |

```mysql { class= ' line-numbers'}
--在2019年购买后又退款的用户--
SELECT a.user_name  
FROM 
      (SELECT distinct user_name
      FROM user_trade
      WHERE year(dt)=2019)a
    JOIN
      (SELECT distinct user_name
      FROM user_refund
      WHERE year(dt)=2019)b on a.user_name=b.user_name;
```

```mysql { class= ' line-numbers'}
--常见错误：没有写别名--
SELECT user_name   
FROM 
      (SELECT distinct user_name
      FROM user_trade
      WHERE year(dt)=2019)a
    JOIN
      (SELECT distinct user_name
      FROM user_refund
      WHERE year(dt)=2019)b on a.user_name=b.user_name;

# FAILED:SemanticException Column user_name Found in more than One Tables/Subqueries
```

```mysql { class= ' line-numbers'}
--如果不去重，会怎样--
SELECT count(a.user_name),
       count(distinct a.user_name)
FROM 
      (SELECT user_name
      FROM user_trade
      WHERE year(dt)=2019)a
    JOIN
      (SELECT user_name
      FROM user_refund
      WHERE year(dt)=2019)b on a.user_name=b.user_name;

# 不去重 count(a.user_name)=61
# 去重 count(distinct a.user_name)=31
"
注意
一定要先去重，再做表连接，养成良好习惯
"
```

```mysql { class= ' line-numbers'}
--在2017年和2018年都购买的用户--
SELECT a.user_name  
FROM 
      (SELECT distinct user_name
      FROM user_trade
      WHERE year(dt)=2017)a
    JOIN
      (SELECT distinct user_name
      FROM user_trade
      WHERE year(dt)=2018)b on a.user_name=b.user_name;
```

| trade_2017&2018&2019列名 | 举例                          |
| ------------------------ | ----------------------------- |
| user_name                | Amy, Dennis                   |
| amount                   | 金额                          |
| trade_time               | 交易时间，2017-02-05 06:31:50 |

```mysql { class= ' line-numbers'}
--在2017、2018、2019年都有交易的用户--
##第一种写法
SELECT distinct a.user_name
FROM trade_2017 a
JOIN trade_2018 b on a.user_name=b.user_name
JOIN trade_2019 c on b.user_name=c.user_name;


##第二种写法
SELECT a.user_name
FROM
      (SELECT distinct user_name
      FROM trade_2017)a
    JOIN
      (SELECT distinct user_name
      FROM trade_2018)b on a.user_name=b.user_name
    JOIN

      (SELECT distinct user_name
      FROM trade_2019)c on b.user_name=c.user_name;

- 在表的数据量级很大时，推荐第二种写法
- 为什么写SELECT a.user_name呢？b.user_name或者c.user_name可以吗？当让可以
因为join是取表的交集，所以不管取哪个表的user_name字段都是一样的结果
```
```mysql { class= ' line-numbers'}
--初学者常见错误写法--
SELECT distinct a.user_name
FROM trade_2017 a
JOIN trade_2018 b
JOIN trade_2019 c on a.user_name=b.user_name=c.user_name;
```

## LEFT JOIN

表1：user_list1
| user_id | user_name |
| ------- | --------- |
| 10001   | Abby      |
| 10002   | Ailsa     |
| 10003   | Alice     |
| 10004   | Alina     |
| 10005   | Allison   |
| 10006   | Angelia   |

表2：user_list2
| user_id | user_name |
| ------- | --------- |
| 10001   | Abby      |
| 10003   | Alice     |
| 10004   | Alina     |
| 10007   | Amanda    |
| 10008   | Anne      |
| 10009   | Ann       |

```mysql { class= ' line-numbers'}
SELECT *
FROM user_list_1 a LEFT JOIN user_list_2 b ON a.user_id=b.user_id;

```
<font color="red">LEFT JOIN表连接方式</font>进行左连接后，以左边的表1为全集，返回能够匹配上的右边表2的匹配结果，没有匹配上的则显示NULL

![LEFT_JOIN_list12](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/LEFT_JOIN_list12.png "LEFT_JOIN_list12")

![RIGHT_JOIN](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/RIGHT_JOIN.png "RIGHT_JOIN")
![在user_list1表中但是不在user_list2的用户](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/在user_list1表中但是不在user_list2的用户.png "在user_list1表中但是不在user_list2的用户")
```mysql { class= ' line-numbers'}
--如何取出，在user_list1表中但是不在user_list2的用户--
SELECT a.user_id,
       a.user_name
FROM user_list_1 a LEFT JOIN user_list_2 b ON a.user_id=b.user_id
WHERE b.user_id is null;
```
- 练习：
  - 练习在2019购买，但是没有退款的用户
```mysql { class= ' line-numbers'}
--在2019购买，但是没有退款的用户--
SELECT a.user_name  
FROM 
      (SELECT distinct user_name
      FROM user_trade
      WHERE year(dt)=2019)a
    LEFT JOIN
      (SELECT distinct user_name
      FROM user_refund
      WHERE year(dt)=2019)b on a.user_name=b.user_name
WHERE b.user_name is null;
```
  - 在2019年购买用户的学历分布

| user_info 列名  | 举例                                                                                                           |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| user_id         | 10001,10002                                                                                                    |
| user_name       | Amy, Dennis                                                                                                    |
| sex             | [male, female]                                                                                                 |
| age             | [13,70]                                                                                                        |
| city            | beijing, shanghai                                                                                              |
| firstactivetime | 2019-04-19 15:40:00                                                                                            |
| level           | [1,10]                                                                                                         |
| extra1          | string类型:{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"}             |
| extra2          | map<string,string>类型:{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"} |

```mysql { class= ' line-numbers'}

SELECT b.education,
       count(distinct a.user_name)  
FROM 
      (SELECT distinct user_name
      FROM user_trade
      WHERE year(dt)=2019)a
    LEFT JOIN
      (SELECT user_name,
              get_json_object(extra1, '$.education') as education
      FROM user_info)b on a.user_name=b.user_name
GROUP BY b.education;

# 注意：get_json_object(extra1, '$.education')可以换成extra2['education']
```
![在2019年购买用户的学历分布](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/在2019年购买用户的学历分布.png "在2019年购买用户的学历分布")

  - 练习2017和2018年都购买，但是没有在2019年购买的用户

| trade_2017&2018&2019列名 | 举例                          |
| ------------------------ | ----------------------------- |
| user_name                | Amy, Dennis                   |
| amount                   | 金额                          |
| trade_time               | 交易时间，2017-02-05 06:31:50 |

```mysql { class= ' line-numbers'}
--2017和2018年都购买，但是没有在2019年购买的用户--
SELECT a.user_name
FROM
      (SELECT distinct user_name
      FROM trade_2017)a
    JOIN
      (SELECT distinct user_name
      FROM trade_2018)b on a.user_name=b.user_name
    LEFT JOIN
      (SELECT distinct user_name
      FROM trade_2019)c on b.user_name=c.user_name
WHERE c.user_name is null;
# a.user_name换成b.user_name也可以
```
```mysql { class= ' line-numbers'}
--这种写法也可以--
SELECT c.user_name
FROM
      (SELECT distinct a.user_name
      FROM trade_2017 a JOIN trade_2018 b on a.user_name=b.user_name)c
    LEFT JOIN
      (SELECT distinct user_name
      FROM trade_2019)d on c.user_name=d.user_name
WHERE d.user_name is null;
```
```mysql { class= ' line-numbers'}
--这种写法也可以，但是不推荐--
SELECT distinct a.user_name
FROM trade_2017 a 
JOIN trade_2018 b on a.user_name=b.user_name
LEFT JOIN trade_2019 c on b.user_name=c.user_name
WHERE c.user_name is null;
# 注意：如果表比较小，这样写影响不大。但是有分区的大表，这样写执行速度很慢
```

## FULL JOIN
```mysql { class= ' line-numbers'}
SELECT *
FROM user_list_1 a FULL JOIN user_list_2 b ON a.user_id=b.user_id;
```
![FULL_JOIN_list12](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/FULL_JOIN_list12.png "FULL_JOIN_list12")

![FULL_JOIN](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/FULL_JOIN.png "FULL_JOIN")

- 练习
```mysql { class= ' line-numbers'}
--user_list_1和user_list_2的所有用户--
SELECT coalesce(a.user_name,b.user_name)
FROM user_list_1 a FULL JOIN user_list_2 b on a.user_id=b.user_id;

# coalesce是一个函数，coalesce(expression1,expression2,...)依次参考各参数表达式，遇到非NULL值即停止并返回该值。如果所有的表达式都是空值，最终将返回一个空值
```
![FULL_JOIN练习](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/FULL_JOIN练习.png "FULL_JOIN练习")
## UNION ALL
UNION ALL：联合所有
表1：user_list1
| user_id | user_name |
| ------- | --------- |
| 10001   | Abby      |
| 10002   | Ailsa     |
| 10003   | Alice     |
| 10004   | Alina     |
| 10005   | Allison   |
| 10006   | Angelia   |

表3：user_list3

| user_id | user_name |
| ------- | --------- |
| 10290   | Michael   |
| 10291   | Avery     |
| 10292   | Reilly    |
| 10293   | Dillon    |
| 10294   | Walton    |

举例说明：将user_list_1和user_list_3合并在一起
```mysql { class= ' line-numbers'}
SELECT user_id,
       user_name
FROM user_list_1 
UNION ALL
SELECT user_id,
       user_name
FROM user_list_3 ;

# 注意
- 字段名称必须一致
- 字段顺序必须一致
- 没有连接条件
```
![UNION_ALL举例说明](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/UNION_ALL举例说明.png "UNION_ALL举例说明")
```mysql { class= ' line-numbers'}
--错误写法--
SELECT user_name,
       user_id
FROM user_list_1 
UNION ALL
SELECT user_id,
       user_name
FROM user_list_3;
```
![UNION_ALL错误写法](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/UNION_ALL错误写法.png "UNION_ALL错误写法")
- 练习：2017-2019年交易的所有用户数

| trade_2017&2018&2019列名 | 举例                          |
| ------------------------ | ----------------------------- |
| user_name                | Amy, Dennis                   |
| amount                   | 金额                          |
| trade_time               | 交易时间，2017-02-05 06:31:50 |

```mysql { class= ' line-numbers'}
--2017-2019年交易的所有用户数--
##写法一：UNION　ＡＬＬ
SELECT count(distinct a.user_name),
       count(a.user_name)
FROM 
    (
      SELECT user_name
      FROM trade_2017
    UNION ALL
      SELECT user_name
      FROM trade_2018
    UNION ALL
      SELECT user_name
      FROM trade_2019)a;

##写法二：UNION
SELECT count(distinct a.user_name),
       count(a.user_name)
FROM 
    (
      SELECT user_name
      FROM trade_2017
    UNION 
      SELECT user_name
      FROM trade_2018
    UNION 
      SELECT user_name
      FROM trade_2019)a;
```

### ＵＮＩＯＮ　ＡＬＬ　和ＵＮＩＯＮ的区别
如果表很大时推荐先去重，再进行union all
| 对比           | UNION ALL                        | UNION                            |
| -------------- | -------------------------------- | -------------------------------- |
| 对重复结果处理 | 不会去除重复                     | 在进行表连接后会筛选掉重复的记录 |
| 对排序的处理   | 只是简单的将两个结果合并后就返回 | 将会按照字段的顺序进行排序       |
| 效率           | 更快                             | 更慢                             |
| 总述           | 不去重不排序                     | 去重排序                         |
```mysql { class= ' line-numbers'}
--常见错误一：没有对union all 后的表进行重命名--
SELECT count(distinct user_name)
FROM 
    (
      SELECT user_name
      FROM trade_2017
    UNION ALL
      SELECT user_name
      FROM trade_2018
    UNION ALL
      SELECT user_name
      FROM trade_2019);

--常见错误二：直接对表进行union all--
SELECT count(distinct user_name)
FROM trade_2017  
UNION ALL trade_2018 
UNION ALL trade_2019;
```
- 练习：2019年每个用户的支付和退款金额汇总

| user_trade列名 | 举例                                              |
| -------------- | ------------------------------------------------- |
| user_name      | Amy, Dennis                                       |
| piece          | 购买数量                                          |
| price          | 价格                                              |
| pay_amount     | 支付金额                                          |
| goods_category | food, clothes, book, computer, electronics, shoes |
| pay_time       | 1323308943，时间戳                                |
| dt             | partition，‘yyyy-mm-dd’                           |

| user_refund列名 | 举例                    |
| --------------- | ----------------------- |
| user_name       | Amy, Dennis             |
| refund_piece    | 退款件数                |
| refund_amount   | 退款金额                |
| refund_time     | 1323308943，时间戳      |
| dt              | partition，‘yyyy-mm-dd’ |

```mysql { class= ' line-numbers'}
--UNION ALL　2019年每个用户的支付和退款金额汇总--
SELECT a.user_name,
       sum(a.pay_amount),
       sum(a.refund_amount)
FROM 
    (
      SELECT user_name,
             sum(pay_amount) as pay_amount,
             0 as refund_amount
      FROM user_trade
      WHERE year(dt)=2019
      GROUP BY user_name
    UNION ALL
      SELECT user_name,
             0 as pay_amount,
             sum(refund_amount) as refund_amount
      FROM user_refund
      WHERE year(dt)=2019
      GROUP BY user_name
    )a
GROUP BY a.user_name;
```
```mysql { class= ' line-numbers'}
--ＦＵＬＬ　ＪＯＩＮ　2019年每个用户的支付和退款金额汇总--
SELECT coalesce(a.user_name,b.user_name),
       a.pay_amount,
       b.refund_amount
FROM 
     (SELECT user_name,
             sum(pay_amount) as pay_amount
      FROM user_trade
      WHERE year(dt)=2019
      GROUP BY user_name)a
    FULL JOIN
      (SELECT user_name,
             sum(refund_amount) as refund_amount
      FROM user_refund
      WHERE year(dt)=2019
      GROUP BY user_name)b on a.user_name=b.user_name;
```
- FULL JOIN与UNION ALL 写法的有什么结果差异？
  - FULL JOIN中没有退款的人，退款金额显示NULL
- 如果用FULL JOIN，如何把NULL都变成0呢？
```mysql { class= ' line-numbers'}
SELECT coalesce(a.user_name,b.user_name),
       if(a.pay_amount is null,0,a.pay_amount),
       if(b.refund_amount is null,0,b.refund_amount)
FROM 
     (SELECT user_name,
             sum(pay_amount) as pay_amount
      FROM user_trade
      WHERE year(dt)=2019
      GROUP BY user_name)a
    FULL JOIN
      (SELECT user_name,
             sum(refund_amount) as refund_amount
      FROM user_refund
      WHERE year(dt)=2019
      GROUP BY user_name)b on a.user_name=b.user_name;
```
- 问题变形：2019年每个支付用户的支付金额和退款金额
```mysql { class= ' line-numbers'}
SELECT a.user_name,
       a.pay_amount,
       b.refund_amount
FROM 
     (SELECT user_name,
             sum(pay_amount) as pay_amount
      FROM user_trade
      WHERE year(dt)=2019
      GROUP BY user_name)a
    LEFT JOIN
      (SELECT user_name,
             sum(refund_amount) as refund_amount
      FROM user_refund
      WHERE year(dt)=2019
      GROUP BY user_name)b on a.user_name=b.user_name;

```
### 重点练习：首次激活时间在2017年，但是一直没有支付的用户年龄段分布（使用user_trade和user_info两个表）

| user_info 列名  | 举例                                                                                                            |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| user_id         | 10001,10002                                                                                                     |
| user_name       | Amy, Dennis                                                                                                     |
| sex             | [male, female]                                                                                                  |
| age             | [13,70]                                                                                                         |
| city            | beijing, shanghai                                                                                               |
| firstactivetime | 2019-04-19 15:40:00                                                                                             |
| level           | [1,10]                                                                                                          |
| extra1          | string类型：{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"}             |
| extra2          | map<string,string>类型：{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"} |

| user_trade列名 | 举例                                              |
| -------------- | ------------------------------------------------- |
| user_name      | Amy, Dennis                                       |
| piece          | 购买数量                                          |
| price          | 价格                                              |
| pay_amount     | 支付金额                                          |
| goods_category | food, clothes, book, computer, electronics, shoes |
| pay_time       | 1323308943，时间戳                                |
| dt             | partition，‘yyyy-mm-dd’                           |

```mysql { class= ' line-numbers'}
--首次激活时间在2017年，但是一直没有支付的用户年龄段分布--
SELECT a.age_level,
       count(a.user_name)
FROM 
        (SELECT user_name,
                case when age<20 then '20岁以下'
                    when age>=20 and age<30 then '20-30岁'
                    when age>=30 and age<40 then '30-40岁'
                    else '40岁以上' end as age_level
        FROM user_info
        WHERE year(firstactivetime)=2017)a
      LEFT JOIN
        (SELECT distinct user_name
        FROM user_trade
        WHERE dt>0)b on a.user_name=b.user_name
WHERE b.user_name is null
GROUP BY a.age_level;
```
 ![重点练习：首次激活时间](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/重点练习：首次激活时间.png "重点练习：首次激活时间")

```mysql { class= ' line-numbers'}
--常见错：没有对子查询中的字段进行重命名--
SELECT a.age,
       count(a.user_name)
FROM 
        (SELECT user_name,
                case when age<20 then '20岁以下'
                    when age>=20 and age<30 then '20-30岁'
                    when age>=30 and age<40 then '30-40岁'
                    else '40岁以上' end  
        FROM user_info
        WHERE year(firstactivetime)=2017)a
      LEFT JOIN
        (SELECT distinct user_name
        FROM user_trade
        WHERE dt>0)b on a.user_name=b.user_name
WHERE b.user_name is null
GROUP BY a.age;
```
### 重点练习：2018、2019年交易的用户，其激活时间段分布（使用trade_2018、trade_2019和user_info三个表）

| trade_2017&2018&2019列名 | 举例                          |
| ------------------------ | ----------------------------- |
| user_name                | Amy, Dennis                   |
| amount                   | 金额                          |
| trade_time               | 交易时间，2017-02-05 06:31:50 |

| user_info 列名  | 举例                                                                                                            |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| user_id         | 10001,10002                                                                                                     |
| user_name       | Amy, Dennis                                                                                                     |
| sex             | [male, female]                                                                                                  |
| age             | [13,70]                                                                                                         |
| city            | beijing, shanghai                                                                                               |
| firstactivetime | 2019-04-19 15:40:00                                                                                             |
| level           | [1,10]                                                                                                          |
| extra1          | string类型：{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"}             |
| extra2          | map<string,string>类型：{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"} |


```mysql { class= ' line-numbers'}
--2018、2019年交易的用户，其激活时间段分布--
SELECT hour(firstactivetime),
       count(a.user_name)
FROM 
      (
        SELECT user_name
        FROM trade_2018
      UNION 
        SELECT user_name
        FROM trade_2019)a
      LEFT JOIN user_info b on a.user_name=b.user_name
GROUP BY hour(firstactivetime);

```
![重点练习：2018、2019年交易的用户](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/重点练习：2018、2019年交易的用户.png "重点练习：2018、2019年交易的用户")
# 总结
- 在实际业务场景中，熟练选择JOIN、LEFT JOIN来解决具体问题
- 区分好FULL JOIN 和UNION ALL的使用场景
- 在多表连接时，注意各种细节和业务逻辑
- 避免常见错误
# 作业
- 在2019年购买后又退款的用户性别分布（使用user_trade、user_refund)
- 在2108年购买，但是没在2019年购买的用户城市城市分布（使用user_trade、user_refund)
- 2017-2019年，有交易单是没退款的用户的手机品牌分布（使用trade_2017、trade_2018、trade_2019、user_refund、user_info)

# HiveSQL窗⼝函数
第7节
## 累计计算窗⼝函数
### sum(…) over(……)
⼤家在做报表的时候，经常会遇到计算截⽌某⽉的累计数值，通常在EXCEL⾥可以通过函数来实现
那么在hive⾥，该如何实现这种累计数值的计算呢？——利⽤窗⼝函数！
![窗⼝函数-计算截⽌某⽉的累计数值](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/窗⼝函数-计算截⽌某⽉的累计数值.png "窗⼝函数-计算截⽌某⽉的累计数值")

- 2018年每⽉的⽀付总额和当年累积⽀付总额：
| user_trade列名 | 举例                                              |
| -------------- | ------------------------------------------------- |
| user_name      | Amy, Dennis                                       |
| piece          | 购买数量                                          |
| price          | 价格                                              |
| pay_amount     | ⽀付⾦额                                            |
| goods_category | food, clothes, book, computer, electronics, shoes |
| pay_time       | 1323308943，时间戳                                |
| dt             | partition，‘yyyy-mm-dd’                           |

```mysql { class= ' line-numbers'}
--2018年每⽉的⽀付总额和当年累积⽀付总额--
SELECT a.month,
       a.pay_amount,
       sum(a.pay_amount) over(order by a.month)
FROM 
      (SELECT month(dt) month,
              sum(pay_amount) pay_amount
      FROM user_trade
      WHERE year(dt)=2018
      GROUP BY month(dt))a;

```
![sum-over2018年每⽉的⽀付总额和当年累积⽀付总额](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/sum-over2018年每⽉的⽀付总额和当年累积⽀付总额.png "sum-over2018年每⽉的⽀付总额和当年累积⽀付总额")

- 2017-2018年每⽉的⽀付总额和当年累积⽀付总额
```mysql { class= ' line-numbers'}
--2017-2018年每⽉的⽀付总额和当年累积⽀付总额--
SELECT a.year,
       a.month,
       a.pay_amount,
       sum(a.pay_amount) over(partition by a.year order by a.month )
FROM 
      (SELECT year(dt) year,
              month(dt) month,
              sum(pay_amount) pay_amount
      FROM user_trade
      WHERE year(dt) in (2017,2018)
      GROUP BY year(dt),
               month(dt))a;

说明：
1、partition by起到分组的作⽤
2、order by 按照什么顺序进⾏累加，升序ASC、降序DESC，默认升序
```
![sum-over2017-2018年每⽉的⽀付总额和当年累积⽀付总额](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/sum-over2017-2018年每⽉的⽀付总额和当年累积⽀付总额.png "sum-over2017-2018年每⽉的⽀付总额和当年累积⽀付总额")
```mysql { class= ' line-numbers'}
--常⻅错误——分组没有限制正确：--
SELECT a.year,
       a.month,
       a.pay_amount,
       sum(a.pay_amount) over(partition by a.year,a.month order by a.month)
FROM 
      (SELECT year(dt) year,
              month(dt) month,
              sum(pay_amount) pay_amount
      FROM user_trade
      WHERE year(dt) in (2017,2018)
      GROUP BY year(dt),
               month(dt))a;
# 最终导致每⽉的数据各为⼀组，分组累计求和后和⾃⼰的数值⼀样，没有达到⽬标要求。所以，如何正确的分组⾮常关键。
```
![sum-over分组没有限制正确](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/sum-over分组没有限制正确.png "sum-over分组没有限制正确")
### avg(…) over(……)
⼤家看股票的时候，经常会看到这种K线图吧，⾥⾯经常⽤到的就是7⽇、30⽇移动平均的趋势图，那如何使⽤窗⼝函数来计算移动平均值呢？
![avgover股票移动平均的趋势图](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/avgover股票移动平均的趋势图.png "avgover股票移动平均的趋势图")
- 2018年每个⽉的近三⽉移动平均⽀付⾦额
![avg-over移动平均值定义](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/avg-over移动平均值定义.png "avg-over移动平均值定义")
```mysql { class= ' line-numbers'}
--2018年每个⽉的近三⽉移动平均⽀付⾦额--
SELECT a.month,
       a.pay_amount,
       avg(a.pay_amount) over(order by a.month rows between 2 preceding and 
current row)
FROM 
      (SELECT month(dt) month,
              sum(pay_amount) pay_amount
      FROM user_trade
      WHERE year(dt)=2018
      GROUP BY month(dt))a;

说明：
我们⽤rows between 2 preceding and current row来限制计算移动平均的范围，本语句含义是包含本⾏及前两⾏，这个就是我们题⽬中要求的近三⽉的写法。
```
![avg-over-rows-between](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/avg-over-rows-between-2-preceding-and-current-row来限制计算移动平均的范围.png "avg-over-rows-between")
### 语法总结
sum(…A…) over(partition by …B… order by …C… rows between …D1… and …D2…)
avg(…A…) over(partition by …B… order by …C… rows between …D1… and …D2…)
A：需要被加⼯的字段名称
B：分组的字段名称
C：排序的字段名称
D：计算的⾏数范围
- rows between unbounded preceding and current row——包括本⾏和之前所有的⾏
- rows between current row and unbounded following——包括本⾏和之后所有的⾏
- rows between 3 preceding and current row——包括本⾏以内和前三⾏
- rows between 3 preceding and 1 following——从前三⾏到下⼀⾏(5⾏)
拓展：
max(……) over(partition by …… order by …… rows between …… and ……)
min(……) over(partition by …… order by …… rows between …… and ……)
## 分区排序窗⼝函数
### row_number() over(……)、rank() over(……)、dense_rank() over(……)
这三个函数的作⽤都是返回相应规则的排序序号
row_number() over(partition by …A… order by …B… )
rank() over(partition by …A… order by …B… )
dense_rank() over(partition by …A… order by …B… )
A：分组的字段名称
B：排序的字段名称
注意：row_number()的这个括号内是不加任何字段名称的，rank() 和dense_rank() 同理。
- row_number：它会为查询出来的每⼀⾏记录⽣成⼀个序号，依次排序且不会重复。
- rank&dense_rank：如果使⽤rank函数来⽣成序号，over⼦句中排序字段值相同的序号是⼀样的，后⾯字段值不相同的序号将跳过相同的排名号排下⼀个，也就是相关⾏之前的排名数加⼀。
dense_rank函数在⽣成序号时是连续的，⽽rank函数⽣成的序号有可能不连续。dense_rank函数出现相同排名时，将不跳过相同排名号，rank值紧接上⼀次的rank值。在各个分组内，rank()是跳跃排序，有两个第⼀名时接下来就是第三名，dense_rank()是连续排序，有两个第⼀名时仍然跟着第⼆名。

分区排序窗⼝函数实例对⽐：

| user_trade列名 | 举例                                              |
| -------------- | ------------------------------------------------- |
| user_name      | Amy, Dennis                                       |
| piece          | 购买数量                                          |
| price          | 价格                                              |
| pay_amount     | ⽀付⾦额                                            |
| goods_category | food, clothes, book, computer, electronics, shoes |
| pay_time       | 1323308943，时间戳                                |
| dt             | partition，‘yyyy-mm-dd’                           |

```mysql { class= ' line-numbers'}
--2019年1⽉，⽤户购买商品品类数量的排名--
SELECT user_name,
       count(distinct goods_category),
       row_number() over(order by count(distinct goods_category)),
       rank() over(order by count(distinct goods_category)),
       dense_rank() over(order by count(distinct goods_category))
FROM user_trade
WHERE substr(dt,1,7)='2019-01'
GROUP BY user_name;
```
![分区排序窗⼝函数实例对⽐](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/分区排序窗⼝函数实例对⽐.png "分区排序窗⼝函数实例对⽐")

- 练习：选出2019年⽀付⾦额排名在第10、20、30名的⽤户
```mysql { class= ' line-numbers'}
--选出2019年⽀付⾦额排名在第10、20、30名的⽤户--
SELECT a.user_name,
       a.pay_amount,
       a.rank
FROM 
      (SELECT user_name,
             sum(pay_amount) pay_amount,
             rank() over(order by sum(pay_amount) desc) rank
      FROM user_trade
      WHERE year(dt)=2019
      GROUP BY user_name)a
WHERE a.rank in (10,20,30);
```
![分区排序窗⼝函数](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/分区排序窗⼝函数-%20练习.png "分区排序窗⼝函数")

## 分组排序窗⼝函数

- ntile(n) over(……)
ntile(n) over(partition by …A… order by …B… )
n：切分的⽚数
A：分组的字段名称
B：排序的字段名称
- NTILE(n)，⽤于将分组数据按照顺序切分成n⽚，返回当前切⽚值
- NTILE不⽀持ROWS BETWEEN，⽐如 NTILE(2) OVER(PARTITION BY …… ORDER BY …… ROWS
- BETWEEN 3 PRECEDING AND CURRENT ROW)
如果切⽚不均匀，默认增加第⼀个切⽚的分布

将2019年1⽉的⽀付⽤户，按照⽀付⾦额分成5组：
```mysql { class= ' line-numbers'}
--将2019年1⽉的⽀付⽤户，按照⽀付⾦额分成5组--
SELECT user_name,
       sum(pay_amount) pay_amount,
       ntile(5) over(order by sum(pay_amount) desc) level
FROM user_trade
WHERE substr(dt,1,7)='2019-01'
GROUP BY user_name;
```
![ntile-over-分组排序窗⼝函数](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/ntile-over-分组排序窗⼝函数.png "ntile-over-分组排序窗⼝函数")

- 练习：选出2019年退款⾦额排名前10%的⽤户

| user_refund列名 | 举例                    |
| --------------- | ----------------------- |
| user_name       | Amy, Dennis             |
| refund_piece    | 退款件数                |
| refund_amount   | 退款⾦额                 |
| refund_time     | 1323308943，时间戳      |
| dt              | partition，‘yyyy-mm-dd’ |

```mysql { class= ' line-numbers'}
--选出2019年退款⾦额排名前10%的⽤户--
SELECT a.user_name,
       a.refund_amount,
       a.level
FROM 
      (SELECT user_name,
             sum(refund_amount) refund_amount,
             ntile(10) over(order by sum(refund_amount) desc) level
      FROM user_refund
      WHERE year(dt)=2019
      GROUP BY user_name)a
WHERE a.level=1;
```
![ntile-over-分组排序练习](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/ntile-over-分组排序练习.png "ntile-over-分组排序练习")
## 偏移分析窗⼝函数
- lag(…) over(……)、lead(…) over(……)
Lag和Lead分析函数可以在同⼀次查询中取出同⼀字段的前N⾏的数据(Lag)和后N⾏的数据(Lead)作为独⽴的列。

在实际应⽤当中，若要⽤到取今天和昨天的某字段差值时，Lag和Lead函数的应⽤就显得尤为重要。当然，这种操作可以⽤表的⾃连接实现，但是LAG和LEAD与left join、right join等⾃连接相⽐，效率更⾼，SQL更简洁。

lag(exp_str,offset,defval) over(partion by ……order by ……)
lead(exp_str,offset,defval) over(partion by ……order by ……)
- exp_str是字段名称。
- offset是偏移量，即是上1个或上N个的值，假设当前⾏在表中排在第5⾏，则offset 为3，则表示我们所要找的数据⾏就是表中的第2⾏（即5-3=2）。offset默认值为1。
- defval默认值，当两个函数取上N/下N个值，当在表中从当前⾏位置向前数N⾏已经超出了表的范围时，lag()函数将defval这个参数值作为函数的返回值，若没有指定默认值，则返回NULL，那么在数学运算中，总要给⼀个默认值才不会出错。

### lag()实例
```mysql { class= ' line-numbers'}
--Alice和Alexander的各种时间偏移lag()--
SELECT user_name,
       dt,
       lag(dt,1,dt) over(partition by user_name order by dt),
       lag(dt) over(partition by user_name order by dt),
       lag(dt,2,dt) over(partition by user_name order by dt),
       lag(dt,2) over(partition by user_name order by dt)
FROM user_trade
WHERE dt>'0' 
      and user_name in ('Alice','Alexander');


--Alice和Alexander的各种时间偏移lead()--
SELECT user_name,
       dt,
       lead(dt,1,dt) over(partition by user_name order by dt),
       lead(dt) over(partition by user_name order by dt),
       lead(dt,2,dt) over(partition by user_name order by dt),
       lead(dt,2) over(partition by user_name order by dt)
FROM user_trade
WHERE dt>'0' 
      and user_name in ('Alice','Alexander');
```
![偏移分析窗⼝函数lag实例](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/偏移分析窗⼝函数lag实例.png "偏移分析窗⼝函数lag实例")
- lag练习：⽀付时间间隔超过100天的⽤户数
```mysql { class= ' line-numbers'}
--⽀付时间间隔超过100天的⽤户数--
SELECT count(distinct user_name)
FROM 
      (SELECT user_name,
             dt,
             lead(dt) over(partition by user_name order by dt) lead_dt
      FROM user_trade
      WHERE dt>'0' )a
WHERE a.lead_dt is not null
      and datediff(a.lead_dt,a.dt)>100;
```
## 重点练习
- 每个城市，不同性别，2018年⽀付⾦额最⾼的TOP3⽤户(使⽤user_trade和user_info两个表)

| user_info       | 列名举例                                                                                                        |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| user_id         | 10001,10002                                                                                                     |
| user_name       | Amy, Dennis                                                                                                     |
| sex             | [male, female]                                                                                                  |
| age             | [13,70]                                                                                                         |
| city            | beijing, shanghai                                                                                               |
| firstactivetime | 2019-04-19 15:40:00                                                                                             |
| level           | [1,10]                                                                                                          |
| extra1          | string类型：{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"}             |
| extra2          | map<string,string>类型：{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"} |

| user_trade列名 | 举例                                              |
| -------------- | ------------------------------------------------- |
| user_name      | Amy, Dennis                                       |
| piece          | 购买数量                                          |
| price          | 价格                                              |
| pay_amount     | ⽀付⾦额                                            |
| goods_category | food, clothes, book, computer, electronics, shoes |
| pay_time       | 1323308943，时间戳                                |
| dt             | partition，‘yyyy-mm-dd’                           |

```mysql { class= ' line-numbers'}
--每个城市，不同性别，2018年⽀付⾦额最⾼的TOP3⽤户--
SELECT c.user_name,
       c.city,
       c.sex,
       c.pay_amount,
       c.rank
FROM 
      (SELECT a.user_name,
              b.city,
              b.sex,
              a.pay_amount,
              row_number() over(partition by b.city,b.sex order by 
a.pay_amount desc) rank
      FROM 
            (SELECT user_name,
                   sum(pay_amount) pay_amount
            FROM user_trade
            WHERE year(dt)=2018
            GROUP BY user_name)a
            LEFT JOIN user_info b on a.user_name=b.user_name)c
WHERE c.rank<=3;
```
![重点练习-TOP3⽤户](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/重点练习-TOP3⽤户.png "重点练习-TOP3⽤户")

```mysql { class= ' line-numbers'}
--常⻅错误——没有指定字段的表别名--
SELECT c.user_name,
       c.city,
       c.sex,
       c.pay_amount,
       c.rank
FROM 
      (SELECT user_name,
              city,
              sex,
              pay_amount,
              row_number() over(partition by city,sex order by pay_amount 
desc) rank
      FROM 
            (SELECT user_name,
                   sum(pay_amount) pay_amount
            FROM user_trade
            WHERE year(dt)=2018
            GROUP BY user_name)a
            LEFT JOIN user_info b on a.user_name=b.user_name)c
WHERE c.rank<=3;

# Failed :SemanticException Columns user_name Found in more than One Tables/Subquries
```

- 每个⼿机品牌退款⾦额前25%的⽤户(使⽤user_refund和user_info两个表)

| user_refund列名 | 举例                    |
| --------------- | ----------------------- |
| user_name       | Amy, Dennis             |
| refund_piece    | 退款件数                |
| refund_amount   | 退款⾦额                 |
| refund_time     | 1323308943，时间戳      |
| dt              | partition，‘yyyy-mm-dd’ |

```mysql { class= ' line-numbers'}
--每个⼿机品牌退款⾦额前25%的⽤户--
SELECT *
FROM
      (SELECT a.user_name,
             extra2['phonebrand'] as phonebrand,
             a.refund_amount,
             ntile(4) over(partition by extra2['phonebrand'] order by 
a.refund_amount desc) level
      FROM 
            (SELECT user_name,
                   sum(refund_amount) refund_amount
            FROM user_refund
            WHERE dt>'0'
            GROUP BY user_name)a
            LEFT JOIN user_info b on a.user_name=b.user_name)c
WHERE c.level=1;
```
![重点练习-前25%的⽤户](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/重点练习-前25%的⽤户.png "重点练习-前25%的⽤户")

```mysql { class= ' line-numbers'}
--常⻅错误——忽略执⾏顺序，先使⽤别名后的字段做运算--
SELECT *
FROM
      (SELECT a.user_name,
             extra2['phonebrand'] as phonebrand,
             a.refund_amount,
             ntile(4) over(partition by phonebrand order by a.refund_amount 
desc) level
      FROM 
            (SELECT user_name,
                   sum(refund_amount) refund_amount
            FROM user_refund
            WHERE dt>'0'
            GROUP BY user_name)a
            LEFT JOIN user_info b on a.user_name=b.user_name)c
WHERE c.level=1;


# FAILED:SemanticException failed to breakup Wingdowing invocations into Group.
```
# 总结
- 注意如何对sum()、avg()这类累计计算的窗⼝函数的⾏数限制
- 不要混淆row_number()、rank()、dense_rank()三种函数
- 会使⽤ntile()进⾏分组查询
- lag()：前N⾏、lead()：后N⾏

# 作业
作业1：计算出每12个⽉的⽤户累计⽀付⾦额(使⽤user_trade)
作业2：计算出每4个⽉的最⼤退款⾦额(使⽤user_refund)
作业3：退款时间间隔最⻓的⽤户(使⽤user_refund)


# HiveSQL常⽤技巧
第四节

## 去重技巧——⽤group by来替换distinct

- 取出user_trade表中全部⽀付⽤户

| user_trade列名 | 举例                                              |
| -------------- | ------------------------------------------------- |
| user_name      | Amy, Dennis                                       |
| piece          | 购买数量                                          |
| price          | 价格                                              |
| pay_amount     | ⽀付⾦额                                            |
| goods_category | food, clothes, book, computer, electronics, shoes |
| pay_time       | 1323308943，时间戳                                |
| dt partition   | ，‘yyyy-mm-dd’                                    |

```mysql { class= ' line-numbers'}
--我们来测试⼀下，这两种写法的执⾏时⻓--
--取出user_trade表中全部⽀付⽤户--
##原有写法
SELECT distinct user_name 
FROM user_trade
WHERE dt>'0';


##优化写法
SELECT user_name FROM user_trade WHERE dt>'0'
GROUP BY user_name;
```
![groupby代替distinct-执行时长](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/优化-groupby代替distinct-执行时长.png "groupby代替distinct-执行时长")

```mysql { class= ' line-numbers'}
--之前案例优化--
--在2019年购买后⼜退款的⽤户--
SELECT a.user_name
FROM
      (SELECT distinct user_name 
      FROM user_trade
      WHERE year(dt)=2019)a 
    JOIN
      (SELECT distinct user_name
      FROM user_refund
      WHERE year(dt)=2019)b on a.user_name=b.user_name;


##优化写法：
SELECT a.user_name
FROM
      (SELECT user_name
      FROM user_trade
      WHERE year(dt)=2019
      GROUP BY user_name)a
    JOIN
      (SELECT user_name
      FROM user_refund
      WHERE year(dt)=2019
      GROUP BY user_name)b on a.user_name=b.user_name;
```
<font color="red">注意：使⽤场景仅限去重，不可以应⽤在去重计算count(distinct **)</font>
拓展：在极⼤的数据量(且很多重复值)时，可以先group by去重，再count()计数，效率⾼于直接count(distinct **)

## 聚合技巧——利⽤窗⼝函数grouping sets、cube、rollup

### grouping sets

- 如果我们想知道⽤户的性别分布、城市分布、等级分布，你会怎么写？

| user_info 列名  | 举例                                                                                                            |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| user_id         | 10001,10002                                                                                                     |
| user_name       | Amy, Dennis                                                                                                     |
| sex             | [male, female]                                                                                                  |
| age             | [13,70]                                                                                                         |
| city            | beijing, shanghai                                                                                               |
| firstactivetime | 2019-04-19 15:40:00                                                                                             |
| level           | [1,10]                                                                                                          |
| extra1          | string类型：{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"}             |
| extra2          | map<string,string>类型：{"systemtype":"ios","education":"master","marriage_status":"1","phonebrand":"iphone X"} |

```mysql { class= ' line-numbers'}
--通常写法：--缺点：要分别写三次SQL，需要执⾏三次，重复⼯作，且费时。
--性别分布--
SELECT sex, 
       count(distinct user_id) FROM user_info
GROUP BY sex;

--城市分布--
SELECT city, 
       count(distinct user_id) FROM user_info
GROUP BY city;

--等级分布--
SELECT level, 
       count(distinct user_id) FROM user_info
GROUP BY level;

```
- GROUPING SETS()：在group by查询中，根据不同的维度组合进⾏聚合，等价
于将不同维度的group by结果集进⾏union all。聚合规则在括号中进⾏指定。
```mysql { class= ' line-numbers'}
--优化--注意：聚合结果均在同⼀列，分类字段⽤不同列来进⾏区分

--性别、城市、等级⽤户分布--
SELECT sex,
       city,
       level, 
       count(distinct user_id) FROM user_info
GROUP BY sex,city,level
GROUPING SETS (sex,city,level);
```
![聚合性别城市等级用户分布](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/优化-聚合性别城市等级用户分布.png "聚合性别城市等级用户分布")

```mysql { class= ' line-numbers'}

如果我们想知道⽤户的性别分布以及每个性别的城市分布，你会怎么写？
--性别分布--
SELECT sex, 
       count(distinct user_id) FROM user_info
GROUP BY sex;

--每个性别的城市分布--
SELECT sex,
       city, 
       count(distinct user_id) FROM user_info
GROUP BY sex,
         city;
```
```mysql { class= ' line-numbers'}
--优化--
--性别、性别&城市的⽤户分布--
SELECT sex,
       city, 
       count(distinct user_id) FROM user_info
GROUP BY sex,city
GROUPING SETS (sex,(sex,city));
注意：第⼆列为NULL的，即是性别的⽤户分布，其余有城市的均为每个性别的城市分布
```
![groupingSets](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/优化-groupingSets性别的城市分布.png "groupingSets") 

### cube：根据group by 维度的所有组合进⾏聚合

```mysql { class= ' line-numbers'}
--性别、城市、等级的各种组合的⽤户分布--
SELECT sex,
       city,
       level,
       count(distinct user_id)
FROM user_info
GROUP BY sex,city,level
GROUPING SETS (sex,city,level,(sex,city),(sex,level),(city,level), (sex,city,level));


##优化写法 
--性别、城市、等级的各种组合的⽤户分布--
SELECT sex,
       city,
       level, 
       count(distinct user_id) FROM user_info
GROUP BY sex,city,level
with cube;

注意：跑完数据后，整理很关键！！
```

### rollup：以最左侧的维度为主，进⾏层级聚合，是cube的⼦集
```mysql{ class= ' line-numbers'}
如果我想同时计算出，每个⽉的⽀付⾦额，以及每年的总⽀付⾦额，该怎么办？
--每⽉的⽀付⾦额和每年的⽀付⾦额汇总--
SELECT a.dt,
       sum(a.year_amount), 
       sum(a.month_amount)
FROM
      (SELECT substr(dt,1,4) as dt, 
             sum(pay_amount) year_amount,
             0 as month_amount
      FROM user_trade
      WHERE dt>'0'
      GROUP BY  substr(dt,1,4)
      UNION ALL
      SELECT substr(dt,1,7) as dt,
             0 as year_amount, 
             sum(pay_amount) as month_amount 
      FROM user_trade
      WHERE dt>'0'
      GROUP BY  substr(dt,1,7)
      )a
GROUP BY a.dt;
```
![cube](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/优化-cube每月每年支付.png "cube")

```mysql{ class= ' line-numbers'}
##优化写法
SELECT year(dt) as year, 
       month(dt) as month, 
       sum(pay_amount)
FROM user_trade
WHERE dt>'0'
GROUP BY year(dt), 
         month(dt)
with rollup;
```
![rollup](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/优化-cube的优化写法rollup每月每年支付.png "rollup")
![rollup-excel](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/优化-cube的优化写法rollup每月每年支付-excel.png "rollup-excel")

## 换个思路解题

条条⼤路通罗⻢，写SQL亦是如此，能达到同样效果的SQL有很多种，要学会思路转换，灵活应⽤。
之前做过的案例：
```mysql{class="line-numbers}
--在2017年和2018年都购买的⽤户--
SELECT a.user_name
FROM
      (SELECT distinct user_name
      FROM user_trade
      WHERE year(dt)=2017)a
    JOIN
      (SELECT distinct user_name
      FROM user_trade
      WHERE year(dt)=2018)b on a.user_name=b.user_name;
```
有没有别的写法？
```mysal{class="line-numbers"}
SELECT a.user_name
FROM
    (SELECT user_name,
            count(distinct year(dt)) as year_num 
    FROM user_trade
    WHERE year(dt) in (2017,2018)
    GROUP BY user_name)a
WHERE a.year_num=2


SELECT user_name,
       count(distinct year(dt)) as year_num
FROM user_trade
WHERE year(dt) in (2017,2018)
GROUP BY user_name having count(distinct year(dt))=2
```
## union all时可以开启并发执⾏

<font color="red">参数设置：set hive.exec.parallel=true</font>
可以并⾏的任务较多时，开启并发执⾏，可以提⾼执⾏效率。
```mysql{class="line-numbers"}
--每个⽤户的⽀付和退款⾦额汇总--
SELECT a.user_name,
       sum(a.pay_amount), 
       sum(a.refund_amount)
FROM
    (
      SELECT user_name, 
             sum(pay_amount) as pay_amount,
             0 as refund_amount
      FROM user_trade
      WHERE dt>'0'
      GROUP BY user_name
    UNION ALL
      SELECT user_name,
             0 as pay_amount, 
             sum(refund_amount) as refund_amount 
      FROM user_refund
      WHERE dt>'0'
      GROUP BY user_name
    )a
GROUP BY a.user_name;
```

![unionAll并发](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/优化-unionAll并发时间对比.png "unionAll并发")

## 利⽤lateral view进⾏⾏转列
  
| user_goods_category 列名 | 举例                              |
| ------------------------ | --------------------------------- |
| user_name                | ⽤户名                             |
| category_detail          | ⽤户购买过的品类列表，⽤逗号进⾏分割 |

![user_goods_category](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/优化user_goods_category列表.png "user_goods_category")

```mysql { class= ' line-numbers'}
--每个品类的购买⽤户数--
SELECT b.category,
       count(distinct a.user_name)
FROM user_goods_category a
lateral view explode(split(category_detail,',')) b as category GROUP BY b.category;


split()：字符串分割函数
explode：⾏转列函数
拓展：
列转⾏函数：concat_ws(',',collect_set(column))
```
![lateralView-explode-split](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/优化lateralView-explode-split.png "lateralView-explode-split")

## 表连接优化

- ⼩表在前，⼤表在后
Hive假定查询中最后的⼀个表是⼤表，它会将其它表缓存起来，然后扫描最后那个表。
- 使⽤相同的连接键
当对3个或者更多个表进⾏join连接时，如果每个on⼦句都使⽤相同的连接键的话，那么只会产⽣⼀个MapReduce job。
- 尽早的过滤数据
减少每个阶段的数据量，对于分区表要加分区，同时只选择需要使⽤到的字段。
- 逻辑过于复杂时，引⼊中间表

## 如何解决数据倾斜

- 数据倾斜的表现：
任务进度⻓时间维持在99%（或100%），查看任务监控⻚⾯，发现只有少量（1个或⼏个）reduce⼦任务未完成。因为其处理的数据量和其他reduce差异过⼤。
- 数据倾斜的原因与解决办法：
	- 空值产⽣的数据倾斜
	解决：如果两个表连接时，使⽤的连接条件有很多空值，建议在连接条件中增加过滤
	例如：on a.user_id=b.user_id and a.user_id is not null
	- ⼤⼩表连接(其中⼀张表很⼤，另⼀张表⾮常⼩)
	解决：将⼩表放到内存⾥，在map端做Join
```mysql { class= ' line-numbers'}
SELECT /*+mapjoin(a)*/, 
       b.*
FROM a join b on a.**=b.**
```

  - 两个表连接条件的字段数据类型不⼀致
	解决：将连接条件的字段数据类型转换成⼀致的
	例如：on a.user_id=cast(b.user_id as string)

## 如何计算按⽉累计去重

⼤家都知道⽤sum() over()来计算按⼀定周期进⾏累计求和，但如何计算按⽉累计去重呢？
```mysql { class= ' line-numbers'}
--2017、2018年按⽉累计去重的购买⽤户数--
SELECT b.year,
       b.month,
       sum(b.user_num) over(partition by b.year order by b.month) FROM
      (SELECT a.year,
             a.month,
             count(distinct a.user_name) user_num
      FROM
          (SELECT year(dt) as year,
                 user_name,
                 min(month(dt)) as month
          FROM user_trade
          WHERE year(dt) in (2017,2018)
          GROUP BY year(dt),
                   user_name)a
      GROUP BY a.year,
               a.month)b
ORDER BY b.year,
         b.month
limit 24;
```
![sumOver](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/优化sumOver按月累计去重.png "sumOver")
有没有其他的写法？

```mysql { class= ' line-numbers'}
--2017、2018年按⽉累计去重的购买⽤户数--
set hive.mapred.mode=nonstrict;
SELECT b.month,
       count(distinct a.user_name)
FROM
        (SELECT substr(dt,1,7) as month, 
               user_name
        FROM user_trade
        WHERE year(dt) in (2017,2018)
        GROUP BY substr(dt,1,7), 
                 user_name)a
      CROSS JOIN
        (SELECT month
        FROM dim_month)b
      WHERE b.month>=a.month
            and substr(a.month,1,4)=substr(b.month,1,4) GROUP BY b.month;
```
![subStr](https://raw.githubusercontent.com/ld269440877/images/master/HiveNotebook/优化subStr按月累计去重.png "subStr")

# 总结

1. 巧⽤group by
2. 利⽤窗⼝函数提升聚合计算效率
3. 必要时开启并发执⾏
4. ⾏转列、列转⾏
5. ⼩技巧提升表连接效率
6. 多思路解题

# 作业

作业1：每个性别、不同性别和⼿机品牌的退款⾦额分布(使⽤user_refund和user_info)
作业2：把每个⽤户购买的品类变成⼀⾏，品类间⽤逗号分隔(使⽤user_trade)
作业3：2017、2018年按⽉累计去重的退款⽤户数(使⽤user_refund)

