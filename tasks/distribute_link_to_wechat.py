# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")
from wrapper import db as DB
from wrapper import builder as BUILDER
from wrapper import client as CLIENT
import CONSTANT
import schedule
import time
from tasks import key_generation
from wrapper import user as USER
import requests
import json

# -1 CONSTANTS:
key='Xjr;H^P(RepxganS'
iv='7297115918661978'
constant=CONSTANT.Constant('test')
# 0. init
my_pgmanager=DB.PGManager(**CONSTANT.DB_CONNECT_ARGS_TEST)

# 1. join inquery:

def allocate_key(user_tokens):
    for user_token in user_tokens:
        sql='select * from private_keys where user_token=\'' + user_token + '\''
        row=my_pgmanager.select(sql)
        if len(row)==0:
            keypairs = key_generation.generate_keypairs(1, key, iv, False)
            sql='insert into private_keys(user_token,private_key,public_key) values(\'%s\',\'%s\',\'%s\')' % (user_token,keypairs[0][0],keypairs[0][1])
            my_pgmanager.execute(sql)
            a=1
    pass

def select_all_of_last_interval(t, interval=3600):
    # dt = '2018-01-01 10:40:30'
    # ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))
    datetime_upperbound = t
    datetime_lowerbound = datetime_upperbound-interval
    sql='select * from orders where created_at<' + str(datetime_upperbound) + ' and created_at>' + str(datetime_lowerbound) + ' and is_filled=0'
    rows=my_pgmanager.select(sql)
    return rows

# √√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√
def total_link_to_be_distributed():
    t=time.time()
    if t<1537203600:
        return 5477
    else:
        return -0.025 * int((t-1537203600)/3600) + 5477.2135

def monitor(inteval=60):
    cnt=0
    while True:
        cnt+=1
        t = int(time.time())
        print('\n' + '-'*120)
        timeArray = time.localtime(t)
        otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        print('Epoch:   %s\tTime:   %s' % (str(cnt),otherStyleTime ))
        print('-' * 120 + '\n')
        t0 = time.time()

        user_tokens = []
        users = {}
        rows = select_all_of_last_interval(t, 100000)

        expenses = {}
        total_expenses = 0

        for row in rows:
            token = row[1]
            expense = row[2]
            if token not in user_tokens:
                user_tokens.append(token)
                sql = 'select * from private_keys where user_token=\'' + token + '\''
                rs = my_pgmanager.select(sql)
                if len(rs) == 0:
                    keypair = key_generation.generate_keypairs(1, key, iv, False)[0]
                    sql = 'insert into private_keys(user_token,private_key,public_key) values(\'%s\',\'%s\',\'%s\')' % (token, keypair[0], keypair[1])
                    my_pgmanager.execute(sql)
                    user = USER.User(token, expense, keypair[0], keypair[1],0)
                else:
                    keypair = (rs[0][3], rs[0][2])
                    user = USER.User(token, expense, keypair[0], keypair[1],1)
                users[token] = user
            else:
                users[token].add_expense(expense)
            total_expenses += expense

        # calculate the link to be distributed to the single person
        if len(users)!=0:
            total_link = total_link_to_be_distributed()
            for k in users:
                user = users[k]
                link_to_be_distributed = user.expense / total_expenses * total_link
                user.link = round(link_to_be_distributed, 6)
            t0=time.time()-t0
            print('-' * 60 )
            print('Link distribution calculated successfully\tin %ss' % (t0,))
            print('-' * 60 + '\n')
        else:
            t0 = time.time() - t0
            print('-' * 60)
            print('Nothing to be calculated...\tin %ss' % (t0,))
            print('-' * 60 + '\n')

        # activate accounts
        t0=time.time()
        builder = BUILDER.Builder(secret=constant.DISTRIBUTOR_SEED, network='testnet')
        users_to_be_activated=[]
        if len(users_to_be_activated)!=0:
            for k in users:
                user = users[k]
                res=requests.get('http://116.62.226.231:8888/accounts/'+user.address).text
                if res.find('"asset_type": "native"')==-1:
                    users_to_be_activated.append(user)
            for user in users_to_be_activated:
                builder.append_create_account_op(destination=user.address, starting_balance=constant.FOTONO_STARTING_BALANCE)
            builder.sign()
            builder.submit()
            t0=time.time()-t0
            print('-' * 60)
            print('Accounts created successfully\tin %ss' % (t0,))
            print('-' * 60 + '\n')
        else:
            t0 = time.time() - t0
            print('-' * 60)
            print('No accounts to be created\tin %ss' % (t0,))
            print('-' * 60 + '\n')

        # create trust
        # multi-thread
        t0=time.time()
        if len(users)!=0:
            import threading
            threads=[]
            for k in users:
                user = users[k]
                private_key = user.private_key
                client = CLIENT.Client(private_key, api_server=constant.API_SERVER)
                thread=threading.Thread(target=client.trust, args=(constant.ISSUER_ADDRESS,'LINK'))
                threads.append(thread)
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            t0=time.time()-t0
            print('-' * 60 )
            print('Trustlines created successfully\tin %ss' % (t0,))
            print('-' * 60 + '\n')
        else:
            t0 = time.time() - t0
            print('-' * 60)
            print('No trustlines to be created...\tin %ss' % (t0,))
            print('-' * 60 + '\n')

        # distribute link
        t0 = time.time()
        builder = BUILDER.Builder(secret=constant.DISTRIBUTOR_SEED, network='testnet')
        if len(users)!=0:
            for k in users:
                user = users[k]
                builder.append_payment_op(destination=user.address, amount=user.link, asset_type='LINK',
                                          asset_issuer=constant.ISSUER_ADDRESS)
            builder.sign()
            res=builder.submit()
            if res.__contains__('hash'):
                sqls=[]
                items=[]
                for k in users:
                    sqls.append({'is_filled': 1, 'user_token': users[k].token})
                    item = {
                        "UserToken": users[k].token,
                        "LinkAddress": users[k].address,
                        "LinkAmount": users[k].link
                    }
                    items.append(item)
                my_pgmanager.execute_many('update orders set is_filled=%(is_filled)s where usertoken=%(user_token)s', sqls)
                t0 = time.time() - t0

                try:
                    # respond to server end
                    url='http://19o60w6992.51mypc.cn/sunday/link/callback'
                    # items=json.dumps(items)
                    # data=json.dumps({'LinkResult1':items})
                    data='LinkResult='+json.dumps(items)
                    res0=requests.get(url+'?'+data)
                    a=1
                except:
                    pass
                print('-' * 60)
                print('Link distributed successfully\tin %ss' % (t0,))
                print('-' * 60 + '\n')
        else:
            t0 = time.time() - t0
            print('-' * 60)
            print('No Link to be distributed, skip...\tin %ss' % (t0,))
            print('-' * 60 + '\n')

        time.sleep(inteval)

if __name__=='__main__':
    monitor()