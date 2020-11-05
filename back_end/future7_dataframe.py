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
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify


df1 = pd.read_csv('./data/date_info.csv')


def row_select(dataframe, column, value):
    second_df = dataframe[dataframe[column] == value]

    index_num = second_df.index.values.tolist()
    return index_num


def date_info(start_date, event_info, break_info):

    arrived_data = request.get_json()  # json 데이터를 받아옴

    weather_df = weather2.weather_api(start_date)

    pre_in_num = row_select(df1, 'date', start_date)
    index_start = int(pre_in_num[0])
    df2 = df1[index_start:index_start + 7]

    pre_event_list = []
    event_info_for_merge = []
    for i in event_info:
        x = int(i)
        pre_event_list.append(x)

    aa = 5
    for i in df2['dow']:
        if i in pre_event_list:
            aa = 1
        else:
            aa = 0

        event_info_for_merge.append(aa)

    df2['promotion_flag'] = event_info_for_merge

    break_list_for_merge = [0, 0, 0, 0, 0, 0]
    if break_info == '1':
        break_list_for_merge.append(1)
    else:
        break_list_for_merge.append(0)
    if break_list_for_merge[-1] == 1:
        break_check = '일요휴무'
    else:
        break_check = '일요일 정상영업'
    df2['break'] = break_list_for_merge

    merged_df = pd.merge(df2, weather_df)

    return_data = {}
    return_data['day'] = int(df2['day'].iloc[5])
    return_data['promotion'] = int(df2['promotion_flag'].iloc[3])

    return return_data, merged_df
