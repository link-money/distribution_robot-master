# -*- coding:utf-8 -*-

import sqlite3
from wrapper.address import *
from wrapper.encryption import *

# global variables:
__key,__iv=generate_random_key_pair()
f=open('../test.test', 'w')
f.write('key:' + __key + '\niv:'+ __iv)
f.close()
pc = prpcrypt(__key, __iv)  # 初始化密钥 和 iv
# 连接sqlite
conn = sqlite3.connect('/home/cc5985/key_pairs.db')
cursor=conn.cursor()


for cnt in range(0,10000):
    # 1. generate 10000 secret keys and corresponding addresses
    key_pair=Keypair.random()
    secret_key=key_pair.seed().decode()
    address=key_pair.address().decode()



    # 2. encrypt the secret keys
    cipher_text = pc.encrypt(secret_key)  # 加密


    # 3. write the cipher_text into sqlite3 database
    sql_str='insert into key_pairs_2018_3_17 values(NULL,"' + cipher_text + '","' + address +'")'
    cursor.execute(sql_str)



conn.commit()
print('success')
# 4. transfer money to the addresses



