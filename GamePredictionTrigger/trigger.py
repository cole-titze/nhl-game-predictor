import datetime
import logging
import MathModels.run_models as run_models
import azure.functions as func

def test():
    run_models.find_and_store_best_model()

def start():
    run_models.predict_and_store_todays_games()


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    start()
    