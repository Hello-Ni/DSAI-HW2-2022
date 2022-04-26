import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout, BatchNormalization
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import regularizers
from trade import Trading

# We choose the fourth feature(close value) as training data
features = 3
scope = 15  # 15 day predict next day
scaler = MinMaxScaler(feature_range=(0, 1))


def LSTM_Model(X_train, y_train):
    keras.backend.clear_session()
    model = Sequential()

    model.add(LSTM(units=16,
                   batch_input_shape=(1, X_train.shape[1], 1),
                   stateful=True
                   ))

    # model.add(Dense(units = 1,activation='sigmoid'))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=20, batch_size=1)
    # model.fit(X_train, y_train, epochs = 10, batch_size = 1)

    return model


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                        default='training.csv',
                        help='input training data file name')
    parser.add_argument('--testing',
                        default='testing.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()

    X_train, y_train, X_test, y_test = preprocessing(
        args.training, args.testing)
    # predicte
    predicted_price = LSTM_Model(
        X_train, y_train).predict(X_test, batch_size=1)
    predicted_price = scaler.inverse_transform(predicted_price)

    Tr = Trading(hold=0, stock=0, last_day=0)
    action = Tr.act(predicted_price)

    test_data = pd.read_csv(args.testing, header=None)
    test_open_data = test_data.iloc[:, 0]
    # use close to predict next day open
    plt.plot(predicted_price, color='red', label='predict')
    plt.plot(test_open_data, color='blue', label='ans')  # open
    plt.legend()
    plt.show()

    with open(args.output, 'w') as output_file:
        for i in range(len(action)):
            output_file.writelines(str(action[i])+"\n")
