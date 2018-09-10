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
