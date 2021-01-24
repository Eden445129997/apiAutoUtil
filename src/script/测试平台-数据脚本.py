#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.utils.ODBC import odbc
import json, requests

test_platform_db = odbc("test_platform")

# eden=1，唐甜=2，国梁=3，嵩鹏=4
plan_id = 2


def select_interface():
    """查询是否存在接口"""
    # url地址信息（/platform/login/）
    path = '/app-http/v104/user/getAppUserBasicInfo'

    interface_info = test_platform_db.selectSQL(
        "SELECT * FROM `test_platform`.`tb_interface` WHERE `path` LIKE '%{}%' LIMIT 0,1000"
            .format(path)
    )
    print(interface_info[0])
    print(interface_info[1])


def select_test_case():
    """查询测试用例"""
    case_info = test_platform_db.selectSQL(
        "SELECT * FROM `test_platform`.`tb_test_case` WHERE `plan_id` = '{}' LIMIT 0,1000"
            .format(plan_id)
    )
    print(case_info[0])
    print(case_info[1])

    for i in case_info[1] if isinstance(case_info[1], tuple) else ():
        print(i)


def select_test_case_detail(case_id):
    """查询测试用例"""

    case_info = test_platform_db.selectSQL(
        "SELECT * FROM `test_platform`.`tb_test_case_detail` WHERE `case_id` = '{}' LIMIT 0,1000"
            .format(case_id)
    )
    print(case_info[0])
    for i in case_info[1] if isinstance(case_info[1], tuple) else ():
        print(i)


def set_interface():
    """填写接口数据"""
    # 接口名称
    api_name = '测试一下'
    # 请求方法（GET、POST、PUT、DELETE）
    method = 'GET'
    # url地址信息（/platform/login/）
    path = '/platform/login/'
    # 接口描述
    text = ''

    test_platform_db.commitSQL(
        "INSERT INTO "
        "`test_platform`.`tb_interface`"
        "(`project_id`, `busi_id`, `api_name`, `method`, `path`, `default_data`, `text`, `status`, `create_time`, `update_time`) VALUES "
        "('1', '1', '%s', '%s', '%s', '{}', %s, 0, now(), now());"
        % (api_name, method, path, text)
    )


def set_test_case():
    """创建测试用例"""

    # 用例名称
    case_name = '查看自己个人主页'
    # 用例描述
    text = '查看自己个人主页'

    case_sort = test_platform_db.selectSQL(
        "SELECT sort FROM `test_platform`.`tb_test_case` WHERE `plan_id` = '{}' order by sort desc LIMIT 0,1000"
            .format(plan_id)
    )[1]
    if isinstance(case_sort, int):
        case_sort = case_sort + 1
    else:
        case_sort = 0
    test_platform_db.commitSQL(
        "INSERT INTO "
        "`test_platform`.`tb_test_case`"
        "( `plan_id`, `case_name`, `text`, `sort`, `status`, `create_time`, `update_time`) VALUES "
        "('%s', '%s', '%s', %s, 1, now(), now());"
        % (plan_id, case_name, text, case_sort)
    )


def set_test_case_detail():
    """创建测试节点"""
    # 绑定的用例id
    case_id = 6
    # 请求的接口id
    interface_id = 156
    # 重连次数（网络延迟原因时会重新发送请求）
    reconnection_times = 3
    # 最长等待时长（网络请求后设置的等待时间，超过则设置为超时请求）
    wait_time = 10
    # 请求头
    headers = {}
    # 请求入参，根据请求的方式而不同：
    # get请求则都是查询参数
    # post则请求参数都在请求体
    # put和delete则都是id放path中，请求数据则放请求体中）
    data = '{}'
    # 参数化(0：不启用，1：启用mock)
    # 如果是1，则data中的数据，则会捕捉参数化表达式，否则当作普通字符串处理
    expression_status = 0
    # mock状态（0：不启用，1：启用mock）默认0
    # 如果是1，则跳过发送该请求，并且将mock_response的数据当做本次请求的响应数据
    mock_status = 0
    mock_response = {}
    # 描述
    text = '节点描述'

    data = json.dumps(data)
    data = data[1:-1]

    case_sort = test_platform_db.selectSQL(
        "SELECT sort FROM `test_platform`.`tb_test_case_detail` WHERE `case_id` = '{}' order by sort desc LIMIT 0,1000"
            .format(case_id)
    )[1]
    if isinstance(case_sort, int):
        case_sort = case_sort + 1
    else:
        case_sort = 0
    test_platform_db.commitSQL(
        "INSERT INTO "
        "`test_platform`.`tb_test_case_detail`"
        "(`case_id`, `interface_id`, `reconnection_times`, `wait_time`, `headers`, `data`, `mock_status`, `mock_response`, `text`, `sort`, `status`, `create_time`, `update_time`, `expression_status`) VALUES "
        "('%s', '%s', %s, %s, '%s', '%s', %s, '%s', '%s', %s, 1, now(), now(), %s);"
        % (case_id, interface_id, reconnection_times, wait_time, headers, data, mock_status, mock_response, text,
           case_sort, expression_status)
    )


def set_check_point():
    """添加检查点"""
    # 测试节点id
    case_detail_id = 1
    # 检查对象（jsonpath语法）
    check_object = '$..'
    # 测试方法（assertEqual、assertNotEqual、assertIn、assertNotIn）
    check_method = 'assertEqual'
    # 期望的校验值
    check_value = '{\"token\": \"Django token\", \"routers\": [\"*\"]}'
    # 状态(0：不启用,1：启用)
    status = 1
    test_platform_db.commitSQL(
        "INSERT INTO "
        "`test_platform`.`tb_check_point`"
        "(`case_detail_id`, `check_object`, `check_method`, `check_value`, `text`, `status`, `create_time`, `update_time`) VALUES "
        "('{}', '{}', '{}', '{}', NULL, {}, now(), now());"
        .format(case_detail_id, check_object, check_method, check_value, status)
    )


def run_test_plan():
    data = {
        'id': plan_id,
        'host': 'http://10.113.248.203',
        'headers': {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTM3NjE3NjgsInVzZXJJZCI6NjI3NDcyNDgxMjI5MjA5NjAwLCJ1c2VyUGxhdGZvcm0iOiJhcHAiLCJ1ZGlkIjoibG9naW4iLCJpc3MiOiJxaWFva3UifQ.E7orgNK1a1waClF_CCxToiKZ9Eq1r969GtZC3yjYrdI"}
    }
    data = json.dumps(data)
    # 平台地址
    platform_host = 'http://localhost:9998/'
    path = 'platform/runTestPlanById/'
    url = platform_host + path
    requests.post(url=url, data=data)


def test():
    """测试代码专用函数"""
    pass
    # data = '{"test":$..&0#}'
    # data = json.dumps(data)
    # print(data[1:-1])


if __name__ == '__main__':
    pass
    # 查询是否存在接口
    # select_interface()
    # 查询测试用例
    # select_test_case()
    # 查询测试用例下的用例细节
    # select_test_case_detail(1)

    # 填写接口数据
    # set_interface()
    # 创建测试用例
    # set_test_case()
    # 创建接口测试数据
    # set_test_case_detail()
    #
    # set_check_point()

    # 根据plan_id执行测试用例
    run_test_plan()
