测试用例 = """
一、测试用例包含哪些东西
    1、前置条件
    2、测试步骤（业务逻辑）
    3、断言（响应、数据库数据断言）
    4、数据提取
    5、后置处理
    6、测试报告
    7、邮件发送
    8、日志收集
    
    
一、前置后置
1、前后置方法不需要手动调用，会自动执行
2、前后置方法可以不写，按自己需求来写
3、前后置方法跟书写顺序没有关系，只要在测试用例类的内部都会被执行
函数级别的前置
def setUp(self) ->None:
    print("函数级别前置，每个测试用例执行之前执行一次")
    
类级别的前置
@classmethod
def setUpClass(cls) -> None:
    print("类级别前置，每个测试类执行之前执行一次")

函数级别的后置
def tearDown(self) -> None:
    print("函数级别的后置，每个测试用例执行结束之后需执行一次")
    
类级别的后置
@classmethod
def tearDownClass(cls) -> None:
    print("类级别后置，每个测试类执行结束之后执行一次")
    
二、用例执行顺序（超过99到100的时候，99会先执行，因为是逐位比较
1、按照测试用例名称ASCII码大小来执行(ASCII码小的先执行)
2、逐位比对大小(ASCII码)
3、ord("a")获取ASCII码
4、chr(97)通过ASCII码获取对应的值
"""
import unittest
#最完整的测试用例，没有用数据驱动
class TestDemo(unittest.TestCase):
    #函数级别的前置
    def setUp(self) -> None:
        print("函数级别前置，每个测试用例执行之前执行一次")

    # 类级别的前置
    @classmethod
    def setUpClass(cls) -> None:
        print("类级别前置，每个测试类执行之前执行一次")

    # 函数级别的后置
    def tearDown(self) -> None:
        print("函数级别的后置，每个测试用例执行结束之后需执行一次")

    # 类级别的后置
    @classmethod
    def tearDownClass(cls) -> None:
        print("类级别后置，每个测试类执行结束之后执行一次")

    def test_01(self):
        print("test_01")

    def test_02(self):
        print("test_02")

if __name__ == "__main__":
    unittest.main()

# 用例执行入口
测试用例收集 = """
一、测试用例维度【了解】
1、添加单个测试用例
su.addTest(TestDemo4("test_01")
2、添加多个测试用例
su.addTest([TestDemo4("test_01"),TestDemo4("test_02"])
3、代码
from day16.demo import TestDemo4
import unittest
#创建测试套件：用来收集测试用例
su = unittest.TestSuite()
#把测试用例放到条件里
# su.addTest(TestDome4("test_01"))
su.addTests([TestDome4("test_01"), TestDome4("test_02")
#创建一个执行器
runner = unittest.TestRunner()
#将测试套件放到执行器去执行
runner.run(su)

三、模块维度【掌握】
1、收集指定目录下的某些py文件下的测试用例类中的测试用例
start_dir=".":测试用例文件(.py)所在的目录
pattern="demo*.py":测试用例文件的名称，*表示通配符，默认是test开头的py文件
su = unittest.defaultTestLoader.discover(start_dir=".",pattern="demo*.py")
2、代码
import unittest
# 创建测试套件：用来收集测试用例
su = unittest.defaultTestLoader.discover(start_dir=".",pattern="demo*.py")
#不建议这样写
# su = unittest.TestLoader().discover(start_dir=".",pattern="demo*.py")
#创建一个执行器
runner = unittest.TeXtTestRunner
#将测试套件放到执行器去执行
runner.run(su)
"""

测试报告 = """
一、BeautifulReport生成测试报告
1、代码
import unittest
from BeautifulReport import BeautifulReport
#创建测试套件：用来收集测试用例
su = unittest.defaultTestLoader.discover(start_dir=".",pattern="demo*.py")
#实例化执行器类
br = BeautifulReport(suites=su)
#执行测试用例收集测试报告
br.report(description="接口测试报告",filename="test.html")

二、拓展（三元运算）
filename="test"
res = filename if filename.endswith('.html') else filename + '.html'

def test(filename):
    if filename.endswith('.html'):
        return filename
    else:
        return filename + '.html'
    
三、unittestreport测试报告生成
1、代码
import unittest
from unittestreport import TestRunner
#创建测试套件：用来收集测试用例
su = unittest.defaultTestLoader.discover(start_dir".",pattern="demo*.py")
runner = TestRunner(
                suite=su,
                filename="py52report.html",
                report_dir="./reports",
                title='接口测试报告',
                tester='海励',
                desc="上课项目测试生成的报告",
                templates=2 #可以换模版
                    )
runner.run()
"""

"""
1、2020年的最老的自动化课程邮件发送，继承在jenkins上发邮件
    问题：jenkins插件不稳定（兼容性问题），不好配置，经常配置失败
2、2021年的自动化课程邮件发送，unittestreport来发发送邮件
    1、构造邮件：标题，正文，附件，发送给谁，谁发送，协议
    2、执行完测试用例，会生成一个html文件，就用作邮件的附件
    3、发送邮件
    
import unittest
from unittestreport import TestRunner

if __name__ == '__main__':  #不写这个模块相同可能执行两遍(也可以把这个文件名改成start)
    #创建测试套件：用来收集测试用例
    su = unittest.defaultTestLoader.discover(start_dir".",pattern="demo*.py")#pattern收集哪个模块
    runner = TestRunner(
                    suite=su,
                    filename="py52report.html",
                    report_dir="./reports",
                    title='接口测试报告',
                    tester='海励',
                    desc="上课项目测试生成的报告",
                    templates=2 #可以换模版
                        )
    runner.run()
    runner.send_email(host="smtp.qq.com",   #发送邮件的smtp服务器
                      port=465,             #163 端口是25 qq邮箱465
                      user="@qq.com",       #qq邮箱
                      password="najvvwadvkxlddij",   #邮箱授权码
                      to_addrs=[],          #要发送人的邮箱
                        )
"""

