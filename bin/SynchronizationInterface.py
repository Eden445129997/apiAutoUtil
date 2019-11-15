# coding=UTF-8
from apiAutoUtil.src.utils import GetRequest
from apiAutoUtil.config.path import dataPath
import json
import time

def getApiList():
    response = GetRequest.noneParams(r"http://10.113.248.59:8771/back-http/v2/api-docs")
    info = response.get("paths").items()
    postDto = response.get("definitions").items()
    dtoDict = {}
    for i,j in postDto:
        dtoDict[i] = j
    print(dtoDict)

    # interfaceDict = {}
    # one = 1
    # try:
    #     with open(dataPath() + "interface.txt","w") as fp:
    #         for i,j in info:
    #             # interfaceDict[i] = j
    #             # fp.write(str(interfaceDict) + "\n")
    #
    #             if one:
    #                 fp.write('{"%s":%s,'%(i,j) +  "\n")
    #                 one = one - 1
    #             else:
    #                 fp.write('"%s":%s,'%(i,j) +  "\n")
    #         fp.flush()
    #         fp.close()
    # except:
    #     print("写入文件失败")

    # query/None参数，则说明这是get请求
    # body说明是post请求

    apiCodeList = []
    listIndex = -1
    for i,j in info:
        listIndex = listIndex + 1
        # print(i,j)
        _get = j.get("get")
        _post = j.get("post")
        # 只拥有get
        if _get:
            # pass
            # print(_get)
            # 地址
            # print("path = %s"%i)

            # todo:导进url数组
            apiCodeList.append([i])
            # print("%s"%i)

            # 查看请求头，并且查看请求参数
            # print("%s"%_get.get("consumes"))
            # 入参信息
            getParameters = _get.get("parameters")
            # print(getParameters)

            # 如果有请求参数,
            if getParameters:
                # getParameters[0]
                getMode = getParameters[0].get("in")
                # print(getMode,end="   ")
                if getMode =="query":

                    # todo：确认这个url数组的请求类型
                    apiCodeList[listIndex].append("@getRequest")
                    # print("@getRequest")

                    # 循环获取get的入参数据
                    for index in range(len(getParameters)):
                        getParticipation = getParameters[index].get("description")

                        # todo:入参的key
                        # print(getParticipation,end=':')

                        # 如果有入参数据，则再获取这个入参数据的type
                        if getParticipation:
                            parametersType = getParameters[index].get("type")
                            # 如果是int或者long类型，则打印
                            if parametersType == 'integer':
                                fmt = getParameters[index].get("format")

                                # print(fmt)
                                # todo:get入参
                                apiCodeList[listIndex].append("%s:%s"%(getParticipation,fmt))

                            else:

                                # print(parametersType)
                                # todo:get入参
                                apiCodeList[listIndex].append("%s:%s"%(getParticipation,parametersType))

                            if index == len(getParameters)-1:
                                # print('\n')
                                pass
                # post请求
                else:
                    # print(getMode)

                    # todo：确认这个url数组的请求类型
                    apiCodeList[listIndex].append("@postRequest")
                    # print("@postRequest")

                    schema = getParameters[0].get("schema")
                    # print(schema)
                    # post入参对象路径
                    participationObject = schema.get("$ref")
                    # 打印postDTO
                    for index in range(len(participationObject))[::-1]:
                        if participationObject[index] == "/":
                            # 拿到post入参的key，拿到入参字典
                            participationObject = participationObject[index+1:]
                            # DTO
                            # print(participationObject)
                            # post入参字典
                            postParticipation = dtoDict.get(participationObject).get("properties")
                            # print(postParticipation)

                            # post入参字典
                            for v,n in postParticipation.items():

                                # todo:post入参
                                apiCodeList[listIndex].append("%s:%s"%(v,n))
                                # print("%s:%s"%(v,n))

                            # print('\n')
                            break


            # 如果是None参数，则说明无参get请求也能使用
            else:

                # todo:因为获取不到Parameters，说明这个url没有参数
                apiCodeList[listIndex].append("@getRequest")
                # print("@getRequest")

                # todo:没有参数，自动生成代码的时候需要自动生成入参说明
                apiCodeList[listIndex].append("None")
                # print("None\n\n")

                # pass
        elif _post:
            # post的路径

            # todo:导进url数组
            apiCodeList.append([i])
            # print(i)

            # todo:post入参
            apiCodeList[listIndex].append("@postRequest")
            # print("@postRequest")

            # print(_post)
            participationObject = _post.get("parameters")
            # 唯一一个接口时form/data的，那个上传接口暂时不管
            if len(participationObject)==1:
                # 入参信息
                # print(participationObject)
                participationObject = participationObject[0].get("schema").get("$ref")
                for index in range(len(participationObject))[::-1]:
                    # 找到dtoKey
                    if participationObject[index] == "/":
                        participationObject = participationObject[index+1:]
                        # DTO
                        # print(participationObject)
                        # post入参字典
                        postParticipation = dtoDict.get(participationObject).get("properties")
                        # print(postParticipation)
                        for v,n in postParticipation.items():

                            # todo:post入参
                            apiCodeList[listIndex].append("%s:%s"%(v,n))
                            # print("%s:%s"%(v,n))

                        # print('\n')
                        break
            pass
        else:
            for n in range(20):
                print("有接口不存在get和post！！！！！")

    # 打印看一下list的东西
    for i in apiCodeList:
        print(i)

    return apiCodeList

if __name__ == '__main__':
    aaa = getApiList()
    for i in aaa:
        print(i)