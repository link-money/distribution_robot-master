# -*- coding: UTF-8 -*-
# 要精确控制每个账户的初始币总量还需要进行一些微小的计算。。。
# 不过我觉得没必要精确控制每个账户的初始币总量，反正加一起是恒定的

STARTING_BALANCE=4304172604
starting_balance=STARTING_BALANCE

from wrapper import db as DB
from wrapper import client as Client
import threading
import CONSTANT1


DB_NAME=CONSTANT1.DB_NAME

# 构造sql_manager： 这个实例用于操纵数据库操作
my_sql_manager=DB.SQLManager(DB_NAME)

# 思路：
# 读取第n+1到2n共n行，取得私钥，然后读取2n+1到4n共2n行的公钥
keypairs=[]
cnt=0 # 每次读取上一迭代的2倍的行数
rows=my_sql_manager.execute('select * from keys order by ID asc limit 1024')

distributors=[]
receivers=[]

# round 0: 初始化状态： rows[0]->发币账户 , rows[1:]->收币账户
# row[0]为发币者， row[1:2]为收币者
distributors=rows[:1]
receivers=rows[1:]

while cnt<9: # 一共进行10个回合的分发，共产生 ∑(n=0..9)(2**n)=1023 个含有等额数量硬币的账户
    # 求当前回合的 分发账户 的数量 n_dis = len(distributor_keypairs)
    # 求当前回合的 收币账户 的数量 n_rec = n_dis
    # 每个分发账户将自己钱包里一半的钱分发给接收账户
    # 完成后，所有的账户变成发币账户，继续下一轮
    n_dis = len(distributors)
    n_rec = n_dis
    # 获得收币账户
    receivers_in_this_round=receivers[:n_rec]

    # 分发量，即 starting_balance = STARTING_BALANCE * (0.5 ** (cnt+1))
    starting_balance = starting_balance * 0.5-0.1

    clients=[]
    threads=[]

    # 扫描每一个分发私钥，生成一个对应的分发实例
    # 每个分发实例每周期向对应的接收者发送 STARTING_BALANCE * (0.5 ** (cnt + 1)) 硬币
    # 写入并行处理

    for i in range(n_dis):
        client=Client.Client(private_key=distributors[i][1])
        clients.append(client)
        thread=threading.Thread(target=client.fund, args=(receivers_in_this_round[i][2],starting_balance))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # 此时接收者转化为分发者
    distributors.extend(receivers_in_this_round)
    # 无法使用set对象，因为set对象不计顺序！ 所以使用pop
    receivers=receivers[n_dis:]
    cnt+=1


