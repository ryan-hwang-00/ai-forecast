from modeling import create_model
from data import prepareData
from prediction import prediction
import pandas as pd
import numpy as np


class start_predict:

    def __init__(self, merged_df, store_code, product_name, train_date, predict_date, sequence_x=180 * 4, sequence_y=7):
        self.merged_df = merged_df
        self.store_code = store_code
        self.product_name = product_name
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


#'백산수2.0L', '백산수500ml', '신라면멀티', '안성탕면멀티', '진라면멀티(순한맛)'

    def predictor(self):

        weight = self.meta_index[(self.meta_index['store'] == self.store_code) & (
            self.meta_index['product'] == self.product_name)].iloc[0]['weight']

        # outlier = meta_index[(meta_index['store'] == store_code) & (
        #     meta_index['product'] == product_name)].iloc[0]['outlier']

        weight = './weight/' + weight

        prepareData1 = prepareData(merged_df=self.merged_df,
                                   product_name=self.product_name,
                                   store_code=self.store_code,
                                   train_date=self.train_date,
                                   predict_date=self.predict_date,
                                   sequence_x=self.sequence_x,
                                   sequence_y=self.sequence_y)

        df, df_train, df_test, sale_qty, x_columns, x_1_columns = prepareData1.sep_data2()

        x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1, x_columns, x_1_columns, sale_qty = prepareData1.scaled_origin()

        x_test_scaled, x_test_1_scaled, y_test_scaled = prepareData1.scaled_data(
            df_train=df_test)

        model = create_model(column_num_x, column_num_x_1,
                             self.sequence_x, self.sequence_y)

        np.nan_to_num(x_test_1_scaled, copy=False)

        print(x_test_scaled.shape, x_test_1_scaled.shape)

        next_week_sales = prediction(x_test_scaled[-2:, :, :], x_test_1_scaled[-2:, :, :],
                                     y_scaler, weight=weight, model=model)

        # print(next_week_sales)

        return next_week_sales
