#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from urllib.parse import urlparse, urlencode, quote

'''
dict1 = {'a':'测试一下'}
url_data = parse.urlencode(dict1) #unlencode()将字典{k1:v1,k2:v2}转化为k1=v1&k2=v2
print(url_data)             #url_data：wd=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91

str1 = '我来了'
str2 = parse.quote(str1)    #将字符串进行编码
print(str2)                 #str2=haha%E5%93%88%E5%93%88
str3 = parse.unquote(str2)  #解码字符串
print(str3)                 #str3=haha哈哈
'''

# 驼峰转换的切割字符串（公共变量）
_SPACE_CHARACTER = '_'

def protocol_validate(scheme : str):
    """
    校验是否合法的协议
    :param url:
    :return:
    """

    schemes = ['http', 'https', 'ftp', 'ftps']
    # 协议判断
    if scheme not in schemes:
        return False
    return True

def domain_validate(domain : str):
    '''
    域名校验
    :param url:
    :return:
    '''

    # rule = r'^[a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63})*$'
    rule = r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'\
           r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'\
           r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'\
           r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'

    return True if re.match(
        rule,
        domain
    ) else False

def ip_validate(ip : str):
    '''
    ip校验
    :param url:
    :return:
    '''
    return True if re.match('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip) else False

def host_validate(host : str):
    '''
    校验是否合法的host
    :param url:
    :return:
    '''
    # 域名校验(域名和ip两个都是false则进入判断)
    if not domain_validate(host) and not ip_validate(host):
        return False
    return True

def port_validate(port : str):
    '''
    端口校验
    :param port:
    :return:
    '''
    return True if re.match(r'(?![a-zA-Z])(\d{2,5})$',port) else False

def url_validate(url : str):
    """
    url校验类
    :param url:
    :return:
    """
    result = urlparse(url)

    # 获取类属性的数组
    # members = [attr for attr in dir(urlparse_result) if not callable(getattr(urlparse_result, attr)) and not attr.startswith("_")]
    # print(members)
    # 循环打印类属性
    # for i in members:
    #     print(getattr(urlparse_result,i))

    # 存在协议则校验协议
    if result.scheme and not protocol_validate(result.scheme):
        return False

    # 不存在host、host校验失败则会进入判断
    if not result.hostname or not host_validate(result.hostname):
        return False

    # 存在端口则校验端口
    if result.port and not port_validate(str(result.port)):
        return False

    return True

def get_dict_by_url(url : str):
    '''
    获取url中的query
    :param url:
    :return: dict
    '''
    url_obj = urlparse(url)
    result = {}

    # 1、判断是否字符串2、判断是否合法的url3、判断url中是否存在query参数
    if not isinstance(url,str) or not url_validate(url) or not url_obj.query:
        return result

    for param in url_obj.query.split("&"):
        pindex = param.find('=')
        if pindex > 0:
            result[param[:pindex]] = param[pindex + 1:]

    return result

def meger_url_with_params(url : str, params : dict):
    '''
    将url和query参数拼接
    :param url:
    :param params:
    :return: str
    '''
    if not isinstance(url, str) or not isinstance(params,dict):
        raise RuntimeError
    return '%s?%s'%(url,urlencode(params))

def underline_to_highhump(simple_string : str):
    """
    下划线转大驼峰
    :param simple_string:
    :return: str
    """
    result = ''
    # 字符串判断
    if not isinstance(simple_string, str):
        raise RuntimeError
    # 切割
    string_list = simple_string.split(_SPACE_CHARACTER)
    for i in range(len(string_list)):
        string_list[i] = string_list[i].title()
    return result.join(string_list)

def underline_to_lowhump(simple_string : str):
    """
    下划线转小驼峰
    :param simple_string:
    :return:
    """

    if not isinstance(simple_string, str):
        raise RuntimeError

    # 切割
    lowhump_list = simple_string.split(_SPACE_CHARACTER)

    # 将所有字符串转成小写
    for i in range(len(lowhump_list)):
        lowhump_list[i] = lowhump_list[i].lower()

    # str.capitalize():将字符串的首字母转化为大写
    highhump_list = [highhump.capitalize() for highhump in lowhump_list[1:]]
    # 大驼峰插入第一个小驼峰的单词
    highhump_list.insert(0,lowhump_list[0])
    return ''.join(highhump_list)

def hump_to_underline(hunp_str : str):
    '''
    (大小)驼峰转下划线
    :param hunp_str: 驼峰形式字符串
    :return: 字母全小写的下划线形式字符串
    '''
    # 匹配正则，匹配小写字母和大写字母的分界位置
    p = re.compile(r'([a-z]|\d)([A-Z])')
    # 这里第二个参数使用了正则分组的后向引用
    sub = re.sub(p, r'\1_\2', hunp_str).lower()
    return sub

def json_hump_underline(hump_json_str : str):
    '''
    把一个json字符串中的所有字段名都从驼峰形式替换成下划线形式。
    注意点：因为考虑到json可能具有多层嵌套的复杂结构，所以这里直接采用正则文本替换的方式进行处理，而不是采用把json转成字典再进行处理的方式
    :param hump_json_str: 字段名为驼峰形式的json字符串
    :return: 字段名为下划线形式的json字符串
    '''
    # 从json字符串中匹配字段名的正则
    # 注：这里的字段名只考虑由英文字母、数字、下划线组成
    attr_ptn = re.compile(r'"\s*(\w+)\s*"\s*:')
    # 使用hump2underline函数作为re.sub函数第二个参数的回调函数
    sub = re.sub(attr_ptn, lambda x: '"' + hump_to_underline(x.group(1)) + '" :', hump_json_str)
    return sub


if __name__ == '__main__':
    # url字符串相关方法
    # print(ip_validate('www.baidu.com:8888/path?a=1&b=2'))
    # print(url_validate('https://www.baidu.com:8888/path?a=1&b=2'))
    # print(url_validate('https://255.255.255.255:8888/path?a=1&b=2'))
    # print(url_validate('aaa:80'))

    val = 'www.baidu.com'
    # val = '10.255.255.255'
    # print(ip_validate(val))
    # print(domain_validate(val))
    print(host_validate(val))
    # print(url_validate(':80/aa/bb?a=1^b=2'))
    # print(port_validate('999'))
    # url = meger_url_with_params('https://www.baidu.com:8888/path',{"a":2,"c":3})
    # print(url)

    # 下划线和驼峰互转
    # string = hump_to_underline("TbTestCase")
    # string = underline_to_lowhump(string)
    # string = underline_to_lowhump("tb_test_case")

    # print(string)