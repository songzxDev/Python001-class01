# -*- coding:utf-8 -*-

import requests
# todo: 使用 requests 或 Selenium 模拟登录石墨文档 https://shimo.im

from hyper.contrib import HTTP20Adapter

if __name__ == '__main__':
    sess = requests.session()
    sess.mount('https://shimo.im', HTTP20Adapter())
    loginheader = {
        ':authority': 'shimo.im',
        ':method': 'POST',
        ':path': '/lizard-api/auth/password/login',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-length': '43',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'cookie': '_csrf=Ik3JTZAzyIAUPgvIu2-kS4Nu; deviceId=eeed712a-5e3b-4aab-9bc7-cbd972392d66; deviceIdGenerateTime=1593912318362; shimo_gatedlaunch=9; shimo_kong=8; shimo_svc_edit=1794; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; _bl_uid=5qk7ycUh8sze249tC5gObnktk40U; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2222600467%22%2C%22%24device_id%22%3A%221731c9418179f-066442e5cde5d1-f7d1d38-1327104-1731c94181828d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221731c9418179f-066442e5cde5d1-f7d1d38-1327104-1731c94181828d%22%7D; Hm_lvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1593914670; anonymousUser=-8146573162; shimo_sid=s%3A6naLMYazcpCIOc6AQQ4QjCYNpPF9w2nY.sGX9zGt2pcgdcFnHmtBjDcARxeFw2bB0aHGtuN5UA80; Hm_lpvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1593915444',
        'eagleeye-pappname': 'cuvx0xni1o@1a8e4117575f9ff',
        'eagleeye-sessionid': 'X8khCc5m8Lkg9936Cod73p5fCRe1',
        'eagleeye-traceid': 'e30d1bc8159391548030210015f9ff',
        'origin': 'https://shimo.im',
        'pragma': 'no-cache',
        'referer': 'https://shimo.im/login?from=home',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'x-requested-with': 'XmlHttpRequest',
        'x-source': 'lizard-desktop',
    }
    # '{"errorCode":5,"error":"需要提供验证码"}'
    # httpcode=400
    login = sess.post(url='https://shimo.im/lizard-api/auth/password/login',
                      data={'mobile': '+18646112326', 'password': 'sj10260392'}, headers=loginheader)
    me = sess.get('https://shimo.im/lizard-api/users/me')
    print(me.json())
