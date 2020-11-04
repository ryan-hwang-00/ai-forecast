from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential, load_model
from sklearn import preprocessing
from modeling import create_model
from data import preprocessing_data
import data
from datetime import datetime
from predictor import predictor

app = Flask(__name__)
CORS(app)


@app.route("/api/v4.0/forecast/sales", methods=['POST'])
def pre():

    horizon = int(request.json['horizon'])
    start_date = '2020-01-01'
    test = preprocessing_data()[0]

    # x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1, x_test_scaled, x_test_1_scaled, y_test_scaled = data.preprocessing_data()
    # sequence_x = 180 * 4
    # sequence_y = 7
    # model = create_model(column_num_x, column_num_x_1, sequence_x, sequence_y)
    # a = prediction(x_test_scaled, x_test_1_scaled,
    # y_scaler, weight='1_bac2.hdf5', model=model)

    # 날짜 지정하면 그 날짜로부터 7일의 날짜 인덱스로 넣을 것.

    pre = predictor()[-horizon:]

    index_1 = (test['date'] == start_date).index[0]
    date_7days = test['date'].loc[index_1: index_1+6]

    pre = pre * 4123
    pre = pd.DataFrame(pre, index=date_7days)
    ret = pre.to_json(orient='columns', date_format='iso')

    return ret


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=3000)
