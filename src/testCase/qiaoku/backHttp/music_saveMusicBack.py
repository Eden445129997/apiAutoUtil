# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp

class music_saveMusicBack(unittest.TestCase):
    """上传音乐(后台)"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)
        # self.userId,self.token = login(self.userPhone,self.smsCode)
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjgyMDQxMTMsInVzZXJJZCI6NjE5OTg4OTI4MjU4MTEzNTM2LCJpc3MiOiJxaWFva3UifQ.81kxXZgRzGVmX6CKQ8lEp09zui_1sH2O4hIRERWyMAw"
        print(self.token)

    def tearDown(self):
        # 清理自动化的测试数据
        # deleteData(self.userPhone)
        pass

    def test(self):
        """上传音乐(后台)"""
        self.a()
        # self.b()

    def a(self):
        data = {
            "coverPhoto":"封面",
            "musicUrl":"Eden的测试url",
            "musicName":"音乐名字",
            "timeLength":"6",
            "singer":"Eden",
            "isDisplay":"1",
            "uploadType":"1",
            "uploadUserId":"1",
            "aliMusicId":"阿里云id",
        }
        backHttp.saveMusicBack(data)

if __name__ == '__main__':
    unittest.main()