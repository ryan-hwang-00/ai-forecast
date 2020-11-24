
import numpy as np
from tensorflow import keras
import tensorflow as tf


def prediction(x_test_scaled, x_test_1_scaled, y_scaler,
               weight='1_bac2.hdf5', model=keras.Model):

    print('loading weights')

    # load weights

    callback_path = "./" + weight
    model.load_weights(callback_path)  # model_name + "1_bac2.hdf5")

    print('successed load weights')
    print('predicting...')

    tf.function(experimental_relax_shapes=True)

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
