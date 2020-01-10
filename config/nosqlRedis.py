#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import wraps


# 测试环境装饰器
def testEnvironment(func):
    def outter_wrapper(*args, **kwargs):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            __redisConfig = {
                "host": r"10.113.248.203",
                "port": 6379,
                "password": r"didong1904",
                "db": 0,
            }
            return __redisConfig

        return func(inner_wrapper)

    return outter_wrapper


# 开发环境装饰器
def productionEnvironment(func):
    def outter_wrapper(*args, **kwargs):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            __redisConfig = {
                "host": r"10.113.248.204",
                "port": 6379,
                "password": r"didong1904",
                "db": 0,
            }
            return __redisConfig

        return func(inner_wrapper)

    return outter_wrapper
