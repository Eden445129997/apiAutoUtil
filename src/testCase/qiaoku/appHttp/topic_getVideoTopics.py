# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import TopicApi


class topic_getVideoTopics(unittest.TestCase):
    """话题-全部话题列表"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1MDg2NzAsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.dpnceZSaXpVYbY4zp_z8yIlCGuarR-c-n4AjvlcRf7k"

    def tearDown(self):
        pass

    def test(self):
        # 获取推荐话题列表
        self.a()
        # 获取热门话题列表
        self.b()
        # 不带token
        self.c()

    def a(self):
        """获取推荐话题列表"""
        data = {
            "pageIndex":1,
            "pageSize":10,
            "type":1
        }
        TopicApi.getVideoTopics(data,self.token)

    def b(self):
        """获取热门话题列表"""
        data = {
            "pageIndex":1,
            "pageSize":100,
            "type":2
        }
        TopicApi.getVideoTopics(data,self.token)

    def c(self):
        """不带token"""
        data = {
            "pageIndex":1,
            "pageSize":10,
            "type":1
        }
        TopicApi.getVideoTopics(data)

if __name__ == '__main__':
    unittest.main()
