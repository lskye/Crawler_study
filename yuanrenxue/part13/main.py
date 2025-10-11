import requests
import re


cookies = {
    'sessionid': 'v9alzmmalvmwjp9sf07lpshe1tv6ce4s',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/13',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=v9alzmmalvmwjp9sf07lpshe1tv6ce4s; no-alert3=true; m=99c165c2f73d600de4c80c9f6fe9ed9a|1759997800000; yuanrenxue_cookie=1760083659|g2830jeimGSd2MtFV49WHXGmbIy7nZfH6hRpM4NHbBExASL6zOgWfyleDAl9CdFcYkkksci4epvjS12szr43eoe5Zh',
}

url = 'http://match.yuanrenxue.com/match/13'


session = requests.Session()
response = session.get(url=url, cookies=cookies)

cookie_list = re.findall(r'\'(.*?)\'\)', response.text)


cookies['yuanrenxue_cookie'] = ''.join(cookie_list)[18:]

sum_num = 0

for i in range(1,6):
    params = {
        'page': str(i),
    }

    response = session.get('https://match.yuanrenxue.cn/api/match/13', params=params, cookies=cookies, headers=headers)
    data = response.json().get('data')
    print(data)
    sum_num += sum(item.get('value', 0) for item in data)
print(sum_num)