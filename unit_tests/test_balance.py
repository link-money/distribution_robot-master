# passed
from wrapper.client import Client
from wrapper import db as DB
import os

api_server='testnet'
private_keys=['SBHTQEEKVTF2E3MQ6WCSFN725D73AELT2NSHS3PI7JASZLEJ4LT6MPD4',
              'SBTCFAL73MPCPIPLSIUTRQDLQQAXYCM4TILA26PGBL6QXXEU5SAGLYEU',
              'SCV5M6ISCCVYBQ5Y4GQ3L2A6JM25Z4CAIZOBSWBRURFCBF4OKW3OAM3M']

addresses=['GDJJB2QA7XZSBHCGIRUAIUC5RJ6MJGV2DG5THNNJOTUQWXEDKXLVFZMI',
            'GCKEZY2FW2MLANNJTQZIKFISGP2MZ57MZWMGECG3WD2FJHEQAGAA7ZUA',
            'GCKEZY2FW2MLANNJTQZIKFISGP2MZ57MZWMGECG3WD2FJHEQAGAA7ZUA']


client=Client(private_keys[2],api_server='testnet')
balance0=client.get_balances()

client0=Client(private_key=private_keys[0],api_server=api_server)
client1=Client(private_key=private_keys[1],api_server=api_server)
client2=Client(address=addresses[0],api_server=api_server)
client3=Client(address=addresses[1],api_server=api_server)

balance0=client0.get_balances()
balance1=client1.get_balances()
balance2=client2.get_balances()
balance3=client3.get_balances()
a=1