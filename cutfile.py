# -*- coding: utf-8 -*-

import os
import xlrd
import xlwt
import pandas as pd

readbook = "E:\\hua.xls"  # 原始文件路径
savebook = "E:\\files"  # 要保存的目录


def hx_file():
    limit = 1000
    if not os.path.exists(readbook):
        print("源文件不存在" + readbook)
        return
    book = xlrd.open_workbook(readbook)
    table = book.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    sheets = nrows / limit
    if not sheets.is_integer():
        sheets = sheets + 1
    title_row = table.row_values(0)
    if not os.path.exists(savebook):
        os.makedirs(savebook)
        print("创建文件夹:" + savebook)
    for i in range(0, int(sheets)):
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet(sheetname="0")  # 设置sheet名称
        for col in range(0, ncols):  # 写首行的标题
            worksheet.write(0, col, title_row[col])
        for row in range(1, limit + 1):  # 每次循环limit行
            newRow = row + limit * i
            if newRow < nrows:
                row_content = table.row_values(newRow)
                for col in range(0, ncols):
                    worksheet.write(row, col, row_content[col])
        print("save:" + savebook + "\\" + "huaxia" + str("%02d" % (i + 1)) + ".xls")
        workbook.save(savebook + "\\" + "huaxia" + str("%02d" % (i + 1)) + ".xls")


# 利用pandas 分割xls文件
def pd_cut_xls():
    if not os.path.exists(readbook):
        print("源文件不存在:" + readbook)
        return
    limit = 1000  # 每个文件容纳多少条记录控制
    data_xls = pd.read_excel(readbook)
    df = pd.DataFrame(data_xls)
    for key in df.keys():
        df[key] = df[key].astype("str")
    nums = len(data_xls.index)
    books = nums / limit
    if not books.is_integer():
        books = int(books) + 1
    for i in range(books):
        start = i * limit
        end = min([(i + 1) * limit, nums])
        data = df.iloc[start: end]
        print("save: " + savebook + "\\" + "hua" + str("%02d" % (i + 1)) + ".xls")
        data.to_excel(savebook + "\\" + "hua" + str("%02d" % (i + 1)) + ".xls", index=False)
    print("转换结束")


if __name__ == "__main__":
    pd_cut_xls()
    pass
