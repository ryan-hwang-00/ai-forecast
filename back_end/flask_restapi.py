from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from flask import Flask, request, jsonify

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import SimpleRNN, Dense, LSTM
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import math

import urllib.request
import xmltodict
import json
import sys
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
from datetime import datetime, timedelta
import weather2
from future7_dataframe import date_info, row_select

url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
key = "NnpxwR7oA3LxPCsLEMG2CcvrkIZRLw0%2BHmz2ClUcOfaKvAMlySAiadvjQKqyQu0HorPtqAGZpj%2Bxfe6iSFyDKw%3D%3D"


# df1=df1.drop('Unnamed: 0', axis=1)

# 날씨 api 함수 정의

# 날씨 api 함수 정의 끝

app = Flask(__name__)
CORS(app)


@app.route('/date_info', methods=['POST'])
def seven_days():

    arrived_data = request.get_json()
    start_date = arrived_data['selected_date']
    event_info = arrived_data['event_info']
    break_info = arrived_data['break_info']

    return_df_7, merged_df = date_info(start_date, event_info, break_info)

    print(merged_df)
    return return_df_7


# def date_info():
#     arrived_data = request.get_json()  # json 데이터를 받아옴
#     start_date = arrived_data['selected_date']
#     event_info = arrived_data['event_info']
#     break_info = arrived_data['break_info']
#     print('받은 Data : ', arrived_data)
#     print("예측 시작일 : ", start_date)
#     print('할인 요일 : ', event_info)
#     # print(type(event_info))
#     # weather_api import
#     weather_df = weather2.weather_api(start_date)
#     print('날씨 df 정보 : ', weather_df.info())
#     # weather_api_df생성 끝
#     # DataFrame 7행 추출
#     print('데이터 프레임 7행 추출 시작-------')
#     pre_in_num = row_select(df1, 'date', start_date)
#     index_start = int(pre_in_num[0])
#     df2 = df1[index_start:index_start + 7]
#     # Dataframe 추출 끝
#     # event 시작
#     print('할인 정보 리스트 작성 시작-------')
#     pre_event_list = []
#     event_info_for_merge = []
#     for i in event_info:
#         x = int(i)
#         pre_event_list.append(x)
#     aa = 5
#     print('str -> int 변경. pre_event_list : ', pre_event_list)
#     for i in df2['dow']:
#         if i in pre_event_list:
#             aa = 1
#         else:
#             aa = 0
#         event_info_for_merge.append(aa)
#     print('event_days_list : ', event_info_for_merge)
#     df2['promotion_flag'] = event_info_for_merge
#     # event 끝
#     # break_info 시작
#     print('휴일정보 적용 시작 -------')
#     break_list_for_merge = [0, 0, 0, 0, 0, 0]
#     if break_info == '1':
#         break_list_for_merge.append(1)
#     else:
#         break_list_for_merge.append(0)
#     if break_list_for_merge[-1] == 1:
#         break_check = '일요휴무'
#     else:
#         break_check = '일요일 정상영업'
#     df2['break'] = break_list_for_merge
#     print('휴무 여부 : ', str(break_check))
#     # break_info 끝
#     print('Dataframe 확인 : ', df2)
#     # DF merge
#     merged_df = pd.merge(df2, weather_df)
#     print(' ')
#     print('merged_DF : ', merged_df)
#     # test_return 코드 나중에 지우고 사용
#     return_data = {}
#     return_data['day'] = int(df2['day'].iloc[5])
#     return_data['promotion'] = int(df2['promotion_flag'].iloc[3])
#     # test_return 코드 끝
#     print('return data : ', return_data)
#     return jsonify(return_data)
if __name__ == "__main__":
    app.run()
