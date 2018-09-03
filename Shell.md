### 术语名词    
IDC（Internet Data Center)互联网数据中心  
ISP--(Internet Service Provider)互联网服务提供商   
ICP--(Internet Content Provider)互联网内容提供商。ICP证成为网站经营的许可证，经营性网站必须办理ICP证   
CDN--(Content Delivery Network)内容分发网络。CDN的关键技术主要有内容存储和分发技术  
LVS--(Linux Virtual Server)Linux虚拟服务器。LVS集群采用IP负载均衡技术和基于内容请求分发技术  
CGI--(Common Gateway Interface)通用网关接口  
GSLB--(Global Server Load Balance）全局负载均衡。 CDN 系统架构中最核心的部分，基于DNS的GSLB正是在返回DNS解析结果的过程中进行智能决策，给用户返回一个最佳的服务IP  
BOSS--(Business & Operation Support System，BOSS)是业务运营支撑系统。四个部分：计费及结算系统、营业与账务系统、客户服务系统和决策支持系统  


### Shell学习   
Shell 脚本：shell script   
要有一个能编写代码的文本编辑器和一个能解释执行的脚本解释器 

Linux 的 Shell 种类众多，常见的有：   
- Bourne Shell（/usr/bin/sh或/bin/sh）   
- **Bourne Again Shell**（/bin/bash）   
- C Shell（/usr/bin/csh）   
- K Shell（/usr/bin/ksh）   
- Shell for Root（/sbin/sh）   
#!/bin/sh，它同样也可以改为 #!/bin/bash因为人们并不去区分他们   

##### 编辑第一个Shell脚本 
```
#!/bin/bash
echo "hello world"
```
##### 运行脚本
方法1：
```
chmod +x ./test.sh   #使脚本具有执行权限
./test.sh            #执行脚本
```
执行脚本：linux会先去PATH里面找test.sh 是找不到的，所以用./告诉系统在当前目录里寻找,然后根据脚本开头的注释#! 寻找解释器/bin/bash，而/bin默认在PATH里，所以运行bash的时候，可以直接/bin/sh

方法2：   
```
/bin/sh test.sh      #运行解释器，把脚本文件作为参数传入
```

##### Shell变量
定义变量  
```
your_name='jack'
```
变量名和等号之间不能有空格

也可以这样赋值
```
for file in `ls / etc`
或
for file in $(ls /etc)
```

使用变量用$，赋值不需要加$,echo输出到显示屏
```
your_name="qinjx"
echo $your_name
echo ${your_name}         #{}是为了更好的识别变量的边界，没有歧义的情况下，可以不加
```

只读变量readonly
```
#!/bin/bash
my_name="Wong"
readonly my_name          #转变为只读变量
my_name="lee"             #报错
```
删除变量unset
```
unset my_name             #不能删除readonly变量
```
变量类型 
- 局部变量
- 环境变量

##### Shell 字符串
```
str='this is string'
```
单引号与双引号的区别
- 引号:''不支持插入变量，不支持转义
- 引号:""支持插入变量，支持转义

拼接字符串
```
greeting="hello, "$your_name" !"
greeting='hello, '$your_name' !'               #等同于'hello, ' + '$your_name + ' !'
greeting_1="hello, ${your_name} !"             #${your_name}识别为变量
greeting_3='hello, ${your_name} !'             #${your_name}不被识别，当作字符串
```
获取字符串长度
```
echo ${your_name}
echo ${#your_name}      #输出字符串长度
```

获取字符串皮那段（切片）
```
echo ${your_name:1:4}
```

查找子字符串序号
```
echo `expr index "$string" ho`            #不是单引号，注意ho，表示两个查询，谁先查到就输出谁
```

##### Shell 数组
```
array_name=(value0 value1 value2 value3)        #用空格分割数组的各元素
```
或者格式变一下
```
array_name=(
value0
value1
value2
value3
)
```
赋值操作
```
array_name[0]=value0
array_name[1]=value1
array_name[n]=valuen          #用下标赋值
```

读取数组
```
a=${arry_name[0]}             #这里用{}防止误认为$arry_name ，使用变量一定要$,被赋值的变量不需要
echo ${array_name[@]}         #用@表示全部元素
```
获取数组的长度
```
length=${#array_name[@]}      #获取数组的长度
length=${#array_name[*]}      #等效上一个
lengthn=${#array_name[n]}     #获取单个元素的长度
```

##### Shell注释  
sh里没有多行注释，只能每一行加一个#号

多行注释
```
${array_name[0]=value0
array_name[1]=value1
array_name[n]=valuen}              #用一对花括号括起来，定义成一个函数,不调用它就等于注释了
                    
```
```
:<<EOF                      #第一种
注释内容...
EOF

:<<'                        #第二种
注释内容...
'

:<<!                        #第三种
注释内容...
!
```

##### Shell 传递参数
脚本内部
```
#!/bin/bash
echo "$0"                 #打印本shell脚本名称'./test.sh'
echo "$1"                 #打运行时传入的第一个参数     haha
echo "$2"                 #打运行时传入的第二个参数     xixi
echo "$3"                 #打运行时传入的第三个参数     dada
```
运行时传参
```
./test.sh haha xixi dada
```
脚本里对传参的处理
```
$#    #参数个数
$*    #用一个字符串显示所有参数  "haha xixi dada"
$!    #脚本当前进程id号
$@    #用对应字符串显示所有参数  "hha" "xixi" "dada"
$?    #显示最后命令的退出状态，0表示没有错误
$-    #显示Shell使用的当前选项，与set命令功能相同
```
##### Shell 基本运算符
- 算数运算符
- 关系运算符
- 布尔运算符
- 字符串运算符
- 文件测试运算符
原生bash不支持简单的数学运算，但是可以通过其他命令来实现









