字典='''
一、特性
1、通过键值对表示元素
2、key不能重复，如果重复了会被覆盖
3、key不能是容器数据类型

二、创建
1、test_dict={'host':'192.168.1.1','post':'33161','user':'root','pwd':'test123'}
res=test_dict.items()
2、dict([('host', '192.168.1.1'), ('post', '33161'), ('user', 'root'), ('pwd', 'test123')])

三、查询
1、通过key去访问
test_dict={'host':'192.168.1.1','post':'33161','user':'root','pwd':'test123'}
host=test_dict['host']
2、get获取不存在的key不会报错，会返回设置的默认值
res=test_dict.get('host1','tesst')
3、获取所有的key，返回的数据类型为(<class 'dict_keys'>)，不能直接获取元素，需要进行数据类型转换
res=test_dict.keys()
4、获取所有的values，返回的数据类型为(<class 'dict_values'>)，不能直接获取元素，需要进行数据类型转换
res=test_dict.values()
5、获取所有的key、value，返回的数据类型为(<class 'dict_items'>)，不能直接获取元素，需要进行数据类型转换
res=test_dict.items()
6、for循环迭代
for k in test_dict.keys():
    print(k)
for v in test_dict.values():
    print(v)
for k,v in test_dict.items():
    print(k,v)
    
四、修改
1、通过key修改值
key存在，修改key对应的value
test_dict['host']='192.168.1.105'
key不存在，相当于添加一个键值对
test_dict['bd']='lemon_test'

2、添加键值对
key不存在，就添加键值对
test_dict.setdefault('bd','lemon_test')
key存在，什么都不做

3、合并字典
test_dict1中key与test_dict2中的key重复，test_dict2中key对应的value会覆盖test_dict1中key对应的value
test_dict1={'host':'192.168.1.1','port':'33061','user':'test_user'}
test_dict2={'user':'root','pwd':'test123}
test_dict1.update(test_dict2)

五、删除
test_dict={'host':'192.168.1.1','post':'33161','user':'root','pwd':'test123'}
1、删除键值对
del test_dict['host']
2、删除键值对，返回key对应的value
res=test_dict.pop('post')
3、删除最后一个进栈的
Python进栈的原则：先进先出，测开内容
res2=test_dict.popitem()

六、字典排序
（一）使用场景
数据加密传输，鉴权
敏感信息做加密传输

PSA非对称加密
内部系统前后端交互
1、字典序，a--z
2、拿公钥进行加密，得到密串
3、传输的时候你只要传密串传过去
4、后端拿到你的数据，通过私钥解密
请求参数：{"user":"root","pwd":"123456","code":"888888"}
实际传给后端的参数：实际传给后端的参数：{"user":"root","pwd":"123456","code":"888888",
"sign":"hP7xEyAGRu/MZjKncRLDzkIo39J6fcWmnKtjhrMVZxTlbWmoqZ"}

鉴权
接口对外部公司开放
1、字典序，a--z
2、拿到这个排序后的字典去签名（公钥），得到签名的串
3、传输的时候，
请求参数：{"user":"root","pwd":"123456","code":"888888"}
实际传给后端的参数：实际传给后端的参数：{"user":"root","pwd":"123456","code":"888888",
"sign":"hP7xEyAGRu/MZjKncRLDzkIo39J6fcWmnKtjhrMVZxTlbWmoqZ"}

（二）怎么排序
result = sorted(test_dict.items(),key=operator.itemgetter(1))
operator.itemgetter(1)
0: 根据key排序
1: 根据value排序
import operator
result = sorted(test_dict.items(),key=operator.itemgetter(0),reverse=True)
print(dict(result))

'''


数据类型转换='''
1、int<==>str
2、list<==>tuple
3、list<==>set
4、tuple<==>set
list<==>tuple<==>set 3个类型可以相互转换，当转换成set时，重复的值会被去重

二、不能直接相互转换（样子是会变化的）
1、str==>tuple
2、str==>list
3、str==>set
需要转换回去可以使用''.join(test_list)



'''
# test_dict={'post':'33161','user':'root','pwd':'test123','host':'192.168.1.1'}
# del test_dict['host']
# print(test_dict)
# res=test_dict.pop('post')
# print(res)
# print(test_dict)
# import operator
# result=sorted(test_dict.items(),key=operator.itemgetter(1))
# operator.itemgetter(1)
# print(result)
# 0:根据key排序
# 1：根据value排序

# result=sorted(test_dict.items(),key=operator.itemgtter(0),reverse=True))
# print(dict(result))

# test_str='user','root', 'pwd','test123', 'post','33161', 'host','192.168.1.1'
# test_list=list(test_str)
# print(test_list)
test_list=['user', 'root', 'pwd', 'test123', 'post', '33161', 'host', '192.168.1.1']
set=''.join(test_list)
new_str=(str(set))
print(new_str)