# -*- coding: UTF-8 -*-

# 本程序生成若干个发币账户的私钥，每个账户持有大量资产，下面的KEY和IV由资产发行者独自持有
# 本程序从自己启动，外部只能调用其方法
# 生成的私钥存储在sqlite数据库中
# 本程序的主入口程序为 main()

# 请填写下面几个参数：
# 第一个参数为生成的密钥对的数量，建议在1000-100,000个
NUMBER=1000
# 第二个参数为AES加密类实例的key，必须为16位ascii字符，必须由 第一人 妥善保存
KEY='$9b@")0U-M(xdS\'f'
# 第三个参数为AES加密类实例的iv，必须为16为数字，必须由 第二人 妥善保存
IV='5340789588690750'
# 并发度，默认为单线程，单线程快38%
CONCURRENCY=1

from tasks.key_generation import generate_keypairs

def main(number=NUMBER,key=KEY,iv=IV):
    import time
    t=time.time()
    keypairs = generate_keypairs(number,KEY,IV)
    print('time used: %d seconds' % int(time.time()-t))
    return keypairs

if __name__ == "__main__":
    main()
