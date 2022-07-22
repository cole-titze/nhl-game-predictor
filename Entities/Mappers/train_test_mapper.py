import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

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


def get_pca_train_test_data(game_list: np.array, year: int, chi_dimensions: int, dimensions: int):
    x_train, y_train, x_test, y_test = get_train_test_data(game_list, year)

    # standarize data
    sc = StandardScaler().fit(x_train)
    x_train = sc.transform(x_train)
    x_test = sc.transform(x_test)
    # Normalize data
    norm = MinMaxScaler(feature_range=(0, 12)).fit(x_train)
    x_train_norm = norm.transform(x_train)
    x_test_norm = norm.transform(x_test)
    # Select features
    feature_selector = SelectKBest(chi2, k=chi_dimensions).fit(x_train_norm, y_train)
    x_train = feature_selector.transform(x_train)
    x_test = feature_selector.transform(x_test)

    # PCA input data (reduce dimensionality)
    pca = PCA(n_components=dimensions)
    x_train = pca.fit_transform(x_train)
    x_test = pca.transform(x_test)

    return x_train, y_train, x_test, y_test