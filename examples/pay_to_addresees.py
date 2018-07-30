# -*- coding:utf-8 -*-
# 该模块给出了一个单线程发币的例子，多线程发币见 ***

import CONSTANT
from wrapper.client import Client

# 定义一个发币端
seed=CONSTANT.SEED
client=Client(private_key=seed)
# 定义一个收币端，of Client
destination=Client(address='GBM3XODY6XQJAORQA5KG77HQ2POB4UBU4G2SBEDYI77UZDDKIZLXYEFF')
# 发币
client.pay_to(destination.address, 25.8369)