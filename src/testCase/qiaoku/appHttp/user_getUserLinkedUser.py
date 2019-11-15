import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import UserApi


class user_updateBlackUserList(unittest.TestCase):
    """获取用户关注的人, 粉丝(1关注 2粉丝)"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)
        # date_str = '2017-10-19'
        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg4OTI5MzAsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.XpBprsWrXwuM9zewVJGnnD3R1Or-vrpH2fMX6nZfASU"

    def test(self):
        pass

    def tearDown(self):
        pass
        # 获取用户关注
        # self.a()
        # 获取用户粉丝
        self.b()

    def a(self):
        """关注 """
        data = {
            "otherUserId":"617013666046279680",
            "type":1,
        }
        UserApi.getUserLinkedUser(data,self.token)

    def b(self):
        """粉丝 """
        data = {
            "otherUserId":"617013666046279680",
            "type":2,
        }
        UserApi.getUserLinkedUser(data,self.token)

if __name__ == '__main__':
    unittest.main()