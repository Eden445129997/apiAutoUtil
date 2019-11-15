# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class video_getVideoAllCategory(unittest.TestCase):
    """获取视频所有的分类"""
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
        # 获取视频所有的分类
        self.a()
        # 缺少token
        # self.b()

    def a(self):
        """获取视频所有的分类"""
        data = {
            "keyword":"景",
            "type":1,
            # "pageIndex":"623834273622786048",
            # "pageSize":"623834273622786048",
        }
        backHttp.getVideoAllCategory(data,self.token)

    def b(self):
        """缺少token"""
        data = {
            "keyword":2,
            "type":"小小马甲",
            # "pageIndex":"623834273622786048",
            # "pageSize":"623834273622786048",
        }
        backHttp.getVideoAllCategory(data)


if __name__ == '__main__':
    unittest.main()

