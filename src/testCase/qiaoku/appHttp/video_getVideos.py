# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import HomePageApi


class video_getVideos(unittest.TestCase):
    """主页-视频列表(关注页,发现页)"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjkyMTcyNDEsInVzZXJJZCI6NjI1MDM4NjEwODg1NzcxMjY0LCJpc3MiOiJxaWFva3UifQ.JqcqKWEIT99GXn-LJCor4SDk7RZYUUdyDCRFUuMwO8Q"

    def tearDown(self):
        pass

    def test(self):
        # 主页-视频列表(关注页,发现页)
        self.a()
        # 不带token
        # self.b()

    def a(self):
        """主页-视频列表(关注页,发现页)"""
        data = {
            "pageIndex":1,
            "pageSize":10,
            "type":"recommend"
        }
        HomePageApi.getVideos(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "pageIndex":1,
            "pageSize":10,
            "type":"follow"
        }
        HomePageApi.getVideos(data)


if __name__ == '__main__':
    unittest.main()
