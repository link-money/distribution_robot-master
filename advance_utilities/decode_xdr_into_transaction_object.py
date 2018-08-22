# -*- coding: UTF-8 -*-

import CONSTANT
from wrapper import client
from wrapper import builder

# 0. 初始化Client实例
client=client.Client(CONSTANT.SEED,api_server=CONSTANT.API_SERVER)
builder=builder.Builder(secret=CONSTANT.SEED)

xdr='''
AAAAANJzNMRdxNYi3nxM/hO1GbWpirESedpy+qj9LDU9+RJMAAATiAAAAAAAAACbAAAAAAAAAAAAAAABAAAAAAAAAAEAAAAAL4fia2XyDulN+lgjl/XWeZpswFZxuzTIsbVUmuQsdYEAAAABTElOSwAAAADSczTEXcTWIt58TP4TtRm1qYqxEnnacvqo/Sw1PfkSTAAAAAAgyFWAAAAAAAAAAAE9+RJMAAAAQJjBc5PjlZFeNLQCAzdwLxGjWZCjcAPqufhkMfZjYywltYKA11/VTrqHh1Tbn16hyLVVuMUnFrrOm69QVY1a1Ao=
'''
import time
t0=time.time()
for cnt in range(100000):
    builder.import_from_xdr(xdr)
print(time.time()-t0)
