import data
# from prediction import prediction
import os
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, LSTM, Activation
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard, ReduceLROnPlateau
from tensorflow.keras.backend import square, mean
from keras import optimizers
from keras.wrappers.scikit_learn import KerasClassifier
from tensorflow import keras
from tensorflow.keras import layers

from future7_dataframe import date_info, row_select

from modeling import create_model


def trainer(store_code=1, product_name='백산수2.0L', predict_date='2020-01-07'):

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

    merged_df = date_info('2020-01-01', ['2', '4', '6', '7'], 0)

    model_name = meta_index[(meta_index['store'] == store_code) & (
        meta_index['product'] == product_name)].iloc[0]['weight']

    df, df_train, df_test, sale_qty, x_columns, x_1_columns = data.sep_data2(train='AI_Sale_ver4.0.csv', test=merged_df,
                                                                             product_name=product_name,
                                                                             store_code=store_code,
                                                                             train_date='2019-12-31',
                                                                             predict_date=predict_date)

    (x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1,
     x_columns, x_1_columns, sale_qty) = data.scaled_origin(sequence_x=180 * 4,
                                                            sequence_y=7,
                                                            product_name=product_name,
                                                            store_code=store_code)

    x_train_scaled, x_train_1_scaled, y_train_scaled = data.scaled_data(sequence_x=180 * 4,
                                                                        sequence_y=7,
                                                                        df_train=df_train,
                                                                        product_name=product_name,
                                                                        store_code=store_code
                                                                        )

    sequence_x = 180 * 4
    sequence_y = 7

    model = create_model(
        column_num_x, column_num_x_1, sequence_x, sequence_y)

    model.compile(
        optimizer=keras.optimizers.Adam(),
        loss=[
            keras.losses.Huber(),  # MeanSquaredError,Huber
        ], metrics=['mse'])

    filepath = './weight/' + model_name

    checkpoint_path = filepath

    checkpoint = ModelCheckpoint(checkpoint_path,
                                 monitor='val_loss',
                                 verbose=1,
                                 save_best_only=True,
                                 mode='min')

    earlystop = EarlyStopping(monitor='val_loss',
                              min_delta=0,
                              patience=30,
                              verbose=0,
                              mode='auto',
                              baseline=None,
                              restore_best_weights=False,)

    callbacks_list = [checkpoint, earlystop]

    model.fit(
        {"long": x_train_scaled, "short": x_train_1_scaled},
        {"prediction": y_train_scaled},
        epochs=2000, batch_size=32,
        callbacks=callbacks_list, validation_split=0.25, shuffle=False)

    return model


# trainer(store_code=6, product_name='백산수500ml', predict_date='2020-01-07')


# weight = meta_index[(meta_index['store'] == store_code) & (
#     meta_index['product'] == product_name)].iloc[0]['weight']

# df, df_train, df_test, sale_qty, x_columns, x_1_columns = data.sep_data(
#     datasets='AI_Sale_ver3.0.csv',
#     store_code=store_code,
#     product_name=product_name,
#     predict_date=predict_date
# )

# x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1, x_columns, x_1_columns, sale_qty = data.scaled_origin()

# x_test_scaled, x_test_1_scaled, y_test_scaled = data.scaled_data(
#     df_train=df_test)

# model = create_model(column_num_x, column_num_x_1, sequence_x, sequence_y)

# next_week_sales = prediction(x_test_scaled, x_test_1_scaled,
#                              y_scaler, weight=weight, model=model)

# print(next_week_sales)
