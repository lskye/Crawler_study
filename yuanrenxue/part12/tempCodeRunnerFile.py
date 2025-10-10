 response = requests.get('https://match.yuanrenxue.cn/api/match/12', params=params, cookies=cookies, headers=headers)
    print(response.json())
    for i in response.json()['data']:
        sum += int(i['value'])
print(sum)