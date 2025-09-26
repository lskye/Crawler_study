import requests
from collections import defaultdict

headers = {
    'content-length': '0',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile':	'?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'origin': 'https://match.yuanrenxue.cn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://match.yuanrenxue.cn/match/3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
}
cookies = {
    'sessionid': 'pveo4x8a6ex3yklhg3micuzdzwu0nm8t',
    'no-alert3': 'true',
    'tk': '3690198760962583646',
    'm': '061f8c6ea055baa1ce325b1fe242b9d6|1758680518000',
    'yuanrenxue_cookie': '1758694340|A9bT1hvQms7DuRsgqFqom8UtArk97zfEB569y8Yt',
}


session = requests.session()
session.headers = headers
res = defaultdict(int)
for i in range(1, 6):
    url = "https://match.yuanrenxue.cn/jssm"
    response = session.post(url, cookies=cookies)

    url_p = 'https://match.yuanrenxue.cn/api/match/3?page={}'.format(i)
    resp = session.get(url=url_p, cookies=cookies)
    print(resp.text)
    for data in resp.json()['data']:
        value = data['value']
        res[value] += 1
print(res)
print(dict(res))
print(max(res, key=lambda x: res[x]))