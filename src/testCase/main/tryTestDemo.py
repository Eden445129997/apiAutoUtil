# import unittest
#
# class tryTest(unittest.TestCase):
#     """用例ID，用例名称"""
#     #测试数据准备
#     def setUp(self):
#         global data
#         data = {
#             "aaa":1
#         }
#     print("开始")
#
#     """执行测试用例阶段"""
#     def testWeather(self):
#         # print(noneParams(data))
#         print(data)
#
#     def testheihei(self):
#         print(data)
#
#     """执行用例后需要执行的操作"""
#     def tearDown(self):
#         print("执行完该测试用例了")

if __name__ == '__main__':
    # unittest.main()
    headers = {}
    headers["device"] = "ios"
    headers["version"] = "1.2.9"

    # 发送短信验证码
    headers["device-product"] = "1"
    headers["device-model"] = "1"
    headers["device-os-ver"] = "1"

    print(str(headers).replace('\'','"'))