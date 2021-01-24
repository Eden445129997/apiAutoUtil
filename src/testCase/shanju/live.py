#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import requests

from src.testCase.shanju import apiObj
from src.utils.ODBC import odbc

class collection(unittest.TestCase):
    # 初始化
    def setUp(self):
        # token
        self.token = "802d717c1809466797fc620119bc8f1e"
        self.phone_list = ['15361899636']
        self.user_id_list = []
        # for i in range(10):
        #     for j in range(10):
        #         self.phone_list.append('153618996%s%s'%(i,j))
        # print(self.phone_list)

    def tearDown(self):
        pass

    def test(self):
        # self.bind_user()
        # self.create_live_party()
        self.query_wolf_game_party()
        # self.create_wolf_game()
        # self.insert_real_auth()
        pass

    def bind_user(self):
        """设为达人"""
        # 目的：将这些手机号码的用户设为达人
        # 1、上面生成了100电话号码
        # 2、根据手机号码从数据库里面获取用户id
        #       1、从执行sql语句获取用户id
        # 3、循环发送请求
        db = odbc('juparty-business')
        sql = 'select user_id from `juparty-business`.ju_user where phone in (%s);'%str(self.phone_list)[1:-1]
        user_id = db.selectSQL(sql)

        for i in user_id[1]:
            self.user_id_list.append(i[0])

        for i in self.user_id_list:
            response = requests.post(
                url='http://10.113.248.198/sys_user/Organization/bindUser',
                data={
                    'respHtml': 0,
                    'orgId': 100020,
                    'userId': i,
                    'bindType': 1,
                    'remark': ''
                },
                headers={
                    'Cookie': 'admin_username=admin; PHPSESSID=kl838tn7mp8740d99dabb1lhe9; thinkphp_show_page_trace=0|0',
                    'X-Requested-With' : 'XMLHttpRequest'
                }
            )
            self.assertEqual(response.text, 200 ,msg="阿斯顿发")
            print(response.text)

    def create_live_party(self):
        """自动创建直播间"""
        for phone in self.phone_list:
            # 登陆
            data = {
                "phone": phone,
                "smsCode":"123456",
                "deviceId":"tester_eden_%s"%phone
            }
            response = apiObj.user_v1_user_login_phone(data, self.token)
            self.token = response.get('result').get('token')
            # 聚会初始化
            response = apiObj.party_v1_party_create_init({},self.token)
            serial_no = response.get('result').get('serialNo')
            # 创建直播间
            data = {
                "applyMicCoin": 0, "expectEndTime": 1602679900000, "expectStartTime": 1602676400000, "joinCoin": 0,
                "partyCategory": "[{\"categoryId\":26,\"title\":\"孤独治愈所\"}]",
                "partyCover": "http://dingdong-yuming.yuming11.com/liveCover/560258/1601962713916.jpg", "partyType": 2,
                "serialNo": serial_no, "title": '自动创建的直播间'
            }
            party_id = apiObj.party_v6_party_createWiseParty(data,self.token).get('result').get('partyId')
            # 加入直播间
            data = {
                "partyId": party_id,
                "agreePay": 0
            }
            apiObj.party_v2_party_join_id(data,self.token)
            # 开始直播
            data = {
                "partyId": party_id
            }
            apiObj.party_v2_party_start(data,self.token)

    def create_wolf_game(self):
        """创建狼人杀游戏"""
        # for phone in self.phone_list:
        #     # 登陆
        #     data = {
        #         "phone": phone,
        #         "smsCode":"123456",
        #         "deviceId":"tester_eden_%s"%phone
        #     }
        #     response = apiObj.user_v1_user_login_phone(data, self.token)
        #     self.token = response.get('result').get('token')

        # 快速加入
        query_data = {
            # 游戏id,狼人杀30100
            'gameId': 30100,
            # wolf_kill_01 - 6人，02 - 9人，03 - 12人
            'gameSubCode': 'wolf_kill_01',
            # [1: 私密酒局 2:达人酒局 3: 官方酒局 5游戏房]
            'partyType': 5
        }
        response = apiObj.party_v7_party_page_preCreate(query_data, self.token)
        print(response)

    def query_wolf_game_party(self):
        """查询狼人杀房间560258"""
        # 快速加入
        query_data = {
            # 游戏id,狼人杀30100
            'gameId': 30100,
            # wolf_kill_01 - 6人，02 - 9人，03 - 12人
            # 'gameSubCode': 'wolf_kill_01',
            # [1: 私密酒局 2:达人酒局 3: 官方酒局 5游戏房]
            'pageNum': 1,
            'pageSize': 100
        }
        response = apiObj.party_v7_party_partyPage_list(query_data, self.token)
        game_party_list = response.get('result').get('list')
        for i in game_party_list:
            print(i)

    def insert_real_auth(self):
        """app端创建合集"""
        db = odbc('juparty-business')
        sql = 'select user_id from `juparty-business`.ju_user where phone in (%s);'%str(self.phone_list)[1:-1]
        user_id = db.selectSQL(sql)

        for i in user_id[1]:
            self.user_id_list.append(i[0])

        for i in self.user_id_list:
            sql = "INSERT INTO `juparty-business`.ju_user_certification " \
                  "(certification_id,user_id,realname,identity_no,identity_img,living_snapshot_img,audit_third_status,audit_status,create_time,update_time,audit_third_time) VALUE" \
                  "(%s,%s,'Eden自动化测试数据','511111111111111122','','',1,1,1596868507220,1596868507220,1596868507220);"%(i,i)
            db.commitSQL(
                sql
            )


if __name__ == '__main__':
    unittest.main()
