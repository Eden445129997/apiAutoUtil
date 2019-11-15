import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import UserApi


class user_getUpToDateVersion(unittest.TestCase):
    """获得最新的app版本信息"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg4MDU5MjMsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.EmgavuvUFeFzyrSPyVqLODvUb_Q6lt0kiNqqLjNkqsw"

    def test(self):
        pass

    def tearDown(self):
        # pass
        # 获得最新的app版本信息
        self.a()

    def a(self):
        """获得最新的app版本信息"""
        data = {
        }
        UserApi.getUpToDateVersion(data,self.token)

if __name__ == '__main__':
    unittest.main()

