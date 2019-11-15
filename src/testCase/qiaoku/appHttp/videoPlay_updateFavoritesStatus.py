# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import VideoPlay


class videoPlay_updateFavoritesStatus(unittest.TestCase):
    """视频播放--视频收藏"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1MDg2NzAsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.dpnceZSaXpVYbY4zp_z8yIlCGuarR-c-n4AjvlcRf7k"

    def tearDown(self):
        pass

    def test(self):
        # 收藏视频
        self.a()
        # 取消收藏视频
        # self.b()

    def a(self):
        """收藏视频"""
        data = {
            "chooseOrCancel":1,
            "videoId":"620644814643265536",
        }
        VideoPlay.updateFavoritesStatus(data,self.token)

    def b(self):
        """取消收藏视频"""
        data = {
            "chooseOrCancel":2,
            "videoId":"620644814643265536",
        }
        VideoPlay.updateFavoritesStatus(data,self.token)

if __name__ == '__main__':
    unittest.main()
