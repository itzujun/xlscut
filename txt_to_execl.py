# import pandas as pd
import xlwt

if __name__ == "__main__":
    file_name = "save-202009"
    file = open(file_name + ".txt")
    workbook = xlwt.Workbook(encoding='utf-8')
    book_sheet = workbook.add_sheet('Sheet1', cell_overwrite_ok=True)

    row = 0
    for line in file:
        data = line.split("|")
        if len(data) == 11:
            data.insert(7, "-")
        for col in range(len(data)):
            if data[col] == "":
                data[col] = "0"
            book_sheet.write(row, col, data[col])
        row = row + 1

    workbook.save(file_name + ".xlsx")
    file.close()
