# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp

class poPush_send(unittest.TestCase):
    """添加官方推送"""
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
        """添加官方推送"""
        self.a()
        # self.b()

    def a(self):
        data = {
            "mainTitle":"主标题",
            "subTitle":"副标题",
            "banner":"banner图",
            "contentType":"3",                                #内容类型 1.URL内容 2.图文内容 3.话题内容 4.视频内容
            "pushTextContent":"推送的文本内容-除了图文",
            # "pushPhotoText":"推送的图文",
            "sendType":"2",                                     #发送方式 1定时发送 2立即发送
            # "sendTime":"",
            "pushPeople":"1",                                   #推送人群 1全部用户 2普通用户 3达人用户
            "pushSystem":"1",                                  #推送系统 1全部系统 2Android 3ios
        }
        backHttp.poPush_add(data)

if __name__ == '__main__':
    unittest.main()