创建文件 HelloWorld.java(文件名需与类名一致)
```
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```
String args[] 与 String[] args 都可以执行，但推荐使用 String[] args，这样可以避免歧义和误读。
```
$ javac HelloWorld.java          #用javac编译文件后面跟着的是java文件的文件全名
$ java HelloWorld                #
Hello World
```

