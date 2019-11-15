import unittest
import time
from apiAutoUtil.config.path import dirPath
from apiAutoUtil.src.utils.ParserMethod import parserMethod
from apiAutoUtil.src.utils.PostRequest import postMethod
from ddt import ddt,data


#微信支付
case1 = {
    "payType" : "wx",
    "orderId":"599549626072170496"
}
#支付宝支付
case2 = {
    "payType" : "zfb",
    "orderId":"599549626072170496"
}

@ddt
class pay(unittest.TestCase):
    """订单支付"""
    #测试数据准备
    def setUp(self):
        global request,url
        #对象初始化
        request = postMethod()
        directory = dirPath()
        inputStream = parserMethod(directory.dataPath() + "url.ini")
        #url拼接
        ip = inputStream.selectData("ip","test")
        addr = inputStream.selectData("life","pay")
        url = ip + addr
        print("url：" + url)

    #微信支付
    @data(case1)
    def testWxPay(self,data):
        #将request类的返回Json序列化
        request.changResultJsonTo_true()

        #发送请求获取返回结果
        result = request.sendJsonMethod(url,data)

        #断言
        # code = result.get("code")
        # message = result.get("message")
        # self.assertEqual(code,200,msg="接口访问失败")
        # self.assertEqual(message,"商户信息查询成功",msg="接口访问失败")
        print(result)

    #支付宝支付
    @data(case2)
    def testZfbPay(self,data):
        #将request类的返回Json序列化
        request.changResultJsonTo_true()

        #发送请求获取返回结果
        result = request.sendJsonMethod(url,data)

        #断言
        # code = result.get("code")
        # message = result.get("message")
        # self.assertEqual(code,200,msg="接口访问失败")
        # self.assertEqual(message,"商户信息查询成功",msg="接口访问失败")
        print(result)

    """执行用例后需要执行的操作"""
    def tearDown(self):
        print("执行完该测试用例了")
        time.sleep(0.5)

if __name__ == '__main__':
    unittest.main()
