# coding:utf-8
from apiAutoUtil.config.gloVar import globalDataBase
from apiAutoUtil.src.utils.Log import log
import pymysql


class odbc(object):

    __instance = None
    __database = None

    # 单例设计模式，并且存在该数据库存在在ini配置文件中（得加锁）
    # def __new__(cls, *args, **kwargs):
    #     if not cls.__instance and not cls.__database:
    #         cls.__instance = super(odbc,cls).__new__(cls)
    #     return cls.__instance

    # 创建Mysql.ini对象
    def __init__(self,database=None):

        # 数据库环境
        mysqlConfig = globalDataBase()

        self.host = mysqlConfig.get("host")
        self.port = mysqlConfig.get("port")
        self.user = mysqlConfig.get("user")
        self.password = mysqlConfig.get("password")
        self.charset = mysqlConfig.get("charset")
        if database:
            self.__database = database

        self.log = log()

    # (弃用)判断ini配置文件中是否存在改数据库数据库
    # def __assertConnect(self):
    #     temp = 0
    #     # 循环查看配置文件database的key是否存在这个数据库
    #     for i in self.parser.options("database"):
    #         temp = temp + 1
    #         if self.__database == i:
    #             return True
    #         elif temp >= len(self.parser.options("database")):
    #             self.log.error("不存在对应的数据库,请确认配置文件中" + dataPath() + "dataBase.ini是否存在该数据库")
    #             return False

    # 尝试数据库连接
    def connectDB(self,db=None):
        if db:
            self.__database = db
        try:
            #连接数据库
            conn = pymysql.connect(
                host = self.host,
                port = int(self.port),
                user = self.user,
                password = self.password,
                database = self.__database,
                charset = self.charset
            )

            return conn
        except:
            self.log.error("连接数据库失败：" + self.__database)
            return False

    # 增删改SQL语句
    def commitSQL(self,sql,data=None):
        # 连接数据库，成功返回连接，失败返回false
        conn = self.connectDB()
        if conn == False:
            return False
        else:
            # 创建游标来执行对数据库的操作
            cursor = conn.cursor()

            # 尝试执行sql语句，成功则关闭连接返回True
            try:
                # 如果有数组
                if data and isinstance(data,list):
                    cursor.execute(sql,data)
                    conn.commit()
                    self.log.info("执行sql成功：" + str(sql) + str(data))
                else:
                    cursor.execute(sql,data)
                    conn.commit()
                    self.log.info("执行sql成功：" + str(sql))

                #如果成功到return的时候，会先执行finally关键字，关闭数据库连接
                return True
            except:
                conn.rollback()
                self.log.error(self.__database + "执行sql失败：" + str(sql))
                return False
            finally:
                # 关闭数据库连接
                cursor.close()
                conn.close()

    # 查询SQL
    def selectSQL(self,sql):
        # 连接数据库，成功返回连接，失败返回false
        conn = self.connectDB()
        if conn == False:
            return False
        else:
            # 创建游标来执行对数据库的操作
            cursor = conn.cursor()

            # 尝试执行sql语句，成功则关闭连接返回True
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                columnName = cursor.description

                # 列表生成式——获取这个查询sql的列名
                if len(columnName) == 1:
                    columnName = columnName[0][0]
                else:
                    columnName = [columnName[i][0] for i in range(len(columnName))]

                if len(result) == 1:
                    # if——如果只有一条数据，并且只有一个字段数据，则返回该数据，否则返回数组
                    # else——列表生成式，如果只有一条数据则返回一个数组
                    if len(result[0]) ==1:
                        result = result[0][0]
                    else:
                        result = [result[0][i] for i in range(len(result[0]))]

                self.log.info("执行sql成功：" + str(sql))

                #如果成功到return的时候，会先执行finally关键字，关闭数据库连接
                return columnName,result
            except:
                self.log.error(str(self.__database) + "执行sql失败：" + str(sql))
                return False
            finally:
                # 关闭数据库连接
                cursor.close()
                conn.close()

    def getDatabase(self,table):
        """根据表名找到数据库"""
        __,__database = self.selectSQL("SELECT table_schema FROM information_schema.TABLES WHERE table_name = '%s';"%table)
        return __database

    def getAllDatabase(self):
        """获取mysql所有的数据库"""
        __,__allDatabase = self.selectSQL("show databases")
        # 将所有表名装进一个list里面
        __allDatabase = [__allDatabase[i][0] for i in range(len(__allDatabase))]
        return __allDatabase

    def getAllTables(self):
        """获取这个数据库所有的表"""

        # 如果有连接到数据库里面才会查这个库下的所有表
        if self.__database:
            __,__allTables = self.selectSQL("show tables")
            __allTables = [__allTables[i][0] for i in range(len(__allTables))]
            return __allTables
        self.log.warning("数据库连接失败")
        self.log.warning("host = %s"%self.host)
        self.log.warning("port = %s"%self.port)
        self.log.warning("user = %s"%self.user)
        self.log.warning("password = %s"%self.password)
        self.log.warning("database = %s"%self.__database)
        self.log.warning("charset = %s"%self.charset)
        return False

if __name__ == '__main__':
    # __,database = globalDataBase()
    # print(database.get("host"))
    db = odbc("qiaoku_user")
    # database = db.getDatabase("tb_user_info")
    # print(database)
    # allDatabase = db.getAllDatabase()
    # print(allDatabase)
    allTables = db.getAllTables()
    print(allTables)
    # user = db.selectSQL("select * from tb_user_info where user_phone = 15361899636;")
    # print(user[0][4])
    db.connectDB("qiaoku_user")
    allTables = db.getAllTables()
    print(allTables)
    # __,user = db.selectSQL("select user_phone from tb_user_info where user_phone = 15361899636;")
    # print(user)