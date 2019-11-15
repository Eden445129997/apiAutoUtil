# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import appHttp


class video_getRecommendTalentVideo(unittest.TestCase):
    """可能感兴趣的人视频(第二页及以后页码的视频)"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzE3OTg3NzYsInVzZXJJZCI6NjMyNjIxMTQ2MzI3NDgyMzY4LCJ1ZGlkIjoiIiwiaXNzIjoicWlhb2t1In0.gK8Auvk3rs9IHFXUJp9dkQgj39PdYnSRgFV93hMluzU"

    def test(self):
        pass

    def tearDown(self):
        pass
        # 可能感兴趣的人视频(第二页及以后页码的视频)
        self.a()

    def a(self):
        """可能感兴趣的人视频(第二页及以后页码的视频)"""
        data = {
            "otherUserId":"627503275461050368",
            # "pageIndex":"1",
            # "pageSize":"10",
        }
        appHttp.getRecommendTalentVideo(data,self.token)

if __name__ == '__main__':
    unittest.main()
