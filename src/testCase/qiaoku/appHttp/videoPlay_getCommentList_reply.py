# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import VideoPlay


class videoPlay_getCommentList_reply(unittest.TestCase):
    """视频播放-获取回复评论列表"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1MDg2NzAsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.dpnceZSaXpVYbY4zp_z8yIlCGuarR-c-n4AjvlcRf7k"

    def tearDown(self):
        pass

    def test(self):
        # 获取回复评论列表
        self.a()
        # 不带token
        # self.b()


    def a(self):
        """获取回复评论列表"""
        data = {
            "videoId":"620644814643265536",
            "replyId":"621675056472260608",
            "cId":"621718935464574976",
            "pageIndex":1,
            "pageSize":10,
            "queryTime":"2019-09-19 15:24:56",
        }
        VideoPlay.reply(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "videoId":"620644814643265536",
            "replyId":"621429496460869632",
            "cId":"621675593125068800",
            "pageIndex":1,
            "pageSize":10,
            "queryTime":"2019-09-19 15:24:56",
        }
        VideoPlay.reply(data)

if __name__ == '__main__':
    unittest.main()
