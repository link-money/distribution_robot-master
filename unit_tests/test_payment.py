# passed

from wrapper.client import Client

api_server='testnet'
private_keys=['SBHTQEEKVTF2E3MQ6WCSFN725D73AELT2NSHS3PI7JASZLEJ4LT6MPD4',
              'SBTCFAL73MPCPIPLSIUTRQDLQQAXYCM4TILA26PGBL6QXXEU5SAGLYEU']

addresses=['GDJJB2QA7XZSBHCGIRUAIUC5RJ6MJGV2DG5THNNJOTUQWXEDKXLVFZMI',
             'GCKEZY2FW2MLANNJTQZIKFISGP2MZ57MZWMGECG3WD2FJHEQAGAA7ZUA']

# key_pairs=[]
# for key in private_keys:
#     key_pair=Keypair.from_seed(seed=key)
#     key_pairs.append(key_pair)
#
# issuer_priv=private_keys[0]
# distributor_priv=private_keys[1]
#
# issuer=key_pairs[0].address().decode()
# distributor=key_pairs[1].address().decode()
#
#
# # sdk.issue_asset(issuer_priv,distributor_priv,'eth',100,'testnet')
#
# builder = Builder(secret=distributor_priv, network='testnet')
# builder.append_payment_op(destination=issuer, amount=(84000000-1), asset_type='ltc', asset_issuer=issuer)
# builder.sign()
# result = builder.submit()

client=Client(private_key=private_keys[0],api_server=api_server)
client.pay_to(addresses[1],123.45)

client.pay_to(addresses[1],543.21,asset_code='ltc', asset_issuer=addresses[0] )
