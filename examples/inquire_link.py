# -*- coding: UTF-8 -*-
# 该模块给出了一个查询账户联金的例子

import CONSTANT
from wrapper.client import Client

# 定义一个client，实际上也可以不定义，但通用方法，先定义一个client
seed=CONSTANT.SEED
client=Client(private_key=seed)

# 临时定义一个遍历balaneces列表的方法，用于查询联金数量
def get_link(balances):
    if not balances:
        return 0
    balance=0
    for item in balances:
        item=dict(item)
        if item.has_key('asset_code') and  item['asset_code']=='LINK' and item['asset_issuer']=='GCHZDZXYLZ76XADS7735LK3OJUFZ2TBSXAR23YXKXCXXHUEEVT5C37PY':
            balance=item['balance']
            return balance
        else:
            return 0

# 查询任意一个地址的所有信息：
balance_of_link=get_link(client.get_balances('GA4OP7NMIWWLKSCIXRYKVQC5L36OPIJHDYKW25EF5BWSR3P2MOHY4REZ'))
print(balance_of_link)
balance_of_link=get_link(client.get_balances('GAFRGA77FLN4JIWG7P7TXUDS5RX2475V5CTVKQJOFMXKBE5AJ25I6HRA'))
print(balance_of_link)
balance_of_link=get_link(client.get_balances())
print(balance_of_link)


