import os
import pymysql
import re

from src.utils.StringUtils import underline_to_highhump


# 生成代码的地址
FILE_PATH = '/Users/eden/workspace/apiAutoUtil/src/script'

controller_path = os.path.join(FILE_PATH, 'controller')

DIR_ABS_PATH_LIST = [
    controller_path
]

controller_name_list = [
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

    if not os.path.isdir(FILE_PATH):
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

def create_code_file():
    for i in controller_name_list:
        class_name = underline_to_highhump(i)
        # 创建service层service文件
        try:
            with open(i + '_controller.py', "w", encoding='utf-8') as fp:
                fp.write('#!/usr/bin/env python3\n')
                fp.write('# -*- coding: utf-8 -*-\n\n')
                fp.write('# 模型\n')
                fp.write('from apps.qa_platform.models import domain\n')
                fp.write('# 自定义模型视图\n')
                fp.write('from apps.common.views import CustomModelViewSet\n')
                fp.write('# 序列化\n')
                fp.write('from apps.qa_platform import serializers\n\n')
                fp.write('class %sViews(CustomModelViewSet):\n'%class_name)
                fp.write('    queryset = domain.%s.objects.all()\n'%class_name)
                fp.write('    serializer_class = serializers.%sSerializer\n'%class_name)


        except:
            print('失败了',i)
            continue

if __name__ == '__main__':
    # if mk_dir():
    #     create_code_file()
    mk_dir()