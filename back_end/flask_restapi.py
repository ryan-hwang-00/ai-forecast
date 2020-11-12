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

from predictor import predictor

url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
key = "NnpxwR7oA3LxPCsLEMG2CcvrkIZRLw0%2BHmz2ClUcOfaKvAMlySAiadvjQKqyQu0HorPtqAGZpj%2Bxfe6iSFyDKw%3D%3D"

meta_index = pd.DataFrame(
    data=[[1, '백산수2.0L', 'promotion_flag_1_bac_2',
           'sale_qty_1_bac_2', '1_bac2.hdf5'],
          [1, '백산수500ml', 'promotion_flag_1_bac_5',
           'sale_qty_1_bac_5', '1_bac5.hdf5'],
          [1, '신라면멀티', 'promotion_flag_1_sin',
           'sale_qty_1_sin', '1_sin.hdf5'],
          [1, '안성탕면멀티', 'promotion_flag_1_ans',
           'sale_qty_1_ans', '1_ans.hdf5'],
          [1, '진라면멀티(순한맛)', 'promotion_flag_1_jin',
           'sale_qty_1_jin', '1_jin.hdf5'],
          [6, '백산수2.0L', 'promotion_flag_6_bac_2',
           'sale_qty_6_bac_2', '6_bac2.hdf5'],
          [6, '백산수500ml', 'promotion_flag_6_bac_5',
           'sale_qty_6_bac_5', '6_bac5.hdf5'],
          [6, '신라면멀티', 'promotion_flag_6_sin',
           'sale_qty_6_sin', '6_sin.hdf5'],
          [6, '안성탕면멀티', 'promotion_flag_6_ans',
           'sale_qty_6_ans', '6_ans.hdf5'],
          [6, '진라면멀티(순한맛)', 'promotion_flag_6_jin', 'sale_qty_6_jin', '6_jin.hdf5']],
    columns=['store', 'product', 'promotion', 'sale', 'weight'])


app = Flask(__name__)
CORS(app)


@app.route('/date_info', methods=['POST'])
def seven_days():

    arrived_data = request.get_json()
    print(arrived_data)
    # start_date = arrived_data['selected_date']
    start_date = "2020-01-01"
    event_info = arrived_data['event_info']
    # break_info = arrived_data['break_info']
    break_info = 0

    print(start_date, event_info, break_info)

    return_df_7, merged_df = date_info(start_date, event_info, break_info)

    next_week_sales = predictor(merged_df, store_code=6,
                                product_name='백산수2.0L', predict_date='2020-01-07')
    next_week_sales = np.around(next_week_sales, 2)
    print(next_week_sales)
    result = {}

    for i in range(0, 7):
        j = i + 1
        result['day' + str(j)] = round(float(next_week_sales[i]), 2)

    print(result)
#    trainer(model_name='1_bac2.hdf5', store_code=1,
#            product_name='백산수2.0L', predict_date='2020-01-07')

    return result


if __name__ == "__main__":
    app.run()
