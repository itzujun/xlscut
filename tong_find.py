import pandas as pd


def isIn(data, src):
    for i in range(len(data)):
        data1 = str(data[i]).replace(" ", "")

        # temp = str(src).replace(" ", "")
        # data2 = temp.replace("'", "")

        # data2 = "".format("%f", src)

        print("data1: ", data1)
        print("data2: ", data2)
        print("src", type(src))
        return False
        if data1 == data2:
            return True
    return False


if __name__ == "__main__":
    df = pd.read_excel("chongqing.xlsx", header=0)
    li1 = list(df["支付平台"])

    

    pass
