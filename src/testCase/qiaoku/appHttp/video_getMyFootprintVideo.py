# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import UserApi


class video_getMyFootprintVideo(unittest.TestCase):
    """获取用户的足迹"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjgyMDQxMTMsInVzZXJJZCI6NjE5OTg4OTI4MjU4MTEzNTM2LCJpc3MiOiJxaWFva3UifQ.81kxXZgRzGVmX6CKQ8lEp09zui_1sH2O4hIRERWyMAw"
    def test(self):
        pass

    def tearDown(self):
        pass
        # 获取用户的足迹
        self.a()

    def a(self):
        """获取用户的足迹"""
        data = {

        }
        UserApi.getMyFootprintVideo(data,self.token)

if __name__ == '__main__':
    unittest.main()
