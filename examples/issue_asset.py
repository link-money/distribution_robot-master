# -*- coding: UTF-8 -*-

# 该模块给出了一个发行数字资产的例子
# 发行资产需要两个账户：一个是发行账户，一个是分发账户，产生的资产在分发账户里
# 对于本例，产生的资产咋子distributor这个账户里

# 发行账户即：
# 分发账户即：
import wrapper.client as client
import CONSTANT

issuer_private_key=CONSTANT.SEED
distributor_private_key='SDFJSFUDRZP65ZWJX5DPSM3CRNDTUYMQ2C2CEDVGGNXWEZ42NK4J4CVP'
issuer=client.Client(private_key=issuer_private_key, api_server=CONSTANT.API_SERVER)
distributor=client.Client(private_key=distributor_private_key, api_server=CONSTANT.API_SERVER)

result=issuer.issue_asset(distributor.private_key,asset_code='SHIT',amount=10000000)
print(result)


