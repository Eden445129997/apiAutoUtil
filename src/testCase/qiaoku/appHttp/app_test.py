#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.testCase.qiaoku import api_obj

class collection(unittest.TestCase):
    """获取用户消息列表"""

    # 初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODUxMDA1NDAsInVzZXJJZCI6NjkyMzA3MzY5ODE1ODcxNDg4LCJ1c2VyUGxhdGZvcm0iOiJhcHAiLCJ1ZGlkIjoibG9naW4iLCJpc3MiOiJxaWFva3UifQ.c8wPd-s4s_YIQBKeqQjACrFulVDnDvfEtXQa-ym_n-g"

    def tearDown(self):
        pass

    def test(self):
        # 获取用户消息列表
        self.save1()

    def save1(self):
        """app端创建合集"""
        data = {
        }
        api_obj.v104_user_getAppUserBasicInfo(data, self.token)


if __name__ == '__main__':
    unittest.main()
