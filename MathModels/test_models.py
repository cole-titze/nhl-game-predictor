import MathModels.sk_models as m
import MathModels.sk_model_wrapper as model_wrapper
from Entities.result import Result
from sklearn.metrics import log_loss
from sklearn.metrics import f1_score

def test_models(x_train, y_train, x_test, y_test):
    MathModelWrapper = model_wrapper.MathModel
    Models = m.MathModels()

    results = []
    # Run with dimensionality reduced
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
