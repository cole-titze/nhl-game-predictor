import MathModels.run_models as run_models
import MathModels.tune_models as tune_models

def test():
    run_models.find_and_store_best_model()

def start():
    run_models.predict_and_store_todays_games()

def tune():
    tune_models.tune_models()
