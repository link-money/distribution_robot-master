# -*- coding: UTF-8 -*-
# 该模块给出了一个加解密的例子


from wrapper.encryption import Prpcrypt

# 定义两个密码：key 和 iv,这两个变量都是16位的字符串，每个字符都是ascii字符
key='1'*16
iv='1'*16

# 初始化一个Prpcrypt类：
prp=Prpcrypt(key=key,iv=iv)

# 定义一个文本
plain="Bitcoin is good..."
# 使用encrypt函数进行加密：
cypher=prp.encrypt(plain)
# 输出密文
print(cypher)
# 解密密文：
restored_plain=prp.decrypt(cypher)
# 打印明文及恢复后的明文：
print("original text:\t%s\nrestored text:\t%s\norigin == restored ? %s" % (plain,restored_plain,plain==restored_plain))
