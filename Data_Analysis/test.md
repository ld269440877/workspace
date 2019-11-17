
```plantuml
@startmindmap

caption UML
title Unified Modeling Language
* UML

**_ 结构型的图(Structure Diagram)
*** 类图(Class Diagram)
*** 对象图(Object Diagram)
*** 构件图(Component Diagram)
*** 部署图(Deployment Diagram)
*** 包图(Package Diagram)

**_ 行为型的图(Behavior Diagram)
*** 活动图(Activity Diagram)
*** 状态机图(State Machine Diagram)
*** 顺序图(Sequence Diagram)
*** 通信图(Communication Diagram)
*** 用例图(Use Case Diagram)
*** 时序图(Timing Diagram)

@endmindmap
```


















```plantuml
@startsalt
{#<font color="red" ><b>"my table"</b></font>|"my table"
Login | "MyName "
Password | "**** "
[Cancel] | [ OK ]
}
@endsalt
```
```plantuml
@startuml
salt
{
Just plain text
[This is my button]
==
() Unchecked radio
(X) Checked radio
[] Unchecked box
[X] Checked box
"Enter text here "
^This is a droplist^
^This is a droplist^
}
@enduml
```
```plantuml
@startuml
object demo {
* Bullet list
* Second item
}
note right
* Bullet list
* Second item
** Sub item
end note
legend
# Numbered list
# Second item
## Sub item
## Another sub item
# Third
end legend
@enduml
```


```plantuml
@startuml

Alice -> Bob: Authentication Request
alt successful case
rnote left
<img:2019-11-17-20-11.png>
end note
Bob -> Alice: Authentication Accepted
else some kind of failure
Bob -> Alice: Authentication Failure
group My own label
Alice -> Log : Log attack start
loop 1000 times
Alice -> Bob: DNS Attack
end
Alice -> Log : Log attack end
end
else Another type of failure
Bob -> Alice: Please repeat
end
@enduml

```

```plantuml


scale 100 height
scale 100 width
scale 5
skinparam class {
BackgroundColor PaleGreen
ArrowColor SeaGreen
BorderColor SpringGreen
}
skinparam stereotypeCBackgroundColor Yellow
class Student{
    Name
    --
    Age
    ==
    Height
    ..
    weight
}

@startuml
listopeniconic 
@enduml

```