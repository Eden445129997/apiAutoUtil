import unittest
import time,datetime

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import UserApi


class user_updateUserInfo(unittest.TestCase):
    """编辑用户信息"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)
        # date_str = '2017-10-19'
        now = time.strftime('%y-%m-%d',time.localtime())
        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjgyMDQxMTMsInVzZXJJZCI6NjE5OTg4OTI4MjU4MTEzNTM2LCJpc3MiOiJxaWFva3UifQ.81kxXZgRzGVmX6CKQ8lEp09zui_1sH2O4hIRERWyMAw"
        self.dateTime = now
    def test(self):
        pass

    def tearDown(self):
        pass
        # 编辑用户信息
        self.a()

    def a(self):
        """编辑用户信息"""
        data = {
            # "nickName":"Eden",
            "userSign":20*"改写人生代码",
            "avatar":None,
            "gender":1,
            "province":"火星",
            "city":"地动联盟",
            "birthday":self.dateTime,
            # "qiaoId":"蓝朋友",
        }
        UserApi.updateUserInfo(data,self.token)

if __name__ == '__main__':
    unittest.main()

