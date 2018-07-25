import json

from stellar_base.address import *


def post_transaction(public_key,seed,amount):
    builder = Builder(secret=seed)
    builder.append_payment_op(destination=public_key,amount=amount)
    builder.sign()
    result = builder.submit()

# publickey = 'GBRHA7VQ6XRHG3FPU4SRAZAF3LVKZUKLRL2BD3U3MNCJ4VUAHIBIDQ5P'
# address = Address(address=publickey) # address = Address(address=publickey,network='public') for livenet
# address.get() # get the updated information
#
# print "balances: " + address.balances
# print "sequence: " + address.sequence
# print "flags: " + address.flags
# print "signers: " + address.signers
# print "data: " + address.data

# master account:
master_private_key='SDD2PXU2QT6EGSCSSZWA374AETH3WJOF3LKQVGJVMCQHEXZ5R75XOXNB'
kp=Keypair.from_seed(seed= master_private_key)
master_public_key=str(kp.address().decode())
# public key = 'GBRHA7VQ6XRHG3FPU4SRAZAF3LVKZUKLRL2BD3U3MNCJ4VUAHIBIDQ5P'

# create 100 accounts:
# cnt=0
# key_pairs=[]
# while cnt<100:
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

# read the accounts from keys.json
f=open('../keys.json','r')
key_pairs=json.loads(f.read())
f.close()

from stellar_base.builder import Builder
seed = master_private_key

public_key=str('GAFBA6AMBJD2VKMTJBLJMUXRAROCTYSBQ4KHIMVUAHQS6WOLKU6IJTO6')
builder = Builder(secret=seed)
builder.append_payment_op(source=master_public_key, destination= public_key, amount= '100')
builder.sign()
result=builder.submit()
print result

cnt=0
import time

t1=time.time()
threads=[]

for key_pair in key_pairs:
    public_key = str(key_pair['public_key'])
    builder = Builder(secret=seed, network='testnet')
    builder.append_payment_op(destination=public_key, amount=66666)
    builder.sign()
    result = builder.submit()
    print(result)
    cnt+=1
    while cnt>10:
        break


t2=time.time()
print(t2-t1)
a=1
