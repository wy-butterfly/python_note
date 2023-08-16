列表_容器类型="""  (容器类型：列表、元组、字典
一、特征
1、可变数据类型（可修改）
2、有序（索引从0开始）
3、元素可以重复
4、元素类型没有限制 
5、可迭代

二、创建列表
test_lisr=['a','b','c']
#求1—100的和
print(sum([i for i in range(1,100)]))
列表推导式：[i for i in range(1,100)]

三、访问（查询）
1、通过索引访问
test_list[0]
2、通过元素获取索引值
test_list.index("b")
3.查看列表的长度
len()
4、查看数据类型
type(obj)
5、切片
    1、切片同字符串
    2、倒序不一样（因为列表中可以嵌套其它数据类型，倒序时嵌套数据类型里面的元素不会倒序）
    
四、修改
1、通过索引修改值
test_list[0]='aaa'
2、添加新的元素
test_list.append("py52")
3、在某个位置（索引位置）插入元素
test_list.insert(1,"py52")
4、合并
将l2的元素通过追加的方式添加到l1
l1=[1,2,3]
l2=[4,5,6]
l2.extend(l1)
print(l1)
print(l2)
生成新的列表，不修改原有列表
l3=l1+l2

五、删除【不用】
1、删除对应索引的值，无返回
del test_list[-1]
2、删除对应索引的值，返回被删除的元素
res=test_list.pop(-1)
3、删除元素（通过元素本身），删除找到的第一个匹配的值
test_list.remove(value)
4、清空list
test_list.cleat()

六、其他操作
1、成员运算【返回布尔值】
    in:存在，是某某的成员
    not in:不存在，不是某某的成员
test_list=['a','b','c',1212,123,'a',['a','b',[1,2,3]]]
print('abbb' in test_list)

七、排序
原理：通过ascii码 大小拍序
1、获取对应字符的ascii码
ord("h")
2、通过ascii码获取对应的字符
chr(104)
3、在原列表基础上排序
test_list.sort(reverse=Ture)  【点运算来调用的对应的方法（不生成对应的方法）】
key:用于嵌套列表排序，排序的依据
reverse:默认是False升序，True:降序
4、排序后生成新的列表，不修改原来的列表
new_list=sorted(test_list,reverse=True)       （这种方式叫做方法）【通过这种方法（生成新的列表）】
key:用于嵌套列表排序，排序的依据
reverse:默认是False升序，True:降序

八、其他方法
1、求最值
result=max(test_list)
result=min(test_list)
result=len(test_list)
result=sum(test_list)

"""



import random #随机数
round #四舍五入(不太准确）

result=(list(map(lambda x:x*2,[1,2,3])))
print(result)

def test01(x):
    return x*2

result=map(test01,[1,2,3])
print(list(result))

new_list=[]
for i in [1,2,3]:
    result=test01(x=i)
    new_list.append(result)
print(new_list)





