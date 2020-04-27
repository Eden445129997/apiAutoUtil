# coding=UTF-8
import unittest

from src.testCase.qiaoku import api_obj


class collection(unittest.TestCase):
    """获取用户消息列表"""

    # 初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODQ2ODMzMzksInVzZXJJZCI6NjI3NDcyNDgxMjI5MjA5NjAwLCJ1c2VyUGxhdGZvcm0iOiJhcHAiLCJ1ZGlkIjoibG9naW4iLCJpc3MiOiJxaWFva3UifQ.DbaMjNZsF9ctSzQ8aZUIu_bqTTaWQhBFPnSJq0GSnyk"

    def tearDown(self):
        pass

    def test(self):
        self.listSubjects()

    def listSubjects(self):
        """app获取主题列表"""
        data = {
            "pageIndex": 1,
            "pageSize": 10,
        }
        api_obj.effects_listSubjects(data, self.token)

if __name__ == '__main__':
    unittest.main()
