#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.utils.Decorator import getRequest
from src.utils.Decorator import postRequest

@postRequest
def mcnInfo_updateTbMcnInfo():
    """(后台)修改mcn机构"""
    return "/back-http/mcnInfo/updateTbMcnInfo"

@postRequest
def mcnInfo_delTbMcnInfo():
    """(后台)删除mcn机构"""
    return "/back-http/mcnInfo/delTbMcnInfo"

@postRequest
def mcnInfo_getMcnTalentUser():
    """(后台)获取mcn关联的达人用户列表"""
    return "/back-http/mcnInfo/getMcnTalentUser"

@postRequest
def vehicle_matchVoiceChat():
    """1v1匹配聊天"""
    return "/app-http/vehicle/matchVoiceChat"

@postRequest
def vehicle_matchVoiceChatHangUp():
    """1v1匹配聊天挂断取消匹配"""
    return "/app-http/vehicle/matchVoiceChatHangUp"

@postRequest
def message_sendImMessage():
    """IM发送消息"""
    return "/app-http/message/sendImMessage"

@postRequest
def message_getUserImlist():
    """IM消息列表获取"""
    return "/app-http/message/getUserImlist"

@getRequest
def statusCode():
    """app（内容在备注）"""
    return "/app-http/statusCode"

@getRequest
def statusCode():
    """back（内容在备注）"""
    return "/back-http/statusCode"

@postRequest
def video_uploadFile():
    """上传文件(阿里云点播)"""
    return "/back-http/video/uploadFile"

@postRequest
def filter_saveFilter():
    """上传滤镜"""
    return "/back-http/filter/saveFilter"

@postRequest
def music_saveMusic():
    """上传音乐"""
    return "/app-http/music/saveMusic"

@postRequest
def music_saveMusicBack():
    """上传音乐(后台)"""
    return "/back-http/music/saveMusicBack"

@postRequest
def music_saveMusicType():
    """上传音乐分类"""
    return "/back-http/music/saveMusicType"

@postRequest
def chatRoom_updateChatRoomById():
    """主键更新聊天室"""
    return "/back-http/chatRoom/updateChatRoomById"

@postRequest
def discussGroup_updateDiscussGroupById():
    """主键更新讨论组"""
    return "/back-http/discussGroup/updateDiscussGroupById"

@postRequest
def talentMark_updateTalentMarkById():
    """主键更新达人标签"""
    return "/back-http/talentMark/updateTalentMarkById"

@getRequest
def video_getFollowLives():
    """主页-关注页直播列表"""
    return "/app-http/video/getFollowLives"

@getRequest
def video_getVideos():
    """主页-视频列表(关注页,发现页,最新页(前身是直播))"""
    return "/app-http/video/getVideos"

@postRequest
def videoPlay_saveReport():
    """举报视频/评论/用户"""
    return "/app-http/videoPlay/saveReport"

@postRequest
def carSalesRankimportCarSalesFromExcel():
    """从Excel导入车系销量排行榜"""
    return "/carSalesRank/importCarSalesFromExcel"

@getRequest
def packagedeleteVideoFromPackage():
    """从视频包中删除视频"""
    return "/package/deleteVideoFromPackage"

@postRequest
def department_delUserForDept():
    """从部门中移除用户"""
    return "/back-http/department/delUserForDept"

@postRequest
def user_updateBackUser():
    """修改/删除后台马甲号"""
    return "/back-http/user/updateBackUser"

@postRequest
def contentPush_update():
    """修改内容推送"""
    return "/back-http/contentPush/update"

@postRequest
def video_updateSystemVideo():
    """修改后台上传的视频"""
    return "/back-http/video/updateSystemVideo"

@postRequest
def backuser_updateDeptBackuser():
    """修改后台用户"""
    return "/back-http/backuser/updateDeptBackuser"

@postRequest
def poPushupdate():
    """修改官方推送"""
    return "/poPush/update"

@postRequest
def helperPushupdate():
    """修改小助手推送"""
    return "/helperPush/update"

@postRequest
def user_setUserGetui():
    """修改推送信息"""
    return "/app-http/user/setUserGetui"

@postRequest
def backuserupdateUserPassword():
    """修改用户密码"""
    return "/backuser/updateUserPassword"

@postRequest
def topic_updateTopicFollowStatus():
    """修改用户对话题的关注状态"""
    return "/app-http/topic/updateTopicFollowStatus"

@postRequest
def carBrand_updateCarBrandFollowStatus():
    """修改用户对车品牌的关注状态"""
    return "/app-http/carBrand/updateCarBrandFollowStatus"

@postRequest
def carSeries_updateCarSeriesFollowStatus():
    """修改用户对车系的关注状态"""
    return "/app-http/carSeries/updateCarSeriesFollowStatus"

@postRequest
def backuserupdateUserPhone():
    """修改用户手机号"""
    return "/backuser/updateUserPhone"

@postRequest
def backuser_updateUserForAuth():
    """修改用户的权限, 对权限增加或减少,此操作只能由管理员或者部门管理员来进行"""
    return "/back-http/backuser/updateUserForAuth"

@postRequest
def department_updateDepartment():
    """修改部门/删除部门"""
    return "/back-http/department/updateDepartment"

@postRequest
def department_updateDepartmentForAuth():
    """修改部门的权限, 对权限增加或减少, 此操作只能由平台admin操作(给部门初始化角色分配权限)"""
    return "/back-http/department/updateDepartmentForAuth"

@postRequest
def department_updateAuthForDeptRole():
    """修改部门角色权限点"""
    return "/back-http/department/updateAuthForDeptRole"

@postRequest
def live_stopPlay():
    """关闭直播"""
    return "/app-http/live/stopPlay"

@postRequest
def live_forbidstream():
    """关闭直播间"""
    return "/back-http/live/forbidstream"

@postRequest
def playerInfo_createTbPlayerInfo():
    """创建主播信息"""
    return "/back-http/playerInfo/createTbPlayerInfo"

@postRequest
def user_createQRCodeCard():
    """创建二维码名片"""
    return "/app-http/user/createQRCodeCard"

@postRequest
def backuser_createDeptBackuser():
    """创建后台用户"""
    return "/back-http/backuser/createDeptBackuser"

@postRequest
def backuser_rejectApplyJoinDeptMessage():
    """创建拒绝申请加入部门的消息"""
    return "/back-http/backuser/rejectApplyJoinDeptMessage"

@postRequest
def backuser_createApplyDeptMessage():
    """创建申请加入部门时产生的消息"""
    return "/back-http/backuser/createApplyDeptMessage"

@postRequest
def vehiclecreateChatRoom():
    """创建聊天室"""
    return "/vehicle/createChatRoom"

@postRequest
def chatRoom_insertChatRoom():
    """创建聊天室"""
    return "/back-http/chatRoom/insertChatRoom"

@postRequest
def videoTopic_createVideoTopic():
    """创建视频话题"""
    return "/back-http/videoTopic/createVideoTopic"

@postRequest
def discussGroup_insertDiscussGroup():
    """创建讨论组"""
    return "/back-http/discussGroup/insertDiscussGroup"

@postRequest
def talentMark_saveTalentMark():
    """创建达人标签"""
    return "/back-http/talentMark/saveTalentMark"

@postRequest
def talentMark_deleteTalentMarkById_id():
    """删除"""
    return "/back-http/talentMark/deleteTalentMarkById/{id}"

@postRequest
def carBrand_deleteCarBrandById():
    """删除品牌"""
    return "/back-http/carBrand/deleteCarBrandById"

@postRequest
def dictData_delete_id():
    """删除字典数据"""
    return "/back-http/dictData/delete/{id}"

@postRequest
def dictType_delete_id():
    """删除字典类型"""
    return "/back-http/dictType/delete/{id}"

@postRequest
def talkingskill_deleteTalkingSkill():
    """删除指定的话术"""
    return "/back-http/talkingskill/deleteTalkingSkill"

@postRequest
def filter_deleteFilter_id():
    """删除滤镜"""
    return "/back-http/filter/deleteFilter/{id}"

@postRequest
def version_deleteVersion():
    """删除版本"""
    return "/back-http/version/deleteVersion"

@postRequest
def user_deleteUserEmerContactById():
    """删除紧急联系人"""
    return "/app-http/user/deleteUserEmerContactById"

@postRequest
def videoPlay_delVideo():
    """删除视频"""
    return "/app-http/videoPlay/delVideo"

@getRequest
def categorydelete():
    """删除视频分类"""
    return "/category/delete"

@getRequest
def labeldelete():
    """删除视频标签"""
    return "/label/delete"

@getRequest
def packagedelete():
    """删除视频运营包"""
    return "/package/delete"

@postRequest
def videoTopic_deleteVideoTopics():
    """删除话题"""
    return "/back-http/videoTopic/deleteVideoTopics"

@postRequest
def carSeries_deleteCarSeriesById():
    """删除车系"""
    return "/back-http/carSeries/deleteCarSeriesById"

@getRequest
def carSalesRank_deleteCarSalesRankById():
    """删除车系销量排行榜"""
    return "/back-http/carSalesRank/deleteCarSalesRankById"

@postRequest
def department_delDeptRole():
    """删除部门角色"""
    return "/back-http/department/delDeptRole"

@postRequest
def music_deleteMusicType():
    """删除音乐类型"""
    return "/back-http/music/deleteMusicType"

@postRequest
def backuser_decideApplyDept():
    """判断申请加入部门的操作"""
    return "/back-http/backuser/decideApplyDept"

@postRequest
def backuser_sendMessage():
    """发消息"""
    return "/back-http/backuser/sendMessage"

@getRequest
def contentPushsend():
    """发送内容推送消息"""
    return "/contentPush/send"

@getRequest
def poPushsend():
    """发送官方推送消息"""
    return "/poPush/send"

@getRequest
def helperPushsend():
    """发送小助手推送消息"""
    return "/helperPush/send"

@getRequest
def contentPushcancelSend():
    """取消发送内容推送消息"""
    return "/contentPush/cancelSend"

@getRequest
def poPushcancelSend():
    """取消发送官方推送消息"""
    return "/poPush/cancelSend"

@getRequest
def helperPushcancelSend():
    """取消发送小助手推送消息"""
    return "/helperPush/cancelSend"

@postRequest
def logincancelLogin():
    """取消登录"""
    return "/login/cancelLogin"

@postRequest
def live_resumeLiveStream():
    """取消禁播"""
    return "/back-http/live/resumeLiveStream"

@getRequest
def video_getRecommendTalent():
    """可能感兴趣的人"""
    return "/app-http/video/getRecommendTalent"

@getRequest
def video_getRecommendTalentVideo():
    """可能感兴趣的人视频(第二页及以后页码的视频)"""
    return "/app-http/video/getRecommendTalentVideo"

@postRequest
def department_agreeApplyJoinDept():
    """同意用户加入部门的申请"""
    return "/back-http/department/agreeApplyJoinDept"

@postRequest
def video_uploadVideo():
    """后台上传视频"""
    return "/back-http/video/uploadVideo"

@postRequest
def talkingskill_saveCommentTalking():
    """后台添加评论话术"""
    return "/back-http/talkingskill/saveCommentTalking"

@postRequest
def backuserlogin():
    """后台用户登录接口"""
    return "/backuser/login"

@postRequest
def backuser_backLoginOut():
    """后台用户退出登录"""
    return "/back-http/backuser/backLoginOut"

@postRequest
def talkingskill_updateCommentTalking():
    """后台编辑评论话术"""
    return "/back-http/talkingskill/updateCommentTalking"

@getRequest
def reportdealReport():
    """处理举报"""
    return "/report/dealReport"

@postRequest
def user_exportUserDataList():
    """导出用户列表"""
    return "/back-http/user/exportUserDataList"

@postRequest
def live_startPlay():
    """开始直播"""
    return "/app-http/live/startPlay"

@getRequest
def reportignoreReport():
    """忽略举报接口"""
    return "/report/ignoreReport"

@getRequest
def appealsuccess():
    """成功申诉"""
    return "/appeal/success"

@getRequest
def music_myCollectingMusic():
    """我收藏音乐列表"""
    return "/app-http/music/myCollectingMusic"

@postRequest
def loginscanQrCode():
    """扫描二维码"""
    return "/login/scanQrCode"

@postRequest
def music_updateMusicToRecommend():
    """批量修改音乐为推荐状态(后台)"""
    return "/back-http/music/updateMusicToRecommend"

@postRequest
def catMachineWebsocketuid():
    """报警消息通知（WebSocket）"""
    return "/catMachineWebsocket/{uid}"

@postRequest
def vehicleVideo_saveAlarmVehicleVideo():
    """报警车机视频上传"""
    return "/app-http/vehicleVideo/saveAlarmVehicleVideo"

@postRequest
def user_updateBlackUserList():
    """拉黑/取消拉黑用户"""
    return "/app-http/user/updateBlackUserList"

@postRequest
def shot_saveVideo():
    """拍摄-上传视频"""
    return "/app-http/shot/saveVideo"

@postRequest
def shot_saveVehicleVideo():
    """拍摄-上传车机视频"""
    return "/app-http/shot/saveVehicleVideo"

@getRequest
def shot_getAliStsResponse():
    """拍摄-获取sts token 凭证"""
    return "/app-http/shot/getAliStsResponse"

@getRequest
def shot_getVodMediaResponse():
    """拍摄-获取阿里云token(andriod)"""
    return "/app-http/shot/getVodMediaResponse"

@postRequest
def talkingskill_getCommentTalkingByCondition():
    """按条件查询评论话术"""
    return "/back-http/talkingskill/getCommentTalkingByCondition"

@postRequest
def music_getMusicTypeByCondition():
    """按条件查询音乐分类列表"""
    return "/back-http/music/getMusicTypeByCondition"

@postRequest
def music_getMusicByCondition():
    """按条件查询音乐列表"""
    return "/back-http/music/getMusicByCondition"

@postRequest
def videoTopic_orderRecommendTopics():
    """推荐话题的重新排序"""
    return "/back-http/videoTopic/orderRecommendTopics"

@getRequest
def music_recommendMusic():
    """推荐音乐列表"""
    return "/app-http/music/recommendMusic"

@postRequest
def version_submitNewVersion():
    """提交新版本信息"""
    return "/back-http/version/submitNewVersion"

@postRequest
def user_submitAppeal():
    """提交申诉"""
    return "/app-http/user/submitAppeal"

@postRequest
def user_getUserListByKeyword():
    """搜索用户"""
    return "/app-http/user/getUserListByKeyword"

@postRequest
def video_getVideoByKeyword():
    """搜索视频"""
    return "/app-http/video/getVideoByKeyword"

@postRequest
def topic_getTopicByKeyword():
    """搜索话题"""
    return "/app-http/topic/getTopicByKeyword"

@postRequest
def music_collectingMusic():
    """收藏音乐"""
    return "/app-http/music/collectingMusic"

@postRequest
def mcnInfo_createTbMcnInfo():
    """新建mcn 机构"""
    return "/back-http/mcnInfo/createTbMcnInfo"

@postRequest
def talkingskill_submitNew():
    """新建话术模版"""
    return "/back-http/talkingskill/submitNew"

@postRequest
def talentMark_useOrNot():
    """是否使用"""
    return "/back-http/talentMark/useOrNot"

@postRequest
def carBrand_updateCarBrand():
    """更新品牌"""
    return "/back-http/carBrand/updateCarBrand"

@postRequest
def dictData_update():
    """更新字典数据"""
    return "/back-http/dictData/update"

@postRequest
def dictType_update():
    """更新字典类型"""
    return "/back-http/dictType/update"

@postRequest
def user_updateUserEmerContact():
    """更新紧急联系人"""
    return "/app-http/user/updateUserEmerContact"

@postRequest
def videoupdateVideoProperties():
    """更新视频相关属性接口"""
    return "/video/updateVideoProperties"

@postRequest
def carSeries_updateCarSeries():
    """更新车系"""
    return "/back-http/carSeries/updateCarSeries"

@getRequest
def nearbyUser_getNearByUser():
    """最新-附近的人列表"""
    return "/app-http/nearbyUser/getNearByUser"

@getRequest
def login_verifyLogin():
    """极验-验证"""
    return "/app-http/login/verifyLogin"

@getRequest
def login_startCaptcha():
    """极验-验证初始化"""
    return "/app-http/login/startCaptcha"

@postRequest
def user_getAppUserBasicInfo():
    """查看个人/他人基本信息"""
    return "/app-http/user/getAppUserBasicInfo"

@postRequest
def v104_user_getAppUserBasicInfo():
    """查看个人/他人基本信息"""
    return "/app-http/v104/user/getAppUserBasicInfo"

@postRequest
def backuser_getBackuserDetail():
    """查看后台用户详细信息"""
    return "/back-http/backuser/getBackuserDetail"

@getRequest
def user_getUserPushStatus():
    """查看用户各通知状态"""
    return "/app-http/user/getUserPushStatus"

@postRequest
def live_hasRightToPlay():
    """查看用户是否有直播权限"""
    return "/app-http/live/hasRightToPlay"

@postRequest
def packageselectPackageVideoPage():
    """查看视频包视频"""
    return "/package/selectPackageVideoPage"

@getRequest
def video_getVideoLabelAndTopic():
    """查看视频详情,获取该视频的标签和话题"""
    return "/back-http/video/getVideoLabelAndTopic"

@postRequest
def department_findDepartmentUser():
    """查看部门成员"""
    return "/back-http/department/findDepartmentUser"

@postRequest
def video_selectUnderLineVideoPage():
    """查询下架视频分页列表"""
    return "/back-http/video/selectUnderLineVideoPage"

@postRequest
def playerInfo_getTbPlayerInfos():
    """查询主播列表"""
    return "/back-http/playerInfo/getTbPlayerInfos"

@postRequest
def report_query():
    """查询举报信息列表"""
    return "/back-http/report/query"

@postRequest
def contentPushgetPageList():
    """查询内容推送分页列表"""
    return "/contentPush/getPageList"

@postRequest
def poPushgetPageList():
    """查询官方推送分页列表"""
    return "/poPush/getPageList"

@postRequest
def vehicle_isTargetHangUp():
    """查询对方是否取消匹配"""
    return "/app-http/vehicle/isTargetHangUp"

@postRequest
def helperPushgetPageList():
    """查询小助手推送分页列表"""
    return "/helperPush/getPageList"

@postRequest
def userModifyRecord_selectUserModifyRecordChkStatusDownPage():
    """查询已审核分页列表"""
    return "/back-http/userModifyRecord/selectUserModifyRecordChkStatusDownPage"

@postRequest
def videoCommentChk_selectChkStatusDownCommentPage():
    """查询已审核分页列表"""
    return "/back-http/videoCommentChk/selectChkStatusDownCommentPage"

@postRequest
def video_selectVideoPage():
    """查询平台视频分页列表"""
    return "/back-http/video/selectVideoPage"

@postRequest
def videoCommentChkselectChkStatusWaitCommentPage():
    """查询待审核分页列表"""
    return "/videoCommentChk/selectChkStatusWaitCommentPage"

@getRequest
def login_queryLogin():
    """查询扫码登录结果"""
    return "/app-http/login/queryLogin"

@postRequest
def video_selectRecommendVideoPage():
    """查询推荐视频分页列表"""
    return "/back-http/video/selectRecommendVideoPage"

@postRequest
def vehicle_selectMatchChatCount():
    """查询正在匹配聊天的人"""
    return "/app-http/vehicle/selectMatchChatCount"

@postRequest
def carSalesRank_selectCarSalesPage():
    """查询热门销量榜分页列表"""
    return "/back-http/carSalesRank/selectCarSalesPage"

@postRequest
def version_query():
    """查询版本列表"""
    return "/back-http/version/query"

@postRequest
def video_selectVideoPageForSpecialUser():
    """查询特殊用户视频分页列表"""
    return "/back-http/video/selectVideoPageForSpecialUser"

@postRequest
def userModifyRecordselectUserModifyRecordChkStatusWaitPage():
    """查询用户审核待审核分页列表"""
    return "/userModifyRecord/selectUserModifyRecordChkStatusWaitPage"

@getRequest
def userModifyRecordselectUserOperateLogByModifyId():
    """查询用户审核日志列表"""
    return "/userModifyRecord/selectUserOperateLogByModifyId"

@postRequest
def appeal_query():
    """查询申诉列表"""
    return "/back-http/appeal/query"

@postRequest
def appeal_getAppealOrigin():
    """查询申诉记录的处理来源"""
    return "/back-http/appeal/getAppealOrigin"

@getRequest
def vehiclequeryChatRoom():
    """查询聊天室"""
    return "/vehicle/queryChatRoom"

@postRequest
def categoryquery():
    """查询视频分类分页列表"""
    return "/category/query"

@postRequest
def packageselectPackageVideoList():
    """查询视频包视频列表-不分页"""
    return "/package/selectPackageVideoList"

@postRequest
def labelquery():
    """查询视频标签分页列表"""
    return "/label/query"

@postRequest
def packagequery():
    """查询视频运营包分页列表"""
    return "/package/query"

@postRequest
def talkingskill_query():
    """查询话术列表"""
    return "/back-http/talkingskill/query"

@postRequest
def backuserverifyOldPassword():
    """校验用户旧密码"""
    return "/backuser/verifyOldPassword"

@getRequest
def categoryid():
    """根据ID查找视频分类"""
    return "/category/id"

@getRequest
def packageid():
    """根据ID查找视频包"""
    return "/package/id"

@getRequest
def labelid():
    """根据ID查找视频标签"""
    return "/label/id"

@getRequest
def carBrand_getCarBrandById():
    """根据ID获取品牌"""
    return "/back-http/carBrand/getCarBrandById"

@getRequest
def message_getAlarmMessageById():
    """根据ID获取报警消息详情"""
    return "/back-http/message/getAlarmMessageById"

@getRequest
def carSeries_getCarSeriesById():
    """根据ID获取车系"""
    return "/back-http/carSeries/getCarSeriesById"

@getRequest
def live_getTbLiveRecordById():
    """根据id获取直播间信息"""
    return "/app-http/live/getTbLiveRecordById"

@postRequest
def version_id():
    """根据id获得指定的版本信息"""
    return "/back-http/version/id"

@getRequest
def carBrand_getCarByKeyword():
    """根据关键字搜索车品牌和车系"""
    return "/app-http/carBrand/getCarByKeyword"

@postRequest
def message_updateByMessageId():
    """根据报警消息ID更新"""
    return "/back-http/message/updateByMessageId"

@getRequest
def message_selectVehicleVideoPackagePosition():
    """根据报警消息ID获取所有视频包的位置信息"""
    return "/back-http/message/selectVehicleVideoPackagePosition"

@postRequest
def department_findDepartmentByDTO():
    """根据条件查询部门列表"""
    return "/back-http/department/findDepartmentByDTO"

@postRequest
def filter_getFilterByCondition():
    """根据条件获取滤镜"""
    return "/back-http/filter/getFilterByCondition"

@postRequest
def videoTopic_listVideoTopics():
    """根据查询条件获得话题列表"""
    return "/back-http/videoTopic/listVideoTopics"

@postRequest
def feedback_query():
    """根据查询条件，获得反馈列表"""
    return "/back-http/feedback/query"

@postRequest
def punishRecord_relievePunish():
    """根据用户ID解封"""
    return "/back-http/punishRecord/relievePunish"

@getRequest
def music_listMusics_musicType():
    """根据音乐类型获取音乐列表"""
    return "/app-http/music/listMusics/musicType"

@postRequest
def message_getMessageList():
    """消息列表获取"""
    return "/app-http/message/getMessageList"

@postRequest
def message_messageStatistics():
    """消息状态修改"""
    return "/app-http/message/messageStatistics"

@postRequest
def contentPush_add():
    """添加内容推送"""
    return "/back-http/contentPush/add"

@postRequest
def user_createBackUser():
    """添加后台马甲号"""
    return "/back-http/user/createBackUser"

@postRequest
def carBrand_saveCarBrand():
    """添加品牌"""
    return "/back-http/carBrand/saveCarBrand"

@postRequest
def punishRecord_addPunishRecord():
    """添加处罚记录"""
    return "/back-http/punishRecord/addPunishRecord"

@postRequest
def dictData_save():
    """添加字典数据"""
    return "/back-http/dictData/save"

@postRequest
def dictType_save():
    """添加字典类型"""
    return "/back-http/dictType/save"

@postRequest
def poPush_add():
    """添加官方推送"""
    return "/back-http/poPush/add"

@postRequest
def helperPush_add():
    """添加小助手推送"""
    return "/back-http/helperPush/add"

@postRequest
def carSalesRank_editCarSales():
    """添加或修改销量排行榜"""
    return "/back-http/carSalesRank/editCarSales"

@postRequest
def message_saveAlarmMessage():
    """添加报警消息"""
    return "/app-http/message/saveAlarmMessage"

@postRequest
def user_submitFeedback():
    """添加系统反馈"""
    return "/app-http/user/submitFeedback"

@postRequest
def user_saveUserEmerContact():
    """添加紧急联系人"""
    return "/app-http/user/saveUserEmerContact"

@postRequest
def category_submit():
    """添加视频分类"""
    return "/back-http/category/submit"

@postRequest
def labelsubmit():
    """添加视频标签"""
    return "/label/submit"

@postRequest
def packageaddVideosToPackage():
    """添加视频至视频包"""
    return "/package/addVideosToPackage"

@postRequest
def packagesubmit():
    """添加视频运营包"""
    return "/package/submit"

@postRequest
def carSeries_saveSeries():
    """添加车系"""
    return "/back-http/carSeries/saveSeries"

@postRequest
def department_createDepartment():
    """添加部门"""
    return "/back-http/department/createDepartment"

@postRequest
def filter_sortFilter():
    """滤镜-拍摄排序"""
    return "/back-http/filter/sortFilter"

@postRequest
def videoTopic_orderHotTopics():
    """热门话题排序"""
    return "/back-http/videoTopic/orderHotTopics"

@postRequest
def carSeries_selectCarSalesPage():
    """热门销量榜分页列表"""
    return "/app-http/carSeries/selectCarSalesPage"

@postRequest
def loginsaveQrCode():
    """生成二维码信息"""
    return "/login/saveQrCode"

@postRequest
def user_getUserLinkedVideo():
    """用户主页视频列表-1发布  2赞过  3收藏"""
    return "/app-http/user/getUserLinkedVideo"

@postRequest
def v104_user_getUserLinkedVideo():
    """用户主页视频列表-1发布  2赞过  3收藏_copy"""
    return "/app-http/v104/user/getUserLinkedVideo"

@getRequest
def userModifyRecord_failPassCheck():
    """用户信息审核不通过接口"""
    return "/app-http/userModifyRecord/failPassCheck"

@getRequest
def userModifyRecordsuccessPassCheck():
    """用户信息审核通过接口"""
    return "/userModifyRecord/successPassCheck"

@postRequest
def user_updateUserFollowStatus():
    """用户关注"""
    return "/app-http/user/updateUserFollowStatus"

@getRequest
def appealfail():
    """申诉失败"""
    return "/appeal/fail"

@postRequest
def login_ykLogin():
    """登录--游客"""
    return "/app-http/login/ykLogin"

@postRequest
def login_logOut():
    """登录--用户退出登录"""
    return "/app-http/login/logOut"

@postRequest
def login_thirdLogin():
    """登录--第三方登陆接口"""
    return "/app-http/login/thirdLogin"

@getRequest
def login_getSmsCode():
    """登录--获取短信验证码"""
    return "/app-http/login/getSmsCode"

@postRequest
def login_checkSmsCode():
    """登录--验证短信验证码"""
    return "/app-http/login/checkSmsCode"

@postRequest
def loginconfirmLogin():
    """确认登录"""
    return "/login/confirmLogin"

@postRequest
def backuser_disableBackUser():
    """禁用/启用后台用户"""
    return "/back-http/backuser/disableBackUser"

@postRequest
def department_createRoleForDept():
    """给部门添加角色"""
    return "/back-http/department/createRoleForDept"

@postRequest
def talkingskill_editTalkingSkill():
    """编辑 指定的话术模版templateContent"""
    return "/back-http/talkingskill/editTalkingSkill"

@postRequest
def filter_updateFilterByCondition():
    """编辑滤镜"""
    return "/back-http/filter/updateFilterByCondition"

@postRequest
def version_editVersion():
    """编辑版本信息"""
    return "/back-http/version/editVersion"

@postRequest
def user_updateUserInfo():
    """编辑用户信息"""
    return "/app-http/user/updateUserInfo"

@postRequest
def categoryupdate():
    """编辑视频分类"""
    return "/category/update"

@postRequest
def labelupdate():
    """编辑视频标签"""
    return "/label/update"

@postRequest
def packageupdate():
    """编辑视频运营包"""
    return "/package/update"

@postRequest
def videoTopic_editVideoTopics():
    """编辑话题"""
    return "/back-http/videoTopic/editVideoTopics"

@postRequest
def department_updateRole():
    """编辑部门角色"""
    return "/back-http/department/updateRole"

@postRequest
def music_updateMusicByConditionBack():
    """编辑音乐"""
    return "/back-http/music/updateMusicByConditionBack"

@postRequest
def music_updateMusicTypeByCondition():
    """编辑音乐分类类型"""
    return "/back-http/music/updateMusicTypeByCondition"

@getRequest
def message_getPoMessage():
    """获取PO官方推送"""
    return "/app-http/message/getPoMessage"

@postRequest
def mcnInfo_getTbMcnInfoPage():
    """获取mcn 机构列表"""
    return "/back-http/mcnInfo/getTbMcnInfoPage"

@getRequest
def user_getMcnInfoList():
    """获取mcn机构列表"""
    return "/back-http/user/getMcnInfoList"

@getRequest
def video_getAliStsResponse():
    """获取sts token凭证"""
    return "/back-http/video/getAliStsResponse"

@getRequest
def openqiyucalltoolbarskd():
    """获取七鱼呼叫工具条sdk"""
    return "/open/qiyu/call_toolbar_skd"

@postRequest
def playerInfo_getPlayerInfo():
    """获取主播信息"""
    return "/back-http/playerInfo/getPlayerInfo"

@getRequest
def playerInfo_getPlayerInfo():
    """获取主播信息"""
    return "/back-http/playerInfo/getPlayerInfo"

@postRequest
def playerInfo_getTbLiveRecordByUserIdPage():
    """获取主播直播信息"""
    return "/back-http/playerInfo/getTbLiveRecordByUserIdPage"

@postRequest
def videoPlay_queryTalkingSkill():
    """获取举报/审核的内容"""
    return "/app-http/videoPlay/queryTalkingSkill"

@getRequest
def rank_allTop():
    """获取全部榜单前三个标题名称"""
    return "/app-http/rank/allTop"

@getRequest
def video_getNewAddFollowVideoCount():
    """获取关注视频新增数量"""
    return "/app-http/video/getNewAddFollowVideoCount"

@getRequest
def video_getOneVideo():
    """获取单个视频信息"""
    return "/app-http/video/getOneVideo"

@postRequest
def backuser_getBackUserCenter():
    """获取后台用户个人中心"""
    return "/back-http/backuser/getBackUserCenter"

@postRequest
def user_getBackuserUserInfo():
    """获取后台用户创建的马甲号列表"""
    return "/back-http/user/getBackuserUserInfo"

@getRequest
def department_getBackuserMessageNum():
    """获取后台用户未读消息数量"""
    return "/back-http/department/getBackuserMessageNum"

@postRequest
def carBrand_selectCarBrandPage():
    """获取品牌分页数据"""
    return "/back-http/carBrand/selectCarBrandPage"

@getRequest
def uniqueId():
    """获取唯一ID"""
    return "/app-http/uniqueId"

@getRequest
def shot_getVodImageResponse():
    """获取图片上传凭证"""
    return "/app-http/shot/getVodImageResponse"

@postRequest
def dictData_listUsable():
    """获取字典可用数据，不分页"""
    return "/back-http/dictData/listUsable"

@postRequest
def dictData_list():
    """获取字典数据分页数据"""
    return "/back-http/dictData/list"

@getRequest
def dictData_detail_id():
    """获取字典数据详情"""
    return "/back-http/dictData/detail/{id}"

@postRequest
def dictType_list():
    """获取字典类型分页数据"""
    return "/back-http/dictType/list"

@getRequest
def dictType_detail_id():
    """获取字典类型详情"""
    return "/back-http/dictType/detail/{id}"

@postRequest
def videogetChkResultVideoPage():
    """获取审核结果视频列表"""
    return "/video/getChkResultVideoPage"

@postRequest
def videogetChkVideoPage():
    """获取审核视频列表"""
    return "/video/getChkVideoPage"

@postRequest
def user_selectPunishUserPage():
    """获取封禁用户分页数据"""
    return "/back-http/user/selectPunishUserPage"

@postRequest
def punishRecord_selectPunishRecordPage():
    """获取封禁记录分页数据"""
    return "/back-http/punishRecord/selectPunishRecordPage"

@getRequest
def message_getHelperMessage():
    """获取小助手推送"""
    return "/app-http/message/getHelperMessage"

@postRequest
def backusergetBackUserList():
    """获取平台用户列表"""
    return "/backuser/getBackUserList"

@getRequest
def video_getLocalVideos():
    """获取当前位置视频列表"""
    return "/app-http/video/getLocalVideos"

@postRequest
def user_getUserFansInfo():
    """获取我的粉丝的信息"""
    return "/back-http/user/getUserFansInfo"

@getRequest
def live_getRoomManagers():
    """获取房间禁言列表和房间管理员信息"""
    return "/app-http/live/getRoomManagers"

@postRequest
def mcnInfo_listAllTbMcnInfos():
    """获取所有mcn列表"""
    return "/back-http/mcnInfo/listAllTbMcnInfos"

@postRequest
def carBrand_selectCarBrand():
    """获取所有可用的车品牌"""
    return "/app-http/carBrand/selectCarBrand"

@postRequest
def carSeries_selectCarSeries():
    """获取所有可用的车系"""
    return "/app-http/carSeries/selectCarSeries"

@getRequest
def live_getAllLivingLiveRecords():
    """获取所有正在直播信息"""
    return "/back-http/live/getAllLivingLiveRecords"

@getRequest
def message_getAlarmMessage():
    """获取报警消息"""
    return "/back-http/message/getAlarmMessage"

@getRequest
def message_getAlarmMessageByMessageId():
    """获取报警消息详情"""
    return "/back-http/message/getAlarmMessageByMessageId"

@postRequest
def music_getRecommendMusic():
    """获取推荐的音乐"""
    return "/back-http/music/getRecommendMusic"

@getRequest
def serviceStatus():
    """获取服务状态"""
    return "/back-http/serviceStatus"

@getRequest
def serviceStatus():
    """获取服务状态"""
    return "/app-http/serviceStatus"

@postRequest
def live_getLivingLiveRecords():
    """获取正在直播的房间信息"""
    return "/back-http/live/getLivingLiveRecords"

@getRequest
def filter_listFilters():
    """获取滤镜列表"""
    return "/app-http/filter/listFilters"

@postRequest
def user_getVestUserList():
    """获取特殊用户(马甲)账号,用于创建特殊用户视频"""
    return "/back-http/user/getVestUserList"

@postRequest
def user_getUserLinkedUser():
    """获取用户关注的人, 粉丝(1关注  2粉丝)"""
    return "/app-http/user/getUserLinkedUser"

@postRequest
def user_getUserFollowInfo():
    """获取用户关注的用户信息"""
    return "/back-http/user/getUserFollowInfo"

@postRequest
def user_getAppUserFollowTopic():
    """获取用户关注的话题"""
    return "/app-http/user/getAppUserFollowTopic"

@postRequest
def user_getUserFollowTopicBack():
    """获取用户关注的话题(后台)"""
    return "/back-http/user/getUserFollowTopicBack"

@postRequest
def user_getUserDataList():
    """获取用户列表"""
    return "/back-http/user/getUserDataList"

@postRequest
def user_getUserVideoPublish():
    """获取用户发布的视频信息"""
    return "/back-http/user/getUserVideoPublish"

@postRequest
def user_getUserBasicInfo():
    """获取用户基本信息"""
    return "/back-http/user/getUserBasicInfo"

@postRequest
def user_getUserFavoritesVideo():
    """获取用户收藏的视频信息"""
    return "/back-http/user/getUserFavoritesVideo"

@postRequest
def user_getUserFavoritesMusicBack():
    """获取用户收藏的音乐信息"""
    return "/back-http/user/getUserFavoritesMusicBack"

@postRequest
def message_getUserMessageList():
    """获取用户消息列表"""
    return "/app-http/message/getUserMessageList"

@postRequest
def backuser_getBackUserMessageList():
    """获取用户消息列表"""
    return "/back-http/backuser/getBackUserMessageList"

@postRequest
def message_getUnreadMessageNum():
    """获取用户消息未读数量"""
    return "/app-http/message/getUnreadMessageNum"

@postRequest
def user_getUserThumbUpVideo():
    """获取用户点赞的视频信息"""
    return "/back-http/user/getUserThumbUpVideo"

@postRequest
def auth_getUserAuth():
    """获取用户的权限点"""
    return "/back-http/auth/getUserAuth"

@postRequest
def video_getMyFootprintVideo():
    """获取用户的足迹"""
    return "/app-http/video/getMyFootprintVideo"

@postRequest
def user_getBlackUserList():
    """获取用户的黑名单列表"""
    return "/app-http/user/getBlackUserList"

@getRequest
def user_getTalentMarkList():
    """获取用户达人选项下拉列表"""
    return "/back-http/user/getTalentMarkList"

@postRequest
def live_getLiveList():
    """获取直播列表"""
    return "/app-http/live/getLiveList"

@postRequest
def backusergetBackUserSmsCode():
    """获取短信验证码"""
    return "/backuser/getBackUserSmsCode"

@postRequest
def auth_getSystemInitAuth():
    """获取系统初始化权限"""
    return "/back-http/auth/getSystemInitAuth"

@getRequest
def message_getSystemMessage():
    """获取系统推送"""
    return "/app-http/message/getSystemMessage"

@getRequest
def user_selectUserEmerContact():
    """获取紧急联系人"""
    return "/app-http/user/selectUserEmerContact"

@postRequest
def chatRoom_selectChatRoomPage():
    """获取聊天室分页数据"""
    return "/back-http/chatRoom/selectChatRoomPage"

@getRequest
def video_getUserVideo():
    """获取视频(消息页)"""
    return "/app-http/video/getUserVideo"

@postRequest
def video_getVideoAllCategory():
    """获取视频所有的分类"""
    return "/back-http/video/getVideoAllCategory"

@postRequest
def video_getVideoAllLabel():
    """获取视频所有的标签"""
    return "/back-http/video/getVideoAllLabel"

@postRequest
def video_getVideoAllTopic():
    """获取视频所有的话题"""
    return "/back-http/video/getVideoAllTopic"

@postRequest
def video_selectVideoRankPage():
    """获取视频榜单分页数据"""
    return "/back-http/video/selectVideoRankPage"

@postRequest
def auth_getRoleAuth():
    """获取角色权限点"""
    return "/back-http/auth/getRoleAuth"

@postRequest
def discussGroup_selectDiscussGroupPage():
    """获取讨论组分页数据"""
    return "/back-http/discussGroup/selectDiscussGroupPage"

@getRequest
def talkingskill_getCommentType():
    """获取评论话术标签"""
    return "/back-http/talkingskill/getCommentType"

@postRequest
def carBrand_selectCarBrandPoolHotPage():
    """获取车品牌热门榜分页数据"""
    return "/app-http/carBrand/selectCarBrandPoolHotPage"

@getRequest
def carBrand_getCarBrandById():
    """获取车品牌详情，包括其所有车系"""
    return "/app-http/carBrand/getCarBrandById"

@postRequest
def vehicleVideo_selectVehicleVideoPackage():
    """获取车机视频包及其视频分页数据"""
    return "/app-http/vehicleVideo/selectVehicleVideoPackage"

@postRequest
def message_selectVehicleVideoPackage():
    """获取车机视频包及其视频分页数据"""
    return "/back-http/message/selectVehicleVideoPackage"

@postRequest
def carSeries_selectCarSeriesPage():
    """获取车系分页数据"""
    return "/back-http/carSeries/selectCarSeriesPage"

@postRequest
def carSeries_selectCarSeriesPoolHotPage():
    """获取车系热门榜分页数据"""
    return "/app-http/carSeries/selectCarSeriesPoolHotPage"

@getRequest
def carSeries_getCarSeriesById():
    """获取车系详情"""
    return "/app-http/carSeries/getCarSeriesById"

@postRequest
def talentMark_listTalentMarkPage():
    """获取达人标签分页数据"""
    return "/back-http/talentMark/listTalentMarkPage"

@postRequest
def auth_getDeptAdminRoleAuth():
    """获取部门admin角色权限"""
    return "/back-http/auth/getDeptAdminRoleAuth"

@postRequest
def department_findDepartmentRole():
    """获取部门角色"""
    return "/back-http/department/findDepartmentRole"

@postRequest
def packageselectNoPackageVideoPage():
    """获取非视频包视频列表"""
    return "/package/selectNoPackageVideoPage"

@getRequest
def music_listMusicTypes():
    """获取音乐分类列表"""
    return "/app-http/music/listMusicTypes"

@postRequest
def videoTopic_getAllEnabledRecommendTopics():
    """获得所有开启状态的推荐话题列表"""
    return "/back-http/videoTopic/getAllEnabledRecommendTopics"

@postRequest
def videoTopic_getAllEnabledHotTopics():
    """获得所有开启状态的热门话题"""
    return "/back-http/videoTopic/getAllEnabledHotTopics"

@postRequest
def videoTopic_getVideoTopicsForBack():
    """获得所有的视频话题-(翻页）"""
    return "/back-http/videoTopic/getVideoTopicsForBack"

@postRequest
def user_getUpToDateVersion():
    """获得最新的app版本信息"""
    return "/app-http/user/getUpToDateVersion"

@postRequest
def videoPlay_saveVideoShare():
    """视频分享"""
    return "/app-http/videoPlay/saveVideoShare"

@getRequest
def videofailPassVideoInitialCheck():
    """视频初审不通过接口"""
    return "/back-http/video/failPassVideoInitialCheck"

@postRequest
def videosuccessPassVideoInitialCheck():
    """视频初审通过接口"""
    return "/back-http/video/successPassVideoInitialCheck"

@getRequest
def videofailPassVideoSecondCheck():
    """视频复审不通过接口"""
    return "/video/failPassVideoSecondCheck"

@postRequest
def videosuccessPassVideoSecondCheck():
    """视频复审通过接口"""
    return "/video/successPassVideoSecondCheck"

@getRequest
def videoPlay_addVideoBrowse():
    """视频播放--视频浏览"""
    return "/app-http/videoPlay/addVideoBrowse"

@getRequest
def videoPlay_addThumbsUp():
    """视频播放--视频点赞"""
    return "/app-http/videoPlay/addThumbsUp"

@getRequest
def videoPlay_addCommentThumbsUp():
    """视频播放--评论点赞"""
    return "/app-http/videoPlay/addCommentThumbsUp"

@postRequest
def videoPlay_delComment():
    """视频播放-删除评论"""
    return "/app-http/videoPlay/delComment"

@getRequest
def webShare_getWebVideo():
    """视频播放-获取H5分享视频页"""
    return "/app-http/webShare/getWebVideo"

@getRequest
def videoPlay_getCommentList_reply():
    """视频播放-获取回复评论列表"""
    return "/app-http/videoPlay/getCommentList/reply"

@getRequest
def videoPlay_getCommentList():
    """视频播放-获取评论列表"""
    return "/app-http/videoPlay/getCommentList"

@postRequest
def videoPlay_comment():
    """视频播放-视频评论"""
    return "/app-http/videoPlay/comment"

@postRequest
def videoPlay_updateFavoritesStatus():
    """视频收藏/取消收藏"""
    return "/app-http/videoPlay/updateFavoritesStatus"

@getRequest
def videoservicedevmaster():
    """视频服务配置"""
    return "/video-service/dev/master"

@postRequest
def talkingskill_saveCommentTalkingToExcel():
    """解析excel批量添加评论话术"""
    return "/back-http/talkingskill/saveCommentTalkingToExcel"

@postRequest
def live_warn():
    """警告"""
    return "/back-http/live/warn"

@postRequest
def live_setManager():
    """设置成为管理员(禁言) / 取消管理员（禁言）"""
    return "/app-http/live/setManager"

@postRequest
def user_updateUserForMark():
    """设置用户为达人"""
    return "/back-http/user/updateUserForMark"

@postRequest
def user_scanQRCodeCard():
    """识别二维码名片"""
    return "/app-http/user/scanQRCodeCard"

@postRequest
def talkingskill_displayed():
    """话术是否启用"""
    return "/back-http/talkingskill/displayed"

@getRequest
def topic_getVideoTopics():
    """话题-全部话题列表"""
    return "/app-http/topic/getVideoTopics"

@getRequest
def topic_recommendTopics():
    """话题-热门话题推荐"""
    return "/app-http/topic/recommendTopics"

@getRequest
def topic_getTopicDetails():
    """话题-话题详情页"""
    return "/app-http/topic/getTopicDetails"

@postRequest
def carBrand_getCarBrandVideos():
    """车品牌热门视频列表"""
    return "/app-http/carBrand/getCarBrandVideos"

@getRequest
def video_getVehicleVideos():
    """车机视频列表"""
    return "/app-http/video/getVehicleVideos"

@postRequest
def vehicleVideo_saveVehicleVideoPackage():
    """车机视频包及其视频上传"""
    return "/app-http/vehicleVideo/saveVehicleVideoPackage"

@postRequest
def carSeries_getCarSeriesVideos():
    """车系热门视频列表"""
    return "/app-http/carSeries/getCarSeriesVideos"

@getRequest
def contentPushdelete():
    """通过ID删除内容推送消息"""
    return "/contentPush/delete"

@getRequest
def poPushdelete():
    """通过ID删除官方推送消息"""
    return "/poPush/delete"

@getRequest
def helperPushdelete():
    """通过ID删除小助手推送消息"""
    return "/helperPush/delete"

@postRequest
def videoCommentgetCommentById():
    """通过ID查找评论"""
    return "/videoComment/getCommentById"

@getRequest
def reportgetReportById():
    """通过ID查询举报信息"""
    return "/report/getReportById"

@getRequest
def videoChkselectVideoChkById():
    """通过id查找视频审核信息"""
    return "/videoChk/selectVideoChkById"

@getRequest
def videogetVideoTopicById():
    """通过topicId查找话题"""
    return "/video/getVideoTopicById"

@getRequest
def videogetVideoByVideoId():
    """通过videoId查找视频"""
    return "/video/getVideoByVideoId"

@getRequest
def videoselectLogByVideoId():
    """通过videoId查看操作日志"""
    return "/video/selectLogByVideoId"

@getRequest
def videoselectChkLogByVideoId():
    """通过videoId获取视频审核历史"""
    return "/video/selectChkLogByVideoId"

@postRequest
def vehicledestroyChatRoom():
    """销毁聊天室"""
    return "/vehicle/destroyChatRoom"

@postRequest
def music_sortMusicType():
    """音乐类型排序"""
    return "/back-http/music/sortMusicType"

@postRequest
def collection_save():
    """创建合集"""
    return "/app-http/v105/collection/save"

@postRequest
def collection_delete():
    """删除合集"""
    return "/app-http/v105/collection/delete"

@postRequest
def collection_updateCollectionToVideo():
    """app端修改合集中的视频"""
    return "/app-http/v105/collection/updateCollectionToVideo"

@postRequest
def collection_update():
    """app端修改合集(封面和名称)"""
    return "/app-http/v105/collection/update"

@postRequest
def collection_getUserCollection():
    """获取用户合集"""
    return "/app-http/v105/collection/getUserCollection"

@postRequest
def collection_getCollectionInfo():
    """获取合集内容"""
    return "/app-http/v105/collection/getCollectionInfo"

@postRequest
def collection_getCollectionVideo():
    """获取合集预选视频列表"""
    return "/app-http/v105/collection/getCollectionVideo"

@postRequest
def collection_getHomeCollection():
    """获取首页合集"""
    return "/app-http/v105/collection/getHomeCollection"

@getRequest
def effects_listSubjects():
    """获取主题列表"""
    return "/app-http/effects/listSubjects"

@postRequest
def audit_user_report():
    """审核平台：用户信息上报"""
    return "/audit-center/user/report"

@postRequest
def audit_room_report():
    """审核平台：酒局上报"""
    return "/audit-center/room/report"

@postRequest
def audit_live_report():
    """审核平台：酒局直播上报"""
    return "/audit-center/live/report"

@postRequest
def audit_appInfo_init():
    return "/audit-center/appInfo/init"

@postRequest
def videoCommentChk_check_wait():
    return "/back-http/videoCommentChk/check/wait"

@postRequest
def videoCommentChk_doCheck():
    return "/back-http/videoCommentChk/doCheck"