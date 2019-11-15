# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import TopicApi


class topic_getTopicDetails(unittest.TestCase):
    """话题-话题详情页"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1MDg2NzAsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.dpnceZSaXpVYbY4zp_z8yIlCGuarR-c-n4AjvlcRf7k"

    def tearDown(self):
        pass

    def test(self):
        # 获取话题详情
        self.a()
        # 不带token
        # self.b()

    def a(self):
        """获取话题详情"""
        data = {
            "topicId":"1",
            "topicType":"new",
            "pageIndex":1,
            "pageSize":1
        }
        TopicApi.getTopicDetails(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "topicId":"18",
            "topicType":"recommend",
            "pageIndex":1,
            "pageSize":10
        }
        TopicApi.getTopicDetails(data)

if __name__ == '__main__':
    unittest.main()
