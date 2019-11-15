# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class video_uploadFile(unittest.TestCase):
    """上传文件(阿里云点播)"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1OTg3NjksImV4cCI6MTU3MTE5MDc2OSwiYmFja191c2VyX2lkIjo2NjYsImlzcyI6InFpYW9rdV9iYWNrIn0.30i2L4PyCQ6kyF_aZ-8Ba2_4NxJAqmh7SL8p_1eiXPY"
    def test(self):
        pass

    def tearDown(self):
        # pass
        # 上传文件(阿里云点播)
        self.a()
        # 缺少token
        # self.b()

    def a(self):
        """上传文件(阿里云点播)"""
        data = {
            "file":2,
            "type":"617013666046279680",
            # "otherUserId":None
        }
        backHttp.uploadFile(data,self.token)

    def b(self):
        """缺少token"""
        data = {
            "file":2,
            "type":"617013666046279680",
            # "otherUserId":None
        }
        backHttp.uploadFile(data)


if __name__ == '__main__':
    unittest.main()

