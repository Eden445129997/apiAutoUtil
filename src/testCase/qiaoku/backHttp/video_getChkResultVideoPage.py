# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class video_getChkResultVideoPage(unittest.TestCase):
    """获取审核结果视频列表"""
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
        """获取审核结果视频列表"""
        self.a()
        # self.b()

    def a(self):
        """获取审核结果视频列表"""
        # "personChkStatus":人工审核状态（3 审核通过（复审）； 4审核不通过）
        data = {
            # "startCheckTime":"2019-01-08T16:00:00.000Z",
            # "endCheckTime":"2019-16-08T16:00:00.000Z",
            # "topicId":"1",
            "videoLevel":"b",
        }
        backHttp.getChkResultVideoPage(data,self.token)

    def b(self):
        """不带token"""
        data = {
            # "startCheckTime":"2019-01-08T16:00:00.000Z",
            # "endCheckTime":"2019-16-08T16:00:00.000Z",
            # "topicId":"1",
            "videoLevel":"s",
        }
        backHttp.getChkResultVideoPage(data)


if __name__ == '__main__':
    unittest.main()

