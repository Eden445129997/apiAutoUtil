import unittest
import time
from apiAutoUtil.config.path import dirPath
from apiAutoUtil.src.utils.ParserMethod import parserMethod
from apiAutoUtil.src.utils.PostRequest import postMethod
from ddt import ddt,data
from apiAutoUtil.src.utils.ODBC import jdbc

case1 = {
    "shopId":"69201700"
}

@ddt
class getShopDetails(unittest.TestCase):
    """点击商户,获取商家详情"""
    #测试数据准备
    def setUp(self):
        global url,request,db_shopId
        #创建对象
        request = postMethod()
        mysqlIni = parserMethod(dirPath.dataPath() + "Mysql.ini")
        inputStream = parserMethod(dirPath.dataPath() + "url.ini")
        #url拼接
        ip = inputStream.selectData("ip","test")
        port = inputStream.selectData("port","8771")
        addr = inputStream.selectData("life","get_shop_details")
        url = ip + port + addr
        print("url：" + url)

        # #数据库表还要改
        try:
            #连接数据库
            conn = jdbc(mysqlIni.selectData("database","db_life_center"))
            db_shopId = conn.selectSQL("select shop_id from db_life_center.tb_shop where shop_id = '69201700'")
            #尝试清理数据，如果没有对应的数据则直接insert
            # id = conn.selectSQL("select id from db_life_center.tb_shop where shop_id = '69201700'")
            # conn.commitSQL("delete from tb_shop where id = %s;"%id[0][0])
            # print("数据清理成功")
            # time.sleep(2)
            # conn.commitSQL("INSERT INTO `db_life_center`.`tb_shop` ( `shop_id`, `shop_user_id`, `invation_code`, `maker_id`, `shop_name`, `longitude`, `latitude`, `trading_area_id`, `trading_area_name`, `address`, `phone`, `shop_image`, `average_rating`, `average_price`, `identify_status`, `identify_time`, `open_status`, `open_time`, `end_time`, `type_id`, `label_names`, `city`, `area`, `recommend`, `qr_code`, `ticket_sell_num`, `comment_num`, `source`, `create_time`, `last_update_time`) VALUES ( '69201700', NULL, NULL, NULL, '唱将录音棚(西湖文化广场店)', '120.215131', '30.219284', NULL, NULL, '下城区中山北路607号现代城建大厦306室（西湖文化广场）', '18658192588/13675875281', 'http://ddiddo.com/image/default/71BC0AAC579E484F91C64A2A8221D21B-6-2.png', '4.0', '50', '1', NULL, '1', '7', '22', '1', '1', NULL, '西湖文化广场', '1', 'http://ddiddo.com/image/default/D22D6DB35262467C9A93CF6ACFE859D8-6-2.png', NULL, '230', NULL, '2019-07-08 10:55:08', '2019-07-20 13:51:34');")
            # conn.commitSQL("INSERT INTO `db_life_center`.`tb_shop` ( `shop_id`, `shop_user_id`, `invation_code`, `maker_id`, `shop_name`, `longitude`, `latitude`, `trading_area_id`, `trading_area_name`, `address`, `phone`, `shop_image`, `average_rating`, `average_price`, `identify_status`, `identify_time`, `open_status`, `open_time`, `end_time`, `type_id`, `label_names`, `city`, `area`, `recommend`, `qr_code`, `ticket_sell_num`, `comment_num`, `source`, `create_time`, `last_update_time`) VALUES ( '69201700', NULL, NULL, NULL, '唱将录音棚(西湖文化广场店)', '120.215131', '30.219284', NULL, NULL, '下城区中山北路607号现代城建大厦306室（西湖文化广场）', '18658192588/13675875281', 'http://ddiddo.com/image/default/71BC0AAC579E484F91C64A2A8221D21B-6-2.png', '4.0', '50', '1', NULL, '1', '7', '22', '1', '1', NULL, '西湖文化广场', '1', 'http://ddiddo.com/image/default/D22D6DB35262467C9A93CF6ACFE859D8-6-2.png', NULL, '230', NULL, '2019-07-08 10:55:08', '2019-07-20 13:51:34');")
            # time.sleep(0.5)
            print("初始化完成\n")

        except:
            time.sleep(0.5)
            print("初始化失败\n")

    """执行测试用例阶段"""
    @data(case1)
    def testGetShopDetails(self,data):
        #将request类的返回Json序列化
        request.changResultJsonTo_true()

        #发送请求获取返回结果
        result = request.sendJsonMethod(url,data)

        #断言
        code = result.get("code")
        data = result.get("data")
        reqShopDTO = data.get("reqShopDTO")
        shopId = reqShopDTO.get("shopId")
        self.assertEqual(code,200,msg="接口访问失败")
        self.assertEqual(shopId,str(db_shopId[0][0]),msg="接口访问失败")
        print(result)

    """执行用例后需要执行的操作"""
    def tearDown(self):
        print("执行完该测试用例了")
        time.sleep(0.5)

if __name__ == '__main__':
    unittest.main()