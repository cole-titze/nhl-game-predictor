from sklearn.model_selection import RandomizedSearchCV
import Entities.Mappers.train_test_mapper as train_test
import DataAccess.data_access as da
import MathModels.Wrappers.sk_models as m
import pandas as pd

number_of_simulations = 1
chi_dimensions = 24
dimensions = 12
start_year = 2011
test_year = 2021

def tune_models():
    # Get Data
    best_params = []
    game_list = da.get_cleaned_pregames(start_year)
    x_train, y_train, x_test, y_test, _ = train_test.get_pca_train_test_data(game_list, test_year, chi_dimensions, dimensions)

    Models = m.TuneModels()
    for model in Models.models:
        math_model = model.model
        model_name = model.name
        parameters = model.tune_parameters
        print("Model: " + model_name)
        clf = RandomizedSearchCV(math_model, parameters, n_jobs=-1, verbose=10)
        clf.fit(x_train, y_train)
        print(clf.score(x_train, y_train))
        print(clf.best_params_)
        best_params.append(clf.best_params_)

        df = pd.DataFrame(clf.cv_results_)
        df.to_csv('./ModelReports/' + model_name + '.csv')

    with open('./ModelReports/BestParams.txt', 'w') as outfile:
        outfile.write('\n'.join(str(params) for params in best_params))

