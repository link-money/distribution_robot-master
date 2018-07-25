# passed

import wrapper.client as client

private_keys=['SBHTQEEKVTF2E3MQ6WCSFN725D73AELT2NSHS3PI7JASZLEJ4LT6MPD4',
              'SBTCFAL73MPCPIPLSIUTRQDLQQAXYCM4TILA26PGBL6QXXEU5SAGLYEU']

me=client.Client(private_key=private_keys[0],api_server='http://47.75.115.19:8888')
me.issue_asset(private_keys[1],asset_code='LNK',amount=10000000000)
