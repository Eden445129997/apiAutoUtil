# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import VideoPlay


class videoPlay_saveVideoShare(unittest.TestCase):
    """视频分享"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1MDg2NzAsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.dpnceZSaXpVYbY4zp_z8yIlCGuarR-c-n4AjvlcRf7k"

    def tearDown(self):
        pass

    def test(self):
        # 视频分享
        self.a()
        # 不带token
        self.b()

    def a(self):
        """视频分享"""
        data = {
            "videoId":"620644814643265536",
            "platform":"wx",
        }
        VideoPlay.saveVideoShare(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "videoId":"620644814643265536",
            "platform":"wx",
        }
        VideoPlay.saveVideoShare(data)


if __name__ == '__main__':
    unittest.main()
