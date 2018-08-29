#### 术语名词    
IDC（Internet Data Center)互联网数据中心  
ISP--(Internet Service Provider)互联网服务提供商   
ICP--(Internet Content Provider)互联网内容提供商。ICP证成为网站经营的许可证，经营性网站必须办理ICP证   
CDN--(Content Delivery Network)内容分发网络。CDN的关键技术主要有内容存储和分发技术  
LVS--(Linux Virtual Server)Linux虚拟服务器。LVS集群采用IP负载均衡技术和基于内容请求分发技术  
CGI--(Common Gateway Interface)通用网关接口  
GSLB--(Global Server Load Balance）全局负载均衡。 CDN 系统架构中最核心的部分，基于DNS的GSLB正是在返回DNS解析结果的过程中进行智能决策，给用户返回一个最佳的服务IP  
BOSS--(Business & Operation Support System，BOSS)是业务运营支撑系统。四个部分：计费及结算系统、营业与账务系统、客户服务系统和决策支持系统  


#### Shell   
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
./test.sh   #执行脚本
```
执行脚本：linux会先去PATH里面找test.sh 是找不到的，所以用./告诉系统在当前目录里寻找，而/bin默认在PATH里，所以运行bash的时候，可以直接/bin/sh

方法2：
`/bin/sh    #运行解释器，把脚本文件作为参数传入`










