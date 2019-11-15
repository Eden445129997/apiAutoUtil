from apiAutoUtil.src.utils.Log import log
from apiAutoUtil.config.path import dataPath
from apiAutoUtil.src.utils.ODBC import odbc
from apiAutoUtil.src.utils.ParserMethod import parserMethod
from apiAutoUtil.config.gloVar import globalRides
import time

def rmToken(userId):
    """根据userId删除token"""
    rds,__ = globalRides()
    rds.delete("challenge:%s"%userId)
    rds.delete("smsCode:%s"%userId)
    return True if rds.delete("token:%s"%userId) else False

# 更新配置文件，连数据库，获取所有的表，更新
def updateDataBase():
    # 创建连接database.ini对象
    database = parserMethod(dataPath()+"dataBase.ini")
    # 创建连接qiaoku_user数据库对象
    userDb = odbc("qiaoku_user")
    videoDb = odbc("qiaoku_video")
    liveDb = odbc("qiaoku_live")
    homeDb = odbc("qiaoku_home")
    dataDb = odbc("qiaoku_data")

    # todo:用上面的方法获取所有需要初始化的表

    #更新dataBase.ini的数据库表配置
    for i in userDb.selectSQL("show tables"):
        database.setParser("userTable",i[0],i[0])
    #更新dataBase.ini的数据库表配置
    for i in videoDb.selectSQL("show tables"):
        database.setParser("videoTable",i[0],i[0])
    #更新dataBase.ini的数据库表配置
    for i in liveDb.selectSQL("show tables"):
        database.setParser("liveTable",i[0],i[0])
    #更新dataBase.ini的数据库表配置
    for i in homeDb.selectSQL("show tables"):
        database.setParser("homeTable",i[0],i[0])
    #更新dataBase.ini的数据库表配置
    for i in dataDb.selectSQL("show tables"):
        database.setParser("dataTable",i[0],i[0])
    # todo:上面的方法在指定的数据库中更新配置文件

    return database

# 根据手机号码，删除数据库所有数据
def deleteData(userPhone):
    list = []
    videoList = []
    logName = log()

    """更新配置文件，返回连接配置文件对象"""
    database = parserMethod(dataPath()+"dataBase.ini")
    # database = parserMethod(dirPath.dataPath()+"dataBase.ini")

    # 创建连接qiaoku_user数据库对象
    userDb = odbc("qiaoku_user")
    # 创建连接qiaoku_user数据库对象
    videoDb = odbc("qiaoku_video")
    # 创建连接qiaoku_user数据库对象
    liveDb = odbc("qiaoku_live")
    # 创建连接qiaoku_user数据库对象
    homeDb = odbc("qiaoku_home")
    # 创建连接qiaoku_user数据库对象
    dataDb = odbc("qiaoku_data")

    # todo:用上面的方法获取所有需要初始化的表

    # 获取database.ini下配置的数据库所有表
    userTable = database.getOptions("userTable")
    videoTable = database.getOptions("videoTable")
    liveTable = database.getOptions("liveTable")
    homeTable = database.getOptions("homeTable")
    dataTable = database.getOptions("dataTable")

    logName.info("开始执行初始化配置")
    for i in range(1):
        user_id = [("624978533432688640","随意填充")]
        # user_id = userDb.selectSQL("select user_id from tb_user_info where user_phone = %s"%userPhone)
        # 如果userId（元组）有数据则删除用户数据
        """user库"""
        if len(user_id) >= 1:
            user_id = user_id[0][0]
            # 如果删除token成功，返回1则写日志，如果删除token失败则返回None写入日志
            logName.info("token清理成功：%s"%user_id) if rmToken(user_id) else logName.info("token清理失败：%s"%user_id)
            # 循环执行delete sql语句
            for i in userTable:
                # 如果存在该数据，返回True，执行数据删除
                if userDb.selectSQL("select * from %s where user_id = %s"%(i,user_id)):
                    try:
                        list.append(userDb.commitSQL("delete from %s where user_id = %s"%(i,user_id)))
                        time.sleep(0.01)
                    except:
                        logName.warning("初始化sql失败")

            """video库"""
            videoTuple = videoDb.selectSQL("select video_id from tb_video where user_id = %s"%user_id)
            if len(videoTuple) >= 1:
                videoList = [i for i in videoTuple]
                # 遍历该用户下的video视频列表
                for video_id in videoList:
                    # 遍历video库的表，都根据用户的video视频删除
                    for i in videoTable:
                        # 如果存在该数据，返回True，执行数据删除
                        if videoDb.selectSQL("select * from %s where video_id = %s"%(i,video_id[0])):
                            try:
                                list.append(videoDb.commitSQL("delete from %s where video_id = %s"%(i,video_id[0])))
                                time.sleep(0.01)
                            except:
                                logName.warning("初始化sql失败")

            """live库"""
            room_id = liveDb.selectSQL("select room_id from tb_player_info where user_id = %s"%user_id)
            if len(room_id) >= 1:
                for i in liveTable:
                    # 如果存在该数据，返回True，执行数据删除
                    if liveDb.selectSQL("select * from %s where room_id = %s"%(i,room_id[0][0])):
                        try:
                            list.append(liveDb.commitSQL("delete from %s where room_id = %s"%(i,room_id[0][0])))
                            time.sleep(0.01)
                        except:
                            logName.warning("初始化sql失败")
                for i in liveTable:
                    # 如果存在该数据，返回True，执行数据删除
                    if liveDb.selectSQL("select * from %s where user_id = %s"%(i,user_id)):
                        try:
                            list.append(liveDb.commitSQL("delete from %s where user_id = %s"%(i,user_id)))
                            time.sleep(0.01)
                        except:
                            logName.warning("初始化sql失败")
            """home库"""
            for i in homeTable:
                # 如果存在该数据，返回True，执行数据删除
                if homeDb.selectSQL("select * from %s where user_id = %s"%(i,user_id)):
                    try:
                        list.append(homeDb.commitSQL("delete from %s where user_id = %s"%(i,user_id)))
                        time.sleep(0.01)
                    except:
                        logName.warning("初始化sql失败")
            # 一个用户可能有多个video视频
            for video_id in videoList:
                for i in homeTable:
                    # 如果存在该数据，返回True，执行数据删除
                     if homeDb.selectSQL("select * from %s where video_id = %s"%(i,video_id[0])):
                        try:
                            list.append(homeDb.commitSQL("delete from %s where video_id = %s"%(i,video_id[0])))
                            time.sleep(0.01)
                        except:
                            logName.warning("初始化sql失败")
            """data库"""
            for i in dataTable:
                # 如果存在该数据，返回True，执行数据删除
                if homeDb.selectSQL("select * from %s where user_id = %s"%(i,user_id)):
                    try:
                        list.append(homeDb.commitSQL("delete from %s where user_id = %s"%(i,user_id)))
                        time.sleep(0.01)
                    except:
                        logName.warning("初始化sql失败")
            # 一个用户可能有多个video视频
            for video_id in videoList:
                for i in dataTable:
                    # 如果存在该数据，返回True，执行数据删除
                    if dataDb.selectSQL("select * from %s where video_id = %s"%(i,video_id[0])):
                        try:
                            list.append(dataDb.commitSQL("delete from %s where video_id = %s"%(i,video_id[0])))
                            time.sleep(0.01)
                        except:
                            logName.warning("初始化sql失败")

            # todo:这里是for循执行其他数据库SQL的地方，如上面for循环代码


                # 统计失败次数
                countFalse = len([i for i in list if not i])
                # 存在失败sql，写入日志
                if countFalse > 0:
                    logName.error("初始化sql失败数:%s"%countFalse)

                # 有失败的sql则返回False
                return True if countFalse == 0 else False
        else:
            # userDb.commitSQL("INSERT INTO `qiaoku_user`.`tb_user_info` "
            #              "(`id`, `user_id`, `qiaoku_id`, `nick_name`, `birthday`, `gender`, `avatar`, `avatar_large`, `user_phone`, `province`, `city`, `region`, `user_sign`, `user_origin`, `belong_back_user`, `udid`, `user_status`, `talent_mark`, `player_mark`, `total_publish_count`, `total_thumb_up_count`, `total_collection_count`, `user_follow_count`, `user_fans_count`, `binding_wx`, `binding_qq`, `del_flag`, `create_time`, `last_update_time`) "
            #              "VALUES ('1', '111111111111111111', '1111111111', 'EdenTestUser', NULL, '3', 'https://thirdwx.qlogo.cn/mmopen/vi_32/iblOuNxMNQoloaPo5xMM0acNt5jezgAyAIpnNDpRjJWDCxficmU4DPMEONuzpWor7FXOLDtYWIq8zOHHptpULUoQ/132', NULL, '12345678901', '', '', NULL, NULL, '0', NULL, '64d96dba-2e5f-4168-ade8-06652cbafeec', '1', '2', '1', NULL, NULL, NULL, NULL, NULL, '1', '2', '0', '2019-08-19 20:52:59', '2019-08-19 20:53:55');")
            # pass
            logName.warning("tb_user_info没有该用户数据，请确认是否存在绑定该手机号的用户")
        return True