import requests

cookies = {
    'sessionid': 'rrmqn6k1hmuug5ohgqkbwz8y1s42rwqa',
    'no-alert3': 'true',
    'tk': '3690198760962583646',
    'm': '6bc44eeec2253b05b97cfc6cbc1f7b98|1758675027000',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/2',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=rrmqn6k1hmuug5ohgqkbwz8y1s42rwqa; no-alert3=true; tk=3690198760962583646; m=6bc44eeec2253b05b97cfc6cbc1f7b98|1758675027000',
}

response = requests.get('https://match.yuanrenxue.cn/api/match/2', cookies=cookies, headers=headers)

print(response.text)