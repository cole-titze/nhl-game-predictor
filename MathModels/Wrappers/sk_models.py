from itertools import product
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.ensemble import StackingClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB

class Model:
    def __init__(self, model_name, math_model, parameters):
        self.name = model_name
        self.model = math_model
        self.tune_parameters = parameters


class TestModels:
    def __init__(self):
        self.models = []

        mlp1 = MLPClassifier(activation="logistic", alpha=1e-6, hidden_layer_sizes=(15, 20, 110), max_iter=800, random_state=8, solver="adam")
        mlp2 = MLPClassifier(activation="logistic", alpha=1e-6, hidden_layer_sizes=(30, 60, 110, 150), max_iter=800, random_state=8, solver="adam")
        mlp3 = MLPClassifier(solver='adam', max_iter=600, activation='logistic', alpha=1e-5, hidden_layer_sizes=(40, 32, 16, 8))
        knn = KNeighborsClassifier(n_neighbors=355, p=1)

        stacking1 = StackingClassifier(estimators=[
            ("MLP", mlp1), ("knn", knn)], n_jobs=-1)
        voting1 = VotingClassifier(estimators=[
            ("MLP", mlp1), ("knn", knn)], n_jobs=-1, voting="soft")

        self.models.append(Model("MLP 1", mlp1, {}))
        #self.models.append(Model("MLP 2", mlp2, {}))
        #self.models.append(Model("MLP 3", mlp3, {}))
        #self.models.append(Model("KNN", knn, {}))
        #self.models.append(Model("Stacking 1", stacking1, {}))
        #self.models.append(Model("Voting 1", voting1, {}))


class TuneModels:
    def __init__(self):
        self.models = []
        # KNN
        knn = KNeighborsClassifier()
        knn_parameters = {
            'weights': ['uniform', 'distance'],
            'n_neighbors': np.arange(5, 200, 10),
            'p': [1, 2, 3]
        }

        # MLP
        first_layer_neurons = np.arange(5, 50, 5)
        second_layer_neurons = np.arange(10, 100, 10)
        third_layer_neurons = [110]
        fourth_layer_neurons = np.arange(10, 200, 10)

        small_hidden_layer_sizes = list(first_layer_neurons) + list(product(first_layer_neurons, second_layer_neurons))
        large_hidden_layer_sizes = list(
            product(first_layer_neurons, second_layer_neurons, third_layer_neurons, fourth_layer_neurons))
        mlp = MLPClassifier()
        mlp_parameters = {
            'solver': ['adam'],
            'max_iter': [800],
            'alpha': [.000001],
            'hidden_layer_sizes': large_hidden_layer_sizes,
            'random_state': [0, 8],
            'activation': ["logistic"]
        }

        # RF
        rf = RandomForestClassifier()
        svm_clf = svm.SVC(probability=True)
        nb = GaussianNB()

        self.models.append(Model("MLP", mlp, mlp_parameters))
        #self.models.append(Model("KNN", knn, knn_parameters))
        #self.models.append(Model("SVM", svm_clf, {}))
        #self.models.append(Model("RF", rf, {}))
        #self.models.append(Model("NB", nb, {}))
