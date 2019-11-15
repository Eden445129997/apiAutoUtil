# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import appHttp


class video_getOneVideo(unittest.TestCase):
    """获取单个视频信息"""
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
        # 获取单个视频信息
        self.a()

    def a(self):
        """获取单个视频信息"""
        data = {
            "videoId":"627545310297587712",
        }
        appHttp.getOneVideo(data,self.token)

if __name__ == '__main__':
    unittest.main()
