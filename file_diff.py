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

    out1 = set(df1).difference(df2)
    out2 = set(df2).difference(df1)

    new_list1 = find_diff(list(df1), out1)
    new_list2 = find_diff(list(df2), out2)

    data.loc[:, "收入差异"] = new_list1
    data.loc[:, "支出差异"] = new_list2
    data.to_excel("new_" + file_name + ".xlsx", index=False)
