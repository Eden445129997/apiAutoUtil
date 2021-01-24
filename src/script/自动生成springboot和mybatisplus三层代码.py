#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pymysql
import re

# # 是否存在文件路径
# print(os.path.exists(file_path))
# # 是否文件夹
# print(os.path.isdir(file_path))
# # 是否存在文件
# print(os.path.isfile(file_path))

# mysql数据库连接
MYSQL_CONFIG = {
    'host': '111.229.54.5',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'test_platform',
    'charset': 'utf8'
}

# 生成的代码中，里面文件的包路径
PACKAGE_NAME = 'com.platform.test'

# 生成代码的地址
FILE_PATH = '/Users/eden/workspace/apiAutoUtil/src/script'

ENTITY = 'entity'
DAO = 'dao'
MAPPER = 'mapper'
SERVICE = 'service'
IMPL = 'impl'

# 文件夹，固定配置
ENTITY_DIR_ABS_PATH = os.path.join(FILE_PATH, ENTITY)
DAO_MAPPER_DIR_ABS_PATH = os.path.join(FILE_PATH, DAO, MAPPER)
DAO_DIR_ABS_PATH = os.path.join(FILE_PATH, DAO)
SERVICE_DIR_ABS_PATH = os.path.join(FILE_PATH, SERVICE)
SERVICE_IMPL_DIR_ABS_PATH = os.path.join(FILE_PATH, SERVICE, IMPL)

# 生成文件夹绝对路径
DIR_ABS_PATH_LIST = [
    ENTITY_DIR_ABS_PATH,
    DAO_MAPPER_DIR_ABS_PATH,
    DAO_DIR_ABS_PATH,
    SERVICE_DIR_ABS_PATH,
    SERVICE_IMPL_DIR_ABS_PATH
]

# 文件名后缀
ENTITY_FILE_SUFFIX = ''  # 'Entity'
DAO_FILE_SUFFIX = 'Dao'
DAO_MAPPER_FILE_SUFFIX = 'Mapper'
SERVICE_FILE_SUFFIX = "Service"
SERVICE_IMPL_FILE_SUFFIX = "ServiceImpl"


# 字符串转下划线，字符串切割
_space_character = '_'

def underline_to_highhump(simple_string):
    """
    下划线转大驼峰
    :param simple_string:
    :return:
    """
    # 切割
    string_list = str(simple_string).split(_space_character)
    hump_string = ''
    for i in string_list:
        hump_string = hump_string + i.title()
    return hump_string


def underline_to_lowhump(simple_string):
    """
    下划线转小驼峰
    :param simple_string:
    :return:
    """
    # 切割
    string_list = str(simple_string).split(_space_character)

    # 将所有字符串转成小写
    for i in range(len(string_list)):
        string_list[i] = string_list[i].lower()

    # 除了开头的单词，其他的都首字母大写
    others = string_list[1:]
    # str.capitalize():将字符串的首字母转化为大写
    others_capital = [word.capitalize() for word in others]
    # 小写的进入list中的第一个索引
    others_capital[0:0] = [string_list[0]]

    # 将list组合成为字符串，中间无连接符。
    hump_string = ''.join(others_capital)

    return hump_string


def hump_to_underline(hunp_str):
    '''
    驼峰形式字符串转成下划线形式
    :param hunp_str: 驼峰形式字符串
    :return: 字母全小写的下划线形式字符串
    '''
    # 匹配正则，匹配小写字母和大写字母的分界位置
    p = re.compile(r'([a-z]|\d)([A-Z])')
    # 这里第二个参数使用了正则分组的后向引用
    sub = re.sub(p, r'\1_\2', hunp_str).lower()
    return sub


class scan_db:
    """
    扫描数据库表
    :return:
    """

    def __init__(self, MYSQL_CONFIG):
        self.conn = pymysql.connect(
            host=MYSQL_CONFIG.get('host'),
            port=int(MYSQL_CONFIG.get('port')),
            user=MYSQL_CONFIG.get('user'),
            password=MYSQL_CONFIG.get('password'),
            database=MYSQL_CONFIG.get('database'),
            charset=MYSQL_CONFIG.get('charset')
        )

    def get_table(self):
        # 获取游标
        cursor = self.conn.cursor()
        try:
            cursor.execute('show tables')
            table_tuple = cursor.fetchall()
            table_list = [i[0] for i in table_tuple]
            # print(table_list)
            return table_list
        except:
            print("数据库查询表失败")
            return []


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


def mk_dao_code_file(dao_file_name_list, dao_mapper_file_name_list, entity_file_name_list):
    """
    创建dao层代码文件
    :param dao_file_name_list:
    :param dao_mapper_file_name_list:
    :param entity_file_name_list:
    :return:
    """

    # 判断文件数一致
    if len(dao_file_name_list) != len(entity_file_name_list):
        print("entity文件和dao文件数量不一致")
        return False

    # 判断文件数一致
    if len(dao_mapper_file_name_list) != len(entity_file_name_list):
        print("entity文件和mapper文件数量不一致")
        return False

    # 判断文件数一致
    if len(dao_file_name_list) != len(dao_mapper_file_name_list):
        print("mapper文件和dao文件数量不一致")
        return False

    for i in range(len(dao_mapper_file_name_list)):
        # 实体类的文件名
        entity_file_name = entity_file_name_list[i]

        # 文件名
        dao_file_name = dao_file_name_list[i]
        mapper_file_name = dao_mapper_file_name_list[i]

        # 文件绝对路径
        dao_input_stream_path = '%s%s' % (os.path.join(DAO_DIR_ABS_PATH, dao_file_name), '.java')
        mapper_input_stream_path = '%s%s' % (os.path.join(DAO_MAPPER_DIR_ABS_PATH, mapper_file_name), '.java')

        # 创建dao层mapper文件
        try:
            with open(mapper_input_stream_path, "w", encoding='utf-8') as fp:
                fp.write('package %s.%s.%s;\n\n' % (PACKAGE_NAME , DAO, MAPPER))
                fp.write('import com.baomidou.mybatisplus.core.mapper.BaseMapper;\n')
                fp.write('import %s.%s.%s;\n\n' % (PACKAGE_NAME, ENTITY, entity_file_name))
                fp.write('public interface %s extends BaseMapper<%s> {\n}\n' % (mapper_file_name, entity_file_name))
        except:
            print('创建dao层mapper文件失败：%s' % dao_input_stream_path)
            continue

        # 大驼峰转小驼峰
        lowhump = underline_to_lowhump(hump_to_underline(mapper_file_name))

        # 创建dao层impl文件
        try:
            with open(dao_input_stream_path, "w", encoding='utf-8') as fp:
                fp.write('package %s.%s;\n\n' % (PACKAGE_NAME, DAO))
                fp.write('import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;\n')
                fp.write('import org.springframework.stereotype.Component;\n')
                fp.write('import %s.%s.%s.%s;\n' % (PACKAGE_NAME, DAO, MAPPER, mapper_file_name))
                fp.write('import %s.%s.%s;\n\n' % (PACKAGE_NAME, ENTITY, entity_file_name))
                fp.write('import javax.annotation.Resource;\n\n')
                fp.write('@Component\n')
                fp.write('public class %s extends ServiceImpl<%s, %s> {\n\n' % (
                dao_file_name, mapper_file_name, entity_file_name))
                fp.write('    @Resource\n')
                fp.write('    private %s %s;\n\n'%(mapper_file_name, lowhump))
                fp.write('}\n')

        except:
            print('创建dao层impl文件失败：%s' % mapper_input_stream_path)
            continue


def mk_service_code_file(service_file_name_list, service_impl_file_name_list, entity_file_name_list):
    """
    创建service层基础代码文件
    :param service_file_name_list:
    :param service_impl_file_name_list:
    :param entity_file_name_list:
    :return:
    """
    for i in range(len(service_file_name_list)):
        # 实体类的文件名
        entity_file_name = entity_file_name_list[i]

        service_file_name = service_file_name_list[i]
        service_impl_file_name = service_impl_file_name_list[i]

        service_input_stream_path = '%s%s' % (os.path.join(SERVICE_DIR_ABS_PATH, service_file_name), '.java')
        service_impl_input_stream_path = '%s%s' % (
        os.path.join(SERVICE_IMPL_DIR_ABS_PATH, service_impl_file_name), '.java')

        # 创建service层service文件
        try:
            with open(service_input_stream_path, "w", encoding='utf-8') as fp:
                fp.write('package %s.%s;\n\n' % (PACKAGE_NAME, SERVICE))
                fp.write('import com.baomidou.mybatisplus.extension.service.IService;\n')
                fp.write('import %s.%s.%s;\n\n' % (PACKAGE_NAME, ENTITY, entity_file_name))
                fp.write('public interface %s {\n}\n' % (service_file_name))
        except:
            print('创建service层service文件失败：%s' % service_input_stream_path)
            continue

        # 创建service层serviceImpl文件
        try:
            with open(service_impl_input_stream_path, "w", encoding='utf-8') as fp:
                fp.write('package %s.%s.%s;\n\n' % (PACKAGE_NAME, SERVICE, IMPL))
                fp.write('import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;\n')
                fp.write('import org.springframework.stereotype.Service;\n')
                fp.write('import %s.%s.%s;\n'%(PACKAGE_NAME, SERVICE, service_file_name))
                fp.write('import %s.%s.%s;\n\n' % (PACKAGE_NAME, ENTITY, entity_file_name))
                fp.write('@Service\n')
                fp.write('public class %s implements %s {\n}\n' % (service_impl_file_name, service_file_name))
        except:
            print('创建service层service文件失败：%s' % service_input_stream_path)
            continue


def mk_code_director():
    """
    生成代码的指挥者
    :return:
    """

    # 连接数据库
    db = scan_db(MYSQL_CONFIG)
    # 获取表名列表
    table_name_list = db.get_table()

    # entity文件名列表
    entity_file_name_list = []

    # dao文件名列表
    dao_file_name_list = []
    dao_mapper_file_name_list = []
    # service文件名列表
    service_file_name_list = []
    service_impl_file_name_list = []

    # 即将创建的文件名列表
    for i in table_name_list:
        # entity文件名，大驼峰
        entity_file_name_list.append('%s%s' % (underline_to_highhump(i), ENTITY_FILE_SUFFIX))

        # dao文件名，表名转大驼峰
        dao_file_name_list.append('%s%s' % (underline_to_highhump(i), DAO_FILE_SUFFIX))
        dao_mapper_file_name_list.append('%s%s' % (underline_to_highhump(i), DAO_MAPPER_FILE_SUFFIX))

        # service层文件名，表名大驼峰
        service_file_name_list.append('%s%s' % (underline_to_highhump(i), SERVICE_FILE_SUFFIX))
        service_impl_file_name_list.append('%s%s' % (underline_to_highhump(i), SERVICE_IMPL_FILE_SUFFIX))

    # 创建文件夹，失败返回false
    if not mk_dir():
        return False

    # 创建dao层文件
    mk_dao_code_file(
        # 文件名 （列表）
        dao_file_name_list=dao_file_name_list, dao_mapper_file_name_list=dao_mapper_file_name_list,
        # 实体类 （列表）
        entity_file_name_list=entity_file_name_list
    )

    # 创建service层文件
    mk_service_code_file(
        service_file_name_list, service_impl_file_name_list,
        entity_file_name_list
    )


if __name__ == '__main__':
    mk_code_director()
