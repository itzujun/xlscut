import os
import pandas as pd


def read_file(path):
    return os.listdir(path)


def deal_file(file_path):
    temp = pd.read_csv(file_path, sep='|')
    return temp.iloc[0:temp.shape[0]]


if __name__ == "__main__":
    dir = "./file"
    files = read_file(dir)
    files.sort()

    path = dir + "/" + files[0]
    temp = pd.read_csv(path, sep='|')
    rowNum = temp.shape[0]
    data = temp.iloc[0:rowNum]
    print("完成" + path)

    for i in range(1, len(files)):
        path_i = dir + "/" + files[i]
        temp = pd.read_csv(path_i, sep='|')
        rowNum = temp.shape[0]
        data = data.append(temp.iloc[0:rowNum])
        print("完成" + path_i)

    data['云商通订单号'] = data['云商通订单号'].astype(str)
    data['渠道流水号'] = data['渠道流水号'].astype(str)

    data['交易金额(单位:分)'] = round(data['交易金额(单位:分)'] / 100, 2)
    data.rename(columns={"交易金额(单位:分)": "交易金额(单位:元)"}, inplace=True)

    data['手续费金额(单位:分)'] = round(data['手续费金额(单位:分)'] / 100, 2)
    data.rename(columns={"手续费金额(单位:分)": "手续费金额(单位:元)"}, inplace=True)

    data['云商通手续费(单位:分)'] = round(data['云商通手续费(单位:分)'] / 100, 2)
    data.rename(columns={'云商通手续费(单位:分)': "云商通手续费(单位:元)"}, inplace=True)

    data['分期金额(单位:分)'] = round(data['分期金额(单位:分)'] / 100, 2)
    data.rename(columns={'分期金额(单位:分)': "分期金额(单位:元)"}, inplace=True)

    data['持卡人手续费(单位:分)'] = round(data['持卡人手续费(单位:分)'] / 100, 2)
    data.rename(columns={'持卡人手续费(单位:分)': "持卡人手续费(单位:元)"}, inplace=True)

    data['预付卡交易金额(单位:分)'] = round(data['预付卡交易金额(单位:分)'] / 100, 2)
    data.rename(columns={'预付卡交易金额(单位:分)': "预付卡交易金额(单位:元)"}, inplace=True)

    data['渠道金额'] = round(data['渠道金额'] / 100, 2)

    print("生成execl...")
    data.to_excel("save_tong_lian" + files[0][0:6] + ".xlsx", index=False)
    print("生成完成")
