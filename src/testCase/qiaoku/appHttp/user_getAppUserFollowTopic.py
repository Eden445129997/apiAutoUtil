import unittest
from src.testCase.qiaoku import api_obj

class user_updateBlackUserList(unittest.TestCase):
    """获取用户关注的话题"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)
        # date_str = '2017-10-19'
        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODg3NDkxMTcsInVzZXJJZCI6NjI3NDcyNDgxMjI5MjA5NjAwLCJ1c2VyUGxhdGZvcm0iOiJhcHAiLCJ1ZGlkIjoibG9naW4iLCJpc3MiOiJxaWFva3UifQ.aq__ldl-l_3KwUvJFJq3r29DUOvgPlddTj8hJ91IdB8"

    def test(self):
        pass

    def tearDown(self):
        # pass
        # 获取用户关注的话题
        self.a()

    def a(self):
        """获取用户关注的话题"""
        data = {
            # "otherUserId":"618815311222669312",
            "pageIndex": 1,
            "pageSize": 10
        }
        api_obj.user_getAppUserFollowTopic(data,self.token)

if __name__ == '__main__':
    unittest.main()
