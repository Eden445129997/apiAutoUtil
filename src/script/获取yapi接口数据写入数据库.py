#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.utils import GetRequest
from src.utils.ODBC import odbc
import os


def get_api_list():
    """从yapi获取接口"""
    api_list = []

    # url = "http://10.113.248.211:3000/api/interface/list_menu?project_id=13"
    url = "http://10.113.248.211:3000/api/interface/list?page=1&limit=1000&project_id=92&status=done,design,undone,testing,deprecated,stoping"

    handers = {
        "Cookie": "_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjc0LCJpYXQiOjE1OTk3Mjg3MDAsImV4cCI6MTYwMDMzMzUwMH0.I2bOpMLbjFqOWhEDdZDrdSEPxN_ccvVWjQoW-5HNQJk; _yapi_uid=74"
    }

    # 响应
    response = GetRequest.send_get(url=url, headers_dict=handers)
    # 获取接口列表
    if 1 == 1:
        yapi_api_json_list = response.get("data").get("list")
        for i in range(len(yapi_api_json_list)):
            """
            # 接口id
            api_id = api_json[i].get("_id")
            # 接口细节请求
            api_info_url = "http://10.113.248.211:3000/api/interface/get?id=%s"%api_id
            handers = {
                "Cookie": "_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjc0LCJpYXQiOjE1NzgzMDc2OTgsImV4cCI6MTU3ODkxMjQ5OH0.hWBMDOiCR9dTC0Ve1EBfedmPjRmed_QG-nKwy5amRVk; _yapi_uid=74"
            }
            response = GetRequest.noneParams(api_info_url,handers)
            url_path = response.get("data").get("path")
            """

            # url路径
            url_path = yapi_api_json_list[i].get("path")
            api_list.append([url_path])

            # url请求方式
            api_method = yapi_api_json_list[i].get("method")

            api_list[i].append(api_method)

            # 接口标题
            api_title = yapi_api_json_list[i].get("title")
            api_list[i].append(api_title)

    # print(api_list)
    return api_list
    # return response

def write_in_datebase(api_list):
    """yapi中获取的接口数据写入脚本中"""
    # pass
    db = odbc("qa_platform")
    for i in range(len(api_list)):
        api_name = api_list[i][2]
        api_method = api_list[i][1]
        api_uri = api_list[i][0]
        if api_method == 'GET':
            db.commitSQL("INSERT INTO `qa_platform`.`tb_api`"
                         "(`project_id`, `api_name`, `content_type`, `method`, `path`, `text`, `is_status`, `is_delete`, `create_time`, `update_time`) VALUES "
                         "(1, '%s', 'application/x-www-form-urlencoded', '%s', '%s', '', 1, 0, '2020-05-30 11:00:14.298704', '2020-05-30 11:00:14.298746');"%(api_name,api_method,api_uri))
        else:
            db.commitSQL("INSERT INTO `qa_platform`.`tb_api`"
                         "(`project_id`, `api_name`, `content_type`, `method`, `path`, `text`, `is_status`, `is_delete`, `create_time`, `update_time`) VALUES "
                         "(1, '%s', 'application/json', '%s', '%s', '', 1, 0, '2020-05-30 11:00:14.298704', '2020-05-30 11:00:14.298746');"%(api_name,api_method,api_uri))

    print("done")

if __name__ == '__main__':
    api_list = get_api_list()
    print(api_list)
    write_in_datebase(api_list)
    #
    # for i in api_list:
    #     if i[1] != 'GET' and i[1] != 'POST':
    #         print(i)