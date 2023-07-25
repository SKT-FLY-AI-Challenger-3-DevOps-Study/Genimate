import requests, xmltodict
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), ".env"))

def getDate():
    current_date = datetime.now().date()
    return current_date.strftime("%Y%m%d")

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'

params = {
    'serviceKey' : os.environ["SERVICE_KEY"],
    'numOfRows' : '100',
    'pageNo' : '1',
    'base_date' : getDate(),
    'base_time' : '0200',
    'nx' : '37',
    'ny' : '127',
}

SKY_MAP = {
    '1' : 'A sktadot enjoying a picnic under a clear blue sky', # 맑음
    '3' : 'A sktadot walking under the many of clouds, cloudy day, blue sky, perfect face', # 구름 많은
    '4' : 'A sktadot walking under the clouds, dark cloudy day, perfect face' # 흐림
}
    
PTY_MAP = {
    '0' : 'A sktadot enjoying a picnic under a clear blue sky', # 없음
    '1' : 'A sktadot walking with an umbrella under the clouds on a rainy, cloudy day', # 비
    '2' : 'A sktadot playing in the rain and snowfal, perfect face', # 비/눈
    '3' : 'A sktadot building a snowman on a snowy day, perfect face', # 눈
    '4' : 'rainy day, sktadot boy, cute, rain, water, artstation, 8k --ar 2:3 --uplight' # 소나기
}


def forecast():
    weather_data = dict()
    try:
        res = requests.get(url, params=params)
        xml_data = res.text
        dict_data = xmltodict.parse(xml_data)

        for item in dict_data['response']['body']['items']['item']:
            if item['fcstTime'] != '0700':
                continue
            if item['category'] == 'SKY':
                weather_data['sky'] = SKY_MAP[item['fcstValue']]
            if item['category'] == 'PTY':
                weather_data['sky2'] = PTY_MAP[item['fcstValue']]
    except Exception as e:
        print(e)
        weather_data = dict()
    finally:
        return weather_data

print(forecast())