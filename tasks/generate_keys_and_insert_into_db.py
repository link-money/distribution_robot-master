# -*- coding: UTF-8 -*-

import os
import CONSTANT1
from wrapper import db as DB
import requests

NUMBER=CONSTANT1.NUMBER_OF_ACCOUNTS
TABLE_NAME=CONSTANT1.TABLE_NAME


path=os.getcwd()
DB_NAME=TABLE_NAME

# 构造sql_manager： 这个实例用于操纵数据库操作
my_pgmanager=DB.PGManager(**CONSTANT1.DB_CONNECT_ARGS_TEST)

# 构造表结构：
# 私钥|公钥|起始数量|起始时间|是否激活
create_table_sql='create table ' + TABLE_NAME + '(id SERIAL primary key ,user_token varchar(32),private_key varchar(128) not null,public_key varchar(128) not null , starting_balance decimal , starting_time bigint, is_activated int )'
create_table_sql={'sql':create_table_sql}

# post the create table function
res=requests.post(CONSTANT1.BASE_URL + '/link/api/call/run/create_table', create_table_sql, verify=False)
print(res.text)

# 如果表上已经有记录了，那么就跳过这个过程：
sql='select count(*) from public.' + TABLE_NAME
rows=my_pgmanager.select(sql)
if rows.count>0:
    if rows[0][0]>=NUMBER:
        pass
    else:
        sqls= []
        number=NUMBER-rows[0][0]  # 待生成的私钥数量
        # 生成NUMBER-rows[0][0]个密钥对
        from tasks import key_generation

        keypairs= key_generation.generate_keypairs(number,'','',True)

        a=1
        # 将这10000个密钥对存入数据库
        for keypair in keypairs:
            sqls.append({'private_key':keypair[0],'public_key':keypair[1]})
        my_pgmanager.execute_many('insert into ' + TABLE_NAME + '(private_key,public_key) values(%(private_key)s,%(public_key)s)',sqls)

my_pgmanager.close()
