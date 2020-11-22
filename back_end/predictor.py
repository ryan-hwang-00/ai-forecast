from modeling import create_model
from data import prepareData
from prediction import prediction
import pandas as pd
import numpy as np
from future7_dataframe import date_info


sequence_x = 180 * 4
sequence_y = 7
#'백산수2.0L', '백산수500ml', '신라면멀티', '안성탕면멀티', '진라면멀티(순한맛)'


def predictor(merged_df, store_code=6, product_name='백산수500ml', predict_date='2020-01-07'):

    meta_index = pd.DataFrame(
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

    weight = meta_index[(meta_index['store'] == store_code) & (
        meta_index['product'] == product_name)].iloc[0]['weight']

    # outlier = meta_index[(meta_index['store'] == store_code) & (
    #     meta_index['product'] == product_name)].iloc[0]['outlier']

    weight = './weight/' + weight

    df, df_train, df_test, sale_qty, x_columns, x_1_columns = prepareData(merged_df=merged_df).sep_data2(train='AI_Sale_ver4.0.csv',
                                                                                                         product_name=product_name,
                                                                                                         store_code=store_code,
                                                                                                         train_date='2019-12-31',
                                                                                                         predict_date=predict_date
                                                                                                         )

    x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1, x_columns, x_1_columns, sale_qty = prepareData(merged_df=merged_df).scaled_origin(sequence_x=180 * 4,
                                                                                                                                                    sequence_y=7,
                                                                                                                                                    product_name=product_name,
                                                                                                                                                    store_code=store_code)

    x_test_scaled, x_test_1_scaled, y_test_scaled = prepareData(merged_df=merged_df).scaled_data(sequence_x=180 * 4,
                                                                                                 sequence_y=7,
                                                                                                 df_train=df_test,
                                                                                                 product_name=product_name,
                                                                                                 store_code=store_code
                                                                                                 )

    model = create_model(column_num_x, column_num_x_1, sequence_x, sequence_y)

    np.nan_to_num(x_test_1_scaled, copy=False)

    next_week_sales = prediction(x_test_scaled, x_test_1_scaled,
                                 y_scaler, weight=weight, model=model)

    # print(next_week_sales)

    return next_week_sales
