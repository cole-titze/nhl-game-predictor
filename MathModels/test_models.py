import MathModels.sk_models as m
import MathModels.sk_model_wrapper as model_wrapper
from Entities.result import Result
import Entities.Mappers.train_test_mapper as train_test
from sklearn.metrics import log_loss
from sklearn.metrics import f1_score

def test_models(game_list: list):
    x_train, y_train, x_test, y_test = train_test.get_train_test_data(game_list, 2021)

    MathModelWrapper = model_wrapper.MathModel
    Models = m.MathModels()

    results = []
    for model in Models.models:
        result = Result()
        current_model = MathModelWrapper(x_train, y_train, x_test, y_test, model)
        current_model.train()
        current_model.predict_results()
        result.accuracy = current_model.get_accuracy()
        result.f_score = f1_score(y_test, current_model.math_model.predict(x_test))
        result.log_loss = log_loss(y_test, current_model.math_model.predict_proba(x_test))
        result.model = current_model
        results.append(result)

    return results
