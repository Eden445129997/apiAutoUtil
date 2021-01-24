#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.utils.Decorator import getRequest
from src.utils.Decorator import postRequest

# po设计模式：pegeObject --> 页面对象
# 核心概念就是把一些资源封装成了一个对象来调用

@postRequest
def user_v1_user_send_smscode():
    """手机短信获取验证码登陆"""
    return "/api-user/v1/user/send/smscode"

@postRequest
def user_v1_user_login_phone():
    """手机短信验证码登陆"""
    return "/api-user/v1/user/login/phone"

@postRequest
def user_v1_sys_last_version():
    """版本号"""
    return "/api-user/v1/sys/last/version"

@postRequest
def user_v3_user_login_apple_third():
    """apple登录接口（新）"""
    return "/api-user/v3/user/login/apple/third"

@postRequest
def user_v3_user_login_apple():
    """apple苹果登录校验（新）"""
    return "/api-user/v3/user/login/apple"

@postRequest
def user_v4_moment_personalList():
    """个人主页-动态列表"""
    return "/api-user/v4/moment/personalList"

@postRequest
def user_v4_moment_report():
    """举报"""
    return "/api-user/v4/moment/report"

@postRequest
def party_v4_party_createBusiness():
    """创建企业房酒局"""
    return "/api-party/v4/party/createBusiness"

@postRequest
def party_v2_party_createWise():
    """创建达人聚会"""
    return "/api-party/v2/party/createWise"

@postRequest
def user_v4_moment_delete():
    """删除动态"""
    return "/api-user/v4/moment/delete"

@postRequest
def user_v4_moment_deleteComment():
    """删除评论"""
    return "/api-user/v4/moment/deleteComment"

@postRequest
def user_v4_user_setting_vod_refreshVideo():
    """刷新视频上传凭证"""
    return "/api-user/v4/user/setting/vod/refreshVideo"

@postRequest
def user_v4_moment_list():
    """动态列表"""
    return "/api-user/v4/moment/list"

@postRequest
def user_v4_moment_recommend_list():
    """动态动态推荐"""
    return "/api-user/v4/moment/recommend/list"

@getRequest
def invalid():
    """动态消息"""
    return "/invalid"

@postRequest
def user_v4_moment_detail():
    """动态详情"""
    return "/api-user/v4/moment/detail"

@postRequest
def user_v4_moment_publish():
    """发布动态"""
    return "/api-user/v4/moment/publish"

@postRequest
def user_v4_moment_cancelLike():
    """取消点赞"""
    return "/api-user/v4/moment/cancelLike"

@postRequest
def game_v4_henan_turntable_start():
    """开始游戏"""
    return "/api-game/v4/henan/turntable/start"

@postRequest
def game_v4_gold_start():
    """开始游戏"""
    return "/api-game/v4/gold/start"

@postRequest
def party_v2_party_list():
    """我的聚会"""
    return "/api-party/v2/party/list"

@postRequest
def party_v4_party_cancel_admin():
    """房主取消管理员"""
    return "/api-party/v4/party/cancel/admin"

@postRequest
def user_v4_moment_addComment():
    """新增评论"""
    return "/api-user/v4/moment/addComment"

@postRequest
def party_v4_shandong_game_selectRule():
    """查询酒局规则"""
    return "/api-party/v4/shandong/game/selectRule"

@postRequest
def party_v4_shandong_game_selec():
    """查询麦位 -座位跟用户信息"""
    return "/api-party/v4/shandong/game/selec"

@postRequest
def user_v4_moment_checkStatus():
    """校验动态是否被删除或被屏蔽"""
    return "/api-user/v4/moment/checkStatus"

@postRequest
def user_v4_user_setting_register():
    """注册"""
    return "/api-user/v4/user/setting/register"

@postRequest
def party_v4_shandong_game_updateRule():
    """添加酒局规则"""
    return "/api-party/v4/shandong/game/updateRule"

@postRequest
def party_v4_shandong_game_exchangeUpdate():
    """游戏座位换位 两个用户之间"""
    return "/api-party/v4/shandong/game/exchangeUpdate"

@postRequest
def party_v4_shandong_game_update():
    """游戏座位更新-单个用户"""
    return "/api-party/v4/shandong/game/update"

@postRequest
def user_v4_moment_like():
    """点赞"""
    return "/api-user/v4/moment/like"

@postRequest
def game_v4_gold_play():
    """玩游戏（点击卡片、跳过）"""
    return "/api-game/v4/gold/play"

@postRequest
def party_v4_shandong_game_check():
    """用户是否正在游戏中"""
    return "/api-party/v4/shandong/game/check"

@postRequest
def party_v4_shandong_game_userUpdate():
    """用户进入游戏，退出游戏的初始化。"""
    return "/api-party/v4/shandong/game/userUpdate"

@postRequest
def party_v4_shandong_game_deleteUser():
    """用户退出游戏"""
    return "/api-party/v4/shandong/game/deleteUser"

@postRequest
def party_v4_shandong_game_delete():
    """结束游戏"""
    return "/api-party/v4/shandong/game/delete"

@postRequest
def game_v4_card_stop():
    """结束游戏"""
    return "/api-game/v4/card/stop"

@postRequest
def game_v4_gold_end():
    """结束游戏"""
    return "/api-game/v4/gold/end"

@postRequest
def game_v4_card_nextPosition():
    """获取下一个麦位"""
    return "/api-game/v4/card/nextPosition"

@postRequest
def game_v4_card_randomList():
    """获取卡牌"""
    return "/api-game/v4/card/randomList"

@postRequest
def user_v4_user_setting_userType():
    """获取用户类型（新）"""
    return "/api-user/v4/user/setting/userType"

@postRequest
def user_v4_user_setting_vod_loadVideo():
    """获取视频上传地址和凭证"""
    return "/api-user/v4/user/setting/vod/loadVideo"

@postRequest
def user_v4_user_setting_vod_watermark():
    """视频-水印图添加"""
    return "/api-user/v4/user/setting/vod/watermark"

@postRequest
def game_v4_henan_turntable_setSkip():
    """设置是否跳过动动效"""
    return "/api-game/v4/henan/turntable/setSkip"

@postRequest
def user_v4_moment_commentList():
    """评论列表"""
    return "/api-user/v4/moment/commentList"

@postRequest
def party_v4_party_kickout_user():
    """踢出用户"""
    return "/api-party/v4/party/kickout/user"

@postRequest
def user_v3_user_wise():
    """达人列表 --查看更多"""
    return "/api-user/v3/user/wise"

@postRequest
def game_v4_henan_turntable_stop():
    """退出游戏"""
    return "/api-game/v4/henan/turntable/stop"

@postRequest
def game_v4_card_chooseCard():
    """选择卡牌"""
    return "/api-game/v4/card/chooseCard"

@postRequest
def party_v4_shandong_game_insert():
    """邀请宾客入座"""
    return "/api-party/v4/shandong/game/insert"

@postRequest
def party_v4_shandong_game_insertBath():
    """邀请宾客入座 批量"""
    return "/api-party/v4/shandong/game/insertBath"

@postRequest
def user_v2_party_list():
    """首页列表"""
    return "/api-user/v2/party/list"

@postRequest
def party_v1_party_create_init():
    return '/api-party/v1/party/create/init'

@postRequest
def party_v6_party_createWiseParty():
    return '/api-party/v6/party/createWiseParty'

@postRequest
def party_v2_party_join_id():
    return '/api-party/v2/party/join/id'

@postRequest
def party_v2_party_start():
    return '/api-party/v2/party/start'

@getRequest
def party_v7_party_page_preCreate():
    '''快速加入'''
    return '/api-party/v7/party/page/preCreate'

@getRequest
def party_v7_party_partyPage_list():
    '''派对列表页'''
    return '/api-party/v7/party/partyPage/list'