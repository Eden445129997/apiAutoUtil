# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import VideoPlay


class videoPlay_saveReport(unittest.TestCase):
    """举报视频/评论/用户"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1MDg2NzAsInVzZXJJZCI6NjIxNzc1NDU1MzA0ODEwNDk2LCJpc3MiOiJxaWFva3UifQ.dpnceZSaXpVYbY4zp_z8yIlCGuarR-c-n4AjvlcRf7k"

    def tearDown(self):
        pass

    def test(self):
        # 举报视频/评论/用户
        self.a()
        # 不带token
        # self.b()

    def a(self):
        """举报视频/评论/用户"""
        data = {
            "otherUserId":"621775455304810496",
            "reportEnumId":"621775455304810496",
            "reportCategoryReason":"too handsome"*100,
            "type":"5",
        }
        VideoPlay.saveReport(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "otherUserId":"621775455304810496",
            "reportEnumId":"621775455304810496",
            "reportCategoryReason":"too handsome",
            "type":"5",
        }
        VideoPlay.saveReport(data)


if __name__ == '__main__':
    unittest.main()
