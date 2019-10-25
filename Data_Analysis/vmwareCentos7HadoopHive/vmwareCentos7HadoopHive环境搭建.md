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

![打开网络主机名node100-手动配置以太网](centos安装-网络和主机名-打开网络主机名node100-手动配置以太网.png '打开网络主机名node100-手动配置以太网')

![-打开网络主机名node100-手动配置以太网-IPv4](centos安装-打开网络主机名node100-手动配置以太网-IPv4.png '-打开网络主机名node100-手动配置以太网-IPv4')

![手动配置以太网-IPv4-完成](centos安装-打开网络主机名node100-手动配置以太网-IPv4-完成.png '手动配置以太网-IPv4-完成')

![centos用户名密码](centos安装-centos用户名密码.png 'centos用户名密码')

![用户密码命令行登录hadoop056335](centos安装-用户密码命令行登录.png '用户密码命令行登录hadoop056335')


### 使用xshell连接虚拟机



![Xshell新建](xshell连接虚拟机-新建.png 'Xshell新建')

![名称-主机-端口号](xshell连接虚拟机-名称-主机-端口号.png '名称-主机-端口号')

![用户身份验证](xshell连接虚拟机-用户身份验证.png '用户身份验证')

![新建会话属性](xshell连接虚拟机-新建会话属性.png '新建会话属性')

## 虚拟机centos基本配置

- 切换到root用户
`su - root`

- 关闭防火墙和禁止防火墙自启动
`systemctl stop firewalld.service`
`systemctl disable firewalld.service`

- 配置时间自动同步：`crontab -e`  #我的执行这个命令后是一个空文件，文件末尾插入这一行
*/5 * * * * /usr/sbin/ntpdate ntp1.aliyun.com

- 修改/etc/hosts文件：`vim /etc/hosts`  # 修改host这三行都放到文件末尾

192.168.5.100 node100
192.168.5.101 node101
192.168.5.102 node102
- 测试是否成功添加了这三个节点，分别执行ping命令,成功即可
`ping 192.168.5.100`
64 bytes from 192.168.5.100: icmp_seq=1 ttl=64 time=0.032 ms
`ping 192.168.5.101`
`ping 192.168.5.102`
From 192.168.5.100 icmp_seq=12 Destination Host Unreachable 没安装100和102主机，正常现象

- 配置ip地址：`vim /etc/sysconfig/network-scripts/ifcfg-ens33`
第四行的BOOTPROTO="dhcp"修改为BOOTPROTO="static"

- 重启网卡: systemctl restart network

- 重启网卡后如果出问题，按如下设置就可解决
 `vim /etc/sysconfig/network-scripts/ifcfg-ens33`

![检查网卡设置](centos-检查网卡设置.png '检查网卡设置')

## CentOS7系统的基本常识

- 学习好linux系统，关键是掌握命令的使用。命令的基本格式：命令 -选项 参数
- 切换用户
    - su - 用户名
- 添加用户并设置密码
        - useradd 用户名
        - passwd 用户名
                输入密码，任意相同的密码输入两次即可
![ifconfig查看ip地址](centos-ifconfig查看ip地址.png 'ifconfig查看ip地址')

# hadoop-hive环境

## Hadoop的安装和部署

### 将软件包上传到node100

(windows使⽤xftp上传，mac使⽤scp命令上传)
- windows的ftp软件创建连接如下：
![ftp软件创建连接](Hadoop安装-ftp软件创建连接.png 'ftp软件创建连接')

![上传JDKHadoopHive文件](Hadoop安装-上传JDKHadoopHive文件.png '上传JDKHadoopHive文件')

### 切换到hadoop用户配置免密登陆

- 切换到root用户
su - root
- 关闭selinux：`vim /etc/selinux/config`
```bash
#SELINUX=enforcing
SELINUX=disabled
```
- hadoop用户在/opt下创建module目录，并修改它的所有者和所属组为hadoop
```bash
su - root
cd /opt
mkdir module
chgrp hadoop module
chown hadoop module
```

- 切换到hadoop用户配置免密登陆
cd 进入hadoop用户的家目录
`ssh-keygen -t rsa` [输入完后连按4个回车]
`ssh node100` [yes，输入hadoop用户的密码]
`ssh-copy-id node100` [输入hadoop用户的密码]
- 测试免密登录
`ssh node100`
成功：Last login: Fri Oct 25 14:20:26 2019 from node100

### 解压软件包到/opt/module

- 进入压缩包所在目录
```bash
#hadoop用户
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
```bash
#export JAVA_HOME=${JAVA_HOME}   # 被注释的行
export JAVA_HOME=/opt/module/jdk1.8.0_181  # 后添加的行

# The jsvc implementation to use. Jsvc is required to run secure datanodes   # 源文件的内容
```
2. `vim ./mapred-env.sh`

```bash
# limitations under the License.

# export JAVA_HOME=/home/y/libexec/jdk1.6.0/  # 被注释的行
export JAVA_HOME=/opt/module/jdk1.8.0_181 # 后添加的行
export HADOOP_JOB_HISTORYSERVER_HEAPSIZE=1000  # 源文件的内容

export HADOOP_MAPRED_ROOT_LOGGER=INFO,RFA  # 源文件的内容
```

3. `vim ./yarn-env.sh`

```bash
# some Java parameters   # 源文件的内容
# export JAVA_HOME=/home/y/libexec/jdk1.6.0/  # 源文件的内容
export JAVA_HOME=/opt/module/jdk1.8.0_181 # 后添加的行
if [ "$JAVA_HOME" != "" ]; then   # 源文件的内容
  #echo "run java in $JAVA_HOME"
  JAVA_HOME=$JAVA_HOME
fi
```
4. `vim ./core-site.xml`

```xml
<!-- 第一和最后一个<configuration>是源文件的内容 注意 指定HDFS中NameNode的地址node100 主机名是什么就写什么 -->
</configuration>
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
</configuration>
```

5. `vim ./hdfs-site.xml`


```xml
<!-- 第一和最后一个<configuration>是源文件的内容  注意指定Hadoop辅助名称节点主机配置 nod100 主机名是什么就写什么 -->
<configuration>
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
</configuration>
```

6. 复制mapred-site.xml.template文件 `cp ./mapred-site.xml.template ./mapred-site.xml`
修改mapred-site.xml.template副本mapred-site.xml
`vim ./mapred-site.xml`

    <!-- 指定MR运行在yarn上 -->
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
```xml

<!-- 第一和最后一个<configuration>是源文件的内容 -->
<configuration>
    <!-- 指定MR运行在yarn上 -->
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
```
7. `vim ./yarn-site.xml`

```xml
<!-- 第一和最后一个<configuration>是源文件的内容 注意指定YARN的ResourceManager的地址 value 是node100 主机名是什么就写什么-->
<configuration>

<!-- Site specific YARN configuration properties -->
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
</configuration>
```
8.`vim ./slaves`
删除文件中的默认本地localhost，添加主机名node100
node100


## Hadoop基本测试
### 格式化hadoop集群

在node100这台机器上执行：`hdfs namenode -format` 只能格式化一次

- 删除文件重新格式化hadoop集群
```bash
cd /opt/module/
# 删除 /opt/module/下的hadoopdata
rm -rf ./hadoopdata

cd hadoop-2.7.3/
#删除hadoop-2.7.3/下的logs
rm -rf logs

# 修改好配置后重新格式化hadoop集群，启动hadoop start-all.sh 查看jps
```
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
hadoop fs -mkdir /test   #在hadoop上创建文件夹 在192.168.5.100:50070网页-Utillities-Browse the file system下看到创建的test文件夹
hadoop fs -put ./word.txt /test # word.txt文件推送到hadoop上的test文件夹下，同样可以在hadoop网页服务器上查看

hadoop jar /opt/module/hadoop-2.7.3/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar wordcount /test/word.txt /output  # 提交计算任务输出结果到/output文件 output下output下产生两个文件_SUCCESS和part-r-00000

hadoop fs -cat /output/part-r-00000 # 查看执行结果，计算文件中的单词数量
```

### Hive的安装和基本操作

```bash
# 当前目录
/opt/module/hadoop-2.7.3/etc/hadoop

hive --version

# 在hdfs上创建hive数据存放目录
hadoop fs -mkdir /tmp
hadoop fs -mkdir -p /user/hive/warehouse # 递归创建目录
hadoop fs -chmod g+w /tmp  # 赋予权限
hadoop fs -chmod g+w /user/hive/warehouse

# 进入hive目录
cd /opt/module/apache-hive-3.1.1-bin/
# 在hive的软件目录下执行初始化命令
bin/schematool -dbType derby -initSchema
# 初始化成功后就会在hive的安装目录下生成derby.log日志文件和metastore_db元数据库
ls #查看
# 注意：在安全模式下，离开hadoop安全模式，没有进入安全模式不用执行下面的命令离开安全模式
hadoop dfsadmin -safemode leave

# hive只能在hive bin目录下启动
#当前目录/opt/module/apache-hive-3.1.1-bin
bin/hive

#MapReduce是一种传统的面向批量任务的处理框架。像Tez这样的新处理引擎越来越倾向于近实时的查询访问。随着Yarn的出现，HDFS正日益成为一个多租户环境，允许很多数据访问模式，例如批量访问、实时访问和交互访问。

#验证hive环境，不要随便执行操作
hive> show databases;
# 退出回到hadoop
hive> quit;

# hive和MysSQL都实现的sql标准，大部分语法是一样的，不要乱执行
```


## Hadoop概述
### Hadoop⽣态圈
- hive可以使用mapreduce、spark的作为计算引擎
![Ambari](Hadoop-Ambari.png 'Ambari')

### Hadoop的组成
Hadoop由三个模块组成：分布式存储HDFS、分布式计算MapReduce、资源调度引擎Yarn

![Hadoop组成](Hadoop-Hadoop组成.png 'Hadoop组成')

### HDFS：块级别的分布式⽂件存储系统
- 存储文件
![HDFS会计别的分布式文件存储系统](Hadoop-HDFS会计别的分布式文件存储系统.png 'HDFS会计别的分布式文件存储系统')

### MapReduce：分布式计算框架
- 运行任务，做计算
- MapReduce是采⽤⼀种分⽽治之的思想设计出来的分布式计算框架
- 如⼀复杂的计算任务，单台服务器⽆法胜任时，可将此⼤任务切分成⼀个个⼩的任务，⼩任务分别
在不同的服务器上并⾏的执⾏；最终再汇总每个⼩任务的结果
- MapReduce由两个阶段组 成：Map阶段（切分成⼀个个⼩的任务）、Reduce阶段（汇总⼩任务的结果）。

![MapReduce分布式计算框架](Hadoop-MapReduce分布式计算框架.png 'MapReduce分布式计算框架')

### Yarn：分布式资源管理器
- Yarn负责资源调度

## Hadoop的shell操作

### 启动/关闭Hadoop集群
在主节点上：start-all.sh/stop-all.sh

### 查看HDFS上的⽂件和⽬录
hadoop fs -ls -R /
### 在HDFS上创建⽂件夹
hadoop fs -mkdir -p /test/kkb
hadoop fs -mkdir /tmp  # 创建目录
hadoop fs -mkdir -p /user/hive/warehouse # 递归创建目录

### 上传⽂件
hadoop fs -put source(本地⽂件路径) dest(HDFS路径)
hadoop fs -put ./word.txt /test # word.txt文件推送到hadoop上的test文件夹下，同样可以在hadoop网页服务器上查看

### 下载⽂件
hadoop fs -get source(HDFS路径) dest(本地⽂件路径)

### 删除⽂件
hadoop fs -rm HDFS⽂件路径 hadoop fs -rm -r HDFS⽬录路径

### 查看⽂件内容
hadoop fs -cat HDFS⽂件路径
hadoop fs -cat /output/part-r-00000 # 查看执行结果，计算文件中的单词数量
### 查看集群的⼯作状态
hdfs dfsadmin -report  # 查看集群资源占用情况

# hadoop-hive启动
1. 启动hadoop：start-all.sh
2. 启动hive：
        1. hive只能在hive bin目录下启动
        2. 当前目录/opt/module/apache-hive-3.1.1-bin
                bin/hive
# hadoop-hive关闭
3. hive> quit;
4. 关闭hadoop：stop-all.sh




