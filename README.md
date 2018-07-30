# 分币机器人

本程序在ubuntu16.04+python2.7及windows10+python2.7下测试通过

一些必要的依赖：
crc16 ed25519 numpy mnemonic toml 等

### 文件夹说明：
1. [党员测试](unit_tests)
2. [联金相关的业务](tasks)
3. [一些例子](examples)


### 使用说明：
1. 执行 pip install -r requirements.txt 完成依赖的安装
2. 在构建Client类的时候，使用api_server='testnet'参数'连接到测试服务器，使用api_server='public'参数连接到主网