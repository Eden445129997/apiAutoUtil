# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import VideoPlay


class videoPlay_addThumbsUp(unittest.TestCase):
    """视频播放--视频点赞"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg3OTUzMzgsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.WRSK6ofZcDv1jv4JV2gcetTs0A849fM9LMy4jsmH43c"

    def tearDown(self):
        pass

    def test(self):
        # 点赞视频
        self.a()
        # 取消点赞视频
        # self.b()

    def a(self):
        """点赞"""
        data = {
            "videoId":"623592368574038016",
            "thumbStatus":"1",
        }
        VideoPlay.addThumbsUp(data,self.token)

    def b(self):
        """取消点赞"""
        data = {
            "videoId":"620644814643265536",
            "thumbStatus":"2",
        }
        VideoPlay.addThumbsUp(data,self.token)

if __name__ == '__main__':
    unittest.main()
