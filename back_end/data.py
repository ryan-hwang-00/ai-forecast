from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
import os
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, LSTM, Bidirectional, Activation, LeakyReLU
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard, ReduceLROnPlateau
from tensorflow.keras.backend import square, mean
from collections import Counter
from matplotlib import rc, font_manager
from keras import optimizers
from keras.wrappers.scikit_learn import KerasClassifier
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.utils import plot_model
import graphviz

import seaborn as sns
from matplotlib import rc, font_manager


def get_sequence(x_train, x_train_1, y_train, sequence_x=21, sequence_y=7):

    m = len(x_train) - (sequence_x + sequence_y) + 1

    feature_x = x_train.shape[-1]
    feature_x_1 = x_train_1.shape[-1]

    x = np.zeros((m, sequence_x, feature_x), np.float32)

    x_1 = np.zeros((m, sequence_y, feature_x_1), np.float32)

    y = np.zeros((m, sequence_y, 1), np.float32)

    for i in range(m):

        x[i] = x_train[i:i+sequence_x]
        x_1[i] = x_train_1[i+sequence_x:i+sequence_x+sequence_y]
        y[i] = y_train[i+sequence_x:i+sequence_x+sequence_y, 0:1]

    return x, x_1, y


def detect_outliers(df, n, features):
    outlier_indices = []
    for col in features:
        Q1 = np.percentile(df[col], 25)
        Q3 = np.percentile(df[col], 75)
        IQR = Q3 - Q1

        outlier_step = 2 * IQR

        outlier_list_col = df[(df[col] < Q1 - outlier_step)
                              | (df[col] > Q3 + outlier_step)].index
#         print(outlier_list_col)
        outlier_indices.extend(outlier_list_col)

#     print(outlier_indices)
    outlier_indices = Counter(outlier_indices)
#     print(outlier_indices)
    multiple_outliers = list(k for k, v in outlier_indices.items() if v > n)

    return multiple_outliers


def sep_xy(df, x_columns, x_1_columns, sale_qty='sale_qty_1_bac_2'):
    x_df = df[x_columns]
#      'man_pop', 'woman_pop', '10s', '20s',,'trend'
#        '30s', '40s', '50s', '60s', '70s',

    x_df_1 = df[x_1_columns]

    # 'national_holiday',
    x_df = pd.get_dummies(x_df)
    x_df_1 = pd.get_dummies(x_df_1)

    y_df = df[[sale_qty]]

    x_df = x_df.values
    x_df_1 = x_df_1.values
    y_df = y_df.values
#     if get_window == True:
#         dataset = []
#         for i in range(len(x_df)-window_size):
#             subset = x_df[i:(i+window_size)]
#             dataset.append(item for item in subset)
    return x_df, x_df_1, y_df


def sep_data(datasets='AI_Sale_ver3.0.csv',
             store_code=1,
             product_name='백산수2.0L',
             train_date='2019-12-24',
             predict_date='2019-12-31'):

    meta_index = pd.DataFrame(
        data=[[1, '백산수2.0L', 'promotion_flag_1_bac_2', 'sale_qty_1_bac_2', '1_bac2.hdf5'],
              [1, '백산수500ml', 'promotion_flag',
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
               'sale_qty_6_sin', ' 6_jin.hdf5'],
              [6, '안성탕면멀티', 'promotion_flag_6_ans',
               'sale_qty_6_ans', '6_ans.hdf5'],
              [6, '진라면멀티(순한맛)', 'promotion_flag_6_jin', 'sale_qty_6_jin', '6_sin.hdf5']],
        columns=['store', 'product', 'promotion', 'sale', 'weight'])

    promotion = meta_index[(meta_index['store'] == store_code) & (
        meta_index['product'] == product_name)].iloc[0]['promotion']

    sale_qty = meta_index[(meta_index['store'] == store_code) & (
        meta_index['product'] == product_name)].iloc[0]['sale']

    df = pd.read_csv(datasets, encoding='euc-kr', index_col=0)

    df['store_code'] = df['store_code'].astype('object')

    df = pd.get_dummies(
        df, columns=['product_name', 'store_code', 'dow', 'holi_name'])

    df_1 = df['store_code_1'] == 1
    df_6 = df['store_code_6'] == 1
    df_bac_2 = df['product_name_백산수2.0L'] == 1
    df_bac_5 = df['product_name_백산수500ml'] == 1
    df_sin = df['product_name_신라면멀티'] == 1
    df_ans = df['product_name_안성탕면멀티'] == 1
    df_jin = df['product_name_진라면멀티(순한맛)'] == 1

    df_1_bac_2 = df[df_1 & df_bac_2]
    df_6_bac_2 = df[df_6 & df_bac_2]
    df_1_bac_5 = df[df_1 & df_bac_5]
    df_6_bac_5 = df[df_6 & df_bac_5]
    df_1_sin = df[df_1 & df_sin]
    df_6_sin = df[df_6 & df_sin]
    df_1_ans = df[df_1 & df_ans]
    df_6_ans = df[df_6 & df_ans]
    df_1_jin = df[df_1 & df_jin]
    df_6_jin = df[df_6 & df_jin]

    df_merge = pd.merge(df_1_bac_2, df_6_bac_2, how='outer',
                        on='date', suffixes=('_1_bac_2', '_6_bac_2'))
    df_merge = pd.merge(df_merge, df_1_bac_5, how='outer',
                        on='date', suffixes=('', '_1_bac_5'))
    df_merge = pd.merge(df_merge, df_6_bac_5, how='outer',
                        on='date', suffixes=('', '_6_bac_5'))
    df_merge = pd.merge(df_merge, df_1_sin, how='outer',
                        on='date', suffixes=('', '_1_sin'))
    df_merge = pd.merge(df_merge, df_6_sin, how='outer',
                        on='date', suffixes=('', '_6_sin'))
    df_merge = pd.merge(df_merge, df_1_ans, how='outer',
                        on='date', suffixes=('', '_1_ans'))
    df_merge = pd.merge(df_merge, df_6_ans, how='outer',
                        on='date', suffixes=('', '_6_ans'))
    df_merge = pd.merge(df_merge, df_1_jin, how='outer',
                        on='date', suffixes=('', '_1_jin'))
    df_merge = pd.merge(df_merge, df_6_jin, how='outer',
                        on='date', suffixes=('', '_6_jin'))

    df_merge_index_date = df_merge.set_index('date')

    df = df_merge_index_date.sort_index()

    df = df[df['flag'] == 1]

    df['sale_qty_1_bac_5'] = df['sale_qty']

    df.loc[:, 'sale_qty_1_bac_2'] = df.loc[:, 'sale_qty_1_bac_2'].clip(lower=0)
    df.loc[:, 'sale_qty_6_bac_2'] = df.loc[:, 'sale_qty_6_bac_2'].clip(lower=0)
    df.loc[:, 'sale_qty_1_bac_5'] = df.loc[:, 'sale_qty_1_bac_5'].clip(lower=0)
    df.loc[:, 'sale_qty_6_bac_5'] = df.loc[:, 'sale_qty_6_bac_5'].clip(lower=0)
    df.loc[:, 'sale_qty_1_sin'] = df.loc[:, 'sale_qty_1_sin'].clip(lower=0)
    df.loc[:, 'sale_qty_6_sin'] = df.loc[:, 'sale_qty_6_sin'].clip(lower=0)
    df.loc[:, 'sale_qty_1_ans'] = df.loc[:, 'sale_qty_1_ans'].clip(lower=0)
    df.loc[:, 'sale_qty_6_ans'] = df.loc[:, 'sale_qty_6_ans'].clip(lower=0)
    df.loc[:, 'sale_qty_1_jin'] = df.loc[:, 'sale_qty_1_jin'].clip(lower=0)
    df.loc[:, 'sale_qty_6_jin'] = df.loc[:, 'sale_qty_6_jin'].clip(lower=0)

    # Outliers_to_drop = detect_outliers(df, 0, ['sale_qty'])

    df = df.reset_index()

    # 찾은 아웃라이어를 바꿔줍니다.
    sales_columns = ['sale_qty_1_bac_2', 'sale_qty_6_bac_2', 'sale_qty_1_bac_5', 'sale_qty_6_bac_5',
                     'sale_qty_1_sin', 'sale_qty_6_sin', 'sale_qty_1_ans', 'sale_qty_6_ans', 'sale_qty_1_jin', 'sale_qty_6_jin']

    for sale in sales_columns:
        Outliers_to_drop = detect_outliers(df, 0, [sale])
        df.loc[Outliers_to_drop, sale] = np.percentile(df[[sale]], 75)*2

    df_train = df.loc[:df[df['date'] == train_date].index[0]]
    df_test = df.loc[:df[df['date'] == predict_date].index[0]]

    df = df.drop(columns='date')
    df_train = df_train.drop(columns='date')
    df_test = df_test.drop(columns='date')

    x_columns = ['year_1_bac_2', 'month_1_bac_2', 'day_1_bac_2',
                 'weekday_1_bac_2', 'weeknum_1_bac_2',
                 'flag_1_bac_2', 'weekend_1_bac_2', 'national_holiday_1_bac_2',
                 'nat_long_holiday_1_bac_2', 'break_1_bac_2', 'mean_temp_1_bac_2',
                 # 최대풍속은 빼자.
                 'precipitation_1day_1_bac_2', 'max_windspeed_1_bac_2',
                 'mean_humidity_1_bac_2', 'mean_pressure_1_bac_2',
                 'sin_month_1_bac_2', 'cos_month_1_bac_2',
                 'sin_day_1_bac_2', 'cos_day_1_bac_2', 'sin_weekday_1_bac_2', 'dow_금요일_1_bac_2', 'dow_목요일_1_bac_2',
                 'dow_수요일_1_bac_2', 'dow_월요일_1_bac_2', 'dow_일요일_1_bac_2',
                 'dow_토요일_1_bac_2', 'dow_화요일_1_bac_2', 'holi_name_0_1_bac_2',
                 'holi_name_1월1일_1_bac_2', 'holi_name_개천절_1_bac_2',
                 'holi_name_광복절_1_bac_2', 'holi_name_국회의원선거일_1_bac_2',
                 'holi_name_기독탄신일_1_bac_2', 'holi_name_대체공휴일_1_bac_2',
                 'holi_name_대체휴무일_1_bac_2', 'holi_name_대통령선거일_1_bac_2',
                 'holi_name_부처님오신날_1_bac_2', 'holi_name_삼일절_1_bac_2',
                 'holi_name_석가탄신일_1_bac_2', 'holi_name_설날_1_bac_2',
                 'holi_name_신정_1_bac_2', 'holi_name_어린이날_1_bac_2',
                 'holi_name_임시공휴일_1_bac_2', 'holi_name_전국동시지방선거_1_bac_2',
                 'holi_name_추석_1_bac_2', 'holi_name_한글날_1_bac_2',
                 'holi_name_현충일_1_bac_2',
                 'promotion_flag_1_bac_2', 'sale_qty_1_bac_2',
                 'promotion_flag_6_bac_2', 'sale_qty_6_bac_2',
                 'promotion_flag', 'sale_qty_1_bac_5',
                 'promotion_flag_6_bac_5', 'sale_qty_6_bac_5',
                 'promotion_flag_1_sin', 'sale_qty_1_sin',
                 'promotion_flag_6_sin', 'sale_qty_6_sin',
                 'promotion_flag_1_ans', 'sale_qty_1_ans',
                 'promotion_flag_6_ans', 'sale_qty_6_ans',
                 'promotion_flag_1_jin', 'sale_qty_1_jin',
                 'promotion_flag_6_jin', 'sale_qty_6_jin']

    x_1_columns = ['year_1_bac_2', 'month_1_bac_2', 'day_1_bac_2',
                   'weekday_1_bac_2', 'weeknum_1_bac_2',
                   'flag_1_bac_2', 'weekend_1_bac_2', 'national_holiday_1_bac_2',
                   'nat_long_holiday_1_bac_2', 'break_1_bac_2', 'mean_temp_1_bac_2',
                   'precipitation_1day_1_bac_2', 'max_windspeed_1_bac_2',
                   'mean_humidity_1_bac_2', 'mean_pressure_1_bac_2',
                   'sin_month_1_bac_2', 'cos_month_1_bac_2',
                   'sin_day_1_bac_2', 'cos_day_1_bac_2', 'sin_weekday_1_bac_2', 'dow_금요일_1_bac_2', 'dow_목요일_1_bac_2',
                   'dow_수요일_1_bac_2', 'dow_월요일_1_bac_2', 'dow_일요일_1_bac_2',
                   'dow_토요일_1_bac_2', 'dow_화요일_1_bac_2', 'holi_name_0_1_bac_2',
                   'holi_name_1월1일_1_bac_2', 'holi_name_개천절_1_bac_2',
                   'holi_name_광복절_1_bac_2', 'holi_name_국회의원선거일_1_bac_2',
                   'holi_name_기독탄신일_1_bac_2', 'holi_name_대체공휴일_1_bac_2',
                   'holi_name_대체휴무일_1_bac_2', 'holi_name_대통령선거일_1_bac_2',
                   'holi_name_부처님오신날_1_bac_2', 'holi_name_삼일절_1_bac_2',
                   'holi_name_석가탄신일_1_bac_2', 'holi_name_설날_1_bac_2',
                   'holi_name_신정_1_bac_2', 'holi_name_어린이날_1_bac_2',
                   'holi_name_임시공휴일_1_bac_2', 'holi_name_전국동시지방선거_1_bac_2',
                   'holi_name_추석_1_bac_2', 'holi_name_한글날_1_bac_2',
                   'holi_name_현충일_1_bac_2',
                   promotion]

    return df, df_train, df_test, sale_qty, x_columns, x_1_columns


def scaled_origin(sequence_x=180 * 4,
                  sequence_y=7):

    df, df_train, df_test, sale_qty, x_columns, x_1_columns = sep_data()

    x_df, x_df_1, y_df = sep_xy(df, x_columns, x_1_columns, sale_qty=sale_qty)

    x_scaler = MinMaxScaler()
    x_1_scaler = MinMaxScaler()
    y_scaler = MinMaxScaler()

    x_df_scaled = x_scaler.fit_transform(x_df)
    x_df_1_scaled = x_1_scaler.fit_transform(x_df_1)
    y_df_scaled = y_scaler.fit_transform(y_df)

    x_df_scaled, x_df_1_scaled, y_df_scaled = get_sequence(
        x_df_scaled, x_df_1_scaled, y_df_scaled, sequence_x=sequence_x, sequence_y=sequence_y)

    column_num_x = len(x_columns)

    column_num_x_1 = len(x_1_columns)

    return x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1, x_columns, x_1_columns, sale_qty


def scaled_data(sequence_x=180 * 4,
                sequence_y=7,
                df_train=pd.DataFrame):

    x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1, x_columns, x_1_columns, sale_qty = scaled_origin()

    x_train, x_train_1, y_train = sep_xy(
        df_train,  x_columns, x_1_columns, sale_qty=sale_qty)

    x_train_scaled = x_scaler.transform(x_train)
    x_train_1_scaled = x_1_scaler.transform(x_train_1)
    y_train_scaled = y_scaler.transform(y_train)

    x_train_scaled, x_train_1_scaled, y_train_scaled = get_sequence(
        x_train_scaled, x_train_1_scaled, y_train_scaled, sequence_x=sequence_x, sequence_y=sequence_y)

    return x_train_scaled, x_train_1_scaled, y_train_scaled
