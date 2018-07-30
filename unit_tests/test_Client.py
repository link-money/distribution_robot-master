# -*- coding: UTF-8 -*-

# 该文件测试wrapper文件夹下Client类

from wrapper.client import Client
import CONSTANT
import unittest
import tools.load_json as TOOLS
import time
from wrapper.utils import *

# 定义一些常数
master_seed=CONSTANT.SEED
keypairs=TOOLS.file2json('keys.json')

# 为了形象化，我们给4个主要的测试账户起了个名字
Odin    =   Client(master_seed)
Heimdar =   Client(keypairs[0]['private_key'])
Heimdar =   Client(keypairs[1]['private_key'])
Loki    =   Client(keypairs[2]['private_key'])
# 这个瓦力是专门用来做balance测试的
Vale    =   Client(keypairs[-1]['private_key'])

class TestClient(unittest.TestCase):
    def test_init(self):
        self.assertTrue(isinstance(Odin, Client))

    def test_fund(self):
        # 我们要确定的事情有：
        # 1. 奥丁账户的钱少了123.345个
        # 2. 洛基的账户被激活了，并且他的钱多了123.345个
        # 3. 这个测试只能做一次，因为fund函数是一次性的
        # 4. 这个测试目前一定会失败，因为这三个收币账户都已经激活了，要测试自己换个收币账户
        initial_balance_of_Odin =   Odin.get_balances()[0]['balance']
        Odin.fund(destination=Loki.address,amount=123.345)
        time.sleep(5)
        current_balance_of_Odin =   Odin.get_balances()[0]['balance']
        current_balance_of_Loki =   Loki.get_balances()[0]['balance']
        self.assertAlmostEqual(float(initial_balance_of_Odin)-float(current_balance_of_Odin),123.345,delta=0.0006)
        self.assertAlmostEqual(float(current_balance_of_Loki),123.345,delta=0.0006)

    def test_pay_to(self):
        # 我们要确定的事情有：
        # 1. 奥丁账户的钱少了9.876个
        # 2. 洛基的账户被激活了，并且他的钱多了9.876个
        initial_balance_of_Odin = float(Odin.get_balances()[0]['balance'])
        initial_balance_of_Loki = float(Loki.get_balances()[0]['balance'])
        Odin.pay_to(destination=Loki.address, amount=9.876)
        time.sleep(5)  # 需要停一会，因为线程可能还没在区块链中生效，区块链确定下来需要至少5秒钟
        current_balance_of_Odin = float(Odin.get_balances()[0]['balance'])
        current_balance_of_Loki = float(Loki.get_balances()[0]['balance'])
        print('initial balance of Odin: %f' % initial_balance_of_Odin)
        print('initial balance of Loki: %f' % initial_balance_of_Loki)
        print('current balance of Odin: %f' % initial_balance_of_Odin)
        print('current balance of Loki: %f' % current_balance_of_Loki)
        self.assertAlmostEqual(float(initial_balance_of_Odin) - float(current_balance_of_Odin), 9.876, delta=0.0006)
        self.assertAlmostEqual(float(current_balance_of_Loki) - float(initial_balance_of_Loki), 9.876, delta=0.0006)

    def test_get_balances(self):
        # 对于一个空账户，get_balances方法返回的是: None
        # 这么一个response.content的字符串
        # 对于一个非空账户，get_balances方法返回的是一个json格式的字符串
        fun_get_balances=Vale.get_balances
        self.assertRaises(AccountNotExistError,fun_get_balances)
        balances = Odin.get_balances()
        self.assertTrue(isinstance(balances,list))
        self.assertTrue(dict.has_key(balances[0],'balance'))
        self.assertEqual(balances[0]['asset_type'], 'native')
        self.assertTrue(balances[0]['balance']>0)



if __name__=="__main__":
    unittest.main()
