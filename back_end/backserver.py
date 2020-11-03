from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential, load_model
from sklearn import preprocessing
from prediction import prediction
from modeling import create_model
from data import preprocessing_data
import data
from datetime import datetime


app = Flask(__name__)
CORS(app)


@app.route("/api/v2.0/forecast/sales", methods=['POST'])
def pre():

    horizon = int(request.json['horizon'])

    x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1, x_test_scaled, x_test_1_scaled, y_test_scaled = data.preprocessing_data()

    sequence_x = 180 * 4
    sequence_y = 7

    model = create_model(column_num_x, column_num_x_1, sequence_x, sequence_y)

    next_week_sales = prediction(x_test_scaled, x_test_1_scaled,
                                 y_scaler, weight='1_bac2.hdf5', model=model)

    next_week_sales = pd.DataFrame(next_week_sales)[-horizon:]

    date = {'date': ['2020-01-01', '2020-01-02', '2020-01-03',
                     '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07']}

    data = pd.DataFrame(date)

    df = pd.merge(data, next_week_sales, how='outer',
                  left_index=True, right_index=True)

    df['date'] = df['date'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))

    # print(next_week_sales)
    df = df.to_json(
        orient='records', date_format='iso')
    return df


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=3000)
