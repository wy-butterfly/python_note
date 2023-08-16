http协议="""
1、超文本传输协议，用于服务器之间传输文本和数据使用得传输规范
2、http协议基于TCP协议之上的协议，默认端口是80端口
    车子---http协议
    高速公路---tcp协议
3、http协议只关注是否按照我的协议规则来使用，不关心传输的内容

一、http常用方法
1、get:向服务器获取资源【掌握】
2、post:向服务器提交资源【掌握】
3、delete:删除资源
4、option:查询接口支持的请求方法
5、trace:测试用例，看接口是否请求通，还请求数据
6、put:修改资源，全部修改{"key1":"val1","key2":"val2"}=={"key1":"val88","key2":"val2"}【掌握】
7、patch:修改资源，部分修改{"key1":"val88"}=={"key1":"val88","key2":"val2"}
8、head:查看响应头
9、connect:http/1.1协议预留的方法，代理服务器，代替用户去访问数据（网站接口），拿到数据后再返回数据

四、http协议报文
http://mall.lemonban.com/admin/#/login
student
123456a


打开谷歌浏览器并导航到您要调试的网页。
点击右上角的菜单图标（三个垂直点），然后选择"更多工具"。
在"更多工具"子菜单中选择"开发者工具"，或使用快捷键"Ctrl+Shift+I"（Windows/Linux）或"Command+Option+I"（Mac）。
开发者工具将会以一个浮动面板的形式打开在当前浏览器窗口中。
"""

"""
http与https的区别
    1、http明文传输，https密文传输
    2、默认端口http 80端口，https 443端口
    3、https需要CA证书，http+ssl/tls认证，http不需要证书
    4、https是有状态的
    http






抓包
"""