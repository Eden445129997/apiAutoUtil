# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import appHttp


class music_saveMusic(unittest.TestCase):
    """上传音乐"""
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
        # 上传音乐
        self.a()

    def a(self):
        """上传音乐"""
        data = {
            "coverPhoto":"http://dd2019071501.didongkj.com/1571645934138.png",
            "musicUrl":"http://dd2019071501.didongkj.com/1571119707318.mp3",
            "musicName":"Eden测试数据",
            "timeLength":"120",
            "singer":"Eden",
        }
        appHttp.saveMusic(data,self.token)

if __name__ == '__main__':
    unittest.main()
