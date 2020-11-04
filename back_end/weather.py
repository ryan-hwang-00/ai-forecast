import urllib.request
import xmltodict
import json
import sys
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import pandas as pd
import numpy as np
import requests

url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
key = "NnpxwR7oA3LxPCsLEMG2CcvrkIZRLw0%2BHmz2ClUcOfaKvAMlySAiadvjQKqyQu0HorPtqAGZpj%2Bxfe6iSFyDKw%3D%3D"


def weather_api(c, d):

    c = str(c)
    d = str(d)
    time1 = datetime(int(c[0:4]), int(c[4:6]), int(c[6:8]))
    time2 = datetime(int(d[0:4]), int(d[4:6]), int(d[6:8]))
    day_len = (time2-time1).days

    queryParams_page1 = '?' + urlencode({

        "ServiceKey": unquote(key),
        "dataCd": "ASOS",
        "dateCd": "DAY",
        "numOfRows": "600",
        "pageNo": "1",
        "startDt": c,
        "endDt": d,
        "stnIds": "159",
        "dataType": "JSON"})

    queryURL_page1 = url + queryParams_page1
    response_page1 = requests.get(queryURL_page1)
    info_page1 = json.loads(response_page1.text)

    a = []
    for i in range(len(info_page1['response']['body']['items']['item'])):

        df = pd.DataFrame(info_page1['response']
                          ['body']['items']['item'][i], index=[0])

        a.append(df)

    weather_api_1 = pd.concat(a)

    weather_api_1 = weather_api_1[['tm', 'avgTa', 'avgRhm', 'avgPa', 'sumRn']]
    weather_api_1 = weather_api_1.rename({'tm': 'date', 'avgTa': 'mean_temp',
                                          'avgRhm': 'mean_humidity', 'avgPa': 'mean_pressure', 'sumRn': 'rain'}, axis=1)
    weather_api_1 = weather_api_1.reset_index(drop=True)
    weather_api_1 = weather_api_1.replace(r'', np.nan, regex=True)
    weather_api_1 = weather_api_1.fillna(0)
    weather_api_1 = weather_api_1.astype({'mean_temp': 'float', 'mean_humidity': 'float',
                                          'mean_pressure': 'float', 'rain': 'float'})

    queryParams_page1 = '?' + urlencode({

        "ServiceKey": unquote(key),
        "dataCd": "ASOS",
        "dateCd": "DAY",
        "numOfRows": "600",
        "pageNo": "2",
        "startDt": c,
        "endDt": d,
        "stnIds": "159",
        "dataType": "JSON"})

    queryURL_page1 = url + queryParams_page1
    response_page1 = requests.get(queryURL_page1)
    info_page1 = json.loads(response_page1.text)

    b = []
    for i in range(len(info_page1['response']['body']['items']['item'])):

        df = pd.DataFrame(info_page1['response']
                          ['body']['items']['item'][i], index=[0])

        b.append(df)

    weather_api_2 = pd.concat(b)

    weather_api_2 = weather_api_2[['tm', 'avgTa', 'avgRhm', 'avgPa', 'sumRn']]
    weather_api_2 = weather_api_2.rename({'tm': 'date', 'avgTa': 'mean_temp',
                                          'avgRhm': 'mean_humidity', 'avgPa': 'mean_pressure', 'sumRn': 'rain'}, axis=1)

    weather_api_2 = weather_api_2.replace(r'', np.nan, regex=True)
    weather_api_2 = weather_api_2.fillna(0)
    weather_api_2 = weather_api_2.astype({'mean_temp': 'float', 'mean_humidity': 'float',
                                          'mean_pressure': 'float', 'rain': 'float'})

    weather_api_3 = pd.concat([weather_api_1, weather_api_2])

    weather_api_3 = weather_api_3.reset_index(drop=True)

    if day_len <= 600:

        return weather_api_1

    else:

        return weather_api_3
