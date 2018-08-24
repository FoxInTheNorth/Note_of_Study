#Numpy内部解除了Python的PIL(全局解释器锁),运算效率极好

import numnpy as np
a = [1,2,3]
b = np.array(a)             #list转化为array

b.size                      #数组元素个数

b.shape                     #数组形状

b.ndim                      #数组元素类型

arrary_one = np.ones([10.10])        #创建10行10列的数值为浮点1的矩阵

arrary_zero = np.zeros([10.10])         创建10行10列的数值为浮点0的矩阵

#从现有的数据创建数组
array(深拷贝)
asarray(浅拷贝)

#Numpy创建随机数组——均匀分布
np.random.rand(10.10)              #创建指定形状的数组(范围在0至1之间)
np.random.uniform(0.100)           #创建指定范围内的一个数
np.random.randint(0.100)           #创建指定范围内的一个整数
