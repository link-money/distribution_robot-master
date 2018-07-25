from stellar_base.address import *
from stellar_base.builder import Builder

def issue_asset(issuer_private_key, distributor_private_key, asset_code, limit,network):
    issuer_address=Keypair.from_seed(issuer_private_key).address().decode()
    distributor_address=Keypair.from_seed(distributor_private_key).address().decode()
    builder=Builder(secret=distributor_private_key, network=network)
    builder.append_trust_op(destination=issuer_address,code=asset_code,limit=limit)
    builder.sign()
    builder.submit()

    builder = Builder(secret=issuer_private_key, network=network)
    builder.append_payment_op(destination=distributor_address, amount=limit, asset_type=asset_code, asset_issuer=issuer_address)
    builder.sign()
    result = builder.submit()

    return result
