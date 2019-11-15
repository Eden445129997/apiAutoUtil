# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import VideoPlay


class videoPlay_queryTalkingSkill(unittest.TestCase):
    """获取举报/审核的内容"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1MDg2NzAsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.dpnceZSaXpVYbY4zp_z8yIlCGuarR-c-n4AjvlcRf7k"

    def tearDown(self):
        pass

    def test(self):
        # 获取举报/审核的内容
        self.a()
        # 不带token
        self.b()

    def a(self):
        """获取举报/审核的内容"""
        data = {
            "type":"7",
        }
        VideoPlay.queryTalkingSkill(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "type":"1",
        }
        VideoPlay.queryTalkingSkill(data)


if __name__ == '__main__':
    unittest.main()
