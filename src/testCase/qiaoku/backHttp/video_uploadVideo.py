# coding=UTF-8
import unittest

from apiAutoUtil.src.testCase.qiaoku.Initialization import login
from apiAutoUtil.src.testCase.qiaoku.Initialization import deleteData
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import backHttp


class video_uploadVideo(unittest.TestCase):
    """后台上传视频"""
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
        # 后台上传视频
        self.a()
        # 缺少token
        # self.b()

    def a(self):
        """后台上传视频"""
        data = {
            "videoTitle":"EdenTest",
            "userId":"621775455304810496",
            "videoCategoryId":"18",
            "videoLabels":[{
                "labelId":"18",
                "labelName":"地动热门/推荐",
            }],
            "videoTopicId":"18",
            "videoUpDownStatus":3,
            "videoRecommendStatus":1,
            "videoUrl":"http://video.didongkj.com/sv/4b17e77d-16d14f7e703/4b17e77d-16d14f7e703.mp4",
            "photo":"http://video.didongkj.com/image/cover/84E92EC6261546568B10BC28A2BCC438-6-2.png",
            "gif":"http://video.didongkj.com/image/cover/D3773B2EF92349059D1BE33B52797F7F-6-2.png",
            "province":"浙江",
            "city":"杭州",
            "region":"滨江",
            "addressName":"天恒大厦",
            # "longitude":"http://video.didongkj.com/image/cover/D3773B2EF92349059D1BE33B52797F7F-6-2.png",
            # "latitude":"http://video.didongkj.com/image/cover/D3773B2EF92349059D1BE33B52797F7F-6-2.png",
        }
        backHttp.uploadVideo(data,self.token)

    def b(self):
        """缺少token"""
        data = {
            "videoTitle":"EdenTest",
            "userId":"621775455304810496",
            "videoCategoryId":"18",
            "videoLabels":[{
                "labelId":"18",
                "labelName":"地动热门/推荐",
            }],
            "videoTopicId":"18",
            "videoUpDownStatus":3,
            "videoRecommendStatus":1,
            "videoUrl":"http://video.didongkj.com/sv/4b17e77d-16d14f7e703/4b17e77d-16d14f7e703.mp4",
            "photo":"http://video.didongkj.com/image/cover/84E92EC6261546568B10BC28A2BCC438-6-2.png",
            "gif":"http://video.didongkj.com/image/cover/D3773B2EF92349059D1BE33B52797F7F-6-2.png",
            "province":"浙江",
            "city":"杭州",
            "region":"滨江",
            "addressName":"天恒大厦",
            "longitude":120.2077,
            "latitude":30.20334,
        }
        backHttp.uploadVideo(data)


if __name__ == '__main__':
    unittest.main()

