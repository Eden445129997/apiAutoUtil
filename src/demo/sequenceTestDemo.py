import unittest
import time

# from apiServers.config.Path import dirPath
# from apiServers.src.utils.parserMethod import parserMethod
# from apiAutoUtil.src.utils import GetRequest

class sequenceTest(unittest.TestCase):
    """用例ID，用例名称"""
    #测试数据准备
    def setUp(self):
        print("初始化")

    """执行用例后需要执行的操作"""
    def tearDown(self):
        print("执行完该测试用例了")
        time.sleep(1)

    def a(self):
        print("我是a节点")

    def b(self):
        print("我是b节点")

    def c(self):
        print("我是c节点")

    """执行测试用例阶段"""
    def testSequence(self):
        self.a()
        self.b()
        self.c()



if __name__ == '__main__':
    unittest.main()