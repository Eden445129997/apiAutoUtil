# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class video_selectUnderLineVideoPage(unittest.TestCase):
    """查询下架视频分页列表"""
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
        # 查询下架视频分页列表
        self.a()
        # 缺少token
        # self.b()

    def a(self):
        """查询下架视频分页列表"""
        data = {
            "searchType":1,
            "keywords":"1567563122",
            # "categoryId":16,
        }
        backHttp.selectUnderLineVideoPage(data,self.token)

    def b(self):
        """缺少token"""
        data = {
            "searchType":1,
            "keywords":"1567563122",
            # "categoryId":16,
        }
        backHttp.selectUnderLineVideoPage(data)


if __name__ == '__main__':
    unittest.main()

