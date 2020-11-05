from modeling import create_model
import data
from prediction import prediction
import pandas as pd


sequence_x = 180 * 4
sequence_y = 7
#'백산수2.0L', '백산수500ml', '신라면멀티', '안성탕면멀티', '진라면멀티(순한맛)'


def predictor(store_code=6, product_name='백산수500ml', predict_date='2019-12-31'):

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

    weight = meta_index[(meta_index['store'] == store_code) & (
        meta_index['product'] == product_name)].iloc[0]['weight']

    df, df_train, df_test, sale_qty, x_columns, x_1_columns = data.sep_data(
        datasets='AI_Sale_ver3.0.csv',
        store_code=store_code,
        product_name=product_name,
        predict_date=predict_date
    )

    x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1, x_columns, x_1_columns, sale_qty = data.scaled_origin()

    x_test_scaled, x_test_1_scaled, y_test_scaled = data.scaled_data(
        df_train=df_test)

    model = create_model(column_num_x, column_num_x_1, sequence_x, sequence_y)

    next_week_sales = prediction(x_test_scaled, x_test_1_scaled,
                                 y_scaler, weight=weight, model=model)

    # print(next_week_sales)

    return next_week_sales


print(predictor())
