# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class user_getUserDataList(unittest.TestCase):
    """获取用户列表"""
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
        """获取用户列表"""
        self.a()
        # self.b()

    def a(self):
        """获取用户列表"""
        data = {
            # "nickName":"敲酷1567916372",
            "userId":"1318180023",
            # "userPhone":"tou_xiang",
            # "talentMark":2,
            # "userOrigin":0,
            # "generalUser":1,
            # "totalPublishCount":1,
            # "userFansCount":1,
            # "totalThumbUpCount":1,
            # "totalCollectionCount":1,
            # "startNumber":1,
            # "endNumber":1,
            "pageIndex":1,
            "pageSize":10,
        }
        backHttp.getUserDataList(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "nickName":"",
            # "userId":"i_am_majia",
            # "userPhone":"tou_xiang",
            # "talentMark":2,
            # "userOrigin":1,
            # "generalUser":1,
            # "totalPublishCount":1,
            # "userFansCount":1,
            # "totalThumbUpCount":1,
            # "totalCollectionCount":1,
            # "startNumber":1,
            # "endNumber":1,
            "pageIndex":0,
            "pageSize":1,
        }
        backHttp.getUserDataList(data)

if __name__ == '__main__':
    unittest.main()

