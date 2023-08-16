数据驱动 = """
一、三方库
ddt

二、使用
什么是数据驱动，为什么要用数据驱动，什么场景适合用数据驱动？
同一个接口（登录页面测试）
1、登录成功
2、登录失败：密码错误
3、登录失败：账号错误
4、登录失败：账号密码不匹配
相同点：
1、请求的接口是一样的
2、请求的方法是一样的
3、请求头信息
不同点：
1、请求参数不一样

不同接口
相同点：
1、鉴权方式（统一系统）
2、协议是一样的(http)
3、域名(ip)
不同点：
1、接口地址不一样  pass
2、请求参数不一样  pass
3、请求方法不一样  pass
4、请求头不一样（请求参数的编码方式）  pass

三、使用
语法
from ddt import ddt,data

test_data = ["2、登录失败:密码错误","3、登录失败:账号错误","4、登录失败：账号密码不匹配,"]
@ddt
class TestDemo(unittest.TestCase):
    @data(*test_data)
    def test_01(self,case):
        pass
        
"""

import requests
import unittest
from ddt import ddt, data

test_data = [
    {"method": "post", "title": "登录成功1", "url": "http://www.lemon.com/login1"},
    {"method": "post", "title": "登录成功2", "url": "http://www.lemon.com/login2"},
    {"method": "post", "title": "登录成功3", "url": "http://www.lemon.com/login3"}
]


@ddt
class Test(unittest.TestCase):
    @data(*test_data)  # 解压数据
    def test_01(self, case):
        print("拿着请求参数去发请求", type(case))  # 查看数据类型
        res = requests.request(method=case["method"], url=case["url"])
        print(res)


if "__name__" == " __main__ ":
    unittest.main()

# @ddt类装饰器
# @data函数装饰器
