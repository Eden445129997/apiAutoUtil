# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.backHttp import createTbMcnInfo


class mcnInfo_createTbMcnInfo(unittest.TestCase):
    """敲酷手机验证码登录"""
    #初始化
    def setUp(self):
        # 用户手机号
        self.userPhone = 15361899636
        self.smsCode = 1761
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)
        # self.userId,self.token = login(self.userPhone,self.smsCode)
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjgyMDQxMTMsInVzZXJJZCI6NjE5OTg4OTI4MjU4MTEzNTM2LCJpc3MiOiJxaWFva3UifQ.81kxXZgRzGVmX6CKQ8lEp09zui_1sH2O4hIRERWyMAw"
        print(self.token)

    def tearDown(self):
        # 清理自动化的测试数据
        # deleteData(self.userPhone)
        pass

    def testLogin(self):
        data = {
            "mcnName":"杰哥贼牛逼",
            "displayStatus":1
        }
        createTbMcnInfo(data)

if __name__ == '__main__':
    unittest.main()

