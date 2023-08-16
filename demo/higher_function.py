作用域="""
一、变量的作用域
1、局部变量：定义在函数内部的变量，作用域就是函数内部
2、全局变量：定义在函数外面的变量，作用域就是整个py文件
3、如果全局变量和局部变量同名，在函数内部优先使用局部变量

二、global关键字
1、作用：将局部变量声明为全局变量
2、语法：先声明，再使用
        global num
        num=10
"""

函数="""
一、内置函数
1、print()
2、input()
3、数据类型:int str list tuple set dict
4、type
5、isinstance(判断某个对象是否是指定的数据类型)
6、id
7、sort(修改原始列表)
8、sorted(新成新的列表)
9、计算相关:sum max min len count
10、range
11、random

四、高阶函数
1、zip【掌握】
作用：打包函数
如果两个list元素个数不一样，打包成字典的时候以元素个数较少的为准去创建字典
l1=['a', 'b', 'c', 'd']
l2=[1,2,3]
res=dict(list(zip(l1,l2)))
print(res)

l1=['a', 'b', 'c', 'd']
l2=[1,2,3]
# 在原来的基础上解压。没打包成字典
# res=list(zip(l1,l2))
# print(res)#list嵌套[('a',1),('b',2),('c',3)]
# result=list(zip(*res))
# print(result)

#打包成字典
# dict([('a',1),('b',2),('c',3)])
result=dict(list(zip(l1,l2)))
print(result)
# 解压
# print(list(result.items()))
test_list=list(result.items())
print('这里是字典的key和value组成的元组放在list中：',test_list)
res2=list(zip(*test_list))
print(res2)


2、lambda 函数的参数：返回值
func=lambda x,y:x+y
result=func(1,5)
print(result)

test_list=[[1,33,4],[2,22,6],[5,55,1]]
test_list.sort(key=lambda x : x[0])
print(dict(test_list))

3、enumerate【面试：在有布尔值的地方取索引】
test_list=['a','b','c']
result=dict(list(enumerate(test_list)))
new_dict={}
for key ,val in result.items():
    print(key,val)
    new_dict[val]=key
print(new_dict)
#设置生成的索引值从1开始
res = list(enumerate(test_list,1))
print(res)

4、map()
作用：将一个可迭代对象的数据，传入一个函数进行遍历操作
传统用法
def test01(x):
    return x*2
result n= map(test01,[1,2,3,])

#结合lambda使用
result = list(map(lambad x:x*2,[1,2,3] ))
print(result)

本质：
new_list = []
for i in [1,2,3]:
    result = test01(x=i)
    new_list.append(result)
print(new_list)

"""
#定义函数乘以2
def test01(x):
    return x*2
new_list = []
for i in [1,2,3]:
    result = test01(x=i)
    new_list.append(result)
print(new_list)