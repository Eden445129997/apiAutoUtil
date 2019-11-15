import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import UserApi


class user_getAppUserBasicInfo(unittest.TestCase):
    """查看个人/他人基本信息"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjgyMDQxMTMsInVzZXJJZCI6NjE5OTg4OTI4MjU4MTEzNTM2LCJpc3MiOiJxaWFva3UifQ.81kxXZgRzGVmX6CKQ8lEp09zui_1sH2O4hIRERWyMAw"

    def test(self):
        pass

    def tearDown(self):
        # pass
        # 查看他人信息
        self.a()

    def a(self):
        """查看他人信息"""
        data = {
            # "otherUserId":"617013666046279680",
            "otherUserId":None,

        }
        UserApi.getAppUserBasicInfo(data,self.token)

if __name__ == '__main__':
    unittest.main()

