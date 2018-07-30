# -*- coding:utf-8 -*-

from wrapper.address import *
import CONSTANT

# 生成随机密钥对，并获得该密钥对的公私钥
key_pair=Keypair.random()
secret_key=key_pair.seed().decode().encode('ascii')
address=key_pair.address().decode().encode('ascii')
print("secret key：%s\npublic key：%s" % (secret_key,address))


# 根据随机字符数组产生密钥对
key_pair=Keypair.deterministic('illness spike retreat truth genius clock brain pass fit cave bargain toe')
secret_key=key_pair.seed().decode().encode('ascii')
address=key_pair.seed().decode().encode('ascii')

# 根据原始私钥生成密钥对
seed=CONSTANT.SEED
key_pair=Keypair.from_seed(seed)
secret_key=key_pair.seed().decode().encode('ascii')
address=key_pair.seed().decode().encode('ascii')
a=1
