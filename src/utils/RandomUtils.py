#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time
import json


class randomUtils():
    """ 随机工具类
    """
    @staticmethod
    def intRandom(x):
        """ 生成x个随机数
        :param x:
        :return string:
        """
        randomString = ""
        for i in range(x):
            toString = str(random.randint(0,9))
            randomString = randomString + toString
        return randomString

    @staticmethod
    def letterRandom(x):
        """ 生成x个随机英文字母
        :param x:
        :return string:
        """
        letter = "abcdefghijklmnopqrstuvwxyz"
        randomString = ""

        # 方法1
        for i in range(random.randint(x,x)):
           randomString = randomString + letter[random.randint(0,len(letter)-1)]
        return randomString

        # 方法2
        # out = 0
        # while True:
        #     out = out + random.randint(1,35)
        #     str = str + letter[random.randint(0,len(letter)-1)]
        #     if out >= 100:
        #         break
        # return str

    @staticmethod
    def timeStamp():
        """获取当前时间以秒为单位的时间戳"""
        return int(time.time())

if __name__ == "__main__":
    a = randomUtils.letterRandom(5)
    print(a)
    b = randomUtils.letterRandom(5)
    print(b)
    c = randomUtils.intRandom(5)
    print(c)
    d = randomUtils.timeStamp()
    print(d)