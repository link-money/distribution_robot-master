# passed

import wrapper.client as client
from wrapper import builder
import CONSTANT
from tools import load_json

seed=CONSTANT.SEED
keypairs=load_json.file2json('keys.json')
keypairs=keypairs[101:200]
import time
t=time.time()
builder = builder.Builder(secret=seed)
for key in keypairs:
    builder.append_create_account_op(destination=key['public_key'],starting_balance=66.6666)
    # builder.append_payment_op(destination=key['public_key'],amount=333.44)
builder.sign()
result = builder.submit()
print(result)
print(time.time()-t)