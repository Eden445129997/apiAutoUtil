# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import appHttp


class music_myCollectingMusic(unittest.TestCase):
    """我收藏音乐列表"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzE3OTk5NzksInVzZXJJZCI6NjMyNjIxMTQ2MzI3NDgyMzY4LCJ1ZGlkIjoiIiwiaXNzIjoicWlhb2t1In0.vgqv5MT749n3crQUs5dqeRtAbjwyyOrlYck1WafxN2M"

    def test(self):
        pass

    def tearDown(self):
        pass
        # 我收藏音乐列表
        self.a()

    def a(self):
        """我收藏音乐列表"""
        data = {
            "pageIndex":"1",
            "pageSize":"10",
        }
        appHttp.myCollectingMusic(data,self.token)

if __name__ == '__main__':
    unittest.main()
