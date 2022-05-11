import MathModels.sk_models as m
import MathModels.sk_model_wrapper as model_wrapper
import DataAccess.data_access as da

def test_models():
    gameList = da.get_cleaned_pregames()

    x_train, y_train, x_test, y_test = da.get_train_test_data(gameList, 2021)

    MathModelWrapper = model_wrapper.MathModel
    Models = m.MathModels()

    accuracies = []
    for model in Models.models:
        current_model = MathModelWrapper(x_train, y_train, x_test, y_test, model)
        current_model.train()
        current_model.predict_results()
        #current_model.print_model_result()
        accuracies.append(current_model.get_accuracy())
    return max(accuracies)

def run_models(test_game):
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
    print("Running Prediction")
    future_games = da.get_future_games()
    for single_game in future_games:
        print(single_game.homeTeamName + "     " + single_game.awayTeamName)
        run_models([single_game.map_data()])