import os
import tensorflow as tf
import pandas as pd
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, LSTM, Activation
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard, ReduceLROnPlateau
from tensorflow.keras.backend import square, mean
from keras import optimizers
from keras.wrappers.scikit_learn import KerasClassifier
from tensorflow import keras
from tensorflow.keras import layers


def create_model(column_num_x, column_num_x_1, sequence_x, sequence_y):

    sequence_x = 180 * 4
    sequence_y = 7

    lstm_dim = 16
    dence_dim = 4

    model = keras.models.Sequential()

    long_input = keras.Input(shape=(sequence_x, column_num_x), name="long")

    short_input = keras.Input(
        shape=(sequence_y, column_num_x_1), name="short")

    encoder = tf.keras.layers.LSTM(
        lstm_dim, return_state=True, dropout=0.4)

    encoder_outputs, state_h, state_c = encoder(long_input)

    decoder_lstm = tf.keras.layers.LSTM(
        lstm_dim, return_sequences=True, dropout=0.4)

    x = decoder_lstm(short_input, initial_state=[state_h, state_c])

    x = tf.keras.layers.Dense(dence_dim, activation='relu')(x)

    x = tf.keras.layers.Dense(dence_dim, activation='relu')(x)

    output = tf.keras.layers.Dense(
        1, activation='relu', name='prediction')(x)

    model = keras.Model(
        inputs=[long_input, short_input],
        outputs=[output],)

    return model
