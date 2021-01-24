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

# 本地环境装饰器
def betaEnvironment(func):
    def outter_wrapper(*args, **kwargs):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            __ip = r"https://newbetaadmin.didongkj.com"
            __port = r""
            return __ip, __port

        return func(inner_wrapper)

    return outter_wrapper

# 测试环境装饰器
def testEnvironment(func):
    def outter_wrapper(*args, **kwargs):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            # 线上环境
            # __ip = r"https://shanjuapi.yuming11.com"
            # 测试
            __ip = r"http://10.113.248.196"
            # beta
            # __ip = r"https://betaapi.yuming11.com"
            __port = r""
            return __ip, __port

        return func(inner_wrapper)

    return outter_wrapper

# 旺环境装饰器
def wangEnvironment(func):
    def outter_wrapper(*args, **kwargs):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            __ip = r"http://10.113.248.63"
            __port = r""
            return __ip, __port

        return func(inner_wrapper)

    return outter_wrapper