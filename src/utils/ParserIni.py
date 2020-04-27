#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
from config.path import dataPath

class parser_ini(object):
    """a为追加模式，w为覆盖模式，b为二进制模式"""
    __read = "r+"
    __write = "w+"

    #注意，所有英文必须为小写，否则读取失败

    #入参文件地址+文件名，默认写入自动格式
    def __init__(self,fileName):
        self.data = configparser.ConfigParser()
        self.fileName = fileName
        self.data.read(fileName)

    #状态：追加写入
    def changeWriteToA(self):
        self.__write = "a+"

    #状态：覆盖写入
    def changeWriteToW(self):
        self.__write = "w+"

    #状态：二进制追加写入
    def changeWriteToAB(self):
        self.__write = "ab+"

    #状态：二进制覆盖写入
    def changeWriteToWB(self):
        self.__write = "wb+"

    """写入数据，set写入模式"""
    def setParser(self,section,key,value):
        temp = 0

        #写入模式为二进制模式则禁止写入
        if self.__write == "ab+" or self.__write == "wb+":
            print("该文件操作不支持二进制文件写入")
            return False

        for i in key:
            temp = temp + 1

            if i.isupper() == True:
                print(i + "是大写字符，写入失败:" + key)
                break

            elif temp == len(key):
                #如果有重复sections则不添加sections
                if self.data.has_section(section) == False:
                    self.data.add_section(section)
                self.data.set(section,key,value)

                #尝试打开文件，完成写入操作
                try:
                    with open(self.fileName,self.__write,encoding="utf-8") as fp:
                        self.data.write(fp)
                        fp.flush()
                        fp.close()
                        return True

                #写入文件失败，关闭输出流
                except:
                    print("setParser（\""+ section +"\",\"" + key + "\",\"" + value + "\"）失败：" + self.fileName)
                    return False

    #手写模式(备注：如果能增加判断存在则修改的作用就很好了)
    # def setParser(self,sections,key,value):
    #
    #     #写入模式为二进制模式则禁止写入
    #     if self.write == "ab+" or self.write == "wb+":
    #         print("该文件操作不支持二进制文件写入")
    #
    #     else:
    #         #尝试打开文件，完成写入操作
    #         try:
    #             with open(self.fileName,self.write) as fp :
    #                 fp.write("[" + sections + "]" + "\n");
    #                 fp.write(key + " = " + value + "\n\n");
    #                 fp.flush();
    #                 fp.close();
    #         #写入文件失败，关闭输入流
    #         except:
    #             fp.close();
    #             print("写入文件失败：" + self.fileName)

    """删除节点"""
    def removeSection(self,section):
        #更改写入状态
        dump = self.__write
        self.changeWriteToW()

        #尝试执行删除操作，输出流
        self.data.remove_section(section)
        try:
            with open(self.fileName,self.__write,encoding="utf-8") as fp:
                self.data.write(fp)
                fp.flush()
                fp.close()
                return True

        #删除操作执行失败，输出流
        except:
            print("removeSection（\""+ section + "\"）删除节点失败：" + section)
            return False

        finally:
            #更改初始写入状态
            self.__write = dump


    """删除指定节点下对应的key，value"""
    def removeOption(self,section,key):
        if self.data.has_section(section) == True:
            #更改写入状态
            dump = self.__write
            self.changeWriteToW()

            #尝试执行删除操作，输出流
            self.data.remove_option(section,key)
            try:
                with open(self.fileName,self.__write,encoding="utf-8") as fp:
                    self.data.write(fp)
                    fp.flush()
                    fp.close()
                    return True

            #删除操作执行失败，输出流
            except:
                print("removeOption（\""+ section +"\",\"" + key + "\"）失败：" + section + "," + key)
                return False

            finally:
                #更改初始写入状态
                self.__write = dump
        else:
            print("removeOption（\""+ section +"\",\"" + key + "\"）失败，缺少指定节点：" + section)

    """清除除了defult数据以外其他所有的数据"""
    def clear(self):
        #更改写入状态
        dump = self.__write
        self.changeWriteToW()

        #尝试执行删除操作，输出流
        self.data.clear()
        try:
            with open(self.fileName,self.__write,encoding="utf-8") as fp:
                self.data.write(fp)
                fp.flush()
                fp.close()
                return True

        #删除操作执行失败，输出流
        except:
            print("clear（）失败")
            return False
        finally:
            #更改初始写入状态
            self.write = dump

    """根据section,key查询数据"""
    def getData(self,section,key):
        #循环，如果存在大写字符则读取失败，返回False
        for i in key:
            if i.isupper() == True:
                print(i + "是大写字符，读取失败:" + key)
                return False

        #循环，不存在section则报缺失异常
        for i in self.data.sections():
            if i == section:
                #循环，不存在key则报缺失异常
                for j in self.data.options(section):
                    if j == key:
                        return self.data.get(section,key)
                    elif j == len(self.data.options(section)):
                        print("selectData(\"" + section + "\",\"" + key + "\")失败，缺失key：" + key)
                        break
            elif i == len(self.data.sections()):
                print("selectData(\"" + section + "\",\"" + key + "\")失败，缺失section：" + section)
                break

    def getSections(self):
        return self.data.sections()

    def getOptions(self,section):
            return self.data.options(section)

if __name__ == '__main__':
    # a = parserMethod(p.dataPath() + "test.ini");
    # a.setParser("Eden","阿辉","帅")
    # a.setParser("a","阿辉","真帅")
    # a.setParser("b","阿辉","无敌帅")
    # a.setParser("Eden","帅","无敌帅")
    #
    # print(a.write)
    # b =a.data.sections()
    # print(b)
    # print(a.selectData("Eden","帅"))

    a = parser_ini(dataPath() + "url(已废除).ini")
    a.setParser("weather","weatherid","http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince")
    a.setParser("weather","woca","http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince")

    # print(a.write)
    # b =a.data.sections()
    # print(b)
    print(a.getData("weather","weatherid"))
    #print(a.data.get("Eden","阿辉"))