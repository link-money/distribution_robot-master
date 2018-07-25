# -*- coding: UTF-8 -*-

import os
import CONSTANT
from wrapper import db as DB

NUMBER=CONSTANT.NUMBER_OF_ACCOUNTS
TABLE_NAME=CONSTANT.DB_NAME


path=os.getcwd()
DB_NAME=path+TABLE_NAME

# 构造sql_manager： 这个实例用于操纵数据库操作
my_sql_manager=DB.SQLManager(DB_NAME)

# 构造表结构：
# 私钥|公钥|起始数量|起始时间|是否激活
column1=DB.Column("private_key","TEXT",False,None,False)
column2=DB.Column("public_key","TEXT",False,None,False)
column3=DB.Column("starting_balance","REAL",True,None,False)
column4=DB.Column("starting_time","BIGINT",True,None,False)
column5=DB.Column("activated","BOOLEAN",True,None,False)
columns=[]
columns.extend([column1,column2,column3,column4,column5])

# 构造表：
table=DB.Table(TABLE_NAME,columns)
print(table.create_table_sql)

# 在介质上创建表
my_sql_manager.execute(table.create_table_sql)

# 如果表上已经有记录了，那么就跳过这个过程：
rows=my_sql_manager.execute('select count(*) from keys')
if rows.count>0:
    if rows[0][0]>=NUMBER:
        pass
    else:
        number=NUMBER-rows[0][0]  # 待生成的私钥数量
        # 生成NUMBER-rows[0][0]个密钥对
        from tasks import distribution_key_generation

        keypairs= distribution_key_generation.main(number)

        # 将这10000个密钥对存入数据库
        my_sql_manager.execute_many("insert into " + TABLE_NAME + "(private_key,public_key) values(?,?)",keypairs)

