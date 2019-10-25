/**
* @module vmwareCentos7HadoopHive环境搭建
* @Version :  win10-vmware15-centos7-jdk1.8.0-hadoop2.7.3-hive3.1.1
* @Author: Dillon
* @Contact: aa269440877@outlook.com
* @WebSite    :   https://github.com/ld269440877/
* @description: Hive环境
**/

# win10系统下vmware安装centos7并配置网络Xhell

[大数据分析之环境部署](大数据分析之环境部署.pdf)
[VMware Workstation](https://download3.vmware.com/software/wkst/file/VMware-workstation-full-15.5.0-14665864.exe)
[vmware15序列号.txt](vmware15序列号.txt)
[虚拟机基本配置](虚拟机基本配置.txt)
[Centos7_64bit](http://isoredirect.centos.org/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-1810.iso)
[迅雷X高级版.exe在当前目录](迅雷X高级版.exe)
## 课程引入

- 回顾已经学过的技能:Excel/MySQL/Tableau/Power BI/Python
- 大数据分析和它们有什么不同？
- 为什么需要在自己电脑上部署环境？
- 课程介绍①大数据分析之环境部署②大数据分析之Hadoop学习③大数据分析之Hive学习
- 行业案例：企业级HiveSQL的应用

## 需要准备好哪些软件?

- VMware
- Xshell6
- Xftp6
- CentOS7系统
- hadoop(服务器上)
- jdk(服务器上)
- hive(服务器上)
![VmwareNat8](VmwareNat8.png 'VmwareNat8')

## 安装vmware并配置网络
### 安装vmware

![Vmware自定义安装位置](Vmware自定义安装位置.png 'Vmware自定义安装位置')
![用户体验设置取消这2项勾选](用户体验设置取消这2项勾选.png '用户体验设置取消这2项勾选')

### 配置windows vmware Network Adapter VMnet8下的Internet协议版本4

![windows下控制面板-网络和internet-网络连接](windows下控制面板-网络和internet-网络连接.png 'windows下控制面板-网络和internet-网络连接')

![vmwareNetworkAdapterVMnet8.](windows下vmwareNetworkAdapterVMnet8.png 'vmwareNetworkAdapterVMnet8.')

![VMnet8-Internet协议版本4TCPIPv4属性](windows下vmwareNetworkAdapterVMnet8-Internet协议版本4TCPIPv4属性.png 'VMnet8-Internet协议版本4TCPIPv4属性')

### 配置vmware网络

VMnet8-NAT模式
![VMnet8-NAT模式](vmware编辑-虚拟网络编辑器-选择VMnet8-NAT模式.png 'VMnet8-NAT模式')

![NAT设置](vmware-NAT设置.png 'NAT设置')

![应用-关闭](vmware-网络设置完毕-应用-关闭.png '应用-关闭')


## 安装CentOS7操作系统

### 新建1台虚拟机

![新建虚拟机](centos安装-新建虚拟机.png '新建虚拟机')

![稍后安装操作系统](centos安装-稍后安装操作系统.png '稍后安装操作系统')

![Centos7-64位](centos安装-Linux-Centos7-64位.png 'Centos7-64位')

![虚拟机名称node100-位置](centos安装-虚拟机名称node100-位置.png '虚拟机名称node100-位置')

![将虚拟磁盘拆分成多个文件](centos安装-将虚拟磁盘拆分成多个文件.png '将虚拟磁盘拆分成多个文件')

### 编辑虚拟机


![编辑虚拟机设置](centos安装-编辑虚拟机设置.png '编辑虚拟机设置')

![使用ISO映像文件](centos安装-CD-DVD使用ISO映像文件.png '使用ISO映像文件)

### 安装CentOS7操作系统

![开启次虚拟机.](centos安装-开启次虚拟机.png '开启次虚拟机.)

![InstallCentos7](centos安装-InstallCentos7.png 'InstallCentos7')

![安装信息摘要](centos安装-安装信息摘要.png '安装信息摘要')

![软件选择基本网页服务器](centos安装-语言-地区-软件选择基本网页服务器.png '软件选择基本网页服务器')

![安装目标位置-我要配置分区](centos安装-安装目标位置-我要配置分区.png '安装目标位置-我要配置分区')

![手动分区](centos安装-手动分区-boot512-swap2048-根目录剩余全部.png '手动分区')

![接受更改](centos安装-手动分区-接受更改.png '接受更改')


![打开网络主机名node100](centos安装-网络和主机名-打开网络主机名node100.png '打开网络主机名node100')

![用户密码命令行登录hadoop056335](centos安装-用户密码命令行登录.png '用户密码命令行登录hadoop056335')

### 使用xshell连接虚拟机

![Xshell新建](xshell连接虚拟机-新建.png 'Xshell新建')

![名称-主机-端口号](xshell连接虚拟机-名称-主机-端口号.png '名称-主机-端口号')

![用户身份验证](xshell连接虚拟机-用户身份验证.png '用户身份验证')

![新建会话属性](xshell连接虚拟机-新建会话属性.png '新建会话属性')

## 虚拟机centos基本配置

- 切换到root用户
su - root

- 关闭防火墙和禁止防火墙自启动
systemctl stop firewalld.service
systemctl disable firewalld.service

- 配置时间自动同步：crontab -e
*/5 * * * * /usr/sbin/ntpdate ntp1.aliyun.com

- 修改/etc/hosts文件：vim /etc/hosts  # 修改host
192.168.5.100 node100    #我的是 192.168.5.128 node100
192.168.5.101 node101
192.168.5.102 node102

- 配置ip地址：vim /etc/sysconfig/network-scripts/ifcfg-ens33
第四行的BOOTPROTO="dhcp"修改为BOOTPROTO="static"

- 重启网卡:systemctl restart network

## CentOS7系统的基本常识

- 学习好linux系统，关键是掌握命令的使用。命令的基本格式：命令 -选项 参数
- 切换用户
    - su - 用户名

# hadoop-hive环境

## Hadoop的安装和部署

### 将软件包上传到node100

(windows使⽤xftp上传，mac使⽤scp命令上传)
- windows的ftp软件创建连接如下：
![ftp软件创建连接](Hadoop安装-ftp软件创建连接.png 'ftp软件创建连接')

![上传JDKHadoopHive文件](Hadoop安装-上传JDKHadoopHive文件.png '上传JDKHadoopHive文件')

### 配置免密登陆

- hadoop用户在/opt下创建module目录，并修改它的所有者和所属组为hadoop
```bash
cd /opt
mkdir module
chgrp hadoop module
chown hadoop module
```

- 切换到root用户
su - root

cd 进入hadoop用户的家目录
`ssh-keygen -t rsa` [输入完后连按4个回车]
`ssh node100` [yes，输入hadoop用户的密码]
`ssh-copy-id node100` [输入hadoop用户的密码]

### 解压软件包到/opt/module

- 进入压缩包所在目录
```bash
cd
tar -zxvf ./jdk-8u181-linux-x64.tar.gz -C /opt/module/
tar -zxvf ./hadoop-2.7.3.tar.gz -C /opt/module/
tar -zxvf ./apache-hive-3.1.1-bin.tar.gz -C /opt/module/
```

### 编辑环境变量

```bash
vim ~/.bash_profile

#在文件末尾添加
JAVA_HOME=/opt/module/jdk1.8.0_181
HADOOP_HOME=/opt/module/hadoop-2.7.3
HIVE_HOME=/opt/module/apache-hive-3.1.1-bin
PATH=$PATH:$HOME/bin:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$HIVE_HOME/bin

export JAVA_HOME
export HADOOP_HOME
export HIVE_HOME
export PATH
```

### 重新加载环境变量

```bash
source ~/.bash_profile

# 查看版本
java -version
hadoop version
```
### 修改hadoop的配置⽂件

本文档中的替换内容保留原（缩进）格式

`cd /opt/module/hadoop-2.7.3/etc/hadoop`

1. `vim ./hadoop-env.sh`
export JAVA_HOME=/opt/module/jdk1.8.0_181
2. `vim ./mapred-env.sh`
export JAVA_HOME=/opt/module/jdk1.8.0_181
3. `vim ./yarn-env.sh`
export JAVA_HOME=/opt/module/jdk1.8.0_181
4. `vim ./core-site.xml`

        <!-- 指定HDFS中NameNode的地址 -->
        <property>
                <name>fs.defaultFS</name>
                <value>hdfs://node100:9000</value>
        </property>

        <!-- 指定Hadoop运行时产生文件的存储目录 -->
        <property>
                <name>hadoop.tmp.dir</name>
                <value>/opt/module/hadoopdata</value>
        </property>

5. `vim ./hdfs-site.xml`

        <!-- 指定HDFS副本的数量 -->
        <property>
                <name>dfs.replication</name>
                <value>1</value>
        </property>

        <!-- 指定Hadoop辅助名称节点主机配置 -->
        <property>
                <name>dfs.namenode.secondary.http-address</name>
                <value>node100:50090</value>
        </property>


6. `cp ./mapred-site.xml.template ./mapred-site.xml`
vim ./mapred-site.xml

    <!-- 指定MR运行在yarn上 -->
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>

7. `vim ./yarn-site.xml`

        <!-- Reducer获取数据的方式 -->
        <property>
                <name>yarn.nodemanager.aux-services</name>
                <value>mapreduce_shuffle</value>
        </property>

        <!-- 指定YARN的ResourceManager的地址 -->
        <property>
                <name>yarn.resourcemanager.hostname</name>
                <value>node100</value>
        </property>

        <!-- 关闭虚拟内存检查 -->
        <property>
                <name>yarn.nodemanager.vmem-check-enabled</name>
                <value>false</value>
        </property>

8.`vim ./slaves`
删除文件中的本地localhost，添加主机名node100
node100


## Hadoop基本测试
### 格式化hadoop集群

在node100这台机器上执行：`hdfs namenode -format`

### 启动/关闭hadoop集群

在node100这台机器上执行：`start-all.sh`
查看Java进程：`jps` #六个进程才是正常安装状态
在node100这台机器上执行：`stop-all.sh`

### 验证启动⻚⾯

浏览器地址栏中分别输入验证是否能访问这两个网址

192.168.5.100:50070

192.168.5.100:8088

### Hadoop的wordcount

1. 创建word.txt文本： `vim word.txt`

hello python
hello java
hello scala
hello world
welcome to beijing

2. wordcount测试

```bash
hadoop fs -mkdir /test
hadoop fs -put ./word.txt /test
hadoop jar /opt/module/hadoop-2.7.3/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar wordcount /test/word.txt /output
hadoop fs -cat /output/part-r-00000
```
### Hive的安装和基本操作

```bash
hive --version

# 在hdfs上创建hive数据存放目录
hadoop fs -mkdir /tmp
hadoop fs -mkdir -p /user/hive/warehouse
hadoop fs -chmod g+w /tmp
hadoop fs -chmod g+w /user/hive/warehouse

# 在hive的软件目录下执行初始化命令
bin/schematool -dbType derby -initSchema
# 初始化成功后就会在hive的安装目录下生成derby.log日志文件和metastore_db元数据库
# 注意：在安全模式下，离开hadoop安全模式 hadoop dfsadmin -safemode leave

# hive只能在hive bin目录下启动

#MapReduce是一种传统的面向批量任务的处理框架。像Tez这样的新处理引擎越来越倾向于近实时的查询访问。随着Yarn的出现，HDFS正日益成为一个多租户环境，允许很多数据访问模式，例如批量访问、实时访问和交互访问。
```

## Hadoop概述
### Hadoop⽣态圈

![Ambari](Hadoop-Ambari.png 'Ambari')

### Hadoop的组成
Hadoop由三个模块组成：分布式存储HDFS、分布式计算MapReduce、资源调度引擎Yarn

![Hadoop组成](Hadoop-Hadoop组成.png 'Hadoop组成')

### HDFS：块级别的分布式⽂件存储系统

![HDFS会计别的分布式文件存储系统](Hadoop-HDFS会计别的分布式文件存储系统.png 'HDFS会计别的分布式文件存储系统')

### MapReduce：分布式计算框架

- MapReduce是采⽤⼀种分⽽治之的思想设计出来的分布式计算框架
- 如⼀复杂的计算任务，单台服务器⽆法胜任时，可将此⼤任务切分成⼀个个⼩的任务，⼩任务分别
在不同的服务器上并⾏的执⾏；最终再汇总每个⼩任务的结果
- MapReduce由两个阶段组 成：Map阶段（切分成⼀个个⼩的任务）、Reduce阶段（汇总⼩任务的结果）。

![MapReduce分布式计算框架](Hadoop-MapReduce分布式计算框架.png 'MapReduce分布式计算框架')

### Yarn：分布式资源管理器


## Hadoop的shell操作

### 启动/关闭Hadoop集群
在主节点上：start-all.sh/stop-all.sh

### 查看HDFS上的⽂件和⽬录
hadoop fs -ls -R /
### 在HDFS上创建⽂件夹
hadoop fs -mkdir -p /test/kkb

### 上传⽂件
hadoop fs -put source(本地⽂件路径) dest(HDFS路径)

### 下载⽂件
hadoop fs -get source(HDFS路径) dest(本地⽂件路径)

### 删除⽂件
hadoop fs -rm HDFS⽂件路径 hadoop fs -rm -r HDFS⽬录路径

### 查看⽂件内容
hadoop fs -cat HDFS⽂件路径

### 查看集群的⼯作状态
hdfs dfsadmin -report






