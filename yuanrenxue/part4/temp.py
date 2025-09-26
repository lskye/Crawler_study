import requests
from bs4 import BeautifulSoup
from hashlib import md5
from base64 import b64encode
import typing


cookies = {
    'sessionid': 'pveo4x8a6ex3yklhg3micuzdzwu0nm8t',
    'no-alert3': 'true',
    'tk': '3690198760962583646',
    'm': '061f8c6ea055baa1ce325b1fe242b9d6|1758680518000',
    'yuanrenxue_cookie': '1758694340|A9bT1hvQms7DuRsgqFqom8UtArk97zfEB569y8Yt',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/4',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=pveo4x8a6ex3yklhg3micuzdzwu0nm8t; no-alert3=true; tk=3690198760962583646; m=061f8c6ea055baa1ce325b1fe242b9d6|1758680518000; yuanrenxue_cookie=1758694340|A9bT1hvQms7DuRsgqFqom8UtArk97zfEB569y8Yt',
}

params = {
    'page': '1',
}

response = requests.get('https://match.yuanrenxue.cn/api/match/4', params=params, cookies=cookies, headers=headers)
info = response.json()['info']


def parse_spritemap(html_string : str,key : str) -> list:
    """
    解析雪碧图HTML，提取显示的图片Base64与位移信息

    Args:
        html_string (str): 包含雪碧图的HTML字符串
        key (str): 雪碧图的class标签，值为display:none。有这个标签的图片是混淆数据，需要去除

    Returns:
        list: 一个大数组，每个元素是一个二维数组
              [[base64_1, base64_2, ...], [left_1, left_2, ...]]
    """
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_string, 'html.parser')

    # 找到所有 <td> 元素
    td_elements = soup.find_all('td')

    result = []

    for td in td_elements:
        img_data_list = []  # 存储 (base64, left_value) 对

        # 找到当前 <td> 下的所有 <img> 标签
        img_tags = td.find_all('img')

        for img in img_tags:
            src = img.get('src', '')
            style = img.get('style', '')
            img_class = img.get('class', '')[1]

            if img_class == key:
                continue

            # 将 (base64, left_value) 添加到列表
            img_data_list.append((src, style))

        left_list = [item[1] for item in img_data_list]
        print(left_list)
        print('=' * 30)
        result.append([left_list])
        # # 构建结果结构
        # if img_data_list:
        #     base64_list = [item[0] for item in img_data_list]
        #     left_list = [item[1] for item in img_data_list]
        #     result.append([base64_list, left_list])
        # else:
        #     # 如果该 td 中没有符合条件的图片，可以添加空数组或跳过
        #     result.append([[], []])

    return result

value = response.json()['value']
key = response.json()['key']
j_key = md5(b64encode((key + value).encode()).decode().replace('=', '').encode()).hexdigest()

p = parse_spritemap(info, j_key)
print(p)