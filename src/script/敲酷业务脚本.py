#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re,time,random,os#,urllib3
from src.utils.ODBC import odbc
# from src.utils.Log import log
from src.testCase.qiaoku import apiObj
from config.gloVar import globalRides
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

def getPhoneNum():
    """生成手机号码"""
    randomString = ""
    for i in range(8):
        toString = str(random.randint(0,9))
        randomString = randomString + toString
    return "153" + randomString

def getSmsCode(phone):
    """获取验证码"""
    rds,__ = globalRides()
    token = rds.get("user:smsCode:app-86-%s"%phone)
    # 获取token
    return str(token)

def randomValue(maxNumber):
    """随机获取列表的某个下标"""
    randomValue = ""
    # 36个数
    value = "abcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(maxNumber):
        ranIndex = random.randint(0,len(value)-1)
        randomValue = randomValue + value[ranIndex]
    return randomValue

def login(userPhone,smsCode=None, udid=None):
    """根据手机号获取账号ID/token"""

    userPhone = str(userPhone)
    smsCode = smsCode
    if not udid:
        udid = randomValue(18)
        udid = "tester_eden" + udid

    ykLoginParams = {
        "udid": udid,
    }
    # 游客登录
    response = apiObj.login_ykLogin(ykLoginParams)
    # print(response)
    assert response.get("code") == 200,"状态码错误"

    try:
        userId = response.get("data").get("userId")
        accessToken = response.get("data").get("accessToken")
    except:
        return False,False,False

    # 如果有验证码，则登录，并且获取登录token
    if smsCode:
        smsCode = str(smsCode)
        checkSmsCodeData = {
                "userPhone":userPhone,
                "type":"1",
                "udid": udid,
            }

        checkSmsCodeData["smsCode"] = str(smsCode)

        # 验证短信验证码——登录——将touken传入请求头
        response = apiObj.login_checkSmsCode(checkSmsCodeData, accessToken)
        assert response.get("code") == 200,"状态码错误"
        accessToken = response.get("data").get("accessToken")
        return userId,accessToken,udid

    # 如果没有验证码，则获取验证码到手机号
    else:
        startCaptchaParams = {
            "userPhone":userPhone,
        }
        # 极验初始化
        response = apiObj.login_startCaptcha(startCaptchaParams)
        assert response.get("code") == 200,"状态码错误"

        getSmsCodeParams = {
                "userPhone":userPhone,
                "udid": udid,
                "dialCode":86,
                # ""
            }

        getSmsCodeParams["challenge"] = response.get("data").get("challenge")
        getSmsCodeParams["type"] = "1"
        # 获取短信验证码
        response = apiObj.login_getSmsCode(getSmsCodeParams)
        # print(response)
        assert response.get("code") == 200,"状态码错误"
        return userId,False,udid

def autoLogin(phoneNum):
    """自动登录获取userId，token"""

    # 发送验证码
    userId,accessToken,udid = login(phoneNum)

    time.sleep(1)

    # 获取redis的smsCode
    smsCode = getSmsCode(phoneNum)
    time.sleep(1)
    # print(smsCode)
    if smsCode:
        # 处理redis获取的数据提取验证码
        smsCode = re.findall(r'\d+',smsCode)
        print(smsCode)
        assert len(smsCode) == 1,"状态码错误"
        smsCode = smsCode[0]

        # 登录获取token
        userId,token,udid = login(phoneNum,smsCode,udid)

        return userId,token,udid
    return False,False,False

def getVideoId():
    """从数据库中直接获取100个上架视频id"""
    db = odbc("qiaoku_video")
    dump = db.selectSQL("select video_id from tb_video where video_up_down_status = 3 limit 0,100;")
    # print(dump)
    video_list = [dump[1][i][0] for i in range(len(dump[1]))]
    # print(video_list)
    return video_list

def getUserId():
    """从数据库中直接获取100个上架视频id"""
    db = odbc("qiaoku_user")
    dump = db.selectSQL("select user_id from tb_user_info where del_flag = 0 limit 0,100;")
    # print(dump)
    user_list = [dump[1][i][0] for i in range(len(dump[1]))]
    # print(len(user_list))
    # print(user_list)
    return user_list

def addVideoThumbsUp(videoId,thumbsUpNum):
    """给视频点赞"""

    # videoId 视频Id
    # thumbsUpNum 点赞次数

    for i in range(thumbsUpNum):
        # 获取手机号码
        phoneNum = getPhoneNum()

        # 登录获取token
        userId,token = autoLogin(phoneNum)

        # 点赞视频
        data = {
            "videoId":"%s"%videoId,
            "thumbStatus":"1",
        }

        response = apiObj.videoPlay_addThumbsUp(data, token)

def addVideoCommentThumbsUp(videoId,thumbsUpNum):
    """给视频下所有评论点赞"""
    # 视频Id
    # 点赞次数

    for i in range(thumbsUpNum):
        # 获取手机号码
        phoneNum = getPhoneNum()

        time.sleep(1)

        # 登录获取token
        userId,token = autoLogin(phoneNum)

        videoDatabase = odbc("qiaoku_video")
        cIdList = videoDatabase.selectSQL("select c_id from tb_video_comment where video_id = '%s';"%videoId)

        print(cIdList)

        # 循环获取这个视频下的所有评论,并且点赞
        for i in range(1,len(cIdList)):
            cId = cIdList[i]
            # print(cId)
            data = {
                "videoId":"%s"%videoId,
                "cId":"%s"%cId,
                "thumbStatus":"1",
            }
            apiObj.videoPlay_addCommentThumbsUp(data, token)
            # print(cId)

def removePunish(userPhone=None,userId=None):
    """给用户解除封禁"""
    userDb = odbc("qiaoku_user")
    if userPhone:
        userId = userDb.selectSQL("select user_id from tb_user_info where user_phone ='%s'"%userPhone)[1]

    if userId:
        # 如果获取到userId，则解封
        userDb.commitSQL("update tb_user_info set user_status = '1' where user_id = '%s'"%userId)
        homeDb = odbc("qiaoku_home")
        homeDb.commitSQL("delete from tb_punish_record where user_id = '%s'"%userId)
        homeDb.commitSQL("delete from tb_report where report_enum_id = '%s'"%userId)

        # 删除封号缓存
        rds,__ = globalRides()
        excuteRedis = rds.delete("userStatus:%s"%userId)
        # if excuteRedis == 1:
        #     setlog = log()
        #     setlog("清除缓存失败——userStatus:%s"%userId)
        return True
    return False

def successPassVideoInitialCheck():
    """视频审核通过"""
    data = {
        # 视频审核ID
        "id":"427",
        # 视频分类ID
        "categoryId":"4",
        # 标签列表
        "labels":["15"],
        # 视频定级
        "videoLevel":"b",
        "videoId":"704378332622258176",
        #
        "videoTopicId":43,

    }
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODc4MDYwMDUsImJhY2tfdXNlcl9pZCI6NDMsImlzcyI6InFpYW9rdV9iYWNrIn0.zD2II7nLGMSaLev1a2nCD6LJAtsX9eFeYF8-5fYdfwE"

    response = apiObj.videosuccessPassVideoInitialCheck(data, token)

    return True

def failPassVideoInitialCheck():
    """视频审核不通过"""
    data = {
        "id":"289",
        "functionOrigin":"101",
        "videoReason":"%E5%A4%AA%E4%B8%91",
    }
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODM0ODQxOTEsImJhY2tfdXNlcl9pZCI6NDMsImlzcyI6InFpYW9rdV9iYWNrIn0.XZS2M_h9Jmo0gcCjeHGOhgDIX33azObiDj_sIiQrJUM"
    response = apiObj.videofailPassVideoInitialCheck(data, token)

    return True

def autoCheckComment():
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODk3ODY4NTUsImJhY2tfdXNlcl9pZCI6NDMsImlzcyI6InFpYW9rdV9iYWNrIn0.2qblJDRLoN1v7GJNTdp8Y72V-H0EgiH0brjioINR6Bo"
    while True:
        data = {
        }
        response = apiObj.videoCommentChk_check_wait(data, token)
        comment_check_list = response.get("data")
        if comment_check_list:
            for i in range(len(comment_check_list)):
                check_id = comment_check_list[i].get("id")
                # print(type(check_id))
                dataList = []
                jsonData = {
                    "id":"%s"%check_id,
                    "result":"PASS"
                }
                jsonData = json.dumps(jsonData)
                dataList.append(jsonData)

                apiObj.videoCommentChk_doCheck(dataList, token)

def test():
    """测试推荐接口"""
    # userId,token,udid = autoLogin(15361899636)
    for i in range(100):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODcwOTQ3MTUsInVzZXJJZCI6NjI3NDcyNDgxMjI5MjA5NjAwLCJ1c2VyUGxhdGZvcm0iOiJhcHAiLCJ1ZGlkIjoibG9naW4iLCJpc3MiOiJxaWFva3UifQ.nXjmUHzsH2ly2nS4rSNm5okMT6BGkT9M5dQUIkRzCHw"
        for i in range(3):
            if i == 1:
                # userId,token,udid = autoLogin(15353913452)#a
                token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODcxMDM1MTcsInVzZXJJZCI6Njg0NTQ5MTcyOTg4NTkyMTI4LCJ1c2VyUGxhdGZvcm0iOiJhcHAiLCJ1ZGlkIjoibG9naW4iLCJpc3MiOiJxaWFva3UifQ.2-RDpRa9lqcH9Km7lvkE2hEx4qhXHjRQ_J3hzoLHeY8"
            if i == 2:
                # userId,token,udid = autoLogin(15350711208)#c
                token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODcxMDM2MzYsInVzZXJJZCI6NzAwNzA4OTYyMTgwODAwNTEyLCJ1c2VyUGxhdGZvcm0iOiJhcHAiLCJ1ZGlkIjoibG9naW4iLCJpc3MiOiJxaWFva3UifQ.F_AJ2AFGEWUnN-9fByFQDce01D9WTsudnAy3AwUAUrg"
            data = {
                # "pageIndex": random.randint(1, 3),
                "pageIndex": 1,
                "pageSize": 10,
                "type": "recommend",
            }
            response = apiObj.video_getVideos(data, token)
            # print(response)
            arraylist = response.get("data")

            if len(arraylist) != 6:
                print("+"*50)
                print(len(arraylist))
                print(arraylist)

            video_db = odbc("qiaoku_video")

            for i in arraylist:
                videoId = i.get("videoId")
                boo = video_db.selectSQL("select id,video_id from qiaoku_video.tb_video where video_id = %s"%videoId)
                # print(boo)
                if not boo:
                    print("=="*50)
                    print(boo)
    # print(arraylist)
    # return True

def updateData():
    # videoDatabase = odbc("qiaoku_video")
    # biz_id = videoDatabase.selectSQL("select biz_id from tb_back_audit_task where type = '2' and status in (0,1);")[1]
    # print(biz_id)
    # for i in range(len(biz_id)):
    #     videoDatabase.commitSQL("update tb_back_audit_task SET back_user_id = 43,status = 2 where biz_id = '%s';"%biz_id[i][0])
    #     videoDatabase.commitSQL("UPDATE `qiaoku_video`.`tb_video_comment_chk` SET `machine_chk_status`='2',`risk_label`='审核通过', `reason`='审核通过' where c_id = '%s';"%biz_id[i][0])
    #     videoDatabase.commitSQL("update tb_video_comment SET chk_status = 3 where c_id = '%s';"%biz_id[i][0])
    pass


# def auth():
#     userDb = odbc("qiaoku_user")
#     datalist = userDb.selectSQL("select * from tb_backuser_auth where backuser_id ='39'")
#     # print(datalist)
#
#     j = 549
#     for i in datalist[1]:
#         userDb.commitSQL("INSERT INTO `qiaoku_user`.`tb_backuser_auth` (`id`, `backuser_id`, `auth_id`, `role_id`, `enabled`, `create_time`, `last_update_time`) values(%s,44,%s,%s,%s,'2020-01-13 10:20:50','2020-01-13 10:20:50');"%(j,i[2],i[3],i[4]))
#         j = j+1

def getTokenTxt(token_num):
    """获取token写入txt文本"""
    token_list = []
    for i in range(token_num):
        phone_num = getPhoneNum()
        userId,accessToken,udid = autoLogin(phone_num)
        token_list.append(accessToken)
    for i in range(len(token_list)):
        with open (os.path.dirname(os.path.abspath(__file__)) + "\\" + "token.txt", 'a',encoding='utf-8') as fp:
            fp.write (token_list[i] + "\n")
            fp.flush()
            fp.close()

# 627472481229209600
def getUserVideoChk(user_id):
    videoDb = odbc("qiaoku_video")
    chk_id_list =[]
    video_id_list = videoDb.selectSQL("select video_id from tb_video where user_id ='%s'"%user_id)[1]
    print(video_id_list)
    for video_id in video_id_list:
        chk_id = videoDb.selectSQL("select id from tb_video_chk where video_id ='%s'" % video_id[0])
        chk_id_list.append(chk_id)
        print(chk_id)
    print(chk_id_list)

if __name__ == '__main__':
    # getUserVideoChk(627472481229209600)
    # auth()
    # autoCheckComment()
    # test()
    # 审核通过
    # successPassVideoInitialCheck()
    # 审核不通过
    # failPassVideoInitialCheck()
    # 登录
    # userId,token,udid = autoLogin(15361899636)
    # userId,token,udid = login(15361899636,1111)
    # print(token)

    # 自动登录
    # for i in range(30):
    #     phone_num = getPhoneNum()
    #     userId,accessToken,udid = autoLogin(phone_num)
    #     with open (os.path.dirname(os.path.abspath(__file__)) + "//" + "token.txt", 'a',encoding='utf-8') as fp:
    #         fp.write (accessToken + "\n")
    #         fp.flush()
    #         fp.close()

    # print(os.path.dirname(os.path.abspath(__file__)))

    # print(userId,accessToken)
    # 从数据库获取视频id

    # videoid = getVideoId()
    # for i in range(100):
    #     for i in videoid:
    #         with open (os.path.dirname(os.path.abspath(__file__)) + "\\" + "videoId.txt", 'a',encoding='utf-8') as fp:
    #             fp.write (str(videoid) + "\n")
    #             fp.flush()
    #             fp.close ()
    # 从数据库获取视频id
    # getUserId()

    # 获取验证码
    smsCode = getSmsCode(15361899636)
    print(smsCode)

    # 账号解封
    # removePunish(userPhone=15658850486,userId=None)
    # 给视频点赞
    # addVideoThumbsUp(648474719883886592,5)
    # 给视频评论点赞
    # addVideoCommentThumbsUp(627550301049585664,1)
    pass