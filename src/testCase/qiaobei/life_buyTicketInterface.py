import unittest
import time
from apiAutoUtil.config.path import dirPath
from apiAutoUtil.src.utils.ParserMethod import parserMethod
from apiAutoUtil.src.utils.PostRequest import postMethod
from apiAutoUtil.src.utils.ODBC import jdbc
from ddt import ddt,data

Case1 = {
    # "userId" : "99999999",
    "shopId":"69201700",
    "ticketId":"999999999999999999"
}

Case2 = {
    "shopId" : "69201700"
}

Case3 = {
    "ticketId":"999999999999999999"
}

Case4 = {
    "ticketId":"000001",
    "merchantId" : "99999999"
}

Case5 = {
    "ticketId":"999999",
    "merchantId" : "00000001"
}

@ddt
class buyTicketInterface(unittest.TestCase):
    """自买省——buyTicketInterface"""
    #初始化
    def setUp(self):
        global url,request
        #创建请求对象
        request = postMethod()
        #创建输入流对象
        inputStream = parserMethod(dirPath.dataPath() + "url.ini")
        mysqlIni = parserMethod(dirPath.dataPath() + "Mysql.ini")
        #获取数据
        ip = inputStream.selectData("ip","test")
        port = inputStream.selectData("port","8771")
        addr = inputStream.selectData("life","buy_ticket_interface")
        url = ip + port + addr
        print("url：" + url)

        try:
            #连接数据库
            conn = jdbc(mysqlIni.selectData("database","db_life_center"))
            #尝试清理数据，如果没有对应的数据则直接insert
            id = conn.selectSQL("select id from db_life_center.tb_ticket where ticket_name = 'testdata'")
            conn.commitSQL("delete from tb_ticket where id = %s and ticket_name = 'testData'"%id[0][0])
            print("数据清理成功")
            time.sleep(2)
            conn.commitSQL("INSERT INTO `db_life_center`.`tb_ticket` (`ticket_id`, `ticket_name`, `shop_id`, `ticket_type`, `ticket_price`, `ticket_value`, `ticket_sold`, `maximum_buy`, `daily_ticket_sold`, `max_ticket_sold`, `total_count`, `low_pay`, `use_condition`, `buy_condition`, `deadline`, `use_explain`, `fee_rate`, `chk_status`, `del_flag`, `create_time`, `last_update_time`) VALUES ( '999999999999999999', 'testdata', '69201700', NULL, '5.00', '30.00', '175', NULL, NULL, NULL, '100', NULL, NULL, NULL, '5', NULL, NULL, '1', '0', now(), now());")
            time.sleep(0.5)
            print("初始化完成\n")
            print()
        except:
            time.sleep(0.5)
            print("初始化失败\n")
        print("")

    #用例1
    @data(Case1)
    def testMaster(self,data):
        print("Case1——正常调用")

        #将request类的返回Json序列化
        request.changResultJsonTo_true()

        print("入参：" + str(data))

        #发送请求获取返回结果
        result = request.sendJsonMethod(url,data)

        print(result)

        #断言
        code = result.get("code")
        self.assertEqual(code,200,msg="接口访问失败")
        #相应data中的Json
        dict = result.get("data")
        ticketId = dict.get("ticketId")
        self.assertEqual(ticketId,999999,msg="ticketId不一致")
        ticketName = dict.get("ticketName")
        self.assertEqual(ticketName,"testdata",msg="ticketName不一致")

    #用例2
    @data(Case2)
    def testNoneKeyTicketId(self,data):
        print("Case2——入参缺少ticketId访问失败")

        #将request类的返回Json序列化
        request.changResultJsonTo_true()

        print("入参：" + str(data))

        #发送请求获取返回结果
        result = request.sendJsonMethod(url,data)

        print(result)

        #断言
        status = result.get("status")
        self.assertEqual(status,500,msg="noneKeyTicketId和预期不符")

    #用例3
    @data(Case3)
    def testNoneKeyMerchantId(self,data):
        print("Case3——入参缺少merchantId访问失败")

        #将request类的返回Json序列化
        request.changResultJsonTo_true()

        print("入参：" + str(data))

        #发送请求获取返回结果
        result = request.sendJsonMethod(url,data)

        print(result)

        #断言
        status = result.get("status")
        self.assertEqual(status,500,msg="noneKeyMerchantId和预期不符")

    #用例4
    @data(Case4)
    def testNoneTicketId(self,data):
        print("Case4——不存在ticketId访问失败")

        #将request类的返回Json序列化
        request.changResultJsonTo_true()

        print("入参：" + str(data))

        #发送请求获取返回结果
        result = request.sendJsonMethod(url,data)

        print(result)

        #断言
        status = result.get("status")
        self.assertEqual(status,500,msg="noneTicketId和预期不符")

    #用例5
    @data(Case5)
    def testNoneMerchantId(self,data):
        print("Case5——不存在merchantId访问失败")

        #将request类的返回Json序列化
        request.changResultJsonTo_true()

        print("入参：" + str(data))

        #发送请求获取返回结果
        result = request.sendJsonMethod(url,data)

        print(result)

        #断言
        status = result.get("status")
        self.assertEqual(status,500,msg="noneMerchantId和预期不符")

    # """执行测试用例阶段"""
    # def testMain(self):
    #     self.master()
    #     self.noneKeyTicketId()
    #     self.noneKeyMerchantId()
    #     self.noneTicketId()
    #     self.noneMerchantId()

    """执行用例后需要执行的操作"""
    def tearDown(self):
        print("该测试用例所有节点都执行完毕")
        time.sleep(0.5)

if __name__ == '__main__':
    unittest.main()

