
/**
* @module hive
* @Version :  
* @Author: Dillon
* @Contact: aa269440877@outlook.com
* @WebSite    :   https://github.com/ld269440877/
* @description: 
* @since: 2019-10-27 20:08:23
**/


hive元数据在derby中，只能在hive的安装目录下启动hive
hive的元数据在mysql中，可以在任意位置启动hive

mysql和hive都实现了SQL标准

hive处理一条sql语句：sql   解析和转换 任务


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