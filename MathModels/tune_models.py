from itertools import product
import numpy as np
from sklearn.model_selection import GridSearchCV
import Entities.Mappers.train_test_mapper as train_test
import DataAccess.data_access as da
import MathModels.sk_models as m
import pandas as pd

number_of_simulations = 1
chi_dimensions = 24
dimensions = 12
start_year = 2011

def tune_models():
    # Get Data
    test_year = 2021
    game_list = da.get_cleaned_pregames(start_year)
    x_train, y_train, x_test, y_test, _ = train_test.get_pca_train_test_data(game_list, test_year, chi_dimensions, dimensions)

    first_layer_neurons = np.arange(10, 200, 10)
    second_layer_neurons = np.arange(10, 200, 10)
    third_layer_neurons = np.arange(10, 200, 10)
    #hidden_layer_sizes = list(first_layer_neurons) + list(product(first_layer_neurons, second_layer_neurons)) + list(product(first_layer_neurons, second_layer_neurons, third_layer_neurons))
    hidden_layer_sizes = list(product(first_layer_neurons, second_layer_neurons, third_layer_neurons))
    parameters = {
                    'solver': ['adam','lbfgs','sgd'],
                    'max_iter': [800, 1000, 1200, 1400, 1600, 1800, 2000],
                    'alpha': 10.0 ** -np.arange(1, 6),
                    'hidden_layer_sizes': hidden_layer_sizes,
                    'random_state': [0, 2, 4, 6, 8],
                    'activation': ["logistic", "relu", "tanh"]
                  }

    Models = m.MathModels()
    for model in Models.models:
        math_model = model.model
        model_name = model.name[0]
        print("Model: " + model_name)
        clf = GridSearchCV(math_model, parameters, n_jobs=-1, verbose=2)
        clf.fit(x_train, y_train)
        print(clf.score(x_train, y_train))
        print(clf.best_params_)
        df = pd.DataFrame(clf.cv_results_)
        df.to_csv(model_name + '.csv')

