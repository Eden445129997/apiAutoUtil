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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODU3MzQ1MTUsImJhY2tfdXNlcl9pZCI6MTIsImlzcyI6InFpYW9rdV9iYWNrIn0.mI-be_SYyBMhR7MQJ1XJEPFcKK6mM3rK0MhrJ8ERc-Q"

    def tearDown(self):
        pass

    def test(self):
        # 获取用户消息列表
        self.save1()

    def save1(self):
        """app端创建合集"""
        data = {
            "nickName":"小恒日常",
            "pageIndex":1,
            "pageSize":200,
            "userOrigin":1
        }
        api_obj.user_getUserDataList(data, self.token)


if __name__ == '__main__':
    unittest.main()
