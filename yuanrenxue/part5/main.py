import time
import requests
import execjs


cookies = {
    'sessionid': 'htx5xax27x30d19ehg2fq13zuybdvi0t',
    'qpfccr': 'true',
    'no-alert3': 'true',
    'tk': '3690198760962583646',
    'm': '',
    'RM4hZBv0dDon443M': '',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/5',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=htx5xax27x30d19ehg2fq13zuybdvi0t; qpfccr=true; no-alert3=true; tk=3690198760962583646; m=988fc5456fd823fafd48a7789fbd15d5; RM4hZBv0dDon443M=/7cpb94RMBzILXd4ZTaldYq7U0id9ajerFEEF5ZzslB+AVkA1FG5NiqiJ49HJ1nXIRnWBlFB12C9BNlv5jhjmdJV4RBIQdHGOjopTcEdp3DlHBMqiRDLej7+VhI9YAJPMSxCfiBk0OfGvubMcSLowIzrqa5Y46JoaoO01pARq2UQciks37fgSsvh9rSfEu4pUpKHLtlcGn1a9ahO9Q3kaBF70dUluoA7VbudPbY8NpQ=',
}


with open('./mian.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

hot = []

for i in range(1,6):

    ctx = execjs.compile(jscode).call('getParamers')

    cookies['m'] = ctx['cookie_m']
    cookies['RM4hZBv0dDon443M'] = ctx['cookie_rm4']

    params = {
        'page': {i},
        'm':ctx['m'],
        'f':ctx['f']

    }


    response = requests.get('https://match.yuanrenxue.cn/api/match/5', params=params, cookies=cookies, headers=headers)
    data = response.json()['data']
    for i in data:
        hot.append(i['value'])
hot.sort(reverse=True)


topfive_hot_sum = sum(hot[:5])
print(topfive_hot_sum)
