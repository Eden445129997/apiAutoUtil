from functools import wraps

# 测试环境装饰器
def testEnvironment(func):
    def outter_wrapper(*args,**kwargs):
        @wraps(func)
        def inner_wrapper(*args,**kwargs):
            __dataBaseConfig = {
                "host" : r"10.113.248.203",
                "port" : 3306,
                "user" : r"root",
                "password" : r"didong1904",
                "charset" : r"utf8",
            }
            return __dataBaseConfig
        return func(inner_wrapper)
    return outter_wrapper

# 测试环境装饰器
def productionEnvironment(func):
    def outter_wrapper(*args,**kwargs):
        @wraps(func)
        def inner_wrapper(*args,**kwargs):
            __dataBaseConfig = {
                "host" : r"10.113.248.204",
                "port" : r"3306",
                "user" : r"root",
                "password" : r"didong1904",
                "charset" : r"utf8",
            }
            return __dataBaseConfig
        return func(inner_wrapper)
    return outter_wrapper