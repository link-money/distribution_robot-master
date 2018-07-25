from stellar_base.address import *

import sdk

private_keys=['SBHTQEEKVTF2E3MQ6WCSFN725D73AELT2NSHS3PI7JASZLEJ4LT6MPD4',
              'SBTCFAL73MPCPIPLSIUTRQDLQQAXYCM4TILA26PGBL6QXXEU5SAGLYEU']
key_pairs=[]
for key in private_keys:
    key_pair=Keypair.from_seed(seed=key)
    key_pairs.append(key_pair)

issuer_priv=private_keys[0]
distributor_priv=private_keys[1]

issuer=key_pairs[0].address().decode()
distributor=key_pairs[1].address().decode()


sdk.issue_asset(issuer_priv, distributor_priv, 'LINK', 100, 'testnet')


