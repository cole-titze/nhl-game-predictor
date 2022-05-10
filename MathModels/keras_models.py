from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution1D, MaxPooling2D


class Model:
    name = None
    model = None

    def __init__(self, Name: str, model):
        self.name = Name
        self.model = model


class MathModels:
    def __init__(self):
        self.models = []
        seq = Sequential()
        #seq.add(Convolution1D(16, 1, 1, activation='sigmoid', input_shape=(34, 1)))
        #seq.add(Flatten(input_shape=(34, 1)))
        seq.add(Dense(34, activation='relu'))
        seq.add(Dense(1, activation='sigmoid'))
        seq.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        self.models.append(Model("cnn", seq))
