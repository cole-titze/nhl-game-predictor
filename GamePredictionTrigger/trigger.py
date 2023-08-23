import datetime
import logging
import MathModels.run_models as run_models

def test():
    run_models.find_and_store_best_model()

def start():
    run_models.predict_and_store_todays_games()

def tune():
    run_models.tune_models()
