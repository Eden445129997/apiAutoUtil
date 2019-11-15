from apiAutoUtil.src.utils.Decorator import getRequest,postRequest

# APP——注册登录——使用手机号码注册登录（第三方登录不支持）
""" :游客登录
    :验证初始化
    :获取短信验证码
    :验证短信验证码
    :退出登录
"""

# 登录——游客
@postRequest
def ykLogin():
    """ :udid 设备号
        :userId 用户Id
    """
    return r"/app-http/login/ykLogin"

# 极验——验证初始化
@getRequest
def startCaptcha():
    """ :userPhone 手机号
    """
    return r"/app-http/login/startCaptcha"

# 登录——获取短信验证码
@getRequest
def getSmsCode():
    """ :userPhone 手机号
        :udid 设备唯一号
        :challenge 极验验证信息
        :type请求类型 1 短信登录 2绑定手机号
        :userId 用户ID（选填，type为2则必填）
    """
    return r"/app-http/login/getSmsCode"

# 登录——验证短信验证码(请求头需要token，从游客登录获取)
# 需要传token
@postRequest
def checkSmsCode():
    return r"/app-http/login/checkSmsCode"

# 登录——退出登录
@postRequest
def logOut(logOutParams):
    """ :token 用户token
    """
    return r"/app-http/login/logOut"

@postRequest
def getRecommendTalent():
    return r"/app-http/video/getRecommendTalent"

@postRequest
def getRecommendTalentVideo():
    return r"/app-http/video/getRecommendTalentVideo"

@getRequest
def getOneVideo():
    return r"/app-http/video/getOneVideo"

@getRequest
def myCollectingMusic():
    return r"/app-http/music/myCollectingMusic"

@postRequest
def collectingMusic():
    return r"/app-http/music/collectingMusic"

@getRequest
def recommendMusic():
    return r"/app-http/music/recommendMusic"

@postRequest
def saveMusic():
    return r"/app-http/music/saveMusic"

# APP——个人中心API
""" :修改用户对话题的关注状态
    :修改用户的关注状态
    :拉黑/取消拉黑用户
    :查看个人/他人基本信息
    :编辑用户信息
    :获取用户关注的人, 粉丝(1关注  2粉丝)
    :获取用户关注的话题
    :获取用户足迹
    :获取用户的黑名单列表
    :获取用户相关的视频(type区分)--1发布  2赞过  3收藏
"""
# APP个人中心——修改用户对话题的关注状态
@postRequest
def updateTopicFollowStatus():
    """ :请求头：token
        :chooseOrCancel 1:选择关注 2:取消关注
        :topicId 话题id
    """
    return r"/app-http/topic/updateTopicFollowStatus"

# APP个人中心——修改用户的关注状态
@postRequest
def updateUserFollowStatus():
    """ :请求头：token
        :chooseOrCancel 1:选择关注 2:取消关注
        :topicId 话题id
    """
    return r"/app-http/user/updateUserFollowStatus"

# APP个人中心——拉黑/取消拉黑用户
@postRequest
def updateBlackUserList():
    """ :请求头：token
        :chooseOrCancel 1:拉黑 2:取消拉黑
        :otherUserId 被操作人id
        :blackUserName 黑名单人员昵称(添加黑名单时填写)
    """
    return r"/app-http/user/updateBlackUserList"

# APP个人中心——查看个人/他人基本信息
@postRequest
def getAppUserBasicInfo():
    """ :请求头：token
        :otherUserId 被操作人id
    """
    return r"/app-http/user/getAppUserBasicInfo"

# APP个人中心——编辑用户信息
@postRequest
def updateUserInfo():
    """ :请求头：token
        :nickName 昵称
        :userSign 个性签名
        :avatar 头像
        :gender 性别 1男 2女 3未知
        :province 省份
        :city 城市
        :birthday 生日
        :qiaoId 敲酷号
    """
    return r"/app-http/user/updateUserInfo"

# APP个人中心——获取用户关注/粉丝
@postRequest
def getUserLinkedUser():
    """ :请求头：token
        :otherUserId 被操作人id
        :type 1关注 2粉丝
        pageIndex 1
        pageSize 10
    """
    return r"/app-http/user/getUserLinkedUser"

# APP个人中心——获取用户关注的话题
@postRequest
def getAppUserFollowTopic():
    """ :请求头：token
        :otherUserId 被操作人id
        pageIndex 1
        pageSize 10
    """
    return r"/app-http/user/getAppUserFollowTopic"

# APP个人中心——获取用户足迹
@postRequest
def getMyFootprintVideo():
    """ :请求头：token
    """
    return r"/app-http/video/getMyFootprintVideo"

# APP个人中心——获取用户的黑名单列表
@postRequest
def getBlackUserList():
    """ :请求头：token
        pageIndex 1
        pageSize 10
    """
    return r"/app-http/user/getBlackUserList"

# APP个人中心——获取用户相关的视频(type区分)--1发布  2赞过  3收藏
@postRequest
def getUserLinkedVideo():
    """ :请求头：token
        :otherUserId 被操作人id
        :type 1关注 2粉丝
        pageIndex 1
        pageSize 10
    """
    return r"/app-http/user/getUserLinkedVideo"

# APP个人中心——获得最新的app版本信息
@postRequest
def getUpToDateVersion():
    """ :请求头：token
    """
    return r"/app-http/user/getUpToDateVersion"

# APP个人中心——添加系统反馈
@postRequest
def submitFeedback():
    """ :请求头：token
        :type
        :content
        :photoUrl
        :contact
    """
    return r"/app-http/user/submitFeedback"


# APP——主页
""" :游客登录
    :验证初始化
    :获取短信验证码
    :验证短信验证码
    :退出登录
"""

# 主页——关注页直播列表
@getRequest
def getFollowLives():
    """ :udid 设备号
        :userId 用户Id
    """
    return r"/app-http/video/getFollowLives"

# 主页——视频列表(关注页,发现页)
@getRequest
def getVideos():
    """ :udid 设备号
        :userId 用户Id
    """
    return r"/app-http/video/getVideos"

# APP——搜索
""" :搜索用户
    :搜索视频
    :搜索话题
"""

# 搜索——搜索用户
@postRequest
def getUserListByKeyword():
    """ :keyword 搜索关键字(qiaoId)
        :pageIndex 不传默认1
        :pageSize 不传默认10
    """
    return r"/app-http/user/getUserListByKeyword"

# 搜索——搜索视频
@postRequest
def getVideoByKeyword():
    """ :keyword 搜索关键字
        :pageIndex 不传默认1
        :pageSize 不传默认10
    """
    return r"/app-http/video/getVideoByKeyword"

# 搜索——搜索话题
@postRequest
def getTopicByKeyword():
    """ :keyword 搜索关键字
        :pageIndex 不传默认1
        :pageSize 不传默认10
    """
    return r"/app-http/topic/getTopicByKeyword"

# APP——话题
""" :游客登录
    :验证初始化
"""

# 话题——全部话题列表
@getRequest
def getVideoTopics():
    """ :pageIndex 分页页码
        :pageSize 分页数量
        :type 分页type
    """
    return r"/app-http/topic/getVideoTopics"

# 话题——获取关注话题
@getRequest
def followTopic():
    """ :pageIndex 分页页码
        :pageSize 分页数量
        :type 分页type
    """
    return r"/app-http/topic/followTopic"

# 话题-话题详情页
@getRequest
def getTopicDetails():
    """ :topicId 话题Id
        ...
    """
    return r"/app-http/topic/getTopicDetails"

# APP——视频播放
""" :视频播放--视频点赞
"""
# APP个人中心——修改用户对话题的关注状态
@getRequest
def addThumbsUp():
    """ :请求头：token
        :videoId 1:视频ID
        :thumbStatus 点赞状态(1:点赞2:取消点赞）
    """
    return r"/app-http/videoPlay/addThumbsUp"

@getRequest
def addCommentThumbsUp():
    """ :请求头：token
        :cId 1:评论ID
        :thumbStatus 点赞状态(1:点赞2:取消点赞）
    """
    return r"/app-http/videoPlay/addCommentThumbsUp"

@postRequest
def updateFavoritesStatus():
    """ :请求头：token
        :chooseOrCancel 1:选择收藏 2:取消收藏
        :videoId 视频id
    """
    return r"/app-http/videoPlay/updateFavoritesStatus"

@postRequest
def saveReport():
    """ :请求头：token
        ...
    """
    return r"/app-http/videoPlay/saveReport"

@postRequest
def delVideo():
    """ :请求头：token
        ...
    """
    return r"/app-http/videoPlay/delVideo"

@postRequest
def delComment():
    """ :请求头：token
        ：cId    评论Id
    """
    return r"/app-http/videoPlay/delComment"

@postRequest
def queryTalkingSkill():
    """ :请求头：token
        :type:(审核)1:视频 2:评论 3:用户 (举报)4;直播 5:用户 6:评论 7:视频',
    """
    return r"/app-http/videoPlay/queryTalkingSkill"

@postRequest
def saveVideoShare():
    """ :请求头：token
        :videoId
        :platform   视频分享平台
    """
    return r"/app-http/videoPlay/saveVideoShare"

@getRequest
def addVideoBrowse():
    """ :请求头：token
        :videoId
        :videoDuration   视频时长(单位S)
        :progressRate   观看进度(精确到0.01)
    """
    return r"/app-http/videoPlay/addVideoBrowse"

@getRequest
def reply():
    """ :请求头：token
        :videoId
        ...
    """
    return r"/app-http/videoPlay/getCommentList/reply"

@getRequest
def getCommentList():
    """ :请求头：token
        :videoId
        ...
    """
    return r"/app-http/videoPlay/getCommentList"

@getRequest
def comment():
    """ :请求头：token
        :videoId
        ...
    """
    return r"/app-http/videoPlay/comment"

# APP——直播API
""" :关闭直播
    :开始直播
    :查看用户是否有直播权限
    :根据id获取直播间信息
    :获取主播信息
    :获取直播列表
    :获取房间禁言列表和房间管理员信息
    :设置成为管理员(禁言) / 取消管理员（禁言）
"""

# 直播——关闭直播
@postRequest
def stopPlay():
    """ :userId 用户Id
        :watchCount 观看人数
        :startTime 开始时间
        :endTime 结束时间
    """
    return r"/app-http/live/stopPlay"

# 直播——开始直播
@postRequest
def startPlay():
    """ :userId 用户Id
        :cover 封面
        :title 直播标题
    """
    return r"/app-http/live/startPlay"

# 直播——查看用户是否有直播权限
@postRequest
def hasRightToPlay():
    """ :userId 用户Id
    """
    return r"/app-http/live/hasRightToPlay"

# 直播——根据id获取直播间信息（根据什么Id？？）
@getRequest
def getTbLiveRecordById():
    """ :id 什么Id啊
    """
    return r"/app-http/live/getTbLiveRecordById"

# 直播——获取主播信息(弃用)可能还有token问题
# @postRequest
# def getPlayerInfo(getPlayerInfoParams):
#     """ :userId 用户Id
#     """
#     return r"/back-http/playerInfo/getPlayerInfo"

# 直播——获取直播列表
@postRequest
def getLiveList():
    """ :userId 用户Id
        :pageIndex 开始页码
        :pageSize 每页显示条数
    """
    return r"/app-http/live/getLiveList"

# 直播——获取房间禁言列表和房间管理员信息
@postRequest
def getRoomManagers():
    """ :roomId 房间Id
    """
    return r"/app-http/live/getRoomManagers"

# 直播——设置成为管理员(禁言) / 取消管理员（禁言）
@postRequest
def setManager():
    """ :userId 用户Id
        :state 1: 设置为管理员，2: 设置为禁言，-1:取消管理员，-2:取消禁言
        :roomId 房间Id
        :nickName 用户名
        :avatar 头像
    """
    return r"/app-http/live/setManager"

# APP——推送
""" :查看用户各通知状态
    :获取用户消息列表
    :设置通知
"""

# 查看用户各通知状态
@getRequest
def getUserPushStatus():
    """ :userId 用户Id
    """
    return r"/app-http/user/getUserPushStatus"

# 获取用户消息列表
@postRequest
def getUserMessageList():
    """ :token
        :messageType 1:新增关注 2:赞和收藏
    """
    return r"/app-http/message/getUserMessageList"

# 设置通知
@postRequest
def setUserGetui():
    return r"/app-http/user/setUserGetui"