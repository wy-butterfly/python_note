测开内容 = '''
一、普通函数
def test(x):
    return x*2
t1=test(100)
print(t1)


二、匿名函数
res=lambda x:x*2
t2=res(100)
print(t2)

#lambda实现 [('user', 'root'), ('pwd', '123456'), ('code', '888888')]
result = sorted(test_dict.items(),key=lambda x:x[0],reverse=True)
print(dict(result))

#嵌套list
test_list = [[22,3,33],[10,4,3],[2,1,63]]
new_list = sorted(test_list,key=lambda x:x[2],reverse=True)
print(new_list)
test_list.sort(key=lambda x:x[2])
print(test_list)

'''
控制流 = '''
一、流程
流程概念：做一件事的先后顺序
    学习流程：上课听懂--课后回放+做笔记--写作业
流程分类：顺序结构、选择结构、循环结构

二、顺序结构
1、代码从上往下执行

三、选择结构（只会执行一个语句体）
1、单if语句
num=100
if num==10:
    print('num为100')
2、标准的if--else语句
num=100
if num==100:
    print('num为100')
else:
    print('num不等于100’）

3、复合if--elif---else
num=10
if num==10:
    print('num等于10'）
elif num>10:
    print('num大于10'）
elif num==20
    print('num等于20')
else:
    print('num 小于10）
    
    
四、循环结构
1、可迭代对象
    1、能够通过for循环取值的数据类型
    2、判断是否是可迭代对象，返回布尔值
     test_str = 'python'
     from collections.abc import Iterable
     result = isinstance(test_str, Iterable)
     print(result)
     
2、for循环
    1、可以遍历字符串、列表、元组、字典、集合
    
3、while循环（一定记得设置退出条件，不设置退出条件就是死循环）
    num=0
    while num<10:
        print(f'num={num}')
        num+=1
'''

'''
for while

一、range函数
作用：用于生成一个可迭代对象
语法：range（起始索引值，结束索引值，步长）

二、循环控制关键字
1、contiune:结束本次循环，进入下一轮循环
for i in range(10):
    if i==5
        continue
    print(i)

2、break:退出循环
for i in range(10):
    if i==5
        break
        print(i)
        
三、for循环和while循环的使用场景
1、知道循环次数的时候用for循环
2、不知道循环次数的时候用while循环
import random
num=0
while num<10:
    print('num的值',num)
    n=random.randint(1,10)
    print('随机生成数=：',n)
    num+=n
'''

'''
一、嵌套循环
1、嵌套循环的分类
for + for
for + while
while + while
2、外循环执行一次，内循环执行一遍（例：99乘法表）
'''





#对字典的第一个元素进行降序排列
"""test_dict = {'post': '33161', 'user': 'root', 'pwd': 'test123', 'host': '192.168.1.1'}
result = sorted(test_dict.items(), key=lambda x: x[0], reverse=True)
print(dict(result))"""

#是否是可迭代对象
"""from collections.abc import Iterable
test_str = 'python'
result = isinstance(test_str, Iterable)
print(result)"""

