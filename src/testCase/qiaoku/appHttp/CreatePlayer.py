import unittest

from apiAutoUtil.src.utils.ODBC import odbc
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject.back_http.BackLiveApi import backLiveApi

class createPlayer(unittest.TestCase):
    """敲酷手机验证码登录"""
    #初始化
    def setUp(self):
        # 用户手机号
        self.userPhone = 13656639027
        # 封装的接口
        self.API = backLiveApi()
        self.userDb = odbc("qiaoku_user")
        self.liveDb = odbc("qiaoku_live")

        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

    def tearDown(self):
        # 清理自动化的测试数据
        # deleteData(self.userPhone)
        pass

    def testCreatePlayer(self):
        # createTbPlayerInfo = {
        #     "userId" : "618463213624754176",
        #     "nickName" : "敲酷1567494720",
        #     "birthday" : "2019-09-04T10:59:59.596Z",
        #     # "avatar" : "https://ddiddo.com/image/cover/E0301A29401A48ED93C7A3D875FDFD34-6-2.png",
        #     "userPhone" : "17621240088",
        #     "mcnId" : 2,
        #     "gender" : 1,
        # }
        #
        # self.API.createTbPlayerInfo(createTbPlayerInfo)

        result = self.userDb.selectSQL("select * from tb_user_info where user_phone = %s;"%self.userPhone)
        user_id = result[0][1]

        if self.userDb.commitSQL("UPDATE `qiaoku_user`.`tb_user_info` set `player_mark`='1' where user_id = %s;"%user_id):
            print("设置成主播")

        nickName = result[0][3]
        birthday = result[0][4]
        gender = result[0][5]
        avatar = result[0][6]

        result = self.liveDb.selectSQL("select * from tb_player_info;")
        room_id = int(result[-1][2])
        room_id = room_id + 1

        result = self.liveDb.commitSQL("INSERT INTO `qiaoku_live`.`tb_player_info` "
                              "( `user_id`, `room_id`, `player_status`, `live_status`, `total_duration`, `mcn_id`, `birthday`, `gender`, `city`, `user_sign`, `udid`, `user_status`, `login_type`, `nick_name`, `avatar`, `avatar_large`, `live_count`, `user_fans_count`, `short_id`, `modified_id`, `user_phone`, `create_time`, `last_update_time`) "
                              "VALUES ( '%s', '%s', NULL, NULL, NULL, '2', '2019-09-03 17:41:34', '%s', NULL, NULL, NULL, NULL, NULL, '%s', '%s', NULL, '2', NULL, NULL, NULL, '15397070726', '2019-09-03 17:41:39', '2019-09-03 17:41:39');"%(user_id,room_id,gender,nickName,avatar))

        print(room_id)

if __name__ == '__main__':
    unittest.main()