# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import UserApi


class user_getUserLinkedVideo(unittest.TestCase):
    """获取用户相关的视频(type区分)--1发布 2赞过 3收藏"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjgyODQ0NDMsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.ExCvWxnn1fA75jewBdz2SNOlxa-VH0jCEyrNWZvnR5k"

    def tearDown(self):
        pass

    def test(self):
        # 发布过
        # self.a()
        # 赞过
        # self.b()
        # 收藏
        self.c()


    def a(self):
        """1发布"""
        data = {
            "otherUserId":"617013666046279680",
            "myVideoType":1,
        }
        UserApi.getUserLinkedVideo(data,self.token)

    def b(self):
        """2赞过"""
        data = {
            "otherUserId":"621775455304810496",
            "myVideoType":2,
        }
        UserApi.getUserLinkedVideo(data,self.token)


    def c(self):
        """3收藏"""
        data = {
            "otherUserId":"621775455304810496",
            "myVideoType":3,
        }
        UserApi.getUserLinkedVideo(data,self.token)

if __name__ == '__main__':
    unittest.main()
