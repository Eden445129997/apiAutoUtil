# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class video_updateSystemVideo(unittest.TestCase):
    """修改后台上传的视频"""
    #初始化
    def setUp(self):
        # 初始化（清理数据库所有的表）
        # deleteData(self.userPhone)

        # token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg1OTg3NjksImV4cCI6MTU3MTE5MDc2OSwiYmFja191c2VyX2lkIjo2NjYsImlzcyI6InFpYW9rdV9iYWNrIn0.30i2L4PyCQ6kyF_aZ-8Ba2_4NxJAqmh7SL8p_1eiXPY"
    def test(self):
        pass

    def tearDown(self):
        # pass
        # 修改后台上传的视频
        self.a()
        # 缺少token
        # self.b()

    def a(self):
        """修改后台上传的视频"""
        data = {
            "videoId":"623187267145433088",
            # "videoTitle":"Eden",
            "videoUpDownStatus":1,
            # "videoRecommendStatus":1,
            # "photo":"http://video.didongkj.com/image/cover/84E92EC6261546568B10BC28A2BCC438-6-2.png",   #http://video.didongkj.com/image/cover/84E92EC6261546568B10BC28A2BCC438-6-2.png
            # "gif":"http://video.didongkj.com/image/cover/D3773B2EF92349059D1BE33B52797F7F-6-2.png",     #http://video.didongkj.com/image/cover/D3773B2EF92349059D1BE33B52797F7F-6-2.png
        }
        backHttp.updateSystemVideo(data,self.token)

    def b(self):
        """缺少token"""
        data = {
            "videoId":"623187267145433088",
            # "videoTitle":"EdenTest",
            # "videoUpDownStatus":2,
            # "videoRecommendStatus":2,
            # "photo":None,   #http://video.didongkj.com/image/cover/84E92EC6261546568B10BC28A2BCC438-6-2.png
            # "gif":None,     #http://video.didongkj.com/image/cover/D3773B2EF92349059D1BE33B52797F7F-6-2.png
        }
        backHttp.updateSystemVideo(data)


if __name__ == '__main__':
    unittest.main()

