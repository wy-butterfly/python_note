配置文件 = """
一、ini配置文件【不用】
{
"section1":{"option1":"val","option2":"val"},
"section2":{"option1":"val","option2":"val"},
}

django里面用setting.py文件做配置文件

1、获取所有的section,返回section名称的list
res = conf.sections() #获取到的是具体的值
res = conf.keys() #获取到的是对象,不是具体的值，要通过for循环去拿值，第0位是DEFAULT

2、获取str类型
get_str = conf.get(section="mysql", option="host")
print(get_str,type(get_str))

3、获取int类型
get_int = conf.getint(section="mysql", option="passwd")
print(get_int,type(get_int))

4、获取小数
get_float = conf.getfloat(section="mysql", option="float")
print(get_float,type(get_float))

5、获取布尔值
get_bool = conf.getboolean(section="mysql", option="is_file")
print(get_bool,type(get_bool))



"""



test_dict = {
"section1":{"option1":"val","option2":"val"},
"section2":{"option1":"val","option2":"val"},
}

from configparser import ConfigParser
conf = ConfigParser()

conf.read(filenames="",encoding="utf-8") #传一个.ini文件名

#获取所有的section
"""res =conf.sections()
print(res)"""
#获取到的是对象,不是具体的值，要通过for循环去拿值，第0位是DEFAULT
"""res = conf.keys()
print(res)

for i in res:
    print(i)"""
#获取option
conf.options(section="")

#获取指定section下的option值
#获取str类型
get_str = conf.get(section="",option="")
print(get_str,type(get_str))
# 获取int类型
get_int = conf.getint(section="",option="")
#获取小数
get_float = conf.getfloat(section="",option="")