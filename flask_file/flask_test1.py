from flask import Flask, request, jsonify

import pandas as pd
import numpy as np
# from keras.models import Sequential
# from keras.layers import SimpleRNN, Dense, LSTM
# from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
# import math


df1=pd.read_csv('./data2/F1_12월23일까지_val이용_7일예측_전반부_for_ensemble_365_to_7_RMSE_202Num_7610.csv')
flask_a=df1['predicted_qty'][5]
app = Flask(__name__)


@app.route('/userLogin', methods=['POST'])
def userLogin2():
    arrived_data = request.get_json()# json 데이터를 받아옴
    print('타입 : ',type(arrived_data)) #json 이기 때문에 user는 dict 타입.
    print(arrived_data)
    return_data={}
    return_data['real_y']=df1['real_y'][arrived_data['real_y']]
    return_data['mean_temp'] = df1['real_y'][arrived_data['mean_temp']]
    # arrived_data['name2']='test2' 변수 user가 dict 형태이기 때문에 새로운 쌍을 지정해주면 변수 저장 가능
    print(return_data)

    return jsonify(return_data)  # 받아온 데이터를 다시 전송


@app.route('/environments/<language>')
def environments(language):
    return jsonify({"language": language})


if __name__ == "__main__":
    app.run()