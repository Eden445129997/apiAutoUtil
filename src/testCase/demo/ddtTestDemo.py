import unittest
import time
import json
from ddt import ddt,data,unpack
from apiAutoUtil.src.utils import PostRequest
from apiAutoUtil.src.testCase.qiaoku.interfaceObject import appHttp

url = "http://10.113.248.204:8771/back-http/music/getRecommendMusic"

#第一个测试用例入参
dataList = [{
    "longitude":"120.2111",
    "latitude":"30.2120"
},{
    "longitude":"11.1111",
    "latitude":"22.2120"
}]

@ddt
class ddtTest(unittest.TestCase):
    def setUp(self):
        pass
        # global request,url
        #获取url
        # inputStream = parserMethod(dataPath() + "url.ini")
        # url = inputStream.selectData("life","buy_ticket_interface")

    def tearDown(self):
        pass

    @data(*dataList)
    def test_main(self,data):
        self.ddt_a(data)
        self.ddt_b(data)

    def ddt_a(self,data):
        response = appHttp

    def ddt_b(self,data):
        response = PostRequest.applicationJson(url=url,data=data)

if __name__ == '__main__':
    unittest.main()

