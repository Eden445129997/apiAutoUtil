# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class package_deleteVideoFromPackage(unittest.TestCase):
    """从视频包中删除视频"""
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
        """从视频包中删除视频"""
        self.a()
        # self.b()

    def a(self):
        """从视频包中删除视频"""
        data = {
            "packageId":"1",
            "videoId":"617023035135754241",
        }
        backHttp.deleteTalkingSkill(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "packageId":"1",
            "videoId":"617022218112306560",
        }
        backHttp.deleteTalkingSkill(data)

if __name__ == '__main__':
    unittest.main()

