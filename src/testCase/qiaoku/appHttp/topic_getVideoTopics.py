# coding=UTF-8
import unittest

from src.testCase.qiaoku.api_obj import topic_getVideoTopics


class getVideoTopics(unittest.TestCase):
    """话题-全部话题列表"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzg3MDc1NzMsInVzZXJJZCI6MzgyMTksInVzZXJQbGF0Zm9ybSI6ImFwcCIsInVkaWQiOiI5Rjk1NzU5OTQ0RDBENkQxRTM0M0QxMjJGNDQ2QjQ4ODc2Rjg2OTQ2IiwiaXNzIjoicWlhb2t1In0.D5pcfIP2P4_iSbgFU1IXh2Hp-0H56CyTVigMW607drc"

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
        topic_getVideoTopics(data,self.token)

    def b(self):
        """获取热门话题列表"""
        data = {
            "pageIndex":1,
            "pageSize":100,
            "type":2
        }
        topic_getVideoTopics(data,self.token)

    def c(self):
        """不带token"""
        data = {
            "pageIndex":1,
            "pageSize":10,
            "type":1
        }
        topic_getVideoTopics(data)

if __name__ == '__main__':
    unittest.main()
