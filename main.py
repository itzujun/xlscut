#  _*_ coding:utf-8  _*_

import pandas as pd

import numpy as np


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
    print(round(101.25 * 0.004, 2))
    pass
