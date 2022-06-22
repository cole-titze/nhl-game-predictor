import MathModels.sk_models as m
import MathModels.sk_model_wrapper as model_wrapper
import DataAccess.data_access as da
import Entities.Mappers.train_test_mapper as train_test
from sklearn.metrics import log_loss
from sklearn.metrics import f1_score

def test_models():
    game_list = da.get_cleaned_pregames()

    x_train, y_train, x_test, y_test = train_test.get_train_test_data(game_list, 2021)

    MathModelWrapper = model_wrapper.MathModel
    Models = m.MathModels()

    accuracies = []
    for model in Models.models:
        current_model = MathModelWrapper(x_train, y_train, x_test, y_test, model)
        current_model.train()
        current_model.predict_results()
        accuracies.append(current_model.get_accuracy())
        fscore = f1_score(y_test, current_model.math_model.predict(x_test))
        print("F1-Score: " + str(fscore))
        logloss = log_loss(y_test, current_model.math_model.predict_proba(x_test))
        print("Log-Loss: " + str(logloss))
    return max(accuracies)