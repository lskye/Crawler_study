import requests
import base64

import requests

cookies = {
    'sessionid': 'v9alzmmalvmwjp9sf07lpshe1tv6ce4s',
    'no-alert3': 'true',
    'm': '99c165c2f73d600de4c80c9f6fe9ed9a|1759997800000',
    'yuanrenxue_cookie': '1760081712|LZKPx3BdxU6U3SsQdeMDKxKvQ6taYW8HG6HvDMQLT7TkewSBsEuXBGIAFnzjIYBaMyjCqj94BTDTYXVcklTqwAmLTSnI4s3mwUzZ7OIhEF7ZgB0g21prqSpuebzQUIR75TBsfSRe6BhVl9aQIBQSziKmvSISMp',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/12',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=v9alzmmalvmwjp9sf07lpshe1tv6ce4s; no-alert3=true; m=99c165c2f73d600de4c80c9f6fe9ed9a|1759997800000; yuanrenxue_cookie=1760081712|LZKPx3BdxU6U3SsQdeMDKxKvQ6taYW8HG6HvDMQLT7TkewSBsEuXBGIAFnzjIYBaMyjCqj94BTDTYXVcklTqwAmLTSnI4s3mwUzZ7OIhEF7ZgB0g21prqSpuebzQUIR75TBsfSRe6BhVl9aQIBQSziKmvSISMp',
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
    print(response.json())
    for i in response.json()['data']:
        sum += int(i['value'])
print(sum)

