
from sklearn.preprocessing import MinMaxScaler

import pandas as pd
import numpy as np

from collections import Counter

from future7_dataframe import date_info


class prepareData:

    def __init__(self, merged_df, train='AI_Sale_ver4.0.csv',
                 product_name='백산수2.0L',
                 store_code=1,
                 train_date='2019-12-31',
                 predict_date='2020-01-07',
                 sequence_x=180 * 4,
                 sequence_y=7
                 ):

        self.merged_df = merged_df
        self.train = train
        self.product_name = product_name
        self.store_code = store_code
        self.train_date = train_date
        self.predict_date = predict_date
        self.sequence_x = sequence_x
        self.sequence_y = sequence_y

        self.meta_index = pd.DataFrame(
            data=[[1, '백산수2.0L', 'promotion_flag_1_bac_2',
                   'sale_qty_1_bac_2', '1_bac2.hdf5', 'outliersale_qty_1_bac_2'],
                  [1, '백산수500ml', 'promotion_flag_1_bac_5',
                   'sale_qty_1_bac_5', '1_bac5.hdf5', 'outliersale_qty_1_bac_5'],
                  [1, '신라면멀티', 'promotion_flag_1_sin',
                   'sale_qty_1_sin', '1_sin.hdf5', 'outliersale_qty_1_sin'],
                  [1, '안성탕면멀티', 'promotion_flag_1_ans',
                   'sale_qty_1_ans', '1_ans.hdf5', 'outliersale_qty_1_ans'],
                  [1, '진라면멀티(순한맛)', 'promotion_flag_1_jin',
                   'sale_qty_1_jin', '1_jin.hdf5', 'outliersale_qty_1_jin'],
                  [6, '백산수2.0L', 'promotion_flag_6_bac_2',
                   'sale_qty_6_bac_2', '6_bac2.hdf5', 'outliersale_qty_6_bac_2'],
                  [6, '백산수500ml', 'promotion_flag_6_bac_5',
                   'sale_qty_6_bac_5', '6_bac5.hdf5', 'outliersale_qty_6_bac_5'],
                  [6, '신라면멀티', 'promotion_flag_6_sin',
                   'sale_qty_6_sin', ' 6_sin.hdf5', 'outliersale_qty_6_sin'],
                  [6, '안성탕면멀티', 'promotion_flag_6_ans',
                   'sale_qty_6_ans', '6_ans.hdf5', 'outliersale_qty_6_ans'],
                  [6, '진라면멀티(순한맛)', 'promotion_flag_6_jin',
                   'sale_qty_6_jin', '6_jin.hdf5', 'outliersale_qty_6_jin']],
            columns=['store', 'product', 'promotion', 'sale', 'weight', 'outlier'])

        self.sale_qty = self.meta_index[(self.meta_index['store'] == self.store_code) & (
            self.meta_index['product'] == self.product_name)].iloc[0]['sale']

        self.promotion = self.meta_index[(self.meta_index['store'] == self.store_code) & (
            self.meta_index['product'] == self.product_name)].iloc[0]['promotion']

        self.outlier = self.meta_index[(self.meta_index['store'] == self.store_code) & (
            self.meta_index['product'] == self.product_name)].iloc[0]['outlier']

    def get_sequence(self, x_train, x_train_1, y_train, sequence_x=21, sequence_y=7):

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

    def detect_outliers(self, df, n, features):
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
        multiple_outliers = list(
            k for k, v in outlier_indices.items() if v > n)

        return multiple_outliers

    def sep_xy(self, df, x_columns, x_1_columns):
        x_df = df[x_columns]
    #      'man_pop', 'woman_pop', '10s', '20s',,'trend'
    #        '30s', '40s', '50s', '60s', '70s',

        x_df_1 = df[x_1_columns]

        # 'national_holiday',
        x_df = pd.get_dummies(x_df)
        x_df_1 = pd.get_dummies(x_df_1)

        y_df = df[[self.sale_qty]]

        x_df = x_df.values
        x_df_1 = x_df_1.values
        y_df = y_df.values
    #     if get_window == True:
    #         dataset = []
    #         for i in range(len(x_df)-window_size):
    #             subset = x_df[i:(i+window_size)]
    #             dataset.append(item for item in subset)
        return x_df, x_df_1, y_df

    def sep_data(self):

        datasets = 'AI_Sale_ver3.5.csv'
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

        df.loc[:, 'sale_qty_1_bac_2'] = df.loc[:,
                                               'sale_qty_1_bac_2'].clip(lower=0)
        df.loc[:, 'sale_qty_6_bac_2'] = df.loc[:,
                                               'sale_qty_6_bac_2'].clip(lower=0)
        df.loc[:, 'sale_qty_1_bac_5'] = df.loc[:,
                                               'sale_qty_1_bac_5'].clip(lower=0)
        df.loc[:, 'sale_qty_6_bac_5'] = df.loc[:,
                                               'sale_qty_6_bac_5'].clip(lower=0)
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
            Outliers_to_drop = self.detect_outliers(df, 0, [sale])
            df.loc[Outliers_to_drop, sale] = np.percentile(df[[sale]], 75)*2
            df.loc[Outliers_to_drop, 'outlier'+sale] = 1

        df_train = df.loc[:df[df['date'] == self.train_date].index[0]]
        df_test = df.loc[:df[df['date'] == self.predict_date].index[0]]

        # df = df.drop(columns='date')
        df_train = df_train.drop(columns='date')
        df_test = df_test.drop(columns='date')

        x_columns = ['date', 'year_1_bac_2', 'month_1_bac_2', 'day_1_bac_2',
                     'weekday_1_bac_2', 'weeknum_1_bac_2', 'weekend_1_bac_2', 'national_holiday_1_bac_2',
                     'break_1_bac_2', 'mean_temp_1_bac_2',
                     'precipitation_1day_1_bac_2',
                     'mean_humidity_1_bac_2', 'mean_pressure_1_bac_2',
                     'sin_month_1_bac_2', 'cos_month_1_bac_2',
                     'sin_day_1_bac_2', 'cos_day_1_bac_2',
                     'sin_weekday_1_bac_2', 'cos_weekday_1_bac_2',
                     'sin_weeknum_1_bac_2', 'cos_weeknum_1_bac_2',
                     'dow_금요일_1_bac_2', 'dow_목요일_1_bac_2',
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
                     'promotion_flag_6_jin', 'sale_qty_6_jin',
                     'outliersale_qty_1_bac_2', 'outliersale_qty_6_bac_2',
                     'outliersale_qty_1_bac_5', 'outliersale_qty_6_bac_5',
                     'outliersale_qty_1_sin', 'outliersale_qty_6_sin',
                     'outliersale_qty_1_ans', 'outliersale_qty_6_ans',
                     'outliersale_qty_1_jin', 'outliersale_qty_6_jin']

        x_1_columns = ['year_1_bac_2', 'month_1_bac_2', 'day_1_bac_2',
                       'weekday_1_bac_2', 'weeknum_1_bac_2', 'weekend_1_bac_2', 'national_holiday_1_bac_2',
                       'break_1_bac_2', 'mean_temp_1_bac_2',
                       'precipitation_1day_1_bac_2',
                       'mean_humidity_1_bac_2', 'mean_pressure_1_bac_2',
                       'sin_month_1_bac_2', 'cos_month_1_bac_2',
                       'sin_day_1_bac_2', 'cos_day_1_bac_2',
                       'sin_weekday_1_bac_2', 'cos_weekday_1_bac_2',
                       'sin_weeknum_1_bac_2', 'cos_weeknum_1_bac_2',
                       'dow_금요일_1_bac_2', 'dow_목요일_1_bac_2',
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
                       self.promotion]
        # df.to_csv('AI_Sale_ver5.0.csv', encoding='euc-kr', columns=x_columns)
        return df, df_train, df_test, self.sale_qty, x_columns, x_1_columns

    def sep_data2(self):

        past = pd.read_csv(self.train, encoding='euc-kr', index_col=0)

        if past.iloc[-1, 0] >= self.train_date:

            past = past.loc[:past[past['date'] == self.train_date].index[0]]

        else:
            past = past

        future = self.merged_df

        future['sin_month'] = np.sin(2*np.pi*future.month/12)
        future['cos_month'] = np.cos(2*np.pi*future.month/12)
        future['sin_day'] = np.sin(2*np.pi*future.day/past.day.max())
        future['cos_day'] = np.cos(2*np.pi*future.day/past.day.max())
        future['sin_weekday'] = np.sin(
            2*np.pi*future.weekday/past.weekday.max())
        future['cos_weekday'] = np.cos(
            2*np.pi*future.weekday/past.weekday.max())
        future['sin_weeknum'] = np.sin(2*np.pi*1/past.weeknum.max())
        future['cos_weeknum'] = np.cos(2*np.pi*1/past.weeknum.max())

        weekends = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 1}

        future['weekend'] = future['weekday'].apply(lambda x: weekends[x])

        future['holi_name'] = future['holiday_name']
        future = future.drop(columns='holiday_name')

        future = pd.get_dummies(future, columns=['dow', 'holi_name'])

        future['precipitation_1day'] = future['rain']
        future = future.drop(columns='rain')

        future[self.promotion] = future['promotion_flag']
        future[self.outlier] = future['outlier']

        future = future.drop(columns='promotion_flag')
        future = future.drop(columns='outlier')

        df = past.append(future, ignore_index=True)
        # print(df)
        df_train = df.loc[:df[df['date'] == self.train_date].index[0]]
        df_test = df.loc[:df[df['date'] == self.predict_date].index[0]]

        df = df.drop(columns='date')
        df_train = df_train.drop(columns='date')
        df_test = df_test.drop(columns='date')

        # print(df_test.tail(20))

        x_columns = ['year', 'month', 'day',
                     'weekday', 'weeknum', 'weekend', 'national_holiday',
                     'break', 'mean_temp',
                     'precipitation_1day',
                     'mean_humidity', 'mean_pressure',
                     'sin_month', 'cos_month',
                     'sin_day', 'cos_day',
                     'sin_weekday', 'cos_weekday',
                     'sin_weeknum', 'cos_weeknum',
                     'dow_금요일', 'dow_목요일',
                     'dow_수요일', 'dow_월요일', 'dow_일요일',
                     'dow_토요일', 'dow_화요일', 'holi_name_0',
                     'holi_name_1월1일', 'holi_name_개천절',
                     'holi_name_광복절', 'holi_name_국회의원선거일',
                     'holi_name_기독탄신일', 'holi_name_대체공휴일',
                     'holi_name_대체휴무일', 'holi_name_대통령선거일',
                     'holi_name_부처님오신날', 'holi_name_삼일절',
                     'holi_name_석가탄신일', 'holi_name_설날',
                     'holi_name_신정', 'holi_name_어린이날',
                     'holi_name_임시공휴일', 'holi_name_전국동시지방선거',
                     'holi_name_추석', 'holi_name_한글날',
                     'holi_name_현충일',
                     'promotion_flag_1_bac_2', 'sale_qty_1_bac_2',
                     'promotion_flag_6_bac_2', 'sale_qty_6_bac_2',
                     'promotion_flag_1_bac_5', 'sale_qty_1_bac_5',
                     'promotion_flag_6_bac_5', 'sale_qty_6_bac_5',
                     'promotion_flag_1_sin', 'sale_qty_1_sin',
                     'promotion_flag_6_sin', 'sale_qty_6_sin',
                     'promotion_flag_1_ans', 'sale_qty_1_ans',
                     'promotion_flag_6_ans', 'sale_qty_6_ans',
                     'promotion_flag_1_jin', 'sale_qty_1_jin',
                     'promotion_flag_6_jin', 'sale_qty_6_jin',
                     'outliersale_qty_1_bac_2', 'outliersale_qty_6_bac_2',
                     'outliersale_qty_1_bac_5', 'outliersale_qty_6_bac_5',
                     'outliersale_qty_1_sin', 'outliersale_qty_6_sin',
                     'outliersale_qty_1_ans', 'outliersale_qty_6_ans',
                     'outliersale_qty_1_jin', 'outliersale_qty_6_jin']

        x_1_columns = ['year', 'month', 'day',
                       'weekday', 'weeknum', 'weekend', 'national_holiday',
                       'break', 'mean_temp',
                       'precipitation_1day',
                       'mean_humidity', 'mean_pressure',
                       'sin_month', 'cos_month',
                       'sin_day', 'cos_day',
                       'sin_weekday', 'cos_weekday',
                       'sin_weeknum', 'cos_weeknum',
                       'dow_금요일', 'dow_목요일',
                       'dow_수요일', 'dow_월요일', 'dow_일요일',
                       'dow_토요일', 'dow_화요일', 'holi_name_0',
                       'holi_name_1월1일', 'holi_name_개천절',
                       'holi_name_광복절', 'holi_name_국회의원선거일',
                       'holi_name_기독탄신일', 'holi_name_대체공휴일',
                       'holi_name_대체휴무일', 'holi_name_대통령선거일',
                       'holi_name_부처님오신날', 'holi_name_삼일절',
                       'holi_name_석가탄신일', 'holi_name_설날',
                       'holi_name_신정', 'holi_name_어린이날',
                       'holi_name_임시공휴일', 'holi_name_전국동시지방선거',
                       'holi_name_추석', 'holi_name_한글날',
                       'holi_name_현충일',
                       self.promotion, self.outlier]

        return df, df_train, df_test, self.sale_qty, x_columns, x_1_columns

    def scaled_origin(self):

        df, df_train, df_test, sale_qty, x_columns, x_1_columns = self.sep_data2(
        )

        x_df, x_df_1, y_df = self.sep_xy(
            df, x_columns, x_1_columns)

        x_scaler = MinMaxScaler()
        x_1_scaler = MinMaxScaler()
        y_scaler = MinMaxScaler()

        x_df_scaled = x_scaler.fit_transform(x_df)
        x_df_1_scaled = x_1_scaler.fit_transform(x_df_1)
        y_df_scaled = y_scaler.fit_transform(y_df)

        x_df_scaled, x_df_1_scaled, y_df_scaled = self.get_sequence(
            x_df_scaled, x_df_1_scaled, y_df_scaled, sequence_x=self.sequence_x, sequence_y=self.sequence_y)

        column_num_x = len(x_columns)

        column_num_x_1 = len(x_1_columns)

        return x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1, x_columns, x_1_columns, sale_qty

    def scaled_data(self, df_train):

        x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1, x_columns, x_1_columns, sale_qty = self.scaled_origin()

        x_train, x_train_1, y_train = self.sep_xy(
            df_train,  x_columns, x_1_columns)

        x_train_scaled = x_scaler.transform(x_train)
        x_train_1_scaled = x_1_scaler.transform(x_train_1)
        y_train_scaled = y_scaler.transform(y_train)

        x_train_scaled, x_train_1_scaled, y_train_scaled = self.get_sequence(
            x_train_scaled, x_train_1_scaled, y_train_scaled, sequence_x=self.sequence_x, sequence_y=self.sequence_y)

        return x_train_scaled, x_train_1_scaled, y_train_scaled


# sep_data()
