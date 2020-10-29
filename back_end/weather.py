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

    weather_api_1 = weather_api_1[['tm', 'avgTa', 'avgRhm', 'avgPa']]
    weather_api_1 = weather_api_1.rename({'tm': 'date', 'avgTa': 'mean_temp',
                                          'avgRhm': 'mean_humidity', 'avgPa': 'mean_pressure'}, axis=1)
    weather_api_1 = weather_api_1.reset_index(drop=True)

    weather_api_1

    queryParams_page2 = '?' + urlencode({

        "ServiceKey": unquote(key),
        "dataCd": "ASOS",
        "dateCd": "DAY",
        "numOfRows": "600",
        "pageNo": "2",
        "startDt": c,
        "endDt": d,
        "stnIds": "159",
        "dataType": "JSON"})

    queryURL_page2 = url + queryParams_page2
    response_page2 = requests.get(queryURL_page2)
    info_page2 = json.loads(response_page2.text)

    b = []
    for i in range(len(info_page2['response']['body']['items']['item'])):

        df = pd.DataFrame(info_page2['response']
                          ['body']['items']['item'][i], index=[0])

        b.append(df)

    weather_api_2 = pd.concat(b)

    weather_api_2 = weather_api_2[['tm', 'avgTa', 'avgRhm', 'avgPa']]
    weather_api_2 = weather_api_2.rename({'tm': 'date', 'avgTa': 'mean_temp',
                                          'avgRhm': 'mean_humidity', 'avgPa': 'mean_pressure'}, axis=1)
    weather_api_2 = weather_api_2.reset_index(drop=True)

    weather_api_concat = pd.concat([weather_api_1, weather_api_2])
    weather_api_concat = weather_api_concat.reset_index(drop=True)

    return(weather_api_concat)
