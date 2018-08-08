# -*- coding:utf-8 -*-
# 该模块给出了一个单线程发币的例子，多线程发币见 ***

import CONSTANT
from wrapper.client import Client

# 定义一个发币端
seed=CONSTANT.SEED
client=Client(private_key=seed, api_server=CONSTANT.API_SERVER)
# 定义一个收币端，of Client
destination=Client(address='GAFRGA77FLN4JIWG7P7TXUDS5RX2475V5CTVKQJOFMXKBE5AJ25I6HRA')
# 发币
client.pay_to(destination.address, 25.8369)

