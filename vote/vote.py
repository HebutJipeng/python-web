import requests
import json
import time
import random

TIME = 523
CURRENT = 0

def generate_random_str(randomlength=8):
    random_str = ''
    # base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    base_str = '0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

def generate_random_str2(randomlength=8):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    # base_str = '0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

EMAIL = [
    '@qq.com',
    # '@163.com',
    # '@gmail.com',
    # '@126.com',
    # '@hotmail.com',
    # '@alibaba.com',
    # '@msn.com',
    # '@yahoo.com',
    # '@aol.com',
    # '@ask.com'
]

def main():
    global CURRENT
    global TIME
    print(CURRENT)
    
    if CURRENT < TIME:
        nickName = generate_random_str(random.randint(8, 12))
        email = nickName + EMAIL[0]
        password = generate_random_str2(6)

        URL = 'http://contest.farener.com/api/user/register?nickName='+ nickName + '&email=' + email + '&password=' + password


        res = requests.post(URL)
        cookies = res.cookies
        cookies = requests.utils.dict_from_cookiejar(res.cookies)
        print(cookies)

        URL2 = 'http://contest.farener.com/api/vote?videoID=30'
        header2 = {
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,ko;q=0.8,ja;q=0.7,th;q=0.6,ru;q=0.5,id;q=0.4,pt;q=0.3,zh-TW;q=0.2,de;q=0.1,en;q=0.1,en-US;q=0.1,es;q=0.1,it;q=0.1,hi;q=0.1',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Cookie': 'sid=' + cookies['sid'],
            'Host': 'contest.farener.com',
            'Origin': 'http://contest.farener.com',
            'Referer': 'http://contest.farener.com/home',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89;Keep/5.7.9 (iPhone; iOS 10.3.2; Scale/2.00)',
        }
        data = {
            'videoID': 30
        }
        try:
            res2 = requests.post(URL2, cookies=cookies,
                                data=json.dumps(data), headers=header2)
            print(res2.content)
            time.sleep(1)
            res2 = requests.post(URL2, cookies=cookies,
                                data=json.dumps(data), headers=header2)
            print(res2.content)
            time.sleep(random.randint(4,10))
            CURRENT = CURRENT+1
            main()
        except ZeroDivisionError as err:
            print(err)


main()
