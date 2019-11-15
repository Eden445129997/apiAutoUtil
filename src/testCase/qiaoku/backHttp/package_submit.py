# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class package_submit(unittest.TestCase):
    """添加视频运营包"""
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
        """添加视频运营包"""
        self.a()
        # self.b()

    def a(self):
        """添加视频运营包"""
        data = {
            "name":"添加视频运营包",
            "imageUrl":"http://video.didongkj.com/image/cover/8CAE0088FAF04CDC9CD47543D88CACDB-6-2.png",
            "displayStatus":1,
        }
        backHttp.package_submit(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "name":"添加视频运营包",
            "imageUrl":"http://video.didongkj.com/image/cover/8CAE0088FAF04CDC9CD47543D88CACDB-6-2.png",
            "displayStatus":1,
        }
        backHttp.package_submit(data)

if __name__ == '__main__':
    unittest.main()
