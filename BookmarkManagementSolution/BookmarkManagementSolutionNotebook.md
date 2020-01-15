
# Bookmark Management Solution

> 参考
[奔跑中的奶酪-一份系统且全面的书签管理方案](https://mp.weixin.qq.com/s/mG28cu3xpp8fCcZXIoNusQ)

书签是用来储存网站地址的一个设计

## 书签的筛选

平时上网浏览网页，按照「使用频率」和「长期价值」来看，我们有下面的处理方式。
<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/书签筛选-使用频率-长期价值.png" alt="书签筛选-使用频率-长期价值"  title="书签筛选-使用频率-长期价值" width="600" height="">

书签则是属于「经常使用」和「有长期价值」的网页。

1. 保存为书签。
造成书签管理混乱的一个重要原因，是因为有太多不经常使用和太多短期内才有用的书签。
我们在收藏的网页时，应该只收藏「经常使用」和「有长期价值」的网站，而且也应该只收藏网站的主页和网站的部分专题页面，能做到这一步，其实就已经大大减少了书签管理的压力。
那如果是网站的某个具体页面，想要收藏又该如何处理呢？
2. 稍后阅读。
比如我们遇到了一个感兴趣的网页，打算以后再次翻看。
通常的做法是点击地址栏右边的“星星”图标，快捷键「Ctrl+D」，网页就会收藏到默认的书签文件夹【其他书签】里，这样的设计其实是一个稍后阅读功能。
但更好的做法是，使用拓展 Pocket 来做稍后阅读的标记，除了可以避免书签的臃肿，而且它还会有时间线，管理起来也更加方便。
> 推荐方案：Pocket（支持 Firefox / Chrome ）

<center><img src="https://raw.githubusercontent.com/ld269440877/images/master/HTMLNotebook/稍后阅读-Pocket插件快捷方式.png" alt="稍后阅读-Pocket插件快捷方式"  title="稍后阅读-Pocket插件快捷方式" width="600" height="" /></center>

3. 会话保存
如果说「稍后阅读」是用于保存一个或者几个网页的话，那么「会话保存」则是针对一个项目或者某一次上网的浏览场景。
比如我们在做一个项目，打开了一些网页，但由于上下班等原因需要暂时停止，这时我们就需要将当前打开的网页保存起来。

通常的做法是使用快捷键「Ctrl+Shift+D」来将当前的会话状态，以新建一个书签文件夹的方式保存到默认的书签文件夹【其他书签】里。
<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/会话保存-Ctrl-Shift-D.png" alt="会话保存-Ctrl-Shift-D"  title="会话保存-Ctrl-Shift-D" width="600" height="">

更好的做法是，使用会话管理拓展 Tab Session Manager 来解决代替，它不仅可以避免收录过多的临时书签，而且操作简单快捷，完全自动化实现。

> 推荐方案：Tab Session Manager（支持 Firefox / Chrome）

<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/会话保存-TabSessionManager插件.png" alt="会话保存-TabSessionManager插件"  title="会话保存-TabSessionManager插件" width="600" height="">

4. 保存到笔记
而如果遇到的是高质量的网页内容，我们往往需要仔细阅读，并做好记录保存到笔记本里去，此后，这样的网页我们一般就不会再打开了。
但如果你还是想做一下标记，那么可以将链接保存到单独的笔记中去，比如下面是我做的主题笔记。
<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/主题笔记.png" alt="主题笔记"  title="主题笔记" width="600" height="">
不过这已经属于“知识管理”的范畴了，我们以后有机会再讲。

5. 查找浏览记录
而对于那些短期内才有用和不经常使用的网页，查找浏览器自带的浏览记录已经足够了。

## 书签的分类

在做书签分类的时候，我们很难一次性就建立起永久且完美的书签分类。
以「关注的领域」和「所在的行业」来进行分类是一个不错的开始，然后再不断迭代升级我们的分类方法。
1. MECE 分类原则。
在面对复杂内容进行分类时，往往都会用到「MECE 原则」，也就是 Mutually Exclusive Collectively Exhaustive，中文意思是「相互独立、完全穷尽」，也就是「无重复、无遗漏」。

为什么这么重要呢？
如果分类没有涵盖问题的所有方面，那么最终推演出来的方案就有可能以偏概全。
而如果分类有很多的重叠，那么我们就无法厘清真正的原因，也可能会做出很多重复劳动。
比如下面这张图：
<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/MECE原则.png" alt="MECE原则"  title="MECE原则" width="600" height="">

又比如我们对【平面设计】这个文件夹进行分类时，只要始终使用一个维度进行分类，那就能做到不重复、不遗漏，很 MECE。
<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/MECE原则-一个维度.png" alt="MECE原则-一个维度"  title="MECE原则-一个维度" width="600" height="">

2. 设置一个暂存文件夹
比如我们有一个【音乐视频】的书签文件夹，一次遇到了一个与音乐相关的网站，但不知道是放在子目录里的【音乐网站】还是【FM 电台】上，而且放在这两个文件夹上面好像都不太对。
那么新建一个【音乐相关】的暂存文件夹，把那些暂时不知道怎么分类的网站都放到这里来，等以后明确了再重新分类也不迟。
<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/音乐相关-暂存文件夹.png" alt="音乐相关-暂存文件夹"  title="音乐相关-暂存文件夹" width="600" height="">
设置一个暂存文件夹的目的，是为了避免新增书签时引起的分类混乱。

3. 文件夹层次不要超过 3 层
经验告诉我们，任何事情超过 3 次就会变得难以记忆
当书签文件夹的层次超过 3 层时，除了难于记忆外，选择书签也会变得复杂起来，你会觉得从一层一层的文件夹中去找想要的书签是一件麻烦的事。
因此，书签文件夹的分级最好不要超过 3 层。
<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/文件夹层级不超过3层.png" alt="文件夹层级不超过3层"  title="文件夹层级不超过3层" width="600" height="">

4. 多用文件夹，避免一个文件夹下有过多书签
大多数浏览器没有书签并排显示的功能，如果同一个文件夹下书签数量过多，书签就会折叠起来，只能通过滚动查看所有书签。
这无疑提高了查找的难度，多用文件夹就可以避免这种情况。

## 书签的命名

统一有序的命名，不仅方便于查找书签，而且在视觉上也会有很好的美感，即使再多的书签也会显得井然有序，一切尽在掌握。

1. 书签的长度不要太长，也不要太短
书签的长度也会影响书签的查找，书签名称的长度最好是在 4 个汉字左右，2个字太短，不方便鼠标点击，6个字以上又会太占空间。
同理，书签文件夹的名称也是如此。

2. 去掉网站自带的 Slogan
在添加书签时，书签的名称默认会是「网站名称 - 网站Slogan」这种格式。
比如爱奇艺的书签名称会显示为「爱奇艺-全球领先的在线视频网站-海量...」，
太多无用的内容会造成信息干扰，不利于查找，我们有必要将其缩短，一般来说只保留「网站名称」就可以了。

3. 为小众网站的名称添加网站描述。
而对于那些不怎么知名的网站，我们往往能记得住它们的功能作用，却很难记住它们的名称，
这时我们可以将书签名称设置为「网站描述 | 网站名称 」这种格式。
网站描述就是你认为网站是做什么的网站，网站描述和网站名称之间用分割线" | " 隔开，这样可以让书签名称更加清晰明朗，
在必要的时候，我们甚至还可以只写网站描述。
<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/小众网站的名称添加网站描述.png" alt="小众网站的名称添加网站描述"  title="小众网站的名称添加网站描述" width="600" height="">

4. 善用分割线
任何相似的东西堆积在一起都会变得难以分辩，书签也是如此，善用分割线是个聪明的做法。
垂直分割线很好办，只需要在书签文件夹名称的后面加上“丨”即可。
而水平分割线，我们可以使用网站 <font color=red>Bookmarks Separator </font>提供的“伪分割线”来解决，而且支持在分割线上添加文字，这一点棒级了。

<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/添加水平分割线-BookmarksSeparator.png" alt="添加水平分割线-BookmarksSeparator"  title="添加水平分割线-BookmarksSeparator" width="600" height="">

## 书签的调用

1. Bookmark Management Solution
   1. 书签的筛选
   2. 书签的分类
   3. 书签的命名
   4. 书签的调用
   5. 一些你可能不知道的书签小技巧
除了使用分类文件夹进行书签查找外，使用浏览器地址栏的模糊匹配功能也是一个调用书签的好方法。
只需要在地址栏输入一两个关键字，地址栏就会自动匹配包括浏览记录、加星书签、书签名称、书签地址等内容。
但地址栏会优先匹配“浏览记录”，这可能会导致“加星书签”无法完全显示，这时只需要在关键字前面输入字符 * 就会优先匹配加星书签了。
> Chrome 浏览器默认没有这个功能，但可以安装<font color=orange>拓展 Holmes </font>来实现这个功能。

<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/书签搜索-Holmes插件.png" alt="书签搜索-Holmes插件"  title="书签搜索-Holmes插件" width="600" height="">

2. 使用关键字调用书签
对于经常要访问的网页，我们还可以使用关键字来做精准匹配，
比如我们把网站“www.runningcheese.com”的书签关键字设置为"rc"，只需要输入 rc 就会最先匹配这个书签了。
<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/关键字调用书签.png" alt="关键字调用书签"  title="关键字调用书签" width="600" height="">

> Chrome 浏览器可以在“搜索引擎管理器”里给书签添加关键字。
比如我们需要经常打开书签管理页面 chrome://bookmarks，那将它的关键字设置为 bbb 就可以快速打开这个书签地址了。

<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/搜索引擎管理器-给书签添加关键字.png" alt="搜索引擎管理器-给书签添加关键字"  title="搜索引擎管理器-给书签添加关键字" width="600" height="">

<img src="https://raw.githubusercontent.com/ld269440877/images/master/BookmarkManagementSolutionNotebook/设置-搜索引擎-给书签添加关键字.png" alt="设置-搜索引擎-给书签添加关键字"  title="设置-搜索引擎-给书签添加关键字" width="600" height="">

## 一些你可能不知道的书签小技巧

1. 按住 `Ctrl` 键点击书签，可以连续打开多个书签。
2. 不同浏览器之间迁移书签，可以手动将浏览器书签导出为 `.html` 文件。
3. 拖动地址栏前面的“`锁`”图标，可以快速地将网页保存到某个指定的书签文件夹，同理，网页上的链接也是如此。
4. 浏览器都会有书签自动备份功能，Firefox 在配置文件夹的 `\bookmarkbackups` 里，Chrome 在配置文件夹下的 `Default\Bookmarks` 里，如果你的浏览器不幸崩溃，可以在这里找回。
5. 书签保存时间长了，你很难保证它是否还有效，Firefox 可以用拓展 `Bookmarks Organizer` 检测，Chrome 可以用 `Bookmarks clean up`。

