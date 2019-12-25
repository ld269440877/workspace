
[阿里云用户中心续费管理查看公网内网IP](https://usercenter2.aliyun.com/renew/manual?spm=5176.12825654.amxosvpfn.28.d2172c4aW8KZwk&aly_as=6jV7Q3Uv)

产品|	实例ID/实例名称|	地域|	公网/内网IP|	倒计时|	付费方式|	开始/结束时间|
-|-|-|-|-|-|-|
云服务器|i-uf6ioqjurm7292xyaw36<br/>iZuf6ioqjurm7292xyaw36Z|华东2（上海）|47.101.189.146<br/>172.19.106.237|1053天|包年包月	|2022-11-12 00:00:00|

# 搭建图床

## PicGo + GitHub 搭建个人图床工具

[PicGo + GitHub 搭建个人图床工具_魔法学徒-CSDN博客](https://blog.csdn.net/yefcion/article/details/88412025)

1. GitHub 仓库设置
> 流程：新建 public 仓库 -> 创建 token -> 复制 token 备用

1.1 新建仓库
点击 git 主页右上角的 + 创建 New repository；
填写仓库信息，例如我就创建了一个images 的仓库
仓库设置为 Public 通过客户端外部访问
![](https://raw.githubusercontent.com/ld269440877/images/master/阿里云服务器/新建images公开仓库.png)

1.2 创建 token 并复制保存
此时images仓库已经建立，点击右上角头像，然后进入设置；
![](https://raw.githubusercontent.com/ld269440877/images/master/阿里云服务器/github-setting.png)
在页面最下找到 Developer settings，点击进入；
![](https://raw.githubusercontent.com/ld269440877/images/master/阿里云服务器/github-setting-DeveloperSettings.png)
创建 token；
![](https://raw.githubusercontent.com/ld269440877/images/master/阿里云服务器/创建token.png)
填 description（也是随心填），勾选复选框 repo ，接着到页面底部 Generate token 就完成了；
![](https://raw.githubusercontent.com/ld269440877/images/master/阿里云服务器/填写描述勾选repo.png)
然后复制生成一串字符 token，这个 token 只出现一次，所以要保存一下（我一般记在微信收藏）
![](https://raw.githubusercontent.com/ld269440877/images/master/阿里云服务器/PicGoGithubToken.png)
PicGoGithubToken：`c7c00444f6e2b14688072da91eb6d1249703e17b`

2. PicGo 客户端配置

2.1 下载&安装
[PicGo](https://github.com/Molunerfinn/PicGo/releases/tag/v2.1.2)

2.2 配置
![](https://raw.githubusercontent.com/ld269440877/images/master/阿里云服务器/PicGo客户端配置.png)
- 仓库名 即你的仓库名
- 分支名 默认 master
- Token 就是刚刚复制的那一串字符
- 存储路径 这个可以填也可以不填，填了的话图片就上传到 git 中 data 这个文件夹
- 域名 https://raw.githubusercontent.com/yefcion/cloudimg/master这个要改一下 格式 https://raw.githubusercontent.com/[username]/[仓库名]/master
我的设定自定义域名`https://raw.githubusercontent.com/ld269440877/images/master`

然后点确定就可以了。

- 关于上传的快捷键设置。默认的是 MacOrWindows: CommandOrContral+Shift+P, 在VS Code中不影响使用
- 关闭更新助手：关
- 开机启动：开
- 上传前重命名：开
- 开启上传提示：开

3. VS Code中使用
- 复制图片到剪切板
- `Contral+Shift+P`
- 剪切板中的图片上传前重命名
- `Ctrl+C`粘贴Markdown格式的图片github链接

## PicGo + 阿里云 OSS 搭建图床

 > 有免费的PicGo + GitHub也没什么隐私就没用这个付费的

阿里云对象存储服务（Object Storage Service，简称 OSS）为您提供基于网络的数据存取服务。使用 OSS，您可以通过网络随时存储和调用包括文本、图片、音频和视频等在内的各种非结构化数据文件。

[致小白:从0开始搭建自己的阿里云OSS图床 - 掘金](https://juejin.im/post/5d9c4c1bf265da5b5d2047a2#heading-0)

使用阿里云管理控制台来完成OSS基本操作的流程如下：
![](https://raw.githubusercontent.com/ld269440877/images/master/阿里云服务器/OSS基本操作的流程.png)

# VS Code 批量修改Markdown图片引用格式

使用VSCode进行查找、替换时，经常需要用到正则表达式，一段时间不用就忘了，每次要用的时候都要耽误很多时间去查找，所以整理了一份很全的放在这里。这个其实是.NET使用的正则表达式，VSCode也是一样的，微软系的产品（比如Visual Studio等）应该都是使用这个标准的。

VS Code替换快捷键`Ctrl+H`
- 查找无图片描述 ![]：`![](`
替换：`![](https://raw.githubusercontent.com/ld269440877/images/master/MarkdownNotebook/`

- 查找 ![有图片描述]：`](`   要主要网站与图片引用方式的相似性，区别只在于有无`!`
替换：`![](https://raw.githubusercontent.com/ld269440877/images/master/MarkdownNotebook/`

![vscode正则替换使用样式](https://raw.githubusercontent.com/ld269440877/images/master/阿里云服务器/vscode正则替换使用样式.png "vscode正则替换使用样式")

> 参考链接
[VSCode查找和替换正则表达式转义字符整理 | 胡刘郏的技术博客](https://www.huliujia.com/blog/a2c7dc8ec28aa650df1ff43c580785decdeba8bc/)
[完整内容请参照微软官方文档Regular Expression Language - Quick Reference | Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)

> 注意事项
在VSCode中使用时，要先把通配符开关打开（开关是查找输入框右边的”.*“符号）

转义字符|	匹配内容|
-|-|
\t|	tab
\r|	回车符号\r
\n|	换行符号\n
\uxxxx|	匹配Unicode编码为xxx的字符,如\u0020匹配空格，这个符号可以用来帮助匹配中文，后面说
`\`|	特殊符号转义，如”\*” ，转义后匹配的是字符”*“， “\(” 匹配的是括号”(”
[字符序列]|	匹配[ ]中的任意字符，如[ae]，字符a和字符e均匹配
[^字符序列]|	匹配不在[ ]中的任意字符，如[^ae]除了a和e，其他字符都匹配
[字符1-字符2]|	匹配在[ ]之间的任意字符，如[a-x]，就是匹配a和x之间的所有字符（包括a和x）
.|	匹配任意单个字符(除了\n)
\w|	匹配所有单词字符（如”a”，”3”，”E”，但不匹配”?“，”.“等）
\W|	和\w相反，匹配所有非单词字符
[\u4e00-\u9fa5]|	利用区间和\u转义符号，匹配中文（该区间包含2万个汉字），可以当做中文版的\w使用
\s|	匹配空格
\S|	和\s相反，匹配非空格
\d	|匹配数字字符，如”1”，”4”，”9”等
\D|	和\d相反，匹配除了数字字符外的其他字符
*|	将前面的元素匹配0到多次，如”\d*.\d”，可以匹配”19.9”，”.0”,“129.9”
+|	将前面的元素匹配1到多次，如”be+“，可以匹配”be”， “beeeeee”
？|	将前面的元素匹配0次或者一次，如”rai?n” 可以且只可以匹配 “ran” 或者 “rain”
{n}|	n是个数字，将前面的元素匹配n次，如”be{3}“可以且只可以匹配 ”beee”
{n, m}|	将前面的元素匹配至少n次，最多m次，如”be{1,3}” 可以且只可以匹配”be”,“bee”, “beee”
`|`|	相当于”或”,表示匹配由|分割的任意一个元素，如the(e| is | at)，可以匹配”the”, “this”, “that”
$n|	n是个数字，这个是替换时使用括号（ ）将匹配的patter分割成了几个元素，然后在替换的patter里面使用，类似于变量。<br>如果查找patter是”(\w+)(\s)(\w+)“,那么$1就是(\w+),$2是(\s),$3是(\w+)，替换patter是$3$2$1,那么替换结果就是(\w+)(\s)(\w+)。<br>假设匹配到的是”one two”，那么$1,$2,$3分别为”one”, “ “, “two”，替换后的结果为”two one”.
