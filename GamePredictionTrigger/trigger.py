import MathModels.run_models as run_models
import MathModels.tune_models as tune_models
import MathModels.test_models as test_models

def test():
    test_models.find_and_store_best_model()

def start():
    run_models.predict_and_store_unplayed_games()

def predict_all_games():
    run_models.predict_all_games()

def tune():
    tune_models.tune_models()
