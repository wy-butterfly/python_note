继承="""
一、
1、子类继承父类，子类就拥有了父类的方法和属性（私有方法和属性除外）

2、普通方法调用
    实例调用的情况：
    1、子类没有重写父类方法：调用父类的方法，方法查找顺序：子类---父类---object
    2、子类有重写父类的方法（优先使用自己的方法）：调用自己的方法，方法查找顺序：子类---父类
    super（）调用的情况：【主要是用来调父类的初始化方法】
    1、子类没有重写父类的方法：调用父类的方法，方法查找顺序：父类
    2、子类有重写父类的方法：调用自己的方法，方法查找顺序：父类
    class Father:
        def car(self):
            print("爸爸的车")
        ...
    class Son(Father):
        super().car() #直接继承父类
        ...
    
    
    
3、重写父类方法
    子类有一个与父类方法名一样的方法，这个就叫重写父类的方法
    
4、调用初始化方法
    1、子类没有写初始化方法
        实例化子类的时候，会自动调用父类的初始化方法
    2、子类重写了初始化方法
        实例化子类的时候，调用的是自己的初始化方法，不会调用父类的初始化方法
    3、父类初始化方法有参数需要传递，但是子类没有初始化方法的时候，在子类初始化的时候要按父类初始化方法的参数进行传递
    4、如果子类和父类都有初始化方法，那么要记得在子类初始化方法中要调用父类的初始化方法


二、多继承 【了解】
多重继承
1、自己有的方法和属性优先用自己的，自己没有的就用父类的，父类没有就用爷爷的，依次往上寻找
    1、一个类继承多个类【不推荐使用】了解
    按继承顺序（从左往右）去对应的父类找方法和属性
        1.继承多个类，属性和方法谁有就执行谁的（方法和属性不重复的情况下）
        2、如果继承多个类，多个父类有相同的方法和属性，按照从左往右的顺序去查找，找到了就执行或者使用
    2、顺序继承
    if __name__ == "__main__":
    cl=C()
    cl.test_01()
    #打印类的继承顺序
    print(C.__mro__)
 
"""

"""
多态【了解】
1、一类事物多种形态
2、一个接口多种实现
class Dog:
    def sleep(self):
        print('狗在睡觉')

class Cat:
    def sleep(self):
        print('猫在睡觉')
        
def animal(obj):
    #实例化传进来的类
    cl = obj()
    cl.sleep()
    
if __name__ == '__main__':
    animal(Dog)
    animal(Cat)
"""

"""
类，类实例都可以设置属性、修改属性、判断属性、删除属性

python反射==动态设置属性【掌握】
class Demo:
    pass
print(Demo.__dict__) #查找类属性
1、设置属性
可以给类设置属性，也可以给类实例设置属性
setattr(object,name,value)【同名会覆盖】
object: 要设置属性的对象
name: 属性的名称
value: 属性的值
2、获取属性
getattr()
如果不设置默认值，当key不存在的时候会报错
3、判断属性
hasattr()
属性存在返回True,否则返回False 
4、删除属性
delattr()

"""

"""
#导入包，获取当前文件目录的路径
import os
os.path.dirname(__file__)
路径处理
1、获取当前执行文件的绝对路径
print(__file__)

2、获取当前执行文件所在目录的绝对路径
my_path = os.path.dirname(__file__)

3、获取指定文件的绝对路径
没有传路径的时候，默认是当前路径下
res = os.path.abspath('demo01.py')

4、路径拼接
res = os.path.abspath(__file__)
print(res)

my_path = os.path.dirname(res)
print(my_path)

result = os.path.dirname(my_path)
print(result)
new_path = os.path.join(result, 'demo','dict.py')
print(new_path)


"""
#路径拼接
"""import os
res = os.path.abspath(__file__)
print(res)

my_path = os.path.dirname(res)
print(my_path)

result = os.path.dirname(my_path)
print(result)
new_path = os.path.join(result, 'demo','dict.py')
print(new_path)
"""


