#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,json,time
import  re
import pandas
import jsonpath

from functools import wraps

# https警告解除
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 尽量别用这种方式，闭包的方式会慢很多
# 3.2901763916015625e-05
# 8.344650268554688e-06
# def timeTaken(func):
#     """计算执行时间"""
#     startTime = time.time()
#
#     @wraps(func)
#     def inner_wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     stopTime = time.time()
#     timeTaken = stopTime - startTime
#     runner_log.info("方法:%s" % func)
#     runner_log.info("执行时长:%s" % timeTaken)
#     return inner_wrapper

def _get(url, data, headers, timeout=10):
    return requests.request(method='GET', url=url, params=data, headers=headers, verify=False, timeout=timeout)


def _post(url, data, headers, timeout=10):
    return requests.request(method='POST', url=url, json=data, headers=headers, verify=False, timeout=timeout)


def _put(url, data, headers, timeout=10):
    id = data.get("id", -1)
    url = "%s%s" % (url, ("%s/" % id if url[-1] == "/" else "/%s/" % id))
    return requests.request(method="PUT", url=url, data=data, headers=headers, verify=False, timeout=timeout)


def _delete(url, data, headers, timeout=10):
    id = data.get("id", -1)
    url = "%s%s" % (url, ("%s/" % id if url[-1] == "/" else "/%s/" % id))
    return requests.request(method="DELETE", url=url, headers=headers, verify=False, timeout=timeout)


# 选择请求方式
choice = {
    'GET': _get,
    'POST': _post,
    'PUT': _put,
    'DELETE': _delete,
}

# 判断是字典还是数组，如果是字典则执行字典方法

data = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}
import jsonpath

jsonobj ={
    "state":1,
    "message":"success",
    "content":{
        "data":{
            "allCitySearchLabels":{
                "A":[{"id":105795,"name":"澳门特别行政区"},
                     {"id":671,"name":"安庆"},
                     {"id":601,"name":"鞍山"}
                     ]
                }
            }
        }
}



# 从根节点开始，匹配name节点
citylist = jsonpath.jsonpath(jsonobj,'$..name')
# print(citylist)

def search():
    data = "{" \
           "'a': '$..&011#'," \
           "'b': '嘿嘿$你大爷的&1#'," \
           "'c': '哈撒$压缩&2#'" \
           "}"
    print(data)
    # 匹配到的字符串列表
    # search_list = re.findall('\$.+&\d#',data)
    search_list = re.findall('\$.*?&\d+?#',data)
    print(search_list)
    for i in range(len(search_list)):
        try:
            report_node = int(search_list[i][-2:-1])
            # print(report_node)
            # re_list = re.findall('&\d+?#', search_list[i])[0]
            # print(re_list[1:-1])
            # print(search_list[i][:-2])
            serarch_data = re.findall('\$.*?&',search_list[i])[0][:-1]
            print(serarch_data)
        except ValueError as e:
            print(e)

    # print(len(search_list))
    # print(search_list)

if __name__ == '__main__':
    search()
    print("-"*100)
    # headers = {
    #     'CONTENT_TYPE' : 'text/plain'
    # }
    # data = {
    #     'id' : 1
    # }
    # startTime = time.time()
    # stopTime = time.time()
    # timeTaken = stopTime - startTime
    # print(timeTaken)

    # print(choice.get("GET")('http://localhost:9998/platform/ProjectViews/',data,headers).text)
    # response = choice.get("GET")('https://www.baidu.com', {}, {}).text
    # response = "[1,2,3]"
    response = '{"a":{}}'

    print(response)
    print(type(response))

    b = json.loads(response)
    print(b)
    print(type(b))
    print(type(b['a']))

    str = "{'a':@re.arr[0].id$,}"
    # str = "@re.1.a.$"
    search = re.findall("@.+\$",str)
    print(search)
    # str = 'print(data.get("a")[2])'
    # # search = exec(str)
    # exec(str)

    # print(array)

    print(data)
    # search = '$.store.*'
    search = '$.expensive'
    print(search[:-1])
    node = jsonpath.jsonpath(data, search)
    print(node)
    # print(type(node[0]))

    aaa = "{\"a\": '测试1', \"b\": \"测试2\"}"
    aaa = json.dumps(aaa)
    bbb = jsonpath.jsonpath(aaa, '$..')
    print(bbb)