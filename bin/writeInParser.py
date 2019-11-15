from apiAutoUtil.src.utils.ParserMethod import parserMethod
from apiAutoUtil.config.path import dataPath
from apiAutoUtil.src.utils.ODBC import odbc

if __name__ == '__main__':
    outStream = parserMethod(dataPath() + "dataBase.ini");
    db = odbc("qiaoku_home")

    # 循环批量写入数据库
    for i in db.selectSQL("show tables"):
        db.commitSQL("truncate table %s;"%i)
        # outStream.setParser("userTable",i[0],i[0])

    # 数据库
    # outStream.setParser("production","ip","10.113.248.200")
    # outStream.setParser("production","port","3306")
    # outStream.setParser("production","user","root")
    # outStream.setParser("production","password","didong1904")
    # outStream.setParser("production","charset","utf8")
    # outStream.setParser("database","qiaoku_data","qiaoku_data")
    # outStream.setParser("database","qiaoku_home","qiaoku_home")
    # outStream.setParser("database","qiaoku_live","qiaoku_live")
    # outStream.setParser("database","qiaoku_user","qiaoku_user")
    # outStream.setParser("database","qiaoku_video","qiaoku_video")

    # url
    # outStream = parserMethod(dirPath.dataPath() + "url.ini");
    # outStream.setParser("weather","weatherid","http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince")
