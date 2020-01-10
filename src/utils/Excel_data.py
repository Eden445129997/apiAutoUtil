#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd
from config import path
from src.utils.Log import log

class get_data():
    def __init__(self,filename,file_suffix=".xls"):
        self.filename = filename + file_suffix
        self.log = log()
        
    def connect_excel(self):
        """建立cxcel连接对象"""
        try:
            # 创建excel文件对象
            __wb = xlrd.open_workbook(path.dataPath()+self.filename)
            return __wb
        except:
            self.log("读取excel失败:%s%s"%(path.dataPath(),self.filename))
            return None

    def get_rows(self,tag_name,row_number):
        # 根据页签和行号获取数据
        wb = self.connect_excel()
        if wb:
            try:
                # 创建页签对象
                sheet = wb.sheet_by_name(tag_name)
                # 获取该sheet中的有效行数
                nrows = sheet.nrows
                # 如果传入的行号小于有效行数，则返回数据
                if row_number < nrows:
                    # 根据行号获取数据
                    row = sheet.row_values(row_number,start_colx=0,end_colx=None)
                    return row
                else:
                    self.log.error("不是有效行：get_rows(%s)"%row_number)
                    return None
            except BaseException:
                self.log.error('数据获取失败')

    def get_columns(self,tag_name,column_number):
        # 根据页签和列号获取数据
        wb = self.connect_excel()
        if wb:
            try:
                # 创建页签对象
                sheet = wb.sheet_by_name(tag_name)
                # 获取该sheet中的有效列数
                ncols = sheet.ncols
                # 如果传入的行号小于有效行数，则返回数据
                if column_number < ncols:
                    # 根据列号获取数据
                    row = sheet.col_values(column_number,start_rowx=1,end_rowx=None)
                    return row
                else:
                    self.log.error("不是有效列：get_columns(%s)"%column_number)
                    return None
            except BaseException:
                self.log.error('数据获取失败')

    def get_cell(self,tag_name,row_number,column_number):
        # 根据页签的行号和列获取具体值
        wb = self.connect_excel()
        if wb:
            try:
                # 创建页签对象
                sheet = wb.sheet_by_name(tag_name)

                # 获取该sheet中的有效行数
                nrows = sheet.nrows
                # 获取该sheet中的有效列数
                ncols = sheet.ncols

                # 如果传入的行号小于有效行数，则返回数据
                if row_number < nrows and column_number < ncols:
                    # 根据行号获取数据
                    row = sheet.cell_value(row_number,column_number)
                    return row
                else:
                    self.log.error("不是有效行,不是有效的列：get_cell(%s,%s)"%row_number,column_number)
                    return None

            except BaseException:
                self.log.error('数据获取失败')

if __name__ == '__main__':
    excel = get_data('user')
    # 获取行
    data = excel.get_rows('user_login',1)
    print(data)
    # 获取列
    data = excel.get_columns('user_login',1)
    print(data)
    # 获取单元格
    data = excel.get_cell('user_login',1,1)
    print(data)
