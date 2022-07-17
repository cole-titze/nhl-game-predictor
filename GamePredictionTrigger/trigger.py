import datetime
import logging
import MathModels.run_models as run_models
import MathModels.test_models as test_models
import DataAccess.data_access as da
import azure.functions as func
import Entities.Mappers.train_test_mapper as train_test

number_of_simulations = 1
dimensions = 8
start_year = 2014

# runtime = number_of_simulations * number_of_models_in_wrapper
# 5 * 4 = 20 loops
def test():
    for team_id in range(60):
        estimators = []
        best_results = None
        game_list = da.get_cleaned_pregames_by_team_id(start_year, team_id)
        if not game_list:
            continue
        x_train, y_train, x_test, y_test = train_test.get_pca_train_test_data(game_list, 2021, dimensions)
        if x_train == [] or y_test == []:
            continue
        for _ in range(number_of_simulations):
            results = test_models.test_models(x_train, y_train, x_test, y_test)
            if best_results is None:
                best_results = results
            for i, result in enumerate(results):
                if result.log_loss < best_results[i].log_loss:
                    best_results[i] = result

        print("Dimensionality Reduction Input Data:" + str(team_id))
        for index, best_result in enumerate(best_results):
            # Create list of trained models
            estimators.append(best_result.model)
            best_result.print()


def start():
    run_models.predict_and_store_todays_games()


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    start()
    