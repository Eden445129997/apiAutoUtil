#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, json
from src.utils.Log import log
from src.utils.StringUtils import get_dict_by_url, meger_url_with_params
# from src.utils import RequestMethod
from src.utils.HttpUtils import choice


setLog = log()


def send_get(url, params_dict=None, body_dict=None, headers_dict=None):
    result = None

    if not params_dict:
        params_dict = get_dict_by_url(params_dict)
    if not body_dict or not headers_dict:
        body_dict = {}
        params_dict = {}
    try:
        # 请求url，不校验证书，超时10s（不写默认120s）
        # 有请求头则发送请求头，没有则默认python自带的请求头
        response = choice.get('GET')(url, params_dict, body_dict, headers_dict)
        response = response.text
        # response = response.content.decode("unicode_escape")

        # 尝试解析成字典对象返回
        try:
            result = json.loads(response)
            return result
        # Text格式返回
        except:
            result = response
            return result
        finally:
            setLog.info(r"接口访问成功，url：%s"%url)
            setLog.info(r"请求头：%s"%str(headers_dict))
            setLog.info(r"请求参：%s"%get_dict_by_url(url))
            setLog.info(r"响应体：%s"%str(result))
    except IOError as e:
        setLog.error(r"请求失败：%s"%meger_url_with_params(url, params_dict))
        setLog.error(e)
        setLog.info(r"请求头：%s"%str(headers_dict))
        setLog.info(r"请求参：%s"%get_dict_by_url(url))


# 测试主方法
if __name__ == '__main__':
    # 天气接口_获取城市对应的id
    # url = r"http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince"
    # url = r"http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString"
    # url = r"http://47.105.175.129:8771/user-http/login/getSmsCode?&userPhone=15361899636&udid=abcdefg"
    # url = r"http://47.105.175.129:8771/user-http/login/getSmsCode"
    # url = "http://10.113.248.203:80/app-http/video/getVideos?pageIndex=1&pageSize=12&type=new&queryTime=2019-11-12%2007%3A45%3A03"
    url = 'http://localhost:9998/testapi/'
    params ={
        "a": 1,
        'b': True,
        'c': "哈哈哈",
        'd': {"a":1,"asdf":{}}
    }
    body = {
        "a": "22"
    }
    headers = {
        'Content-Type': 'application/json',
        "aa": "aaa"
    }
    b = send_get(url=url,params_dict=params,body_dict=body, headers_dict=headers)
    print(b)
    # 安卓
    # 2019-11-12%2007%3A56%3A33
    # ios
    # 2019-11-12%2019%3A57%3A01
