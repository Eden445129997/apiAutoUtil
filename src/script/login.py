# -*- coding: utf-8 -*-

import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re

s = requests.session()

pro_csrf_url = 'https://employee.91jkys.com/login?redirect=https%3A%2F%2Fcrm-new.91jkys.com'
pro_login_url = 'https://employee.91jkys.com/api/login'

csrf_url = pro_csrf_url
login_url = pro_login_url

def get_csrftoken():
    '''获取csrf_cookie'''
    #  loginUrl = "https://employee.qa.91jkys.com/api/login"
    headers = {
    }
    params = {
    }
    body = {
    }

    response = s.get(url=csrf_url, params=params, data=body, headers=headers, verify=False, timeout=10)

    prefix_features = 'window.CSRF_TOKEN = \''
    suffix_features = '\';'
    str_list = re.findall(prefix_features + '.+?' + suffix_features, response.text)
    csrf_token: str = str_list[0]
    csrf_token = csrf_token.split(prefix_features)[1].split(suffix_features)[0]

    return csrf_token

def zhiyun_login():
    '''登陆'''
    csrf_token = get_csrftoken()
    print('csrf_token:' + csrf_token)

    headers1 = {
        "content-type": "pplication/json",
        "referer": "https://employee.qa.91jkys.com/login?redirect=https%3A%2F%2Fcrm-new.qa.91jkys.com",
        # "csfr_token":csrf_token
    }
    headers1['csrf_token'] = csrf_token
    body1 = {
        "username": "heyayun",
        "passwd": "hb123456."
    }

    response = s.post(url=login_url, data=body1, headers=headers1, verify=False, timeout=10)
    print('登陆状态码：%s'%response.status_code)
    print("登陆之后的cookies:%s"%s.cookies.__dict__)
    print(response.headers)
    return s.cookies.__dict__

def crmdrugstore_hzPartySites_main_save():
    save = "https://crm-new.91jkys.com/api/crmdrugstore/hzPartySites/main/save"
    # save = 'https://crm-new.91jkys.com/api/sys/window/window_config/7'
    headers2= {
            "content-type": "application/json;charset=UTF-8",
            # "referer": "https://employee.91jkys.com/login?redirect=https%3A%2F%2Fcrm-new.91jkys.com",
            'referer': 'https://crm-new.91jkys.com/',
            #"csfr_token":csrf_token
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "cookie" : "_JKYS_E_SESSION_ID=43253297e4ae343518e61a07351c699d482aacae; JSESSIONID=7A6BA69864EF35F2EDF6D893B142A6AE",
            'Set-Cookie': '_JKYS_E_SESSION_ID=43253297e4ae343518e61a07351c699d482aacae; JSESSIONID=7A6BA69864EF35F2EDF6D893B142A6AE'

        }
    #headers1['csrf_token'] = csrf_token
    body2 = {
         "name": "自动化测试2", "address": "1", "contactInfoDOList": [{"editable": 'true', "contactPerson": "汉堡", "contactTelphone": "17786304092", "kpType": "null","modifyUserName": "null"}], "province": 1, "city": 35, "district": "null", "createUser": 3297
    }

    response2 = requests.get(url=save, data=body2, headers=headers2, verify=False,timeout=10)
    print(response2.status_code)

    #print("登陆之后的cookies:", s.cookies)
    print(response2.text)
    print(response2.headers)

if __name__=="__main__":
    cookie_dict = zhiyun_login()
    print(cookie_dict)
    # crmdrugstore_hzPartySites_main_save()




















































































