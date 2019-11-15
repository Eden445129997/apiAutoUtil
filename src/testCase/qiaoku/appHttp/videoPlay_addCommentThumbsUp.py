# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import VideoPlay


class videoPlay_addCommentThumbsUp(unittest.TestCase):
    """视频播放--评论点赞"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1MDg2NzAsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.dpnceZSaXpVYbY4zp_z8yIlCGuarR-c-n4AjvlcRf7k"

    def tearDown(self):
        pass

    def test(self):
        # 点赞评论
        self.a()
        # 取消点赞评论
        # self.b()


    def a(self):
        """点赞"""
        data = {
            "cId":"620644814643265536",
            "thumbStatus":"1",
        }
        VideoPlay.addCommentThumbsUp(data,self.token)

    def b(self):
        """取消点赞"""
        data = {
            "cId":"620644814643265536",
            "thumbStatus":"2",
        }
        VideoPlay.addCommentThumbsUp(data,self.token)

if __name__ == '__main__':
    unittest.main()
