模块="""
一、模块导入
1、python自带的包或者模块
2、第三方包（库）
3、自定义包（模块）

二、导入场景
自动导包：alt+回车

1、同一包下面导入模块
    1、导入模块
     imprt demo2
    2、导入指定的对象
     from day10 demo02 import test_01
     from day10.demo02 import test_01,name
2、跨包导入其他包的模块
     from day09.demo04 import demo01
     import day09.demo04 as demo
3、跨项目导入模块
     from 项目名称.day09.demo04 import demo01
     import 项目名称.day09.demo04 as demo
     
三、注意点
1、自定义模块的时候，命名一定不能用关键字
2、导包出错了怎么排查问题
    1、看你自己的解释器用的是哪个版本
    2、你的包在不在Python默认的目录下
        1、动态添加
            import sys
            print(sys.path)
            sys.path.append('你的目录')
        2、标记为资源
            Mark Directory as >> source root
            
"""

"""
异常处理
一、概念：
什么事异常处理：程序或者代码在执行过程中报错了，无法继续执行，这就叫异常 

二、常见的异常
NameError: name 'name' is not defined

三、异常捕获
try:
    print("可能报错的代码放这里")
    print(num)
except:
    print("报错之后赴执行这里的代码放这里")
    print(num)
    
    
num = 10
try:
    print("可能报错的代码放这里")
    print(num)
except:
    print("报错之后赴执行这里的代码放这里")
    print(num)
else:
    print("执行没有报错的时候执行的代码")
    
try:
    print("可能报错的代码放这里")
    print(num)
except:
    print("报错之后赴执行这里的代码放这里")
    print(num)
else:
    print("执行没有报错的时候执行的代码")
finally:
    print("不管是否报错都会执行的代码")

五、自定义异常
使用场景：unittest断言原理，他是以程序员执行过程中是否抛出异常，如果抛出异常就认为用例执行失败，没抛出异常认为成功
num = 10
try:
    print("可能报错的代码放这里")
    print(num1)
except Exception as e::
    print("报错之后赴执行这里的代码放这里")
    #手动抛出异常
    raise AssertionError("py52")
    raise Exception("手动抛出的异常")

Exception("最大的异常")

"""

"""
debug进阶
1、step over:下一步
2、step into:进入函数内部
3、resume program:到下一个断点处
4、step into my code:从源码处回到自己写的代码里面
5、run to cursor:断点停到鼠标聚焦的位置

"""

# 函数调用（模块导入）
def test_01():
    print('module import.py里面的test_01函数')
    return{'user':'test_user','pwd':'123455'}

test_01()