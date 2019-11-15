import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import UserApi


class registerLogin(unittest.TestCase):
    """修改用户对用户的关注状态"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg3MDUzNDEsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.hJoCwyR4GwnCBUZuLWFPZWUQdKEpFM9goaEHyUl1hH0"

    def test(self):
        pass

    def tearDown(self):
        # pass
        # 选择关注
        self.a()
        # 取消关注
        # self.b()

    def a(self):
        """选择关注"""
        data = {
            "chooseOrCancel":2,
            "otherUserId":"617013666046279680",
            # "otherUserId":None

        }
        UserApi.updateUserFollowStatus(data,self.token)

    def b(self):
        """取消关注"""
        data = {
            "chooseOrCancel":2,
            "otherUserId":"617013666046279680",
            # "otherUserId":None

        }
        UserApi.updateUserFollowStatus(data,self.token)


if __name__ == '__main__':
    unittest.main()

