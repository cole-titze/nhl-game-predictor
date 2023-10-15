from datetime import datetime
import MathModels.pickle_skmodel as model_loader
import Entities.Mappers.train_test_mapper as train_test
import DataAccess.data_access as da

chi_dimensions = 24
dimensions = 12

def get_season_start_year():
    end_season_date_str = str(datetime.utcnow().year) + "-08-01"
    current_date = datetime.utcnow()
    end_season_date = datetime.strptime(end_season_date_str, "%Y-%m-%d")

    if current_date > end_season_date:
        last_season_year = current_date.year
    else:
        last_season_year = current_date.year - 1
    return last_season_year


def predict_and_store_unplayed_games():
    print("Running Prediction")
    season_start_year = get_season_start_year()
    game_list = da.get_training_and_unplayed_cleaned_pregames(season_start_year)
    x_train, y_train, x_test, y_test, predict_ids = train_test.get_pca_train_test_data(game_list, season_start_year,
                                                                                       chi_dimensions, dimensions)
    print("Games to predict: " + str(len(x_test)))

    model = model_loader.load_model()
    for index, single_game in enumerate(x_test):
        model.predict_single_game([single_game])
        prediction = model.odds[0]
        home_prob = prediction[0]
        away_prob = prediction[1]
        da.store_probabilities(predict_ids[index], home_prob, away_prob)
        # model.partial_fit([single_game], [y_test[index]])
    print("Finished Processing")


def predict_all_games():
    print("Running Prediction")
    start_year = 2011
    season_start_year = 2021
    game_list = da.get_cleaned_pregames(start_year)
    x_train, y_train, x_test, y_test, predict_ids = train_test.get_pca_train_test_data(game_list, season_start_year,
                                                                                       chi_dimensions, dimensions)
    print("Games to predict: " + str(len(x_test)))

    model = model_loader.load_model()
    for index, single_game in enumerate(x_test):
        model.predict_single_game([single_game])
        prediction = model.odds[0]
        home_prob = prediction[0]
        away_prob = prediction[1]
        da.store_probabilities(predict_ids[index], home_prob, away_prob)
        # model.partial_fit([single_game], [y_test[index]])
    print("Finished Processing")