# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class videoTopic_editVideoTopics(unittest.TestCase):
    """编辑话题"""
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
        """编辑话题"""
        self.a()
        # self.b()

    def a(self):
        """编辑话题"""
        data = {
            "topicName":"地动热门/推荐",
            "imageUrl":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3276179142,1686381254&fm=26&gp=0.jpg",
            "displayStatus":1,
            "recommendStatus":"1",
            "hotStatus":1,
            # "operator":666,
            "remark":"Eden",
            "id":18,
        }
        backHttp.editVideoTopics(data,self.token)

    def b(self):
        """不带token"""
        data = {
            "topicName":"地动热门/推荐",
            "imageUrl":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3276179142,1686381254&fm=26&gp=0.jpg",
            "displayStatus":1,
            "recommendStatus":"1",
            "hotStatus":1,
            # "operator":666,
            "remark":"Eden",
            "id":18,
        }
        backHttp.editVideoTopics(data)

if __name__ == '__main__':
    unittest.main()
