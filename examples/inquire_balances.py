# -*- coding: UTF-8 -*-
# 该模块给出了一个查询账户余额列表的例子

import CONSTANT
from wrapper.client import Client


def inquire():
    # 定义一个client，实际上也可以不定义，但通用方法，先定义一个client
    seed=CONSTANT.SEED
    client=Client(private_key=seed, api_server=CONSTANT.API_SERVER)
    # 查询任意一个地址的所有信息：
    balances=client.get_balances('GAFRGA77FLN4JIWG7P7TXUDS5RX2475V5CTVKQJOFMXKBE5AJ25I6HRA')[0]['balance']
    print(balances)
    balances=client.get_info('GCHZDZXYLZ76XADS7735LK3OJUFZ2TBSXAR23YXKXCXXHUEEVT5C37PY')
    print(balances)
    balances=client.get_info()
    print(balances)

def inquire_accounts_in_key_dot_json():
    seed = CONSTANT.SEED
    client = Client(private_key=seed, api_server=CONSTANT.API_SERVER)
    import tools.load_json
    keys=tools.load_json.file2json('keys.json')[0:1]
    for key in keys:
        address=key['public_key']
        balance=client.get_balances(address)[0]['balance']
        print("%s\t%s" % (address,balance))

if __name__=='__main__':
    inquire_accounts_in_key_dot_json()