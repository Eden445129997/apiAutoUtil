#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from src.utils.Log import log

# 将url地址和字典参数合并
def merge(url,data):
    url = url + "?"
    for i in data.keys():
        url = url + "&" + i + "=" + str(data[i])
    return url

# 获取get请求，并将参数转换成字典
def splitUrl(url):
    params = ""
    data = {}

    # 拆分url参数，从？开始拆分
    for i in range(len(url)):
        if url[i] == "?":
            params = url[i+1:]
            url = url[:i]
            break

    # 分割&，组装成list
    list = params.split("&")

    # 将list里面的键值对转换成字典
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == "=":
                data[list[i][:j]] = list[i][j+1:]
    return url,data

#有参get请求,params入参为字典类型
def hadParams(url,data,headers=None):
    # 合并url和字典参数
    if isinstance(data,dict):
        url = merge(url,data)
    # 如果自定义请求头，则发送带有请求头的get请求，没有则默认
    if headers:
        response = noneParams(url,headers)
    else:
        response = noneParams(url)
    return response

#无参get请求
def noneParams(url,headers=None):
    setLog = log()
    try:
        # 请求url，不校验证书，超时10s（不写默认120s）
        # 有请求头则发送请求头，没有则默认python自带的请求头
        if headers:
            response = requests.get(url=url,headers=headers,verify=False,timeout=10)
        else:
            response = requests.get(url=url,verify=False,timeout=10)
        response.encoding = "UTF-8"
        result = None

        # 尝试解析成Json格式返回
        try:
            result = json.loads(response.text)
            return result
        # Text格式返回
        except:
            result = response.text
            return result
        finally:
            setLog.info(r"接口访问成功，url：" + str(splitUrl(url)[0]))
            setLog.info(r"请求头：" + str(headers))
            setLog.info(r"请求参：" + str(splitUrl(url)[1]))
            setLog.info(r"响应体：" + str(result))
    except:
        setLog.error(r"请求失败：" + url)
        setLog.info(r"请求头：" + str(headers))
        setLog.info(r"请求参：" + str(splitUrl(url)))

#测试主方法
if __name__ == '__main__':
    #天气接口_获取城市对应的id
    # url = r"http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince"
    # url = r"http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString"
    # url = r"http://47.105.175.129:8771/user-http/login/getSmsCode?&userPhone=15361899636&udid=abcdefg"
    # url = r"http://47.105.175.129:8771/user-http/login/getSmsCode"
    url = "http://10.113.248.203:80/app-http/video/getVideos?pageIndex=1&pageSize=12&type=new&queryTime=2019-11-12%2007%3A45%3A03"

    #极验初始化
    # url = "http://10.113.248.200:8771/app-http/login/startCaptcha?&userPhone=12345678901&c=1&d=2&b=3&a=4&a=5&a=6&"
    # data = {
    #     "userPhone":"15361899636",
    #     "udid":"abcdefg",
    # }
    # splitUrl(url)
    b = noneParams(url,{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzM1NTE3MTUsInVzZXJJZCI6NjI3NDcyNDgxMjI5MjA5NjAwLCJ1ZGlkIjoiIiwiaXNzIjoicWlhb2t1In0.CJb-gAQJH_UCaA8WbMW4Jmwd_fQrX4fAV498EJ7nE84"})
    # b = a.sendHadParams(url,data)
    print(b)
    # 安卓
    # 2019-11-12%2007%3A56%3A33
    # ios
    # 2019-11-12%2019%3A57%3A01