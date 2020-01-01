# <font color=red>tableau介绍与基本图形可视化</font>
## 课前准备
1. 下载及安装Tableau：
   1. 下载：https://www.tableau.com/zh-cn/products
   2. 安装：按照默认安装程序流程即可。
2. Tableau入门和介绍：
>1. What is Tableau?
>>1. tableau简介：
Tableau是一款定位于数据可视化敏捷开发和实现的商务智能展现工具，可以实现交互的、可视化的分析和仪表板应用，从而帮助企业快速地认识、理解和分析业务，以应对快速变化的市场环境带来的挑战。
>>2. 主要特性：
>>>1. 高效性：Tableau通过内存数据引擎，可以直接查询外部数据，还可以动态地从数据仓库抽取数据，实时更新连接数据，大大提高数据访问和查询和分析的效率。
>>>2. 简单易用：不需要技术背景和专业统计知识，容易上手；交互可视化界面友好，操作简单。
>>>3. 可连接多种数据源：包括带分隔符的文本文件、Excel文件、SQL数据库、Oracle
数据库和多维数据库等。允许用户把多个不同数据源结合起来使用，轻松实现数据
融合。
>>3. 产品体系：
>>>1. 制作报表、视图和仪表板的桌面端设计和分析工具Tableau Desktop。
>>>2. 适用于企业部署的Tableau Server产品。
>>>3. 适用于网页上创建和分享数据可视化内容的完全免费服务产品Tableau Public。
>2. How to use Tableau？
>>1. Tableau工作区是制作工作表、设计仪表板、生成故事、发布和共享工作簿的工作环境。
>>>1. 工作表（work sheet）：又称视图，是可视化分析的基本单元。
>>>2. 仪表板（dashboard）：是多个工作表和一些对象（eg：图像、文本、网页和空白等）的组合，按照一定方式对其进行组织和布局，以揭示数据关系和内涵。
>>>3. 故事（story）：是按顺序排列的工作表或仪表板的集合，故事中各单独的工作表或仪表板称为“故事点“，以故事方式揭示各种事实之间的上下文或者事件发展关系。
>>2. 关于Tableau的数据
>>>1. Tableau连接数据后，会将数据显示在工作区的左侧，称为数据窗口，见下图框出部分。
>>>2. 数据窗口的顶部是数据源窗口，其中显示的是连接到Tableau的数据源；
>>>3. 数据源窗口下方是维度窗口和度量窗口，分别用来显示导入的维度字段和度量字段（Tableau将数据表中的一列变量称为字段）。

![主界面](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/Tableau主界面.png "主界面")
- <font color=red><b>维度窗口</b></font>显示的数据角色是维度，表示分类、事件方面的定性分类字段，以蓝色显示。将其拖放到功能区，Tableau不会对其进行计算，而是对视图进行划分或分割或者颜色标记等
- <font color=red><b>度量窗口</b></font>显示的数据角色是度量值，表示数值字段。以绿色显示。将其拖放到功能区，Tableau默认会进行聚合运算，同时，视图区产生相应的轴。离散和连续是另一种角色分类，在Tableau中，<font color=orange>蓝色是离散字段，绿色表示连续字段</font>。两者可以相互转换。
>>3. 创建工作表（视图）
>>>- 下图展示了Tableau创建视图的功能区和视图区。
>>>     - 红色范围是创建视图的主要<font color=red>功能区</font>，其中左边是卡功能区，从上至下依次是页面卡、筛选器卡、标记卡，标记卡包含了许多小的按钮如颜色、大小、标签、详细信息等；上方红色框部分为行列功能区，将数据窗口中的字段拖放至此处就会在视图区显示相应的轴或标题。
>>>     - 黑色框部分是<font color=red>视图区</font>，当我们使用卡和行列功能区进行操作时，图形的变化就会显示在视图区。
>>>     - 另外如果想新创建一个工作表、dashboard或者story，可以点击黄色框相应区域。

![创建工作表](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/Tableau创建工作表.png "创建工作表")

>>4. 创建仪表板
>>>- 完成所有工作表的视图后，我们便可以将其组织在dashboard中了。
操作方法：将创建好的工作表拖放到右侧排版区，按照一定的逻辑和布局排版好即可。

![创建仪表板](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/Tableau创建仪表板.png "创建仪表板")
## 课堂主题
在excel课程的基础上带领大家复习各类常用图形的信息展现方式和对应的应用场景，并掌握工作中常用图形条形图、柱状图、折线图、散点图、饼图、环形图、箱线图的tableau制作做法。
## 课堂目标
1. 掌握各类可视化图形的特征和信息展示方式。
2. 掌握tableau各作图功能区和对应的操作实现。
3. 掌握图形制作的基本流程和方法。
4. 深化理解各类型图表的展示特征和信息的表达形式。
5. 了解工作中的应用案例。
## 柱状图与条形图
柱状图是可视化中最常使用的图形，它可以有效地对比信息，凸显出高低、大小差异、与时序数据结合可以凸显趋势等。
###  何时使用
1. 比较不同类别的数量关系或反映时序数据的趋势。
2. 查看总体数据内部结构或结构的变化趋势。
###  使用技巧
1. 在dashboard上同时展示多个条形图。帮助浏览者略去翻页的步骤，迅速对比信息。
2. 在条形图上增加颜色，区分凸显对比效果。
3. 可以堆叠条形图去展示相关数据，便于更加深入分析。
### 常用图形
![柱状图与条形图](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/柱状图与条形图.png "柱状图与条形图")
###各地区销售概览条形图绘制步骤
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/示例超市excel源数据.png)
1. 数据源面板-数据-新建数据源-连接到文件-Microsoft excel-"示例 - 超市.xls"
将excel超市中的sheet订单拖到右侧-连接-实时，然后才会在工作表中将Sheet订单的字段和数据自动分为维度和度量两个选项卡（如果自动化分不满足要求需要手动处理）
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/数据源面板.png)
2. 在度量选项卡中创建销售利润字段，度量选项卡右击-创建-计算字段-字段名：销售利润，计算：SUM([利润])/SUM([销售额])，分别拖拽利润和销售额到sum函数中
3. 绘制条形图，了解产品在一个国家各地区的销售概览。
将度量拖到行或列中Tableau默认将该度量加总求和，
将维度字段拖到行或列中Tableau实现的是对图形按类分割的操作
4. 柱子按照销售额字段排序
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/字段销售额升降序排列.png)
5. 修改每个字段的图形颜色
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/度量推到对应的功能区点击修改颜色.png)
6. 每个柱子添加数据标签并设置单位
将度量区数量拖到标记-总和（数量）-标签
下面会增加标签T总和（数量），在他上面右击-设置格式--区-默认值-数字-数字（自定义）-显示单位-百万（M）
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/柱子添加数据标签标记并设置单位.png)
7. 每个柱子宽度大于等于空白区域的宽度
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/调整每个柱子与空白宽度比为1.png)
8. 设置筛选器-日期范围
将订单日期拖到筛选器卡-会弹出对话框-选择日期范围-下一步-应用-确定
选择筛选器卡中的订单日期-右击-显示筛选器
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/设置筛选器-日期范围.png)

### 各地区客户类型利润分布-条形图
1. 行地区-列利润
2. 将维度中的细分字段拖到标记-颜色
每一个颜色代表一个客户-公司，消费者，小型企业
3. 添加柱子上不同客户的百分比，
行总和（利润）右击-快速表计算-合计百分比（纵坐标有整数变为百分比）
行总和（利润）右击-计算依据-表（向下）（柱子变为堆积百分比柱状图，每一个柱子总量均为百分之百）
4. 每一个地区每一个客户贡献百分比添加到数据标签，
CTRL+行总和（利润）拖到标签-相当于复制百分比计算后的利润值到数据标签
5. 选择纵坐标轴标签-右击-编辑轴-轴标题-设置为利润占比
6. 订单日期拖到筛选器卡-弹出筛选器字段订单日期对话框-选择日期范围
右击筛选器卡的订单日期-显示筛选器-即可在右侧看到订单日期筛选器滚动条-筛选日期范围-条形图会随着日期范围的变化而变化
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/各地区客户类型利润分布-条形图.png)
### 各地区利润分-总销售额与利润嵌套布条形图
1. 导入数据-行总和（销售额）总和（利润）列（地区）
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/总销售额与利润嵌套分布条形图.png)
2. 任意纵坐标轴右击-双轴（左右两纵坐标轴刻度可以不同）
3. 标记-全部-自动改为条形图
4. 右击纵坐标轴-同步轴（左右两纵坐标轴刻度相同）
5. 修改利润柱子宽度小于销售总额宽度
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/修改利润柱子宽度.png)
6. 修改柱子颜色，标记-全部-颜色-交换利润和销售额柱子颜色[利润-橙色，销售额-蓝色]
7. 柱状图转换为条形图，上方工具栏-交换行和列（Ctrl+w）
8. 柱子排序，轴标签旁边有升序降序按钮或者上方工具栏上的升序降序按钮
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/柱状图柱子排序.gif)
9. 添加销售额数据标签，拖度量-销售额到标记-总和（销售额）-标签上添加数据标签，右击总和（销售额）-设置总和（销售额）格式-区-默认值-数字-数字自定义-显示单位-百万
10. 将多张工作表合并到同一个仪表板上，
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/多张工作表合并到同一个仪表板.png)
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/仪表板上的个工作表添加边框.png)
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/拖拽文本添加标题.png)
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/设置文本标题背景色.png)
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/仪表板制作完成后隐藏工作表.png)
选中仪表板右击-显示所有工作表/隐藏所有工作表
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/显示隐藏的工作表-选中仪表板中的工作表或者右击仪表板取消隐藏.png)
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/制作多表联动的筛选器.png)


## 折线图与面积图
折线图连接单个数据点，主要能展示数据随时序的变化规律。
### 何时使用
1. 希望看到数据随时序的变化，找出高点、低谷、周期性、趋势性、异常点等。
例如：过去5年股票价格的变化；过去一个月网页点击量变化；过去三年内各月份的交易额变化规律；时序数据的规律性探索。
### 使用技巧
1. 与条形图结合，折线图体现随时间的变化，条形图给出每个时间格的具体数值。
2. 将折线图下方区域加阴影，当视图中有多个折线图时，阴影可以给出更多有效信息。
### 常用图形
![折线图与面积图](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/折线图与面积图.png "折线图与面积图")
### 面积图
1. 选择折线图和面积图数据源-示例超市-订单
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/选择折线图和面积图数据源.png)
2. 在工作表中查看数据并创建计算字段发货天数（实际）
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/创建字段发货天数.png)
3. 在工作表中创建计划发货天数字段
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/在工作表中创建计划发货天数.png)
4. 在工作表中创建查看数据并计算装运状态字段
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/查看数据并创建装运状态字段.png)
5. 画总订单记录数的柱状图并且根据装运状态对柱状图进行颜色分类
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/柱状图根据装运状态进行颜色分类.png)
6. 纵坐标设置为每一个装运状态占整体的百分比-计算百分比
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/折线图修改纵坐标刻度为百分比类型.png)
7. 总订单中个运输状态占比作为标签添加到对应颜色的区域-ctrl+行总和（记录数）拖拽到标记选项卡-标签上
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/折线图-标签添加到对应颜色的区域.png)
8. 创建订单日期筛选器
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/创建订单日期筛选器.png)
9. 行列转换-标题显示与隐藏
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/折线图-行列转换-标题显示与隐藏.png)
10. 标注最近日期的订单数
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/折线图-标注最近日期的订单数.png)

### 折线图
1. 选择折线图和面积图数据源-示例超市-订单
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/选择折线图和面积图数据源.png)
2. 添加横纵轴数据-根据装运状态设置个曲线颜色-掩藏记录数（一个记录数代表一个订单）
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/折线图-设置折线图线条颜色隐藏冗余标签记录数.png)
3. 根据现有数据对未来进行预测并修改预测的时间范围
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/折线图-预测并修改预测的时间范围.png)
4. 添加订单日期筛选器-日期范围
右击筛选器卡下的订单日期-显示筛选器-工作表右侧会显示订单日期筛选器
### 各装运状态订单分布堆积图
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/各装运状态订单分布堆积图制作步骤.png)
### 各装运状态订单分布堆积图转换为百分比堆积面积图
1. 合计百分比3.5%
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/百分比堆积面积图-合计百分比.png)
2. 表向下100%
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/百分比堆积面积图-表向下100%.png)
### 多张工作表制作成一个仪表板
1. 做仪表板时先做上下调整再做左右调整
2. 拖拽成合适的布局比例即可
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/折线图仪表板-设置仪表板.png)

## 饼图和环形图
饼图和环形图用来展示整体中各类型数据的占比分布。
### 何时使用：
1. 凸显占比，反映整体数据的内部结构。
### 使用技巧：
1. 饼图和环形图的主要缺点：
   1. 饼图不适用于多分类的数据，原则上一张饼图**不可多于 6个分类**，因为随着分类的增多，每个切片就会变小，最后导致大小区分不明显，每个切片看上去都差不多大小，这样会失去使用饼图的意义。所以饼图不适合分类很多的情况。
   2. 相比于具备同样功能的其他图表（比如百分比柱状图、环图），饼图需要占据更大的画布空间。
   3. 很难进行多个饼图之间的数值比较。
2. 饼图和环形图小技巧：
   1. 超过6种的分类将不重要的归为“其他”一类。
   2. 最重要的类别放在12点钟方向。
   3. 同等重要就按照从大到小排列。
   4. 环形图中间是空的，可以放置标签，整体数据、平均数值或其他内容等，其信息表达方式与饼图类似。
### 常用图形
![饼图和环形图](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/饼图和环形图.png "饼图和环形图")
### 饼图
1. 选择数据-首先双击维度选项卡下的地区，然后双击度量选项卡下的销售额
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/饼图-选择数据.png)
2. 工作表右上角-智能显示-饼图
饼图-制作饼图-增加饼图打下-标准视图会显示多边形-设置为整个视图即可正常显示为圆形饼图
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/饼图-智能显示-饼图.png)
3. 设置标签-地区，销售额（销售额合计百分比样式）
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/饼图-标签样式.png)
4. 扇形位置根据不同的字段数据关系升降排序
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/饼图-扇形位置根据不同的字段数据关系升降排序.png)
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/饼图-根据字段排序.png)
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/饼图-手动排序.png)

### 个地区订单分布环形图
1. 制作环形图添加数据源-记录数拖拽两次到行
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/环形图-制作环形图添加数据源.png)
2. 计算两个记录数的平均值并绘制两个饼图
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/环形图-计算记录平均值并绘制两个饼图.png)
3. 根据地区设置大圆饼图颜色，根据记录数设置扇形角，双轴-同步轴合并两个大小饼图，设置小圆颜色白色，调整中坐标轴刻度将环形图置于工作表中心
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/环形图-合并并设置环形图.png)
3. 根据记录数和地区为环形图添加标签，记录数标签右击合计百分比设置为百分比样式
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/环形图-添加百分比和地区标签.png)
4. 环形图中间添加总记录数标签，将记录数拖拽到标签-小圆的平均值（记录数）-标签上
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/环形图-环形空白处即小圆上添加总记录数标签.png)
5. 调节环形图中各扇形的顺序
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/环形图-扇形排序.png)

### 饼图与地图结合使用-省产品销售数量与客户细分类型分布
1. 位置数据转换成地理数据
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/饼图与地图结合使用-位置数据转换成地理数据.png)
2. 地图上圆圈大小代表销售数量-度量-数量拖到标记-大小（气泡与地图的结合）
3. 标记-自动--》 标记-饼图
4. 维度-细分拖到标记-颜色（单一颜色的饼状图变为按照公司、消费者、小型企不同业颜色进行分类的饼状图）
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/饼图与地图结合使用-颜色进行分类的饼状图.png)
5. 地图中展示各省份-将维度-省自治区拖到标记-标签
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/饼图与地图结合使用-地图中展示各省份标签.png)

### 仪表板制作先设置好上下布局再设置左右布局
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/饼图-仪表板制作先设置好上下布局再设置左右布局.png)


## 散点图与气泡图-查看全国各省份的销售情况
### 何时使用：
1. 气泡图展示各分类数据的大小，散点图探索各不同变量之间的关系。
### 使用技巧：
1. 可以在散点图增加趋势线，以便更直观的发现规律。
2. 添加过滤器，从不同数据视角探索数据之间的关系。
3. 使用带有信息的标志类型。
![散点图与气泡图](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/散点图与气泡图.png "散点图与气泡图")
### 各省份销售额分布气泡图
1. 制作气泡图先制作柱状图然后智能显示-气泡图
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/气泡图-制作气泡图先制作柱状图然后智能显示-气泡图.png)
2. 气泡图添加标签和颜色
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/气泡图添加标签和颜色.png)
### 销售额-销售利润与折扣分布气泡图散点图和气泡图的结合
1. 整体总销售额与整体总利润分别放在行和列中默认是一个点
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/散点图-整体总销售额与整体总利润.png)
2. 每一个所对应的销售额和其产生的利润-维度-客户ID拖到标记-详细信息
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/散点图-每一个所对应的销售额和其产生的利润.png)
3. 拖拽度量-折扣到标记-大小：气泡最大的客户利润为负值说明公司给这个客户的折扣太大
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/散点图-气泡最大的客户利润为负值.png)
根据列-大于或小于销售额与行-大于或小于利润对所有客户做四象限划分
4. 创建计算字段-客户销售额均值判断：如果客户的销售额大于整体的平均销售额那么标记为大于销售额均值否则小于销售额均值
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/散点图-客户销售额均值判断.png)
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/散点图-ATTR函数.png)
5. 创建计算字段-客户利润均值判断：如果客户的利润大于整体的平均利润那么标记为大于利润均值否则小于利润均值
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/散点图-客户利润均值判断.png)
6. 根据列-大于或小于销售额与行-大于或小于利润对所有客户做四象限划分
- 由于标记-颜色拖进一个字段后载拖进另一个字段进行颜色划分会替换前一个所以通过标记-详细信息间然后修改颜色间接的给图形按照两个字段的信息进行颜色划分
  - 先将新创建的字段-客户销售额均值判断-拖到标记-颜色
  - 然后将新创建的字段-客户利润均值判断-拖到标记-详细信息-再修改详细信息标签的颜色
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/散点图-用两个字段的信息多图形对所有客户做四象限颜色划分.png)



## 箱线图
### 何时使用
1. 探索各不同分类数据下数值型数据分布情况。
### 使用技巧
1. 可以将箱线图重合的散点打乱使得数据分布展示更直观。
2. 使用带有信息的标志类型使得分类数据更直观。
### 常用图形
![箱线图](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/箱线图.png "箱线图")
## Tableau图表总结
### 相比excel，tableau有哪些优点？
![tableau优点](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/tableau比excel的优点.png "tableau优点")
### 数据类型与图形选择
![数据类型与图形选择](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/数据类型与图形选择.png "数据类型与图形选择")
![图形的相同点和差异](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/图形的相同点和差异.png "图形的相同点和差异")
### 箱线图

![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/箱线图-全国各子品类利润分布情况.png)

![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/散点图-各地区子类别利润率分布.png)
1. 拖拽度量-利润到行
2. 双击客户名称
3. 智能显示-箱线图
没有random函数客户与客户是重合的
由于个数据点在箱线图中过于集中在列中单击输入 random（）函数，使个点离散
4. 拖拽客户ID到标记-颜色将图中的个数据根据客户ID进行颜色分类
5. 拖拽地区到列，绘制各地区的箱线图
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/箱线图-各地区客户利润率分布.png)
![](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/箱线图仪表板.png)


## 总结
1. 课程内容总结：
   1. 条形图柱状图多用于展示数据的对比和内部结构随时间变化，不同的探索目标对数据的要求也不一样。
   2. 折线图和体面积图多展示趋势变化，面积图多展示整体中各部分的分布和各部分占比变化趋势。
   3. 环形图是饼图类似，但环形图中间的圆环可以展示更多信息，相比饼图更美观也能展示丰富的信息，缺点是操作比饼图复杂，此外饼图也可与地图结合使用。
   4. 散点图主要研究变量之间的关系特征，与气泡图的主要区别为变量的数量和表现形式。
   5. 箱线图多用于对比多组数内部分布或用于找出各组数据的离群点和异常值。
2. 对比excel，tableau的可视化更加简单、灵活、高效；主要体现在几个方面：
   1. 对数据的操作量级更大、运算更快。
   2. tableau中提供了更多自定义的功能和插件，可以依据需求自行调整可视化效果。
   3. tableau的交互性能更便捷，可以添加任何筛选框、标记高亮等方式来进行友好交互。
   4. tableau的工作表、仪表板、故事的结构化呈现，更好的支持了结构化表达，为分析的故事性提供了更好的展现形式。
## 作业
1. 复习tableau各部分作用并尝试拖拽各功能键提升对各作图功能区的熟练和认知程度。
2. 针对课件中涉及到的5大类14个可视化图形重现，并做成相应的dashboard，尝试讲述完整的故事。
3. 找出超市数据中退货的订单在城市和地域上的分布，这些退货的订单在品类上是否有分布特征，是否退货的这些订单主要集中在个别客户上，尝试分析并选择相应的可视化图形展示，针对结论尝试提出降低退货率的建议。

# <font color=red>Tableau高级图表实现</font>
# TODO Tableau高级图表实现有笔记copy但是还没有听课程做详细的笔记
## 课堂主题
深化学习tableau各种图形的信息展现方式和应用场景，理解tableau作图的各种要领，并掌握常用图形的制作方法。
## 课堂目标
1. 掌握tableau各相应作图功能区和对应的功能操作。
2. 学习各类不同图形信息展示特征和表达形式。
3. 了解工作中实际案例的展示方案。
## 散点图与气泡图
### 何时使用
气泡图展示各分类数据的大小，散点图探索各不同变量之间的关系。
### 使用技巧
- 可以在散点图增加趋势线，以便更直观的发现规律。
- 添加过滤器，从不同数据视角探索数据之间的关系。
- 使用带有信息的标志类型。
### 常用图形
![散点图和气泡图](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/高级-散点图和气泡图.png "散点图和气泡图")
## 箱线图
### 何时使用
探索各不同分类数据下数值型数据分布情况。
### 使用技巧
- 可以将箱线图重合的散点打乱使得数据分布展示更直观。
- 使用带有信息的标志类型。
### 常用图形
![箱线图](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/高级-箱线图.png "箱线图")
## 瀑布图
### 何时使用
探索数值型数据的内部结构，了解初始值如何受到一系列中间正负因素的影响后变成最终的汇总结果。
### 使用技巧
可用各类型数据的颜色深浅代表各分类数据的大小。
### 常用图
![瀑布图](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/高级-瀑布图.png "瀑布图")

## 漏斗图
### 何时使用
探索各行为流程中的转化效率时、多用于运营中的流量转化，用户行为分析，运营环节分析等，通过漏斗分析找出各环节的转化效率，进而定位问题。
### 使用技巧
- 可以用条形漏斗图、面积漏斗图、折线漏斗图、标记漏斗图等多种方式展示。
- 标记每个环节的转化率可以清晰的展示各环节的转化或流转情况。
- 漏斗图的左右两侧可以分别用不同的类型标记，譬如说男性和女性的转化效率，既达到漏斗分析的目的，又达到了对比的目标。
- 条形漏斗图可以用颜色的深浅来展示各环节数据的大小。
### 常用图形
![漏斗图](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/高级-漏斗图.png "漏斗图")

## 树状图
### 何时使用
展示数据内部结构<font color=red>和各叶子节点数据特征</font>。
### 常用图形
![树状图](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/高级-树状图.png "树状图")

## 组合图
### 何时使用
希望在一张图上展示多种信息，并希望通过各种组合对比信息来反映出数据问题。
### 使用技巧
- 双轴。
- 合计、汇总。
- 重合等
### 示例图形
![组合图](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/高级-组合图.png "组合图")

## 图表
### 何时使用
既需要看到数据的规律特征，又要看到数据的最原始丰富的信息。
### 使用技巧
- 可以在表格中增加颜色带代表数据的大小和变化趋势。
- 可以在表格中增加添加柱状图。
- 可以和图形结合使用。
### 常用图形
![产品销售热力图表](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/高级-产品销售热力图表.png "产品销售热力图表")
![绩效考核图表](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/高级-绩效考核图表.png "绩效考核图表")
![销售日历图表](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/高级-销售日历图表.png "销售日历图表")
## 桑吉图
### 何时使用
- 用于反映事物有方向性的流转
- 既要反映流转方向又要反映流转多少时候。
### 使用技巧
和柱状图结合使用。
![产品流向分布桑吉图](https://raw.githubusercontent.com/ld269440877/images/master/TableauVisualization/高级-产品流向分布桑吉图.png "产品流向分布桑吉图")

## 总结

- 可视化的精髓在于信息的传递和表达，用何种图形来传递自己要展示的信息需要不断的思考和打磨。

- tableau中高级图表的表达形式多样，可以依据具体的需求进行图形的各种组合、设计；工作中经常会把图形和表格放在一张仪表板中，随着统一筛选框的联动既可以从图形中发现规律，又可以从表格中获取最原始最丰富的信息。

- tableau相比excel的优点在于高效、交互和灵活，用户可以根据自己的分析主题制作不同可视化图形并制作仪表板或故事来阐述完整的问题；在阐述的同时也可借助交互功能帮助读者更好的理解。

## 知识拓展

在企业里tableau除了本地的desktop探索性分析之外，越来越多的企业把相关的数据模型搭建到线上，使用tableau的server工具把更多的分析模型固化、通过把模型和数据报表与后台数据库链接可以实现实时调度、监控和分析，大大提升了数据的使用效率和分析时效性，帮助老板进行更快速的决策和运营调整。

Tableau server 工具的特点：
- 图形丰富，在dasktop中可以展示的图形可以直接发布到线上server端。
- 数据处理效率高，交互性能强，可实时抽取数据库中的数据进行交互、探索分析，也可直接做成olap类型的工具方便指标维度的拆解和深化分析。
- 对于线上的报表、图形可以定时调度、更新，也可以按照设置定时自动的发送邮件，减少人工干预环节，降低生产成本。
- 后台监控管理、权限管控比较完善，查看，筛选、现在等行为一应俱全，都可监控到。
- 从成本方面考虑，中小型企业没有足够的产品开发资源可直接搭建tableau的线上化系统，这些企业更多使用线下的desktop离线探索。

tableau当前也出了一款数据清洗和生产的软件叫tableau prep对于分析之前的数据清洗有很大帮助，感兴趣的同学可以了解和学习一下。

## 课后习题
1、用tableau的可视化交互探索2018Q4造成西北地区的销售利润低的原因有哪些，假设自己是西北地区的销售负责人，依据自己得出的多维度结论，建议如何调整本地区的销售策略提升整体的销售利润；
尝试制作一个dashboard探索发现问题，通过问题尝试来讲述一个故事，所用的图表类型不限。

