import requests
import time
import random
import math
import pywasm

cookies = {
    'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3': '1760085836',
    'sessionid': 'drneaestw1tohnzydeweptgwgyrfd0gp',
    'qpfccr': 'true',
    'no-alert3': 'true',
    'tk': '4792691933558433445',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/15',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1760085836; sessionid=drneaestw1tohnzydeweptgwgyrfd0gp; qpfccr=true; no-alert3=true; tk=4792691933558433445',
}

wasm_url = "https://match.yuanrenxue.cn/static/match/match15/main.wasm"
resp1 = requests.get(wasm_url)
with open("main.wasm", mode="wb") as file:
	file.write(resp1.content)


def encode(t1,t2):
	module = pywasm.load('./main.wasm')
	result = module.exec('encode', [t1, t2])
	m = str(result) + '|' + str(t1) + '|' + str(t2)
	return m

t1 = int(time.time() / 2)
t2 = int(time.time() / 2 - math.floor(random.random() * 50 + 1))

m = encode(t1, t2)
total = 0

for i in range(1,6):
    params = {
        'm': m,
        'page': i,
    }

    response = requests.get('https://match.yuanrenxue.cn/api/match/15', params=params, cookies=cookies, headers=headers)
    values = response.json()['data']

    total += sum(item['value'] for item in values)
print("总和:", total)