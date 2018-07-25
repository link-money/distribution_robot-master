# -*- coding:utf-8 -*-

import sqlite3

from wrapper.client import Client

seed='SDSSWWPCGGRDB6SVVOJUWFQ3ODQFX62GVTKCPELNULO5PXVCFE67L7HO'
client=Client(seed,api_server='test')

# 连接sqlite
conn = sqlite3.connect('/home/cc5985/key_pairs.db')
cursor=conn.cursor()
sql_str='select * from key_pairs_2018_3_17'
data = cursor.execute(sql_str).fetchall()



cnt=0
for line in data:
    if cnt>=100:
        break
    address=str(line[2])
    client.fund(destination=address,amount= 1000000000-0.00001)
    cnt+=1

print "Operation done successfully";
conn.close()
