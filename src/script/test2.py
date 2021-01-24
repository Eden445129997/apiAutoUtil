#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

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


prefix_features = 'window.CSRF_TOKEN = \''
suffix_features = '\';'
str_list = re.findall(prefix_features + '.+?' + suffix_features, response.text)
csrf_token: str = str_list[0]
csrf_token = csrf_token.split(prefix_features)[1].split(suffix_features)[0]
print(csrf_token)