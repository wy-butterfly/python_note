函数执行入口 = """
if __name__ == '__main__':
1、执行当前文件，if __name__ == '__main__':条件成立，会执行if下面的代码块
2、将当前文件导入到其他模块执行，if __name__ == '__main__':条件不成立，不会执行if 下面的代码块

"""

类和对象 = """
一、什么是类
1、有相同属性和行为的一类事物的统称（抽象概念）
class Demo:
    #类属性
    name = "老王"
    age = "20"
    #行为
    def test_01(self):
        pass
类的特性
    封装：代码内部实现不让调用者知道，不暴露出来，只提供某些功能
二、对象
1、对象是类对应的具体的东西（具体的概念）
class car:
    # 初始化方法
    def __init__(self,name,color):
    #车子的属性，实例属性
    self.name = name 
    self.color = color
    
    #行为1
    def test_01(self):
        print(self.name,"车子开走了")
        
    #行为2
    def test_02(self):
        print(self.name,"车子刹车了")
    
    #行为3
    def test_03(self):
        print(self.name,"车子按喇叭")

#宝马 红色的
#类实例
car = Car(name="宝马x6",color="red")
#类实例
car = Car(name="保时捷",color="blue")
"""

"""
一、定义类
1、语法
class Demo:
    pass
2、self是什么
    self就是类实例
3、__init__()初始化方法（魔术方法）
    执行时间:在类实例化的时候自动执行，不需要调用
    
二、类属性
拓展：http://testingpai.com/article/16226334899176
1、定义:定义在类里面，在方法外面
2、调用：
    在类外面：实例.属性名称         类名称.属性名称
    在类里面：实例==self.属性名称   类名称.属性名称
3、特性
    1、可以直接通过类访问，不需要实例化类
    2、可修改的，根据数据类型而定（可变数据类型可修改，不可变数据类型不可修改）
"""

"""
Dome:类
Dome():类实例
三、实例属性
1、定义：写在类的初始化方法中的变量，命名要以self.开头
2、初始化方法def __init__()
    1、执行时间：在类实例化之后自动执行
    2、参数：初始化方法的参数，要在类实例化的时候传进去
3、特性
    1、定义实例属性的时候一定要加上self.作用域是整个类都可以使用
    2、定义实例属性的时候不加self.作用域只是在__init__方法内使用
4、调用
    1、只能通过实例调用：实例.属性名   self(==类实例).属性名
    2、类不能调用实例属性
"""

"""
类访问类属性，类实例访问所有属性
双下划线开头的属性就叫私有属性
私有属性就是作用域改变了，只能在类的内部访问，不能再类外面访问

一、私有属性
1、定义：双下划线开头的属性就叫私有属性
2、特性
    1、作用域改变了，只能在类的内部访问，不能在类的外面访问
3、强行访问【不能进行强行访问】
print(Demo.clolr)
print(Demo._Demo__name)
print("实例的所有属性:",cl.__dict__)
print(cl._Demo__age)

二、私有方法
1、定义的时候以双下划线开头的方法，叫私有方法
2、使用：作为对外调用方法的辅助方法，不希望被外部调用的时候就定义为私有方法
3、私有方法作用域：只能在类的内部被使用（不要去强制访问）
4、实例方法、类方法、静态方法都可以定义为私有方法
5、一个下划线定义的方法和属性实际上可以直接使用，但是不建议使用

"""

"""
一、实例方法
创建：定义在类里面，第一参数默认接收类实例，一般情况下用self表示
特性：只能被实例调用
调用：实例.方法名称（）
使用场景：你的方法里面如果需要用到实例属性/类属性/实例方法就定义为【实例方法】
属性和方使用：实例方法可以使用所有的属性和方法

二、类方法
创建：使用@classmethod修饰的方法就叫类方法，第一个参数默认用来接收类本身，一般用cls代替
特性：无法使用实例属性+实例方法
     不需要实例化可以直接通过类.方法名称（）调用
调用：类.方法名称（）   类实例.方法名称（）
使用场景：如果你不需要使用实例属性和实例方法，就适合定义一个类方法
属性和方法使用：类可以使用类方法和类属性，类不能使用实例属性和实例方法
"""

"""
静态方法
一、创建
1、静态方法定义通过@staticmethod修饰的普通函数，没有默认传递的参数(self,cls都不需要)

二、特性
1、不需要实例化类，直接通过类调用，实例也可以调用
2、不能直接使用类实例相关的方法和属性，也不能直接使用类相关的方法和属性

三、调用
1、类调用静态方法：类名称.方法名称()
2、实例调用静态方法：类名称().方法名称()

四、使用场景
1、当你在定义一个方法的时候，你方法内部不需要使用实例的方法和属性又不需要使用类的方法和属性，
那就适合定义一个静态方法
"""

"""
类实例调用所有的方法和属性
总结：
一、实例方法
1、创建：
class Demo1:
    def test_01(self):
        print("实例方法")
2、调用：
class Demo1:
    def test_01(self):
        print("实例方法1")
    def test_01(self):
        print("实例方法2")   
        self.test_01()
cl = Demo1
cl.test_02
3、属性/方法调用：
class Demo1:
    name = "类属性"
    def __init__(self,age):
        self.age = age
        
    def test_01(self):
        print("实例方法1")
        
    def test_02(self):
        print("实例方法2")
        #实例调用
        print(self.name) #类属性
        print(self.age) #实例属性
        self.test_01() #实例方法
        self.test_03() #类方法
        self.test_04() #静态方法
        
    @classmethod
    def test_03(cls):
        print("类方法")
        
    @staticmethod
    def test_04():
        print("静态方法")
        
cl = Demo1(age=20)
cl.test_02()
#实例调用
print(cl.name) #类属性
print(cl.age) #实例属性
cl.test_03()
cl.test_04()

二、类方法
1、创建:
class Demo2:
    @classmethod
    def test_01(cls):
        print("类方法")
2、调用
class Demo2:
    @classmethod
    def test_01(cls):
        print("类方法1")
    @classmethod
    def test_01(cls):
        print("类方法2")
Demo2.test_02()
3、属性/方法调用：
class Demo2:
    name = "类属性"
    def __init__(self,age):
        self.age = age
    @classmethod
    def test_01(cls):
        print("类方法1")
    @classmethod
    def test_02(cls):
        print("类方法2")
        #调用类属性
        print(cls.name)
        #无法通过cls调用实例属性
        #类调用类方法
        cls.test_01()
        #无法调用实例方法
        #类调用静态方法
        cls.test_03()
    @staticmethod
    def test_03():
        print("静态方法")
Demo2.test_02()

三、静态方法
1、创建：
class Demo3:
    @staticmethod
    def test_01():
        print("静态方法")
2、调用：
clss Demo3:
    @staticmethod
    def test_01():
        print("静态方法1")
            @staticmethod
    def test_02():
        print("静态方法2")
        Demo3.test_01()
Demo3.test_02()

3、属性/方法调用：
clss Demo3:
    name = "类属性"
    def __init__(self,age):
        self.age = age
        
    @staticmethod
    def test_01():
        print("静态方法1")
        
    @staticmethod
    def test_02():
        print("静态方法2")
        #以下方法不建议使用，如果使用建议定义对应的方法（实例方法或者类方法）
        print(Demo3.name) #类调用类属性
        print(Demo3.name)#实例调用实例属性
        #间接调用静态方法
        Demo3.test_01() #类调用静态方法
        #不建议这样调用，实例调用实例方法
        Demo3(20).test_03 #Demo3.test_03(Demo3(20))
        Demo3.test_04() #Demo3.test_04() #类调用类方法
        
    def test_03(self):
        print("实例方法")
        
    @classmethod
    def test_04(cls):
        print("类方法")
Demo3.test_02()
"""