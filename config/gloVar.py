#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import environment
from config import dataBase
from config import nosqlRedis
from src.utils.Log import log
import redis


# import pymysql

@environment.testEnvironment
def globalEnvironment(env):
    """使用装饰器的方式，定义服务器环境"""
    setLog = log()
    __ip, __port = env()

    # 如果url和port都存在值（True）
    if __ip and __port:
        # 尝试ping目标地址
        # if PingCmd(__ip):
        #     setLog.info("目标地址可ping通")
        # else:
        #     setLog.error("目标地址Ping不通，请确认该环境是否正常")
        return __ip, __port
    # 其中一个不存在值，打印日志并返回
    else:
        setLog.error("路由寻址失败：")
        setLog.error("ip:%s" % __ip)
        setLog.error("port:%s" % __port)
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
