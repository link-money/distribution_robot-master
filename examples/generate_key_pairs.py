# -*- coding:utf-8 -*-

from wrapper.address import *
import CONSTANT

def generate_random_keypai():
    # 生成随机密钥对，并获得该密钥对的公私钥
    key_pair=Keypair.random()
    secret_key=key_pair.seed().decode().encode('ascii')
    address=key_pair.address().decode().encode('ascii')
    print("secret key：%s\npublic key：%s" % (secret_key,address))

def generate_keypair_from_words():
    # 根据随机字符数组产生密钥对
    key_pair=Keypair.deterministic('hello my name is ')
    secret_key=key_pair.seed().decode().encode('ascii')
    address=key_pair.seed().decode().encode('ascii')

# # 根据原始私钥生成密钥对
# seed=CONSTANT.SEED
# key_pair=Keypair.from_seed(seed)
# secret_key=key_pair.seed().decode().encode('ascii')
# address=key_pair.seed().decode().encode('ascii')
# a=1

if __name__=='__main__':
    flag=False
    cnt=0
    while flag==False:
        keypair=Keypair.random()
        address=keypair.address().decode().encode('ascii')
        if address[-4]==('LINK'):
            print(address)
        cnt+=1
        if cnt%100==0:
            print(cnt)