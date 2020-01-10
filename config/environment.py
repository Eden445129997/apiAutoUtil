#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import wraps
import os


# cmd命令行，使用ICMP协议PING主机Environment
def PingCmd(ip):
    __ip = ip

    # 去除指定字符串
    if r"http://" in __ip:
        __ip = __ip.replace(r"http://", "")
    elif r"https://" in __ip:
        __ip = __ip.replace(r"https://", "")

    # 四次ping机会，成功则返回True
    for i in range(4):
        backinfo = os.system("ping -n 1 -w 2 %s" % __ip)
        # 如果数据包没有丢失则返回True
        if not backinfo:
            return True
    return False


# 生产环境装饰器
def productionEnvironment(func):
    def outter_wrapper(*args, **kwargs):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            __ip = r"http://10.113.248.204"
            __port = r":8771"
            return __ip, __port

        return func(inner_wrapper)

    return outter_wrapper


# 测试环境装饰器
def testEnvironment(func):
    def outter_wrapper(*args, **kwargs):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            __ip = r"http://10.113.248.203"
            __port = r":80"
            return __ip, __port

        return func(inner_wrapper)

    return outter_wrapper


# 小目标的服务器
def xiaomubiaoEnvironment(func):
    def outter_wrapper(*args, **kwargs):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            __ip = r"http://10.113.248.86"
            __port = r":8771"
            return __ip, __port

        return func(inner_wrapper)

    return outter_wrapper


# 石杰的服务器
def shijieEnvironment(func):
    def outter_wrapper(*args, **kwargs):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            __ip = r"http://10.113.248.67"
            __port = r":8771"
            return __ip, __port

        return func(inner_wrapper)

    return outter_wrapper
