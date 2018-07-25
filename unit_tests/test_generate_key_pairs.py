import json

from stellar_base.address import *
from stellar_base.builder import Builder

from wrapper.client import Client


def op(source, destination, amount):
    builder = Builder(secret=source)
    builder.append_payment_op(destination=destination,amount=amount)
    builder.sign()
    builder.submit()


# master account:
master_private_key='SDSSWWPCGGRDB6SVVOJUWFQ3ODQFX62GVTKCPELNULO5PXVCFE67L7HO'
kp=Keypair.from_seed(seed= master_private_key)
master_public_key=str(kp.address().decode())
client=Client(master_private_key,api_server='test')
balance=float(client.get_balances()[0]["balance"])

# create 10000 accounts:
# cnt=0
# key_pairs=[]
# while cnt<10000:
#     key_pair=Keypair.random()
#     publickey = key_pair.address().decode()
#     seed = key_pair.seed().decode()
#     key_pair={'private_key':seed,'public_key':publickey}
#     key_pairs.append(key_pair)
#     cnt+=1
# # write to a json file
# json_string=json.dumps(key_pairs)
# f=open('keys.json','w')
# f.write(json_string)
# f.close()

# read the json file and convert it to an array:
f=open('keys.json','r')
key_pairs=json.loads(f.read())
f.close()

# from stellar_base.builder import Builder
seed = master_private_key

cnt=0

# make initial funded accounts:
for key_pair in key_pairs:
    pub_key=key_pair['public_key']
    print(client.fund(destination=pub_key,amount= 10000))
#
# funded_key_pairs=key_pairs[:51]
#
# # make an array of threads
# threads=[]
# import threading
# for i in range(50):
#     priv=funded_key_pairs[i]["private_key"]
#     publ=funded_key_pairs[i+1]["public_key"]
#     thread=threading.Thread(target=op, args=(priv,publ,10,) )
#     threads.append(thread)
#
# t1=time.time()
# # do operations using multithread
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
# t2=time.time()
# print(t2-t1)
# a=1
