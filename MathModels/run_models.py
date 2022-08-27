import MathModels.sk_models as m
import MathModels.sk_model_wrapper as model_wrapper
from datetime import datetime
import MathModels.pickle_skmodel as model_loader
import Entities.Mappers.train_test_mapper as train_test
import MathModels.pickle_skmodel as model_saver
import MathModels.test_models as test_models
import DataAccess.data_access as da

number_of_simulations = 1000
chi_dimensions = 42
dimensions = 12
start_year = 2011

def run_models(test_game):
    game_list = da.get_cleaned_pregames(2011)

    # Use all data to train instead of just some
    x_train, y_train, x_test, y_test = train_test.get_train_test_data(game_list, 0)

    MathModelWrapper = model_wrapper.MathModel
    Models = m.MathModels()

    prediction = []
    for model in Models.models:
        current_model = MathModelWrapper(x_train, y_train, x_test, y_test, model)
        current_model.train()
        current_model.predict_single_game(test_game)
        prediction = current_model.odds[0]
    return prediction

def get_model():
    game_list = da.get_cleaned_pregames(2011)

    # Use all data to train instead of just some
    x_train, y_train, x_test, y_test = train_test.get_train_test_data(game_list, 0)

    MathModelWrapper = model_wrapper.MathModel
    model = m.MathModels().models[0]

    current_model = MathModelWrapper(x_train, y_train, x_test, y_test, model)
    current_model.train()
    return current_model

def get_last_year():
    end_season_date_str = str(datetime.utcnow().year) + "-08-01"
    current_date = datetime.utcnow()
    end_season_date = datetime.strptime(end_season_date_str, "%Y-%m-%d")

    if current_date > end_season_date:
        last_season_year = current_date.year - 1
    else:
        last_season_year = current_date.year - 2
    return last_season_year

def predict_and_store_todays_games():
    print("Running Prediction")
    last_year = get_last_year()
    game_list = da.get_cleaned_pregames(2011)
    x_train, y_train, x_test, y_test, predict_ids = train_test.get_pca_train_test_data(game_list, 2021, chi_dimensions, dimensions)

    model = model_loader.load()
    for index, single_game in enumerate(x_test):
        model.predict_single_game([single_game])
        prediction = model.odds[0]
        home_prob = prediction[0]
        away_prob = prediction[1]
        da.store_probabilities(predict_ids[index], home_prob, away_prob)

# runtime = number_of_simulations * number_of_models_in_wrapper
# 5 * 4 = 20 loops
def find_and_store_best_model():
    # Get Data
    game_list = da.get_cleaned_pregames(start_year)
    x_train, y_train, x_test, y_test, _ = train_test.get_pca_train_test_data(game_list, 2021, chi_dimensions, dimensions)

    estimators = []
    best_results = None
    for _ in range(number_of_simulations):
        results = test_models.test_models(x_train, y_train, x_test, y_test)
        if best_results is None:
            best_results = results
        for i, result in enumerate(results):
            if result.log_loss < best_results[i].log_loss:
                best_results[i] = result

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
    model_saver.save(best_model)