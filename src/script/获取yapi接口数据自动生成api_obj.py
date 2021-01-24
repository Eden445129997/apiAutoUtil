#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from src.utils import GetRequest
import os


def get_api_list(open):
    """
    从yapi获取接口
    :param open:如果是1则装进list
    :return:
    """

    api_list = []

    # url = "http://10.113.248.211:3000/api/interface/list_menu?project_id=13"
    url = "http://10.113.248.211:3000/api/interface/list?page=1&limit=1000&project_id=71&status=done,design,undone,testing,deprecated,stoping"

    handers = {
        "Cookie": "_yapi_uid=74; _yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjc0LCJpYXQiOjE1OTU5MjczMDIsImV4cCI6MTU5NjUzMjEwMn0.dfCj4uoUG2sZfpR6fkLU26rYytVcv2tqAFl73NyxZTg"

    }

    # 响应
    # response = GetRequest.noneParams(url, handers)
    # 获取接口列表
    if 1 == open:
        api_json = response.get("data").get("list")
        for i in range(len(api_json)):
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
            url_path = api_json[i].get("path")
            api_list.append([url_path])

            # url请求方式
            url_method = api_json[i].get("method")

            if url_method == "POST":
                api_list[i].append("@postRequest")
            else:
                api_list[i].append("@getRequest")

            # 接口标题
            url_title = api_json[i].get("title")
            api_list[i].append(url_title)

    # print(api_list)
    # return api_list
    return api_list

def write_api_obj(api_list):
    """yapi中获取的接口数据写入脚本中"""

    try:
        with open(os.path.dirname(os.path.abspath(__file__)) + "/" + "apiObj.py", "w", encoding='utf-8') as fp:
            # 写顶部
            fp.write("#!/usr/bin/env python3\n")
            fp.write("# -*- coding: utf-8 -*-\n")
            fp.write("from src.utils.Decorator import getRequest\n")
            fp.write("from src.utils.Decorator import postRequest\n\n")

            for i in range(len(api_list)):
                # 装饰器请求方式
                # @postRequest or @getRequest
                fp.write(api_list[i][1] + "\n")

                # 接口方法名——将path改成合法的python命名
                urlPath = api_list[i][0]
                # urlPath = urlPath.replace("_app-http_", "")
                urlPath = urlPath.replace("/", "_")
                urlPath = urlPath.replace("api-", "")
                # urlPath = urlPath.replace("{", "")
                # urlPath = urlPath.replace("}", "")
                # urlPath = urlPath.replace("-", "_")
                # urlPath = urlPath.replace(urlPath[0], "") if urlPath[0] == "_" else urlPath
                urlPath = urlPath[1:]

                # 写定义函数方法
                # def mcnInfo_updateTbMcnInfo():
                fp.write("def " + str(urlPath) + "():\n")

                # 标题
                # """(后台)删除mcn机构"""
                fp.write(4 * " " + "\"\"\"%s\"\"\"\n" % api_list[i][2])

                # 写入参数据
                # for index in range(len(info[i])-2):
                #     fp.write(4*" " + "# " + info[i][index+2] + "\n")

                # 接口路径字符串
                # ‘    return "/back-http/mcnInfo/updateTbMcnInfo"’
                fp.write(4 * " " + "return \"" + api_list[i][0] + "\"\n\n")

            fp.flush()
            fp.close()
    except:
        print("写入文件失败")


if __name__ == '__main__':
    api_list = get_api_list(1)
    print(api_list)
    # print(os.path.dirname(os.path.abspath(__file__)) + "/" + "apiObj.py")
    write_api_obj(api_list)
