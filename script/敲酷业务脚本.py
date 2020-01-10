#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import random
import time
from src.utils.ODBC import odbc
# from src.utils.Log import log
from src.testCase.qiaoku.interfaceObject import appHttp
from config.gloVar import globalRides

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
    token = rds.get("smsCode:%s"%phone)
    # 获取token
    return str(token)

def login(userPhone,smsCode=None):
    """根据手机号获取账号ID/token"""

    userPhone = str(userPhone)
    smsCode = smsCode

    ykLoginParams = {
        "udid":"123",
    }
    # 游客登录
    response = appHttp.ykLogin(ykLoginParams)

    userId = response.get("data").get("userId")
    accessToken = response.get("data").get("accessToken")

    # 如果没有验证码，则获取验证码到手机号
    if not smsCode:
        startCaptchaParams = {
            "userPhone":userPhone,
        }
        # 极验验证
        response = appHttp.startCaptcha(startCaptchaParams)

        getSmsCodeParams = {
                "userPhone":userPhone,
                "udid":"abcefg",
            }

        getSmsCodeParams["challenge"] = response.get("data").get("challenge")
        getSmsCodeParams["type"] = "1"
        # 获取短信验证码
        response = appHttp.getSmsCode(getSmsCodeParams)

    # 如果有验证码，则登录，并且获取登录token
    if smsCode:
        smsCode = str(smsCode)
        checkSmsCodeData = {
                "userPhone":userPhone,
                "type":"1",
                "udid":"abcefg",
            }

        checkSmsCodeData["smsCode"] = str(smsCode)

        # 验证短信验证码——登录——将touken传入请求头
        response = appHttp.checkSmsCode(checkSmsCodeData,accessToken)
        accessToken = response.get("data").get("accessToken")
        return userId,accessToken
    return userId,False

def autoLogin(phoneNum):
    """一键登录获取userId，token"""

    # 发送验证码
    login(phoneNum)

    time.sleep(1)

    # 获取redis的smsCode
    smsCode = getSmsCode(phoneNum)
    # print(smsCode)
    if smsCode:
        # 处理redis获取的数据提取验证码
        smsCode = re.findall(r'\d+',smsCode)
        # print(smsCode)
        smsCode = smsCode[0]

        # 登录获取token
        userId,token = login(phoneNum,smsCode)

        return userId,token
    return False

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

        response = appHttp.addThumbsUp(data,token)

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
            appHttp.addCommentThumbsUp(data,token)
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

if __name__ == '__main__':
    # userId,token = login(15361899636)
    # time.sleep(1)
    # smsCode = getSmsCode(15361899636)
    # print(smsCode)

    # 账号解封
    removePunish(userPhone=15658850486,userId=None)
    # 给视频点赞
    # addVideoThumbsUp(648474719883886592,5)
    # 给视频评论点赞
    # addVideoCommentThumbsUp(627550301049585664,1)
    pass