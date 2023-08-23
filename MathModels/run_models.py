from datetime import datetime
from itertools import product
import numpy as np
from sklearn.model_selection import GridSearchCV
import MathModels.pickle_skmodel as model_loader
import Entities.Mappers.train_test_mapper as train_test
import MathModels.pickle_skmodel as model_saver
import MathModels.test_models as test_models
import DataAccess.data_access as da
import MathModels.sk_models as m
import pandas as pd

number_of_simulations = 1
chi_dimensions = 24
dimensions = 12
start_year = 2011

def get_season_start_year():
    end_season_date_str = str(datetime.utcnow().year) + "-08-01"
    current_date = datetime.utcnow()
    end_season_date = datetime.strptime(end_season_date_str, "%Y-%m-%d")

    if current_date > end_season_date:
        last_season_year = current_date.year
    else:
        last_season_year = current_date.year - 1
    return last_season_year

def predict_and_store_todays_games():
    print("Running Prediction")
    season_start_year = get_season_start_year()
    game_list = da.get_cleaned_pregames(start_year)
    x_train, y_train, x_test, y_test, predict_ids = train_test.get_pca_train_test_data(game_list, season_start_year, chi_dimensions, dimensions)
    print("Games to predict: " + str(len(x_test)))

    model = model_loader.load_model()
    for index, single_game in enumerate(x_test):
        model.predict_single_game([single_game])
        prediction = model.odds[0]
        home_prob = prediction[0]
        away_prob = prediction[1]
        da.store_probabilities(predict_ids[index], home_prob, away_prob)
        #model.partial_fit([single_game], [y_test[index]])
    print("Finished Processing")

# runtime = number_of_simulations * number_of_models_in_wrapper
# 5 * 4 = 20 loops
def find_and_store_best_model():
    # Get Data
    test_year = get_season_start_year()
    game_list = da.get_cleaned_pregames(start_year)
    x_train, y_train, x_test, y_test, _ = train_test.get_pca_train_test_data(game_list, test_year, chi_dimensions, dimensions)

    estimators = []
    best_results = None
    print("Number of Simulations: " + str(number_of_simulations))
    print("Number of Games to train on: " + str(len(x_train)))
    print("Number of Games to test on: " + str(len(x_test)))
    for i in range(number_of_simulations):
        print("Running Simulation " + str(i + 1))
        results = test_models.test_models(x_train, y_train, x_test, y_test)
        if best_results is None:
            best_results = results
        for j, result in enumerate(results):
            if result.log_loss < best_results[j].log_loss:
                best_results[j] = result

    # Find best model and print all models
    best_model = best_results[0]
    print("Dimensionality Reduction Input Data:")
    for index, best_result in enumerate(best_results):
        if best_result.log_loss < best_model.log_loss:
            best_model = best_result
        # Create list of trained models
        estimators.append(best_result.model)
        best_result.print()
    best_model = best_model.model

    print("Determine Best Model and save with pickle...")
    model_saver.save_model(best_model)

def tune_models():
    # Get Data
    test_year = 2021
    game_list = da.get_cleaned_pregames(start_year)
    x_train, y_train, x_test, y_test, _ = train_test.get_pca_train_test_data(game_list, test_year, chi_dimensions, dimensions)

    first_layer_neurons = np.arange(10, 200, 10)
    second_layer_neurons = np.arange(10, 200, 10)
    third_layer_neurons = np.arange(10, 200, 10)
    hidden_layer_sizes = list(first_layer_neurons) + list(product(first_layer_neurons, second_layer_neurons)) + list(product(first_layer_neurons, second_layer_neurons, third_layer_neurons))

    parameters = {
                    'solver': ['adam','lbfgs','sgd'],
                    'max_iter': [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],
                    'alpha': 10.0 ** -np.arange(1, 10),
                    'hidden_layer_sizes': hidden_layer_sizes,
                    'random_state': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
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

