# -*- coding:utf-8 -*-

import CONSTANT
from wrapper import keypair
from wrapper.client import Client

seed=CONSTANT.SEED
client=Client(seed,api_server='test')
destination=keypair.Keypair.random()
address=destination.address().decode().encode('ascii')
client.fund(destination=address,amount=30)
