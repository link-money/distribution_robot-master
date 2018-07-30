# distribution_robot-master


本程序在ubuntu16.04+python2.7及windows10+python2.7下测试通过

一些必要的依赖：
crc16 ed25519 numpy mnemonic toml 等

说明：
1. 测试请见unit_tests文件夹

2. 联金相关的业务请见tasks文件夹
    1. 首先，执行/tasks/generate_keys_and_insert_into_db生成一堆私钥，并存入sqlite数据库，后续要转移到你们的数据库中；
    2.

3.


使用说明：
1. 执行 pip install -r requirements.txt 完成依赖的安装
2. 进入tasks文件夹，按照相关说明进行操作
3. 在构建Client类的时候，使用api_server='testnet'参数'连接到测试服务器，使用api_server='public'参数连接到主网