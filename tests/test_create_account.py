# test funding function
import time

from wrapper.client import Client
from wrapper.keypair import Keypair

seed='SDSSWWPCGGRDB6SVVOJUWFQ3ODQFX62GVTKCPELNULO5PXVCFE67L7HO'
client=Client(seed,api_server='test')
key_pairs=[]

t1=time.time()
for i in range(0,5):
    key_pair=Keypair.random()
    secret_key=key_pair.seed().decode()
    address=key_pair.address().decode()
    client.fund(address,1000)
    print(secret_key+'     '+address)
    key_pairs.append(key_pair)

t2=time.time()
print('\n' + str(t2-t1))