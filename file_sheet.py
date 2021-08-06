# -*- coding: utf-8 -*-

import os
import xlrd
import xlwt


def deal_file(file):
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet(sheetname="0")  # 设置sheet名称
    book = xlrd.open_workbook(file)
    table = book.sheets()[0]
    for col in range(0, table.ncols):  # 写首行的标题
        worksheet.write(0, col, table.row_values(0)[col])
    j = 1
    for index in range(0, len(book.sheets())):
        table = book.sheets()[index]
        n_rows = table.nrows
        n_cols = table.ncols
        for i in range(1, n_rows):  # 循环写入内容
            if table.row_values(i)[2] == "":
                continue
            for col in range(1, n_cols):
                worksheet.write(j, col, table.row_values(i)[col])
            j = j + 1
    workbook.save("save.xls")


if __name__ == "__main__":
    deal_file("./汇总表.xlsx")
