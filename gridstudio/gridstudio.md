# gridstudio

[统一了Excel和Python的神级编辑器GridStudio](https://blog.csdn.net/liyue071714118/article/details/100996146)

## 安装前电脑配置

1. 首先检查电脑的虚拟化开启了没有：进入任务管理器（ctrl+alt+delete），点击性能->CPU ,查看虚拟化是否已启用，如果虚拟化是已禁用，那么你需要重启电脑进入BIOS开启虚拟化（我的笔记本CPU是支持虚拟化的，重启时进入bios按esc -> 再按f12 -> 去开启虚拟化）
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200218134735.png" alt="20200218134735"  title="" width="600" height="" /><figcaption><font color=green></font></figcaption></center></figure>

2. 然后再是进入电脑的控制面板->程序->启用或关闭Windows功能->把Hyper-v勾上，启用后电脑会重启，后面就可以安装Docker for Windows了
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200218134819.png" alt="20200218134819"  title="" width="600" height="" /><figcaption><font color=green></font></figcaption></center></figure>

## 下载Docker

接着需要[下载Docker for Windows](https://www.docker.com/products/docker-desktop)
注意：如果你是第一次在官网下载，需要先在Docker官网注册一个账号，注册过程中会通过邮箱给你发一个校验链接，点击链接即可登录下载。

## 安装Docker

Docker安装很简单，直接双击安装包，一路 Next，点击 Finish 完成安装，不需要手动配置。安装完成后会在桌面出现Docker的图标和提示重新启动电脑。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200218134905.png" alt="20200218134905"  title="" width="600" height="" /><figcaption><font color=green></font></figcaption></center></figure>

重启后，电脑右下角会出现Docker的任务图标，打开CMD命令窗口输入`docker --version`查看安装版本
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200218134943.png" alt="20200218134943"  title="" width="600" height="" /><figcaption><font color=green></font></figcaption></center></figure>

这样Docker就安装成功了。
根据Grid Studio给的安装提示，我们需要配置Docker的磁盘共享。
我们之前已经把Grid Studio下载到C盘的根目录，那么我们就直接共享C盘即可。如下图：
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200218135021.png" alt="20200218135021"  title="" width="600" height="" /><figcaption><font color=green></font></figcaption></center></figure>
点击Apply，如果你是域用户，会提示你输入电脑的账号密码。
然后重启一下电脑即可。
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200218135057.png" alt="20200218135057"  title="" width="600" height="" /><figcaption><font color=green></font></figcaption></center></figure>

## 安装Git  Bash

根据Grid Studio的提示，我们需要[下载安装git bash](https://gitforwindows.org/)
Git的安装很简单，一路Next即可，不需要额外配置，安装完桌面会出现一个图标。

## 下载Grid Studio

[Grid Studio的下载](https://github.com/ricklamers/gridstudio)
> 注意：将项目放在C盘根目录下，文件名小写字母命名。
[项目给的安装提示](https://github.com/ricklamers/gridstudio/wiki/Installation)
在本地安装Grid Studio非常简单：
1. Clone the repository with this command:
`git clone https://github.com/ricklamers/gridstudio`
2. Run the bash script (on Windows use e.g. Git Bash) with this command:
`cd /c/gridstudio && ./run.sh`
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200218135201.png" alt="20200218135201"  title="" width="600" height="" /><figcaption><font color=green></font></figcaption></center></figure>
直到提示完成，并且给出访问地址：http://127.0.0.1:8080即表示编译成功。
3. Go to `http://127.0.0.1:8080` in your browser. Note! Username: admin password: admin

> 注意：如果你成功运行过一次，下次重启电脑登录不需要编译，但还是需要从run.sh进入。而且在进入前还需要先执行destroy.sh
> 这个命令行界面最好一直开启

## 可能遇到的问题

刚开始编译的时候，可能会遇到如下问题：
### daemon is not running
<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200218135327.png" alt="20200218135327"  title="" width="600" height="" /><figcaption><font color=green></font></figcaption></center></figure>

> 解决办法：
> 关闭防火墙，关闭360安全卫士，重启电脑！！！

### 端口占用查询及释放被占用端口 命令

我的是wechat占用8080端口，杀掉wechat进程即可
假设查看443端口占用情况：

打开cmd：win+s，输入cmd + 回车
根据端口找到PID：
`netstat -aon|findstr "443"`
TCP 0.0.0.0:443 0.0.0.0:0 LISTENING 12380
根据PID找到程序名：
`tasklist|findstr "12380"`
杀死进程：
`taskkill /PID 12380`
完成

### login gridstudio网页无法正常运作disk I/O error

<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200218140338.png" alt="20200218140338"  title="" width="600" height="" /><figcaption><font color=green></font></figcaption></center></figure>

<figure><center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200218140530.png" alt="20200218140530"  title="" width="600" height="" /><figcaption><font color=green></font></figcaption></center></figure>