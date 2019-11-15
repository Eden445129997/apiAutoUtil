# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class userModifyRecord_failPassCheck(unittest.TestCase):
    """用户信息审核不通过接口"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)
        # self.userId,self.token = login(self.userPhone,self.smsCode)
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1OTg3NjksImV4cCI6MTU3MTE5MDc2OSwiYmFja191c2VyX2lkIjo2NjYsImlzcyI6InFpYW9rdV9iYWNrIn0.30i2L4PyCQ6kyF_aZ-8Ba2_4NxJAqmh7SL8p_1eiXPY"
        # print(self.token)

    def tearDown(self):
        # 清理自动化的测试数据
        # deleteData(self.userPhone)
        pass

    def test(self):
        """用户信息审核不通过接口"""
        self.a()
        # self.b()

    def a(self):
        """用户信息审核不通过接口"""
        data = {
            "id":"308",
            "reason":"AAAAA",
        }
        backHttp.userModifyRecord_failPassCheck(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "id":"307",
            "reason":"AAAA",
        }
        backHttp.userModifyRecord_failPassCheck(data)

if __name__ == '__main__':
    unittest.main()

