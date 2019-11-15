# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import appHttp


class video_getRecommendTalent(unittest.TestCase):
    """可能感兴趣的人"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzE3NDgyNTgsInVzZXJJZCI6NjMyNjIxMTQ2MzI3NDgyMzY4LCJ1ZGlkIjoiIiwiaXNzIjoicWlhb2t1In0.4kXK74C96k5UcQ5wtJLmyWcw46OtExswboe0Ic_hZNo"

    def test(self):
        pass

    def tearDown(self):
        pass
        # 可能感兴趣的人
        self.a()

    def a(self):
        """可能感兴趣的人"""
        data = {
            # "pageIndex":"1",
            # "pageSize":"5",
        }
        appHttp.getRecommendTalent(data,self.token)

if __name__ == '__main__':
    unittest.main()
