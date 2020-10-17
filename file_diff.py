#  _*_ coding:utf-8  _*_

import pandas as pd


def find_diff(data1, data2):
    resp = []
    for d in data1:
        if d in data2:
            resp.append(d)
            data2.remove(d)

        else:
            resp.append(0)
    return resp


def list_sub(data1, data2):
    dt1 = data1.copy()
    dt2 = data2.copy()
    resp = []
    for i in range(len(dt1)):
        if dt1[i] in dt2:
            resp.append(0)
            dt2.remove(dt1[i])
        else:
            resp.append(dt1[i])
    return resp


if __name__ == "__main__":
    file_name = "DEMO-差异"
    data = pd.read_excel(file_name + ".xlsx", header=0)

    rowNum = data.shape[0]
    data = data.iloc[0:rowNum]

    for index, rows in data.iterrows():
        for i in range(len(rows)):
            if isinstance(rows[i], str) and rows[i] == "":
                data.iloc[index, i] = "-"
            if isinstance(rows[i], float) and rows[i] == 0:
                data.iloc[index, i] = 0

    df1 = data["收入"]
    df2 = data["支出"]

    out1 = list_sub(list(df1), list(df2))
    out2 = list_sub(list(df2), list(df1))

    list_3 = find_diff(list(df1), out1)
    list_4 = find_diff(list(df2), out2)

    data.loc[:, "收入差异"] = list_3
    data.loc[:, "支出差异"] = list_4
    data.to_excel("new_" + file_name + ".xlsx", index=False)
