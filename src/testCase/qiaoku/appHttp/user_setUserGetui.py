# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import PushMsg


class user_setUserGetui(unittest.TestCase):
    """设置通知"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1MDg2NzAsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.dpnceZSaXpVYbY4zp_z8yIlCGuarR-c-n4AjvlcRf7k"

    def tearDown(self):
        pass

    def test(self):
        # 设置通知
        self.a()
        # 不带token
        # self.b()

    def a(self):
        """设置通知"""
        data = {
            "userId":621775455304810496,
            "cid":"111",
            "platform":"ios",
            "thumbUpNoticeStatus":1,
            "commentNoticeStatus":2,
            "followNoticeStatus":2,
            "followOtherPublishNoticeStatus":2,
            "privatelyNoticeStatus":2,
        }
        PushMsg.setUserGetui(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "userId":621775455304810496,
            "cid":"111",
            "platform":"ios",
            "thumbUpNoticeStatus":1,
            "commentNoticeStatus":1,
            "followNoticeStatus":1,
            "followOtherPublishNoticeStatus":1,
            "privatelyNoticeStatus":1,
        }
        PushMsg.setUserGetui(data)

if __name__ == '__main__':
    unittest.main()
