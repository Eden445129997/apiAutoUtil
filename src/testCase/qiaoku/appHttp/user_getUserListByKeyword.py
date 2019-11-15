# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import SearchApi


class user_getUserListByKeyword(unittest.TestCase):
    """搜索用户"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjgyODQ0NDMsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.ExCvWxnn1fA75jewBdz2SNOlxa-VH0jCEyrNWZvnR5k"

    def tearDown(self):
        pass

    def test(self):
        # 搜索用户
        self.a()

    def a(self):
        """搜索用户"""
        data = {
            "keyword":"1567916372",
        }
        SearchApi.getUserListByKeyword(data,self.token)

if __name__ == '__main__':
    unittest.main()
