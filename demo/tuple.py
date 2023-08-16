元组='''
一、特性
1、元素可以重复
2、可以通过索引获取
3、元组本身不可修改
4、当元组只有一个元素的时候要加一个逗号
5、元素的数据类型可以不一致

二、创建
test_tuple=(1,"a")
test_tuple=(1,)

三、查询
1、通过索引取值
test_tuple[1]
2、查询长度
len(test_tuple)
3、切片
同字符串和列表

四、可变与不可变
1、不可变，元组本身不支持修改
2、可变：元组里边嵌套了可变的数据类型（list)

五、支持各种嵌套
test_tuple=[(),(),[],"python",123]

'''



'set不能重复'

# test_str="alec"
# test_str=(list(test_str))
# print(test_str)
# new_str="".join(test_str)
# print(new_str)

# test_dict=[('user','root'),('x',2),('c',3),('w',0),('q',4)]
# result=sorted(test_dict,key=lambda x:x[0],reverse=True)
# print(result)
#
# num=3
# while num<10:
#     print(f"num={num}")
#     num=num+1

print((list(range(4))))

print("="*3)