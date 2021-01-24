#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib3, requests, random

# https警告解除
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

METHOD_LIST = ['GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE']

CONTENT_TYPE = [
    "text/plain",
    "application/x-www-form-urlencoded",
    "application/json",
]


def _default(method, url, params=None, body=None, headers=None, timeout=10):
    if not isinstance(method, str) or method.upper() not in METHOD_LIST:
        raise RuntimeError
    if headers and 'application/json' in headers.get('Content-Type','') :
        return requests.request(method=method, url=url, params=params, json=body, headers=headers, verify=False,
                                timeout=timeout)
    return requests.request(method=method, url=url, params=params, data=body, headers=headers, verify=False,
                            timeout=timeout)


def _get(url, params, body, headers, timeout=10):
    return _default('GET', url, params, body, headers, timeout=timeout)


def _post(url, params, body, headers, timeout=10):
    return _default('POST', url, params, body, headers, timeout=timeout)


def _put(url, params, body, headers, timeout=10):
    return _default('PUT', url, params, body, headers, timeout=timeout)


def _delete(url, params, body, headers, timeout=10):
    return _default('DELETE', url, params, body, headers, timeout=timeout)


# 选择请求方式
choice = {
    'DEFAULT': _default,
    'GET': _get,
    'POST': _post,
    'PUT': _put,
    'DELETE': _delete,
}


def int_random(x):
    """ 生成x个随机数
    :param x:
    :return string:
    """
    randomString = ""
    for i in range(x):
        toString = str(random.randint(0, 9))
        randomString = "%s%s"%(randomString, toString)
    return randomString

if __name__ == '__main__':
    # 循环手机号码的次数
    x = 1

    for i in range(x):
        phone_num = "153%s"%int_random(8)

        # 请求1
        params = {
            "a": "1",
            "b": "2",
            "c": "3"
        }
        body = {
            "a": "1",
            "b": "2",
            "c": "3"
        }
        response = choice.get('GET')('http://localhost:9998/testapi/?test=aaa', params, body,
                                     {"Content-Type": "text/plain"}, 10)
        print(response.text)

        # 请求2
        params = {
            "a": "1",
            "b": "2",
            "c": "3"
        }
        body = {
            "a": "1",
            "b": "2",
            "c": "3"
        }
        response = choice.get('GET')('http://localhost:9998/testapi/?test=aaa', params, body,
                                     {"Content-Type": "text/plain"}, 10)
        print(response.text)