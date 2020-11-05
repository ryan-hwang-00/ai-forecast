from modeling import create_model
import numpy as np
import data


df, df_train, df_test, sale_qty, x_columns, x_1_columns = data.sep_data()

(x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1,
 x_columns, x_1_columns, sale_qty) = data.scaled_origin()

x_test_scaled, x_test_1_scaled, y_test_scaled = data.scaled_data(
    df_train=df_test)


sequence_x = 180 * 4
sequence_y = 7
model = create_model(column_num_x, column_num_x_1, sequence_x, sequence_y)


def prediction(x_test_scaled, x_test_1_scaled, y_scaler,
               weight='1_bac2.hdf5', model=model):

    print('loading weights')

    # load weights

    callback_path = "./" + weight
    model.load_weights(callback_path)  # model_name + "1_bac2.hdf5")

    print('successed load weights')
    print('predicting...')

    y_test_predict = model.predict(
        x=(x_test_scaled, x_test_1_scaled))  # ,batch_size=1)

    y_test_predict = np.reshape(
        y_test_predict, (y_test_predict.shape[0], y_test_predict.shape[1]))

    print('successed prediction')

    print('inversing data')

    y_test_pre_in = y_scaler.inverse_transform(y_test_predict)

    print('successed inversion')

    # 데이터프레임으로 만들어줘야 할듯?? -> .to_json하려면
    # y_test_pre_in = pd.DataFrame(y_test_pre_in)

    return y_test_pre_in[-1]
