#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.testCase.shanju import apiObj

class collection(unittest.TestCase):
    # 初始化
    def setUp(self):
        # token
        self.token = "0beb1ff21ffb4008b18228c317100910"

    def tearDown(self):
        pass

    def test(self):
        # self.smscode()
        # self.login()
        # self.save1()
        # self.version()
        self.version_one()

    def smscode(self):
        """app端创建合集"""
        data = {
            "phone":"15361899636",
            # "phone": "15219890524",

            "smsType":1,
        }
        response = apiObj.user_v1_user_send_smscode(data, self.token)
        print(response)
        # token = response.get()
        # global token

    def login(self):
        """app端创建合集"""
        data = {
            "phone":"15361899636",
            "smsCode":"123456",
            "deviceId":"tester_eden"
        }
        apiObj.user_v1_user_login_phone(data, self.token)

    def save1(self):
        """app端创建合集"""
        data = {
            "userId":245661,
            "gameType":27477747
        }
        apiObj.party_v4_shandong_game_check(data, self.token)

    def version(self):
        """app端创建合集"""
        data = {
        }
        headers = {}
        # apiObj.user_v1_sys_last_version(data, self.token)
        while True:
            for i in range(0,5):
                for j in range(0,12):
                    # 中间
                    middle_int = str(i)
                    last_int = str(j)
                    version = '1.%s.%s'%(middle_int,last_int)

                    # headers = {
                    #     "device": "ios",
                    #     "version": version
                    # }

                    version = '1.2.%s.%s'%(middle_int,last_int)
                    headers = {
                        "device": "android",
                        "version": version
                    }

                    apiObj.user_v1_sys_last_version(data, self.token, headers)

    def version_one(self):
        data = {
        }
        # version = '1.1.1.0'
        # version = '1.2.2.9'
        version = '1.2.12'
        # version = '1.2.10'178

        headers = {
            "device": "android",
            "version": version
        }
        apiObj.user_v1_sys_last_version(data, self.token, headers)


if __name__ == '__main__':
    unittest.main()
