# 联金区块链SDK

###本SDK打包了该区块链的基础功能，包括：
####1. [地址相关功能](wrapper/address.py)
####2. [资产相关功能](wrapper/asset.py)
####3. [base58编码解码功能](wrapper/base58.py)
####4. [builder](wrapper/builder.py)
####5. [一个高度抽象的面向账户的操作类](wrapper/client.py)
####6. [sqlite数据库操作类](wrapper/db.py)
####7. [AES256加解密的操作类](wrapper/encryption.py)

本程序在ubuntu16.04+python2.7及windows10+python2.7下测试通过

一些必要的依赖：
crc16 ed25519 numpy mnemonic toml 等

### 文件夹说明：
1. [党员测试](unit_tests/README.md)
2. [联金相关的业务](tasks/README.md)
3. [一些例子](examples/README.md)


### 使用说明：
1. 执行 pip install -r requirements.txt 完成依赖的安装
2. 在构建Client类的时候，使用api_server='testnet'参数'连接到测试服务器，使用api_server='public'参数连接到主网