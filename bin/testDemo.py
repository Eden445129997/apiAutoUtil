# coding=UTF-8

from apiAutoUtil.config.path import qiaokuInterfaceObject,dataPath
from apiAutoUtil.bin.SynchronizationInterface import getApiList
import time

info = getApiList()

try:
    with open(dataPath() + "backHttp.py","w") as fp:
        fp.write("# coding=UTF-8\n")
        fp.write("from apiAutoUtil.src.utils.Decorator import getRequest\n")
        fp.write("from apiAutoUtil.src.utils.Decorator import postRequest\n\n")

        for i in range(len(info)):
            # 装饰器请求方式
            fp.write(info[i][1] + "\n")

            # 接口方法名
            urlPath = None
            # 倒序循环，截取字符串
            for index in range(len(info[i][0]))[::-1]:
                if info[i][0][index] == "/":
                    urlPath = info[i][0][index+1:]
                    break
            fp.write("def " + urlPath + "():\n")

            # 写入参数据
            for index in range(len(info[i])-2):
                fp.write(4*" " + "# " + info[i][index+2] + "\n")

            # 接口路径字符串
            fp.write(4*" " + "return \"/back-http" + info[i][0] + "\"\n\n")

        fp.flush()
        fp.close()
except:
    print("写入文件失败")