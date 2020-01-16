
# HTMLNotebook

> 参考
[HTML 基础教程](https://www.w3school.com.cn/html/html_jianjie.asp)
[HTML在线测试-W3School TIY Editor](https://www.w3school.com.cn/tiy/t.asp?f=html_headers)
[在Markdown中嵌入youtube视频的写法](https://gist.github.com/aoxu/7783280#file-youtube-md)

[![点我-我是在线图片生成器tablesgenerator](https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116225405.png)](http://www.tablesgenerator.com/html_tables)

# HTML 简介

## 实例

```html
<html>
<body>

<h1>我的第一个标题</h1>

<p>我的第一个段落。</p>

</body>
</html>
```
## 什么是 HTML？

HTML 是用来<font color=red>描述网页的一种语言</font>。

- HTML 指的是超文本标记语言 (Hyper Text Markup Language)
- HTML <font color=orange>不是一种编程语言</font>，而是一种标记语言 (markup language)
- 标记语言是一套标记标签 (markup tag)
- HTML 使用标记标签来描述网页

## HTML 标签

HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

HTML 标签是由尖括号包围的关键词，比如 `<html>`
HTML 标签通常是成对出现的，比如 `<b>` 和 `</b>`
标签对中的第一个标签是开始标签，第二个标签是结束标签
开始和结束标签也被称为开放标签和闭合标签

## HTML 文档 = 网页

- HTML 文档描述网页
- HTML 文档包含 HTML 标签和纯文本
- HTML 文档也被称为网页

Web 浏览器的作用是读取 HTML 文档，并以网页的形式显示出它们。浏览器不会显示 HTML 标签，而是使用标签来解释页面的内容：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/web浏览器读取html文档.png" alt="web浏览器读取html文档"  title="web浏览器读取html文档" width="600" height=""></center>

## 例子解释

`<html>` 与 `</html>` 之间的文本描述网页
`<body>` 与 `</body>` 之间的文本是可见的页面内容
`<h1>` 与 `</h1>` 之间的文本被显示为标题
`<p>` 与 `</p>` 之间的文本被显示为段落

# 基本的 HTML 标签 - 四个实例

> 提示：学习 HTML 最好的方式就是边学边做实验。

## HTML 标题
HTML 标题（Heading）是通过 `<h1> - <h6>` 等标签进行定义的。

实例
```html
<h1>This is a heading</h1>
<h2>This is a heading</h2>
<h3>This is a heading</h3>
```

## HTML 段落
HTML 段落是通过 <p> 标签进行定义的。

实例
```html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/html段落标签p.png" alt="html段落标签p"  title="html段落标签p" width="600" height=""></center>

## HTML 链接

HTML 链接是通过 `<a>` 标签进行定义的。

实例
```html
<a href="http://www.w3school.com.cn">This is a link</a>
<!-- 注释：在 href 属性中指定链接的地址。 -->
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/HTML链接标签a.png" alt="HTML链接标签a"  title="HTML链接标签a" width="600" height=""></center>

## HTML 图像
HTML 图像是通过 `<img>` 标签进行定义的。

实例
```html
<img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/HTML图像标签img.png" width="104" height="142" />
<!-- 注释：图像的名称和尺寸是以属性的形式提供的。 -->
```

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/html图像标签img.png" alt="HTML图像标签img"  title="HTML图像标签img" width="600" height="" /></center>

# HTML 元素

HTML 文档是由 HTML 元素定义的。

<font color=red>HTML 元素</font>
    : 从开始标签（start tag）到结束标签（end tag）的所有代码。

| 开始标签                  | 元素内容            | 结束标签 |
| ------------------------- | ------------------- | -------- |
| `<p>`                     | This is a paragraph | `	</p>`  |
| `<a href="default.htm" >` | This is a link      | `</a>`   |
| `<br />`                  |                     |          |

> 注释：开始标签常被称为开放标签（opening tag），结束标签常称为闭合标签（closing tag）。

## HTML 元素语法

- HTML 元素以开始标签起始
- HTML 元素以结束标签终止
- **元素的内容**是开始标签与结束标签之间的内容
- 某些 HTML 元素具有空内容（empty content）
- **空元素**在开始标签中进行关闭（**以开始标签的结束而结束**）
- 大多数 HTML 元素可拥有属性

## 嵌套的 HTML 元素

大多数 HTML 元素可以嵌套（可以包含其他 HTML 元素）。
HTML 文档由嵌套的 HTML 元素构成。

HTML 文档实例
```html
<html>

<body>
<p>This is my first paragraph.</p>
</body>

</html>

<!-- 上面的例子包含三个 HTML 元素 -->
```

## HTML 实例解释

### `<p>` 元素

```html
<p>This is my first paragraph.</p>
```
这个 `<p>` 元素定义了 HTML 文档中的一个段落。
这个元素拥有一个开始标签 `<p>`，以及一个结束标签 `</p>`。
元素内容是：This is my first paragraph。

### `<body>` 元素

```html
<body>
<p>This is my first paragraph.</p>
</body>
```
`<body>` 元素定义了 HTML 文档的主体。
这个元素拥有一个开始标签 `<body>`，以及一个结束标签 `</body>`。
元素内容是另一个 HTML 元素（p 元素）。

### `<html>` 元素

```html
<html>

<body>
<p>This is my first paragraph.</p>
</body>

</html>
```
`<html>` 元素定义了整个 HTML 文档。
这个元素拥有一个开始标签 `<html>`，以及一个结束标签 `</html>`。
元素内容是另一个 HTML 元素（body 元素）。

### 不要忘记结束标签

即使您忘记了使用结束标签，大多数浏览器也会正确地显示 HTML：
```htnl
<p>This is a paragraph
<p>This is a paragraph
```
上面的例子在大多数浏览器中都没问题，但不要依赖这种做法。忘记使用结束标签会产生不可预料的结果或错误。
> 注释：未来的 HTML 版本不允许省略结束标签。

### 空的 HTML 元素
没有内容的 HTML 元素被称为空元素。空元素是在开始标签中关闭的。
`<br>` 就是没有关闭标签的空元素（`<br>` 标签定义换行）。
在 XHTML、XML 以及未来版本的 HTML 中，所有元素都必须被关闭。
在开始标签中添加斜杠，比如 `<br />`，是<font color=blue>关闭空元素的正确方法</font>，HTML、XHTML 和 XML 都接受这种方式。
即使 `<br>` 在所有浏览器中都是有效的，但使用 `<br />` 其实是更长远的保障。

### HTML 提示：使用小写标签

HTML 标签对大小写不敏感：`<P>` 等同于 `<p>`。许多网站都使用大写的 HTML 标签。
W3School 使用的是小写标签，因为万维网联盟（W3C）在 HTML 4 中推荐使用小写，而<font color=red>在未来 (X)HTML 版本中强制使用小写</font>。

# HTML 属性

<font color=red size=5>属性为 HTML 元素提供附加信息</font>。
- HTML 标签可以拥有属性。属性提供了有关 HTML 元素的更多的信息。
- 属性总是以名称/值对的形式出现，比如：name="value"。
- 属性总是在 HTML 元素的开始标签中规定。

## 属性实例

HTML 链接由 `<a>` 标签定义。链接的地址在 href 属性中指定：
`<a href="http://www.w3school.com.cn">This is a link</a>`

### 属性例子 1

`<h1>` 定义标题的开始。
`<h1 align="center">` 拥有关于对齐方式的附加信息。
```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">

<html>

<body>

<h1 align="center">This is heading 1</h1>

<p>上面的标题在页面中进行了居中排列。上面的标题在页面中进行了居中排列。上面的标题在页面中进行了居中排列。</p>

</body>
</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/属性例子1-标题对其方式.png" alt="属性例子1-标题对其方式"  title="属性例子1-标题对其方式" width="600" height="" /></center>

### 属性例子 2

`<body>` 定义 HTML 文档的主体。
`<body bgcolor="yellow">` 拥有关于背景颜色的附加信息。
```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<meta http-equiv="Content-Language" content="zh-cn" />
</head>

<body bgcolor="yellow">
<h2>请看: 改变了颜色的背景。</h2>
</body>

</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTML背景颜色属性.png" alt="HTML背景颜色属性"  title="HTML背景颜色属性" width="600" height="" /></center>

属性例子 3
`<table>` 定义 HTML 表格。（您将在稍后的章节学习到更多有关 HTML 表格的内容）

`<table border="1">` 拥有关于表格边框的附加信息。

### 属性例子 3

`<table>` 定义 HTML 表格。（您将在稍后的章节学习到更多有关 HTML 表格的内容）
`<table border="1">` 拥有关于表格边框的附加信息。

## HTML 提示：使用小写属性

属性和属性值对大小写不敏感。
不过，万维网联盟在其 HTML 4 推荐标准中推荐小写的属性/属性值。
而新版本的 (X)HTML 要求使用小写属性。

## 始终为属性值加引号
属性值应该始终被包括在引号内。双引号是最常用的，不过使用单引号也没有问题。

在某些个别的情况下，比如属性值本身就含有双引号，那么您必须使用单引号，例如：
`name='Bill "HelloWorld" Gates'`

## HTML 属性参考手册
我们的完整的 HTML 参考手册提供了每个 HTML 元素可使用的合法属性的完整列表：
[HTML 参考手册](https://www.w3school.com.cn/tags/index.asp)
[HTML 全局属性](https://www.w3school.com.cn/tags/html_ref_standardattributes.asp)

下面列出了适用于大多数 HTML 元素的属性：

| 属性  | 值               | 描述                                     |
| ----- | ---------------- | ---------------------------------------- |
| class | classname        | 规定元素的类名（classname）              |
| id    | id               | 规定元素的唯一 id                        |
| style | style_definition | 规定元素的行内样式（inline style）       |
| title | text             | 规定元素的额外信息（可在工具提示中显示） |

# HTML 标题

标题（Heading）是通过 `<h1>` - `<h6>` 等标签进行定义的。
`<h1>` 定义最大的标题。`<h6>` 定义最小的标题。
实例
```html
<h1>This is a heading</h1>
<h2>This is a heading</h2>
<h3>This is a heading</h3>
```
> 注释：浏览器会自动地在标题的前后添加空**行**。
> 注释：默认情况下，HTML 会自动地在块级元素前后添加一个额外的空**行**，比如段落、标题元素前后。

标题很重要
- 请确保将 HTML heading 标签只用于标题。不要仅仅是为了产生粗体或大号的文本而使用标题。
- 搜索引擎使用标题为您的网页的结构和内容编制索引。
- 因为用户可以通过标题来快速浏览您的网页，所以用标题来呈现文档结构是很重要的。
- 应该将 h1 用作主标题（最重要的），其后是 h2（次重要的），再其次是 h3，以此类推。

## HTML 水平线

`<hr />` 标签在 HTML 页面中创建水平线。
hr 元素可用于分隔内容。
实例
```html
<p>This is a paragraph</p>
<hr />
<p>This is a paragraph</p>
<hr />
<p>This is a paragraph</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTML水平线hr标签.png" alt="HTML水平线hr标签"  title="HTML水平线hr标签" width="600" height="" /></center>

> 提示：使用水平线 (`<hr>` 标签) 来分隔文章中的小节是一个办法（但并不是唯一的办法）。

## HTML 注释
可以将注释插入 HTML 代码中，这样可以提高其可读性，使代码更易被人理解。浏览器会忽略注释，也不会显示它们。
注释是这样写的：
实例
`<!-- This is a comment -->`
> 注释：开始括号之后（左边的括号）需要紧跟一个叹号，结束括号之前（右边的括号）不需要。
> 提示：合理地使用注释可以对未来的代码编辑工作产生帮助。

## HTML 提示 - 如何查看源代码

您一定曾经在看到某个网页时惊叹道 “WOW! 这是如何实现的？”
如果您想找到其中的奥秘，只需要单击右键，然后选择“查看源文件”（IE）或“<font color=red>查看页面源代码</font>”（Firefox），其他浏览器的做法也是类似的。这么做会打开一个包含页面 HTML 代码的窗口。

## HTML 标签参考手册

[Back to HTMLNotebook](#HTMLNotebook)

W3School 的标签参考手册提供了有关这些标题及其属性的更多信息。
您将在本教程下面的章节中学到更多有关 HTML 标签和属性的知识。

| 标签             | 描述             |
| ---------------- | ---------------- |
| `<html>`         | 定义 HTML 文档。 |
| `<body>`         | 定义文档的主体。 |
| `<h1>` to `<h6>` | 定义 HTML 标题   |
| `<hr>`           | 定义水平线。     |
| `<!-->`          | 定义注释。       |

# HTML 段落

可以把 HTML 文档分割为若干段落。
段落是通过 <p> 标签定义的。
实例
```html
<p>This is a paragraph</p>
<p>This is another paragraph</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTML段落标签p.png" alt="HTML段落标签p"  title="HTML段落标签p" width="600" height="" /></center>

> 注释：浏览器会自动地在段落的前后添加空行。（`<pre>` 是块级元素）
> 提示：使用空的段落标记 `<p></p>` 去插入一个空行是个坏习惯。用 `<br />` 标签代替它！（但是不要用 `<br />` 标签去创建列表。不要着急，您将在稍后的篇幅学习到 HTML 列表。）

## HTML 折行

如果您希望在不产生一个新段落的情况下进行换行（新行），请使用 `<br />` 标签：
`<p>This is<br />a para<br />graph with line breaks</p>`

> <br /> 元素是一个空的 HTML 元素。由于关闭标签没有任何意义，因此它没有结束标签。

## HTML 输出 - 有用的提示

我们无法确定 HTML 被显示的确切效果。屏幕的大小，以及对窗口的调整都可能导致不同的结果。
对于 HTML，您无法通过在 HTML 代码中添加额外的空格或换行来改变输出的效果。
当显示页面时，浏览器会移除源代码中多余的空格和空行。所有连续的空格或空行都会被算作一个空格。需要注意的是，HTML 代码中的所有连续的空行（换行）也被显示为一个空格。

# HTML 样式

style 属性用于改变 HTML 元素的样式。
style 属性的作用：
**提供了一种改变所有 HTML 元素的样式的通用方法**。
样式是 HTML 4 引入的，它是一种新的首选的改变 HTML 元素样式的方式。通过 HTML 样式，能够通过使用 style 属性直接将样式添加到 HTML 元素，或者间接地在独立的样式表中（CSS 文件）进行定义。
您可以在我们的 [CSS 教程](https://www.w3school.com.cn/css/index.asp)中学习关于样式和 CSS 的所有知识。
在我们的 HTML 教程中，我们将使用 style 属性向您讲解 HTML 样式。

## 不赞成使用的标签和属性

在 HTML 4 中，有若干的标签和属性是被废弃的。被废弃（Deprecated）的意思是在未来版本的 HTML 和 XHTML 中将不支持这些标签和属性。
这里传达的信息很明确：请避免使用这些被废弃的标签和属性！

**应该避免使用下面这些标签和属性 , 请使用样式代替！：**

| 标签                 | 描述             |
| -------------------- | ---------------- |
| `<center>`             | 定义居中的内容。 |
| `<font>` 和 `<basefont>` | 定义 HTML 字体。 |
| `<s>` 和 `<strike>`      | 定义删除线文本   |
| `<u>`                  | 定义下划线文本   |

| 属性    | 描述               |
| ------- | ------------------ |
| align   | 定义文本的对齐方式 |
| bgcolor | 定义背景颜色       |
| color   | 定义文本颜色       |

## HTML 样式实例 - 背景颜色

background-color 属性为元素定义了背景颜色：
```html
<html>

<body style="background-color:yellow">
<h2 style="background-color:red">This is a heading</h2>
<p style="background-color:green">This is a paragraph.</p>
</body>

</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/HTML样式style背景色background-color.png" alt="HTML样式style背景色background-color"  title="HTML样式style背景色background-color" width="600" height="" /></center>

> style 属性淘汰了“旧的” bgcolor 属性。

## HTML 样式实例 - 字体、颜色和尺寸

font-family、color 以及 font-size 属性分别定义元素中文本的字体系列、颜色和字体尺寸：
```html
<html>

<body>
<h1 style="font-family:verdana">A heading</h1>
<p style="font-family:arial;color:red;font-size:20px;">A paragraph.</p>
</body>

</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/HTML样式style字体颜色尺寸.png" alt="HTML样式style字体颜色尺寸"  title="HTML样式style字体颜色尺寸" width="600" height="" /></center>

> style 属性淘汰了旧的 <font> 标签

## HTML 样式实例 - 文本对齐

text-align 属性规定了元素中文本的水平对齐方式：
```html
<html>

<body>
<h1 style="text-align:center">This is a heading</h1>
<p>The heading above is aligned to the center of this page.</p>
</body>

</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115220504.png" alt="20200115220504"  title="HTML样式style文本对齐方式" width="600" height="" /></center>

> style 属性淘汰了旧的 "align" 属性。

# HTML 文本格式化

HTML 可定义很多供格式化输出的元素，比如粗体和斜体字。
[HTML 教程延伸阅读：改变文本的外观和含义](https://www.w3school.com.cn/html/html_style.asp)

## HTML 文本格式化实例

如何在一个 HTML 文件中对文本进行格式化
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115220856.png" alt="20200115220856"  title="HTML文本格式化" width="600" height="" /></center>

如何使用 pre 标签对空行和空格进行控制。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115222847.png" alt="20200115222847"  title="预格式文本" width="600" height="" /></center>

不同的“计算机输出”标签的显示效果
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115222338.png" alt="20200115222338"  title="HTML计算机输出标签的显示效果" width="600" height="" /></center>

如何在 HTML 文件中写地址。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115223105.png" alt="20200115223105"  title="HTML中写链接地址" width="600" height="" /></center>

如何实现缩写或首字母缩写。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115223551.png" alt="20200115223551"  title="缩写或首字母缩写" width="600" height="" /></center>

如何改变文字的方向。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115223755.png" alt="20200115223755"  title="变文字的方向逆序" width="600" height="" /></center>

如何实现长短不一的引用语。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115224009.png" alt="20200115224009"  title="长短不一的引用语" width="600" height="" /></center>



如何标记删除文本和插入文本。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115224152.png" alt="20200115224152"  title="标记删除文本和插入文本" width="600" height="" /></center>

## 如何查看 HTML 源码

您是否有过这样的经历，当你看到一个很棒的站点，你会很想知道开发人员是如何将它实现的？

你有没有看过一些网页，并且想知道它是如何做出来的呢？

要揭示一个网站的技术秘密，其实很简单。单击浏览器的“查看”菜单，选择“查看源文件”即可。随后你会看到一个弹出的窗口，窗口内就是实际的 HTML 代码。

## 文本格式化标签

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115224300.png" alt="20200115224300"  title="文本格式化标签" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115224449.png" alt="20200115224449"  title="引用和术语定义" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200115224401.png" alt="20200115224401"  title="计算机输出标签" width="600" height="" /></center>

# HTML 引用Quotation

HTML `<q>` 用于短的引用
HTML `<q>` 元素定义短的引用。

浏览器通常会为 `<q>` 元素包围引号。

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116085827.png" alt="20200116085827"  title="HTML短引用" width="600" height="" /></center>

## 用于长引用的 HTML <blockquote>

HTML `<blockquote>` 元素定义被引用的节。
浏览器通常会对 `<blockquote>` 元素进行缩进处理。
```html
<p>以下内容引用自 WWF 的网站：</p>
<blockquote cite="http://www.worldwildlife.org/who/index.html">

五十年来，WWF 一直致力于保护自然界的未来。
世界领先的环保组织，WWF 工作于 100 个国家，
并得到美国一百二十万会员及全球近五百万会员的支持。
</blockquote>
```

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116090319.png" alt="20200116090319"  title="HTML长引用" width="600" height="" /></center>

## 用于缩略词的 HTML `<abbr>`

HTML `<abbr>` 元素定义缩写或首字母缩略语。
对缩写进行标记能够为浏览器、翻译系统以及搜索引擎提供有用的信息。
<p><abbr title="World Health Organization">WHO</abbr> 成立于 1948 年。</p>
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116090814.png" alt="20200116090814"  title="HTML缩略词abbr" width="600" height="" /></center>

## 用于定义的 HTML <dfn>

HTML `<dfn>` 元素定义项目或缩写的定义。
`<dfn>` 的用法，按照 HTML5 标准中的描述，有点复杂：

1. 如果设置了 `<dfn>` 元素的 title 属性，则定义项目：
```html
<p><dfn title="World Health Organization">WHO</dfn> 成立于 1948 年。</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116112516.png" alt="20200116112516"  title="HTML定义元素dfn" width="600" height="" /></center>

2. 如果 <dfn> 元素包含具有标题的 <abbr> 元素，则 title 定义项目：
```html
<p><dfn><abbr title="World Health Organization">WHO</abbr></dfn> 成立于 1948 年。</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116112955.png" alt="20200116112955"  title="HTML定义dfn元素包含标题的abbr元素" width="600" height="" /></center>

3. 否则，<dfn> 文本内容即是项目，并且父元素包含定义。
```html
<p><dfn>WHO</dfn> World Health Organization 成立于 1948 年。</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116113249.png" alt="20200116113249"  title="HTML定义dfn元素文本内容即项目" width="600" height="" /></center>

> 注释：如果您希望简而化之，请使用第一条，或使用 <abbr> 代替。

## 用于联系信息的 HTML <address>

HTML `<address>` 元素定义文档或文章的联系信息（作者/拥有者）。
此元素通常以斜体显示。大多数浏览器会在此元素前后添加折行。
```html
<address>
Written by Donald Duck.<br> 
Visit us at:<br>
Example.com<br>
Box 564, Disneyland<br>
USA
</address>
```

## 用于著作标题的 HTML `<cite>`

HTML `<cite>` 元素定义著作的标题。
浏览器通常会以斜体显示 `<cite>` 元素。

<p><cite>The Scream</cite> by Edward Munch. Painted in 1893.</p>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116113838.png" alt="20200116113838"  title="HTML著作标题引用cite" width="600" height="" /></center>

## 用于双向重写的 HTML `<bdo>`
HTML `<bdo>` 元素定义双流向覆盖（bi-directional override）。
`<bdo>` 元素用于覆盖当前文本方向：
```html
<bdo dir="rtl">This text will be written from right to left</bdo>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116114242.png" alt="20200116114242"  title="HTML双向重写" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116114349.png" alt="20200116114349"  title="HTML 引文引用和定义元素" width="600" height="" /></center>

# HTML 计算机代码元素

```js
var person = {
    firstName:"Bill",
    lastName:"Gates",
    age:50,
    eyeColor:"blue"
}
```

## HTML 计算机代码格式

通常，HTML 使用可变的字母尺寸，以及可变的字母间距。
在显示计算机代码示例时，并不需要如此。
`<kbd>`, `<samp>`, 以及 `<code>` 元素全都支持固定的字母尺寸和间距。

## HTML 键盘格式

HTML `<kbd>` 元素定义键盘输入：
```html
<p>To open a file, select:</p>
<p><kbd>File | Open...</kbd></p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116114959.png" alt="20200116114959"  title="HTML键盘格式元素kbd" width="600" height="" /></center>

## HTML 样本格式

HTML `<samp>` 元素定义计算机输出示例：

```html
<samp>
demo.example.com login: Apr 12 09:10:17

Linux 2.6.10-grsec+gg3+e+fhs6b+nfs+gr0501+++p3+c4a+gr2b-reslog-v6.189
</samp>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116115435.png" alt="20200116115435"  title="样本格式元素samp定义计算机输出示例" width="600" height="" /></center>

## HTML 代码格式
HTML `<code>` 元素定义编程代码示例：
```html
<code>
var person = { firstName:"Bill", lastName:"Gates", age:50, eyeColor:"blue" }
</code>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116115640.png" alt="20200116115640"  title="代码格式code" width="600" height="" /></center>

> `<code>` 元素不保留多余的空格和折行：

```html
<p>Coding Example:</p>

<code>
var person = {
    firstName:"Bill",
    lastName:"Gates",
    age:50,
    eyeColor:"blue"
}
</code>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116115846.png" alt="20200116115846"  title="代码格式code不保留多余的空格和折行" width="600" height="" /></center>

> 如需保留多余的空格和折行，您必须在 <pre> 元素中包围代码：

```html
<p>Coding Example:</p>

<code>
<pre>
var person = {
    firstName:"Bill",
    lastName:"Gates",
    age:50,
    eyeColor:"blue"
}
</pre>
</code>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116120049.png" alt="20200116120049"  title="代码格式code加pre保留多余的空格和折行" width="600" height="" /></center>

## HTML 变量格式化
HTML <var> 元素定义数学变量：
```html
<p>Einstein wrote:</p>

<p><var>E = m c<sup>2</sup></var></p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116120321.png" alt="20200116120321"  title="HTML 计算机代码元素标签" width="600" height="" /></center>

# HTML 注释

注释标签 `<!-- 与 -->` 用于在 HTML 插入注释。
> 注释：在开始标签中有一个惊叹号，但是结束标签中没有。
浏览器不会显示注释，但是能够帮助记录您的 HTML 文档。
您可以利用注释在 HTML 中放置通知和提醒信息：
```html
<!-- 这是一段注释 -->

<p>这是一个段落。</p>

<!-- 记得在此处添加信息 -->
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116120646.png" alt="20200116120646"  title="HTML 注释" width="600" height="" /></center>

## 条件注释

您也许会在 HTML 中偶尔发现条件注释：
```html
<!--[if IE 8]>
    .... some HTML here ....
<![endif]-->
```
> 条件注释定义只有 Internet Explorer 执行的 HTML 标签。

## 软件程序标签

各种 HTML 软件程序也能够生成 HTML 注释。
例如 `<!--webbot bot-->` 标签会被包围在由 FrontPage 和 Expression Web 创建的 HTML 注释中。
作为一项规则，这些标签的存在，有助于对创建这些标签的软件的支持。

# HTML CSS

通过使用 HTML4.0，所有的格式化代码均可移出 HTML 文档，然后移入一个独立的样式表。

如何使用添加到 `<head>` 部分的样式信息对 HTML 进行格式化。
```html
<html>

<head>
<style type="text/css">
h1 {color: red}
p {color: blue}
</style>
</head>

<body>
<h1>header 1</h1>
<p>A paragraph.</p>
</body>

</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116141908.png" alt="20200116141908"  title="添加到 head部分的样式信息对 HTML 进行格式化" width="600" height="" /></center>

如何使用样式属性做一个没有下划线的链接。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116142706.png" alt="20200116142706"  title="使用样式style属性做一个没有下划线的链接" width="600" height="" /></center>

如何 `<link>` 标签链接到一个外部样式表。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116144050.png" alt="20200116144050"  title="link标签链接到一个外部样式表" width="600" height="" /></center>

## 如何使用样式

当浏览器读到一个样式表，它就会按照这个样式表来对文档进行格式化。有以下三种方式来插入样式表：
1. 外部样式表
当样式需要被应用到很多页面的时候，外部样式表将是理想的选择。使用外部样式表，你就可以通过更改一个文件来改变整个站点的外观。
```html
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

2. 内部样式表
当单个文件需要特别样式时，就可以使用内部样式表。你可以在 head 部分通过 `<style>` 标签定义内部样式表。
```html
<html>
<head>

<style type="text/css">
body {background-color: red}
p {margin-left: 200px}
</style>
</head>

<body><p>我引用了内部样式表</p></body>
</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116144908.png" alt="20200116144908"  title="在 head 部分通过style标签定义内部样式表" width="600" height="" /></center>

3. 内联样式
当特殊的样式需要应用到个别元素时，就可以使用内联样式。 使用内联样式的方法是在相关的标签中使用样式属性。样式属性可以包含任何 CSS 属性。以下实例显示出如何改变段落的颜色和左外边距。
```html
<p style="color: red; margin-left: 200px">
This is a paragraph
</p>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116145229.png" alt="20200116145229"  title="20200116145229" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116145426.png" alt="20200116145426"  title="常见样式标签" width="600" height="" /></center>

# HTML 链接

[什么是超文本？](https://www.w3school.com.cn/tags/tag_term_hypertext.asp)

HTML 使用超级链接与网络上的另一个文档相连。
几乎可以在所有的网页中找到链接。点击链接可以从一张页面跳转到另一张页面。

如何在 HTML 文档中创建链接。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116145953.png" alt="20200116145953"  title="HTML 文档中创建链接" width="600" height="" /></center>

如何使用图像作为链接。
```html
<html>

<body>
<p>
您也可以使用图像来作链接：
<a href="/example/html/lastpage.html">
<img border="0" src="/i/eg_buttonnext.gif" />
</a>
</p>

</body>
</html>
```
<a href="https://www.w3school.com.cn/tiy/t.asp?f=html_imglink">
<center><img border="0" src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/buttonnext.png" alt="buttonnext"  title="buttonnext图像作为链接" width="600" height="" /></center>
</a>

如何在新窗口打开一个页面，这样的话访问者就无需离开你的站点了。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116151647.png" alt="20200116151647"  title=" target 属性设置为 '_blank'该链接会在新窗口中打开" width="600" height="" /></center>

如何使用链接跳转至文档的另一个部分
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116155017.png" alt="20200116155017"  title="使用链接跳转至文档的另一个部分" width="600" height="" /></center>

如何跳出框架，假如你的页面被固定在框架之内。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116155450.png" alt="20200116155450"  title="跳出框架" width="600" height="" /></center>

如何链接到一个邮件。（本例在安装邮件客户端程序后才能工作。）
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116194635.png" alt="20200116194635"  title="链接到一个邮件" width="600" height="" /></center>

更加复杂的邮件链接
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116194820.png" alt="20200116194820"  title="更加复杂的邮件链接" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116194858.png" alt="20200116194858"  title="HTML 链接标签" width="600" height="" /></center>

# HTML 图像

通过使用 HTML，可以在文档中显示图像。
如何在网页中显示图像。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116195534.png" alt="20200116195534"  title="网页中显示图像" width="600" height="" /></center>

如何将其他文件夹或服务器的图片显示到网页中。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116195729.png" alt="20200116195729"  title="将其他文件夹或服务器的图片显示到网页中" width="600" height="" /></center>

如何向 HTML 页面添加背景图片。
```html
<html>

<body background="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/eg_cute.gif">

<h3>图像背景</h3>

<p>gif 和 jpg 文件均可用作 HTML 背景。</p>

<p>如果图像小于页面，图像会进行重复。</p>

</body>
</html>
```
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/d9492d2e-0e88-46e9-9bc4-2c273e6cab25.gif" alt="d9492d2e-0e88-46e9-9bc4-2c273e6cab25"  title="HTML 页面添加背景图片" width="600" height="" /></center>

如何在文字中排列图像
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116201255.png" alt="20200116201255"  title="文字中排列图像" width="600" height="" /></center>

如何使图片浮动至段落的左边或右边。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116201438.png" alt="20200116201438"  title="图片浮动至段落的左边或右边" width="600" height="" /></center>

如何将图片调整到不同的尺寸。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116201618.png" alt="20200116201618"  title="图片调整到不同的尺寸" width="600" height="" /></center>

如何为图片显示替换文本。在浏览器无法载入图像时，替换文本属性告诉读者们失去的信息。为页面上的图像都加上替换文本属性是个好习惯。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116201832.png" alt="20200116201832"  title="alt属性为图片显示替换文本" width="600" height="" /></center>

如何将图像作为一个链接使用。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116202000.png" alt="20200116202000"  title="将图像作为一个链接使用" width="600" height="" /></center>

如何创建带有可供点击区域的图像地图。其中的每个区域都是一个超级链接。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116202521.png" alt="20200116202521"  title="区域的图像地图" width="600" height="" /></center>

如何把一幅普通的图像设置为图像映射。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116202846.png" alt="20200116202846"  title="普通的图像设置为图像映射" width="600" height="" /></center>

## 图像标签（`<img>`）和源属性（Src）

在 HTML 中，图像由 `<img>` 标签定义。
`<img>` 是空标签，意思是说，它只包含属性，并且没有闭合标签。
要在页面上显示图像，你需要使用源属性（src）。src 指 "source"。源属性的值是图像的 URL 地址。
`<img src="url" />`

## 替换文本属性（Alt）

alt 属性用来为图像定义一串预备的可替换的文本。替换文本属性的值是用户定义的。
`<img src="boat.gif" alt="Big Boat">`
在浏览器无法载入图像时，替换文本属性告诉读者她们失去的信息。此时，浏览器将显示这个替代性的文本而不是图像。为页面上的图像都加上替换文本属性是个好习惯，这样有助于更好的显示信息，并且对于那些使用纯文本浏览器的人来说是非常有用的。

## 基本的注意事项 - 有用的提示：

假如某个 <font color=red>HTML 文件</font>包含十个图像，那么为了正确显示这个页面，需要加载 11 个文件。加载图片是需要时间的，所以我们的建议是：<font color=red>慎用图片</font>。

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116202943.png" alt="20200116202943"  title="图像标签" width="600" height="" /></center>

# HTML 表格

1. 表格由 `<table>` 标签来定义。
2. 每个表格均有若干行（由 `<tr>` 标签定义），字母 tr 指表格行（table row）。
3. 每行被分割为若干单元格（由 `<td>` 标签定义）, 字母 td 指表格数据（table data），即数据单元格的内容。

数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。

如何在 HTML 文档中创建表格
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116204333.png" alt="20200116204333"  title="创建表格" width="600" height="" /></center>

各种类型的表格边框
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116204538.png" alt="20200116204538"  title="表格边框" width="600" height="" /></center>

## 表格和边框属性

如果不定义边框属性，表格将不显示边框。有时这很有用，但是大多数时候，我们希望显示边框。

使用边框属性来显示一个带有边框的表格：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116205207.png" alt="20200116205207"  title="边框属性border" width="600" height="" /></center>

## 表格的表头

表格的表头使用 `<th>` 标签进行定义。
大多数浏览器会把表头显示为粗体居中的文本：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116205405.png" alt="20200116205405"  title="表格的表头标签th" width="600" height="" /></center>

如何水平或竖直地显示表格表头
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116210510.png" alt="20200116210510"  title="水平或竖直地显示表格表头" width="600" height="" /></center>

## 表格中的空单元格

在一些浏览器中，没有内容的表格单元显示得不太好。如果某个单元格是空的（没有内容），浏览器可能无法显示出这个单元格的边框。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116210133.png" alt="20200116210133"  title="表格中的空单元格" width="600" height="" /></center>

正如您看到的，其中一个单元没有边框。这是因为它是空的。在该单元中插入一个空格后，仍然没有边框。
我们的技巧是在单元中插入一个 no-breaking 空格。
no-breaking 空格是一个字符实体。如果您不清楚什么是字符实体，请阅读关于字符实体的章节。
no-breaking 空格由和号开始 ("&")，然后是字符"nbsp"，并以分号结尾(";")。

## 带有标题的表格caption

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116210958.png" alt="20200116210958"  title="带有标题的表格" width="600" height="" /></center>

## 定义跨行或跨列的表格单元格
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116211411.png" alt="20200116211411"  title="跨行或跨列的表格单元格" width="600" height="" /></center>

## 在不同的元素内显示元素

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116213200.png" alt="20200116213200"  title="不同的元素内显示元素" width="600" height="" /></center>

> Markdown 不支持border属性，表格异常

## Cell padding 来创建单元格内容与其边框之间的空白

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116215318.png" alt="20200116215318"  title="20200116215318" width="600" height="" /></center>

## Cell spacing 增加单元格之间的距离

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116215526.png" alt="20200116215526"  title="20200116215526" width="600" height="" /></center>

## 向表格添加背景

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116215746.png" alt="20200116215746"  title="表格添加背景" width="600" height="" /></center>

## 向一个或者更多表格单元添加背景

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116220020.png" alt="20200116220020"  title="一个或者更多表格单元添加背景" width="600" height="" /></center>

## align 属性排列单元格内容

排列单元格内容,以便创建一个美观的表格
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116220232.png" alt="20200116220232"  title="align 属性排列单元格内容" width="600" height="" /></center>

## frame 属性来控制围绕表格的边框

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116220857.png" alt="20200116220857"  title=" frame属性来控制围绕表格的边框" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116221032.png" alt="20200116221032"  title="表格标签" width="600" height="" /></center>

# HTML 列表

HTML 支持有序、无序和定义列表

## 无序列表

无序列表是一个项目的列表，此列项目使用粗体圆点（典型的小黑圆圈）进行标记。

无序列表始于 `<ul>` 标签。每个列表项始于 `<li>`。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116221452.png" alt="20200116221452"  title="无序列表" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116222129.png" alt="20200116222129"  title="不同类型的无序列表" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116222506.png" alt="20200116222506"  title="嵌套列表" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116222728.png" alt="20200116222728"  title="嵌套列表" width="600" height="" /></center>

## 有序列表

同样，有序列表也是一列项目，列表项目使用数字进行标记。

有序列表始于 `<ol>` 标签。每个列表项始于 `<li>` 标签。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116221621.png" alt="20200116221621"  title="有序列表" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116222326.png" alt="20200116222326"  title="不同类型的有序列表" width="600" height="" /></center>

## 定义列表

自定义列表不仅仅是一列项目，而是项目及其注释的组合。

自定义<font color=red></font>列表以 `<dl>` 标签开始</font>。每个自定义<font color=orange></font>列表项以 `<dt>` 开始</font>。每个自定义<font color=blue></font>列表项的定义以 `<dd>` 开始</font>。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116221807.png" alt="20200116221807"  title="自定义列表" width="600" height="" /></center>

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116222824.png" alt="20200116222824"  title="20200116222824" width="600" height="" /></center>

# HTML 块元素

可以通过 `<div>` 和 `<span>` 将 HTML 元素组合起来。

## HTML 块

大多数 HTML 元素被定义为块级元素或内联元素。

编者注：“块级元素”译为 block level element，“内联元素”译为 inline element。

块级元素在浏览器显示时，通常会以新行来开始（和结束）。

例子：`<h1>, <p>, <ul>, <table>`

## HTML 内联元素

内联元素在显示时通常不会以新行开始。

例子：`<b>, <td>, <a>, <img>`

## HTML `<div>`<font color=red>块级</font>元素

HTML `<div>` 元素是块级元素，它是可用于组合其他 HTML 元素的容器。

`<div>` <font color=red>元素没有特定的含义</font>。除此之外，由于它属于块级元素，浏览器会在其前后显示折行。

如果与 CSS 一同使用，`<div>` 元素<font color=red>可用于对大的内容块设置样式属性</font>。

`<div>` 元素的另一个常见的用途是文档布局。它取代了使用表格定义布局的老式方法。使用 `<table>` 元素进行文档布局不是表格的正确用法。`<table>` 元素的作用是显示表格化的数据。

## HTML `<span>` <font color=blue>内联</font>元素

HTML `<span>` 元素是 <font color=blue>内联元素，可用作文本的容器</font>。

`<span>` 元素<font color=blue>也没有特定的含义</font>。

当与 CSS 一同使用时，`<span>` 元素可用于<font color=blue>为部分文本设置样式属性</font>。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116223723.png" alt="20200116223723"  title="HTML 分组标签" width="600" height="" /></center>

# HTML 类

对 HTML 进行分类（设置类），使我们能够为元素的类定义 CSS 样式。

为相同的类设置相同的样式，或者为不同的类设置不同的样式。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116224248.png" alt="20200116224248"  title="元素的类定义 CSS 样式" width="600" height="" /></center>

## 分类块级元素

HTML `<div>` 元素是块级元素。它能够用作其他 HTML 元素的容器。

设置 `<div>` 元素的类，使我们能够为相同的 `<div>` 元素设置相同的类：
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116224541.png" alt="20200116224541"  title="相同的div块级元素设置相同的类" width="600" height="" /></center>

## 分类行内元素

HTML `<span>` 元素是行内元素，能够用作文本的容器。

设置 `<span>` 元素的类，能够为相同的 `<span>` 元素设置相同的样式。
<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/20200116225044.png" alt="20200116225044"  title="相同的span行内元素设置相同的样式" width="600" height="" /></center>

# HTML 布局

HTML 布局
https://www.w3school.com.cn/html/html_layout.asp