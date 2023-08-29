import MathModels.Wrappers.sk_models as m
import MathModels.Wrappers.sk_model_wrapper as model_wrapper
from Entities.result import Result
from sklearn.metrics import log_loss
from sklearn.metrics import f1_score
import MathModels.pickle_skmodel as model_saver
import Entities.Mappers.train_test_mapper as train_test
import DataAccess.data_access as da

number_of_simulations = 1
chi_dimensions = 24
dimensions = 12
start_year = 2011
test_year = 2021

def find_and_store_best_model():
    # Get Data
    game_list = da.get_cleaned_pregames(start_year)
    x_train, y_train, x_test, y_test, _ = train_test.get_pca_train_test_data(game_list, test_year, chi_dimensions, dimensions)

    estimators = []
    best_results = None
    print("Number of Simulations: " + str(number_of_simulations))
    print("Number of Games to train on: " + str(len(x_train)))
    print("Number of Games to test on: " + str(len(x_test)))
    for i in range(number_of_simulations):
        print("Running Simulation " + str(i + 1))
        results = test_models(x_train, y_train, x_test, y_test)
        if best_results is None:
            best_results = results
        for j, result in enumerate(results):
            if result.log_loss < best_results[j].log_loss:
                best_results[j] = result

    # Find best model and print all models
    best_model = best_results[0]
    print("Dimensionality Reduction Input Data:")
    for index, best_result in enumerate(best_results):
        if best_result.log_loss < best_model.log_loss:
            best_model = best_result
        # Create list of trained models
        estimators.append(best_result.model)
        best_result.print()
    best_model = best_model.model

    print("Determine Best Model and save with pickle...")
    model_saver.save_model(best_model)

def test_models(x_train, y_train, x_test, y_test):
    MathModelWrapper = model_wrapper.MathModel
    Models = m.TestModels()

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
