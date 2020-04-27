#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.testCase.qiaoku import api_obj

class collection(unittest.TestCase):
    """获取用户消息列表"""

    # 初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODQ1OTc4NzcsInVzZXJJZCI6NjI3NDcyNDgxMjI5MjA5NjAwLCJ1c2VyUGxhdGZvcm0iOiJhcHAiLCJ1ZGlkIjoibG9naW4iLCJpc3MiOiJxaWFva3UifQ.Bw1ytO1nOZ3hPxuY3ZHR62qUvanTDJwJhUFNv49zld0"

    def tearDown(self):
        pass

    def test(self):
        # 获取用户消息列表
        self.save1()
        # self.save2()
        # self.save3()
        # self.delete1()
        # self.delete2()
        # self.updateCollectionToVideo()
        # self.collectionUpdate()
        # self.getUserCollection()
        # self.getCollectionInfo()
        # self.getCollectionVideo()
        # self.getHomeCollection()

    def save1(self):
        """app端创建合集"""
        data = {
            "videoIdList": [],
            "collectionName": "Eden接口创建合集",
            "collectionCover": "https://didongpic.didongkj.com/1578369317466.png",
        }
        api_obj.collection_save(data, self.token)

    def save2(self):
        """app端创建合集
        标题名称20限制
        数组地址，最后为null取上一个
        自己的视频数据
        """
        data = {
            "videoIdList": [627544576952893440,633315390545461248,634101487953248256,643389499677605888,647473852217032704,647742440446361600,648484872637120512,648607727123169280],
            "collectionName": "Eden接口创建合集Eden接口创建合集",
            "collectionCover": "https://didongpic.didongkj.com/1578369317466.png",
        }
        api_obj.collection_save(data, self.token)

    def save3(self):
        """app端创建合集
        返例：绑定别人的videoId（不符合业务数据）"""
        data = {
            "videoIdList": [627544576952893440,633315390545461248,634101487953248256,643389499677605888,647473852217032704,647742440446361600,648484872637120512,648607727123169280,627543992287887360],
            "collectionName": "Eden接口创建合集Eden接口创建合集",
            "collectionCover": "https://didongpic.didongkj.com/1578369317466.png",
        }
        api_obj.collection_save(data, self.token)

    def delete1(self):
        """删除自己的合集"""
        data = {
            "collectionId": 29,
        }
        api_obj.collection_delete(data, self.token)

    def delete2(self):
        """删除别人的合集"""
        data = {
            "collectionId": 12,
        }
        api_obj.collection_delete(data, self.token)

    def updateCollectionToVideo(self):
        """app端修改合集中的视频"""
        data = {
            "videoIdList": [627544576952893440],
            "collectionId": 19,
        }
        api_obj.collection_updateCollectionToVideo(data, self.token)

    def collectionUpdate(self):
        """app端修改合集(封面和名称)"""
        data = {
            "collectionId": 12,
            "collectionName": "测试合集名称",
            "collectionCover":"测试合集封面",
        }
        api_obj.collection_update(data, self.token)

    def getUserCollection(self):
        """获取用户合集"""
        data = {
            # "userId": 627449976342970368,627472481229209600
            # "otherUserId": 627449976342970368,
            "pageIndex": 1,
            "pageSize": 10
        }
        api_obj.collection_getUserCollection(data, self.token)

    def getCollectionInfo(self):
        """获取合集内容"""
        data = {
            "collectionId": 53,
            "pageIndex": 1,
            "pageSize": 10
        }
        response = api_obj.collection_getCollectionInfo(data, self.token)
        # videoInfo = response.get("data").get("collectionVideoDTOList")

        # for i in range(len(videoInfo)):
        #     print(videoInfo[i])

    def getCollectionVideo(self):
        """获取合集预选视频列表"""
        data = {
            "pageIndex": 1,
            "pageSize": 100
        }
        response = api_obj.collection_getCollectionVideo(data, self.token)
        videoInfo = response.get("data")
        print(len(videoInfo))
        for i in range(len(videoInfo)):
            print(videoInfo[i])

    def getHomeCollection(self):
        """获取用户合集"""
        data = {
            "province": "浙江",
            "pageIndex": 1,
            "pageSize": 10
        }
        api_obj.collection_getHomeCollection(data, self.token)

if __name__ == '__main__':
    unittest.main()
