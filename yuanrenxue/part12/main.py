import requests
import base64

cookies = {
    'sessionid': 'pveo4x8a6ex3yklhg3micuzdzwu0nm8t',
    'qpfccr': 'true',
    'no-alert3': 'true',
    'tk': '3690198760962583646',
    'm': '061f8c6ea055baa1ce325b1fe242b9d6|1758680518000',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/12',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=pveo4x8a6ex3yklhg3micuzdzwu0nm8t; qpfccr=true; no-alert3=true; tk=3690198760962583646; m=061f8c6ea055baa1ce325b1fe242b9d6|1758680518000',
}

sum = 0
# params = {
#     'page': '3',
#     'm': 'eXVhbnJlbnh1ZTM=',
# }
for i in range(1,6):
    encoded_str = base64.b64encode(f'yuanrenxue{i}'.encode())
    params = {
        'page': f'{i}',
        'm': encoded_str,
    }
    response = requests.get('https://match.yuanrenxue.cn/api/match/12', params=params, cookies=cookies, headers=headers)
    for i in response.json()['data']:
        sum += int(i['value'])
print(sum)

