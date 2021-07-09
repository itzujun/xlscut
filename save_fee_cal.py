#  _*_ coding:utf-8  _*_

import pandas as pd

if __name__ == "__main__":
    file_name = "save-202106.xlsx"
    df = pd.read_excel("./files/" + file_name)

    df["收入/支出"] = df["收入/支出"].astype(float)
    df['手续费'] = df['手续费'].astype(float)

    print("微信收款手续费:", "")

    df1 = df.loc[(df['订单类型'] == "收款") & (df['支付方式'] == "微信公众号")]
    print("微信收款:", df1["收入/支出"].sum())
    print("微信收款手续费:", df1["手续费"].sum())

    df1 = df.loc[(df['订单类型'] == "退款") & (df['支付方式'] == "微信公众号")]
    print("微信退款:", df1["收入/支出"].sum())
    print("微信退款手续费:", df1["手续费"].sum())

    print("# ---------- 快捷 ---------- #")

    df1 = df.loc[(df['订单类型'] == "收款") & (df['支付方式'] == "快捷支付")]
    print("快捷支付收款:", df1["收入/支出"].sum())
    print("快捷支付收款手续费:", df1["手续费"].sum())

    df1 = df.loc[(df['订单类型'] == "退款") & (df['支付方式'] == "快捷支付")]
    print("快捷支付退款:", df1["收入/支出"].sum())
    print("快捷支付退款手续费:", df1["手续费"].sum())

    print("# ---------- 提现手续费 ---------- #")
    df1 = df.loc[(df['订单类型'] == "提现")]
    print("提现手续费:", df1["手续费"].sum())
