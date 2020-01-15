
# HTMLNotebook

> 参考
[HTML 基础教程](https://www.w3school.com.cn/html/html_jianjie.asp)
[HTML在线测试-W3School TIY Editor](https://www.w3school.com.cn/tiy/t.asp?f=html_headers)


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

# HTML 引用

# TODO HTML 引用
https://www.w3school.com.cn/html/html_quotation_elements.asp