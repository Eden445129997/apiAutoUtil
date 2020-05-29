#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.testCase.qiaoku import api_obj
from src.script.敲酷业务脚本 import randomValue

class audit(unittest.TestCase):
    """获取用户消息列表"""

    # 初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODQ1OTc4NzcsInVzZXJJZCI6NjI3NDcyNDgxMjI5MjA5NjAwLCJ1c2VyUGxhdGZvcm0iOiJhcHAiLCJ1ZGlkIjoibG9naW4iLCJpc3MiOiJxaWFva3UifQ.Bw1ytO1nOZ3hPxuY3ZHR62qUvanTDJwJhUFNv49zld0"

    def tearDown(self):
        pass

    def test(self):
        # 初始化应用
        # self.app_info_init()
        # 获取用户消息列表
        self.user_report()
        # self.room_report()
        # self.live_report ()

    def app_info_init(self):
        data = {
            "appName": "eden_test"
        }
        api_obj.audit_appInfo_init(data,self.token)

    def user_report(self):
        """app端创建合集"""
        for i in range(1):
            data = {
                "appId": "eden",
                "appSecret": "123456789",
                "callback": "http://10.113.248.142:9998/platform/test/",
                "btId": randomValue(10),
                # "type": "NAME",
                "type": "AVATAR",
                "userId": "123456789",
            }
            if data.get("type") == "NAME":
                data["content"] = "eden_test"
            else:
                data["content"] = "http://didongpic.didongkj.com/1585896083549.png"
            api_obj.audit_user_report(data, self.token)

    def room_report(self):
        """app端创建合集"""
        for i in range(1):
            data = {
                "appId": "eden",
                "appSecret": "123456789",
                "callback": "http://10.113.248.142:9998/platform/test/",
                "btId": randomValue(10),
                "type": "RULE", # 类型（RULE, NAME）
                "userId": "123456789",
                # "content": "eden_test_room",
                "content": "https://video.didongkj.com/image/cover/4336D37DBCF248009E75A27EC6528A00-6-2.png",
            }
            api_obj.audit_room_report(data, self.token)

    def live_report(self):
        """app端创建合集"""
        for i in range(1):
            data = {
                "appId": "eden",
                "appSecret": "123456789",
                "callback": "http://10.113.248.142:9998/platform/test/",
                "btId": randomValue(10),
                "partyId": "12345689",
                "imgs": [
                    {
                        "userId": "123456",
                      # "photo": "https://video.didongkj.com/image/cover/4336D37DBCF248009E75A27EC6528A00-6-2.png",
                        "photo": "http://www.xinhuanet.com/photo/18cpcnc/2012-11/15/123959140_11n.jpg",#习近平
                        "snapTime": "2020-04-14 19:50:14"
                    },
                ],
            }
            api_obj.audit_live_report(data, self.token)

if __name__ == '__main__':
    unittest.main()
