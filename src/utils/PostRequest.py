#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.utils.Log import log
import json
import requests


# 添加post请求头
def base(url, data, headers):
    setLog = log()

    # 如果是字典类型，则Json序列化
    if isinstance(data, dict):
        try:
            data = json.dumps(data)
        except:
            setLog.info("失败代码：data = json.dumps(data)")
            setLog.info("失败json序列化参数：" + data)

    # 发送post请求
    try:
        response = requests.post(url=url, data=data, headers=headers, verify=False, timeout=10)
        response = response.content.decode("unicode_escape")
        result = None

        # 判断返回能不能被字典序列化，如果能则返回字典
        try:
            result = json.loads(response)
            return result
        # 非Json的数据则返回text
        except:
            result = response
            return result
        finally:
            setLog.info("接口访问成功，url：" + url)
            setLog.info("请求头：" + str(headers))
            setLog.info("请求体：" + str(data))
            setLog.info("响应体：" + str(result))
    except:
        setLog.error("请求失败：" + url)
        setLog.error("失败请求头：" + str(headers))
        setLog.error("失败请求体：" + str(data))


# 发送返回Json的post请求
def applicationJson(url, data):
    headers = {"Content-Type": "application/json;charset=utf-8"}
    response = base(url, data, headers)
    return response


# 表单为键值对格式（纯字符串）
def applicationFormUrlencode(url, data):
    headers = {"Content-Type": "application/x-www-form-urlencode"}
    response = base(url, data, headers)
    return response


# 将表单数据全部上传，支持value文件格式（二进制文件）
def multipartFormData(url, data):
    headers = {"Content-Type": "multipart/form-data"}
    response = base(url, data, headers)
    return response


if __name__ == '__main__':
    # 天气接口_获取城市对应的id
    # url = "http://47.105.175.129:8771/life-http/life/getMerchantInfoOnClick"
    url = "http://47.105.175.129:8771/life-http/life/getMyNearMerchant"

    # headers = {"Content-Type":"application/json;charsetLog=utf-8"}
    data = {
        "longitude": "120.2111",
        "latitude": "30.2120"
    }
    result = applicationJson(url, data)
    # print(result)
