import os
import pymysql
import re

from src.utils.StringUtils import underline_to_highhump


# 生成代码的地址
ROOT_PATH = '/Users/eden/workspace/apiAutoUtil/src/script'

domain_path = os.path.join(ROOT_PATH, 'domain')

DIR_ABS_PATH_LIST = [
    domain_path
]

FILE_NAME_list = [
    'project',
    'host',
    'api',
    'qa_plan',
    'qa_case',
    'api_case_model',
    'api_case_data',
    'api_case_data_node',
    'api_assert',
    'event',
    'event_api_result',
    'event_api_record',
]

def mk_dir(rest_try=3):
    """
    创建三层文件夹，失败重试
    :param file_path:
    :return:
    """

    rest_try = rest_try - 1

    if not os.path.isdir(ROOT_PATH):
        return False

    if not rest_try:
        return False

    for i in DIR_ABS_PATH_LIST:
        if os.path.isdir(i):
            continue
        # 递归重试
        try:
            os.makedirs(i)
        except:
            if not mk_dir(rest_try):
                return False
    return True

def mk_file():
    for i in FILE_NAME_list:
        # class_name = underline_to_highhump(i)
        # 创建service层service文件
        try:
            with open(os.path.join(domain_path, i)  + '.py', "w", encoding='utf-8') as fp:
                fp.write(

"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from django.db import models

from apps.qa_platform.enumeration import (
    REQUEST_METHOD, EVENT_API_STUTAS, CHECK_METHOD, HTTP_CONTENT_TYPE
)
"""
                )
                pass
        except:
            print('失败了',i)
            continue

if __name__ == '__main__':
    mk_dir()
    mk_file()