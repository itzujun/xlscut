import pandas as pd

if __name__ == "__main__":
    df = pd.read_excel("易支付.xlsx")
    print("保存中...")
    df.to_csv("易支付.csv", encoding="utf-8")
    print("保存success")
