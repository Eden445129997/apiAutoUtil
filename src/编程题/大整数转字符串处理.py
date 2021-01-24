#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 1.生成loan.txt文件（文件数据1000万），文件只有order(订单号）是变量
# 20200317,xm20000000001,20200317,20200317,20200317,,5000,156,01,M,6,1,18,3,1000,1000,1000,10000,20,10,20,10,20,10,15,30,10,15,2,1,0,1
# 2.生成open.txt,文件里的order与loan.txt一样，cerno是身份证，只要18位数就可以
# 20200317,XIAOMI,zhangsan,test01,01,120115199612000000001,xm20000000001,20200317,20200317,20220316,62170000007898,xm20316000001,5000,156,个人日常消费,01,M,6,3,1

dump_int = 100000
dump_int2 = 10000

file_dir = os.path.dirname(os.path.abspath(__file__))

loan_file_name = "loan.txt"
loan_file_path = os.path.join(file_dir, loan_file_name)

open_file_name = "open.txt"
open_file_path = os.path.join(file_dir, open_file_name)

while True:
    dump_int = dump_int+1
    dump_str = str(dump_int)[1:]

    dump_str2 = str(dump_int2)[1:]

    loan_txt = '20200317,xm20%s%s,20200317,20200317,20200317,,5000,156,01,M,6,1,18,3,1000,1000,1000,10000,20,10,20,10,20,10,15,30,10,15,2,1,0,1\n'%(dump_str2,dump_str)
    # print(loan_txt)

    open_txt = "20200317,XIAOMI,zhangsan,test01,01,120115199612%s%s,xm20%s%s,20200317,20200317,20220316,62170000007898,xm20316000001,5000,156,个人日常消费,01,M,6,3,1\n"%(dump_str2,dump_str,dump_str2,dump_str)

    try:
        with open(loan_file_path,'a+',encoding='utf-8') as f:
            f.write(loan_txt)
    except:
        break

    try:
        with open(open_file_path,'a+',encoding='utf-8') as f:
            f.write(open_txt)
    except:
        break

    # if dump_str == "00099":
    #     break

    if dump_str == "99999":
        dump_int2 = dump_int2 + 1
        dump_int = dump_int -99999
        print(dump_int2)

    if dump_str2 == "0001":
        break


