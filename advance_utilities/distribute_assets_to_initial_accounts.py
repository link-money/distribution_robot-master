# -*- coding: UTF-8 -*-

import CONSTANT
from wrapper import client
from wrapper import builder

# 0. 初始化Client实例
client=client.Client(CONSTANT.SEED,api_server=CONSTANT.API_SERVER)
builder=builder.Builder(secret=CONSTANT.SEED)

# 1. 产生100个密钥对
from wrapper import keypair

keypairs=[]
for i in range(10):
    keypairs.append(keypair.Keypair.random())

# 2. 将资产等量的分发给这100个账户，其中最后一个账户拿的资产略微少一点
for keypair in keypairs:
    address=keypair.address().decode()
    print(address)
    builder.append_create_account_op(destination=address, starting_balance=20)
builder.sign()
builder.submit()