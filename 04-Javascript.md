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

#### 变量
```
var x, length    #使用关键字 var 来定义变量
x = 5
length = 6
```
在指令式语言中，变量通常是可变的。字面量是一个恒定的值

#### 操作符
