import unittest
from apiAutoUtil.config.path import dataPath
from apiAutoUtil.src.utils.ParserIni import parserMethod
from apiAutoUtil.src.utils.GetRequest import noneParams


class tryTest(unittest.TestCase):
    """用例ID，用例名称"""
    #测试数据准备
    def setUp(self):
        global data,request
        #创建输入流对象
        inputStream = parserMethod(dataPath() + "url(已废除).ini")
        #获取数据
        data = inputStream.getData("weather","weatherid")

    """执行测试用例阶段"""
    def testWeather(self):
        print(noneParams(data))

    """执行用例后需要执行的操作"""
    def tearDown(self):
        print("执行完该测试用例了")

if __name__ == '__main__':
    unittest.main()