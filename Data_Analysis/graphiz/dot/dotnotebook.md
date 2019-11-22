<!-- dot 思维导图 -->
<!-- dot  组件-->
<!-- dot 完整例子 -->
- dot
  - 思维导图
  - 组件
  - 完整例子
```plantuml

@startmindmap #orgmode语法
scale 1.5
caption Caption:Dot
title Title:Dot mindmap
* <&flag>Graphvizdot\n<s>graphviz is a tool, and dot is a language.</s>
left
** <&graph>graph-subgraph
** digraph
right
' kexuan
** Graph/Digraph声明图，名字可选
** Node修饰节点
** Edge修饰连线

header
Header: Dot mindmap
endheader

center footer Footer: Dot mindmap

legend right
    Legend:
    Dot
endlegend

@endmindmap
```

```dot  # graph
digraph G{
compound=true;  /* lhead and ltail of clusters depend compound that is true. */
concentrade=true
size ="8,6"; ratio=fill; node[fontsize=38];

    subgraph cluster0 {
# 设定graph属性
bgcolor=black
center=true
clusterrank=global
concentrate=true
dpi=300

style=filled;
color=ghostwhite;
fontcolor=green
fontsize=50;
label = "process #1";
labeljust=l
labelloc=bottom
margin=0.5

mindist=1
nodesep=1
orientation=30
rotate=30

page="8.5,11"
pencolor=yellow
penwidth=10

#peripheries=1
#samplepoints=8
size=10
#splines=polylines



    # 设定节点node属性
    node [style=filled, color=blue, shape=egg, image="2019-11-19-09-11.png", imagescale=true,margin="1.5,.5",samplepoints=80, fillcolor=lightyellow, distortion=0.3,comment="12345",fontcolor=red];
    a0 [label="a000", shape=polygon, sides=5, peripheries=2,style=filled, color="255, 255,255",orientation=180]


    a0 -> a1
     a0 -> a1 -> a2 -> a3
    
    }

    subgraph cluster1 {
        node [style=filled];
        b0->b1->b2->b3;
        label="process #2";
        color=blue;
        b0 [color=orange]
        }

#设置连线edge属性
start -> a0  [arrowsize=5,color=cyan, dir=both, arrowhead=curve,arrowtail=normal, fontcolor=orange,label="start-a0",fontsize=50,headlabel =123, taillabel="abc",headport=w,tailport=w, id="A",labeldistance=15, labelangle=-10, labelfontcolor=purple,labelfontsize=30,minlen=10, penwidth=10, style=dotted, weight=1];

start -> b0;
# Graph with edges on clusters
a1 -> b3  [lhead=cluster1, ltail=cluster0];
a3 -> end;
b3 -> end[lhead=end, ltail=cluster1];

start [shape=Mdiamond];
end [shape=Msquare];
}
```




```dot  # table
digraph structs {
node [shape=record];
    struct1 [shape=record,label="<f0> left |<f1> middle |<f2> right"];
    struct2 [shape=record,label="<f0>one|<f1>two|<f2>|<f3>",height=.1,width=.1, fontcolor=red, fontsize=20];
    struct3 [shape=record,label="hello \nworld |{b |{c |<here>d|e}|f}|g|h"];
    struct1:f0:nw -> struct2:f0;
    struct1:f1:se -> struct3:here [tailport=s];
struct1:f2 -> a1 [label="1-1"];
}
```


