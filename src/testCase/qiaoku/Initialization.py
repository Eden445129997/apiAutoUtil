import time
import re
import redis
import random
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import appHttp
from apiAutoUtil.src.utils.Log import log
from apiAutoUtil.src.utils.ODBC import odbc
from apiAutoUtil.config.gloVar import globalRides

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

        # print(cIdList)

        # 循环获取这个视频下的所有评论,并且点赞
        for i in range(len(cIdList)):
            cId = cIdList[i][0]
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
        userId = userDb.selectSQL("select user_id from tb_user_info where user_phone ='%s'"%userPhone)[0][0]
        print(userId)

    if userId:
        # 如果获取到userId，则解封
        userDb.commitSQL("update tb_user_info set user_status = '1' where user_id = '%s'"%userId)
        homeDb = odbc("qiaoku_home")
        homeDb.commitSQL("delete from tb_punish_record where user_id = '%s'"%userId)

        # 获取封号缓存
        rds =redis.StrictRedis(host="10.113.248.203",port=6379,password="didong1904",db=0)
        excuteRedis = rds.delete("userStatus:%s"%userId)
        # if excuteRedis == 1:
        #     setlog = log()
        #     setlog("清除缓存失败——userStatus:%s"%userId)
        return True
    return False

def resetData():
    """清理数据库，将数据库所有数据清空"""
    # 数据库列表
    dataBaseList = ["qiaoku_home","qiaoku_live","qiaoku_message","qiaoku_user","qiaoku_video"]

    # 循环数据库列表
    for dataBase in dataBaseList:
        db = odbc(dataBase)
        # 循环批量删除数据库所有表
        for i in db.selectSQL("show tables"):
            db.commitSQL("truncate table %s;"%i)

    __,rdsJson = globalRides()

    host = rdsJson.get("host")
    port = rdsJson.get("port")
    password = rdsJson.get("password")

    # 建立redis连接池
    pool = redis.ConnectionPool(host=host, port=port,password=password)
    # 连接redis
    rds = redis.Redis(connection_pool=pool)
    # 清空redis所有数据
    rds.flushall()

def getToken(userId):
    """根据userId清理缓存"""
    rds,__ = globalRides()
    token = rds.get("token:%s"%userId)
    print(str(token))
    # 获取token
    return token

def rmToken(userId):
    """根据userId删除token"""
    rds,__ = globalRides()
    rds.delete("challenge:%s"%userId)
    rds.delete("smsCode:%s"%userId)
    return True if rds.delete("token:%s"%userId) else False


if __name__ == '__main__':
    # 更新database.ini配置
    # updateDataBase()

    # 重置数据库（很严重，别乱点）
    # resetData()

    # 清理mysql数据
    # deleteData("15361899636")

    # 查询redis
    # getToken(619988928258113536)

    # 清理redis
    # print(rmToken(15361899636))

    # 登录，获取验证码
    userId, accessToken = login(15361899636)
    print(userId,accessToken)
    pass