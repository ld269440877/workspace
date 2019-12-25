# 系统安装

## 工具/原料

- [Ubuntu官网](cn.ubuntu.com/)
- U盘安装Ubuntu 16.04 教程（安装全过程，不包含下载）
- ubuntu-16.04-desktop-amd64.iso
- 制作启动盘

<rufus-3.1.exe>
![rufus-31](https://raw.githubusercontent.com/ld269440877/images/master/ubuntu1804_configure/rufus-31.png "rufus-31")

## grub rescue模式下修复分区缺失问题

[grub rescue模式下修复分区缺失问题 - 知乎](https://zhuanlan.zhihu.com/p/31996206)
安装完Ubuntu16-18,重启登录系统显示:

- error: no such partition.（没有这个分区）
- Entering rescue mode...

1. Ctrl+Alt+Delete退出重启
2. 插入之前安装Ubuntu所使用的live-USB，F12进入BIOS，选择USB引导Ubuntu，选择==试用Ubuntu==
3. 联网
4. 终端输入:

```bash {class='line-numbers'}
sudo add-apt-repository ppa:yannubuntu/boot-repair && sudo apt-get update
sudo apt-get install -y boot-repair && boot-repair
```

1. 得到引导修复框，选择推荐修复（修复常见问题）
2. 修复成功重启计算机，拔下优盘

# Software & Updates 配置

## 更新源

- 找到Software & Updates，将源更新为阿里云的源
    Download from:<http://mirros.aliyun.com/ubuntu>
- 在Other Software里将Canonical Partners勾上
- 手动更新

```bash
sudo apt update
sudo apt upgrade
```

## 软件安装与卸载

```bash
'root'
su -

'删除已安装的软件包（保留配置文件），不会删除依赖软件包，且保留配置文件。'
sudo apt-get remove

'删除已安装包（不保留配置文件)。
如软件包a，依赖软件包b，则执行该命令会删除a，而且不保留配置文件'
sudo apt-get purge
or
sudo apt-get --purge remove

'删除为了满足依赖而安装的，但现在不再需要的软件包（包括已安装包），保留配置文件。'
sudo apt-get autoremove

'APT的底层包是dpkg, 而dpkg 安装Package时, 会将 *.deb 放在 /var/cache/apt/archives/中，apt-get autoclean 只会删除 /var/cache/apt/archives/ 已经过期的deb。'
sudo apt-get autoclean

'使用 apt-get clean 会将 /var/cache/apt/archives/ 的 所有 deb 删掉，可以理解为 rm /var/cache/apt/archives/*.deb。'
sudo apt-get clean
```

# 系统备份

## Ubuntu 备份和恢复系统

[Ubuntu14.04如何备份和恢复系统 - 小毅哥哥Bob - 博客园](https://www.cnblogs.com/Thinker-Bob/articles/10478228.html)
[ubuntu16.04备份和恢复系统 - 人生苦短，我用golang - CSDN博客](https://blog.csdn.net/Lazybones_3/article/details/85124913)

### 备份系统

在备份系统前，请保证系统是无错和干净的
先清空回收站，软件升级到最新

```bash
# 清空回收站
"empty trash"

# 软件升级到最新
sudo apt update
sudo apt upgrade
```

Ubuntu系统与Windows系统所采用的文件系统不同， Ubuntu系统在使用或更新过程中不会产生文件碎片和垃圾文件，所以在使用 Ubuntu系统中不用考虑清理系统的文件垃圾和整理文件碎片。
如果你确实想去清理一下Ubuntu系统的话，那么请你参照下述方法去做吧：

```bash
# 1、按“Ctrl+Alt+T”，调出终端。
# 2、在终端输入下面的命令（复制到终端窗口即可）——按回车键——输入帐户密码——按回车键。
sudo apt-get autoclean（清理旧版本的软件缓存）
sudo apt-get clean（清理所有软件缓存）
sudo apt-get autoremove（删除系统不再使用的孤立软件）
```

```bash
# root 设置密码
sudo passwd root

# 切换root权限并进入根目录
su -

# 到根目录
cd /

# 新建restore文件夹来保存备份文件
mkdir restore
# 备份系统

tar cvpzf /restore/Ubuntu.tgz --exclude=/proc --exclude=/lost+found --exclude=/Ubuntu.tgz --exclude=/mnt --exclude=/media --exclude=/sys --exclude=/restore /

# Bzip2比gzip的压缩率高，但是速度慢一些。
# 如果压缩率对你来说很重要，那么你应该使用Bzip2，用“j”代替命令中的“z”，并且给档案文件一个正确的扩展名“bz2”
# tar cvpjf /restore/Ubuntu.tar.bz2 –exclude=/proc –exclude=/lost+found –exclude=/Ubuntu.tar.bz2 –exclude=/mnt –exclude=/sys /
"注：出现”tar: 由于前次错误，将以上次的错误状态退出“，可以忽略"

'''
'tar' 是用来备份的程序
c - 新建一个备份文档
v - 详细模式， tar程序将在屏幕上实时输出所有信息。
p - 保存许可，并应用到所有文件。
z - 采用‘gzip’压缩备份文件，以减小备份文件体积。
f - 说明备份文件存放的路径， Ubuntu.tgz 是本例子中备份文件名。
“/”是我们要备份的目录，在这里是整个文件系统。
'''
```

### 恢复系统

```bash
"切换到root用户，并把文件“Ubuntu.tgz”拷贝到分区的根目录下。"
# 切换root用户执行恢复命令

su root
tar xvpfz Ubuntu.tgz -C /

# 如果你的档案文件是使用Bzip2压缩的，应该用：
# tar xvpfj Ubuntu.tar.bz2 -C /

'''
注意：上面的命令会用档案文件中的文件覆盖分区上的所有文件。
参数x是告诉tar程序解压缩备份文件。 -C 参数是指定tar程序解压缩到的目录。( 在本例中是/ ），这会花一段时间。只需确保在你做其他任何事情之前，重新创建你剔除的目录： ( /proc, /lost+found, /mnt, /sys, 等等。)
'''
# 重建没备份的目录
mkdir /proc /lost+found /mnt /sys

# mkdir proc
# mkdir lost+found
# mkdir mnt
# mkdir media
# mkdir sys
```

执行恢复命令之前请再确认一下你所键入的命令是不是你想要的，执行恢复命令可能需要一段不短的时间。触类旁通，熟练以上操作后，对用户和部分升级文件进行定期备份，可以节省大量时间和提高安全性。

## Time Shift 系统备份

```python {class= ' line-numbers'}
sudo apt-add-repository -y ppa:teejee2008/ppa
sudo apt-get update
sudo apt-get install timeshift
```

# 搜狗拼音
---
[(Back to Top)](#系统安装)

[原文链接](https://blog.csdn.net/hymanjack/article/details/80285400)

## 终端执行下列命令

```bash
sudo apt-get install fcitx-bin      #安装fcitx-bin
sudo apt-get update --fix-missing   #修复fcitx-bin安装失败的情况
sudo apt-get install fcitx-bin      #重新安装fcitx-bin
sudo apt-get install fcitx-table    #安装fcitx-table
```

## 搜狗输入法Linux官网下载64bit的程序

```bash
sudo dpkg -i sogoupinyin*.deb       #安装搜狗拼音
sudo apt-get install -f             #修复搜狗拼音安装的错误
sudo dpkg -i sogoupinyin*.deb       #重新安装搜狗拼音
```

重启！重启！重启！重要的事情说三遍！

1. 找到Fcitx Configure，点击进入

![FictxConfigure](https://raw.githubusercontent.com/ld269440877/images/master/ubuntu1804_configure/https://raw.githubusercontent.com/ld269440877/images/master/ubuntu1804_configure/FictxConfigure.png)
![FictxConfigure1](https://raw.githubusercontent.com/ld269440877/images/master/ubuntu1804_configure/FictxConfigure1.png)
![FictxConfigure2](https://raw.githubusercontent.com/ld269440877/images/master/ubuntu1804_configure/FictxConfigure2.png)

# electron-ssr

[electron-ssr-backup/Ubuntu.md at master · qingshuisiyuan/electron-ssr-backup](https://github.com/qingshuisiyuan/electron-ssr-backup/blob/master/Ubuntu.md?1569587463052)

## 安装依赖

```bash
sudo apt install libcanberra-gtk-module libcanberra-gtk3-module gconf2 gconf-service libappindicator1
```

## 可选依赖

```bash {class='line-numbers'}
sudo apt-get install libssl-dev
sudo apt-get install libsodium-dev
"如果软件报错，请安装可选依赖"
```

##  安装软件

`sudo dpkg -i *.deb`

## 系统需要安装Python2.7 否则可以正常运行但不能翻墙

`sudo apt install python`

## 系统设置

系统设置-网络设置-网络代理设置
![alt 系统网络代理设置](https://raw.githubusercontent.com/ld269440877/images/master/ubuntu1804_configure/系统网络代理设置.png)

```bash
"自动"
http://127.0.0.1:2333/proxy.pac
```

## Google browser 设置

使用系统配置

# 百度网盘客户端

[百度网盘 客户端下载](http://pan.baidu.com/download)

# Anaconda+vscode

---

[(Back to Top)](#系统安装)

[Index of /anaconda/archive/ | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)

## Anaconda 安装

[Anaconda | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirror.tuna.tsinghua.edu.cn/help/anaconda/)

### jupyter设置工作目录

#### 配置jupyter工作目录（ubuntu）

```bash
jupyter-notebook --generate-config
```

#### 创建配置文件

打开/home/.jupyter 文件，找到jupyter_notebook_config.py并打开以“.”开头的文件是ubuntu隐藏文件，按 Ctrl+h 显示隐藏文件，​在文档中添加如下命令保存：

```bash
c.NotebookApp.notebook_dir = 'working directory'
```

### Jupyter notebook extensions 扩展插件的安装

```bash {class='line-numbers'}
python -m pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user --skip-running-check
"hinterland是代码提示插件"
```

## git配置

[Ubuntu 18.04下GitHub和Git的安装配置入门教程_Linux教程_Linux公社-Linux系统门户网站](https://www.linuxidc.com/Linux/2018-05/152611.htm)

### 使用命令apt-get来安装

```bash
sudo apt install git
```

### 配置用户名密码

```bash
git config --global user.name "ld269440877"
git config --global user.email "aa269440877@outlook.com"
git config --list

# user.name=ld269440877
# user.email=aa269440877@outlook.com

"此时，Home目录下会新建一个.gitconfig文件"
```

### GitHub添加SSH Keys

#### 生成Keys

```bash
ssh-keygen -t rsa -C "aa269440877@outlook.com"
"系统会提示key的保存位置（一般是~/.ssh目录）和指定口令，保持默认，连续三次回车即可"
```

#### 复制SSH Key到GITHUB

```bash
"打开该文件，id_rsa.pub文件内的内容，粘帖到github帐号管理的添加SSH key界面中"
cat ~/.ssh/id_rsa.pub
# Hi ld269440877! You've successfully authenticated, but GitHub does not provide shell access.
```

#### 添加key

登录github-> Settings-> SSH and GPG Keys-> New SSH key添加

#### 测试是否连接成功

`ssh -T git@github.com`

### 添加本地与远程仓库链接

```bash
'…or create a new repository on the command line'
echo "# vscode" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:ld269440877/vscode.git
git push -u origin master

'…or push an existing repository from the command line'
git remote add origin git@github.com:ld269440877/vscode.git
git push -u origin master

```
## Git使用
[Git使用教程笔记 | Michael翔](https://michael728.github.io/2018/11/24/git-advance/)


## GitHub使用

### 搜热门：GitHub Trend 和 GitHub Topic

[GitHub Trend](https://github.com/trending)
:   页面总结了每天/每周/每月周期的热门 Repositories 和 Developers，你可以看到在某个周期处于热门状态的开发项目和开发者。

[GitHub Topic](https://github.com/topics)
:   展示了最新和最流行的讨论主题，在这里你不仅能够看到开发项目，还能看到更多非开发技术的讨论主题，比如 Job、Chrome 浏览器等

### 搜开发者

（注：GitHub 官方还支持很多搜索条件，在 [About searching on GitHub - GitHub Help](https://help.github.com/en/articles/about-searching-on-github)可以查看官方出品的搜索技巧。）

| Github搜索-找开发者 | 搜索时设置 location 为 China，language 为 javascript，整个搜索条件：language:javascript location:china |
|---------------------|---------------------------------------------------------------------------------------------------|
| 搜索条件            | 备注                                                                                                |
| location:           | location:china,匹配用户填写的地址在china                                                            |
| language:           | language:javascript,匹配开发语言为javascript的开发者                                                |
| in:fullname         | jack in:fullname,匹配用户实名为jack的开发者                                                         |
### 搜项目

先用某些关键词搜索，得到的搜索结果优先展示一些现成的软件和工具

| Github搜索-找项目 | Awesome windows                       |
|:-----------------:|:--------------------------------------|
|     搜索条件      | 备注                                  |
|  Awesome+关键字   | 关键字Awesome,帮助找到优秀的工具列表  |
|      stars:       | stars:>=500,匹配收藏数量超过500的项目 |
|     language:     | 匹配javascript为开发语言的项目        |
|      forks:       | forks:>=500,匹配分支数量超过500的项目 |

### 设置搜索条件

stars:、language:、forks:，其实就是设置项目收藏、开发语言派生的搜索条件
- 如果觉得记住这些搜索条件略显繁琐的话，使用 GitHub 提供的高级搜索功能[GitHub · Where software is built](https://github.com/search/advanced)，同样可用自定义条件进行搜索
- 参考官方给出的帮助指南 [Searching on GitHub](https://help.github.com/en/articles/searching-on-github) ，里面有更多关于项目、代码、评论、问题等搜索技巧

[free-programming-books](https://github.com/vhf/free-programming-books)：整理了所有和编程相关的免费书籍，同时也有 [中文版项目](https://github.com/vhf/free-programming-books/blob/master/free-programming-books-zh.md)。
[github-cheat-sheet](https://github.com/tiimgreen/github-cheat-sheet/)：集合了使用 GitHub 的各种技巧。
[android-open-project](https://github.com/Trinea/android-open-project)：涵盖 Android 开发的优秀开源项目。
[chinese-independent-developer](https://github.com/1c7/chinese-independent-developer)：聚合所有中国独立开发者的项目

## vscode配置

[超实用VS Code插件推荐——不定期更新！ - 蚂蚁的博客 - CSDN博客](https://blog.csdn.net/qq_41139830/article/details/85221330)

> 在VScode 从EXTENSIONS:MARKETPLACE上查看插件使用方法

### setting-sync

[vscode使用setting-sync插件同步设置 - 掘金](https://juejin.im/post/5cd933e5e51d456e39631997)
[超实用VS Code插件推荐——不定期更新！ - 蚂蚁的博客 - CSDN博客](https://blog.csdn.net/qq_41139830/article/details/85221330)
[Visual Studio Code（VS code）你们都在用吗？或许你们需要看一下这篇博文 - Dawnzhang - 博客园](https://www.cnblogs.com/clwydjgs/p/10078065.html)

#### vscode插件中心安装 setting-sync
#### Gists
    > github.com/settings/Developer settings/Generate new token
        - 填写Note what is this token for？
        - Select scopes---勾选 gist
        - Generate token
            一定要复制生成的token  保存好 下一次进入这个网页就看不到token 了
            一定要复制生成的token  保存好
            一定要复制生成的token  保存好
    > github.com/Your Gists
    > 右上角加号（+），新建gists
![GenerateGist](https://raw.githubusercontent.com/ld269440877/images/master/ubuntu1804_configure/GenerateGist1.png "GenerateGist")
![(GistId](https://raw.githubusercontent.com/ld269440877/images/master/ubuntu1804_configure/GistId.png "GistId")

#### 重置所有sync settings配置
- Ctrl + Shift + P 开启命令面板，找到同步命令，选择 Reset Extension Settings 重置所有配置
- 在通过 Alt + Shift + U 重新填写 token 进行同步
- sync settings 界面点击：login with github

windows10-20191013:
Gist token:d4dd325d5d30726d9eb4f0a16a7d3011726c6861
Gist Id   : 839a1a78984d838fa1d81bfa193ca6ae

ubuntu18_vscode_20190930
:   Gist token: a46643712552e6b247745d5a5d9894c5d4ffaae5
    Gist Id   : e054c9b617c8c2d2d8899f1ad46ba710
3. 回到vscode，在任意界面按 Alt + Shift + U，在对话框中输出刚才复制的 token
4. 再次按 Alt + Shift + U 完成配置上传，使用组合键 Alt + Shift + D 即可下载配置
5. 如若出现 token 配置无问题却出现报错无法上传配置时，可按 Ctrl + Shift + P 开启命令面板，找到同步命令，选择 Reset Extension Settings 重置所有配置，在通过 Alt + Shift + U 重新填写 token 进行同步

//TODO 的方法 1

#TODO 的方法 2
- [ ] TODO 的方法 3 待做事项

#### 外观

- [x] Darula Theme 主题
- [x] vscode-icons 图标

## Markdown

- [x] Markdown Preview Enhanced: 增加markdown文件的预览功能，可以实时查看效果
- [x] Markdown All in One: markdown语法的快捷方式
- [x] markdownlint
- [x] Markdown Extension Pack
- [x] :emojisense: 快速挑选 Markdown 中的 Emoji。
- [x] Markdown Table Maker :Ctrl+shift+p-->table maker-->对齐方式-->行数
- [x] Paste Image : Ctrl+ alt + V

<ruby>n p m<rp>(</rp><rt>Node 包管理器</rt><rp>)</rp></ruby>
<font color="RGB255">orange</font>
## 代码检查

- [x] code spell checker
- [x] guides 高亮缩进基准线 参考线，可自定义
- [ ] Indent-Rainbow :A simple extension to make indentation more readable
- [x] [CodeLf](https://unbug.github.io/codelf/#%E4%BB%A3%E7%A0%81)是一个用来给变量命名的网站，你只要输入你想起的中文名，它就会给你提供很多建议的命名
- [ ] Syntax Highlighter for VSCode
- [x] Trailing Spaces :press F1 and select/type "Trailing Spaces: Delete"
- [ ] Turbo Console Log快捷添加 console.log，一键 注释 / 启用 / 删除 所有 console.log

> 简单说下这个插件要用到的快捷键:
ctrl + alt + l 选中变量之后，使用这个快捷键生成 console.log
alt + shift + c 注释所有 console.log
alt + shift + u 启用所有 console.log
alt + shift + d 删除所有 console.log

- [ ] LeetCode
- [ ] change-case 转换变量命名风格

## 自动补全

- TabNine配置
- [x] Path Intellisense ：自动提示补全路径
- [x] Auto Close Tag ：自动闭合 html 等标签 （</...>）
- Auto Rename Tag ：修改 html 标签时，自动修改闭合标签

## 代码片段

[VS Code跟我一起在Visual Studio Code 添加自定义snippet（代码段），附详细配置 - 前端 - 掘金](https://juejin.im/entry/5aebc727f265da0b9526f54e)

- snippets ：搭建可以自己安装各种代码片段
![UserSnippets](https://raw.githubusercontent.com/ld269440877/images/master/ubuntu1804_configure/UserSnippets.png "UserSnippets")
![NewGlobalSnippets](https://raw.githubusercontent.com/ld269440877/images/master/ubuntu1804_configure/NewGlobalSnippets.png "NewGlobalSnippets")

## 功能扩展
- [x] Todo Tree :Show TODO, FIXME, etc. comment tags in a tree view
- [x] Bracket Pair Colorizer ：让代码的各种括号呈现不同的颜色
- [x] Code Runner ：可以在编辑器里直接运行代码，查看结果
- [x] Color Picker ：可以直接在编辑器里打开色板，选择各种模式的颜色
- [x]  Guides：An extension for more guide lines
- [x] better comments
- [x] bookmarks 添加行书签
- [ ] Document This ：可以给函数、类等自动的加上详细的注释
- [ ] Regex Previewer 实时预览正则表达式的效果
- [x] RegExp Preview and Editor ：正则可视化解析匹配过程
- [x] any-rule :快速查看且引用常用的正则,很实用,F1->输入关键字字母
## Git 
- [ ] Git History ：方便的查看git版本管理的详细信息
- [ ] GitLens 详细的 Git 提交日志。Git 重度使用者必备，尤其是多人协作时：哪一行代码，何时、何人提交都有记录
- [ ] Live Server ：可以一键在本地启动服务器



## Mysql
[使用 Visual Studio Code 链接 MySql 数据库并进行查询 - 台部落](https://www.twblogs.net/a/5b8cdc332b71771883364ab4/zh-cn)
- [x] MySQL
- [x] MySQL Syntax
`mysql -uroot -p123456`
>host: localhost
port: 3306
username: root
password: 123456

> vscode connect MySQL 8.0 - Client does not support authentication protocol requested by server; consider upgrading MySQL client
- Full Steps For MySQL 8
- Connect to MySQL
```mysql { class="line-numbers"}
$ mysql -u root -p

<!-- Enter password: (enter your root password)
Reset your password
(Replace your_new_password with the password you want to use) -->

mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_new_password';
mysql> FLUSH PRIVILEGES;
mysql> quit
```





# java installion & configure

---

[(Back to Top)](#系统安装)

[如何在Ubuntu 18.04上安装Java - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1162527)

## 执行以下命令安装OpenJDK：

```bash
sudo apt install default-jre
java -version
"此命令将安装Java运行时环境（JRE）。这将允许您运行几乎所有Java软件。"
```

## Java 编译和运行环境
除了JRE之外，您可能还需要Java Development Kit（JDK）才能编译和运行某些特定的基于Java的软件。要安装JDK，请执行以下命令，该命令还将安装JRE：

```bash
sudo apt install default-jdk
#通过检查Java编译器的javac版本，来验证是否已安装JDK ：
javac -version
```

## 管理Java

```bash
# 查看所有版本的Java
sudo update-alternatives --config java
# 设置JAVA_HOME环境变量
"复制安装路径,文本编辑器打开/etc/environment"
 sudo vim /etc/environment
'''
JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64/bin/java"
'''
source /etc/environment
#验证是否已设置环境变量：
echo $JAVA_HOME
```

# PlantUML安装

[安装PlantUML + Visual Studio Code（Ubuntu环境）](https://www.ted027.com/post/puml-ubu/)

## 需要以下内容

- Java JRE或JDK
- Graphviz

## 在Ubuntu上安装

   1. 安装Visual Studio代码
        `sudo apt -y install code`
    1. 安装Java
         `sudo apt -y install default-jre`
    2. 安装Graphviz
        `sudo apt -y install graphviz`
    3. 从Visual Studio Code扩展中PlantUML搜索并安装
    4. 导出图片
    Ctrl + Shift + P要打开命令面板，
    输入: plantuml: export current diagram

## PyCharm

[JetBrains PyCharm/IDEA 使用技巧总结 | Michael翔](https://michael728.github.io/2019/05/11/tools-dev-pycharm-idea/)



# Ubuntu Software

---

[(Back to Top)](#系统安装)

## Telegram

socks 127.0.0.1 端口1080

## Shutter

[Ubuntu 18.04中截图工具Shutter的编辑按钮不可用的解决办法 - Jaxu - 博客园](https://www.cnblogs.com/jaxu/archive/2018/08/30/9561992.html)
[Ubuntu18 安装截图工具 Shutter 并设置快捷键 - 程序员大本营](http://www.pianshen.com/article/320249796/)
[Ubuntu18.04 系统截图 and Shutter 设置快捷键](https://www.jianshu.com/p/b01c0c675203)
shutter设置快捷键不灵

## 系统自带截图功能

```sh
＃ 保存到图片文件夹
Print Screen  #截取整个桌面
Alt + Print Screen #截取选中的窗口
Shift + Print Screen #自由选区
＃复制到剪贴板
Ctrl + Print Screen  #整个桌面
Ctrl + Alt + Print Screen #选中的窗口

Ctrl + Shift + Print Screen #自由选区

```

# 命令行安装

---
[(Back to Top)](#系统安装)

## Vim

`apt-get install vim`

## Chrome

```bash {code_block=true class= ' line-numbers' }
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install libappindicator1 libindicator7
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get -f install
```

## openssh-server

`sudo apt-get install openssh-server`

## tree

```bash
"查看文件的树状目录结构，而且不同类型的文件夹和文件都用不同的颜色标记"
# 安装
sudo apt-get install tree
# 使用
tree
```

# [设置 ubuntu 开机启动软件](https://blog.csdn.net/vola9527/article/details/52799607)

1. 终端输入： `gnome-session-properties`

2. 弹出窗口为“ 启动应用程序首选项”
![alt "设置开机启动项" ](https://raw.githubusercontent.com/ld269440877/images/master/ubuntu1804_configure/设置开机启动项.png "设置开机启动项" )

3. 点击右侧添加

4. 输入描述和软件路径

5. 这里的软件路径在 /usr/local/bin/目录下，所以最终的命令栏输入的内容是：/usr/local/bin/electron-ssr  （以添加electron-ssr开机启动为例）

# 阅读器

---

- [分享|Linux 下的六款最佳 PDF 文档阅览器](https://linux.cn/article-7245-1.html) # Gnome桌面环境中是默认安装的Evince, :ok_hand:

[(Back to Top)](#系统安装)

- [Typora — a markdown editor, markdown reader.](https://typora.io/#linux)

```sh
# or run:
# sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
# add Typora's repository
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update
# install typora
sudo apt-get install typora
```

- [Ubuntu 18.04 LTS 安装WPS - 简书](https://www.jianshu.com/p/3407c18e1337)
```sh
字体缺失问题
下载当前目录下 wps_symbol_fonts.zip
创建目录：
sudo mkdir /usr/share/fonts/wps-office

将下载的字体复制到创建的目录：
sudo cp -r wps_symbol_fonts.zip /usr/share/fonts/wps-office

解压字体包：
sudo unzip wps_symbol_fonts.zip

解压后删除字体包：
sudo rm -r wps_symbol_fonts.zip
```
