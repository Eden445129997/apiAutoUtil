# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import VideoPlay

class videoPlay_comment(unittest.TestCase):
    """视频播放-视频评论"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1MDg2NzAsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.dpnceZSaXpVYbY4zp_z8yIlCGuarR-c-n4AjvlcRf7k"

    def tearDown(self):
        pass

    def test(self):
        # 视频评论
        self.a()
        # 不带token
        # self.b()

    def a(self):
        """视频评论"""
        data = {
            "videoId":"620644814643265536",
            "text":"Eden",
            # "replyId":"621429496460869632",
            # "replyToReplyId":"0",
            # "replyToUserId":"0",
        }
        VideoPlay.comment(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "videoId":"620644814643265536",
            "text":"620644814643265536",
            "replyId":"620644814643265536",
            "replyToReplyId":"620644814643265536",
            "replyToUserId":"620644814643265536",
        }
        VideoPlay.comment(data)

if __name__ == '__main__':
    unittest.main()
