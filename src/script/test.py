#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib3

import requests

from bs4 import BeautifulSoup

from selenium import webdriver

import time

# https警告解除
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

METHOD_LIST = ['GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE']

CONTENT_TYPE = [
    "text/plain",
    "application/x-www-form-urlencoded",
    "application/json",
]


def _default(method, url, params=None, body=None, headers=None, timeout=10):
    if method.upper() not in METHOD_LIST:
        raise RuntimeError
    if headers and 'application/json' in headers.get('Content-Type') :
        return requests.request(method=method, url=url, params=params, json=body, headers=headers, verify=False,
                                timeout=timeout)
    return requests.request(method=method, url=url, params=params, data=body, headers=headers, verify=False,
                            timeout=timeout)


def _get(url, params, body, headers, timeout=10):
    return _default('GET', url, params, body, headers, timeout=timeout)


def _post(url, params, body, headers, timeout=10):
    return _default('POST', url, params, body, headers, timeout=timeout)


def _put(url, params, body, headers, timeout=10):
    return _default('PUT', url, params, body, headers, timeout=timeout)


def _delete(url, params, body, headers, timeout=10):
    return _default('DELETE', url, params, body, headers, timeout=timeout)


# 选择请求方式
choice = {
    'DEFAULT': _default,
    'GET': _get,
    'POST': _post,
    'PUT': _put,
    'DELETE': _delete,
}

from selenium import webdriver

#显示等待所需的包
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class WebdriverWrap():
    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        '''获取页面和判断'''
        try:
            self.driver.get(url)
        except BaseException:
            pass

    def logcat_of_element(self,*loc):
        #显示等待，捕捉元素
        try:
            element = WebDriverWait(self.driver,10,0.5).until(
                ec.presence_of_element_located(loc)
            )
            return element
        except BaseException:
            print('元素捕捉失败。报错元素：'+str(loc))

    def input_text(self,loc1,loc2,text):
        try:
            self.logcat_of_element(loc1,loc2).clear()
            #显示等待捕捉元素，输入text文本
            self.logcat_of_element(loc1,loc2).send_keys(text)
        except BaseException:
            print('输入文本失败'+str(text))

    def click_element(self,loc1,loc2):
        #显示等待捕捉元素，点击
        self.logcat_of_element(loc1,loc2).click()

    def switch_to_frame(self,loc):
        #切换框架
        self.driver.switch_to.frame(loc)

    def switch_to_default_content(self):
        #切回原来框架
        self.driver.switch_to.default_content()

    def switch_to_window(self,n):
        #切换窗口
        self.driver.switch_to.window(self.driver.window_handles[n])


def login(csrf=None):
    url = 'https://employee.91jkys.com/sso/login?redirect=https://crm-new.91jkys.com'
    # 'https://crm-new.91jkys.com/#/backlog'
    headers = {
        'referer': 'https://employee.91jkys.com/sso/login',
        'origin': 'https://employee.91jkys.com',
        'upgrade-insecure-requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        # 第一次为none
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1'
    }
    params = {
        "redirect": "https://crm-new.91jkys.com",
    }
    body = {
        "name": "heyayun",
        "passwd": "hb123456.",
    }
    if not csrf:
        response = choice.get('GET')(url , params, body, headers, 10)
        print(response.status_code)
        _SESSION_ID = response.cookies.get('_SESSION_ID')
        soup = BeautifulSoup(response.text, 'lxml')
        csrf_token = soup.find('input')['value']

        body['csrf_token'] = csrf
        headers['_SESSION_ID'] = _SESSION_ID
        headers['sec-fetch-site'] = 'same-origin'

        print(_SESSION_ID)
        print(csrf_token)
    time.sleep(3)
    response2 = choice.get('POST')(url, params, body, headers, 10)
    print(response2.status_code)
    print(response2.headers)


def get_cookie():
    cookie = {}
    browser = webdriver.Chrome()
    browserWrap = WebdriverWrap(browser)
    try:
        # 跳转链接
        browserWrap.open_url('https://employee.91jkys.com/sso/login?redirect=https://crm-new.91jkys.com')
        # 登陆
        browserWrap.input_text(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/form/div[1]/div/input', 'heyayun')
        browserWrap.input_text(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/form/div[2]/div/input', 'hb123456.')
        browserWrap.click_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/form/div[3]/button')
        time.sleep(3)
        cookie_list = browserWrap.driver.get_cookies()
        for i in cookie_list:

            key = i.get('name')
            value = i.get('value')
            cookie[key] = value
        return cookie
    except:
        pass
    finally:
        print(cookie)
        browser.quit()

def test_webdriver():
    option = webdriver.ChromeOptions()
    browser = webdriver.Chrome()
    time.sleep(3)
    browser.quit()


if __name__ == '__main__':
    # cookie = get_cookie()
    # headers = {
    #     'referer': 'https://employee.91jkys.com/sso/login',
    #     'origin': 'https://employee.91jkys.com',
    #     'upgrade-insecure-requests': '1',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'zh-CN,zh;q=0.9',
    #     'cache-control': 'max-age=0',
    #     'sec-fetch-dest': 'document',
    #     'sec-fetch-mode': 'navigate',
    #     # 第一次为none
    #     'sec-fetch-site': 'same-origin',
    #     'sec-fetch-user': '?1'
    # }
    # headers = {**headers,**cookie}
    # print(headers)
    # test_webdriver()

    url = 'https://employee.91jkys.com/login?redirect=https%3A%2F%2Fcrm-new.91jkys.com'
    headers = {
    }
    params = {
    }
    body = {
    }
    response = requests.request(method='GET', url=url, params=params, data=body, headers=headers, verify=False,
                     timeout=10)
    print(response.status_code)
    import re
    prefix_features = 'window.CSRF_TOKEN = \''
    suffix_features = '\';'
    str_list = re.findall(prefix_features + '.+?' + suffix_features, response.text)
    csrf_token : str = str_list[0]
    csrf_token = csrf_token.split(prefix_features)[1].split(suffix_features)[0]
    print(csrf_token)