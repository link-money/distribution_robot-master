# -*- coding:utf-8 -*-

import CONSTANT
from wrapper import keypair
from wrapper.client import Client
from tools import load_json
from wrapper import builder as BUILDER

# fund a random account
def fund_a_random_account():
    seed=CONSTANT.SEED
    client=Client(seed,api_server=CONSTANT.API_SERVER)
    destination=keypair.Keypair.random()
    address=destination.address().decode().encode('ascii')
    print(address)
    client.fund(destination=address,amount=10)

# fund the first 100 accounts in keys.json
def fund_accounts_in_keys_dot_json(lower_bound=0, upper_bound=1):
    seed=CONSTANT.SEED
    client=Client(seed,api_server=CONSTANT.API_SERVER)
    builder=BUILDER.Builder(secret=seed)
    keys=None
    keys=load_json.file2json('keys.json')[lower_bound:upper_bound]
    for key in keys:
        address=key['public_key']
        builder.append_create_account_op(destination=address, starting_balance=345.678)
    builder.sign()
    builder.submit()

if __name__=='__main__':
    fund_a_random_account();
    # fund_accounts_in_keys_dot_json()