import requests
import execjs

cookies = {
    'sessionid': '3x2vrjnp98422ytvfcc60wwab3uz20wx',
    'no-alert3': 'true',
    'tk': '3690198760962583646',
    'm': '9dcf748a003d4f61583640bbb067dd41',
    'RM4hZBv0dDon443M': 'undefined',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/6',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=3x2vrjnp98422ytvfcc60wwab3uz20wx; no-alert3=true; tk=3690198760962583646; m=9dcf748a003d4f61583640bbb067dd41; RM4hZBv0dDon443M=undefined',
}

with open('main.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
ctx = execjs.compile(jscode)
mony = 0
for i in range(1,6):
    p = ctx.call('get_param')
    #print(p)
    params = {
        'page': {i},
        'm': p['m'],
        'q': p['q'],
    }

    response = requests.get('https://match.yuanrenxue.cn/api/match/6', params=params, cookies=cookies, headers=headers)

    value = response.json()['data']
    print(value)

    for i in value:
        mony += i['value']*24
print(mony)

