# from src.demo import testCode2
import re
#
# print(testCode2.__name__)
#
# print(5000+1434+4606-300-1500+4606+841+2159+4606)
#
# print(1789.41+4606)
#
# s = ''.join(map(str,range(0,1000)))
# print(s)
#
# print('service_impl_file_suffix'.upper())
#
#
# testaaaa = "a:aaabbbb?s=1"
# print(testaaaa[testaaaa.find(':'):])
#
# string = '(a,b,c)'
# search_list = re.findall('[A-Za-z]',string)
# print(search_list)
#
# print('(',end='')
# for i in range(len(search_list)):
#     for j in range(len(search_list)):
#         for x in range(len(search_list)):
#             if i!=j and i!=x and j!=x:
#                 print("%s%s%s"%(search_list[i],search_list[j],search_list[x]),end='')
#                 print(',',end='')
# print(')')
#
#
# print(4096/4)

import json
# string = 'test string'
# string = '{"哈哈哈": 12}'
# string = '{\'哈哈哈\': 12}'
# string = {}
string = '''{
	'assert_method': 'assertEqual',
	'assert_obj': {
		'path': '/testapi/',
		'method': 'GET',
		'contentType': 'text/plain',
		'queryString': '',
		'queryJson': {
            'a': '{{aaaasdfsdfsfsf}}',
            'b': '{{ $.. | \\'1\\' }}',
            'c': '${ test | 2 }'
		},
		'body': ''
	}
}
'''.replace('\'','\"')

print(string)
# 字符串转字典
string_json = json.loads(string)
# 字典转字符串
# string_json = json.dumps(string,ensure_ascii=False)

print(type(string_json))
print(string_json)

# print(string_json.get('assert_obj').get('queryJson'))
print(type(string_json.values()))
print(list(string_json.values()))

# '\$.*?&\d+?#'
# result = re.findall('"\{\{.*?\}\}"', string)
result = re.findall('"\$\{.*?\}"', string)
a,b = result[0].split('|')
# print(a[3:],b[:-2])

print(re.findall('\d', b))

# 先找到字符串："{{ $.. ｜ 0 }}"
# 将{{}}字符串去掉
# 字符串从 ｜ 分割
# 分割后的数组，索引0字符串前后去空格，索引1直接正则获取数字
# 索引1找到对应节点，索引0捕捉元素

print(re.findall(r'(?![a-zA-Z])(\d{1,2})', '5555'))

print(int('aaa'))