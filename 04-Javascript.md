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












