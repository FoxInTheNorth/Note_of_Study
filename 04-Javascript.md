#### JavaScript 用法 
JavaScript 是一种轻量级的编程语言  
ECMA-262 是 JavaScript 标准的官方名称


##### 直接写入 HTML 输出流
```
<script>
document.write("<h1>这是一个标题</h1>");         #<h1>这是一个标题</h1>同html一起渲染
document.write("<p>这是一个段落。</p>");
</script>
```
##### 对事件的反应
```
<button type="button" onclick="alert('欢迎!')">点我!</button>
```
##### 改变 HTML 内容
```
<script>
function myFunction()
{
	x=document.getElementById("demo");  // 找到元素
	x.innerHTML="Hello JavaScript!";    // 改变内容
}
</script>
<button type="button" onclick="myFunction()">点击这里</button>
```
##### 改变 HTML 图像
```
<script>
function changeImage()
{
    element=document.getElementById('myimage')
    if (element.src.match("bulbon"))            #检索 element 里面 src 属性的值有没有包含 bulbon 这个字符串
    {
        element.src="/images/pic_bulboff.gif";
    }
    else
    {
        element.src="/images/pic_bulbon.gif";
    }
}
</script>
<img id="myimage" onclick="changeImage()" src="/images/pic_bulboff.gif" width="100" height="180">
```
更简洁的三目运算
```
<script>
function changeImage(){
	var s = document.getElementById('myimage');
	s.src = s.src.match('bulboff')?"/images/pic_bulbon.gif":"/images/pic_bulboff.gif";
}
</script>
<img id="myimage" onclick="changeImage()" src="/images/pic_bulboff.gif" width="100" height="180">

```
##### 改变 HTML 样式
```
x=document.getElementById("demo")  //找到元素 
x.style.color="#ff0000";           //改变样式
```
##### 验证输入
```
if isNaN(x) {
    alert("不是数字");
}
```
如果输入的空格，或者连续空格 isNaN 是判别不出来的。可以添加正则来判断
```
if(isNaN(x)||x.replace(/(^\s*)|(\s*$)/g,"")==""){
    alert("不是数字");
}
```
以前可能会写成 <script type="text/javascript"> 
现在直接 <script> 就可以了。JavaScript 是所有现代浏览器以及 HTML5 中的默认脚本语言

##### 位置
通常的做法是把函数放入 <head> 部分中，或者放在页面底部。这样就可以把它们安置到同一处位置，不会干扰页面的内容  
也可以外置 script
```
<body>
<script src="myScript.js"></script>        #外部脚本不能包含 <script> 标签
</body>
```

#### JavaScript 输出
##### 显示数据
- window.alert() 弹出警告框。
- document.write() 将内容写到 HTML 文档中。      #如果在文档已完成加载后执行 document.write，整个 HTML 页面将被覆盖
- innerHTML 写入到 HTML 元素。
- console.log() 写入到浏览器的控制台

```
window.alert(5 + 6)
document.write("段落已修改")
document.write(date())           #调用日期函数        
document.getElementById("demo").innerHTML = "段落已修改。"

a = 5;
b = 6;
c = a + b;
console.log(c)
```

#### JavaScript 语法
##### 字面量   
在编程语言中，一般固定值称为字面量  
- 数字（Number）字面量  可以是整数或者是小数，或者是科学计数(e)
- 字符串（String）字面量  可以使用单引号或双引号:
- 表达式字面量 用于计算
- 数组（Array）字面量  定义一个数组
- 对象（Object）字面量 定义一个对象（如json）
- 函数（Function）字面量 定义一个函数
##### 数据类型
```
var length = 16;                                  // Number 通过数字字面量赋值 
var points = x * 10;                              // Number 通过表达式字面量赋值
var lastName = "Johnson";                         // String 通过字符串字面量赋值
var cars = ["Saab", "Volvo", "BMW"];              // Array  通过数组字面量赋值
var person = {firstName:"John", lastName:"Doe"};  // Object 通过对象字面量赋值
```
##### 变量
```
var x, length    #使用关键字 var 来定义变量
x = 5
length = 6
```
在指令式语言中，变量通常是可变的。字面量是一个恒定的值

##### 操作符
- 赋值，算术和位运算符	=  +  -  *  /	在 JS 运算符中描述
- 条件，比较及逻辑运算符	==  != <  > 	在 JS 比较运算符中描述

##### 关键字与注释
语句是用分号分隔
```
var y = x * 10;
```
JavaScript 关键字必须以字母、下划线（_）或美元符（$）开始

##### 函数
```
function myFunction(a, b) {
   	return a * b;                                // 返回 a 乘以 b 的结果
}
```

javascript字母大小写
javaScript 使用 Unicode 字符集
JavaScript 中，常见的是驼峰法的命名规则

#### JavaScript 语句
通常我们在每条可执行的语句结尾添加分号。
```
var y = x * 10;
```
使用分号的另一用处是在一行中编写多条语句。
```
var y = x * 10;var m 
```

##### 代码块
代码块以左花括号开始，以右花括号结束。
代码块的作用是一并地执行语句序列
函数中常见

##### 语句标识符
JavaScript 语句通常以一个 语句标识符 为开始，并执行该语句
```
break	
catch	语句块，在 try 语句块执行出错时执行 catch 语句块。
continue	跳过循环中的一个迭代。
do ... while	执行一个语句块，在条件语句为 true 时继续执行该语句块。
for	在条件语句为 true 时，可以将代码块执行指定的次数。
for ... in	
function	定义一个函数
if ... else	
return	
switch	用于基于不同的条件来执行不同的动作。
throw	抛出（生成）错误 。
try	实现错误处理，与 catch 一同使用。
var	
while	
```
##### 对代码行进行折行
```
document.write("你好 \
世界!");

document.write \       #但是这样不行
("你好世界!");
```
#### JavaScript 注释
##### 多行注释
以 /* 开始，以 */ 结尾。

#### 应用注释符号验证浏览器是否支持 JavaScript 脚本功能
```
<script>
<!--                                                    #HTML提供的注释符号进行验证,不支持javascrip的会被注释掉
document.write("您的浏览器支持JavaScript脚本!");          #支持的会读取，用//避免 JavaScript 执行 --> 标签
//-->
</script>
```

#### JavaScript 变量
- 变量必须以字母开头
- 变量也能以 $ 和 _ 符号开头（不过我们不推荐这么做）
- 变量名称对大小写敏感（y 和 Y 是不同的变量）
```
var carname;  #声明一个变量，为空值undefined
````
一条语句，多个变量
```
var lastname="Doe", age=30, job="carpenter";
```
也可以分行
```
var lastname="Doe",
age=30,
job="carpenter";
```
但是这样不行
```
var x,y,z=1;    #x,y 为 undefined， z 为 1
```
重新声明变量不会丢失值
```
var carname="Volvo"; 
var carname;              #还是"Volvo"  
```
##### let变量
let允许你声明一个作用域被限制在块级中的变量、语句或者表达式。在Function中局部变量推荐使用let变量，避免变量名冲突
let 声明的变量只在其声明的块或子块中可用  
var 声明的变量的作用域是整个封闭函数
```
function varTest() {
    var x = 1;
    if (true) {
        var x = 2;       // 同样的变量!
        console.log(x);  // 2
    }
    console.log(x);  // 2
}

function letTest() {
    let x = 1;
    if (true) {
        let x = 2;       // 不同的变量    
        console.log(x);  // 2  
    }
    console.log(x);  // 1
}
```

##### 变量作用域
Javascript声明变量的时候，虽然用var关键字声明和不用关键字声明，很多时候运行并没有问题，但是这两种方式还是有区别的
```
// num1为全局变量，num2为window的一个属性      #????????
var num1 = 1;
num2 = 2;
// delete num1;  无法删除
// delete num2;  删除
function model(){
var num1 = 1; // 本地变量
num2 = 2;     // window的属性
    // 匿名函数
    (function(){
        var num = 1; // 本地变量
        num1 = 2; // 继承作用域（闭包）
        num3 = 3; // window的属性
    }())
}
```
#### JavaScript 数据类型
字符串（String）、数字(Number)、布尔(Boolean)、数组(Array)、对象(Object)、空（Null）、未定义（Undefined）

##### 动态类型
相同的变量可用作不同的类型

##### 字符串
...
##### 数字
只有一种数字类型。数字可以带小数点，也可以不带
```
var x1=34.00;      //使用小数点来写
var x2=34;         //不使用小数点来写
```
极大或极小的数字可以通过科学（指数）计数法来书写
```
var y=123e5;      // 12300000
var z=123e-5;     // 0.00123
```

##### 布尔
```
var x=true;
var y=false;      #首字母小写，python首字母大写
```
##### 数组
```
var cars=new Array();
cars[0]="Saab";                
cars[1]="Volvo";
cars[2]="BMW";
```
或者(condensed array):
```
var cars=new Array("Saab","Volvo","BMW");
```
或者 (literal array):
```
var cars=["Saab","Volvo","BMW"];
```
##### java对象       
对象由花括号分隔。在括号内部，对象的属性以名称和值对的形式 (name : value) 来定义。属性由逗号分隔，有点像python dict
```
var person={firstname:"John", lastname:"Doe", id:5566};   #有三个属性
```
查找
```
name=person.lastname;        
name=person["lastname"];
```

##### Undefined 和 Null
可以通过将变量的值设置为 null 来清空变量
```
cars=null;
person=null;
```
##### 声明变量类型
声明新变量时，可以使用关键词 "new" 来声明其类型
```
var carname=new String;
var x=      new Number;
var y=      new Boolean;
var cars=   new Array;
var person= new Object;
```
#### JavaScript 对象
键值对在 JavaScript 对象通常称为 对象属性

##### 访问对象属性
两种方式访问对象属性
```
person.lastName;
person["lastName"];
```
##### 对象方法
对象方法通过添加 () 调用 (作为一个函数)
```
var person = {
    firstName: "John",
    lastName : "Doe",
    id : 5566,
    fullName : function() 
	{
       return this.firstName + " " + this.lastName;
    }
};
```
对上述对象操作
```
name = person.fullName;     #结果：function() { return this.firstName + " " + this.lastName; }

name = person.fullName();   #结果John Doe
```
#### JavaScript 函数
函数就是包裹在花括号中的代码块，前面使用了关键词 function：
```
function functionname()
{
执行代码
}
```
##### 传参
您可以发送任意多的参数，由逗号 (,) 分隔：
```
myFunction(argument1,argument2)

```
声明函数时，请把参数作为变量来声明
```
function myFunction(var1,var2)
{
代码
}
```
实例
```
<p>点击这个按钮，来调用带参数的函数。</p>
<button onclick="myFunction('Harry Potter','Wizard')">点击这里</button>
<script>
function myFunction(name,job){
    alert("Welcome " + name + ", the " + job);
}
</script>
```
##### 带有返回值的函数``
```
function myFunction()
{
    var x=5;
    return x;
}
```
函数调用将被返回值取代
```
var myVar=myFunction();
document.getElementById("demo").innerHTML=myFunction();
```
return退出函数
```
function myFunction(a,b)       
{
    if (a>b)       #如果 a 大于 b，则上面的代码将退出函数，并不会计算 a 和 b 的总和
    {
        return;
    }
    x=a+b
}
```

##### 向未声明的 JavaScript 变量分配值
如果您把值赋给尚未声明的变量，该变量将被自动作为 window 的一个属性。 并不是windows
```
carname="Volvo";
```
非严格模式下给未声明变量赋值创建的全局变量，是全局对象的可配置属性，可以删除。
```
var var1 = 1; // 不可配置全局属性
var2 = 2; // 没有使用 var 声明，可配置全局属性

console.log(this.var1); // 1
console.log(window.var1); // 1

delete var1; // false 无法删除
console.log(var1); //1

delete var2; 
console.log(delete var2); // true
console.log(var2); // 已经删除 报错变量未定义
```
##### JavaScript 变量的全局属性
？？？？？

#### JavaScript 作用域
作用域为可访问变量，对象，函数的集合  
##### 局部作用域
变量在函数内声明，变量为局部作用域
```
// 此处不能调用 carName 变量
function myFunction() {
    var carName = "Volvo";
    // 函数内可调用 carName 变量
}
```
因为局部变量只作用于函数内，所以不同的函数可以使用相同名称的变量

##### 全局作用域
全局变量有 全局作用域
```
var carName = " Volvo";
// 此处可调用 carName 变量
function myFunction() {
    // 函数内可调用 carName 变量
}
```
如果变量在函数内没有声明（没有使用 var 关键字），该变量为全局变量    

```
// 此处可调用 carName 变量
 
function myFunction() {
    carName = "Volvo";
    // 此处可调用 carName 变量
}
```

##### JavaScript 变量生命周期 
局部变量在函数执行完毕后销毁   
全局变量在页面关闭后销毁

##### HTML 中的全局变量  
在 HTML 中, 全局变量是 window 对象: 所有数据变量都属于 window 对象
```
全局变量，或者函数，可以覆盖 window 对象的变量或者函数  
局部变量，包括 window 对象可以覆盖全局变量和函数
```

#### JavaScript 事件
常见的HTML事件
```
onchange      HTML 元素改变
onclick       用户点击 HTML 元素
onmouseover   用户在一个HTML元素上移动鼠标
onmouseout    用户从一个HTML元素上移开鼠标
onkeydown     用户按下键盘按键
onload        浏览器已完成页面的加载
```

HTML 元素中可以添加事件属性，使用 JavaScript 代码来添加 HTML 元素。 
```
<some-HTML-element some-event='JavaScript 代码'>
<some-HTML-element some-event="JavaScript 代码">
```
```
<button onclick="getElementById('demo').innerHTML=Date()">现在的时间是?</button>       
<button onclick="this.innerHTML=Date()">现在的时间是?</button>               #修改自身button元素显示的文字
```

#### JavaScript 字符串
##### 特殊字符
```
\'	单引号
\"	双引号
\\	反斜杠
\n	换行
\r	回车
\t	tab(制表符)
\b	退格符
\f	换页符
```

##### 字符串可以是对象
通常JavaScript 字符串是原始值（原始值字符串），可以使用字符创建： var firstName = "John"   
但我们也可以使用 new 关键字将字符串定义为一个对象（对象字符串）： var firstName = new String("John")
```
var x = "John";
var y = new String("John");
typeof x // 返回 String
typeof y // 返回 Object
```
不要创建 String 对象。它会拖慢执行速度，并可能产生其他副作用
```
var x = "John";              
var y = new String("John");
(x === y) // 结果为 false，因为 x 是字符串，y 是对象
```
=== 为绝对相等，即数据类型与值都必须相等。

##### 字符串属性和方法
原始值字符串，如 "John", 没有属性和方法(因为他们不是对象)。
原始值可以使用 JavaScript 的属性和方法，因为 JavaScript 在执行方法和属性时可以把原始值当作对象
**属性**
```
constructor	返回创建字符串属性的函数
length	返回字符串的长度
prototype	允许您向对象添加属性和方法
```
**方法**
```
charAt()	返回指定索引位置的字符
charCodeAt()	返回指定索引位置字符的 Unicode 值
concat()	连接两个或多个字符串，返回连接后的字符串
fromCharCode()	将 Unicode 转换为字符串
indexOf()	返回字符串中检索指定字符第一次出现的位置
lastIndexOf()	返回字符串中检索指定字符最后一次出现的位置
localeCompare()	用本地特定的顺序来比较两个字符串
match()	找到一个或多个正则表达式的匹配
replace()	替换与正则表达式匹配的子串
search()	检索与正则表达式相匹配的值
slice()	提取字符串的片断，并在新的字符串中返回被提取的部分
split()	把字符串分割为子字符串数组
substr()	从起始索引号提取字符串中指定数目的字符
substring()	提取字符串中两个指定的索引号之间的字符
toLocaleLowerCase()	根据主机的语言环境把字符串转换为小写，只有几种语言（如土耳其语）具有地方特有的大小写映射
toLocaleUpperCase()	根据主机的语言环境把字符串转换为大写，只有几种语言（如土耳其语）具有地方特有的大小写映射
toLowerCase()	把字符串转换为小写
toString()	返回字符串对象值
toUpperCase()	把字符串转换为大写
trim()	移除字符串首尾空白
valueOf()	返回某个字符串对象的原始值
```
#### JavaScript 运算符
##### 算术运算符
y=5
```
+	加法	   x=y+2	7	5	
-	减法	   x=y-2	3	5	
*	乘法	   x=y*2	10	5	
/	除法	   x=y/2	2.5	5	
%	取模（余数）	x=y%2	     1	     5	
++	自增	   x=++y	6	6	 #++y先自增后赋值
                     x=y++	  5	  6	   #y++先赋值后自增
--	自减	   x=--y	4	4	
                     x=y--	  5	  4
```

##### 赋值运算符
x=10 和 y=5
```
=	x=y	 	x=5	 
+=	x+=y	x=x+y	x=15	 
-=	x-=y	x=x-y	x=5	 
*=	x*=y	x=x*y	x=50	 
/=	x/=y	x=x/y	x=2	 
%=	x%=y	x=x%y	x=0
```

##### 用于字符串的 + 运算符
```
txt1="What a very";
txt2="nice day";
txt3=txt1+txt2;             #What a verynice day
```
把空格插入一个字符串之中
```
txt1="What a very ";
txt2="nice day";
txt3=txt1+txt2;             #What a very nice day
```
把空格插入表达式中
```
txt1="What a very";
txt2="nice day";
txt3=txt1+" "+txt2;             #What a very nice day
```
##### 对字符串和数字进行加法运算
如果把数字与字符串相加，结果将成为字符串！
```
x=5+5;
y="5"+5;
z="Hello"+5;
```

##### 逻辑运算符
逻辑运算符用于测定变量或值之间的逻辑。
给定 x=6 以及 y=3
```
&&	and	(x < 10 && y > 1) 为 true
||	or	(x==5 || y==5) 为 false
!	not	!(x==y) 为 true
```
##### 条件运算符
基于某些条件对变量进行赋值
```
voteable=(age<18)?"年龄太小":"年龄已达到";   #如果变量 age 中的值小于 18，则向变量 voteable 赋值 "年龄太小"，否则赋值 "年龄已达到"

```
#### JavaScript if...Else 语句
##### if 语句
```
if (time<20)
{
    x="Good day";
}
```

##### if...else 语句
```
if (time<20)
{
    x="Good day";
}
else
{
    x="Good evening";
}

```

##### if...else if...else 语句
```
if (time<10)
{
    document.write("<b>早上好</b>");
}
else if (time>=10 && time<16)
{
    document.write("<b>今天好</b>");
}
else
{
    document.write("<b>晚上好!</b>");
}
```
#### JavaScript switch 语句
switch 语句来选择要执行的多个代码块之一
```
var d=new Date().getDay(); 
switch (d) 
{ 
  case 0:x="今天是星期日"; 
  break; 
  case 1:x="今天是星期一"; 
  break; 
  case 2:x="今天是星期二"; 
  break; 
  case 3:x="今天是星期三"; 
  break; 
  case 4:x="今天是星期四"; 
  break; 
  case 5:x="今天是星期五"; 
  break; 
  case 6:x="今天是星期六"; 
  break; 
}
```

##### default 关键词
请使用 default 关键词来规定匹配不存在时做的事情
```
var d=new Date().getDay();
switch (d)
{
    case 6:x="今天是星期六";
    break;
    case 0:x="今天是星期日";
    break;
    default:
    x="期待周末";
}
document.getElementById("demo").innerHTML=x;b
```
#### JavaScript for 循环
```
for (var i=0;i<cars.length;i++)
{ 
    document.write(cars[i] + "<br>");
}
```
##### 不同类型的循环
- for - 循环代码块一定的次数
- for/in - 循环遍历对象的属性
- while - 当指定的条件为 true 时循环指定的代码块
- do/while - 同样当指定的条件为 true 时循环指定的代码块

**For 循环**
```
for (var i=0; i<5; i++)
{
      x=x + "该数字为 " + i + "<br>";
}
```
开始变量省略写法
```
var i=2,len=cars.length;      #循环体外部已经定义变量
for (; i<len; i++)
{ 
    document.write(cars[i] + "<br>");
}
```
循环条件省略，那么必须在循环内提供 break。否则循环就无法停下来

变量的变化也可以省略
```
var i=0,len=cars.length;
for (; i<len; )
{ 
    document.write(cars[i] + "<br>");
    i++;                     #但是通常内部有相应的代码
}
```
##### For/In 循环
JavaScript for/in 语句循环遍历对象的属性
```
var x;
var txt="";
var person={fname:"John",lname:"Doe",age:25}; 

for (x in person)  // x 为属性名
{
    txt=txt + person[x];
}
```

#### JavaScript while 循环
##### while
```
while (i<5)
{
    x=x + "The number is " + i + "<br>";
    i++;
}
```
##### do/while 循环
```
	var x="",i=0;
	do{
		x=x + "该数字为 " + i + "<br>";
	    i++;
	}
	while (i<5)  
```
##### 比较 for 和 while
```
cars=["BMW","Volvo","Saab","Ford"];
var i=0;
while (cars[i])
{
    document.write(cars[i] + "<br>");
    i++;
}
```
while 和 do/while 的区别 : do/while至少会执行一遍

#### JavaScript Break 和 Continue 语句
##### Break 语句
```
for (i=0;i<10;i++)
{
    if (i==3)
    {
        break;
    }
    x=x + "The number is " + i + "<br>";
}
```
##### Continue 语句
```
for (i=0;i<=10;i++)
{
    if (i==3) continue;                            #该例子跳过了值 3
    x=x + "The number is " + i + "<br>";
}
```
##### JavaScript 标签   
break 和 continue 语句仅仅是能够跳出代码块的语句
continue 语句（带有或不带标签引用）只能用在循环中。
break 语句（不带标签引用），只能用在循环或 switch 中。
通过标签引用，break 语句可用于跳出任何 JavaScript 代码块
```
cars=["BMW","Volvo","Saab","Ford"];
list: 
{
    document.write(cars[0] + "<br>"); 
    document.write(cars[1] + "<br>"); 
    document.write(cars[2] + "<br>"); 
    break list;
    document.write(cars[3] + "<br>"); 
    document.write(cars[4] + "<br>"); 
    document.write(cars[5] + "<br>"); 
}
```
代码块: 基本上是｛｝大括号之间

**默认标签的情况** 
除了默认标签情况，其他时候必须要有名标签
当 break 和 continue 同时用于循环时，没有加标签，此时默认标签为当前"循环"的代码块。
当 break 用于 switch 时，默认标签为当前的 switch 代码块
有名标签的情况 
```
cars=["BMW","Volvo","Saab","Ford"];
list:
{
    document.write(cars[0] + "");
    document.write(cars[1] + "");
    document.write(cars[2] + "");
    break list;
    document.write(cars[3] + "");
    document.write(cars[4] + "");
    document.write(cars[5] + "");
}
```
上述break list;会跳出list的代码块。如果将break换成continue会有惊喜，违反了明确中的第二点，因为list只是个普通代码块，而不是循环。除非list写成如下形式 list:
```
for(var i=0; i<10; ++i)
{
    continue list;
}
```

有了标签，可以使用break和continue在多层循环的时候控制外层循环。
例如下面：
```
outerloop:
for (var i = 0; i < 10; i++)
{
    innerloop:
    for (var j = 0; j < 10; j++)
    {
        if (j > 3)
        {
            break;
        }
        if (i == 2)
        {
            break innerloop;
        }
        if (i == 4)
        {
            break outerloop;
        }
        document.write("i=" + i + " j=" + j + "");
    }
}
```

#### JavaScript typeof、 null、undefined、valueOf()
##### typeof 操作符
检测变量的数据类型 
```
typeof "John"                // 返回 string 
typeof 3.14                  // 返回 number
typeof false                 // 返回 boolean
typeof [1,2,3,4]             // 返回 object
typeof {name:'John', age:34} // 返回 object
```
##### null
null是一个只有一个值的特殊类型。表示一个空对象引用
用 typeof 检测 null 返回是object
你可以设置为 null 来清空对象
```
var person = null;           // 值为 null(空), 但类型为对象
```
你可以设置为 undefined 来清空对象
```
var person = undefined;     // 值为 undefined, 类型为 undefined
```
##### undefined 和 null 的区别
null 和 undefined 的值相等，但类型不等
typeof undefined             // undefined
typeof null                  // object
null === undefined           // false
null == undefined            // true

#### JavaScript 类型转换
Number() 转换为数字， String() 转换为字符串， Boolean() 转化为布尔值
在 JavaScript 中有 5 种不同的数据类型：
- string
- number
- boolean
- object
- function
3 种对象类型：
- Object
- Date
- Array
2 个不包含任何值的数据类型：
- null
- undefined

NaN 的数据类型是 number
数组(Array)的数据类型是 object
日期(Date)的数据类型为 object
null 的数据类型是 object
未定义变量的数据类型为 undefined

如果对象是 JavaScript Array 或 JavaScript Date ，我们就无法通过 typeof 来判断他们的类型，因为都是 返回 Object。

##### constructor 属性
constructor 属性返回所有 JavaScript 变量的构造函数
```
"John".constructor                 // 返回函数 String()  { [native code] }
(3.14).constructor                 // 返回函数 Number()  { [native code] }
false.constructor                  // 返回函数 Boolean() { [native code] }
[1,2,3,4].constructor              // 返回函数 Array()   { [native code] }
{name:'John', age:34}.constructor  // 返回函数 Object()  { [native code] }
new Date().constructor             // 返回函数 Date()    { [native code] }
function () {}.constructor         // 返回函数 Function(){ [native code] }
```
你可以使用 constructor 属性来查看对象是否为数组 (包含字符串 "Array")或者是否为日期 (包含字符串 "Date"):
```
function isArray(myArray) {
    return myArray.constructor.toString().indexOf("Array") > -1;
}

function isDate(myDate) {
    return myDate.constructor.toString().indexOf("Date") > -1;       //？？？？
}
```
##### JavaScript 类型转换
全局方法 String() ，可用于任何类型的数字，字母，变量，表达式
```
String(x)         // 将变量 x 转换为字符串并返回
String(123)       // 将数字 123 转换为字符串并返回
String(100 + 23)  // 将数字表达式转换为字符串并返回
```
Number 方法 toString() 也是有同样的效果
```
x.toString()
(123).toString()
(100 + 23).toString()
```
Number 还包括的一些方法
``` 
toExponential()	把对象的值转换为指数计数法。
toFixed()	把数字转换为字符串，结果的小数点后有指定位数的数字。
toPrecision()	把数字格式化为指定的长度。
```
##### 将布尔值转换为字符串
全局方法 String() 可以将布尔值转换为字符串。
```
String(false)        // 返回 "false"
String(true)         // 返回 "true"
```
Boolean 方法 toString() 也有相同的效果
```
false.toString()     // 返回 "false"
true.toString()      // 返回 "true"
```
##### 将日期转换为字符串
Date() 返回字符串
```
Date()      // 返回 Thu Jul 17 2014 15:38:19 GMT+0200 (W. Europe Daylight Time)
```
全局方法 String() 可以将日期对象转换为字符串
```
String(new Date())      // 返回 Thu Jul 17 2014 15:38:19 GMT+0200 (W. Europe Daylight Time)
```
Date 方法 toString() 也有相同的效果
```
obj = new Date()
obj.toString()   // 返回 Thu Jul 17 2014 15:38:19 GMT+0200 (W. Europe Daylight Time)--
```
更多
```
getDate()	从 Date 对象返回一个月中的某一天 (1 ~ 31)。
getDay()	从 Date 对象返回一周中的某一天 (0 ~ 6)。
getFullYear()	从 Date 对象以四位数字返回年份。
getHours()	返回 Date 对象的小时 (0 ~ 23)。
getMilliseconds()	返回 Date 对象的毫秒(0 ~ 999)。
getMinutes()	返回 Date 对象的分钟 (0 ~ 59)。
getMonth()	从 Date 对象返回月份 (0 ~ 11)。
getSeconds()	返回 Date 对象的秒数 (0 ~ 59)。
getTime()	返回 1970 年 1 月 1 日至今的毫秒数。
```
##### 将字符串转换为数字
全局方法 Number() 可以将字符串转换为数字。
字符串包含数字(如 "3.14") 转换为数字 (如 3.14).
空字符串转换为 0。
其他的字符串会转换为 NaN (不是个数字)
```
Number("3.14")    // 返回 3.14
Number(" ")       // 返回 0 
Number("")        // 返回 0
Number("99 88")   // 返回 NaN
```
更多
```
parseFloat()	解析一个字符串，并返回一个浮点数。
parseInt()	解析一个字符串，并返回一个整数。
```

##### 一元运算符 +
Operator + 可用于将变量转换为数字
```
var y = "5";      // y 是一个字符串
var x = + y;      // x 是一个数字
```
如果变量不能转换，它仍然会是一个数字类型，但值为 NaN (不是一个数字):
```
var y = "John";   // y 是一个字符串
var x = + y;      // x 是一个数字 (NaN)
```
##### 将布尔值转换为数字
全局方法 Number() 可将布尔值转换为数字。
```
Number(false)     // 返回 0
Number(true)      // 返回 1
```
##### 将日期转换为数字
全局方法 Number() 可将日期转换为数字。
```
d = new Date();
Number(d)          // 返回 1404568027739
```
日期方法 getTime() 也有相同的效果。
```
d = new Date();
d.getTime()        // 返回 1404568027739
```
##### 自动转换类型
当 JavaScript 尝试操作一个 "错误" 的数据类型时，会自动转换为 "正确" 的数据类型。
以下输出结果不是你所期望的：
```
5 + null    // 返回 5         null 转换为 0
"5" + null  // 返回"5null"   null 转换为 "null"
"5" + 1     // 返回 "51"      1 转换为 "1"  
"5" - 1     // 返回 4         "5" 转换为 5
```
##### 自动转换为字符串
当你尝试输出一个对象或一个变量时 JavaScript 会自动调用变量的 toString() 方法
```
document.getElementById("demo").innerHTML = myVar;
myVar = {name:"Fjohn"}  // toString 转换为 "[object Object]"
myVar = [1,2,3,4]       // toString 转换为 "1,2,3,4"
myVar = new Date()      // toString 转换为 "Fri Jul 18 2014 09:08:55 GMT+0200"
```
数字和布尔值也经常相互转换
```
myVar = 123             // toString 转换为 "123"
myVar = true            // toString 转换为 "true"
myVar = false           // toString 转换为 "false"
```


一些常用的转化方法
```
原始值		转换为数字		转换为字符串	转换为布尔值
false			0		"false"	false	 
true			1		"true"	true	 
0			0		"0"	false	 
1			1		"1"	true	 
"0"			0		"0"	true	 
"000"			0		"000"	true	 
"1"			1		"1"	true	 
NaN			NaN		"NaN"	false	 
Infinity		Infinity	"Infinity"	true	 
-Infinity		-Infinity	"-Infinity"	true	 
""			0		""	false	 
"20"			20		"20"	true	 
"Runoob"		NaN		"Runoob"	true	 
[ ]			0		""	true	 
[20]			20		"20"	true	 
[10,20]			NaN		"10,20"	true	 
["Runoob"]		NaN		"Runoob"	true	 
["Runoob","Google"]	NaN		"Runoob,Google"	true	 
function(){}		NaN		"function(){}"	true	 
{ }			NaN		"[object Object]"	true	 
null			0		"null"	false	 
undefined		NaN		"undefined"	false
```
注意，null、undefined、 NAN、0、"" 的布尔值为false
     false、"0"、"000"、""、[ ]、null 的数值为0，而{ }的数值为NAN
     
**检测数据类型：typeof 与 instanceof**
typeof 
typeof 用以获取一个变量或者表达式的类型，typeof 一般只能返回如下几个结果：
```
number,boolean,string,function（函数）,object（NULL,数组，对象）,undefined。
```
可以使用 typeof 来获取一个变量是否存在，如 if(typeof a!="undefined"){}，而不要去使用 if(a) 因为如果 a 不存在（未声明）则会出错。

正因为 typeof 遇到 null,数组,对象时都会返回 object 类型，所以当我们要判断一个对象是否是数组时。或者判断某个变量是否是某个对象的实例则要选择使用另一个关键语法 instanceof

可通过 instanceof 操作符来判断对象的具体类型，返回布尔值，如果是指定类型返回 true，否则返回 false
```
arr = [1,2,3];
if(arr instanceof Array){
    document.write("arr 是一个数组");
} else {
    document.write("arr 不是一个数组");
}
```

**undefined 与 null 的区别**

表面上 undefined 与 null 都是什么都没有的意思，但是实际上 undefined 是未定义（就是变量没有初始化），null 是一个变量初始化了，但是什么值都没给，只给了一个空对象；进一步说，undefined 与 null是值相等，类型不相等


#### JavaScript 正则表达式
##### 语法
```
/正则表达式主体/修饰符(可选)
var patt = /runoob/i
```
/runoob/i  是一个正则表达式。
runoob  是一个正则表达式主体 (用于检索)。
i  是一个修饰符 (搜索不区分大小写)

##### 使用字符串方法
在 JavaScript 中，正则表达式通常用于两个字符串方法 : search() 和 replace()
```
var str = "Visit Runoob!"; 
var n = str.search(/Runoob/i);   返回匹配的起始位置6

var str = document.getElementById("demo").innerHTML; 
var txt = str.replace(/microsoft/i,"Runoob");

var str = document.getElementById("demo").innerHTML; 
var txt = str.replace("Microsoft","Runoob");

```
**正则表达式修饰符**
```
修饰符	描述
i	执行对大小写不敏感的匹配。
g	执行全局匹配（查找所有匹配而非在找到第一个匹配后停止）。
m	执行多行匹配。
```
**正则表达式模式**
```
表达式	描述
[abc]	查找方括号之间的任何字符。
[0-9]	查找任何从 0 至 9 的数字。
(x|y)	查找任何以 | 分隔的选项。

元字符	描述
\d	查找数字。
\s	查找空白字符。
\b	匹配单词边界。
\uxxxx	查找以十六进制数 xxxx 规定的 Unicode 字符。

量词	描述
n+	匹配任何包含至少一个 n 的字符串。
n*	匹配任何包含零个或多个 n 的字符串。
n?	匹配任何包含零个或一个 n 的字符串。
```
**使用 RegExp 对象**
RegExp 对象是一个预定义了属性和方法的正则表达式对象

##### 使用 test()
test() 方法用于检测一个字符串是否匹配某个模式，如果字符串中含有匹配的文本，则返回 true，否则返回 false
```
var patt1=new RegExp("e");     //规则用于搜索字符串中的字符 "e"
document.write(patt1.test("The best things in life are free"));   //返回true

var patt = /e/;                //规则用于搜索字符串中的字符 "e"  
patt.test("The best things in life are free!");   

/e/.test("The best things in life are free!")   //合并为一串，不用设置正则表达式的变量
```
##### 使用 exec()
exec() 方法用于检索字符串中的正则表达式的匹配，该函数返回一个数组，其中存放匹配的结果。如果未找到匹配，则返回值为 null。
```
/e/.exec("The best things in life are free!");    //返回的是 e
```

**判断输入是否为数字、字母、下划线组成**
```
function isValid(str) { return /^\w+$/.test(str); }         //定义了一个函数，直接返回一个RegExp对象的调用结果
str = "1234abd__"
document.write(isValid(str));
document.write("<br>");

str2 = "$32343#"
document.write(isValid(str2));
document.write("<br>");
```

**判断字符串是否全部为字母**
```
val = "123456"
var isletter = /^[a-zA-Z]+$/.test(val);
document.write(isletter);
document.write("<br>");

val2 = "asaaa"
var isletter2 = /^[a-zA-Z]+$/.test(val2);
document.write(isletter2);
```
**正则表达式表单验证实例**
```
/*是否带有小数*/
function    isDecimal(strValue )  {  
   var  objRegExp= /^\d+\.\d+$/;
   return  objRegExp.test(strValue);  
}  
/*校验是否中文名称组成 */
function ischina(str) {
    var reg=/^[\u4E00-\u9FA5]{2,4}$/;   /*定义验证表达式*/
    return reg.test(str);     /*进行验证*/
}
/*校验是否全由8位数字组成 */
function isStudentNo(str) {
    var reg=/^[0-9]{8}$/;   /*定义验证表达式*/
    return reg.test(str);     /*进行验证*/
}
/*校验电话码格式 */
function isTelCode(str) {
    var reg= /^((0\d{2,3}-\d{7,8})|(1[3584]\d{9}))$/;
    return reg.test(str);
}
/*校验邮件地址是否合法 */
function IsEmail(str) {
    var reg=/^\w+@[a-zA-Z0-9]{2,10}(?:\.[a-z]{2,4}){1,3}$/;        //  (?:) 匹配组, ?:用於标记该匹配组不应被捕获
    return reg.test(str);                      //例如， ‘industr(?:y|ies) 就是一个比 ‘industry|industries’ 更简略的表达式
}
```

#### JavaScript 错误 - throw、try 和 catch
```
try {
  //在这里运行代码
} catch(err) {
  //在这里处理错误
}
```
throw 语句允许我们创建自定义错误
如果把 throw 与 try 和 catch 一起使用，那么您能够控制程序流，并生成自定义的错误消息
```
function myFunction() {
    var message, x;
    message = document.getElementById("message");
    message.innerHTML = "";
    x = document.getElementById("demo").value;
    try { 
        if(x == "")  throw "值为空";
        if(isNaN(x)) throw "不是数字";
        x = Number(x);
        if(x < 5)    throw "太小";
        if(x > 10)   throw "太大";
    }
    catch(err) {
        message.innerHTML = "错误: " + err;
    }
}
```
**设置断点**
**debugger 关键字**

#### JavaScript 变量提升/函数提升
JavaScript 中，函数及变量的声明都将被提升到函数的最顶部。
JavaScript 中，变量可以在使用后声明，也就是变量可以先使用再声明
```
x = 5; // 变量 x 设置为 5

elem = document.getElementById("demo"); // 查找元素 
elem.innerHTML = x;                     // 在元素中显示 x

var x; // 声明 x
```

##### JavaScript 初始化不会提升
##### 理解 js 的解析机制
遇到 script 标签的话 js 就进行预解析，将变量 var 和 function 声明提升
```
a=5;
show();
var a;
function show(){};
```
预解析
```
function show(){};
var a;
a=5;
show();
```
声明匿名函数，使用匿名函数的方式不存在函数提升，因为函数名称使用变量表示的，只存在变量提升
```
var getName=function(){
  console.log(2);
}

function getName(){
  console.log(1);
}

getName();
//结果为2
```
虽然函数声明和变量声明都会被提升，但是函数会首先被提升，然后才是变量
```
//函数、变量声明提升后
function getName(){    //函数声明提升到顶部
  console.log(1);
}

var getName;    //变量声明提升
getName = function(){    //变量赋值依然保留在原来的位置
  console.log(2);
}

getName();    // 最终输出：2
```
