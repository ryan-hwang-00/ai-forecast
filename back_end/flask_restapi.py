
from flask_cors import CORS

from flask import Flask, request

import pandas as pd

from datetime import datetime, timedelta
<<<<<<< HEAD
=======

>>>>>>> 44ce09c400f9b89e4d3bfa74accca2f1ee69c990
from future7_dataframe import date_info, row_select

from predictor import predictor

from matplotlib import pyplot

from testtrainer import start_train

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

    print('arrived_data : ', arrived_data)

    start_date = arrived_data['selected_date']
    print('start_data >>>>', start_date)

    #     할인정보 시작
    pre_event_info = arrived_data['event_info']
    print('pre_event_info >>>>>>', pre_event_info)

    event_info = []
    for i in pre_event_info.keys():

        if pre_event_info[i] == 'true':
            event_info.append(i)

    print('event_info >>>>', event_info)
    #     할인정보 끝

    break_info = arrived_data['break_info']
    store_info = arrived_data['store_info']

    print('break_info >>>>', break_info)
    print('store_info>>> ', store_info)

<<<<<<< HEAD
=======
    product_info = arrived_data['item_info']

>>>>>>> 44ce09c400f9b89e4d3bfa74accca2f1ee69c990
    # 11/13 오전 11시 45분 수정

    merged_df = date_info(start_date, event_info, break_info)

    startdt = datetime.strptime(start_date, "%Y-%m-%d")

    predict_addtime = timedelta(days=6)

    predict_date = startdt + predict_addtime

    predict_date = predict_date.strftime('%Y-%m-%d')

    next_week_sales = predictor(merged_df, store_code=store_info,
                                product_name=product_info, predict_date=predict_date)

    result = {}

    addtime = timedelta(days=1)

    for i in range(0, 7):
        j = i + 1
        gg = {}
        dt = startdt.strftime('%Y-%m-%d')
        gg[dt] = round(float(next_week_sales[i]), 2)
        result['day' + str(j)] = gg
        startdt = startdt + addtime

    # print(result)

    return result


@app.route('/training', methods=['POST'])
def trainer():

    arrived_data = request.get_json()
    print('arrived_data : ', arrived_data)

    start_date = arrived_data['selected_date']
    print('start_data >>>>', start_date)

    #     할인정보 시작
    pre_event_info = arrived_data['event_info']
    print('pre_event_info >>>>>>', pre_event_info)

    event_info = []
    for i in pre_event_info.keys():

        if pre_event_info[i] == 'true':
            event_info.append(i)

    print('event_info >>>>', event_info)
    #     할인정보 끝

    break_info = arrived_data['break_info']
    store_info = arrived_data['store_info']

    print('break_info >>>>', break_info)
    print('store_info>>> ', store_info)

    product_info = arrived_data['item_info']

    return_df_7, merged_df = date_info(start_date, event_info, break_info)

    startdt = datetime.strptime(start_date, "%Y-%m-%d")

    train_subtracttime = timedelta(days=1)

    train_date = startdt - train_subtracttime

    train_date = train_date.strftime('%Y-%m-%d')

    predict_addtime = timedelta(days=6)

    predict_date = startdt + predict_addtime

    predict_date = predict_date.strftime('%Y-%m-%d')
    print("training init")

    ready_train = start_train(merged_df, store_info, product_info, train_date,
                              predict_date)

    score = ready_train.trainer()

    return {'loss': score[0], 'mse': score[1]}


if __name__ == "__main__":
    app.run()
