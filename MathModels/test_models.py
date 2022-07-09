import MathModels.sk_models as m
import MathModels.sk_model_wrapper as model_wrapper
from Entities.result import Result
import Entities.Mappers.train_test_mapper as train_test
from sklearn.metrics import log_loss
from sklearn.metrics import f1_score

def test_models(game_list: list):
    x_train, y_train, x_test, y_test = train_test.get_train_test_data(game_list, 2021)
    x_pca_train, y_pca_train, x_pca_test, y_pca_test = train_test.get_pca_train_test_data(game_list, 2021)

    MathModelWrapper = model_wrapper.MathModel
    Models = m.MathModels()

    results = []
    # Run with dimensionality reduced
    for model in Models.models:
        result = Result()
        current_model = MathModelWrapper(x_pca_train, y_pca_train, x_pca_test, y_pca_test, model)
        current_model.train()
        current_model.predict_results()
        result.accuracy = current_model.get_accuracy()
        result.f_score = f1_score(y_test, current_model.math_model.predict(x_pca_test))
        result.log_loss = log_loss(y_test, current_model.math_model.predict_proba(x_pca_test))
        result.model = current_model
        results.append(result)

    return results
