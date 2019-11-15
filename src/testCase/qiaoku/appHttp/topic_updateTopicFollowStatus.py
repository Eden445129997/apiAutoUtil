import unittest

from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import RegisterLoginApi as LoginApi
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.app_http import UserApi


class registerLogin(unittest.TestCase):
    """修改用户对话题的关注状态"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjgyMDQxMTMsInVzZXJJZCI6NjE5OTg4OTI4MjU4MTEzNTM2LCJpc3MiOiJxaWFva3UifQ.81kxXZgRzGVmX6CKQ8lEp09zui_1sH2O4hIRERWyMAw"

    def test(self):
        pass

    def tearDown(self):
        # pass
        # 选择关注
        # self.a()
        # 取消关注
        self.b()

    def a(self):
        """选择关注"""
        data = {
            "chooseOrCancel":1,
            "topicId":"181"
        }
        UserApi.updateTopicFollowStatus(data,self.token)

    def b(self):
        """取消关注"""
        data = {
            "chooseOrCancel":2,
            "topicId":"181"
        }
        UserApi.updateTopicFollowStatus(data,self.token)


if __name__ == '__main__':
    unittest.main()

