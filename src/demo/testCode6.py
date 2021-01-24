import requests

# https警告解除
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def _get(url, data, headers, timeout=10):
    return requests.request(method='GET', url=url, params=data, headers=headers, verify=False, timeout=timeout)


def _post(url, data, headers, timeout=10):
    return requests.request(method='POST', url=url, json=data, headers=headers, verify=False, timeout=timeout)


def _put(url, data, headers, timeout=10):
    id = data.get("id", -1)
    url = "%s%s" % (url, ("%s/" % id if url[-1] == "/" else "/%s/" % id))
    return requests.request(method="PUT", url=url, data=data, headers=headers, verify=False, timeout=timeout)


def _delete(url, data, headers, timeout=10):
    id = data.get("id", -1)
    url = "%s%s" % (url, ("%s/" % id if url[-1] == "/" else "/%s/" % id))
    return requests.request(method="DELETE", url=url, headers=headers, verify=False, timeout=timeout)

# 选择请求方式
choice = {
    'GET': _get,
    'POST': _post,
    'PUT': _put,
    'DELETE': _delete,
}

if __name__ == '__main__':
    headers = {
        # 'CONTENT_TYPE' : 'text/plain'
    }
    data = {
        # 'id' : 1
    }

    print(choice.get("GET")('https://www.baidu.com/',data,headers).content)
