import unittest
import requests
import json
from apiAutoUtil.config.path import dirPath
from apiAutoUtil.src.utils.ParserMethod import parserMethod

class getBanner(unittest.TestCase):
    def setUp(self):
        global url
        #对象初始化
        inputStream = parserMethod(dirPath.dataPath() + "url.ini")
        #url拼接
        ip = inputStream.selectData("ip","test")
        port = inputStream.selectData("port","8771")
        addr = inputStream.selectData("life","get_banner")
        url = ip + port + addr
        print("url：" + url)

    def testGetBanner(self):
        response = requests.post(url=url)
        result = json.loads(response.text)
        code = result.get("code")
        data = result.get("data")
        id1 = data[0].get("bannerUrl")
        id2 = data[1].get("bannerUrl")
        id3 = data[2].get("bannerUrl")
        self.assertEqual(code,200,"接口访问失败")
        self.assertEqual(id1,"http://ddiddo.com/image/default/FD8BACD6C92A41FAB1C0F3EAD3D1293F-6-2.png","接口访问失败")
        self.assertEqual(id2,"http://ddiddo.com/image/default/2E02EC0A37EC4EBE82886FA692C8A468-6-2.png","接口访问失败")
        self.assertEqual(id3,"http://ddiddo.com/image/default/95131DD1C480472289DBDEC46D393D4C-6-2.png","接口访问失败")
        print(result)

if __name__ == '__main__':
    unittest.main()
