from modeling import create_model
import numpy as np
import data

x_scaler, x_1_scaler, y_scaler, column_num_x, column_num_x_1, x_test_scaled, x_test_1_scaled, y_test_scaled = data.preprocessing_data

model = create_model


def prediction(x_train_scaled, x_train_1_scaled, y_scaler, weight='1_bac2.hdf5', model=model):

    # load weights
    callback_path = "./" + weight
    model.load_weights(callback_path)  # model_name + "1_bac2.hdf5")

    y_train_predict = model.predict(
        x=(x_train_scaled, x_train_1_scaled))  # ,batch_size=1)

    y_train_predict = np.reshape(
        y_train_predict, (y_train_predict.shape[0], y_train_predict.shape[1]))

    y_train_pre_in = y_scaler.inverse_transform(y_train_predict)

    return y_train_pre_in
