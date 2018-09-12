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
#### let变量
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

#### 变量作用域
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
