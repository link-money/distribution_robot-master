# -*- coding: UTF-8 -*-

import CONSTANT
from wrapper import client
from wrapper import builder as BUILDER
import time
from tools import load_json

# 0. 初始化Client实例
constant=CONSTANT.Constant('local')
client=client.Client(constant.SEED,api_server=constant.API_SERVER)



# 1. 产生100个密钥对
from wrapper import keypair

keypairs=[]
keypairs=load_json.file2json('keys.json')[0:100]

while True:
    # 2. 将LINK资产等量的分发给这100个账户
    builder = BUILDER.Builder(secret=constant.SEED)
    for keypair in keypairs:
        address=keypair['public_key']
        print(address)
        builder.append_payment_op(destination=address, amount=1, asset_type='LINK', asset_issuer=constant.ISSUER_ADDRESS)
    builder.sign()
    builder.submit()
    time.sleep(5)