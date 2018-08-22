# -*- coding:utf-8 -*-
# 该模块给出了一个单线程发币的例子，多线程发币见 ***

import CONSTANT
from wrapper.client import Client
from tools import load_json

constant=CONSTANT.Constant('test')

# 定义一个发币端
seed=constant.SEED
client=Client(private_key=constant.SEED, api_server=constant.API_SERVER)
# 定义一个收币端，of Client
destination=Client(address=constant.DISTRIBUTOR_ADDRESS)
# 发币
keys=load_json.file2json('keys.json')[102:103]

for keypair in keys:
    client.pay_to(constant.DISTRIBUTOR_ADDRESS,1000000)
    # client.pay_to(keypair['public_key'], 800, asset_code='LINK', asset_issuer=constant.ISSUER_ADDRESS)

