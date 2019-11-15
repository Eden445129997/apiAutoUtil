# coding:utf-8
from apiAutoUtil.src.utils.Log import log
from apiAutoUtil.src.utils.GetRequest import merge,splitUrl
from apiAutoUtil.config.gloVar import globalEnvironment
import json
import requests


# Json表单请求装饰器
def postRequest(func):
    # 有参post请求
    # 有参post请求，带token
    # 无参post请求
    # 无参post请求，不带token
    def inner_wrapper(data=None,token=None):
        setLog = log()
        __ip,__port = globalEnvironment()
        url = __ip + __port + func()
        headers = {"Content-Type":"application/json;charset=utf-8"}

        # 如果有传token，则用token表单发送请求
        if token:
            headers["token"] = token
            headers["auth"] = token

        # 如果是字典类型，则Json序列化
        if isinstance(data,dict):
            try:
                data = json.dumps(data)
            except:
                setLog.info("失败代码：data = json.dumps(data)" )
                setLog.info("失败json序列化参数：" + data)
            # pass
        # 有data并且data不是字典，并且不带token，那我认为data就是token
        elif data and not isinstance(data,dict) and not token:
            headers["token"] = data
            headers["auth"] = data
            data = None

        # 发送post请求
        try:
            # 有参post请求，带/不带token
            if data:
                response = requests.post(url=url,data=data,headers=headers,verify=False,timeout=10)
            # 无参post请求，带/不带token
            else:
                response = requests.post(url=url,headers=headers,verify=False,timeout=10)
            response.encoding = "UTF-8"
            result = None

            # 判断返回能不能被字典序列化，如果能则返回字典
            try:
                result = json.loads(response.text)
                return result
            # 非Json的数据则返回text
            except:
                result = response.text
                return result
            finally:
                setLog.info("接口访问成功，url：" + url)
                setLog.info("请求头：" + str(headers))
                if data not in headers.values():
                    setLog.info("请求体：" + str(data))
                setLog.info("响应体：" + str(result))
        except:
            setLog.error("请求失败：" + url)
            setLog.error("失败请求头：" + str(headers))
            if data not in headers.values():
                setLog.info("请求体：" + str(data))
    return inner_wrapper

# get请求装饰器
def getRequest(func):
    # 无参url
    # 无参url带token
    # 有参url
    # 有参url带token
    def inner_wrapper(data=None,token=None):
        setLog = log()
        __ip,__port = globalEnvironment()
        url = __ip + __port + func()
        headers = {}

        # 如果有token，则构造token请求头
        if token:
            headers["token"] = token
            headers["auth"] = token

        # 如果data是字典类型，则将data拼接成url
        if isinstance(data,dict):
            url = merge(url,data)
        # 或者如果data不是字典，并且不带token，那我认为data就是token
        elif data and not token:    # 因为上面有if isinstance(data,dict)，所以这里隐藏带一个条件if not isinstance(data,dict)
            headers["token"] = data
            # headers["auth"] = data
            data = None

        try:
            # 请求url，不校验证书，超时10s（不写默认120s）
            # 有请求头则发送请求头，没有则默认python自带的请求头
            if data:
                response = requests.get(url=url,headers=headers,verify=False,timeout=10)
            else:
                response = requests.get(url=url,verify=False,timeout=10)
            response.encoding = "UTF-8"
            result = None

            # 尝试解析成Json格式返回
            try:
                result = json.loads(response.text)
                return result
            # Text格式返回
            except:
                result = response.text
                return result
            finally:
                # setLog.info(r"接口访问成功，url：" + str(splitUrl(url)[0]))
                setLog.info(r"接口访问成功，url：" + url)
                setLog.info(r"请求头：" + str(headers))
                setLog.info(r"请求参：" + str(splitUrl(url)[1]))
                setLog.info(r"响应体：" + str(result))
        except:
            setLog.error(r"请求失败：" + url)
            setLog.info(r"请求头：" + str(headers))
            setLog.info(r"请求参：" + str(splitUrl(url)))
    return inner_wrapper

@postRequest
def postTest():
    return r"/life-http/life/getMyNearMerchant"

@getRequest
def getTest():
    return "/user-http/login/getSmsCode"

if __name__ == '__main__':
    # 天气接口_获取城市对应的id
    # url = "http://47.105.175.129:8771/life-http/life/getMerchantInfoOnClick"
    url = "http://47.105.175.129:8771/life-http/life/getMyNearMerchant"

    headers = {"Content-Type":"application/json;charsetLog=utf-8"}
    data = {
        "longitude":"120.2111",
        "latitude":"30.2120"
    }
    token = "aaa"
    result = postTest(data)
    # print(result)
