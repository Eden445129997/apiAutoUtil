#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.utils.ODBC import odbc
# from src.testCase.qiaoku import api_obj


def add_collection_data(user_id):
    """添加合集测试数据"""
    # user_id = 631815167985844224
    # 上架视频
    up_video = [627543992287887360,633314628415258624,634100823806181376]
    # 下架视频
    down_video = []
    # 删除的视频
    del_video = []
    # 合集所属平台 1:app  2:系统
    platform = 1
    # 合集视频数量
    video_count = len(up_video) + len(down_video) + len(del_video)
    # 合集地理位置省份（涉及合集推荐逻辑，取视频最后一级视频的地理位置，进行同省推荐）
    province = ""
    # 合集上下架状态  1:上架  2:下架
    up_down_status = 1
    # 合集推荐状态(是否推荐 1:推荐 2:不推荐)
    recommend_status = 1
    # 合集浏览数
    browse_count = 0
    # 机审状态 1:待审核 2:通过  3:不通过 4:疑似 5:审核异常
    machine_chk_status = 2
    # 人工审核状态 1.待审核 2：审核通过，3：审核不通过
    person_chk_status = 2
    # # 审核不通过原因
    # reason = ""

    video_db = odbc("qiaoku_video")

    # 插入合集表数据
    tb_video_collection_status = video_db.commitSQL(
            "INSERT INTO `qiaoku_video`.`tb_video_collection` " \
            "(`user_id`, `collection_name`, `collection_cover`, `video_count`, `province`, `platform`, `up_down_status`, `recommend_status`, `browse_count`, `create_time`, `last_update_time`) " \
            "VALUES ('%s', 'Eden合集脚本测试数据', 'https://didongpic.didongkj.com/1578369317466.png', '%s', '%s', '%s', '%s', '%s', '%s', '2020-03-06 14:52:00', '2020-03-11 18:01:52');"
            % (user_id, video_count, province, platform, up_down_status, recommend_status, browse_count))

    # 如果合集表有数据
    if tb_video_collection_status:
        collection_id = \
            video_db.selectSQL("select id from `qiaoku_video`.`tb_video_collection` where user_id = %s;" % user_id)[1]
        # print(collection_id)

        # 根据合集id循环写入“视频”到合集映射表
        if collection_id:
            # 视频排序video_sort
            video_sort = 0
            if up_video:
                for i in range(len(up_video)):
                    video_db.commitSQL("INSERT INTO `qiaoku_video`.`tb_video_collection_mapping` "
                                       "(`collection_id`, `video_id`, `video_sort`, `create_time`, `last_update_time`) "
                                       "VALUES ('%s', '%s', '%s', '2020-03-06 14:52:53', '2020-03-11 15:03:43');"
                                       % (collection_id, up_video[i], video_sort)
                                       )
                    video_sort += 1

            if down_video:
                for i in range(len(down_video)):
                    video_db.commitSQL("INSERT INTO `qiaoku_video`.`tb_video_collection_mapping` "
                                       "(`collection_id`, `video_id`, `video_sort`, `create_time`, `last_update_time`) "
                                       "VALUES ('%s', '%s', '%s', '2020-03-06 14:52:53', '2020-03-11 15:03:43');"
                                       % (collection_id, down_video[i], video_sort)
                                       )
                    video_sort += 1

            if del_video:
                for i in range(len(del_video)):
                    video_db.commitSQL("INSERT INTO `qiaoku_video`.`tb_video_collection_mapping` "
                                       "(`collection_id`, `video_id`, `video_sort`, `create_time`, `last_update_time`) "
                                       "VALUES ('%s', '%s', '%s', '2020-03-06 14:52:53', '2020-03-11 15:03:43');"
                                       % (collection_id, del_video[i], video_sort)
                                       )
                    video_sort += 1

        # 写审核表数据
        video_db.commitSQL("INSERT INTO `qiaoku_video`.`tb_video_collection_chk` "
                           "( `collection_id`, `collection_name`, `collection_cover`, `machine_chk_status`, `person_chk_status`, `reason`, `operator_id`, `operate_time`, `create_time`, `last_update_time`) "
                           "VALUES ( '%s', '测试合集名称', '测试合集封面', '%s', '%s', NULL, NULL, NULL, '2020-03-16 14:34:55', '2020-03-16 14:34:55');"%(collection_id,machine_chk_status,person_chk_status)
                           )

    # print("数据写入完成")
    return True


def del_collection_data(collection_id):
    """清理合集测试数据"""
    # user_id = 631815167985844224

    video_db = odbc("qiaoku_video")
    collection_id = \
        video_db.selectSQL("select id from `qiaoku_video`.`tb_video_collection` where id = %s;" % collection_id)[1]
    # print(collection_id)
    if collection_id:
        # 清理所有数据成功则返回True，有一个失败则False
        if video_db.commitSQL(
                        "delete from `qiaoku_video`.`tb_video_collection_mapping` where collection_id = %s;" % collection_id) and video_db.commitSQL(
                        "delete from `qiaoku_video`.`tb_video_collection_chk` where collection_id = %s;" % collection_id) and video_db.commitSQL(
                        "delete from `qiaoku_video`.`tb_video_collection` where id = %s;" % collection_id):
            return True
        return False
    else:
        return False

def insert_data(num):
    video_db = odbc("qiaoku_video")
    for i in range(num):
        video_db.commitSQL("INSERT INTO `qiaoku_video`.`tb_paster` (`paster_name`, `cover_photo`, `paster_version`, `paster_url`, `paster_file_name`, `use_count`, `use_status`, `del_flag`, `create_time`, `last_update_time`) VALUES ('救护车', 'http://didongpic.didongkj.com/1585648905615.png', '1', 'http://didongpic.didongkj.com/56A1D1CB-1CCA-40ED-B978-0ABA66021231.animatedsticker', '56A1D1CB-1CCA-40ED-B978-0ABA66021231.animatedsticker', '0', '1', '0', '2020-03-31 17:32:19', '2020-03-31 18:01:58');")
    print(True)
if __name__ == '__main__':
    # 写入合集数据
    # add_collection_data(627449976342970368)
    # del_collection_data(627449976342970368)

    # 删除合集数据
    # del_collection_data(63)
    # collection_check_to_not_check(45)

    # 贴纸数据写入
    insert_data(200)
    pass
