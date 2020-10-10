
import pandas as pd


def deal_file(file_path):
    temp = pd.read_csv(file_path, sep='|')
    return temp.iloc[0:temp.shape[0]]


if __name__ == "__main__":
    file_name = "save-202009"
    data = deal_file(file_name + ".txt")

    data["订单编号"] = data["订单编号"].fillna(-1)
    data["订单编号"] = data["订单编号"].astype("int64")

    data["药品订单号"] = data["药品订单号"].fillna(-1)
    data["药品订单号"] = data["药品订单号"].astype("int64")

    data.to_excel(file_name + ".xlsx", index=False)
