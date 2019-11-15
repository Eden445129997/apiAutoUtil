import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import UserApi


class user_updateBlackUserList(unittest.TestCase):
    """拉黑/取消拉黑用户"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjgyODQ0NDMsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.ExCvWxnn1fA75jewBdz2SNOlxa-VH0jCEyrNWZvnR5k"

    def test(self):
        pass

    def tearDown(self):
        # pass
        # 拉黑
        # self.a()
        # 取消拉黑
        self.b()

    def a(self):
        """拉黑"""
        data = {
            "chooseOrCancel":1,
            "otherUserId":"617013666046279680",
            # "otherUserId":None,
            "blackUserName":"快乐的大言酱"
        }
        UserApi.updateBlackUserList(data,self.token)

    def b(self):
        """取消拉黑"""
        data = {
            "chooseOrCancel":2,
            "otherUserId":"617013666046279680",
            # "otherUserId":None,
            "blackUserName":"快乐的大言酱"

        }
        UserApi.updateBlackUserList(data,self.token)

if __name__ == '__main__':
    unittest.main()