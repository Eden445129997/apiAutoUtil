#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from src.utils.Log import log

class deleteMethod(object):
    """
    # 当resultJson
    # True则格式化成Json格式返回
    # False则返回text格式
    """
    __instance = None
    __resultJson = True

    # 单例设计模式
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(deleteMethod,cls).__new__(cls)
        return cls.__instance

    # 初始化
    def __init__(self):
        self.codingFormat = "UTF-8"
        self.log = log()

    #更改返回编码格式
    def changeCodingFormat(self,codingFormat):
        self.codingFormat = codingFormat

    #修改返回结果状态（解析成Json格式）
    def changResultJsonTo_true(self):
        self.__resultJson = True

    #修改返回结果状态（解析成text格式化）
    def changResultJsonTo_false(self):
        self.__resultJson = False

    # 将url地址和字典参数合并
    def merge(self,url,dict):
        url = url + "?"
        for i in dict.keys():
            url = url + "&" + i + "=" + str(dict[i])
        return url

    # 获取get请求，并将参数转换成字典
    def splitUrl(self,url):
        params = ""
        dict = {}

        # 拆分url参数，从？开始拆分
        for i in range(len(url)):
            if url[i] == "?":
                params = url[i+1:]
                break

        # 分割&，组装成list
        list = params.split("&")

        # 删除分割之后的空字符串，但发现下一个for循环的代码不会生成空字符串为Key的字典
        # for i in range(len(list))[::-1]:
        #     if list[i] == "":
        #         list.pop(i)

        # 将list里面的键值对转换成字典
        for i in range(len(list)):
            for j in range(len(list[i])):
                if list[i][j] == "=":
                    dict[list[i][:j]] = list[i][j+1:]
        return dict

    #无参get请求
    def sendNoneParams(self,url):

        try:
            #请求url，不校验证书，超时10s（不写默认120s）
            response = requests.delete(url=url,verify=False,timeout=10)
            response.encoding = self.codingFormat

            #解析成Json格式返回
            if self.__resultJson == True:
                result = json.loads(response.text)
                self.log.info("接口访问成功，url：" + url)
                self.log.info("响应参数：" + str(result))

                return result
            # Text格式返回
            elif self.__resultJson == False:
                result = response.text
                self.log.info(r"接口访问成功，url：" + url)
                self.log.info(r"响应参数：" + result)
                return result

        except:
            # now = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())
            self.log.error(r"get请求失败：" + url)
            self.log.info(r"请求入参：" + str(self.splitUrl(url)))

    #有参get请求,params入参为字典类型
    def sendHadParams(self,url,dict):
        url = self.merge(url,dict)

        try:
            #请求url，不校验证书，超时10s（不写默认120s）
            response = requests.delete(url=url,verify=False,timeout=10)
            response.encoding = self.codingFormat

            #解析成Json格式返回
            if self.__resultJson == True:
                result = json.loads(response.text)
                self.log.info(r"接口访问成功，url：" + url)
                self.log.info(r"响应参数：" + str(result))

                return result
            # Text格式返回
            elif self.__resultJson == False:
                result = response.text
                self.log.info(r"接口访问成功，url：" + url)
                self.log.info(r"响应参数：" + result)
                return result

        except:
            # now = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())
            self.log.error(r"get请求失败：" + url)
            self.log.info(r"请求入参：" + str(dict))

# 测试主方法
if __name__ == '__main__':
    #天气接口_获取城市对应的id
    #url = r"http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince"
    #url = r"http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString"
    # url = r"http://47.105.175.129:8771/user-http/login/getSmsCode?&userPhone=15361899636&udid=abcdefg"
    url = r"http://10.113.248.59:8771/back-http/backuser/deleteDepartment?&departmentId=2"

    deleteRequest  = deleteMethod()
    # data = {
    #     "userPhone":"15361899636",
    #     "udid":"abcdefg",
    # }
    # print(a.splitUrl(url))

    for i in range(99999):
        response = deleteRequest.sendNoneParams(url)
    # b = a.sendHadParams(url,data)

    # a = {}
    # a[""] = "b"
        print(response)