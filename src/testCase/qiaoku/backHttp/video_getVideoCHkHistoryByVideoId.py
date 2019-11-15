# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class mcnInfo_createTbMcnInfo(unittest.TestCase):
    """通过videoId获取视频审核历史"""
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
        """通过videoId获取视频审核历史"""
        self.a()
        # self.b()

    def a(self):
        """通过videoId获取视频审核历史"""
        # type 1 审核
        # type 2 上下架
        # type 3 视频推荐
        # type 4 用户权限
        # type 5 用户头像
        # type 6 用户昵称
        # type 7 个性签名
        # type 8 敲ID

        data = {
            "videoId":621746727497498624,
        }
        backHttp.selectChkLogByVideoId(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "videoId":617023035135754241,
        }
        backHttp.selectChkLogByVideoId(data)


if __name__ == '__main__':
    unittest.main()

