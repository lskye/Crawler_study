import requests
from base64 import b64decode
from fontTools.ttLib import TTFont
from bs4 import BeautifulSoup
import lxml

cookies = {
    'sessionid': 'pveo4x8a6ex3yklhg3micuzdzwu0nm8t',
    'qpfccr': 'true',
    'no-alert3': 'true',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/7',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=pveo4x8a6ex3yklhg3micuzdzwu0nm8t; qpfccr=true; no-alert3=true',
}

on_map = {
	'1001101111': '1',
	'101010101101010001010101101010101010010010010101001000010': '8',
	'10101010100001010111010101101010010101000': '6',
	'10100100100101010010010010': '0',
	'1110101001001010110101010100101011111': '5',
	'10010101001110101011010101010101000100100': '9',
	'100110101001010101011110101000': '2',
	'111111111111111': '4',
	'1111111': '7',
	'10101100101000111100010101011010100101010100': '3',
}

lps = []

name=['爷灬霸气傀儡','梦战苍穹','傲世哥','мaη肆風聲','一刀メ隔世','横刀メ绝杀','Q不死你R死你',
      '魔帝殤邪','封刀不再战','倾城孤狼','戎马江湖','狂得像风','影之哀伤','謸氕づ独尊','傲视狂杀',
      '追风之梦','枭雄在世','傲视之巅','黑夜刺客','占你心为王','爷来取你狗命','御风踏血','凫矢暮城',
      '孤影メ残刀','野区霸王','噬血啸月','风逝无迹','帅的睡不着','血色杀戮者','冷视天下','帅出新高度',
      '風狆瑬蒗','灵魂禁锢','ヤ地狱篮枫ゞ','溅血メ破天','剑尊メ杀戮','塞外う飛龍','哥‘K纯帅','逆風祈雨',
      '恣意踏江山','望断、天涯路','地獄惡灵','疯狂メ孽杀','寂月灭影','骚年霸称帝王','狂杀メ无赦','死灵的哀伤',
      '撩妹界扛把子','霸刀☆藐视天下','潇洒又能打']

def request(page):
    params = {
        'page': page,
    }

    response = requests.get('https://match.yuanrenxue.cn/api/match/7', params=params, cookies=cookies, headers=headers).json()

    key = response['woff']
    data  = response['data']
    return key, data

def woff_to_xml(key):
    with open('7.ttf', 'wb') as f:
        f.write(b64decode(key))  # 将base64编码的woff解码并写入到文件

    font = TTFont('7.ttf')  # 使用fonttools库将解密后的woff文件转换成ttf文件
    font.saveXML('7.xml')   # 将ttf文件转换成xml文件

def parse_xml_to_font():

    with open ('7.xml', 'r', encoding='utf-8') as f:  # 读取xml文件
        xml = f.read()
    font_map = {}
    soup = BeautifulSoup(xml,'xml')
    tags = soup.find_all('TTGlyph')[1:]  # 提取所有的TTGlyph标签

    for tag in tags:
        name = tag.get('name')  # 提取每个TTGlyph标签的name属性
        contours = tag.find_all('contour')  # 提取每个TTGlyph标签下的所有contour标签
        on = ''
        for contour in contours:
            points = contour.find_all('pt')  # 提取每个contour标签下的所有pt标签
            for point in points:
                on += point.get('on')  # 提取每个pt标签的on属性，并拼接成一个字符串
        #print(name, on)
        if on in on_map:
            font_map['&#x' + name[3:]] = on_map[on]  # 将name属性和on属性拼接成的字符串映射到数字
    return font_map


for i in range(1,6):
    key, data = request(i)
    woff_to_xml(key)
    font_map = parse_xml_to_font()

    for item in data:
        nums = item['value'].split(' ')[:-1]
        lp = ''
        for num in nums:
            lp+= font_map[num]
        lps.append(int(lp))

max_lp_index = lps.index(max(lps))
print(name[max_lp_index])