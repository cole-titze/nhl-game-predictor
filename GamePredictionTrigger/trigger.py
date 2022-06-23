import datetime
import logging
import MathModels.run_models as run_models
import MathModels.test_models as test_models
import DataAccess.data_access as da
import azure.functions as func

number_of_simulations = 50

# runtime = number_of_simulations * number_of_models_in_wrapper
# 5 * 4 = 20 loops
def start():
    game_list = da.get_cleaned_pregames()

    best_results = None
    for _ in range(number_of_simulations):
        results = test_models.test_models(game_list)
        if best_results is None:
            best_results = results
        for i, result in enumerate(results):
            if result.log_loss < best_results[i].log_loss:
                best_results[i] = result
    for best_result in best_results:
        best_result.print()

    #run_models.predict_and_store_todays_games()


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    start()
    