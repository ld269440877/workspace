# vultr-centos7X64-build-vpn

2020年1月1日20:36:45

## 自建翻墙相较于付费VPN翻墙的优势

- 自建获得的时独立IP，在安全性，稳定性【尤其是社交账号的培养】强于付费VPN
- 自建使用人数使用人数可控，速度上理论上有一定优势
[SSD VPS Servers, Cloud Servers and Cloud Hosting by Vultr - Vultr.com](https://www.vultr.com/)

## 付费shadowsocks服务商 Just My Socks

如果倾向于用ss翻墙的，可以先看 JMS的服务，官方承诺7/24小时更新IP保证可用。
[Portal Home - Just My Socks](https://justmysocks1.net/members/)


最主要是Vultr按分钟计费，IP不能用的时候可以直接删除，不会多扣钱。

## Vultr主机的注册及简单设置

> VPS主机我用的是Vultr,我也推荐新手从Vultr开始用。原因有两个。
> 1. Vultr计费是按需计费，注册账号不需要直接付款，即使绑定了paypal或信用卡，不开实例不扣钱。【如果搭建一半计划有变或者觉得麻烦想直接购买付费VPN完全不受影响】
> 2. Vultr使用灵活，付费VPN至少按月订阅。Vultr按秒计费。假期旅游不想用不能用，随时关掉实例。一点不浪费。
> 3. Vultr有内置的Open VPN应用，傻瓜式搭建以及连接，非常方便。相比较于搬瓦工的openvpn连接，简单了不知道多少倍。

1. 首先点击进入[Vultr官网](https://www.vultr.com/) 注册账号
2. 输入相关注册信息，然后点击创建账户

> 其中密码的规则需要注意一下：
>- 至少10个字符
>- 必须有一个大写字母
>- 必须有一个小写字母
>- 至少含有一个数字

3. 创建好账户之后，你会收到一封邮件，你需要点击邮件中的链接验证邮箱。
然后就可用登录账号，登录账号进入后台之后会看到右边有10美金
【也有可能没有赠送，根据活动状况】的额度可以用【必须通过链
接注册才有哦支付宝Alipay支付**首次最低充值10美金**后就会被激活

# 第一种VPN搭建方案：利用OpenVPN协议链接

## 进入Vultr首页-Products-右侧加号Deploy New Server

<img src="https://raw.githubusercontent.com/ld269440877/images/master/vultr-centos7X64-build-vpn/右侧加号DeployNewServer.png" alt="右侧加号DeployNewServer"  title="右侧加号DeployNewServer" width="600" height="">

## Deploy New Instance

- Choose Server-Cloud Compute
- Server Location-All Location-Tokyo
- Server Type-Application-OpenVPN
- Server Size-$5/month
- Deploy Now
- 服务器安装
- Server Information

<img src="https://raw.githubusercontent.com/ld269440877/images/master/vultr-centos7X64-build-vpn/DeployNewInstance.png" alt="DeployNewInstance"  title="DeployNewInstance" width="600" height="">

<img src="https://raw.githubusercontent.com/ld269440877/images/master/vultr-centos7X64-build-vpn/服务器安装.png" alt="服务器安装"  title="服务器安装" width="600" height="">

<img src="https://raw.githubusercontent.com/ld269440877/images/master/vultr-centos7X64-build-vpn/ServerInformation.png" alt="ServerInformation"  title="ServerInformation" width="600" height="">

### 下载-安装-配置OpenVPN软件

[Community Downloads | OpenVPN](https://openvpn.net/community-downloads/)

<img src="https://raw.githubusercontent.com/ld269440877/images/master/vultr-centos7X64-build-vpn/openvpn配置.png" alt="openvpn配置"  title="openvpn配置" width="600" height="">


# 第二种VPN方案：利用Docker一键安装Shadowsocks(影梭)搭建VPN

## 第一步：服务器的部署

1. 进入Vultr首页-Products-右侧加号Deploy New Server
2. Deploy New Instance
- Choose Server-Cloud Compute
- Server Location-All Location-Tokyo(在上海日本和迈阿密网速可以其他的有点慢)
- Server Type-64 bit OS - CentOS 7 x64
- Server Size-$5/month
- Deploy Now
- 服务器安装
- Server Information
<img src="https://raw.githubusercontent.com/ld269440877/images/master/vultr-centos7X64-build-vpn/ServerType64bitOS-CentOS7x64.png" alt="ServerType64bitOS-CentOS7x64"  title="ServerType64bitOS-CentOS7x64" width="600" height="">

> 注：Server安装版本CentOS 7 x64，如果是其他版本安装Docker会报错`Failed to start docker.service: Unit docker.service not found.`

<img src="https://raw.githubusercontent.com/ld269440877/images/master/vultr-centos7X64-build-vpn/ServerType-64bitOS-ServerInformation.png" alt="ServerType-64bitOS-ServerInformation"  title="ServerType-64bitOS-ServerInformation" width="600" height="">

## 第二步：VPS的设置以及VPN的搭建－影梭

- 使用SSH工具设置VPS
1. 下载Xshell (可以从网上找链接下载 这个软件，我是从这个网页下载的。<http://www.onlinedown.net/soft/36383.htm>)
2. 打开Xshell在新建会话窗口填写相关信息，
`名称：`可以自定义
`IP：` 填入上第一部分显示的主机（IP Adress），
`端口：`22 默认即可
不用点确定，接下来进行下一步-用户身份的设置。
3. 点击用户身份验证，方法选择Password，填写服务器的用户名和密码
<img src="https://raw.githubusercontent.com/ld269440877/images/master/vultr-centos7X64-build-vpn/XShell设置.png" alt="XShell设置"  title="XShell设置" width="600" height="">

## 第三步：开始VPN的搭建

1. 安装Docker `[root@vultr ~]# yum install docker -y`
2. 启动DOcker `[root@vultr ~]# service docker start`
3. 开启系统服务`[root@vultr ~]# chkconfig docker on`
4. 检查Docker 状态`[root@vultr ~]# docker version`
5. 安装 Shadowsocks 的 VPN Docker 镜像`[root@vultr ~]# docker pull oddrationale/docker-shadowsocks`
6. 运行镜像`[root@vultr ~]# docker run -d -p 2020:2020 oddrationale/docker-shadowsocks -s 0.0.0.0 -p 2020 -k Aa2020 -m aes-256-cfb`
7. 查看容器信息`[root@vultr ~]# docker ps -a`
8. 添加Docker服务到系统自启动`[root@vultr ~]# systemctl enable docker`
9. 安装lrzsz使用rz、sz命令进行Windows-Linux文件互传receive - send zmodem协议`[root@vultr ~]# sudo yum -y install lrzsz`

- 本安装并配置shadowsocks DockerBuildVPN shell脚
```sh
echo "使用rz、sz命令进行文件互传receive - send zmodem协议"
#sudo yum -y install lrzsz
echo "安装Docker"
yum install docker -y
echo "启动Docker"
service docker start
echo "chkconfig docker on"
chkconfig docker on
echo "查看Docker版本"
docker version
echo "安装 Shadowsocks 的 VPN Docker 镜像"
docker pull oddrationale/docker-shadowsocks
echo "创建VPN"
docker run -d -p 2020:2020 oddrationale/docker-shadowsocks -s 0.0.0.0 -p 2020 -k Aa2020 -m aes-256-cfb
echo "查看docker下进程运行状态"
docker ps -a
```
- `chmod +x DockerBuildVPN`
- `./DockerBuildVPN`

> 只需要修改端口和密码，其他默认即可。
`-p` 端口这里要前后一致，比如2020:2020 2020
`-k` 后面设置你的 VPN 的密码，比如：Aa2020
检查运行; 到这一步基本上就完成了，接下来就开始连接了。

## 第四步：使用SHADOWSOCKS进行连接

1. 下载Shadow Socks软件<https://github.com/shadowsocks>
2. 2.打开软件，填写刚创建势力Server Information的信息
- 服务器地址（填写Your Server IP）`167.179.92.73`
- 端口号(填写Your Server Port)`2020`
- 密码(填写Your Password)`Aa2020`
- 加密方式(填写Your Encryption Method)`aes-256-cfb`
- 代理端口(填写Your Local Port)`1080`
<img src="https://raw.githubusercontent.com/ld269440877/images/master/vultr-centos7X64-build-vpn/Shadowsocks配置.png" alt="Shadowsocks配置"  title="Shadowsocks配置" width="600" height="">
