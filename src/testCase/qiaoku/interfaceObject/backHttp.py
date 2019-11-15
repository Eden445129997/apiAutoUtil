# coding=UTF-8
from apiAutoUtil.src.utils.Decorator import getRequest
from apiAutoUtil.src.utils.Decorator import postRequest

@postRequest
def addUserInDepartment():
    # avatar:{'type': 'string'}
    # createTime:{'type': 'string', 'format': 'date-time'}
    # departmentId:{'type': 'integer', 'format': 'int64'}
    # enabled:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # nickName:{'type': 'string'}
    # password:{'type': 'string'}
    # userPhone:{'type': 'string'}
    # userRole:{'type': 'integer', 'format': 'int32'}
    # username:{'type': 'string'}
    return "/back-http/backuser/addUserInDepartment"

@postRequest
def createDepartment():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # delFlag:{'type': 'integer', 'format': 'int32'}
    # departmentName:{'type': 'string'}
    # departmentRemark:{'type': 'string'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    return "/back-http/backuser/createDepartment"

@getRequest
def deleteDepartment():
    # departmentId:string
    return "/back-http/backuser/deleteDepartment"

@postRequest
def disabledUserRightFormDepartment():
    # backuserId:{'type': 'integer', 'format': 'int64'}
    # departmentId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/backuser/disabledUserRightFormDepartment"

@postRequest
def editDepartment():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # delFlag:{'type': 'integer', 'format': 'int32'}
    # departmentName:{'type': 'string'}
    # departmentRemark:{'type': 'string'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    return "/back-http/backuser/editDepartment"

@postRequest
def editUserInDepartment():
    # avatar:{'type': 'string'}
    # createTime:{'type': 'string', 'format': 'date-time'}
    # departmentId:{'type': 'integer', 'format': 'int64'}
    # enabled:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # nickName:{'type': 'string'}
    # password:{'type': 'string'}
    # userPhone:{'type': 'string'}
    # userRole:{'type': 'integer', 'format': 'int32'}
    # username:{'type': 'string'}
    return "/back-http/backuser/editUserInDepartment"

@postRequest
def enabledUserRightFormDepartment():
    # backuserId:{'type': 'integer', 'format': 'int64'}
    # departmentId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/backuser/enabledUserRightFormDepartment"

@getRequest
def login():
    # None
    return "/back-http/backuser/login"

@postRequest
def modifyDepartmentRight():
    # departmentId:{'type': 'integer', 'format': 'int64'}
    # rightIds:{'type': 'array', 'items': {'type': 'integer', 'format': 'int64'}}
    return "/back-http/backuser/modifyDepartmentRight"

@postRequest
def modifyUserDepartmentRight():
    # backuserId:{'type': 'integer', 'format': 'int64'}
    # departmentId:{'type': 'integer', 'format': 'int64'}
    # rights:{'type': 'array', 'items': {'type': 'integer', 'format': 'int64'}}
    return "/back-http/backuser/modifyUserDepartmentRight"

@postRequest
def removedUserFromDepartment():
    # backuserId:{'type': 'integer', 'format': 'int64'}
    # departmentId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/backuser/removedUserFromDepartment"

@getRequest
def category_delete():
    # id:string
    return "/back-http/category/delete"

@getRequest
def category_id():
    # id:string
    return "/back-http/category/id"

@postRequest
def category_query():
    # beginTime:{'type': 'string', 'format': 'date-time'}
    # endTime:{'type': 'string', 'format': 'date-time'}
    # keywords:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # useType:{'type': 'integer', 'format': 'int32'}
    return "/back-http/category/query"

@postRequest
def category_submit():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # displayOrder:{'type': 'integer', 'format': 'int32'}
    # displayStatus:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # imageId:{'type': 'string'}
    # imageUrl:{'type': 'string'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # name:{'type': 'string'}
    # operator:{'type': 'integer', 'format': 'int64'}
    # recommendStatus:{'type': 'boolean'}
    # remark:{'type': 'string'}
    # useType:{'type': 'integer', 'format': 'int32'}
    # videoCount:{'type': 'integer', 'format': 'int32'}
    return "/back-http/category/submit"

@postRequest
def update():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # displayOrder:{'type': 'integer', 'format': 'int32'}
    # displayStatus:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # imageId:{'type': 'string'}
    # imageUrl:{'type': 'string'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # name:{'type': 'string'}
    # operator:{'type': 'integer', 'format': 'int64'}
    # recommendStatus:{'type': 'boolean'}
    # remark:{'type': 'string'}
    # useType:{'type': 'integer', 'format': 'int32'}
    # videoCount:{'type': 'integer', 'format': 'int32'}
    return "/back-http/category/update"

@getRequest
def id():
    # id:int32
    return "/back-http/feedback/id"

@postRequest
def feedback_query():
    # beginTime:{'type': 'string', 'format': 'date-time'}
    # endTime:{'type': 'string', 'format': 'date-time'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    return "/back-http/feedback/query"

@postRequest
def submit():
    # content:{'type': 'string'}
    # createTime:{'type': 'string', 'format': 'date-time'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # photoUrl:{'type': 'string'}
    # type:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/feedback/submit"

@getRequest
def label_delete():
    # id:string
    return "/back-http/label/delete"

@getRequest
def id():
    # id:string
    return "/back-http/label/id"

@postRequest
def label_query():
    # beginTime:{'type': 'string', 'format': 'date-time'}
    # endTime:{'type': 'string', 'format': 'date-time'}
    # keywords:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # useType:{'type': 'integer', 'format': 'int32'}
    return "/back-http/label/query"

@postRequest
def label_submit():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # displayOrder:{'type': 'integer', 'format': 'int32'}
    # displayStatus:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # imageId:{'type': 'string'}
    # imageUrl:{'type': 'string'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # name:{'type': 'string'}
    # operator:{'type': 'integer', 'format': 'int64'}
    # recommendStatus:{'type': 'boolean'}
    # remark:{'type': 'string'}
    # useType:{'type': 'integer', 'format': 'int32'}
    # videoCount:{'type': 'integer', 'format': 'int32'}
    return "/back-http/label/submit"

@postRequest
def label_update():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # displayOrder:{'type': 'integer', 'format': 'int32'}
    # displayStatus:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # imageId:{'type': 'string'}
    # imageUrl:{'type': 'string'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # name:{'type': 'string'}
    # operator:{'type': 'integer', 'format': 'int64'}
    # recommendStatus:{'type': 'boolean'}
    # remark:{'type': 'string'}
    # useType:{'type': 'integer', 'format': 'int32'}
    # videoCount:{'type': 'integer', 'format': 'int32'}
    return "/back-http/label/update"

@postRequest
def forbidstream():
    # roomId:{'type': 'string'}
    # userId:{'type': 'string'}
    return "/back-http/live/forbidstream"

@getRequest
def getAllLivingLiveRecords():
    # None
    return "/back-http/live/getAllLivingLiveRecords"

@postRequest
def getLivingLiveRecords():
    # nickName:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'string'}
    return "/back-http/live/getLivingLiveRecords"

@postRequest
def onCreateCallBack():
    # appid:{'type': 'string'}
    # channel_id:{'type': 'string'}
    # create_time:{'type': 'integer', 'format': 'int32'}
    # event:{'type': 'string'}
    # hdl_url:{'type': 'array', 'items': {'type': 'string'}}
    # hls_url:{'type': 'array', 'items': {'type': 'string'}}
    # nonce:{'type': 'string'}
    # pic_url:{'type': 'array', 'items': {'type': 'string'}}
    # publish_id:{'type': 'string'}
    # publish_name:{'type': 'string'}
    # rtmp_url:{'type': 'array', 'items': {'type': 'string'}}
    # signature:{'type': 'string'}
    # stream_alias:{'type': 'string'}
    # stream_sid:{'type': 'string'}
    # timestamp:{'type': 'string'}
    # title:{'type': 'string'}
    return "/back-http/live/onCreateCallBack"

@postRequest
def onShutDownCallBack():
    # appid:{'type': 'string'}
    # channel_id:{'type': 'string'}
    # event:{'type': 'string'}
    # nonce:{'type': 'string'}
    # signature:{'type': 'string'}
    # stream_alias:{'type': 'string'}
    # stream_sid:{'type': 'string'}
    # timestamp:{'type': 'string'}
    # type:{'type': 'integer', 'format': 'int32'}
    return "/back-http/live/onShutDownCallBack"

@postRequest
def resumeLiveStream():
    # roomId:{'type': 'string'}
    # userId:{'type': 'string'}
    return "/back-http/live/resumeLiveStream"

@postRequest
def warn():
    # roomId:{'type': 'string'}
    # userIds:{'type': 'array', 'items': {'type': 'string'}}
    return "/back-http/live/warn"

@postRequest
def createTbMcnInfo():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # displayStatus:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # mcnName:{'type': 'string'}
    # playerCount:{'type': 'integer', 'format': 'int32'}
    # talentCount:{'type': 'integer', 'format': 'int32'}
    return "/back-http/mcnInfo/createTbMcnInfo"

@postRequest
def getTbMcnInfoPage():
    # endTime:{'type': 'string', 'format': 'date-time'}
    # keyword:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # startTime:{'type': 'string', 'format': 'date-time'}
    return "/back-http/mcnInfo/getTbMcnInfoPage"

@getRequest
def listAllTbMcnInfos():
    # None
    return "/back-http/mcnInfo/listAllTbMcnInfos"

@postRequest
def addVideosToPackage():
    # packageId:{'type': 'integer', 'format': 'int64'}
    # videoIds:{'type': 'array', 'items': {'type': 'integer', 'format': 'int64'}}
    return "/back-http/package/addVideosToPackage"

@getRequest
def package_delete():
    # id:string
    return "/back-http/package/delete"

@getRequest
def deleteVideoFromPackage():
    # packageId:int64
    # videoId:int64
    return "/back-http/package/deleteVideoFromPackage"

@getRequest
def package_id():
    # id:string
    return "/back-http/package/id"

@postRequest
def package_query():
    # beginTime:{'type': 'string', 'format': 'date-time'}
    # endTime:{'type': 'string', 'format': 'date-time'}
    # keywords:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # useType:{'type': 'integer', 'format': 'int32'}
    return "/back-http/package/query"

@postRequest
def selectNoPackageVideoPage():
    # packageId:{'type': 'integer', 'format': 'int64'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    return "/back-http/package/selectNoPackageVideoPage"

@postRequest
def selectPackageVideoList():
    # categoryId:{'type': 'string'}
    # endTime:{'type': 'string'}
    # keywords:{'type': 'string'}
    # packageId:{'type': 'integer', 'format': 'int64'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # startTime:{'type': 'string'}
    # videoTitle:{'type': 'string'}
    return "/back-http/package/selectPackageVideoList"

@postRequest
def selectPackageVideoPage():
    # categoryId:{'type': 'string'}
    # endTime:{'type': 'string'}
    # keywords:{'type': 'string'}
    # packageId:{'type': 'integer', 'format': 'int64'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # startTime:{'type': 'string'}
    # videoTitle:{'type': 'string'}
    return "/back-http/package/selectPackageVideoPage"

@postRequest
def package_submit():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # displayOrder:{'type': 'integer', 'format': 'int32'}
    # displayStatus:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # imageId:{'type': 'string'}
    # imageUrl:{'type': 'string'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # name:{'type': 'string'}
    # operator:{'type': 'integer', 'format': 'int64'}
    # recommendStatus:{'type': 'boolean'}
    # remark:{'type': 'string'}
    # useType:{'type': 'integer', 'format': 'int32'}
    # videoCount:{'type': 'integer', 'format': 'int32'}
    return "/back-http/package/submit"

@postRequest
def package_update():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # displayOrder:{'type': 'integer', 'format': 'int32'}
    # displayStatus:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # imageId:{'type': 'string'}
    # imageUrl:{'type': 'string'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # name:{'type': 'string'}
    # operator:{'type': 'integer', 'format': 'int64'}
    # recommendStatus:{'type': 'boolean'}
    # remark:{'type': 'string'}
    # useType:{'type': 'integer', 'format': 'int32'}
    # videoCount:{'type': 'integer', 'format': 'int32'}
    return "/back-http/package/update"

@postRequest
def createTbPlayerInfo():
    # avatar:{'type': 'string'}
    # belongBackUser:{'type': 'integer', 'format': 'int32'}
    # bindingQq:{'type': 'integer', 'format': 'int32'}
    # bindingWx:{'type': 'integer', 'format': 'int32'}
    # birthday:{'type': 'string', 'format': 'date-time'}
    # city:{'type': 'string'}
    # createTime:{'type': 'string', 'format': 'date-time'}
    # delFlag:{'type': 'integer', 'format': 'int32'}
    # gender:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # liveStatus:{'type': 'integer', 'format': 'int32'}
    # mcnId:{'type': 'integer', 'format': 'int64'}
    # nickName:{'type': 'string'}
    # playerMark:{'type': 'integer', 'format': 'int32'}
    # province:{'type': 'string'}
    # qiaoId:{'type': 'string'}
    # region:{'type': 'string'}
    # talentMark:{'type': 'integer', 'format': 'int32'}
    # totalCollectionCount:{'type': 'integer', 'format': 'int32'}
    # totalLikeVideoCount:{'type': 'integer', 'format': 'int32'}
    # totalPublishCount:{'type': 'integer', 'format': 'int32'}
    # totalThumbUpCount:{'type': 'integer', 'format': 'int32'}
    # udid:{'type': 'string'}
    # userFansCount:{'type': 'integer', 'format': 'int32'}
    # userFollowCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userOrigin:{'type': 'integer', 'format': 'int32'}
    # userPhone:{'type': 'string'}
    # userSign:{'type': 'string'}
    # userStatus:{'type': 'integer', 'format': 'int32'}
    return "/back-http/playerInfo/createTbPlayerInfo"

@postRequest
def getTbLiveRecordByUserIdPage():
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'string'}
    return "/back-http/playerInfo/getTbLiveRecordByUserIdPage"

@postRequest
def getTbPlayerInfos():
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # playerInfoDTO:{'$ref': '#/definitions/PlayerInfoDTO'}
    return "/back-http/playerInfo/getTbPlayerInfos"

@postRequest
def report_query():
    # keywords:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    return "/back-http/report/query"

@getRequest
def deleteTalkingSkill():
    # id:int64
    return "/back-http/talkingskill/deleteTalkingSkill"

@postRequest
def talkingskill_displayed():
    # displayed:{'type': 'integer', 'format': 'int32'}
    # talkingSkillId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/talkingskill/displayed"

@postRequest
def editTalkingSkill():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # displayEnable:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # operator:{'type': 'integer', 'format': 'int32'}
    # templateContent:{'type': 'string'}
    # templateType:{'type': 'integer', 'format': 'int32'}
    return "/back-http/talkingskill/editTalkingSkill"

@postRequest
def talkingskill_query():
    # beginTime:{'type': 'string', 'format': 'date-time'}
    # endTime:{'type': 'string', 'format': 'date-time'}
    # keywords:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    return "/back-http/talkingskill/query"

@postRequest
def submitNew():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # displayEnable:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # operator:{'type': 'integer', 'format': 'int32'}
    # templateContent:{'type': 'string'}
    # templateType:{'type': 'integer', 'format': 'int32'}
    return "/back-http/talkingskill/submitNew"

@postRequest
def createBackUser():
    # avatar:{'type': 'string'}
    # belongBackUser:{'type': 'integer', 'format': 'int32'}
    # bindingQq:{'type': 'integer', 'format': 'int32'}
    # bindingWx:{'type': 'integer', 'format': 'int32'}
    # birthday:{'type': 'string', 'format': 'date-time'}
    # city:{'type': 'string'}
    # createTime:{'type': 'string', 'format': 'date-time'}
    # delFlag:{'type': 'integer', 'format': 'int32'}
    # gender:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # liveStatus:{'type': 'integer', 'format': 'int32'}
    # mcnId:{'type': 'integer', 'format': 'int64'}
    # mcnName:{'type': 'string'}
    # nickName:{'type': 'string'}
    # playerMark:{'type': 'integer', 'format': 'int32'}
    # province:{'type': 'string'}
    # qiaoId:{'type': 'string'}
    # region:{'type': 'string'}
    # talentMark:{'type': 'integer', 'format': 'int32'}
    # totalCollectionCount:{'type': 'integer', 'format': 'int32'}
    # totalLikeVideoCount:{'type': 'integer', 'format': 'int32'}
    # totalPublishCount:{'type': 'integer', 'format': 'int32'}
    # totalThumbUpCount:{'type': 'integer', 'format': 'int32'}
    # udid:{'type': 'string'}
    # userFansCount:{'type': 'integer', 'format': 'int32'}
    # userFollowCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIdStr:{'type': 'string'}
    # userOrigin:{'type': 'integer', 'format': 'int32'}
    # userPhone:{'type': 'string'}
    # userSign:{'type': 'string'}
    # userStatus:{'type': 'integer', 'format': 'int32'}
    # videoLabelCountPublishList:{'type': 'array', 'items': {'$ref': '#/definitions/TbVideoLabelCountPublish'}}
    return "/back-http/user/createBackUser"

@postRequest
def getBackuserUserInfo():
    # endNumber:{'type': 'integer', 'format': 'int32'}
    # generalUser:{'type': 'integer', 'format': 'int32'}
    # nickName:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # playerMark:{'type': 'integer', 'format': 'int32'}
    # startNumber:{'type': 'integer', 'format': 'int32'}
    # talentMark:{'type': 'integer', 'format': 'int32'}
    # totalBrowseCount:{'type': 'integer', 'format': 'int32'}
    # totalCollectionCount:{'type': 'integer', 'format': 'int32'}
    # totalPublishCount:{'type': 'integer', 'format': 'int32'}
    # totalShareCount:{'type': 'integer', 'format': 'int32'}
    # totalThumbUpCount:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    # userFansCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIdStr:{'type': 'string'}
    # userOrigin:{'type': 'integer', 'format': 'int32'}
    # userPhone:{'type': 'string'}
    # videoCategoryId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/user/getBackuserUserInfo"

@getRequest
def getMcnInfoList():
    # None
    return "/back-http/user/getMcnInfoList"

@postRequest
def getUserBasicInfo():
    # endNumber:{'type': 'integer', 'format': 'int32'}
    # generalUser:{'type': 'integer', 'format': 'int32'}
    # nickName:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # playerMark:{'type': 'integer', 'format': 'int32'}
    # startNumber:{'type': 'integer', 'format': 'int32'}
    # talentMark:{'type': 'integer', 'format': 'int32'}
    # totalBrowseCount:{'type': 'integer', 'format': 'int32'}
    # totalCollectionCount:{'type': 'integer', 'format': 'int32'}
    # totalPublishCount:{'type': 'integer', 'format': 'int32'}
    # totalShareCount:{'type': 'integer', 'format': 'int32'}
    # totalThumbUpCount:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    # userFansCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIdStr:{'type': 'string'}
    # userOrigin:{'type': 'integer', 'format': 'int32'}
    # userPhone:{'type': 'string'}
    # videoCategoryId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/user/getUserBasicInfo"

@postRequest
def getUserDataList():
    # endNumber:{'type': 'integer', 'format': 'int32'}
    # generalUser:{'type': 'integer', 'format': 'int32'}
    # nickName:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # playerMark:{'type': 'integer', 'format': 'int32'}
    # startNumber:{'type': 'integer', 'format': 'int32'}
    # talentMark:{'type': 'integer', 'format': 'int32'}
    # totalBrowseCount:{'type': 'integer', 'format': 'int32'}
    # totalCollectionCount:{'type': 'integer', 'format': 'int32'}
    # totalPublishCount:{'type': 'integer', 'format': 'int32'}
    # totalShareCount:{'type': 'integer', 'format': 'int32'}
    # totalThumbUpCount:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    # userFansCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIdStr:{'type': 'string'}
    # userOrigin:{'type': 'integer', 'format': 'int32'}
    # userPhone:{'type': 'string'}
    # videoCategoryId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/user/getUserDataList"

@postRequest
def getUserFansInfo():
    # endNumber:{'type': 'integer', 'format': 'int32'}
    # generalUser:{'type': 'integer', 'format': 'int32'}
    # nickName:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # playerMark:{'type': 'integer', 'format': 'int32'}
    # startNumber:{'type': 'integer', 'format': 'int32'}
    # talentMark:{'type': 'integer', 'format': 'int32'}
    # totalBrowseCount:{'type': 'integer', 'format': 'int32'}
    # totalCollectionCount:{'type': 'integer', 'format': 'int32'}
    # totalPublishCount:{'type': 'integer', 'format': 'int32'}
    # totalShareCount:{'type': 'integer', 'format': 'int32'}
    # totalThumbUpCount:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    # userFansCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIdStr:{'type': 'string'}
    # userOrigin:{'type': 'integer', 'format': 'int32'}
    # userPhone:{'type': 'string'}
    # videoCategoryId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/user/getUserFansInfo"

@postRequest
def getUserFavoritesVideo():
    # endNumber:{'type': 'integer', 'format': 'int32'}
    # generalUser:{'type': 'integer', 'format': 'int32'}
    # nickName:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # playerMark:{'type': 'integer', 'format': 'int32'}
    # startNumber:{'type': 'integer', 'format': 'int32'}
    # talentMark:{'type': 'integer', 'format': 'int32'}
    # totalBrowseCount:{'type': 'integer', 'format': 'int32'}
    # totalCollectionCount:{'type': 'integer', 'format': 'int32'}
    # totalPublishCount:{'type': 'integer', 'format': 'int32'}
    # totalShareCount:{'type': 'integer', 'format': 'int32'}
    # totalThumbUpCount:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    # userFansCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIdStr:{'type': 'string'}
    # userOrigin:{'type': 'integer', 'format': 'int32'}
    # userPhone:{'type': 'string'}
    # videoCategoryId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/user/getUserFavoritesVideo"

@postRequest
def getUserFollowInfo():
    # endNumber:{'type': 'integer', 'format': 'int32'}
    # generalUser:{'type': 'integer', 'format': 'int32'}
    # nickName:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # playerMark:{'type': 'integer', 'format': 'int32'}
    # startNumber:{'type': 'integer', 'format': 'int32'}
    # talentMark:{'type': 'integer', 'format': 'int32'}
    # totalBrowseCount:{'type': 'integer', 'format': 'int32'}
    # totalCollectionCount:{'type': 'integer', 'format': 'int32'}
    # totalPublishCount:{'type': 'integer', 'format': 'int32'}
    # totalShareCount:{'type': 'integer', 'format': 'int32'}
    # totalThumbUpCount:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    # userFansCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIdStr:{'type': 'string'}
    # userOrigin:{'type': 'integer', 'format': 'int32'}
    # userPhone:{'type': 'string'}
    # videoCategoryId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/user/getUserFollowInfo"

@postRequest
def getUserThumbUpVideo():
    # endNumber:{'type': 'integer', 'format': 'int32'}
    # generalUser:{'type': 'integer', 'format': 'int32'}
    # nickName:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # playerMark:{'type': 'integer', 'format': 'int32'}
    # startNumber:{'type': 'integer', 'format': 'int32'}
    # talentMark:{'type': 'integer', 'format': 'int32'}
    # totalBrowseCount:{'type': 'integer', 'format': 'int32'}
    # totalCollectionCount:{'type': 'integer', 'format': 'int32'}
    # totalPublishCount:{'type': 'integer', 'format': 'int32'}
    # totalShareCount:{'type': 'integer', 'format': 'int32'}
    # totalThumbUpCount:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    # userFansCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIdStr:{'type': 'string'}
    # userOrigin:{'type': 'integer', 'format': 'int32'}
    # userPhone:{'type': 'string'}
    # videoCategoryId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/user/getUserThumbUpVideo"

@postRequest
def getUserVideoPublish():
    # endNumber:{'type': 'integer', 'format': 'int32'}
    # generalUser:{'type': 'integer', 'format': 'int32'}
    # nickName:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # playerMark:{'type': 'integer', 'format': 'int32'}
    # startNumber:{'type': 'integer', 'format': 'int32'}
    # talentMark:{'type': 'integer', 'format': 'int32'}
    # totalBrowseCount:{'type': 'integer', 'format': 'int32'}
    # totalCollectionCount:{'type': 'integer', 'format': 'int32'}
    # totalPublishCount:{'type': 'integer', 'format': 'int32'}
    # totalShareCount:{'type': 'integer', 'format': 'int32'}
    # totalThumbUpCount:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    # userFansCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIdStr:{'type': 'string'}
    # userOrigin:{'type': 'integer', 'format': 'int32'}
    # userPhone:{'type': 'string'}
    # videoCategoryId:{'type': 'integer', 'format': 'int64'}
    return "/back-http/user/getUserVideoPublish"

@postRequest
def updateBackUser():
    # avatar:{'type': 'string'}
    # belongBackUser:{'type': 'integer', 'format': 'int32'}
    # bindingQq:{'type': 'integer', 'format': 'int32'}
    # bindingWx:{'type': 'integer', 'format': 'int32'}
    # birthday:{'type': 'string', 'format': 'date-time'}
    # city:{'type': 'string'}
    # createTime:{'type': 'string', 'format': 'date-time'}
    # delFlag:{'type': 'integer', 'format': 'int32'}
    # gender:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # liveStatus:{'type': 'integer', 'format': 'int32'}
    # mcnId:{'type': 'integer', 'format': 'int64'}
    # mcnName:{'type': 'string'}
    # nickName:{'type': 'string'}
    # playerMark:{'type': 'integer', 'format': 'int32'}
    # province:{'type': 'string'}
    # qiaoId:{'type': 'string'}
    # region:{'type': 'string'}
    # talentMark:{'type': 'integer', 'format': 'int32'}
    # totalCollectionCount:{'type': 'integer', 'format': 'int32'}
    # totalLikeVideoCount:{'type': 'integer', 'format': 'int32'}
    # totalPublishCount:{'type': 'integer', 'format': 'int32'}
    # totalThumbUpCount:{'type': 'integer', 'format': 'int32'}
    # udid:{'type': 'string'}
    # userFansCount:{'type': 'integer', 'format': 'int32'}
    # userFollowCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIdStr:{'type': 'string'}
    # userOrigin:{'type': 'integer', 'format': 'int32'}
    # userPhone:{'type': 'string'}
    # userSign:{'type': 'string'}
    # userStatus:{'type': 'integer', 'format': 'int32'}
    # videoLabelCountPublishList:{'type': 'array', 'items': {'$ref': '#/definitions/TbVideoLabelCountPublish'}}
    return "/back-http/user/updateBackUser"

@postRequest
def updateUserForMark():
    # avatar:{'type': 'string'}
    # belongBackUser:{'type': 'integer', 'format': 'int32'}
    # bindingQq:{'type': 'integer', 'format': 'int32'}
    # bindingWx:{'type': 'integer', 'format': 'int32'}
    # birthday:{'type': 'string', 'format': 'date-time'}
    # city:{'type': 'string'}
    # createTime:{'type': 'string', 'format': 'date-time'}
    # delFlag:{'type': 'integer', 'format': 'int32'}
    # gender:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # liveStatus:{'type': 'integer', 'format': 'int32'}
    # mcnId:{'type': 'integer', 'format': 'int64'}
    # mcnName:{'type': 'string'}
    # nickName:{'type': 'string'}
    # playerMark:{'type': 'integer', 'format': 'int32'}
    # province:{'type': 'string'}
    # qiaoId:{'type': 'string'}
    # region:{'type': 'string'}
    # talentMark:{'type': 'integer', 'format': 'int32'}
    # totalCollectionCount:{'type': 'integer', 'format': 'int32'}
    # totalLikeVideoCount:{'type': 'integer', 'format': 'int32'}
    # totalPublishCount:{'type': 'integer', 'format': 'int32'}
    # totalThumbUpCount:{'type': 'integer', 'format': 'int32'}
    # udid:{'type': 'string'}
    # userFansCount:{'type': 'integer', 'format': 'int32'}
    # userFollowCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIdStr:{'type': 'string'}
    # userOrigin:{'type': 'integer', 'format': 'int32'}
    # userPhone:{'type': 'string'}
    # userSign:{'type': 'string'}
    # userStatus:{'type': 'integer', 'format': 'int32'}
    # videoLabelCountPublishList:{'type': 'array', 'items': {'$ref': '#/definitions/TbVideoLabelCountPublish'}}
    return "/back-http/user/updateUserForMark"

@getRequest
def userModifyRecord_failPassCheck():
    # id:string
    return "/back-http/userModifyRecord/failPassCheck"

@postRequest
def selectUserModifyRecordChkStatusDownPage():
    # applyType:{'type': 'integer', 'format': 'int32'}
    # chkStatus:{'type': 'integer', 'format': 'int32'}
    # endApplyDate:{'type': 'string', 'format': 'date-time'}
    # endOperateDate:{'type': 'string', 'format': 'date-time'}
    # modifyType:{'type': 'integer', 'format': 'int32'}
    # operatePersonName:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # startApplyDate:{'type': 'string', 'format': 'date-time'}
    # startOperateDate:{'type': 'string', 'format': 'date-time'}
    return "/back-http/userModifyRecord/selectUserModifyRecordChkStatusDownPage"

@postRequest
def selectUserModifyRecordChkStatusWaitPage():
    # applyType:{'type': 'integer', 'format': 'int32'}
    # chkStatus:{'type': 'integer', 'format': 'int32'}
    # endApplyDate:{'type': 'string', 'format': 'date-time'}
    # endOperateDate:{'type': 'string', 'format': 'date-time'}
    # modifyType:{'type': 'integer', 'format': 'int32'}
    # operatePersonName:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # startApplyDate:{'type': 'string', 'format': 'date-time'}
    # startOperateDate:{'type': 'string', 'format': 'date-time'}
    return "/back-http/userModifyRecord/selectUserModifyRecordChkStatusWaitPage"

@getRequest
def userModifyRecord_successPassCheck():
    # id:string
    return "/back-http/userModifyRecord/successPassCheck"

@getRequest
def failPassVideoCheck():
    # id:string
    # titleReason:string
    # videoReason:string
    return "/back-http/video/failPassVideoCheck"

@postRequest
def getChkResultVideoPage():
    # chkStatus:{'type': 'integer', 'format': 'int32'}
    # endTime:{'type': 'string', 'format': 'date-time'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # startTime:{'type': 'string', 'format': 'date-time'}
    # topicId:{'type': 'integer', 'format': 'int32'}
    # videoLevel:{'type': 'integer', 'format': 'int32'}
    return "/back-http/video/getChkResultVideoPage"

@postRequest
def getChkVideoPage():
    # chkStatus:{'type': 'integer', 'format': 'int32'}
    # endTime:{'type': 'string', 'format': 'date-time'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # startTime:{'type': 'string', 'format': 'date-time'}
    # topicId:{'type': 'integer', 'format': 'int32'}
    # videoLevel:{'type': 'integer', 'format': 'int32'}
    return "/back-http/video/getChkVideoPage"

@postRequest
def getVideoAllCategory():
    # keyword:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    return "/back-http/video/getVideoAllCategory"

@postRequest
def getVideoAllLabel():
    # keyword:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    return "/back-http/video/getVideoAllLabel"

@postRequest
def getVideoAllTopic():
    # keyword:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # type:{'type': 'integer', 'format': 'int32'}
    return "/back-http/video/getVideoAllTopic"

@getRequest
def getVideoLabelAndTopic():
    # videoId:string
    return "/back-http/video/getVideoLabelAndTopic"

@getRequest
def selectChkLogByVideoId():
    # videoId:int64
    return "/back-http/video/selectChkLogByVideoId"

@getRequest
def selectLogByVideoId():
    # videoId:int64
    return "/back-http/video/selectLogByVideoId"

@postRequest
def selectRecommendVideoPage():
    # beginCount:{'type': 'integer', 'format': 'int32'}
    # categoryId:{'type': 'integer', 'format': 'int32'}
    # countType:{'type': 'integer', 'format': 'int32'}
    # endCount:{'type': 'integer', 'format': 'int32'}
    # endRecommendDate:{'type': 'string', 'format': 'date-time'}
    # endTime:{'type': 'string', 'format': 'date-time'}
    # keywords:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # recommendPerson:{'type': 'integer', 'format': 'int64'}
    # searchType:{'type': 'integer', 'format': 'int32'}
    # startRecommendDate:{'type': 'string', 'format': 'date-time'}
    # startTime:{'type': 'string', 'format': 'date-time'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIds:{'type': 'array', 'items': {'type': 'integer', 'format': 'int64'}}
    return "/back-http/video/selectRecommendVideoPage"

@postRequest
def selectUnderLineVideoPage():
    # categoryId:{'type': 'integer', 'format': 'int32'}
    # endUnderLineTime:{'type': 'string', 'format': 'date-time'}
    # keywords:{'type': 'string'}
    # operatorId:{'type': 'integer', 'format': 'int64'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # searchType:{'type': 'integer', 'format': 'int32'}
    # startUnderLineTime:{'type': 'string', 'format': 'date-time'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIds:{'type': 'array', 'items': {'type': 'integer', 'format': 'int64'}}
    return "/back-http/video/selectUnderLineVideoPage"

@postRequest
def selectVideoPage():
    # beginCount:{'type': 'integer', 'format': 'int32'}
    # categoryId:{'type': 'integer', 'format': 'int32'}
    # countType:{'type': 'integer', 'format': 'int32'}
    # endCount:{'type': 'integer', 'format': 'int32'}
    # endTime:{'type': 'string', 'format': 'date-time'}
    # keywords:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # searchType:{'type': 'integer', 'format': 'int32'}
    # startTime:{'type': 'string', 'format': 'date-time'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIds:{'type': 'array', 'items': {'type': 'integer', 'format': 'int64'}}
    return "/back-http/video/selectVideoPage"

@postRequest
def selectVideoPageForSpecialUser():
    # beginCount:{'type': 'integer', 'format': 'int32'}
    # categoryId:{'type': 'integer', 'format': 'int32'}
    # countType:{'type': 'integer', 'format': 'int32'}
    # endCount:{'type': 'integer', 'format': 'int32'}
    # endTime:{'type': 'string', 'format': 'date-time'}
    # keywords:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # searchType:{'type': 'integer', 'format': 'int32'}
    # startTime:{'type': 'string', 'format': 'date-time'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userIds:{'type': 'array', 'items': {'type': 'integer', 'format': 'int64'}}
    return "/back-http/video/selectVideoPageForSpecialUser"

@postRequest
def successPassVideoCheck():
    # categoryId:{'type': 'integer', 'format': 'int64'}
    # chkType:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # labels:{'type': 'array', 'items': {'type': 'integer', 'format': 'int64'}}
    # videoId:{'type': 'integer', 'format': 'int64'}
    # videoLevel:{'type': 'string'}
    return "/back-http/video/successPassVideoCheck"

@postRequest
def updateSystemVideo():
    # addressName:{'type': 'string'}
    # aoiAddress:{'type': 'string'}
    # backUserId:{'type': 'integer', 'format': 'int64'}
    # browseCount:{'type': 'integer', 'format': 'int32'}
    # chkStatus:{'type': 'integer', 'format': 'int32'}
    # city:{'type': 'string'}
    # commentCount:{'type': 'integer', 'format': 'int32'}
    # completeCount:{'type': 'integer', 'format': 'int32'}
    # coverSize:{'type': 'string'}
    # createTime:{'type': 'string', 'format': 'date-time'}
    # delFlag:{'type': 'integer', 'format': 'int32'}
    # favoritesCount:{'type': 'integer', 'format': 'int32'}
    # gif:{'type': 'string'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # latitude:{'type': 'number', 'format': 'double'}
    # longitude:{'type': 'number', 'format': 'double'}
    # photo:{'type': 'string'}
    # province:{'type': 'string'}
    # region:{'type': 'string'}
    # score:{'type': 'string'}
    # shareCount:{'type': 'integer', 'format': 'int32'}
    # thirdVideoId:{'type': 'string'}
    # thumbsUpCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userSource:{'type': 'integer', 'format': 'int32'}
    # videoCategoryId:{'type': 'integer', 'format': 'int64'}
    # videoId:{'type': 'integer', 'format': 'int64'}
    # videoLabels:{'type': 'array', 'items': {'type': 'object'}}
    # videoLevel:{'type': 'string'}
    # videoOrigin:{'type': 'string'}
    # videoRecommendStatus:{'type': 'integer', 'format': 'int32'}
    # videoTitle:{'type': 'string'}
    # videoTopicId:{'type': 'integer', 'format': 'int64'}
    # videoUpDownStatus:{'type': 'integer', 'format': 'int32'}
    # videoUrl:{'type': 'string'}
    return "/back-http/video/updateSystemVideo"

@postRequest
def updateVideoProperties():
    # categoryId:{'type': 'integer', 'format': 'int64'}
    # chkType:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # labels:{'type': 'array', 'items': {'type': 'integer', 'format': 'int64'}}
    # videoId:{'type': 'integer', 'format': 'int64'}
    # videoLevel:{'type': 'string'}
    return "/back-http/video/updateVideoProperties"

@postRequest
def uploadFile():
    return "/back-http/video/uploadFile"

@postRequest
def uploadVideo():
    # addressName:{'type': 'string'}
    # aoiAddress:{'type': 'string'}
    # backUserId:{'type': 'integer', 'format': 'int64'}
    # browseCount:{'type': 'integer', 'format': 'int32'}
    # chkStatus:{'type': 'integer', 'format': 'int32'}
    # city:{'type': 'string'}
    # commentCount:{'type': 'integer', 'format': 'int32'}
    # completeCount:{'type': 'integer', 'format': 'int32'}
    # coverSize:{'type': 'string'}
    # createTime:{'type': 'string', 'format': 'date-time'}
    # delFlag:{'type': 'integer', 'format': 'int32'}
    # favoritesCount:{'type': 'integer', 'format': 'int32'}
    # gif:{'type': 'string'}
    # id:{'type': 'integer', 'format': 'int64'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # latitude:{'type': 'number', 'format': 'double'}
    # longitude:{'type': 'number', 'format': 'double'}
    # photo:{'type': 'string'}
    # province:{'type': 'string'}
    # region:{'type': 'string'}
    # score:{'type': 'string'}
    # shareCount:{'type': 'integer', 'format': 'int32'}
    # thirdVideoId:{'type': 'string'}
    # thumbsUpCount:{'type': 'integer', 'format': 'int32'}
    # userId:{'type': 'integer', 'format': 'int64'}
    # userSource:{'type': 'integer', 'format': 'int32'}
    # videoCategoryId:{'type': 'integer', 'format': 'int64'}
    # videoId:{'type': 'integer', 'format': 'int64'}
    # videoLabels:{'type': 'array', 'items': {'type': 'object'}}
    # videoLevel:{'type': 'string'}
    # videoOrigin:{'type': 'string'}
    # videoRecommendStatus:{'type': 'integer', 'format': 'int32'}
    # videoTitle:{'type': 'string'}
    # videoTopicId:{'type': 'integer', 'format': 'int64'}
    # videoUpDownStatus:{'type': 'integer', 'format': 'int32'}
    # videoUrl:{'type': 'string'}
    return "/back-http/video/uploadVideo"

@getRequest
def videoCommentChk_failPassCheck():
    # id:string
    # reason:string
    return "/back-http/videoCommentChk/failPassCheck"

@postRequest
def selectChkStatusDownCommentPage():
    # endCheckTime:{'type': 'string', 'format': 'date-time'}
    # keywords:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # startCheckTime:{'type': 'string', 'format': 'date-time'}
    # status:{'type': 'integer', 'format': 'int32'}
    return "/back-http/videoCommentChk/selectChkStatusDownCommentPage"

@postRequest
def selectChkStatusWaitCommentPage():
    # endCheckTime:{'type': 'string', 'format': 'date-time'}
    # keywords:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    # startCheckTime:{'type': 'string', 'format': 'date-time'}
    # status:{'type': 'integer', 'format': 'int32'}
    return "/back-http/videoCommentChk/selectChkStatusWaitCommentPage"

@getRequest
def videoCommentChk_successPassCheck():
    # id:string
    return "/back-http/videoCommentChk/successPassCheck"

@postRequest
def createVideoTopic():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # delFlag:{'type': 'integer', 'format': 'int32'}
    # displayStatus:{'type': 'integer', 'format': 'int32'}
    # followCount:{'type': 'integer', 'format': 'int32'}
    # followInitCount:{'type': 'integer', 'format': 'int32'}
    # hotOrder:{'type': 'integer', 'format': 'int32'}
    # hotStatus:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # imageUrl:{'type': 'string'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # operator:{'type': 'integer', 'format': 'int32'}
    # recommendOrder:{'type': 'integer', 'format': 'int32'}
    # recommendStatus:{'type': 'integer', 'format': 'int32'}
    # remark:{'type': 'string'}
    # sevenVideoCount:{'type': 'integer', 'format': 'int32'}
    # topicName:{'type': 'string'}
    # videoCount:{'type': 'integer', 'format': 'int32'}
    return "/back-http/videoTopic/createVideoTopic"

@getRequest
def deleteVideoTopics():
    # id:int64
    return "/back-http/videoTopic/deleteVideoTopics"

@postRequest
def editVideoTopics():
    # createTime:{'type': 'string', 'format': 'date-time'}
    # delFlag:{'type': 'integer', 'format': 'int32'}
    # displayStatus:{'type': 'integer', 'format': 'int32'}
    # followCount:{'type': 'integer', 'format': 'int32'}
    # followInitCount:{'type': 'integer', 'format': 'int32'}
    # hotOrder:{'type': 'integer', 'format': 'int32'}
    # hotStatus:{'type': 'integer', 'format': 'int32'}
    # id:{'type': 'integer', 'format': 'int64'}
    # imageUrl:{'type': 'string'}
    # lastUpdateTime:{'type': 'string', 'format': 'date-time'}
    # operator:{'type': 'integer', 'format': 'int32'}
    # recommendOrder:{'type': 'integer', 'format': 'int32'}
    # recommendStatus:{'type': 'integer', 'format': 'int32'}
    # remark:{'type': 'string'}
    # sevenVideoCount:{'type': 'integer', 'format': 'int32'}
    # topicName:{'type': 'string'}
    # videoCount:{'type': 'integer', 'format': 'int32'}
    return "/back-http/videoTopic/editVideoTopics"

@getRequest
def getAllEnabledHotTopics():
    # None
    return "/back-http/videoTopic/getAllEnabledHotTopics"

@getRequest
def getAllEnabledRecommendTopics():
    # None
    return "/back-http/videoTopic/getAllEnabledRecommendTopics"

@postRequest
def getVideoTopicsForBack():
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    return "/back-http/videoTopic/getVideoTopicsForBack"

@postRequest
def listVideoTopics():
    # beginTime:{'type': 'string', 'format': 'date-time'}
    # endTime:{'type': 'string', 'format': 'date-time'}
    # keywords:{'type': 'string'}
    # pageIndex:{'type': 'integer', 'format': 'int32'}
    # pageSize:{'type': 'integer', 'format': 'int32'}
    return "/back-http/videoTopic/listVideoTopics"

@postRequest
def orderHotTopics():
    # topicOrder:{'type': 'array', 'items': {'type': 'integer', 'format': 'int64'}}
    return "/back-http/videoTopic/orderHotTopics"

@postRequest
def orderRecommendTopics():
    # topicOrder:{'type': 'array', 'items': {'type': 'integer', 'format': 'int64'}}
    return "/back-http/videoTopic/orderRecommendTopics"

@postRequest
def getUserFollowTopicBack():
    # 获取用户关注的话题(后台)
    return "/back-http/user/getUserFollowTopicBack"

@getRequest
def getTalentMarkList():
    # 获取用户达人选项下拉列表
    return "/back-http/user/getTalentMarkList"

@postRequest
def getUserFavoritesMusicBack():
    # 获取用户关注的话题(后台)
    return "/back-http/user/getUserFavoritesMusicBack"

@postRequest
def getMusicByCondition():
    # 按条件查询音乐列表
    return "/back-http/music/getMusicByCondition"

@postRequest
def updateMusicToRecommend():
    # 批量修改音乐为推荐状态(后台)
    return "/back-http/music/updateMusicToRecommend"

@postRequest
def updateMusicByConditionBack():
    # 编辑音乐
    return "/back-http/music/updateMusicByConditionBack"

@postRequest
def getRecommendMusic():
    # 获取推荐的音乐
    return "/back-http/music/getRecommendMusic"

@getRequest
def contentPush_send():
    # 发送内容推送消息
    return "/back-http/contentPush/send"

@getRequest
def poPush_send():
    # 发送内容推送消息
    return "/back-http/poPush/send"

@postRequest
def poPush_add():
    # 添加官方推送
    return "/back-http/poPush/add"

@postRequest
def updateCommentTalking():
    # 后台编辑评论话术
    return "/back-http/talkingskill/updateCommentTalking"

@postRequest
def getCommentTalkingByCondition():
    # 按条件查询评论话术
    return "/back-http/talkingskill/getCommentTalkingByCondition"

@getRequest
def getCommentType():
    # 按条件查询评论话术
    return "/back-http/talkingskill/getCommentType"

@postRequest
def saveCommentTalking():
    # 按条件查询评论话术
    return "/back-http/talkingskill/saveCommentTalking"

@postRequest
def saveMusicBack():
    # 上传音乐(后台)
    return "/back-http/music/saveMusicBack"