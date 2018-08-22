# -*- coding:utf-8 -*-
# 该模块给出了一个单线程发币的例子，多线程发币见 ***

import CONSTANT
from wrapper.client import Client
from tools import load_json

constant=CONSTANT.Constant('local')

# trustee
trustee=constant.ISSUER_ADDRESS
keys=load_json.file2json('keys.json')[102:103]
for keypair in keys:
    client=Client(private_key=keypair['private_key'], api_server=constant.API_SERVER)
    client.trust(constant.ISSUER_ADDRESS,'LINK', 1000)


