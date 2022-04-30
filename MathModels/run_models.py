import MathModels.math_models as m
import MathModels.sk_math_model_wrapper as model_wrapper
import DataAccess.data_access as da
from nhlstats import list_games

def test_models():
    gameList = da.get_cleaned_pregames()

    x_train, y_train, x_test, y_test = da.get_train_test_data(gameList, 2021)

    MathModelWrapper = model_wrapper.MathModel
    Models = m.MathModels()

    for model in Models.models:
        current_model = MathModelWrapper(x_train, y_train, x_test, y_test, model)
        current_model.train()
        current_model.predict_results()
        current_model.print_model_result()

def run_models(single_game):
    gameList = da.get_cleaned_pregames()

    # Use all data to train instead of just some
    x_train, y_train, x_test, y_test = da.get_train_test_data(gameList, 0)

    MathModelWrapper = model_wrapper.MathModel
    Models = m.MathModels()

    for model in Models.models:
        current_model = MathModelWrapper(x_train, y_train, x_test, y_test, model)
        current_model.train()
        current_model.predict_single_game(test_game)
        current_model.print_single_game_odds()

def predict_todays_games():
    for game in list_games():
        home_team = game['home_team']
        away_team = game['away_team']
        print("Running Prediction")
        #single_game = 
        #test_models(single_game)