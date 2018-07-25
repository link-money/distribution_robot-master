# -*- coding: UTF-8 -*-
import os,sys

# 下面是一些常数，需要你们确定一下

# 0. 所有资金的种子账户：
MOTHER_SEED=''

# 1. 发币账户（钱包）的总数量，建议是2^n-1,其中n为整数，例如127、255：
NUMBER_OF_ACCOUNTS=255

# 2. 数据库文件的位置，默认是运行的程序的目录+文件名，只需要确认文件名即可：
path=os.getcwd()
DB_NAME=path+'\\keys.db'