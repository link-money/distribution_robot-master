# -*- coding: UTF-8 -*-
# 该模块给出了一个查询账户余额列表的例子

import CONSTANT
from wrapper.client import Client

# 定义一个client，实际上也可以不定义，但通用方法，先定义一个client
seed=CONSTANT.SEED
client=Client(private_key=seed)
# 查询任意一个地址的所有信息：
balances=client.get_balances('GA4OP7NMIWWLKSCIXRYKVQC5L36OPIJHDYKW25EF5BWSR3P2MOHY4REZ')
print(balances)
balances=client.get_info('GAFRGA77FLN4JIWG7P7TXUDS5RX2475V5CTVKQJOFMXKBE5AJ25I6HRA')
print(balances)
balances=client.get_info()
print(balances)
