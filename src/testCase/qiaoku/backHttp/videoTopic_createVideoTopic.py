# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.backHttp import createVideoTopic


class videoTopic_createVideoTopic(unittest.TestCase):
    """创建视频话题"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1OTg3NjksImV4cCI6MTU3MTE5MDc2OSwiYmFja191c2VyX2lkIjo2NjYsImlzcyI6InFpYW9rdV9iYWNrIn0.30i2L4PyCQ6kyF_aZ-8Ba2_4NxJAqmh7SL8p_1eiXPY"

    def tearDown(self):
        # 清理自动化的测试数据
        # deleteData(self.userPhone)
        pass

    def test(self):
        # pass
        # 创建话题
        self.a()

    def a(self):
        """创建热门/推荐话题"""
        data = {
            "topicName":"地动热门/推荐",
            # "imageUrl":1,
            "displayStatus":"1",
            "recommendStatus":"1",
            "hotStatus":"1",
            "remark":"Eden",
        }
        createVideoTopic(data)

if __name__ == '__main__':
    unittest.main()

