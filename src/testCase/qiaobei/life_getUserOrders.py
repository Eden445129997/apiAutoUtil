import unittest
import time
from apiAutoUtil.config.path import dirPath
from apiAutoUtil.src.utils.ParserMethod import parserMethod
from apiAutoUtil.src.utils.PostRequest import postMethod

class getUserOrders(unittest.TestCase):
    """获取用户订单信息"""
    #测试数据准备
    def setUp(self):
        global url,request
        #创建dir对象和输入流对象
        directory = dirPath()
        inputStream = parserMethod(directory.dataPath() + "url.ini")
        #获取数据
        url = inputStream.selectData("life","get_user_orders")
        #创建请求对象
        request = postMethod()

    """执行测试用例阶段"""
    def master(self):
        #将request类的返回Json序列化
        request.changResultJsonTo_true()

        data = {
            "orderStatus" : "1",
            "userId":"12315646"
        }

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