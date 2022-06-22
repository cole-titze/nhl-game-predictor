import numpy as np

def get_train_test_data(game_list: np.array, test_year: int):
    x_test = []
    y_test = []
    x_train = []
    y_train = []
    test = []
    train = []

    for game in game_list:
        if game.seasonStartYear == test_year:
            test.append(game)
        elif not game.isExcluded:
            train.append(game)

    for game in test:
        y_test.append(game.winner)
        x_test.append(game.map_data())
    for game in train:
        y_train.append(game.winner)
        x_train.append(game.map_data())
    return np.asarray(x_train), np.asarray(y_train), np.asarray(x_test), np.asarray(y_test)