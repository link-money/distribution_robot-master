# -*- coding: UTF-8 -*-

import CONSTANT
import time
from wrapper import client as CLIENT
from wrapper import builder as BUILDER
from tools import load_json
from wrapper import keypair

def all_in_one(activate_the_distributor=True, activate_accounts=True, send_native_asset_to_accounts=True, issue_asset=True, do_trust=True, send_LINK_to_accounts=True):

    # 初始化Client实例
    constant=CONSTANT.Constant('test')
    master=CLIENT.Client(constant.SEED,api_server=constant.API_SERVER)
    # 产生100个密钥对
    keypairs = load_json.file2json('keys.json')[201:290]
    distributor = CLIENT.Client(constant.DISTRIBUTOR_SEED)
    builder = BUILDER.Builder(secret=constant.SEED, network='testnet')

    if activate_the_distributor:
        # activate the distributor
        master.fund(destination=distributor.address,amount=100)

    if activate_accounts:
        # activate the above accounts using parallel method
        for keypair in keypairs:
            address=keypair['public_key']
            print(address)
            builder.append_create_account_op(destination=address, starting_balance=100)
        builder.sign()
        builder.submit()

    if send_native_asset_to_accounts:
        # send native asset to accounts
        builder = BUILDER.Builder(secret=constant.SEED, network='testnet')
        for keypair in keypairs:
            address=keypair['public_key']
            print(address)
            builder.append_payment_op(destination=address, amount=123.456)
        builder.sign()
        builder.submit()

    if issue_asset:
        result = master.issue_asset(distributor.private_key, asset_code='LINK', amount=10000000)
        print(result)

    if do_trust:
        for keypair in keypairs:
            try:
                client=CLIENT.Client(private_key=keypair['private_key'],api_server=constant.API_SERVER)
                client.trust(constant.ISSUER_ADDRESS, asset_code='LINK', limit=1000000)
            except:
                print(client.address)


    if send_LINK_to_accounts:
        # send LINK asset to accounts
        while True:
            builder = BUILDER.Builder(secret=constant.DISTRIBUTOR_SEED, network='testnet')
            for keypair in keypairs:
                address=keypair['public_key']
                print(address)
                import random
                amount=round(random.random()*10,4)
                builder.append_payment_op(destination=address, amount=amount, asset_type='LINK', asset_issuer=constant.ISSUER_ADDRESS)
            builder.sign()
            builder.submit()

if __name__=='__main__':
    all_in_one(activate_the_distributor=False, activate_accounts=False, send_native_asset_to_accounts=False, issue_asset=False, do_trust=False, send_LINK_to_accounts=True)