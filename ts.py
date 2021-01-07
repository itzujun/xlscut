import tushare as ts
import os
import argparse

ts.set_token('53c96c569abe3baa2828835684f2c1ef539067725fb89d61d9253088')
pro = ts.pro_api()

data = pro.stock_basic(list_status='L')
code_list = data['ts_code'].values
print('code_list', code_list)
i = 0

parser = argparse.ArgumentParser(description='Personal information')
parser.add_argument('-code', dest='code', type=str, help='Name of the candidate')

args = parser.parse_args()
print("code----", args.code)

for now_code in code_list:
    if (args.code is not None) and (str(now_code).__contains__(args.code) is False):
        continue
    print("find it", now_code)
    print(now_code)
    file_name = '%s.xlsx' % now_code
    df = ts.pro_bar(ts_code=now_code, adj='qfq')
    df.to_excel(file_name)
    pass
