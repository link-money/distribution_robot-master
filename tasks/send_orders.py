import requests
import json
import random
import CONSTANT

url=CONSTANT.BASE_URL_TEST + '/link/api/call/run/orders'
user_tokens=['oliver','Thor','jeff','gary','jessy','omega','lindsey','mary','c001','c002','c003','Jacob','Michael','Ethan','Joshua','Alexander','Anthony','William','Christopher','Jayden','Andrew','Joseph','David','Noad','Aiden','James','Ryan','Logan','John','Nathan','Elijah','Christian','Gabriel','Benjamin','Jonathan','Tyler','Samuel','Nicholas','Gavin','Dylan']
user_tokens=['oOZg40kK2BLQAXxGY29kpxXetc0c']
fees=[1,1,1,1,3,3,5]

def send_orders(span, interval=0.1):
    import time

    order_no = 0

    t0=time.time()
    end_time=t0+span

    while t0<end_time:
        t0=time.time()
        data = {'UserToken': random.choice(user_tokens), 'OrderAmount': random.choice(fees)}
        order_no+=1
        r=requests.post(url,data=data)
        print(r.text)
        time.sleep(interval)

if __name__=='__main__':
    send_orders(2)