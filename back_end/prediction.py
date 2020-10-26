import model


class prediction():

    def prediction():

        # load weights
        callback_path = "./1_bac2.hdf5"
        model.load_weights(callback_path)  # model_name + "weights.best.hdf5")

        y_train_predict = model.predict(
            x=(x_train_scaled, x_train_1_scaled))  # ,batch_size=1)

        y_train_predict = np.reshape(
            y_train_predict, (y_train_predict.shape[0], y_train_predict.shape[1]))

        y_train_pre_in = y_scaler.inverse_transform(y_train_predict)

        return y_train_pre_in
