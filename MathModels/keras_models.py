import keras
from keras.metrics import BinaryAccuracy
from keras.losses import BinaryCrossentropy
from keras.models import Sequential
from keras.layers import Dense

class Model:
    name = None
    model = None

    def __init__(self, Name: str, model):
        self.name = Name
        self.model = model


class MathModels:
    def __init__(self):
        self.models = []
        inputs = keras.Input(shape=(34, 1))
        seq = Sequential()
        #seq.add(Convolution1D(16, 1, 1, activation='sigmoid', input_shape=(34, 1)))
        #seq.add(Flatten(input_shape=(34, 1)))
        seq.add(Dense(40, activation='sigmoid'))
        seq.add(Dense(1, activation='sigmoid'))
        seq.compile(loss=BinaryCrossentropy(), optimizer='adam', metrics=[BinaryAccuracy()])

        self.models.append(Model("cnn", seq))
