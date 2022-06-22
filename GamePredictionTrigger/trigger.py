import datetime
import logging
import MathModels.run_models as run_models
import azure.functions as func

def start():
    accuracies = []
    for i in range(10):
        accuracy = run_models.test_models()
        accuracies.append(accuracy)
    print(max(accuracies))

    run_models.predict_and_store_todays_games()


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    start()
    