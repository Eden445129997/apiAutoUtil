#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import environment
from config import dataBase
from config import nosqlRedis
import redis

# import pymysql

@environment.testEnvironment
def globalEnvironment(env):
    """使用装饰器的方式，定义服务器环境"""
    __ip, __port = env()
    return __ip, __port

@dataBase.testEnvironment
def globalDataBase(env):
    """使用装饰器的方式，定义数据库环境"""
    # setLog = log()
    __dataBaseConfig = env()
    return __dataBaseConfig

@nosqlRedis.testEnvironment
def globalRides(env):
    """使用装饰器的方式，定义rides环境"""
    # 返回元组，第一对象，第二是字典
    # setLog = log()
    __redisConfig = env()
    # 尝试连接rides，并返回rides
    try:
        __host = __redisConfig.get("host")
        __port = __redisConfig.get("port")
        __password = __redisConfig.get("password")
        __db = __redisConfig.get("db")
        __rds = redis.StrictRedis(host=__host, port=__port, password=__password, db=__db)
        return __rds, __redisConfig
    except:
        return False, __redisConfig


if __name__ == '__main__':
    # __dict = {
    #     "url":r"http://10.113.248.200",
    #     "port":r":8771"
    # }
    a = globalEnvironment()
    print(a)
    # a = "abcdefg"
    # for i in range(len(a))[::-1]:
    #     print(a[i])

    dataBase = globalDataBase()
    print(dataBase)

    __, redisConfig = globalRides()
    print(redisConfig)
