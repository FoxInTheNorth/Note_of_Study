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

**算术运算符**
```
#!/bin/bash

val=`expr 2 + 2`                #这里用expr表达式 2+2 是不对的，必须写成 2 + 2，用``而不是单引号
echo "两数之和为 : $val"
```
常用运算
```
`expr $a + $b` 
`expr $a - $b` 
`expr $a \* $b`         #这里\*应该是转义？？？
`expr $a / $b` 
`expr $a % $b` 
[ $a == $b ]            #条件表达式
[ $a != $b ]
```
**关系运算符**
```
[ $a -eq $b ]
[ $a -ne $b ]
[ $a -gt $b ]
[ $a -lt $b ]
[ $a -ge $b ]
[ $a -le $b ]
```
**布尔运算符**
```
[ ! false ]
[ 0 -ge 1 -o 1 -ge 0 ]
[ 0 -ge 1 -a 1 -ge 0 ]
```
**逻辑运算符**
```
[[ $a -lt 100 && $b -gt 100 ]] 
[[ $a -lt 100 || $b -gt 100 ]] 
```
**字符串运算符**
```
[ $a = $b ]
[ $a != $b ]
[ -z $a ]     #长度为0
[ -n $a ]     #长度不为0
[ $a ]        #值不为空
```
**文件测试运算符**
文件测试运算符用于检测 Unix 文件的各种属性
```
file="/var/test/test.sh"     #把文件路径赋值给file变量
[ -b $file ]    #是块设备文
[ -c $file ]    #是字符设备文件
[ -d $file ]    #是目录
[ -f $file ]    #是普通文件（既不是目录，也不是设备文件）
[ -g $file ]    #设置了 SGID 位
[ -k $file ]    #设置了粘着位(Sticky Bit)
[ -p $file ]    #是有名管道
[ -u $file ]    #设置了 SUID 位
[ -r $file ]    #可读
[ -w $file ]    #可写
[ -x $file ]    #可执行
[ -s $file ]    #为空（文件大小是否大于0）
[ -e $file ]    #文件（包括目录）是否存在
```

##### Shell echo命令

```
echo 'hello'        #显示普通字符串
echo "hello"
echo hello          #可以省略引号
echo "\"It is a test\""    #双引号支持转义
```

read 命令从标准输入中读取一行,并把输入行的每个字段的值指定给 shell 变量
```
read Str1 Str2                             #read可以读取多个参数
echo "第一个参数:$Str1; 第二个参数:$Str2"
```
上面这个脚本运行
```
./test.sh a b c d      #参数多给，多的会给最后一个变量Str2：b c d 
```
read实例
```
read -p "请输入一段文字:" -n 6 -t 5 -s password
echo -e "\npassword is $password"
运行：
$ sh test.sh 
结果：
请输入一段文字:
password is asdfgh
```

read 命令与shell 变量
```
#!/bin/sh
read name
echo "$name It is a test"
```
运行上面这个shell脚本`./test.sh`   或者`/bin/sh test.sh`
```
OK                     #标准输入
OK It is a test        #输出
```
强制换行
```
echo -e "hello \n"     #-e开启转义    但是\"好像可以自动转义？
echo "world"           #两行之间多一行
```
强制同行
```
echo -e "hello \c"     #-e开启转义   
echo "world"           #两行之间在一行
```
结果定向至文件
```
echo "It is a test" > myfile
```
显示命令执行结果
```
echo `date`            #显示出date的执行结果
```

##### Shell printf 命令
printf与shell
```
$ echo "Hello, Shell"               #自动换行
Hello, Shell
$ printf "Hello, Shell\n"           #手动换行
Hello, Shell
$
```
printf格式化输出
```
printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg            #-表示左对齐，没有则表示右对齐
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234        
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543 
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876
结果：
姓名     性别   体重kg
郭靖     男      66.12
杨过     男      48.65
郭芙     女      47.99
```
更多案例
```
printf "%d %s\n" 1 "abc"
printf '%d %s\n' 1 "abc"      #效果同上
printf %s abcdef              #没有引号也可以
printf %s abc def             #格式对多个传参起作用
printf "%s\n" abc def
printf "%s %s %s\n" a b c d e f g h i j
```
```
printf "%s and %d \n"   #缺参数的情况，%s对应NULL，%d对应0
结果：
 and 0
```
%s %c %d %f都是格式替代符，%c会截取str的第一个字符，比如"abc"，变成"a"
**printf的转义序列**
```
printf "\a "  #警告
$ printf "www.runoob.com \a"
结果：www.runoob.com $ 

printf "\b "  #后退，%b格式指示符控制下的参数字符串中有效
$ printf "a string, no processing:<%b>\n" "A\nB"
结果：
a string, no processing:<A
B>

printf "\c "  #不显示换行符，除非%b中的
printf "\f "  #换页
printf "\n "  #换行
printf "\r "  #回车
printf "\t"   #水平制表符
printf "\v"   #垂直制表符
printf "\\"   #\
printf "ddd"   #1到3位数八进制值的字符。仅在格式字符串中有效
printf "0ddd"   #1到3位数八进制值的字符
```
##### Shell test 命令
**数值测试**
-eq -ne -gt -ge -lt -le
```
num1=100
num2=100
if test $[num1] -eq $[num2]         #[]执行基本的算数运算
then
    echo '两个数相等！'
else
    echo '两个数不相等！'
fi
```
[]的使用
```
#!/bin/bash

a=5
b=6

result=$[a+b]                  # 注意等号两边不能有空格
echo "result 为： $result"
```
**字符串测试**
=  !=	 -z  -n
```
num1="ru1noob"
num2="runoob"
if test $num1 = $num2            #字符串不用[]号
then
    echo '两个字符串相等!'
else
    echo '两个字符串不相等!'
fi
```
**文件测试**
-e -r -w -x -s -d -f -c -b 
``` 
cd /bin                  #进入目录
if test -e ./bash        #指定文件
then
    echo '文件已存在!'
else
    echo '文件不存在!'
fi
```
**逻辑操作符**
与( -a )、或( -o )、非( ! )三个逻辑操作符用于将测试条件连接起来，其优先级为："!"最高，"-a"次之，"-o"最低
```
cd /bin
if test -e ./notFile -o -e ./bash
then
    echo '至少有一个文件存在!'
else
    echo '两个文件都不存在'
fi
```
##### Shell 流程控制
if
```
if condition
then
    command1 
    command2
    ...
    commandN 
fi
```
写成一行
```
if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi
```
if-elseif-else
```
if condition1
then
    command1
elif condition2 
then 
    command2
else
    commandN
fi
```
for
```
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done
```
写成一行
```
for var in item1 item2 ... itemN; do command1; command2… done;
```
