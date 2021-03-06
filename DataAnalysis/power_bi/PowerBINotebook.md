/**
* @module power_bi
* @Version :  Power BI Desktop
* @Author: Dillon
* @Contact: aa269440877@outlook.com
* @WebSite    :   https://github.com/ld269440877/
* @description: 数据可视化—Power BI,Power BI与MySQL结合
**/

# 课前准备

1. 安装Power BI，；[Power BI Desktop 交互式报表 | Microsoft Power BI 下载链接](https://powerbi.microsoft.com/zh-cn/desktop/)
2. 了解常见的图表类型：折线图、条形图、组合图、饼图、散点图；基本图表占80%
3. 了解power query、powerpivot等；
4. 熟悉数据源，并将数据导入到数据库中；

# 课堂主题

本节课主要分成四大部分：
1、第一部分是power BI的学习指南和简介；
2、第二部分是数据可视化图表的类型；
3、第三大部分是项目实战，通过实际案例来讲power BI的应用要点和dashboard的制作流程；
4、第四大部分是综合应用：Power BI与MySQL的组合使用

# 课堂目标

1. 掌握POWER BI的建模分析流程；
2. 制作power BI的可视化仪表板dashboard，掌握dashboard的设计原则；
3. 熟练使用power BI，并且总结掌握快速入门一门软件的方法；
4. 了解可视化图表的类型；
5. Power BI与MySQL的组合使用

# 快速入门

##  学习（防坑）指南

### 构建学习框架，再学具体内容

<font color="color">先通过系统化学习（构建学习框架和知识体系）</font>，<font color="orange">再碎片化学习（具体内容）</font>

### 借助官方帮助文档、视频

查漏补缺，寻找感兴趣的点：
官方帮助文档：https://docs.microsoft.com/zh-cn/power-bi/consumer/end-user-consumer
官方学习视频：https://docs.microsoft.com/zh-cn/power-bi/guided-learning/
碎片化学习-公众号：PowerPivot工坊

### 多操作、多应用

### 多百度Google

例如：power BI 箱线图；power BI 排序；power BI 度量值；power BI DAX 函数；
## Power BI简介

### power BI 系列

桌面版、在线版、移动版
- 桌面版——Desktop：制作报表（满足日常需要）
- 在线版——Pro 和 Premium:分享写作
- 移动版——mobile:随时查看


![无秘钥不要登录自己账号使用](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi无秘钥不要登录自己账号使用，登录后有试用期.png '无秘钥不要登录自己账号使用')

### power BI 界面介绍：

多页报表视图——数据视图——关系视图
多页报表视图：
字段：菜单
可视化：图表类型、可视化对象调整、筛选器（视觉-当前图表、报告-所有报表、页面-当前页面）
获取数据、编辑数据、新建页、
管理关系、新建度量值、
发布：
建模：powerpivot
文件：导入，，，，，

 ![多页报表视图](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBI界面-多页报表视图.png '多页报表视图')
![powerBI界面-数据视图](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBI界面-数据视图.png 'powerBI界面-数据视图')
![powerBI界面-关系视图](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBI界面-关系视图.png 'powerBI界面-关系视图')

## power BI 数据可视化流程

一堆原材料，怎么做成桌菜？
数据源A——建模——清洗——可视化图表——dashboard
获取数据：power query
分析数据：power pivot
呈现数据：power view、power map（地图）
分布数据：在线版

![数据可视化流程](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBI数据可视化流程.png '数据可视化流程')

# 可视化图表类型

## 常用图表（80%）

### 折线图：时间

展示数量随时间变化的趋势
![折线图数量随时间变化趋势](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBI折线图数量随时间变化趋势.png '折线图数量随时间变化趋势')

### 条形图（柱形图）：分类

不同分组之间数据的差异；分类过多则无法展示数据特点
![条形图-柱形图-分类展示数据特点](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBI条形图-柱形图-分类展示数据特点.png '条形图-柱形图-分类展示数据特点')
### 饼图（环状图）：静态构成

![饼图-静态构成](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBI饼图-静态构成.png '饼图-静态构成')
![环状图](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBI环状图-静态构成.png '环状图')

### 散点图：分布或联系

用于发现各变量之间的关系、数据之间的规律——身高和体重
![散点图-分布或联系](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBI散点图-分布或联系.png '散点图-分布或联系')

## 高阶图表（了解即可）

图表是为了更好的说明问题，而不是追求高级，让人看不懂
合适第一，好看第二！
百度谷歌教程：power BI 漏斗图；

### 卡片图

突出显示KPI（销售额、利润、增长率、完成率等）
![卡片图-突出显示目标](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power卡片图-突出显示目标.png '卡片图-突出显示目标')
### 雷达图

了解同类别的不同属性的综合情况，以及比较不同类别的相同属性差异
![雷达图芝麻分](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power雷达图芝麻分.png '雷达图芝麻分')
![雷达图数据分析师的核心技能](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power雷达图数据分析师的核心技能.png '雷达图数据分析师的核心技能')

### 瀑布图

麦肯锡咨询公司首创
展示各成分分布构成情况，比如各项生活开支的占比情况
展示数据的累计变化过程；
![瀑布图-各成分分布构成情况](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power瀑布图-各成分分布构成情况.png '瀑布图-各成分分布构成情况')

### 箱线图

盒须图、盒式图、箱线图 因型状如箱子而得名
显示出一组数据的最大值、最小值、中位数、及上下四分位数；
![箱线图显示出一组数据的分位数](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power箱线图显示出一组数据的分位数.png '箱线图显示出一组数据的分位数')
![箱线图](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power箱线图.png '箱线图')

### 标靶图

也叫子弹图
销售业绩完成情况：
![标靶图销售业绩完成情况](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power标靶图销售业绩完成情况.png '标靶图销售业绩完成情况')

### 漏斗图

有固定流程并且环节较多的分析，可以直观地显示转化率和流失率（电商、PPT）
![漏斗图-有固定流程并且环节较多的分析](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power漏斗图-有固定流程并且环节较多的分析.png ‘漏斗图-有固定流程并且环节较多的分析’)

### 树状图

面积大小、颜色深浅代表数值大小
![树状图-面积大小颜色深浅代表数值大小](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power树状图-面积大小颜色深浅代表数值大小.png '树状图-面积大小颜色深浅代表数值大小')

### 气泡图

面积大小、颜色深浅代表数值大小
![气泡图-面积大小颜色深浅代表数值大小](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power气泡图-面积大小颜色深浅代表数值大小.png '气泡图-面积大小颜色深浅代表数值大小')

### 词云图

词云图，也叫文字云，是对文本中出现频率较高的“关键词”予以视觉化的展现，词云图过滤掉大量的低频低质的文本信息，使得浏览者只要一眼扫过文本就可领略文本的主旨。
![词云图-出现频率较高的关键词予以视觉化展现](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power词云图-出现频率较高的关键词予以视觉化展现.png '词云图-出现频率较高的关键词予以视觉化展现')

### 桑基图

桑基能量分流图，也叫桑基能量平衡图；
揭示数据复杂变化趋势的图表。
![桑基图-揭示数据复杂变化趋势的图表](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power桑基图-揭示数据复杂变化趋势的图表.png '桑基图-揭示数据复杂变化趋势的图表')

### 热力图

以特殊高亮的形式显示访客热衷的页面区域和访客所在的地理区域的图示
适合：
地理空间（拥挤程度）、网页浏览（访客兴趣焦点）
![热力图-颜色区分数据密集程度](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power热力图-颜色区分数据密集程度.png '热力图-颜色区分数据密集程度')

### 地理图

![power地理图](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/power地理图-.png 'power地理图')

# 项目实战

## 数据导入与整理

### 导入数据

数据源：文件类、数据库类、power platform 、azure、其他

![导入数据](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBI导入数据.png '导入数据')

介绍数据基本情况：
订单表等等
数据导入实际操作：
#### Excel：获取数据、加载、编辑（查询编辑器）

![Excel获取数据-加载-编辑](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBIExcel获取数据-加载-编辑.png 'Excel获取数据-加载-编辑')

#### 数据库：服务器、SQL语句

![MySQL查询获取数据](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBiMySQL查询获取数据.png 'MySQL查询获取数据')

### 使用查询编辑器（Excel数据）

删除前几行、第一行调整为标题、合并两张表格--追加查询、合并查询（vlookup、left join）
![powerBi使用查询编辑器](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi使用查询编辑器-操作Excel-SQLServer-CSV数据.png 'powerBi使用查询编辑器')

![使用查询编辑器合并](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi使用查询编辑器合并-选择表和匹配列以创建合并表.png '使用查询编辑器合并')
![询编辑器显示子字段](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi使用查询编辑器显示子字段.png '询编辑器显示子字段')

分组依据——相当于数据透视表
透视列、逆透视列
![查询编辑器分组依据](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi使用查询编辑器分组依据—相当于数据透视表.png '查询编辑器分组依据')

应用步骤——返回历史步骤
![查询编辑器应用步骤—返回历史步骤](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi使用查询编辑器应用步骤——返回历史步骤.png '查询编辑器应用步骤—返回历史步骤')

高级编辑器：M语言，不需要单独学，会改就行
![高级编辑器-M语言会改就行](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi使用查询编辑器高级编辑器-M语言会改就行.png '高级编辑器-M语言会改就行')

### 建立数据模型

载入两张数据表、确认是否建立关系、编辑关系

- 载入两张数据表
主页-->获取数据
或
主页--->编辑查询-->编辑查询-->主页--->新建源

- 创建关系
![建立数据模型-创建关系](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi建立数据模型-创建关系.png '建立数据模型-创建关系')

- 关系试图
![建立数据模型-关系视图](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBI建立数据模型-关系视图.png '建立数据模型-关系视图')

### 新建度量值和新建列

度量值：新建度量值
![新建度量值和新建列](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi新建度量值和新建列.png '新建度量值和新建列')

### DAX函数：Data Analysis eXpressions

参考Excel函数：如sum、min、max、if、int、day等等，
基于列或表的计算；引用“表”、“列”或度量值
通过“‘”或“[”启动智能感知
注：不同软件的函数相通的，Excel函数、SQL函数、Python函数等，不需要全部掌握，了解即可；

#### 聚合函数

|     函数      | 说明           |
| :-----------: | :------------- |
|      SUM      | 求和           |
|    AVERAGE    | 求平均值       |
|    MEDIEN     | 求中位值       |
|      MAX      | 求最大值       |
|      MIN      | 求最小值       |
|     COUNT     | 数值格式的计数 |
|    COUNTA     | 所有格式的计数 |
|  COUNTBLANK   | 空单元格的计数 |
|   COUNTROWS   | 表格中的行数   |
| DISTINCTCOUNT | 不重复计数     |

#### 逻辑函数

|  函数   | 说明                                          |
| :-----: | :-------------------------------------------- |
|   IF    | 根据某个/几个逻辑判断是否成立，返回指定的数值 |
| IFERROR | 如果计算出错，返回指定数值                    |
|   AND   | 逻辑关系的“且” - &&                           |
|   OR    | 逻辑关系的“或” -                              |  |
| SWITCH  | 数值转换                                      |

#### 信息函数

|   函数    | 说明       |
| :-------: | :--------- |
|  ISBLANK  | 是否空值   |
| ISNUMBER  | 是否数值   |
|  ISTEXT   | 是否文本   |
| ISNONTEST | 是否非文本 |
|  ISERROR  | 是否错误   |

#### 数学函数

|   函数    | 说明                     |
| :-------: | :----------------------- |
|    ABS    | 绝对值                   |
|   ROUND   | 四舍五入                 |
|  ROUNDUP  | 向上舍入                 |
| ROUNDDOWN | 向下舍入                 |
|    INT    | 向下舍入到整数（取整数） |

#### 文本函数

|    函数     | 说明                                           |
| :---------: | :--------------------------------------------- |
|   FORMAT    | 日期或数字格式的转换                           |
|    LEFT     | 从左向右取                                     |
|    RIGHT    | 从右向左取                                     |
|     MID     | 从中间开始取                                   |
|     LEN     | 返回指定字符串的长度                           |
|    FIND     | 查找                                           |
|   SEARCH    | 查找                                           |
|   REPLACE   | 替换                                           |
| SUBSTITUTE  | 查找替换                                       |
|    VALUE    | 转换成数值                                     |
|    BLANK    | 返回空值                                       |
| CONCATENATE | 连接字符串，等同于“&”                          |
|    LOWER    | 将字母转换成小写                               |
|    UPPER    | 将字母转换成大写                               |
|    TRIM     | 从文本中删除两个词之间除了单个空格外的所有空格 |
|    REPT     | 重复字符串                                     |

#### 转换函数

|   函数   | 说明                 |
| :------: | :------------------- |
|  FORMAT  | 日期或数字格式的转换 |
|  VALUE   | 转换成数值           |
|   INT    | 转换成整数           |
|   DATE   | 转换成日期格式       |
|   TIME   | 转换时间格式         |
| CURRENCY | 转换成货币           |

#### 时间日期函数

|   函数    | 说明                                        |
| :-------: | :------------------------------------------ |
|   YEAR    | 返回当前日期的年份                          |
|   MONTH   | 返回1到12的月份的整数                       |
|    DAY    | 返回月中第几天的整数                        |
|   HOUR    | 返回0到23的整数（小时）                     |
|  MINUTE   | 返回0到59的整数（分钟）                     |
|  SECOND   | 返回0到59的整数（秒）                       |
|   TODAY   | 返回当前的日期                              |
|    NOW    | 返回当前的日期和时间                        |
|   DATE    | 根据年、月、日生成日期                      |
|   TIME    | 根据时、分、秒生成日期时间                  |
| DATEVALUE | 将文本格式的日期转换成日期格式              |
| TIMEVALUE | 将文本格式的时间转换成日期时间格式          |
|   EDATE   | 调整日期格式中的月份                        |
|  EOMONTH  | 返回调整后的日期中月份的最后一天            |
|  WEEKDAY  | 返回1到7的整数（星期几），返回参数建议使用2 |
|  WEEKNUM  | 当前日期在一整年中的周数（1月1日开始算）    |

## 可视化报告

#TODO powerBi可视化报告 没看懂怎么操作的  要看powerbi视频

[可视化报告模板](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/可视化报告模板.pbix)
### 生成可视化报告

仪表板——报表N——报表页N——图表
设计好思路，再做报表
![可视化报告-思路](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi可视化报告-思路.png '可视化报告-思路')

![可视化报告-报表](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi可视化报告-报表.png '可视化报告-报表')

### 报告的筛选设置

视觉-当前图表、
页面-当前页面、
报告-所有报表、

- 常用筛选类型：
文本、日期、数值

![报告的筛选设置](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi报告的筛选设置.png '报告的筛选设置')

### 报告的格式设置

- 字段：
- 页面：
- 图表：参考线、数据标签、字体、标题、背景、格式对齐、边框
- 编辑交互：点击某个图形，其他更着动
    - 格式——编辑交互——筛选、无

![报告的格式设置-字段](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi报告的格式设置-字段.png '报告的格式设置-字段')
![报告的格式设置-格式](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi报告的格式设置-格式.png '报告的格式设置-格式')
![报告的格式设置-编辑交互](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi报告的格式设置-编辑交互.png '报告的格式设置-编辑交互')

### 设置报告的钻取

双击华北——所有省份——城市
轴、详细信息：区域、省份
钻取开关——深化
展开全部
添加一层、打开开关
![设置报告的钻取](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi设置报告的钻取.png '设置报告的钻取')

## Dashboard的制作原则（5分钟）

### 选择合适的图表

详见可视化图表类型部分
使用自定义可视化图表和第三方图库
visual 可视化库：官网链接[Find the right app | Microsoft AppSource](https://appsource.microsoft.com/en-us/marketplace/apps?product=power-bi-visuals&page=1&src=office&corrid=e4928050-1894-4966-aca5-ad0c569a629b&omexanonuid=cc978dd5-f0d4-4517-89d8-3c11f55a5c56&referralurl=)

导入自定义可视化图表：文件导入、应用商店导入

### Dashboard的设计建议

使用场景：给谁看、为什么看、如何看
主次分明：核心指标、一级指标、二级指标
指标体系

![Dashboard的设计建议](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBiDashboard的设计建议.png 'Dashboard的设计建议')
![Dashboard的指标体系](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBiDashboard的指标体系.png 'Dashboard的指标体系')

## Power BI与MySQL结合

[Power BI与MySQL综合应用](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/Power BI与MySQL综合应用.pbix)

## MySQL数据导入Power BI
![数据库表介绍](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerbi与MySQL结合-数据库表介绍.png '数据库表介绍')
查询语句：
```mysql { class= ' line-numbers'}
SELECT a.*,b.province,b.area,c.category,c.small_category
from spm_order a
left JOIN spm_area b on a.city = b.city
left JOIN spm_product c on a.product_id = c.product_id
```

![连接数据库](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi连接数据库.png '连接数据库')
![连接数据库-选择这些设置所应用的级别](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi连接数据库-选择这些设置所应用的级别.png '连接数据库-选择这些设置所应用的级别')

## 可视化图表

### 计算每个销售人员销售额排名top5的城市
- SQL高级查询：
```mysql { class= ' line-numbers'}
select t1.sales_name,t1.city,t1.sales,t1.rank
from
(select sales_name,city,sum(sales) as 'sales',ROW_NUMBER() OVER(PARTITION BY
sales_name ORDER BY sum(sales) DESC) as 'rank'
from spm_order
group by sales_name,city)t1
where t1.rank<=5
```
![连接数据库-SQL高级查询top5](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi连接数据库-SQL高级查询.png '连接数据库-SQL高级查询top5')

- 可视化图表
![连接数据库-可视化图表top5](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi连接数据库-可视化图表.png '连接数据库-可视化图表top5')

### 计算出盈利订单、不盈利订单和不盈不亏订单的销售额

- SQL高级查询
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
![连接数据库-SQL高级查询盈利](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi连接数据库-SQL高级查询盈利.png '连接数据库-SQL高级查询盈利')
- 可视化图表
![连接数据库-可视化图表盈利](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/powerBi连接数据库-可视化图表盈利.png '连接数据库-可视化图表盈利')

# 拓展点、未来计划、行业趋势

1、可视化的核心不是工具，而是思维，可视化可以更好的表达思想；专门做可视乎价值不大；
2、BI让更多的人可以很快上手数据分析（门槛降低），让业务人员更理解业务，了解需求，可以自助
分析；
人人都是产品经理×
人人都要会可视化√
3、商业智能软件越来越多，区别不太大，精通一个，触类旁通其他的；
4、BI产业图谱：分工越来越细，BI供应商越来越多；数据分析师日常工作是可视化图表

![Bi产业图谱](https://raw.githubusercontent.com/ld269440877/images/master/PowerBINotebook/Bi产业图谱.png 'Bi产业图谱')
[《爱分析·中国BI商业智能行业报告》](https://mp.weixin.qq.com/s/dtyv4S8xt0n5YflY7VKAzw)

# 总结

1. 可视化重在思维和操作练习，要有意识的锻炼自己的数据分析思维和实际动手能力，多练习多操
作，听懂了不一定代表掌握，实际操作中会遇到各种各样的问题
2. 数据可视化的流程：获取、分析、呈现、分享（导入数据、清洗数据、建立模型、可视化报告）
3. MySQL与power bi的组合使用
4. 总结快速掌握一门软件的方法：用途、关键点、构建学习框架，再碎片化学习

#  作业

必做题：
使用课堂上所采用的数据，制作一个dashboard（简单）
选做题：任意选择其中一道题做练习
选做题A：使用自己工作中的一份数据，制作一个dashboard（中等）
选做题B：选一个感兴趣的主题，通过爬虫或者其他途径整理一份数据源，并制作一个dashboard（较
难）




