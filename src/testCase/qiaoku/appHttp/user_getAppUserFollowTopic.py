import unittest
import time,datetime

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import UserApi


class user_updateBlackUserList(unittest.TestCase):
    """获取用户关注的话题"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)
        # date_str = '2017-10-19'

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjkwNjI1ODEsInVzZXJJZCI6NjI1MDM4NjEwODg1NzcxMjY0LCJpc3MiOiJxaWFva3UifQ.inNwOa1NFIwpAcESHSFflpuRdTWdOh7j6GSBGwku2Vg"
    def test(self):
        pass

    def tearDown(self):
        pass
        # 获取用户关注的话题
        self.a()

    def a(self):
        """获取用户关注的话题"""
        data = {
            # "otherUserId":"618815311222669312",
        }
        UserApi.getAppUserFollowTopic(data,self.token)

if __name__ == '__main__':
    unittest.main()
