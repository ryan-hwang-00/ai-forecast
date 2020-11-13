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
from datetime import datetime, timedelta


url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
key = "6vFwBIO5ZKEEPDpVKwkmfssrPdCMNtDdPSff4szG9k4lVLL9qkYIfTxhw6gEggcK9CA6dCD8GsrCDXe%2FU1zKYQ%3D%3D"


def weather_api(startdt):

    startdt = datetime.strptime(startdt, "%Y-%m-%d")

    addtime = timedelta(days=6)
    enddt = startdt + addtime

    startdt = startdt.strftime('%Y-%m-%d')
    enddt = enddt.strftime('%Y-%m-%d')

    startdt = int(startdt.replace('-', ''))
    enddt = int(enddt.replace('-', ''))

    startdt = str(startdt)
    enddt = str(enddt)

    print('step1 finished -------')
    queryParams_page1 = '?' + urlencode({

        "ServiceKey": unquote(key),
        "dataCd": "ASOS",
        "dateCd": "DAY",
        "numOfRows": "600",
        "pageNo": "1",
        "startDt": startdt,
        "endDt": enddt,
        "stnIds": "159",
        "dataType": "JSON"

    })

    queryURL_page1 = url + queryParams_page1
    response_page1 = requests.get(queryURL_page1)
    info_page1 = json.loads(response_page1.text)

    a = []
    for i in range(len(info_page1['response']['body']['items']['item'])):

        df = pd.DataFrame(info_page1['response']
                          ['body']['items']['item'][i], index=[0])

        a.append(df)

    print('step2 finished -------')

    weather_api_1 = pd.concat(a)

    weather_api_1 = weather_api_1[['tm', 'avgTa', 'avgRhm', 'avgPa', 'sumRn']]
    weather_api_1 = weather_api_1.rename({'tm': 'date', 'avgTa': 'mean_temp',
                                          'avgRhm': 'mean_humidity', 'avgPa': 'mean_pressure', 'sumRn': 'rain'}, axis=1)
    weather_api_1 = weather_api_1.reset_index(drop=True)
    weather_api_1 = weather_api_1.replace(r'', np.nan, regex=True)
    weather_api_1 = weather_api_1.fillna(0)
    weather_api_1 = weather_api_1.astype({'mean_temp': 'float', 'mean_humidity': 'float',
                                          'mean_pressure': 'float', 'rain': 'float'})
    print('step3 finished -------')

    return weather_api_1


def utc_to_date(utc):
    date = datetime.utcfromtimestamp(utc).strftime('%Y-%m-%d')

    return date


def future7_weather_api():

    url = 'https://api.openweathermap.org/data/2.5/onecall'
    key = "9688b3e45c54541ccc6c099da90380ab"

    queryParams_page1 = '?' + urlencode({

        "lat": 35.1028,
        "lon": 129.0403,
        "appid": unquote(key),
        "exclude": "hourly,minutely,current,alerts",
        "units": "metric"

    })

    queryURL_page1 = url + queryParams_page1
    response_page1 = requests.get(queryURL_page1)
    info_page1 = json.loads(response_page1.text)

    a = []
    for i in range(len(info_page1['daily'])):

        utc_num = info_page1['daily'][i]['dt']

        if 'rain' in list(info_page1['daily'][i].keys()):

            dict = {"date": utc_to_date(utc_num), 'mean_temp': info_page1['daily'][i]['temp']['day'],
                    'mean_humidity': info_page1['daily'][i]['humidity'],
                    'mean_pressure': info_page1['daily'][i]['pressure'],
                    'rain': info_page1['daily'][i]['rain']}

        else:

            dict = {"date": utc_to_date(utc_num), 'mean_temp': info_page1['daily'][i]['temp']['day'],
                    'mean_humidity': info_page1['daily'][i]['humidity'],
                    'mean_pressure': info_page1['daily'][i]['pressure'],
                    'rain': 0}

        predict = pd.DataFrame(dict, index=[0])

        a.append(predict)

    weather_pre = pd.concat(a).reset_index(drop=True)

    return weather_pre
